"""Ch 25: Databricks company-stated revenue run-rate disclosures (data/ch25_databricks_runrate.csv)."""
from chartlib import load, num, save, source_note, PALETTE, plt
import pandas as pd


SERIES_SPEC = [
    ("total_run_rate", "Total revenue run-rate", PALETTE["blue"], "o", "-"),
    ("data_warehousing_run_rate", "Data warehousing (Databricks SQL) run-rate", PALETTE["orange"], "s", "-"),
    ("ai_products_run_rate", "AI products run-rate", PALETTE["green"], "^", "-"),
    ("lakebase_run_rate", "Lakebase run-rate", PALETTE["vermillion"], "D", "-"),
]


def make():
    d = load("ch25_databricks_runrate")
    d["dt"] = pd.to_datetime(d["date"], errors="coerce")
    d["v"] = num(d["value_usd_b"])
    fig, ax = plt.subplots(figsize=(10, 5.4))
    for metric, label, color, marker, ls in SERIES_SPEC:
        s = d[d["metric"] == metric].sort_values("dt")
        if s.empty:
            continue
        ax.plot(s["dt"], s["v"], marker=marker, markersize=7, linewidth=2, linestyle=ls, color=color, label=label)
        last = s.iloc[-1]
        ax.annotate(f"${last['v']:.1f}B", (last["dt"], last["v"]), xytext=(8, -3), textcoords="offset points",
                    fontsize=8, color=PALETTE["black"])
    # selective labels on the total series
    tot = d[d["metric"] == "total_run_rate"].sort_values("dt")
    for _, r in tot.iloc[:-1].iterrows():
        if r["v"] >= 1.0:
            ax.annotate(f"${r['v']:.1f}B", (r["dt"], r["v"]), xytext=(-12, 8), textcoords="offset points",
                        fontsize=8, color=PALETTE["black"])
    fy = d[d["metric"] == "fiscal_year_revenue"].sort_values("dt")
    if not fy.empty:
        ax.scatter(fy["dt"], fy["v"], s=60, facecolors="none", edgecolors=PALETTE["grey"], linewidths=1.6,
                   label="Fiscal-year revenue (FY ends Jan 31)", zorder=3)
        for _, r in fy.iterrows():
            ax.annotate(f"FY ${r['v']:.1f}B", (r["dt"], r["v"]), xytext=(6, -12), textcoords="offset points",
                        fontsize=7.5, color=PALETTE["grey"])
    ax.set_ylim(0, 8)
    ax.set_ylabel("US$ billions (annualized)")
    ax.set_title("Databricks company-stated revenue run-rate, 2021–2026 (private; unaudited)")
    ax.legend(fontsize=8, frameon=False, loc="upper left")
    source_note(ax, "Source: data/ch25_databricks_runrate.csv (Databricks press releases; CNBC, Bloomberg, TechCrunch for "
                    "pre-2025 points). Most values are floors ('surpassed $X'); 2024-07 and 2025-01 are company projections. "
                    "Run-rate definition not disclosed. Retrieved 2026-11-01.")
    return [save(fig, "ch25_databricks_runrate")]
