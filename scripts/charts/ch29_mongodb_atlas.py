"""Ch 29: MongoDB quarterly GAAP revenue and YoY growth (data/ch29_mongodb_quarterly.csv)."""
from chartlib import load, num, save, source_note, PALETTE, plt


ORDER = [f"Q{q} FY{y}" for y in (2024, 2025, 2026, 2027) for q in (1, 2, 3, 4)][:14]  # through Q2 FY2027


def make():
    d = load("ch29_mongodb_quarterly")
    d = d[d["metric"] == "total_revenue"].copy()
    d["v"] = num(d["value"])
    vals = dict(zip(d["fiscal_period"], d["v"]))
    xs = list(range(len(ORDER)))
    fig, (ax, ax2) = plt.subplots(2, 1, figsize=(10, 6.4), sharex=True, gridspec_kw={"height_ratios": [2.2, 1]})
    heights = [vals.get(p, 0) for p in ORDER]
    ax.bar(xs, heights, color=PALETTE["green"], width=0.7)
    for x, p in zip(xs, ORDER):
        if p in vals:
            ax.text(x, vals[p] + 8, f"${vals[p]:.0f}M", ha="center", va="bottom", fontsize=7.5)
        else:
            ax.text(x, 20, "not in\ndataset", ha="center", va="bottom", fontsize=7, color=PALETTE["grey"])
    ax.set_ylabel("Revenue, US$M (GAAP)")
    ax.set_ylim(0, 900)

    # YoY growth: same quarter, prior fiscal year; break the line where a quarter is missing
    gx, gy = [], []
    for x, p in zip(xs, ORDER):
        q, fy = p.split(" ")
        prior = f"{q} FY{int(fy[2:]) - 1}"
        if p in vals and prior in vals:
            gx.append(x)
            gy.append((vals[p] / vals[prior] - 1) * 100)
        else:
            gx.append(x)
            gy.append(float("nan"))
    ax2.plot(gx, gy, color=PALETTE["vermillion"], marker="o", linewidth=2)
    for x, y in zip(gx, gy):
        if y == y:
            ax2.annotate(f"{y:.1f}%", (x, y), xytext=(0, 7), textcoords="offset points", ha="center", fontsize=7.5,
                         color=PALETTE["vermillion"])
    ax2.set_ylim(0, 40)
    ax2.set_ylabel("YoY growth, %")
    ax2.set_xticks(xs)
    ax2.set_xticklabels([p.replace(" ", "\n") for p in ORDER], fontsize=8)
    ax.set_title("MongoDB quarterly revenue (top) and YoY growth (bottom), Q1 FY2024 to Q2 FY2027 (FY ends Jan 31)")
    source_note(ax, "Source: data/ch29_mongodb_quarterly.csv (MongoDB quarterly earnings releases, 8-K; GAAP). "
                    "Q2 FY2027 = May-Jul 2026. Q1 FY2027 (Feb-Apr 2026) not yet in the dataset. Growth computed vs the "
                    "same quarter a year earlier. Quarters before Q4 FY2026 were not live-fetched; they reconcile to 10-K annual totals. "
                    "Retrieved 2026-11-01.")
    return [save(fig, "ch29_mongodb_atlas")]
