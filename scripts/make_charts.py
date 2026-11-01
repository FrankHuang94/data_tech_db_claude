#!/usr/bin/env python3
"""Regenerate every chart in docs/assets/charts/ from data/*.csv.

Charts live in scripts/charts/*.py. Each module exposes `make() -> list[pathlib.Path]`
(or a single Path). This runner imports every module in alphabetical order, calls
make(), and reports successes and failures. Exit code 1 if any chart fails.

Usage:
  scripts/make_charts.py            # all charts
  scripts/make_charts.py core_ma    # only modules whose name contains "core_ma"
"""
from __future__ import annotations

import importlib.util
import sys
import traceback
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


def main() -> int:
    filt = sys.argv[1] if len(sys.argv) > 1 else ""
    mods = sorted(p for p in (HERE / "charts").glob("*.py") if not p.name.startswith("_") and filt in p.stem)
    ok = fail = 0
    for p in mods:
        spec = importlib.util.spec_from_file_location(f"charts.{p.stem}", p)
        mod = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(mod)  # type: ignore[union-attr]
            out = mod.make()
            outs = out if isinstance(out, (list, tuple)) else [out]
            for o in outs:
                print(f"OK   {p.stem:40} -> {Path(o).name}")
            ok += len(outs)
        except Exception as exc:  # noqa: BLE001
            fail += 1
            print(f"FAIL {p.stem:40} {exc.__class__.__name__}: {exc}")
            traceback.print_exc(limit=2)
    print(f"Charts: {ok} generated, {fail} failed.")
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
