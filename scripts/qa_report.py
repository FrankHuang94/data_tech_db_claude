#!/usr/bin/env python3
"""QA report: template compliance, visual density, word budgets, VERIFY count, footnotes.

Writes meta/qa-report.md and prints a summary. Exit code 1 with --strict if any chapter fails.

Usage:
  scripts/qa_report.py               # all chapters
  scripts/qa_report.py docs/…/ch07…  # specific files (no report file written)
  scripts/qa_report.py --strict
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from wordcount import count_words, chapter_files  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUTLINE = ROOT / "meta" / "outline.md"

CONCEPT = ["tl;dr", "why this matters", "how it works", "design choices and trade-offs", "who's who",
           "history and trajectory", "numbers that matter", "conversation playbook", "going deeper",
           "key terms", "sources"]
COMPANY = ["tl;dr", "snapshot table", "origin story and strategic arc", "product and technology",
           "how it makes money", "financials", "customers and go-to-market", "m&a and investments",
           "competitive position", "why it's winning / bull case", "risks / bear case and open questions",
           "relevance to everpure", "conversation playbook", "sources"]
TOOLKIT = ["tl;dr", "why this matters", "key terms", "sources"]
START = ["tl;dr", "key terms", "sources"]

FENCE_RE = re.compile(r"^\s*```\s*(\w+)?")


def budgets() -> dict[str, int]:
    out = {}
    if OUTLINE.exists():
        for m in re.finditer(r"\|\s*[\d.]+\s*\|\s*`([^`]+\.md)`\s*\|\s*([\d,]+)\s*\|", OUTLINE.read_text()):
            out[m.group(1)] = int(m.group(2).replace(",", ""))
    return out


def analyze(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    mermaid = images = tables = 0
    in_fence = False
    table_rows = 0
    h2 = []
    for line in lines + [""]:
        m = FENCE_RE.match(line)
        if m:
            if not in_fence and (m.group(1) or "").lower() == "mermaid":
                mermaid += 1
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        s = line.strip()
        if s.startswith("|"):
            table_rows += 1
        else:
            if table_rows >= 4:  # header + separator + ≥2 rows… require ≥3 data rows below
                if table_rows >= 5:
                    tables += 1
            table_rows = 0
        images += len(re.findall(r"!\[[^\]]*\]\([^)]+\)", s)) + len(re.findall(r"<img\s", s))
        if s.startswith("## "):
            h2.append(s[3:].strip().lower())
    name = path.name
    part = path.parent.name
    if part.startswith("04-"):
        required = COMPANY
    elif part.startswith("07-"):
        required = TOOLKIT + (["conversation playbook"] if name[:4] in ("ch46", "ch47") else [])
    elif part.startswith("00-"):
        required = START
    else:
        required = CONCEPT
    missing = [r for r in required if not any(h.startswith(r) for h in h2)]
    refs = set(re.findall(r"\[\^([^\]]+)\](?!:)", text))
    defs = set(re.findall(r"^\[\^([^\]]+)\]:", text, flags=re.M))
    words = count_words(text)
    diagrams = mermaid + images
    visuals = diagrams + tables
    return {
        "file": name, "path": path, "part": part, "words": words, "mermaid": mermaid, "images": images,
        "tables": tables, "visuals": visuals, "diagrams": diagrams,
        "words_per_visual": round(words / visuals) if visuals else None,
        "missing": missing, "verify": len(re.findall(r"\[VERIFY", text)),
        "footnotes": len(defs), "undefined_refs": sorted(refs - defs), "unused_defs": sorted(defs - refs),
    }


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    strict = "--strict" in sys.argv
    files = chapter_files(args or None)
    b = budgets()
    rows, failures = [], 0
    for f in files:
        r = analyze(f)
        r["budget"] = b.get(r["file"])
        problems = []
        if r["visuals"] < 3:
            problems.append("<3 visuals")
        if r["diagrams"] < 2:
            problems.append("<2 diagrams/charts")
        if r["words"] and r["visuals"] and r["words"] / r["visuals"] > 700:
            problems.append(">700 words/visual")
        if r["missing"]:
            problems.append("missing: " + ", ".join(r["missing"]))
        if r["undefined_refs"]:
            problems.append("undefined footnotes: " + ", ".join(r["undefined_refs"][:5]))
        if r["budget"] and r["words"] < 0.9 * r["budget"]:
            problems.append(f"under budget ({r['words']}/{r['budget']})")
        if r["footnotes"] < 3 and not r["part"].startswith("07-"):
            problems.append("<3 sources")
        r["problems"] = problems
        failures += bool(problems)
        rows.append(r)

    total_words = sum(r["words"] for r in rows)
    total_visuals = sum(r["visuals"] for r in rows)
    total_verify = sum(r["verify"] for r in rows)
    lines = ["# QA report", "", "Generated by `scripts/qa_report.py`.", "",
             f"**Chapters:** {len(rows)} · **Prose words:** {total_words:,} · **Visuals:** {total_visuals} "
             f"(Mermaid {sum(r['mermaid'] for r in rows)}, images {sum(r['images'] for r in rows)}, tables {sum(r['tables'] for r in rows)}) · "
             f"**[VERIFY] markers:** {total_verify} · **Chapters with problems:** {failures}", "",
             "| File | Words | Budget | Visuals (M/I/T) | W/visual | VERIFY | Footnotes | Problems |",
             "|---|---|---|---|---|---|---|---|"]
    for r in rows:
        lines.append(f"| {r['file']} | {r['words']:,} | {r['budget'] or ''} | {r['visuals']} ({r['mermaid']}/{r['images']}/{r['tables']}) | "
                     f"{r['words_per_visual'] or ''} | {r['verify']} | {r['footnotes']} | {'; '.join(r['problems']) or 'OK'} |")
    report = "\n".join(lines) + "\n"
    if not args:
        (ROOT / "meta" / "qa-report.md").write_text(report, encoding="utf-8")
    print(report)
    return 1 if (strict and failures) else 0


if __name__ == "__main__":
    sys.exit(main())
