"""Ch 36: Rule of 40 scatter - latest revenue growth vs FCF margin (data/ch36_rule_of_40.csv)."""
import numpy as np

from chartlib import load, num, save, source_note, PALETTE, plt

OFFSETS = {"NTNX": (-62, -14), "ESTC": (6, 4), "SNOW": (9, -5), "DDOG": (6, 5), "P": (6, -12), "RBRK": (6, 5),
           "MDB": (-62, -14), "NTAP": (-62, 5)}
HIGHLIGHT = {"SNOW": PALETTE["blue"], "MDB": PALETTE["green"], "P": PALETTE["vermillion"]}


def make():
    d = load("ch36_rule_of_40")
    d["g"] = num(d["revenue_growth_yoy_pct"])
    d["f"] = num(d["fcf_margin_pct"])
    fig, ax = plt.subplots(figsize=(10, 6.2))

    xs = np.linspace(-5, 100, 50)
    ax.plot(xs, 40 - xs, color=PALETTE["grey"], linestyle="--", linewidth=1.3)
    ax.fill_between(xs, 40 - xs, 75, color=PALETTE["green"], alpha=0.06)
    ax.text(3, 40, "Rule of 40 line\n(growth + FCF margin = 40)", fontsize=8, color=PALETTE["grey"], va="bottom")

    markers = {"quarter": "o", "full-year": "s"}
    for basis, mk in markers.items():
        sub = d[d["fcf_basis_type"] == basis]
        cols = [HIGHLIGHT.get(t, PALETTE["orange"]) for t in sub["ticker"]]
        ax.scatter(sub["g"], sub["f"], s=70, marker=mk, c=cols, edgecolor="black", linewidth=0.5, zorder=3)
    for _, r in d.iterrows():
        label = f"{r['ticker']} ({r['rule_of_40']:.0f})"
        ax.annotate(label, (r["g"], r["f"]), xytext=OFFSETS.get(r["ticker"], (6, 4)), textcoords="offset points", fontsize=8.5,
                    color=HIGHLIGHT.get(r["ticker"], "black"),
                    fontweight="bold" if r["ticker"] in HIGHLIGHT else "normal")

    # legend proxies for FCF basis
    ax.scatter([], [], marker="o", c="white", edgecolor="black", label="FCF margin = latest reported quarter")
    ax.scatter([], [], marker="s", c="white", edgecolor="black", label="FCF margin = full-year guide or full-year actual")
    ax.legend(loc="lower right", fontsize=8, frameon=False)
    ax.set_xlim(0, 100)
    ax.set_ylim(-2, 70)
    ax.set_xlabel("Revenue growth, % YoY (GAAP total revenue, latest reported quarter; Nutanix = FY2026)")
    ax.set_ylabel("Free cash flow margin, % (non-GAAP; company definitions)")
    ax.set_title("Rule of 40: revenue growth vs FCF margin, data and infrastructure software comps (score in brackets)")
    source_note(ax, "Source: data/ch36_rule_of_40.csv, compiled from company earnings releases (quarters ending Jun-Aug 2026; "
                    "ServiceNow Q3 2026). FCF definitions differ: Snowflake/Palantir/Elastic/GitLab use 'adjusted' FCF. "
                    "Everpure FCF margin is an estimate (FY2027 FCF guide midpoint / revenue guide midpoint). "
                    "NetApp growth includes an extra week. Retrieved 2026-11-01.")
    return [save(fig, "ch36_rule_of_40")]
