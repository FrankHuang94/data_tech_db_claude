"""Ch 27: Databricks company-stated run-rate vs Snowflake annualized GAAP product revenue (different bases)."""
from chartlib import load, num, save, source_note, PALETTE, plt
import pandas as pd


def _snowflake():
    f = load("company_financials")
    f = f[(f["company"] == "Snowflake") & (f["metric"] == "product_revenue")].copy()
    f["dt"] = pd.to_datetime(f["period_end"], errors="coerce")
    f["v"] = num(f["value"]) / 1000.0  # USD_m -> USD_b
    quarterly = f[f["fiscal_period"].str.startswith("Q")].sort_values("dt").copy()
    quarterly["annualized"] = quarterly["v"] * 4
    annual = f[f["fiscal_period"].str.match(r"^FY\d{4}$")].sort_values("dt")
    return quarterly, annual


def make():
    d = load("ch25_databricks_runrate")
    d["dt"] = pd.to_datetime(d["date"], errors="coerce")
    d["v"] = num(d["value_usd_b"])
    db_rr = d[d["metric"] == "total_run_rate"].sort_values("dt")
    db_fy = d[d["metric"] == "fiscal_year_revenue"].sort_values("dt")
    sf_q, sf_fy = _snowflake()
    sf_fy = sf_fy[sf_fy["dt"] >= pd.Timestamp("2021-01-01")]

    fig, ax = plt.subplots(figsize=(10, 5.6))
    ax.plot(db_rr["dt"], db_rr["v"], marker="o", linewidth=2.2, color=PALETTE["orange"],
            label="Databricks: company-stated revenue run-rate (floor, unaudited)")
    ax.scatter(db_fy["dt"], db_fy["v"], s=60, facecolors="none", edgecolors=PALETTE["orange"], linewidths=1.6,
               label="Databricks: company-stated fiscal-year revenue (press-reported)", zorder=3)
    ax.plot(sf_q["dt"], sf_q["annualized"], marker="s", linewidth=2.2, color=PALETTE["blue"],
            label="Snowflake: 4 x quarterly GAAP product revenue (our annualization)")
    ax.scatter(sf_fy["dt"], sf_fy["v"], s=60, marker="D", facecolors="none", edgecolors=PALETTE["blue"],
               linewidths=1.6, label="Snowflake: fiscal-year GAAP product revenue", zorder=3)
    for _, r in db_rr.tail(3).iterrows():
        ax.annotate(f"${r['v']:.1f}B", (r["dt"], r["v"]), xytext=(-30, 8), textcoords="offset points",
                    fontsize=8, color=PALETTE["orange"])
    for _, r in sf_q.iterrows():
        ax.annotate(f"${r['annualized']:.2f}B", (r["dt"], r["annualized"]), xytext=(6, -14),
                    textcoords="offset points", fontsize=8, color=PALETTE["blue"])
    for _, r in sf_fy.iterrows():
        ax.annotate(f"FY ${r['v']:.2f}B", (r["dt"], r["v"]), xytext=(6, -12), textcoords="offset points",
                    fontsize=7.5, color=PALETTE["grey"])
    ax.set_ylim(0, 8)
    ax.set_ylabel("US$ billions (annualized or fiscal-year)")
    ax.set_title("Databricks run-rate vs Snowflake product revenue: different bases, same Jan-31 fiscal calendar")
    ax.legend(fontsize=8, frameon=False, loc="upper left")
    source_note(ax, "Sources: data/ch25_databricks_runrate.csv (Databricks press releases; CNBC, Bloomberg, TechCrunch); "
                    "data/company_financials.csv (Snowflake 10-K and earnings releases). NOT like-for-like: Databricks figures are "
                    "company-stated floors on an undisclosed run-rate definition and exclude cloud VM costs on classic compute; "
                    "Snowflake figures are GAAP product revenue (excludes professional services) that include cloud infrastructure "
                    "cost. Both fiscal years end Jan 31. Retrieved 2026-11-01.")
    return [save(fig, "ch27_growth_compare")]
