"""Ch 31: latest valuation or market cap for analytical-engine challengers and legacy platforms.

Private marks come from data/private_funding.csv (latest row with a post-money valuation per company);
public market caps come from data/public_comps.csv. The two bases are NOT comparable like-for-like:
private post-money valuations are set on preferred shares at a point in time, public market caps float daily.
"""
from chartlib import load, num, save, source_note, PALETTE, plt
import pandas as pd

PRIVATE = ["ClickHouse", "Dremio", "MotherDuck", "Starburst", "Firebolt", "StarTree"]
PUBLIC = ["Palantir", "SAP", "IBM", "Teradata"]


def make():
    f = load("private_funding")
    f["val"] = num(f["post_money_valuation_usd_b"])
    f["dt"] = pd.to_datetime(f["date"], errors="coerce")
    rows = []
    missing = []
    for co in PRIVATE:
        s = f[(f["company"] == co) & f["val"].notna()].sort_values("dt")
        if s.empty:
            missing.append(co)
            continue
        r = s.iloc[-1]
        basis = str(r["valuation_basis"])
        label = f"{co} (private post-money, {r['round']}, {r['dt']:%b %Y}; {basis})"
        if co == "Dremio":
            label = f"Dremio (last private mark, {r['round']}, {r['dt']:%b %Y}; acquired by SAP 2026, terms undisclosed)"
        rows.append((label, float(r["val"]), "private"))
    c = load("public_comps")
    c["mc"] = num(c["market_cap_usd_b"])
    for co in PUBLIC:
        s = c[c["company"] == co]
        if s.empty or s["mc"].isna().all():
            missing.append(co)
            continue
        r = s.iloc[0]
        rows.append((f"{co} (public market cap, {r['as_of']})", float(r["mc"]), "public"))
    d = pd.DataFrame(rows, columns=["label", "v", "kind"]).sort_values("v")

    fig, ax = plt.subplots(figsize=(10, 5.6))
    colors = [PALETTE["vermillion"] if k == "private" else PALETTE["blue"] for k in d["kind"]]
    ax.barh(d["label"], d["v"], color=colors)
    ax.set_xscale("log")
    ax.set_xlabel("US$ billions (log scale)")
    for i, (_, r) in enumerate(d.iterrows()):
        txt = f"${r['v']:,.1f}B" if r["v"] < 10 else f"${r['v']:,.0f}B"
        ax.annotate(txt, (r["v"], i), xytext=(4, -3), textcoords="offset points", fontsize=8)
    ax.set_xlim(0.2, 1500)
    ax.set_title("Challengers vs incumbents: latest valuation or market cap (mixed bases)")
    handles = [plt.Rectangle((0, 0), 1, 1, color=PALETTE["vermillion"]),
               plt.Rectangle((0, 0), 1, 1, color=PALETTE["blue"])]
    ax.legend(handles, ["Private post-money valuation (point in time)", "Public market capitalization"],
              fontsize=8, frameon=False, loc="lower right")
    note = ("Source: data/private_funding.csv (Bloomberg, Business Wire, The Register, Dremio) and data/public_comps.csv "
            "(stockanalysis.com, 2026-10-28/30). Private and public figures are different bases and are not directly "
            "comparable. ")
    if missing:
        note += "No priced valuation on file for: " + ", ".join(missing) + ". "
    note += "Retrieved 2026-11-01."
    source_note(ax, note)
    return [save(fig, "ch31_valuations")]
