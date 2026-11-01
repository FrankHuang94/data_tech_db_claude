#!/usr/bin/env python3
"""Regenerate the chapter-tracker table in PROGRESS.md from the chapter files.

Status: 'not started' (file missing), 'drafted' (exists), 'QA pass' (no QA problems),
'reviewed' (listed in meta/reviewed.txt). Also refreshes the totals line.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from qa_report import analyze, budgets  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
prog = ROOT / "PROGRESS.md"
outline = (ROOT / "meta" / "outline.md").read_text()
reviewed = set()
rv = ROOT / "meta" / "reviewed.txt"
if rv.exists():
    reviewed = {l.strip() for l in rv.read_text().splitlines() if l.strip()}
b = budgets()
rows, tw, tv, tver, done = [], 0, 0, 0, 0
part = None
for line in outline.splitlines():
    m = re.search(r"`docs/(\d\d-[a-z-]+)/`", line)
    if m:
        part = m.group(1)
        continue
    m = re.match(r"\|\s*([\d.]+)\s*\|\s*`([^`]+\.md)`", line)
    if not (m and part):
        continue
    num, fname = m.groups()
    f = ROOT / "docs" / part / fname
    if f.exists():
        a = analyze(f)
        problems = []
        if a["visuals"] < 3 or a["diagrams"] < 2 or a["missing"] or a["undefined_refs"]:
            problems.append(1)
        status = "reviewed" if fname in reviewed else ("QA pass" if not problems else "drafted")
        words, vis, ver = a["words"], a["visuals"], a["verify"]
        done += 1
    else:
        status, words, vis, ver = "not started", 0, 0, 0
    tw += words; tv += vis; tver += ver
    rows.append(f"| {num} | {fname} | {status} | {words:,} | {b.get(fname, '')} | {vis} | {ver} | {'yes' if fname in reviewed else 'no'} |")
text = prog.read_text()
head, _, _ = text.partition("| Ch | File | Status |")
table = "| Ch | File | Status | Words | Budget | Visuals | VERIFY | Reviewed |\n|---|---|---|---|---|---|---|---|\n" + "\n".join(rows) + "\n"
totals = f"\n**Totals:** {done}/{len(rows)} chapters drafted · {tw:,} prose words · {tv} visuals · {tver} [VERIFY] markers.\n"
head = re.sub(r"\n\*\*Totals:\*\*.*\n", "\n", head)
prog.write_text(head.rstrip() + "\n" + totals + "\n" + table)
print(totals.strip())
