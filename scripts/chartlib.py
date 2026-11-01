"""Shared chart helpers: colorblind-safe palette (Okabe-Ito), CSV loading, consistent styling.

Every chart in the atlas is generated from data/*.csv by scripts/make_charts.py
(core charts) or by a per-chapter script in scripts/charts/ (auto-discovered).
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = ROOT / "docs" / "assets" / "charts"
OUT.mkdir(parents=True, exist_ok=True)

PALETTE = {
    "blue": "#0072B2", "orange": "#E69F00", "green": "#009E73", "vermillion": "#D55E00",
    "sky": "#56B4E9", "purple": "#CC79A7", "yellow": "#F0E442", "black": "#000000", "grey": "#666666",
}
SERIES = [PALETTE[k] for k in ("blue", "orange", "green", "vermillion", "sky", "purple", "yellow", "grey")]

plt.rcParams.update({
    "figure.figsize": (9, 5), "figure.dpi": 110, "savefig.dpi": 150, "savefig.bbox": "tight",
    "axes.spines.top": False, "axes.spines.right": False, "axes.grid": True, "grid.alpha": 0.25,
    "axes.prop_cycle": matplotlib.cycler(color=SERIES), "font.size": 10, "axes.titleweight": "bold",
    "axes.titlesize": 12, "axes.titlelocation": "left",
})


def load(name: str) -> pd.DataFrame:
    """Load data/<name>.csv (name with or without .csv)."""
    p = DATA / (name if name.endswith(".csv") else f"{name}.csv")
    return pd.read_csv(p)


def num(series: pd.Series) -> pd.Series:
    """Coerce a column to numeric (blank / text -> NaN)."""
    return pd.to_numeric(series.astype(str).str.replace(r"[,$%x]", "", regex=True), errors="coerce")


def source_note(ax, text: str) -> None:
    """Put a small source line under the plot."""
    ax.figure.text(0.01, -0.02, text, fontsize=7.5, color=PALETTE["grey"], ha="left", va="top", wrap=True)


def save(fig, name: str) -> Path:
    path = OUT / (name if name.endswith(".png") else f"{name}.png")
    fig.savefig(path)
    plt.close(fig)
    return path
