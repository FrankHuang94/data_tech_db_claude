#!/usr/bin/env bash
# Render every ```mermaid block with mermaid-cli (mmdc); fail on any error.
# Usage: scripts/lint_mermaid.sh            # all docs/**/*.md
#        scripts/lint_mermaid.sh file.md…   # specific files
# Requires: npm i -g @mermaid-js/mermaid-cli
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

# Puppeteer config: use the preinstalled Chromium when present (cloud sandbox), else mmdc's default.
CFG="$TMP/puppeteer.json"
if [ -x /opt/pw-browsers/chromium ]; then
  echo '{"executablePath":"/opt/pw-browsers/chromium","args":["--no-sandbox","--headless"]}' > "$CFG"
else
  echo '{"args":["--no-sandbox"]}' > "$CFG"
fi

if [ "$#" -gt 0 ]; then FILES=("$@"); else mapfile -t FILES < <(find "$ROOT/docs" -name '*.md' | sort); fi

fail=0; blocks=0; nfiles=0
for f in "${FILES[@]}"; do
  [ -f "$f" ] || continue
  # Extract each mermaid block to its own .mmd file so errors point at a block.
  base="$(basename "$f" .md)"
  python3 - "$f" "$TMP/$base" <<'PY'
import re, sys, pathlib
src, prefix = sys.argv[1], sys.argv[2]
lines = pathlib.Path(src).read_text(encoding="utf-8").splitlines()
inside, buf, n, start = False, [], 0, 0
for i, line in enumerate(lines, 1):
    s = line.strip()
    if not inside and re.match(r"^```\s*mermaid\s*$", s):
        inside, buf, start = True, [], i
        continue
    if inside and s.startswith("```"):
        n += 1
        pathlib.Path(f"{prefix}__{n:03d}__L{start}.mmd").write_text("\n".join(buf) + "\n", encoding="utf-8")
        inside = False
        continue
    if inside:
        buf.append(line)
PY
  shopt -s nullglob
  for m in "$TMP/$base"__*.mmd; do
    blocks=$((blocks+1))
    if ! out=$(mmdc -q -p "$CFG" -i "$m" -o "${m%.mmd}.svg" 2>&1); then
      fail=$((fail+1))
      line="${m##*__L}"; line="${line%.mmd}"
      echo "FAIL: ${f#$ROOT/}:${line}"
      echo "$out" | grep -v '^\s*at ' | head -5 | sed 's/^/    /'
    fi
  done
  shopt -u nullglob
  nfiles=$((nfiles+1))
done
echo "Mermaid lint: $blocks blocks in $nfiles files, $fail failures."
[ "$fail" -eq 0 ]
