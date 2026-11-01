#!/usr/bin/env python3
"""Build a print-ready PDF of the Simplified Chinese edition (`Chinese translation/`).

Pipeline
  1. Render every Mermaid block of each Chinese chapter to PNG with mermaid-cli (mmdc).
  2. Convert each chapter's Markdown to HTML (python-markdown: tables, footnotes, md_in_html…),
     namespacing footnote ids per chapter, expanding <details> flashcards, pointing images at
     absolute file paths and turning cross-chapter links into in-book anchors.
  3. Assemble one HTML book: cover → notes → contents → Part dividers → chapters → glossary.
  4. Render with Chromium (scripts/zh_pdf_render.js) twice: pass 1 finds the page where each
     chapter starts (hidden markers), pass 2 prints those page numbers in the contents.

Usage:
  python3 scripts/zh_build_pdf.py --fonts /path/to/node_modules/@fontsource --out out.pdf
Requirements: mmdc, node + playwright (Chromium), python packages markdown, pypdf.
"""
from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import markdown
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent.parent
ZH = ROOT / "Chinese translation"
PARTS = [
    ("00-start-here", "第 0 部分 · 从这里开始"),
    ("01-data-systems-foundations", "第 1 部分 · 数据系统基础"),
    ("02-pipelines-and-governance", "第 2 部分 · 数据管道、数据流动与治理"),
    ("03-ai-data-stack", "第 3 部分 · AI 数据技术栈"),
    ("04-company-deep-dives", "第 4 部分 · 公司深度研究"),
    ("05-business-and-economics", "第 5 部分 · 商业模式与经济学"),
    ("06-history-and-future", "第 6 部分 · 历史与未来"),
    ("07-conversation-toolkit", "第 7 部分 · 对话工具箱"),
]
LINK = re.compile(r"(!?)\[([^\]]*)\]\(([^)\s]+)\)")


def chapter_key(path: Path) -> str:
    if path.name == "glossary.md":
        return "glossary"
    if path.name == "index.md":
        return "preface"
    return re.match(r"(ch[\d-]+)", path.name).group(1).rstrip("-")


def render_mermaid(src: Path, build: Path, cfg: Path, mcfg: Path) -> Path:
    out = build / f"{chapter_key(src)}.md"
    if "```mermaid" not in src.read_text(encoding="utf-8"):
        shutil.copy(src, out)
        return out
    r = subprocess.run(["mmdc", "-q", "-p", str(cfg), "-c", str(mcfg), "-i", str(src), "-o", str(out),
                        "-e", "png", "-s", "2.2", "-b", "white"],
                       capture_output=True, text=True)
    if r.returncode != 0 or not out.exists():
        print(f"  mmdc failed for {src.name}; keeping Mermaid as code: {r.stderr[:200]}")
        shutil.copy(src, out)
    return out


def preprocess(text: str, key: str, built: Path, src: Path) -> str:
    en_src = ROOT / src.relative_to(ZH)
    # namespace footnote ids
    text = re.sub(r"\[\^([^\]]+)\]", lambda m: f"[^{key}-{m.group(1)}]", text)

    def fix(m: re.Match) -> str:
        bang, label, target = m.groups()
        if re.match(r"^(https?:|mailto:)", target):
            return m.group(0)
        path, _, anchor = target.partition("#")
        if bang:  # image → absolute path
            for base in (built.parent, src.parent, en_src.parent):
                p = (base / path).resolve()
                if p.exists():
                    return f"![{label}]({p.as_uri()})"
            return f"*[图：{label}]*"
        if not path:
            return f"[{label}](#{key}--{anchor})" if anchor else label
        name = Path(path).name
        if name == "glossary.md":
            return f"[{label}](#glossary--{anchor})" if anchor else f"[{label}](#chap-glossary)"
        m2 = re.match(r"(ch[\d-]+)", name)
        if m2 and name.endswith(".md"):
            ck = m2.group(1).rstrip("-")
            return f"[{label}](#{ck}--{anchor})" if anchor else f"[{label}](#chap-{ck})"
        return label  # links to repo files (csv, scripts) become plain text in print

    return LINK.sub(fix, text)


def to_html(text: str, key: str) -> tuple[str, str]:
    md = markdown.Markdown(extensions=["extra", "sane_lists", "toc"],
                           extension_configs={"toc": {"slugify": lambda v, s: v}})
    body = md.convert(text)
    # namespace explicit anchors and heading ids so cross-chapter links resolve
    body = re.sub(r'<a id="([^"]+)"></a>', lambda m: f'<a id="{key}--{m.group(1)}"></a>', body)
    body = re.sub(r'<(h[1-6]) id="[^"]*"', r"<\1", body)
    body = body.replace("<details", "<details open")
    m = re.search(r"<h1>(.*?)</h1>", body, flags=re.S)
    title = re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else key
    return body, title


CSS = """
@page { size: A4; }
html { font-size: 10.2pt; }
body { font-family: 'Noto Serif SC', 'WenQuanYi Zen Hei', serif; line-height: 1.72; color: #1a1a1a;
       text-align: justify; -webkit-font-smoothing: antialiased; }
h1, h2, h3, h4, .toc, .part, .cover, th, figcaption, .meta { font-family: 'Noto Sans SC', 'WenQuanYi Zen Hei', sans-serif; }
h1 { font-size: 21pt; color: #0b3c66; border-bottom: 2.5px solid #0072B2; padding-bottom: 6px; margin: 0 0 14px; line-height: 1.35; }
h2 { font-size: 14.5pt; color: #0b3c66; margin: 22px 0 8px; border-left: 4px solid #0072B2; padding-left: 8px; break-after: avoid; }
h3 { font-size: 12pt; color: #1f4e79; margin: 16px 0 6px; break-after: avoid; }
h4 { font-size: 10.8pt; margin: 12px 0 4px; break-after: avoid; }
p { margin: 0 0 8px; orphans: 2; widows: 2; }
a { color: #0b5cad; text-decoration: none; }
section.chapter { break-before: page; }
.part { break-before: page; height: 240mm; display: flex; flex-direction: column; justify-content: center; align-items: center; }
.part h1 { border: none; font-size: 28pt; text-align: center; }
.part .sub { color: #666; font-size: 11pt; }
blockquote { margin: 10px 0; padding: 8px 12px; background: #f3f7fb; border-left: 4px solid #56B4E9; color: #222; break-inside: avoid; }
blockquote p:last-child { margin-bottom: 0; }
table { border-collapse: collapse; width: 100%; margin: 10px 0 12px; font-size: 8.4pt; line-height: 1.45; text-align: left; }
th { background: #e8f0f8; font-weight: 700; }
th, td { border: 1px solid #b9c7d6; padding: 3px 5px; vertical-align: top; word-break: break-word; }
tr { break-inside: avoid; }
thead { display: table-header-group; }
img { max-width: 100%; max-height: 210mm; display: block; margin: 8px auto; break-inside: avoid; }
p > img + em, p > em:only-child { display: block; text-align: center; }
code { font-family: 'DejaVu Sans Mono', monospace; font-size: 8.6pt; background: #f4f4f4; padding: 0 2px; border-radius: 2px; }
pre { background: #f6f8fa; border: 1px solid #ddd; padding: 8px; font-size: 8pt; white-space: pre-wrap; word-break: break-all; break-inside: avoid; }
pre code { background: none; padding: 0; }
ul, ol { margin: 4px 0 8px 1.4em; padding: 0; }
li { margin: 2px 0; }
details { margin: 4px 0 6px; padding: 4px 8px; border: 1px solid #dde5ee; border-radius: 4px; break-inside: avoid; background: #fbfcfe; }
summary { font-weight: 700; list-style: none; }
summary::-webkit-details-marker { display: none; }
.footnote { font-size: 7.6pt; line-height: 1.45; color: #444; word-break: break-all; }
.footnote ol { margin-left: 1.6em; }
.footnote hr { display: none; }
sup { font-size: 70%; line-height: 0; }
.pm { font-size: 2px; color: #ffffff; line-height: 0; }
.cover { height: 250mm; display: flex; flex-direction: column; justify-content: center; text-align: center; }
.cover .t1 { font-size: 34pt; font-weight: 700; color: #0b3c66; margin-bottom: 10px; }
.cover .t2 { font-size: 15pt; color: #333; margin-bottom: 30px; }
.cover .t3 { font-size: 10.5pt; color: #555; line-height: 1.9; }
.cover .bar { height: 6px; background: linear-gradient(90deg,#0072B2,#E69F00,#009E73,#D55E00); margin: 26px 15%; }
.notes { break-before: page; }
.toc { break-before: page; font-size: 9.6pt; }
.toc h1 { font-size: 20pt; }
.toc .tp { font-weight: 700; margin: 10px 0 3px; color: #0b3c66; font-size: 10.5pt; }
.toc .te { display: flex; align-items: baseline; margin: 1px 0 1px 1.2em; }
.toc .te .tt { flex: 0 1 auto; }
.toc .te .dots { flex: 1 1 auto; border-bottom: 1px dotted #999; margin: 0 4px; transform: translateY(-3px); }
.toc .te .pg { flex: 0 0 auto; min-width: 2.6em; text-align: right; font-variant-numeric: tabular-nums; }
"""


def font_css(fonts: Path | None) -> str:
    if not fonts:
        return ""
    out = []
    for fam in ("noto-serif-sc", "noto-sans-sc"):
        for w in ("400", "700"):
            p = fonts / fam / f"{w}.css"
            if p.exists():
                out.append(f'<link rel="stylesheet" href="{p.as_uri()}">')
    return "\n".join(out)


def build_html(toc_entries, body_entries, pages: dict[str, int] | None, fonts: Path | None) -> str:
    toc = ['<div class="toc"><h1>目录</h1>']
    for kind, key, title, part_title in toc_entries:
        if kind == "part":
            toc.append(f'<div class="tp">{html.escape(part_title)}</div>')
        else:
            pg = str(pages.get(key, "")) if pages else "000"
            toc.append(f'<div class="te"><a class="tt" href="#chap-{key}">{html.escape(title)}</a>'
                       f'<span class="dots"></span><span class="pg">{pg}</span></div>')
    toc.append("</div>")
    body = []
    for kind, key, content, part_title in body_entries:
        if kind == "part":
            body.append(f'<div class="part"><h1>{html.escape(part_title)}</h1><div class="sub">AI 数据图谱 · 简体中文参考译本</div></div>')
        else:
            body.append(f'<section class="chapter" id="chap-{key}"><span class="pm">@@PM:{key}@@</span>{content}</section>')
    cover = """<div class="cover"><div class="t1">AI 数据图谱</div><div class="t2">AI Data Atlas · 数据库、数据管道、数据平台与 AI 数据技术栈</div>
<div class="bar"></div><div class="t3">技术如何运作 · 企业如何赚钱 · 数据栈与存储的交汇<br/>简体中文参考译本（英文原版为准）<br/>数据截至 2026-11-01</div></div>"""
    notes = """<div class="notes"><h1>译本说明</h1>
<p>本书为《AI Data Atlas》（AI 数据图谱）的简体中文参考译本，供阅读与打印参考之用；如与英文原版有出入，以仓库根目录下的英文原版为准。</p>
<p>书中所有数字均保留英文原版中的标注（GAAP / 非 GAAP / 公司披露的年化运行率 / 媒体报道 / 估算）、财年口径与资料来源；公司、产品与人名保留英文。标记为 <code>[VERIFY: …]</code> 的内容表示原版中尚待核实的事项。</p>
<p>图表（PNG 图表与 SVG 图）沿用英文原版，图中文字为英文；Mermaid 示意图已译为中文。脚注中的资料标题与网址保持原文。</p>
<p>本 PDF 由 <code>scripts/zh_build_pdf.py</code> 自动生成。</p></div>"""
    return f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><title>AI 数据图谱（简体中文参考译本）</title>
{font_css(fonts)}<style>{CSS}</style></head><body>{cover}{notes}{''.join(toc)}{''.join(body)}</body></html>"""


def find_pages(pdf: Path) -> dict[str, int]:
    pages = {}
    for i, page in enumerate(PdfReader(str(pdf)).pages, 1):
        for key in re.findall(r"@@PM:([\w-]+)@@", (page.extract_text() or "").replace(" ", "")):
            pages.setdefault(key, i)
    return pages


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fonts", type=Path, default=None, help="path to node_modules/@fontsource (optional)")
    ap.add_argument("--out", type=Path, default=ZH / "AI-Data-Atlas-zh.pdf")
    ap.add_argument("--keep", type=Path, default=None, help="keep build dir here")
    ap.add_argument("--only", nargs="*", default=None, help="chapter keys to include (testing)")
    a = ap.parse_args()
    build = a.keep or Path(tempfile.mkdtemp(prefix="zhpdf-"))
    build.mkdir(parents=True, exist_ok=True)
    cfg, mcfg = build / "puppeteer.json", build / "mermaid.json"
    exe = "/opt/pw-browsers/chromium"
    cfg.write_text(json.dumps({"executablePath": exe, "args": ["--no-sandbox", "--headless"]} if Path(exe).exists() else {"args": ["--no-sandbox"]}))
    mcfg.write_text(json.dumps({"theme": "default", "themeVariables": {"fontFamily": "Noto Sans SC, WenQuanYi Zen Hei, sans-serif"}}))

    files = [ZH / "docs" / "index.md"]
    for part, _ in PARTS:
        files += sorted((ZH / "docs" / part).glob("ch*.md"))
    files.append(ZH / "docs" / "glossary.md")
    if a.only:
        files = [f for f in files if chapter_key(f) in a.only]
    entries = []
    current_part = None
    for f in files:
        if not f.exists():
            print(f"MISSING: {f.relative_to(ZH)}")
            continue
        part = f.parent.name
        if part != current_part and part.startswith("0"):
            current_part = part
            entries.append(("part", part, None, dict(PARTS)[part]))
        elif f.name == "glossary.md":
            current_part = "glossary"
            entries.append(("part", "glossary-part", None, "附录 · 术语表"))
        key = chapter_key(f)
        print(f"render {f.relative_to(ZH)}")
        built = render_mermaid(f, build, cfg, mcfg)
        text = preprocess(built.read_text(encoding="utf-8"), key, built, f)
        body, title = to_html(text, key)
        if key == "preface":
            title = "前言"
        entries.append(("chapter", key, body, title))
    toc_entries = [(k, key, (t if k == "chapter" else None), (t if k == "part" else None)) for k, key, _, t in entries]
    body_entries = [(k, key, c, (t if k == "part" else None)) for k, key, c, t in entries]

    def assemble(pages):
        return build_html(toc_entries, body_entries, pages, a.fonts)

    renderer = ROOT / "scripts" / "zh_pdf_render.js"
    html1 = build / "book_pass1.html"
    html1.write_text(assemble(None), encoding="utf-8")
    pdf1 = build / "pass1.pdf"
    print("Chromium pass 1 …")
    subprocess.run(["node", str(renderer), str(html1), str(pdf1)], check=True, cwd=str(build))
    pages = find_pages(pdf1)
    print(f"found {len(pages)} chapter start pages")
    html2 = build / "book.html"
    html2.write_text(assemble(pages), encoding="utf-8")
    print("Chromium pass 2 …")
    subprocess.run(["node", str(renderer), str(html2), str(a.out)], check=True, cwd=str(build))
    n = len(PdfReader(str(a.out)).pages)
    print(f"PDF written: {a.out} ({n} pages, {a.out.stat().st_size/1e6:.1f} MB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
