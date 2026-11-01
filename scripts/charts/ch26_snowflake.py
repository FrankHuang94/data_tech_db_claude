"""Ch 26: Snowflake growth vs. NRR, and GAAP vs. non-GAAP margin bridge (data/company_financials.csv)."""
from chartlib import load, num, save, source_note, PALETTE, plt
import numpy as np


def _sf(f, metric):
    s = f[(f["company"] == "Snowflake") & (f["metric"] == metric)].copy()
    s["v"] = num(s["value"])
    return s.drop_duplicates("fiscal_period").set_index("fiscal_period")["v"]


def growth_vs_nrr(f):
    rev = _sf(f, "product_revenue")
    qg = _sf(f, "product_revenue_growth_yoy_pct")
    nrr = _sf(f, "nrr_pct")
    fy = [p for p in ["FY2021", "FY2022", "FY2023", "FY2024", "FY2025", "FY2026"] if p in rev.index]
    q = [p for p in ["Q4 FY2026", "Q1 FY2027", "Q2 FY2027"] if p in qg.index]
    cats, growth, exp = [], [], []
    for p in fy:
        prev = f"FY{int(p[2:]) - 1}"
        growth.append((rev[p] / rev[prev] - 1) * 100 if prev in rev.index else np.nan)
        exp.append(nrr.get(p, np.nan))
        cats.append(p)
    for p in q:
        cats.append(p)
        growth.append(qg[p])
        exp.append(nrr.get(p, np.nan))
    fig, ax = plt.subplots(figsize=(10, 5.2))
    x = np.arange(len(cats))
    colors = [PALETTE["sky"]] * len(fy) + [PALETTE["blue"]] * len(q)
    ax.bar(x, growth, color=colors, label="Product revenue growth, YoY % (FY = annual; Q = quarter vs year-ago quarter)")
    for xi, g in zip(x, growth):
        if not np.isnan(g):
            ax.text(xi, g + 2, f"{g:.0f}%", ha="center", fontsize=8)
    ax.plot(x, [e - 100 for e in exp], color=PALETTE["vermillion"], marker="o", linewidth=2,
            label="NRR minus 100 (growth contributed by existing customers), pts")
    for xi, e in zip(x, exp):
        if not np.isnan(e):
            ax.annotate(f"NRR {e:.0f}%", (xi, e - 100), xytext=(0, -14), textcoords="offset points",
                        ha="center", fontsize=7.5, color=PALETTE["vermillion"])
    ax.set_xticks(x)
    ax.set_xticklabels(cats, rotation=25, ha="right")
    ax.set_ylabel("Percent / percentage points")
    ax.set_ylim(0, 135)
    ax.set_title("Snowflake: product revenue growth tracks net revenue retention")
    ax.legend(fontsize=8, frameon=False, loc="upper right")
    source_note(ax, "Source: data/company_financials.csv (Snowflake 10-K and quarterly releases; GAAP product revenue; NRR is a "
                    "company-stated trailing-12-month KPI). FY ends Jan 31: FY2026 = Feb 2025-Jan 2026; Q2 FY2027 = May-Jul 2026. "
                    "Annual growth computed from FY product revenue. Retrieved 2026-11-01.")
    return save(fig, "ch26_snowflake_growth_vs_nrr")


def margin_bridge(f):
    periods = ["FY2025", "FY2026", "Q2 FY2027"]
    gaap = _sf(f, "gaap_operating_margin_pct")
    ng = _sf(f, "non_gaap_operating_margin_pct")
    fcf = _sf(f, "non_gaap_fcf_margin_pct")
    sbc = _sf(f, "sbc_expense")
    rev = _sf(f, "total_revenue")
    sbc_pct = {p: sbc[p] / rev[p] * 100 for p in periods if p in sbc.index and p in rev.index}
    metrics = [
        ("GAAP operating margin", [gaap.get(p, np.nan) for p in periods], PALETTE["grey"]),
        ("Non-GAAP operating margin", [ng.get(p, np.nan) for p in periods], PALETTE["blue"]),
        ("Non-GAAP adjusted FCF margin", [fcf.get(p, np.nan) for p in periods], PALETTE["green"]),
        ("Stock-based comp, % of total revenue (GAAP)", [sbc_pct.get(p, np.nan) for p in periods], PALETTE["vermillion"]),
    ]
    fig, ax = plt.subplots(figsize=(10, 5.2))
    x = np.arange(len(periods))
    w = 0.2
    for i, (lab, vals, col) in enumerate(metrics):
        xs = x + (i - 1.5) * w
        vals_plot = [0 if np.isnan(v) else v for v in vals]
        ax.bar(xs, vals_plot, w, color=col, label=lab)
        for xi, v in zip(xs, vals):
            txt = "n/a" if np.isnan(v) else f"{v:.1f}%"
            y = 0 if np.isnan(v) else v
            ax.text(xi, y + (1.5 if y >= 0 else -4.5), txt, ha="center", fontsize=7.5)
    ax.axhline(0, color=PALETTE["black"], linewidth=0.8)
    ax.set_xticks(x)
    ax.set_xticklabels(["FY2025\n(Feb 2024-Jan 2025)", "FY2026\n(Feb 2025-Jan 2026)", "Q2 FY2027\n(May-Jul 2026)"])
    ax.set_ylabel("Percent of total revenue")
    ax.set_ylim(-48, 50)
    ax.set_title("Snowflake: GAAP losses, non-GAAP profits; stock comp is most of the gap")
    ax.legend(fontsize=8, frameon=False, loc="upper left", ncol=2)
    source_note(ax, "Source: data/company_financials.csv (Snowflake 10-K FY2026 for SBC; Q4 FY2026 and Q2 FY2027 releases for margins). "
                    "SBC % = GAAP stock-based compensation / GAAP total revenue (author arithmetic). n/a = not in dataset. "
                    "Q2 FCF margin is seasonally low; FY2027 guide is 23%. Retrieved 2026-11-01.")
    return save(fig, "ch26_snowflake_margin_bridge")


def make():
    f = load("company_financials")
    return [growth_vs_nrr(f), margin_bridge(f)]
