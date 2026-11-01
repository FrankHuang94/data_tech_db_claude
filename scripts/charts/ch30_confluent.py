"""Ch 30: Confluent GAAP revenue FY2019-FY2025 with Confluent Cloud revenue and YoY growth (data/ch30_confluent_financials.csv)."""
from chartlib import load, num, save, source_note, PALETTE, plt


def make():
    d = load("ch30_confluent_financials")
    d["v"] = num(d["value_usd_m"])
    d["g"] = num(d["growth_yoy_pct"])
    tot = d[d["metric"] == "total_revenue"].sort_values("fiscal_year").reset_index(drop=True)
    cloud = d[d["metric"] == "cloud_revenue"].set_index("fiscal_year")["v"]
    years = list(tot["fiscal_year"])
    x = range(len(years))

    fig, ax = plt.subplots(figsize=(10, 5.4))
    ax.bar(x, tot["v"], color=PALETTE["sky"], width=0.62, label="Total revenue (GAAP)")
    cl = [cloud.get(y) for y in years]
    cl_x = [i for i, v in zip(x, cl) if v == v and v is not None]
    cl_v = [v for v in cl if v == v and v is not None]
    ax.bar(cl_x, cl_v, color=PALETTE["blue"], width=0.62,
           label="of which Confluent Cloud (FY2024 derived from FY2025 growth)")
    for i, r in tot.iterrows():
        ax.annotate(f"${r['v']:,.0f}M", (i, r["v"]), xytext=(0, 4), textcoords="offset points",
                    ha="center", fontsize=8.5)
    for i, v in zip(cl_x, cl_v):
        share = v / tot.loc[i, "v"] * 100
        ax.annotate(f"Cloud\n{share:.0f}%", (i, v / 2), ha="center", va="center", fontsize=8, color="white")
    ax.set_xticks(list(x))
    ax.set_xticklabels([y.replace("FY", "FY ") for y in years])
    ax.set_ylabel("US$ millions (GAAP, fiscal year = calendar year)")
    ax.set_ylim(0, 1400)

    ax2 = ax.twinx()
    g = tot.dropna(subset=["g"])
    ax2.plot(list(g.index), g["g"], color=PALETTE["vermillion"], marker="o", linewidth=2, label="Revenue growth YoY (%)")
    for i, r in g.iterrows():
        ax2.annotate(f"{r['g']:.0f}%", (i, r["g"]), xytext=(6, 4), textcoords="offset points", fontsize=8,
                     color=PALETTE["vermillion"])
    ax2.set_ylim(0, 80)
    ax2.set_ylabel("YoY growth (%)", color=PALETTE["vermillion"])
    ax2.grid(False)
    ax2.spines["right"].set_visible(True)

    h1, l1 = ax.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax.legend(h1 + h2, l1 + l2, fontsize=8, frameon=False, loc="upper left")
    ax.set_title("Confluent revenue and growth, FY2019–FY2025 (GAAP; acquired by IBM 2026-03-17)")
    source_note(ax, "Source: data/ch30_confluent_financials.csv (Confluent S-1/10-K filings, SEC EDGAR CIK 1699838). "
                    "FY2019–FY2024 totals recalled from filings and flagged [VERIFY]; FY2025 per Confluent FY2025 10-K (total $1,166.7M GAAP; Cloud $624M); "
                    "FY2024 Cloud revenue derived from stated FY2025 Cloud growth of 27%. Retrieved 2026-11-01.")
    return [save(fig, "ch30_confluent")]
