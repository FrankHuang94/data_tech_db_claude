"""Ch 39: deal count and disclosed value by category group, from data/ma_deals.csv.

Left panel: number of deals per category group, split by value basis
(disclosed / press-reported / undisclosed). Right panel: sum of deal values
that are disclosed or press-reported, per group (US$B). Corrections staged in
data/staging/ch39-ma_deals.csv (rows whose outcome starts with CORRECTION) are
applied on acquirer+target before plotting, if that file exists.
"""
from chartlib import DATA, load, num, save, source_note, PALETTE, plt

GROUPS = {
    "Databases & engines": ["database", "Postgres/operational DB", "data warehouse/analytics", "Hadoop/big data",
                            "search", "analytical engine"],
    "Formats, catalogs & quality": ["table format/catalog", "governance/catalog", "data quality/governance",
                                    "data quality"],
    "Pipelines, streaming & MDS": ["data integration", "streaming", "modern data stack consolidation", "orchestration"],
    "AI data, models & talent": ["vector/AI data", "AI talent/acquihire", "acquihire/AI", "ML platform"],
    "Data security & DSPM": ["data security/DSPM", "security analytics", "AI security"],
    "Observability & BI": ["observability", "BI", "ad/marketing data", "data marketplace"],
    "PE take-privates": ["PE take-private"],
    "App-vendor, storage & infra": ["application-vendor data layer", "storage-adjacent data",
                                    "open-source infrastructure", "infrastructure automation"],
}


def group(cat: str) -> str:
    for g, cats in GROUPS.items():
        if cat in cats:
            return g
    return "App-vendor, storage & infra"


def deals():
    d = load("ma_deals")
    stage = DATA / "staging" / "ch39-ma_deals.csv"
    if stage.exists():
        s = load("staging/ch39-ma_deals.csv")
        for _, r in s[s["outcome"].astype(str).str.startswith("CORRECTION")].iterrows():
            m = (d["acquirer"] == r["acquirer"]) & (d["target"] == r["target"])
            for col in ("date", "value_usd_m", "value_basis", "status"):
                d.loc[m, col] = r[col]
    d["group"] = d["category"].fillna("").map(group)
    d["value"] = num(d["value_usd_m"])
    return d


def make():
    d = deals()
    order = list(GROUPS)
    counts = d.pivot_table(index="group", columns="value_basis", values="target", aggfunc="count", fill_value=0)
    counts = counts.reindex(order, fill_value=0)
    value = (d[d["value"].notna()].groupby("group")["value"].sum() / 1000).reindex(order, fill_value=0)

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(12, 5.5), sharey=True)
    y = range(len(order))
    left = [0] * len(order)
    for basis, col in (("disclosed", PALETTE["blue"]), ("press-reported", PALETTE["sky"]),
                       ("undisclosed", PALETTE["grey"])):
        vals = counts[basis] if basis in counts else [0] * len(order)
        a1.barh(list(y), vals, left=left, color=col, label=basis, alpha=0.9 if basis != "undisclosed" else 0.5)
        left = [l + v for l, v in zip(left, vals)]
    for i, tot in enumerate(left):
        a1.text(tot + 0.3, i, str(int(tot)), va="center", fontsize=8)
    a1.set_yticks(list(y))
    a1.set_yticklabels(order)
    a1.invert_yaxis()
    a1.set_xlabel("Number of deals in dataset")
    a1.set_title("Deal count by category group and value basis")
    a1.legend(fontsize=8, frameon=False, loc="lower right")

    a2.barh(list(y), value.values, color=PALETTE["orange"])
    for i, v in enumerate(value.values):
        a2.text(v + 0.5, i, f"${v:.0f}B", va="center", fontsize=8)
    a2.set_xlabel("US$B, sum of disclosed + press-reported values")
    a2.set_title("Value where a number exists")
    source_note(a1, f"Source: data/ma_deals.csv ({len(d)} curated deals, 2010–Oct 2026; ch39 staged corrections applied). "
                    "Not an exhaustive census; values mix equity and enterprise value and exclude undisclosed deals. "
                    "Retrieved 2026-11-01.")
    fig.tight_layout()
    return [save(fig, "ch39_deals_by_category")]
