#!/usr/bin/env python3
"""Regenerate the auto-generated sections of README.md (contents/progress table, totals).

README.md contains the markers
  <!-- AUTO:CONTENTS START --> … <!-- AUTO:CONTENTS END -->
which are replaced by a table of every chapter (linked) with prose words, visuals,
[VERIFY] count and review status, computed by qa_report.analyze().
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from qa_report import analyze  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
PARTS = {
    "00-start-here": "Part 0 · Start Here",
    "01-data-systems-foundations": "Part 1 · Data Systems Foundations",
    "02-pipelines-and-governance": "Part 2 · Pipelines, Movement and Governance",
    "03-ai-data-stack": "Part 3 · The AI Data Stack",
    "04-company-deep-dives": "Part 4 · Company Deep Dives",
    "05-business-and-economics": "Part 5 · Business and Economics",
    "06-history-and-future": "Part 6 · History and Future",
    "07-conversation-toolkit": "Part 7 · Conversation Toolkit",
}


def title(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def main() -> int:
    reviewed = set()
    rv = ROOT / "meta" / "reviewed.txt"
    if rv.exists():
        reviewed = {l.strip() for l in rv.read_text().splitlines() if l.strip()}
    rows = ["| Part | Chapter | Prose words | Visuals | [VERIFY] | Reviewed |", "|---|---|---|---|---|---|"]
    tw = tv = tver = n = 0
    for part, label in PARTS.items():
        for f in sorted((ROOT / "docs" / part).glob("ch*.md")):
            a = analyze(f)
            n += 1
            tw += a["words"]; tv += a["visuals"]; tver += a["verify"]
            rows.append(f"| {label.split(' · ')[0]} | [{title(f)}](docs/{part}/{f.name}) | {a['words']:,} | {a['visuals']} | {a['verify']} | {'✓' if f.name in reviewed else ''} |")
    block = (f"**{n} chapters · {tw:,} prose words · {tv} visuals · {tver} open [VERIFY] markers** "
             f"(counts from `scripts/qa_report.py`; prose excludes tables, code/Mermaid, captions and footnotes).\n\n" + "\n".join(rows))
    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    text = re.sub(r"<!-- AUTO:CONTENTS START -->.*<!-- AUTO:CONTENTS END -->",
                  f"<!-- AUTO:CONTENTS START -->\n{block}\n<!-- AUTO:CONTENTS END -->", text, flags=re.S)
    readme.write_text(text, encoding="utf-8")
    print(f"README updated: {n} chapters, {tw:,} words, {tv} visuals")
    return 0


if __name__ == "__main__":
    sys.exit(main())
