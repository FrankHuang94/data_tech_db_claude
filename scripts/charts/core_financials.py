"""Company financial charts from data/company_financials.csv."""
from chartlib import load, num, save, source_note, PALETTE, plt
import pandas as pd


def series(f, company, metric, annual=True):
    s = f[(f["company"].str.startswith(company)) & (f["metric"] == metric)].copy()
    s["v"] = num(s["value"])
    is_fy = s["fiscal_period"].astype(str).str.match(r"^FY\d{4}$")
    s = s[is_fy] if annual else s[~is_fy]
    return s.drop_duplicates("fiscal_period").sort_values("period_end")


def make():
    f = load("company_financials")
    outs = []

    # Snowflake product revenue + growth
    s = series(f, "Snowflake", "product_revenue")
    if len(s):
        fig, ax = plt.subplots(figsize=(9, 5))
        ax.bar(s["fiscal_period"], s["v"] / 1000, color=PALETTE["sky"])
        g = s["v"].pct_change() * 100
        for x, y, gr in zip(s["fiscal_period"], s["v"] / 1000, g):
            ax.text(x, y, f"${y:.2f}B" + ("" if pd.isna(gr) else f"\n+{gr:.0f}%"), ha="center", va="bottom", fontsize=7.5)
        ax.set_title("Snowflake product revenue by fiscal year (GAAP, US$B)")
        ax.set_ylabel("US$ billions")
        source_note(ax, "Source: data/company_financials.csv (Snowflake 10-K / earnings releases). FY ends Jan 31: FY2026 = Feb 2025–Jan 2026.")
        outs.append(save(fig, "snowflake_product_revenue"))

    # Snowflake NRR (all periods)
    n = f[(f["company"] == "Snowflake") & (f["metric"] == "nrr_pct")].copy()
    n["v"] = num(n["value"])
    n = n.drop_duplicates("fiscal_period").sort_values("period_end")
    if len(n):
        fig, ax = plt.subplots(figsize=(9, 4.5))
        ax.plot(n["fiscal_period"], n["v"], marker="o", color=PALETTE["blue"])
        for x, y in zip(n["fiscal_period"], n["v"]):
            ax.annotate(f"{y:.0f}%", (x, y), fontsize=7.5, xytext=(0, 6), textcoords="offset points", ha="center")
        ax.set_title("Snowflake net revenue retention rate (company-reported, trailing 12 months)")
        ax.set_ylabel("NRR, %")
        plt.setp(ax.get_xticklabels(), rotation=30, ha="right")
        source_note(ax, "Source: data/company_financials.csv (Snowflake earnings releases / 10-K). Period labels are fiscal (FY ends Jan 31).")
        outs.append(save(fig, "snowflake_nrr"))

    # Snowflake RPO
    r = f[(f["company"] == "Snowflake") & (f["metric"] == "rpo")].copy()
    r["v"] = num(r["value"])
    r = r.drop_duplicates("fiscal_period").sort_values("period_end")
    if len(r):
        fig, ax = plt.subplots(figsize=(9, 4.5))
        div = 1000 if r["v"].max() > 200 else 1
        ax.bar(r["fiscal_period"], r["v"] / div, color=PALETTE["orange"])
        ax.set_title("Snowflake remaining performance obligations (GAAP, US$B)")
        ax.set_ylabel("US$ billions")
        plt.setp(ax.get_xticklabels(), rotation=30, ha="right")
        source_note(ax, "Source: data/company_financials.csv (Snowflake 10-K/10-Q).")
        outs.append(save(fig, "snowflake_rpo"))

    # MongoDB total revenue
    m = series(f, "MongoDB", "total_revenue")
    if len(m):
        fig, ax = plt.subplots(figsize=(9, 4.5))
        ax.bar(m["fiscal_period"], m["v"] / 1000, color=PALETTE["green"])
        g = m["v"].pct_change() * 100
        for x, y, gr in zip(m["fiscal_period"], m["v"] / 1000, g):
            ax.text(x, y, f"${y:.2f}B" + ("" if pd.isna(gr) else f"\n+{gr:.0f}%"), ha="center", va="bottom", fontsize=7.5)
        ax.set_title("MongoDB total revenue by fiscal year (GAAP, US$B)")
        ax.set_ylabel("US$ billions")
        source_note(ax, "Source: data/company_financials.csv. MongoDB FY ends Jan 31: FY2026 = Feb 2025–Jan 2026.")
        outs.append(save(fig, "mongodb_revenue"))
    return outs
