"""M&A charts from data/ma_deals.csv: deals per year by category group, disclosed value by year, top-deal timeline."""
from chartlib import load, num, save, source_note, PALETTE, SERIES, plt
import pandas as pd

GROUPS = {
    "AI": ["vector/AI data", "AI talent/acquihire", "acquihire/AI"],
    "Databases & warehouses": ["database", "Postgres/operational DB", "data warehouse/analytics", "Hadoop/big data", "table format/catalog", "search"],
    "Pipelines & streaming": ["data integration", "streaming", "modern data stack consolidation"],
    "Governance & security": ["data security/DSPM", "governance/catalog", "data quality/governance", "security analytics"],
    "Analytics, BI & observability": ["BI", "observability", "ad/marketing data", "data marketplace"],
    "PE, app-vendor & other": ["PE take-private", "application-vendor data layer", "storage-adjacent data", "open-source infrastructure"],
}


def group(cat: str) -> str:
    for g, cats in GROUPS.items():
        if cat in cats:
            return g
    return "PE, app-vendor & other"


def make():
    d = load("ma_deals")
    d["year"] = d["date"].astype(str).str[:4].astype(int)
    d["group"] = d["category"].fillna("").map(group)
    d["value"] = num(d["value_usd_m"])
    outs = []

    # 1. Deal count by year, stacked by group
    pv = d.pivot_table(index="year", columns="group", values="target", aggfunc="count", fill_value=0)
    pv = pv.reindex(range(d.year.min(), d.year.max() + 1), fill_value=0)
    fig, ax = plt.subplots(figsize=(10, 5))
    bottom = None
    for i, g in enumerate(GROUPS):
        if g not in pv:
            continue
        ax.bar(pv.index, pv[g], bottom=bottom, label=g, color=SERIES[i % len(SERIES)])
        bottom = pv[g] if bottom is None else bottom + pv[g]
    ax.set_title("Data-infrastructure M&A in the atlas dataset: deals per year by category")
    ax.set_ylabel("Number of deals in dataset")
    ax.legend(fontsize=8, frameon=False, ncol=2)
    source_note(ax, f"Source: data/ma_deals.csv ({len(d)} curated deals, announcement year; not an exhaustive census). Retrieved 2026-11-01.")
    outs.append(save(fig, "ma_deals_per_year"))

    # 2. Disclosed/press-reported value by year
    v = d[d["value"].notna()].groupby("year")["value"].sum() / 1000
    v = v.reindex(range(d.year.min(), d.year.max() + 1), fill_value=0)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(v.index, v.values, color=PALETTE["blue"])
    ax.set_title("Disclosed or press-reported deal value by announcement year (US$B)")
    ax.set_ylabel("US$ billions (sum of deals with a value)")
    for x, y in v.items():
        if y > 0:
            ax.text(x, y, f"{y:.0f}", ha="center", va="bottom", fontsize=7)
    source_note(ax, "Source: data/ma_deals.csv; only deals with disclosed or press-reported values; mixes equity and enterprise values (see value_basis).")
    outs.append(save(fig, "ma_value_per_year"))

    # 3. Timeline of largest deals
    top = d[d["value"].notna()].nlargest(22, "value").copy()
    top["dt"] = pd.to_datetime(top["date"], errors="coerce")
    fig, ax = plt.subplots(figsize=(11, 6))
    cols = {g: SERIES[i % len(SERIES)] for i, g in enumerate(GROUPS)}
    for g, sub in top.groupby("group"):
        ax.scatter(sub["dt"], sub["value"] / 1000, s=(sub["value"] / 1000) * 12 + 20, alpha=0.75, color=cols[g], label=g, edgecolor="white")
    import re
    from matplotlib.ticker import FuncFormatter
    def short(s):
        s = re.split(r" and | & |;|,", str(s))[0]
        return re.sub(r" (Software|Technologies|Partners|Capital|Equity Partners|Networks|funds)\b.*", "", s).strip()
    for _, r in top.iterrows():
        ax.annotate(f"{short(r['acquirer'])}–{short(re.sub(r' [(].*', '', str(r['target'])))}", (r["dt"], r["value"] / 1000), fontsize=6.5, xytext=(4, 4), textcoords="offset points")
    ax.set_yscale("log")
    ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f"${y:g}B"))
    ax.yaxis.set_minor_formatter(FuncFormatter(lambda y, _: ""))
    ax.set_ylabel("Deal value, US$B (log scale)")
    ax.set_title("The largest data-infrastructure deals, 2010–2026")
    ax.legend(fontsize=7.5, frameon=False, loc="upper left", markerscale=0.5)
    source_note(ax, "Source: data/ma_deals.csv (disclosed or press-reported values). Bubble size ∝ value.")
    outs.append(save(fig, "ma_top_deals_timeline"))
    return outs
