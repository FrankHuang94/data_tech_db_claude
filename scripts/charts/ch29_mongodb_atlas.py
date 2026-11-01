"""Ch 29: MongoDB quarterly GAAP revenue and YoY growth (data/ch29_mongodb_quarterly.csv)."""
from chartlib import load, num, save, source_note, PALETTE, plt


ORDER = [f"Q{q} FY{y}" for y in (2024, 2025, 2026, 2027) for q in (1, 2, 3, 4)][:14]  # through Q2 FY2027


def make():
    d = load("ch29_mongodb_quarterly")
    d = d[d["metric"] == "total_revenue"].copy()
    d["v"] = num(d["value"])
    vals = dict(zip(d["fiscal_period"], d["v"]))
    xs = list(range(len(ORDER)))
    fig, ax = plt.subplots(figsize=(10, 5.2))
    heights = [vals.get(p, 0) for p in ORDER]
    colors = [PALETTE["green"] if p in vals else PALETTE["grey"] for p in ORDER]
    ax.bar(xs, heights, color=colors, width=0.7)
    for x, p in zip(xs, ORDER):
        if p in vals:
            ax.text(x, vals[p] + 8, f"${vals[p]:.0f}M", ha="center", va="bottom", fontsize=7.5)
        else:
            ax.text(x, 20, "not in\ndataset", ha="center", va="bottom", fontsize=7, color=PALETTE["grey"])
    ax.set_xticks(xs)
    ax.set_xticklabels([p.replace(" ", "\n") for p in ORDER], fontsize=8)
    ax.set_ylabel("Quarterly total revenue, US$ millions (GAAP)")
    ax.set_ylim(0, 900)

    # YoY growth: same quarter, prior fiscal year
    ax2 = ax.twinx()
    gx, gy = [], []
    for x, p in zip(xs, ORDER):
        q, fy = p.split(" ")
        prior = f"{q} FY{int(fy[2:]) - 1}"
        if p in vals and prior in vals:
            gx.append(x)
            gy.append((vals[p] / vals[prior] - 1) * 100)
    ax2.plot(gx, gy, color=PALETTE["vermillion"], marker="o", linewidth=2, label="YoY growth (right axis)")
    for x, y in zip(gx, gy):
        ax2.annotate(f"{y:.0f}%", (x, y), xytext=(0, 7), textcoords="offset points", ha="center", fontsize=8,
                     color=PALETTE["vermillion"])
    ax2.set_ylim(0, 45)
    ax2.set_ylabel("YoY revenue growth, %", color=PALETTE["vermillion"])
    ax2.spines["right"].set_visible(True)
    ax2.grid(False)
    ax2.legend(loc="upper left", frameon=False, fontsize=8)
    ax.set_title("MongoDB quarterly revenue and growth, Q1 FY2024 to Q2 FY2027 (FY ends Jan 31)")
    source_note(ax, "Source: data/ch29_mongodb_quarterly.csv (MongoDB quarterly earnings releases, 8-K; GAAP). "
                    "Q2 FY2027 = May-Jul 2026. Q1 FY2027 (Feb-Apr 2026) not yet in the dataset. Growth computed vs the "
                    "same quarter a year earlier. Pre-FY2026 Q4 quarters not live-fetched; they reconcile to 10-K annual totals. "
                    "Retrieved 2026-11-01.")
    return [save(fig, "ch29_mongodb_atlas")]
