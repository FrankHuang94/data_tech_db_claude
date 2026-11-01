"""Ch 41: latest market-size value per segment (mixed bases, log scale).

Reads data/market_sizes.csv plus data/ch41_market_sizes_additions.csv. Where both files hold the same
(segment, year), the additions rows win (they are corrections or better sources). For each segment the chart
shows the latest year at or before 2026 (actuals or near-term forecasts beat far-out projections), breaking ties
by the most recent as_of date; segments with only future-dated rows show their earliest year. "(f)" marks a
forecast (year not yet complete at publication). Bars are coloured by basis; hatched bars are weak, derived or
unverified rows (notes contain WEAK, DERIVED or a bare [VERIFY] tag).
"""
from chartlib import load, num, save, source_note, PALETTE, plt
import pandas as pd

SHORT = {
    "AI spending (total, all categories)": "AI spending, all categories",
    "Public cloud services end-user spending (context for cloud database)": "Public cloud services (all)",
    "Generative AI spending (total)": "Generative AI spending",
    "AI infrastructure spending (servers, storage for AI)": "AI infrastructure (servers + storage)",
    "Information security end-user spending (proxy for DSPM/data security)": "Information security (all)",
    "Snowflake addressable market (data, analytics and AI platforms)": "Snowflake-stated TAM",
    "Data and analytics software (incl. DBMS, analytics, data management)": "Data and analytics software",
    "DBMS (worldwide, all deployment)": "DBMS (all deployment)",
    "Everpure addressable market (company total)": "Everpure-stated TAM (total)",
    "Data streaming (Confluent addressable market)": "Confluent-stated streaming TAM",
    "Sovereign cloud IaaS spending": "Sovereign cloud IaaS",
    "Cloud database (cloud DBMS / dbPaaS)": "Cloud DBMS (dbPaaS)",
    "Enterprise storage market (Everpure framing)": "Enterprise storage (Everpure framing)",
    "Analytic platforms software (incl. data science and AI platforms)": "Analytic platforms (incl. ABI, DSML)",
    "Integration software technologies (broad: iPaaS + data integration + API)": "Integration software (broad)",
    "Everpure Modern Data Software addressable market": "Everpure Modern Data Software TAM",
    "Analytics and BI software (narrow definition)": "Analytics and BI (narrow)",
    "Metadata management tools (governance and catalog proxy)": "Metadata management tools",
    "Data management software excl. DBMS (integration, quality, metadata/governance)": "Data mgmt software ex-DBMS",
    "Everpure Scale AI addressable market": "Everpure Scale AI TAM",
    "Data integration software": "Data integration software",
    "AI training dataset market": "AI training datasets",
    "Vector database": "Vector database",
    "Data security posture management (DSPM)": "DSPM",
}


def _kind(basis: str) -> str:
    b = basis.lower()
    if "company-stated" in b:
        return "company"
    if "syndicated" in b or "tracker" in b:
        return "syndicated"
    if "press" in b:
        return "press"
    return "analyst"


COLORS = {"analyst": PALETTE["blue"], "company": PALETTE["vermillion"],
          "syndicated": PALETTE["orange"], "press": PALETTE["grey"]}
LABELS = {"analyst": "Analyst estimate or forecast (Gartner, IDC)", "company": "Company-stated TAM",
          "syndicated": "Syndicated research / tracker", "press": "Press-reported analyst figure"}


def make():
    base = load("market_sizes")
    base["_src"] = 0
    add = load("ch41_market_sizes_additions")
    add["_src"] = 1
    keys = set(zip(add["segment"], add["year"]))
    base = base[[(s, y) not in keys for s, y in zip(base["segment"], base["year"])]]
    d = pd.concat([base, add], ignore_index=True)
    d["v"] = num(d["value_usd_b"])
    d["year"] = num(d["year"]).astype(int)
    d["asof"] = d["as_of"].astype(str)

    rows = []
    for seg, g in d.groupby("segment"):
        near = g[g["year"] <= 2026]
        if near.empty:
            r = g.sort_values("year").iloc[0]
        else:
            r = near.sort_values(["year", "asof"]).iloc[-1]
        notes = str(r["notes"])
        weak = any(k in notes for k in ("WEAK", "DERIVED", "[VERIFY]"))
        fcst = r["year"] >= int(r["asof"][:4])
        rows.append({"label": SHORT.get(seg, seg[:40]), "v": float(r["v"]),
                     "year": f"{int(r['year'])}{' (f)' if fcst else ''}",
                     "pub": str(r["publisher"]).split(" (")[0], "kind": _kind(str(r["basis"])), "weak": weak})
    c = pd.DataFrame(rows).sort_values("v").reset_index(drop=True)

    fig, ax = plt.subplots(figsize=(11, 9.5))
    for i, r in c.iterrows():
        ax.barh(i, r["v"], color=COLORS[r["kind"]], hatch="///" if r["weak"] else None,
                edgecolor="white" if r["weak"] else COLORS[r["kind"]], linewidth=0)
        val = f"${r['v']:,.0f}B" if r["v"] >= 10 else f"${r['v']:,.1f}B"
        tag = " *" if r["weak"] else ""
        ax.annotate(f"{val}  {r['pub']}, {r['year']}{tag}", (r["v"], i), xytext=(4, -3),
                    textcoords="offset points", fontsize=7.5)
    ax.set_yticks(range(len(c)))
    ax.set_yticklabels(c["label"], fontsize=8.5)
    ax.set_xscale("log")
    ax.set_xlim(0.5, 60000)
    ax.set_xlabel("US$ billions (log scale)")
    ax.set_title("Market-size claims by segment: latest value at or before 2026 (mixed bases, not additive)")
    kinds = [k for k in LABELS if k in set(c["kind"])]
    handles = [plt.Rectangle((0, 0), 1, 1, color=COLORS[k]) for k in kinds]
    handles.append(plt.Rectangle((0, 0), 1, 1, facecolor=PALETTE["grey"], hatch="///", edgecolor="white"))
    ax.legend(handles, [LABELS[k] for k in kinds] + ["Hatched / * = weak, derived or unverified source"],
              fontsize=8, frameon=False, loc="lower right")
    source_note(ax, "Source: data/market_sizes.csv and data/ch41_market_sizes_additions.csv (Gartner abstracts and "
                    "press releases, IDC, Snowflake and Everpure investor materials, Confluent call, MarketsandMarkets, "
                    "Global Market Insights, Grand View, FMI via Securiti, Apps Run the World). Bases differ: vendor "
                    "revenue, end-user spending, company TAM and syndicated estimates are not comparable or additive. "
                    "(f) = forecast (year not complete when published). Everpure figures are fiscal years (FY2030 ends ~Jan 2030); far-future rows shown only where no earlier year exists. "
                    "Retrieved 2026-11-01.")
    return [save(fig, "ch41_market_sizes")]
