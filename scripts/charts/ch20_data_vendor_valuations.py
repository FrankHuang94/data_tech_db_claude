"""Ch 20: latest post-money valuations of AI-training-data vendors.

Reads data/private_funding.csv (category "AI training data") plus the chapter's staged rows in
data/staging/ch20-private_funding.csv (until the integrator merges them), and overlays
press-reported valuation talks that have not closed from data/ch20_valuation_talks.csv.
"""
from pathlib import Path

import pandas as pd

from chartlib import DATA, PALETTE, load, num, plt, save, source_note

BASIS_COLOR = {"company-stated": PALETTE["blue"], "press-reported": PALETTE["orange"]}


def _rounds() -> pd.DataFrame:
    frames = [load("private_funding")]
    staged = DATA / "staging" / "ch20-private_funding.csv"
    if staged.exists():
        frames.append(pd.read_csv(staged))
    d = pd.concat(frames, ignore_index=True)
    d = d[d["category"].astype(str).str.strip().str.lower() == "ai training data"].copy()
    d["dt"] = pd.to_datetime(d["date"], errors="coerce")
    d["val"] = num(d["post_money_valuation_usd_b"])
    d = d.dropna(subset=["val"]).drop_duplicates(subset=["company", "date", "round"], keep="last")
    return d.sort_values("dt").groupby("company", as_index=False).tail(1)


def make():
    latest = _rounds().sort_values("val")
    talks_path = DATA / "ch20_valuation_talks.csv"
    talks = pd.read_csv(talks_path) if talks_path.exists() else pd.DataFrame(columns=["company"])
    if not talks.empty:
        talks["v"] = num(talks["reported_valuation_usd_b"])

    companies = list(latest["company"])
    for c in talks.get("company", []):
        if c not in companies:
            companies.insert(0, c)
    ypos = {c: i for i, c in enumerate(companies)}

    fig, ax = plt.subplots(figsize=(10, 5.2))
    for _, r in latest.iterrows():
        basis = str(r["valuation_basis"]).strip().lower()
        color = BASIS_COLOR.get(basis, PALETTE["grey"])
        ax.barh(ypos[r["company"]], r["val"], color=color, height=0.6)
        ax.annotate(f"${r['val']:.1f}B  ({r['round']}, {r['dt']:%b %Y})", (r["val"], ypos[r["company"]]),
                    xytext=(5, -3), textcoords="offset points", fontsize=8)
    for _, t in talks.iterrows():
        ax.scatter(t["v"], ypos[t["company"]], marker="D", s=70, facecolors="none",
                   edgecolors=PALETTE["vermillion"], linewidths=1.8, zorder=3)
        ax.annotate(f"talks ${t['v']:.0f}B ({pd.to_datetime(t['date']):%b %Y}, not closed)",
                    (t["v"], ypos[t["company"]]), xytext=(8, 6), textcoords="offset points", fontsize=8,
                    color=PALETTE["vermillion"])
    ax.set_yticks(range(len(companies)))
    ax.set_yticklabels(companies)
    ax.set_xlim(0, 38)
    ax.set_xlabel("Post-money valuation, US$ billions")
    ax.set_title("AI training-data vendors: latest priced valuation vs. reported talks (as of Nov 2026)")
    handles = [plt.Rectangle((0, 0), 1, 1, color=c) for c in BASIS_COLOR.values()]
    handles.append(plt.Line2D([], [], marker="D", linestyle="", markerfacecolor="none",
                              markeredgecolor=PALETTE["vermillion"], markersize=8))
    ax.legend(handles, ["Priced round, company-stated", "Priced round, press-reported",
                        "Reported talks (not closed)"], frameon=False, fontsize=8, loc="center right")
    source_note(ax, "Source: data/private_funding.csv + data/staging/ch20-private_funding.csv (category 'AI training data'); "
                    "data/ch20_valuation_talks.csv. Scale AI = implied by Meta's $14.3B for 49% (Jun 2025). Invisible = 'over $2B' floor. "
                    "Surge AI is bootstrapped (no priced primary round). Handshake, Labelbox, Toloka omitted: no verified valuation. "
                    "Retrieved 2026-11-01.")
    return [save(fig, "ch20_data_vendor_valuations")]
