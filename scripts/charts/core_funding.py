"""Private-market charts from data/private_funding.csv."""
from chartlib import load, num, save, source_note, PALETTE, SERIES, plt
import pandas as pd


def make():
    d = load("private_funding")
    d["dt"] = pd.to_datetime(d["date"], errors="coerce")
    d["val"] = num(d["post_money_valuation_usd_b"])
    d["amt"] = num(d["amount_usd_m"])
    outs = []

    # Databricks valuation step-ups
    db = d[d["company"].str.lower().str.startswith("databricks") & d["val"].notna()].sort_values("dt")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(db["dt"], db["val"], marker="o", color=PALETTE["vermillion"])
    last = None
    for _, r in db.iterrows():
        if last is not None and (r["dt"] - last["dt"]).days < 150 and abs(r["val"] - last["val"]) < 10:
            continue  # skip near-duplicate points (final closes, term sheet vs close)
        label = str(r["round"]).replace(" (close)", "").replace(" final close + debt", "")[:22]
        ax.annotate(f"{label}\n${r['val']:.0f}B", (r["dt"], r["val"]), fontsize=7, xytext=(-28, 8), textcoords="offset points")
        last = r
    ax.set_title("Databricks post-money valuation by round (US$B)")
    ax.set_ylabel("US$ billions")
    source_note(ax, "Source: data/private_funding.csv (company-stated or press-reported post-money valuations; see valuation_basis). Retrieved 2026-11-01.")
    outs.append(save(fig, "databricks_valuation_timeline"))

    # Snowflake pre-IPO valuations
    sf = d[d["company"].str.lower().str.startswith("snowflake") & d["val"].notna()].sort_values("dt")
    if len(sf):
        fig, ax = plt.subplots(figsize=(9, 4.5))
        ax.plot(sf["dt"], sf["val"], marker="o", color=PALETTE["sky"])
        for _, r in sf.iterrows():
            ax.annotate(f"{r['round']} ${r['val']:.1f}B", (r["dt"], r["val"]), fontsize=7, xytext=(-10, 8), textcoords="offset points")
        ax.set_title("Snowflake pre-IPO post-money valuation by round (US$B)")
        ax.set_ylabel("US$ billions")
        source_note(ax, "Source: data/private_funding.csv. Snowflake IPO'd in Sept 2020.")
        outs.append(save(fig, "snowflake_preipo_valuation"))

    # Latest valuation per company (excluding Databricks for scale), top 20
    latest = d[d["val"].notna()].sort_values("dt").groupby("company").tail(1)
    latest = latest[~latest["company"].str.lower().str.startswith(("databricks", "snowflake"))].nlargest(20, "val").sort_values("val")
    fig, ax = plt.subplots(figsize=(9, 7))
    cats = sorted(latest["category"].fillna("other").unique())
    cmap = {c: SERIES[i % len(SERIES)] for i, c in enumerate(cats)}
    ax.barh(latest["company"], latest["val"], color=[cmap[c] for c in latest["category"].fillna("other")])
    for i, (v, dt) in enumerate(zip(latest["val"], latest["dt"])):
        ax.text(v, i, f" ${v:.1f}B ({dt:%b %Y})", va="center", fontsize=7)
    handles = [plt.Rectangle((0, 0), 1, 1, color=cmap[c]) for c in cats]
    ax.legend(handles, cats, fontsize=7, frameon=False, loc="lower right")
    ax.set_title("Latest private valuation marks, data and AI-data companies (ex-Databricks)")
    ax.set_xlabel("Post-money valuation, US$B")
    source_note(ax, "Source: data/private_funding.csv (latest round per company with a disclosed or reported valuation).")
    outs.append(save(fig, "private_marks_latest"))

    # Funding by category (sum of amounts, 2023+)
    rec = d[(d["dt"] >= "2023-01-01") & d["amt"].notna()]
    cat = rec.groupby("category")["amt"].sum().sort_values() / 1000
    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.barh(cat.index, cat.values, color=PALETTE["green"])
    ax.set_title("Capital raised by category in the dataset, 2023–2026 (US$B)")
    ax.set_xlabel("US$ billions (sum of round sizes in dataset)")
    source_note(ax, "Source: data/private_funding.csv; curated rounds, not a census. Includes debt where the company reported it with the round.")
    outs.append(save(fig, "funding_by_category"))

    # Vector DB funding
    vdb = d[(d["category"] == "vector database") & d["amt"].notna()].sort_values("dt")
    if len(vdb):
        fig, ax = plt.subplots(figsize=(9, 4.5))
        labels = [f"{c}\n{r} ({t:%Y})" for c, r, t in zip(vdb["company"], vdb["round"], vdb["dt"])]
        ax.bar(range(len(vdb)), vdb["amt"], color=PALETTE["green"])
        ax.set_xticks(range(len(vdb)), labels, fontsize=7)
        ax.set_ylabel("Round size, US$M")
        ax.set_title("Vector-database funding rounds in the dataset (US$M)")
        source_note(ax, "Source: data/private_funding.csv.")
        outs.append(save(fig, "vector_db_funding"))
    return outs
