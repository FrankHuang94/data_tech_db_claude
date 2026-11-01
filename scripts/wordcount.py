#!/usr/bin/env python3
"""Count prose words per chapter, per part and in total.

Prose excludes: fenced code blocks (incl. Mermaid), table rows, footnote
definitions, headings, HTML tags, image lines, URLs and the chapter metadata
line (the first blockquote starting with **Depth:** or **Status:**).
The glossary is excluded from totals (reported separately).

Usage:
  scripts/wordcount.py                 # table for all chapters + totals
  scripts/wordcount.py docs/x/ch07.md  # one or more files
  scripts/wordcount.py --json          # machine-readable
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
EXCLUDE_NAMES = {"glossary.md", "index.md"}

FENCE_RE = re.compile(r"^\s*(```|~~~)")
WORD_RE = re.compile(r"[A-Za-z0-9$€£%][A-Za-z0-9$€£%'’.,/+\-–]*")


def prose_text(md: str) -> str:
    out: list[str] = []
    in_fence = False
    for line in md.splitlines():
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        s = line.strip()
        if not s:
            continue
        if s.startswith("|"):
            continue  # table row
        if re.match(r"^\[\^[^\]]+\]:", s):
            continue  # footnote definition
        if s.startswith("#"):
            continue  # heading
        if s.startswith("![") or s.startswith("<img"):
            continue
        if re.match(r"^>\s*\*\*(Depth|Status):", s):
            continue  # metadata line
        if re.match(r"^\*Figure [0-9.]+", s):
            continue  # captions are not prose
        s = re.sub(r"<[^>]+>", " ", s)  # html tags
        s = re.sub(r"\[\^[^\]]+\]", " ", s)  # footnote refs
        s = re.sub(r"\]\([^)]*\)", "] ", s)  # link targets
        s = re.sub(r"https?://\S+", " ", s)
        s = re.sub(r"[*_`>]", " ", s)
        out.append(s)
    return "\n".join(out)


def count_words(md: str) -> int:
    return len(WORD_RE.findall(prose_text(md)))


def chapter_files(paths: list[str] | None = None) -> list[Path]:
    if paths:
        return [Path(p).resolve() for p in paths]
    files = sorted(p for p in DOCS.rglob("*.md") if p.name not in EXCLUDE_NAMES)
    return [p for p in files if "assets" not in p.parts]


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    as_json = "--json" in sys.argv
    files = chapter_files(args or None)
    rows = []
    for f in files:
        rows.append({"file": str(f.relative_to(ROOT)), "part": f.parent.name, "words": count_words(f.read_text(encoding="utf-8"))})
    parts: dict[str, int] = {}
    for r in rows:
        parts[r["part"]] = parts.get(r["part"], 0) + r["words"]
    total = sum(r["words"] for r in rows)
    gloss = DOCS / "glossary.md"
    if as_json:
        print(json.dumps({"chapters": rows, "parts": parts, "total": total}, indent=2))
        return 0
    print(f"{'file':70} {'words':>7}")
    for r in rows:
        print(f"{r['file']:70} {r['words']:>7}")
    print("-" * 78)
    for p, w in sorted(parts.items()):
        print(f"{p:70} {w:>7}")
    print(f"{'TOTAL (prose, excl. glossary)':70} {total:>7}")
    if gloss.exists() and not args:
        print(f"{'(glossary, not in total)':70} {count_words(gloss.read_text(encoding='utf-8')):>7}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
