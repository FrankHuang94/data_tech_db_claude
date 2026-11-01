"""Ch 37: median EV/NTM revenue by peer group, with each company shown as a dot.

Reads data/public_comps.csv. Groups are an editorial assignment (see GROUPS below and
meta/staging/ch37-decisions.md). Acquired companies (Confluent) and Domo (asset sale
pending; listed multiple not meaningful) are excluded from the medians.
"""
from chartlib import load, num, save, source_note, PALETTE, plt

GROUPS = {
    "Cloud data & analytics platforms": ["SNOW", "PLTR", "TDC", "AI"],
    "Operational database": ["MDB"],
    "Observability & search": ["DDOG", "ESTC", "DT"],
    "Application platforms with data layers": ["CRM", "NOW", "SAP", "WDAY", "IBM", "GTLB"],
    "Hyperscalers (incl. Oracle)": ["MSFT", "AMZN", "GOOGL", "ORCL"],
    "Storage & infrastructure (incl. Everpure)": ["P", "NTAP", "NTNX"],
    "Data security & protection": ["VRNS", "RBRK", "CVLT"],
}
CAP = 30  # x-axis cap; values above are annotated at the edge


def make():
    c = load("public_comps")
    c["tk"] = c["ticker"].astype(str).str.split(" ").str[0]
    c["mult"] = num(c["ev_ntm_revenue"])
    rows = []
    for g, tks in GROUPS.items():
        sub = c[c["tk"].isin(tks) & c["mult"].notna()]
        rows.append((g, sub["mult"].median(), sub[["tk", "mult"]].values.tolist()))
    rows.sort(key=lambda r: r[1])
    fig, ax = plt.subplots(figsize=(11, 7))
    for i, (g, med, members) in enumerate(rows):
        color = PALETTE["vermillion"] if "Everpure" in g else PALETTE["blue"]
        ax.barh(i, med, color=color, alpha=0.35, height=0.6)
        ax.text(CAP + 0.8, i, f"median {med:.1f}x (n={len(members)})", fontsize=8, va="center", ha="left")
        for j, (tk, m) in enumerate(sorted(members, key=lambda t: t[1])):
            x = min(m, CAP)
            dot = PALETTE["vermillion"] if tk == "P" else PALETTE["black"]
            ax.plot(x, i, "o", color=dot, ms=5)
            label = f"{tk} {m:.1f}x" + (" →" if m > CAP else "")
            dy = [-11, 6, -20, 15][j % 4]
            ax.annotate(label, (x, i), xytext=(-4 if m > CAP else 2, dy), textcoords="offset points",
                        fontsize=6.5, ha="right" if m > CAP else "left", color=PALETTE["grey"])
    ax.set_yticks(range(len(rows)), [r[0] for r in rows], fontsize=9)
    ax.set_xlim(0, CAP + 1)
    ax.set_xlabel("EV / NTM revenue (x)  — bar = group median, dots = companies (axis capped at 30x)")
    ax.set_title("Median EV/NTM revenue by peer group, data and infrastructure comps")
    asof = c.loc[c["tk"].isin(sum(GROUPS.values(), [])), "as_of"].dropna()
    source_note(ax, f"Source: data/public_comps.csv (market data {asof.min()} to {asof.max()}; NTM mostly FY-guidance proxies, "
                    "some TTM — see ntm_revenue_basis). Groups are the author's assignment. Excludes Confluent (acquired) and Domo (asset sale).")
    return save(fig, "ch37_multiples_by_group")
