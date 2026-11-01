#!/usr/bin/env bash
# Integrator helper: QA + Mermaid lint a chapter, merge staging, update PROGRESS, commit.
# Usage: scripts/integrate.sh <chapter-file> "<commit subject>"
set -uo pipefail
cd "$(dirname "$0")/.."
f="$1"; msg="$2"
python3 scripts/qa_report.py "$f" | tail -n 2
scripts/lint_mermaid.sh "$f" | tail -n 4
python3 scripts/check_links.py "$f" | grep -v glossary.md | tail -n 6
python3 scripts/merge_staging.py >/dev/null
python3 scripts/make_charts.py >/dev/null 2>&1 || python3 scripts/make_charts.py | grep FAIL
python3 scripts/update_progress.py
git add -A
git commit -q -m "$msg

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_015j6Et44vVa5dK62bXN3KKX" && echo "committed: $msg"
