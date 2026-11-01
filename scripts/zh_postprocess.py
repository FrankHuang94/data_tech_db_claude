#!/usr/bin/env python3
"""Post-process the Simplified Chinese edition in `Chinese translation/`.

1. Anchors: for every `##`/`###`/`####` heading in a translated file, insert an
   `<a id="english-slug"></a>` line before it, using the slug of the English heading at the
   same position, so every `file.md#english-anchor` link keeps working on GitHub/MkDocs.
2. Links: any relative link/image whose target does not exist relative to the Chinese file
   but does exist relative to the English counterpart (e.g., docs/assets/*, data/*.csv,
   meta/*) is rewritten to point at the shared English file.
3. Root glossary: regenerate `Chinese translation/glossary.md` from
   `Chinese translation/docs/glossary.md` (links prefixed with docs/).

Usage: scripts/zh_postprocess.py [--check]
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_links import slugify  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
ZH = ROOT / "Chinese translation"
FENCE = re.compile(r"^\s*(```|~~~)")
HEAD = re.compile(r"^(#{2,4})\s+(.*?)\s*#*\s*$")
LINK = re.compile(r"(!?\[[^\]]*\])\(([^)\s]+)\)")
ANCHOR_LINE = re.compile(r'^<a\s+id="([^"]+)"></a>\s*$')


def headings(lines: list[str]) -> list[tuple[int, int, str]]:
    out, fence = [], False
    for i, line in enumerate(lines):
        if FENCE.match(line):
            fence = not fence
            continue
        if fence:
            continue
        m = HEAD.match(line)
        if m:
            out.append((i, len(m.group(1)), m.group(2)))
    return out


def en_slugs(lines: list[str]) -> list[tuple[int, str]]:
    counts: dict[str, int] = {}
    res = []
    for _, lvl, text in headings(lines):
        s = slugify(text)
        n = counts.get(s, 0)
        res.append((lvl, s if n == 0 else f"{s}-{n}"))
        counts[s] = n + 1
    return res


def inject_anchors(zh_file: Path, en_file: Path) -> str:
    zl = zh_file.read_text(encoding="utf-8").splitlines()
    el = en_file.read_text(encoding="utf-8").splitlines()
    es = en_slugs(el)
    zh = headings(zl)
    if [l for l, _ in es] != [l for _, l, _ in zh]:
        # fall back: align by level sequence greedily
        status = f"level-mismatch (en {len(es)} vs zh {len(zh)})"
        pairs = []
        j = 0
        for (i, lvl, text) in zh:
            while j < len(es) and es[j][0] != lvl:
                j += 1
            if j < len(es):
                pairs.append((i, es[j][1]))
                j += 1
    else:
        status = "ok"
        pairs = [(i, s) for (i, _, _), (_, s) in zip(zh, es)]
    existing = set()
    for line in zl:
        m = ANCHOR_LINE.match(line.strip())
        if m:
            existing.add(m.group(1))
    inserts = {}
    for i, slug in pairs:
        if slug in existing:
            continue
        zh_slug = slugify(HEAD.match(zl[i]).group(2))
        if zh_slug == slug:
            continue
        inserts[i] = f'<a id="{slug}"></a>'
    if inserts:
        new = []
        for i, line in enumerate(zl):
            if i in inserts:
                if new and new[-1].strip():
                    new.append("")
                new.append(inserts[i])
            new.append(line)
        zh_file.write_text("\n".join(new) + "\n", encoding="utf-8")
    return f"{status}, +{len(inserts)} anchors"


def fix_links(zh_file: Path, en_file: Path) -> int:
    text = zh_file.read_text(encoding="utf-8")
    changed = 0

    def repl(m: re.Match) -> str:
        nonlocal changed
        label, target = m.group(1), m.group(2)
        if re.match(r"^(https?:|mailto:|#)", target):
            return m.group(0)
        path, sep, anchor = target.partition("#")
        if not path:
            return m.group(0)
        if (zh_file.parent / path).resolve().exists():
            return m.group(0)
        en_target = (en_file.parent / path).resolve()
        if en_target.exists():
            rel = os.path.relpath(en_target, zh_file.parent).replace(os.sep, "/")
            changed += 1
            return f"{label}({rel}{sep}{anchor})"
        return m.group(0)

    out = LINK.sub(repl, text)
    if changed:
        zh_file.write_text(out, encoding="utf-8")
    return changed


def root_glossary() -> None:
    src = ZH / "docs" / "glossary.md"
    if not src.exists():
        return
    text = src.read_text(encoding="utf-8")

    def fix(m: re.Match) -> str:
        label, target = m.group(1), m.group(2)
        if re.match(r"^(https?:|mailto:|#)", target):
            return m.group(0)
        if target.startswith("../"):
            return f"{label}({target[3:]})"
        return f"{label}(docs/{target})"

    banner = "<!-- 由 scripts/zh_postprocess.py 根据 docs/glossary.md 自动生成，请勿在此编辑。 -->\n"
    (ZH / "glossary.md").write_text(banner + LINK.sub(fix, text), encoding="utf-8")


def main() -> int:
    files = sorted(p for p in ZH.rglob("*.md") if p.name != "glossary.md" or p.parent.name == "docs")
    for zf in files:
        rel = zf.relative_to(ZH)
        ef = ROOT / rel
        if not ef.exists():
            print(f"skip (no English counterpart): {rel}")
            continue
        info = inject_anchors(zf, ef) if zf.name != "glossary.md" else "glossary (anchors by translator)"
        n = fix_links(zf, ef)
        print(f"{str(rel):70} {info}; {n} links re-pointed")
    root_glossary()
    return 0


if __name__ == "__main__":
    sys.exit(main())
