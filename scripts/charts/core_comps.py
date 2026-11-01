"""Public comps scatter: EV/NTM revenue vs revenue growth (signature visual SV-14)."""
from chartlib import load, num, save, source_note, PALETTE, plt
import numpy as np


def make():
    c = load("public_comps")
    c["mult"] = num(c["ev_ntm_revenue"])
    c["g"] = num(c["revenue_growth_yoy_pct"])
    c = c[c["mult"].notna() & c["g"].notna() & ~c["category"].fillna("").str.contains("acquired")]
    fig, ax = plt.subplots(figsize=(10, 6))
    hl = c["company"].str.contains("Everpure|Snowflake|MongoDB|Palantir", regex=True)
    ax.scatter(c.loc[~hl, "g"], c.loc[~hl, "mult"], color=PALETTE["blue"], s=50, alpha=0.8)
    ax.scatter(c.loc[hl, "g"], c.loc[hl, "mult"], color=PALETTE["vermillion"], s=70)
    for _, r in c.iterrows():
        ax.annotate(r["ticker"].split(" ")[0], (r["g"], r["mult"]), fontsize=8, xytext=(4, 3), textcoords="offset points")
    fit = c[c["mult"] < 40]
    if len(fit) >= 4:
        k, b = np.polyfit(fit["g"], fit["mult"], 1)
        xs = np.linspace(fit["g"].min(), fit["g"].max(), 50)
        r2 = np.corrcoef(fit["g"], fit["mult"])[0, 1] ** 2
        ax.plot(xs, k * xs + b, ls="--", color=PALETTE["grey"], lw=1)
        ax.text(xs[-1], k * xs[-1] + b, f"  OLS ex-outliers (>40x): y={k:.2f}x{b:+.1f}, R²={r2:.2f}", fontsize=7.5, color=PALETTE["grey"], va="bottom", ha="right")
    ax.set_xlabel("Revenue growth, latest reported quarter YoY (%)")
    ax.set_ylabel("EV / NTM revenue (x)")
    ax.set_title("Public data and infrastructure software comps: EV/NTM revenue vs. growth")
    asof = c["as_of"].dropna()
    source_note(ax, f"Source: data/public_comps.csv (market data snapshots {asof.min()} to {asof.max()}; NTM revenue mostly guidance-derived estimates — see ntm_revenue_basis).")
    return save(fig, "comps_ev_ntm_vs_growth")
