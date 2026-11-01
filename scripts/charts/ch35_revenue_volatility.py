"""Ch 35: same customer, three business models -- illustrative quarterly revenue (data/ch35_illustrative_revenue.csv).

Illustrative author model, not company data. Assumptions are documented in the chapter's worked example
and in meta/staging/ch35-decisions.md.
"""
from chartlib import load, num, save, source_note, PALETTE, plt

MODELS = [
    ("subscription", "(a) Subscription, \\$500K/yr recognised ratably", PALETTE["blue"], "-", "s"),
    ("consumption", "(b) Pure consumption, 30%/yr usage growth, one 20% optimization", PALETTE["orange"], "-", "o"),
    ("capacity_commit_overage", "(c) Capacity commit (ratable floor) plus overage", PALETTE["green"], "--", "^"),
]


def make():
    d = load("ch35_illustrative_revenue")
    d["v"] = num(d["revenue_usd_k"])
    quarters = list(dict.fromkeys(d["quarter"]))
    xs = list(range(len(quarters)))
    fig, ax = plt.subplots(figsize=(10, 6.4))
    fig.subplots_adjust(bottom=0.27)
    for key, label, color, ls, marker in MODELS:
        s = d[d["model"] == key].set_index("quarter").reindex(quarters)["v"]
        y1, y2 = s.iloc[:4].sum(), s.iloc[4:].sum()
        ax.plot(xs, s.values, color=color, linestyle=ls, marker=marker, linewidth=2.2,
                label=f"{label}  [Y1 \\${y1:,.0f}K, Y2 \\${y2:,.0f}K]")
    cons = d[d["model"] == "consumption"].set_index("quarter").reindex(quarters)["v"]
    ax.annotate("Optimization event:\nusage level reset -20%", xy=(4, cons.iloc[4]), xytext=(4.25, 106),
                fontsize=8.5, color=PALETTE["vermillion"],
                arrowprops=dict(arrowstyle="->", color=PALETTE["vermillion"]))
    ax.annotate("Holiday quarter:\n-4% seasonal dip", xy=(3, cons.iloc[3]), xytext=(2.0, 109),
                fontsize=8.5, color=PALETTE["grey"], arrowprops=dict(arrowstyle="->", color=PALETTE["grey"]))
    ax.axvline(3.5, color=PALETTE["grey"], linewidth=0.8, linestyle=":")
    ax.text(3.55, 100.5, "renewal", fontsize=8, color=PALETTE["grey"])
    ax.set_xticks(xs)
    ax.set_xticklabels(quarters)
    ax.set_ylim(98, 142)
    ax.set_ylabel("Vendor revenue recognised in quarter, US$K (illustrative)")
    ax.set_title("ILLUSTRATIVE: one customer, three business models -- quarterly revenue to the vendor")
    fig.legend(loc="lower center", bbox_to_anchor=(0.5, 0.01), ncol=1, fontsize=8.5, frameon=False)
    source_note(ax, "Source: data/ch35_illustrative_revenue.csv (author model, as of 2026-11-01; basis = illustrative, not company data). "
                    "Assumptions: consumption sized so Y1 trend spend = \\$500K, grows 30%/yr (6.8%/qtr), dips 4% in each holiday quarter, and "
                    "resets 20% lower at the start of Y2 after an optimization project. Model (c): reserve commit of \\$480K (Y1) and \\$500K (Y2), "
                    "recognised ratably as a floor; usage above the quarterly floor billed as overage at the same unit price.")
    return [save(fig, "ch35_revenue_volatility")]
