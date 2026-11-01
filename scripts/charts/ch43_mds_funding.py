"""Ch 43: modern-data-stack (MDS) category funding by year, from data/private_funding.csv.

Left panel: sum of disclosed round sizes (US$M) per year, stacked by MDS category.
Right panel: the latest priced post-money valuation per MDS company in the dataset,
coloured by the year it was set, to show how many marks date from the 2021-22 peak.

Category mapping (CSV category -> chart group):
  data integration, reverse ETL / data activation -> Integration and activation
  transformation                                  -> Transformation
  orchestration                                   -> Orchestration
  observability/quality                           -> Observability and quality
  catalog/governance                              -> Catalog and governance
  BI/analytics, semantic layer                    -> BI, analytics and semantics
Cribl is excluded: the CSV files it under observability/quality, but it sells IT and
security telemetry pipelines, not analytics-data observability (see ch43 decisions log).
Rows staged in data/staging/ch43-private_funding.csv are appended if that file exists.
"""
from chartlib import DATA, load, num, save, source_note, PALETTE, plt

GROUPS = {
    "Integration and activation": ["data integration", "reverse ETL / data activation"],
    "Transformation": ["transformation"],
    "Orchestration": ["orchestration"],
    "Observability and quality": ["observability/quality"],
    "Catalog and governance": ["catalog/governance"],
    "BI, analytics and semantics": ["BI/analytics", "semantic layer"],
}
COLORS = [PALETTE["blue"], PALETTE["orange"], PALETTE["green"], PALETTE["vermillion"], PALETTE["sky"],
          PALETTE["purple"]]
EXCLUDE = {"Cribl"}


def rounds():
    d = load("private_funding")
    stage = DATA / "staging" / "ch43-private_funding.csv"
    if stage.exists():
        import pandas as pd
        d = pd.concat([d, load("staging/ch43-private_funding.csv")], ignore_index=True)
    lookup = {c: g for g, cats in GROUPS.items() for c in cats}
    d["group"] = d["category"].map(lookup)
    d = d[d["group"].notna() & ~d["company"].isin(EXCLUDE)].copy()
    d["year"] = d["date"].astype(str).str[:4].astype(int)
    d["amount"] = num(d["amount_usd_m"])
    d["post"] = num(d["post_money_valuation_usd_b"])
    return d


def make():
    d = rounds()
    years = list(range(d["year"].min(), d["year"].max() + 1))
    pivot = d.pivot_table(index="year", columns="group", values="amount", aggfunc="sum", fill_value=0)
    pivot = pivot.reindex(index=years, columns=list(GROUPS), fill_value=0)
    counts = d.groupby("year")["company"].count().reindex(years, fill_value=0)

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13, 5.6), gridspec_kw={"width_ratios": [1.15, 1]})
    bottom = [0.0] * len(years)
    for g, col in zip(GROUPS, COLORS):
        vals = pivot[g].tolist()
        a1.bar([str(y) for y in years], vals, bottom=bottom, color=col, label=g)
        bottom = [b + v for b, v in zip(bottom, vals)]
    for i, (tot, n) in enumerate(zip(bottom, counts.tolist())):
        a1.text(i, tot + 15, f"${tot:,.0f}M\n{n} rounds", ha="center", fontsize=8)
    a1.set_ylabel("US$M, sum of disclosed round sizes")
    a1.set_ylim(0, max(bottom) * 1.22)
    a1.set_title("MDS-category rounds in the curated dataset")
    a1.legend(fontsize=7.5, frameon=False, loc="upper right")

    v = d[d["post"].notna()].sort_values("date").groupby("company").tail(1).sort_values("post")
    cmap = {2021: PALETTE["vermillion"], 2022: PALETTE["orange"], 2023: PALETTE["yellow"],
            2024: PALETTE["sky"], 2025: PALETTE["blue"], 2026: PALETTE["green"]}
    a2.barh(v["company"], v["post"], color=[cmap.get(y, PALETTE["grey"]) for y in v["year"]])
    for i, (val, dt) in enumerate(zip(v["post"], v["date"])):
        a2.text(val + 0.08, i, f"${val:.2f}B ({str(dt)[:7]})", va="center", fontsize=8)
    a2.set_xlim(0, v["post"].max() * 1.45)
    a2.set_xlabel("US$B, latest priced post-money valuation in dataset")
    a2.set_title("Latest marks: most were set in 2021-22")
    handles = [plt.Rectangle((0, 0), 1, 1, color=c) for c in cmap.values()]
    a2.legend(handles, [str(y) for y in cmap], title="Year set", fontsize=7.5, title_fontsize=8,
              frameon=False, loc="lower right")
    source_note(a1, "Source: AI Data Atlas curated dataset data/private_funding.csv (+ ch43 staging), "
                    f"{len(d)} MDS-category rounds; not a census of all venture rounds, and pre-2021 rounds are "
                    "largely absent. Valuations mix company-stated and press-reported bases; undisclosed amounts "
                    "excluded. Cribl excluded (IT telemetry). Retrieved 2026-11-01.")
    fig.tight_layout()
    return [save(fig, "ch43_mds_funding")]
