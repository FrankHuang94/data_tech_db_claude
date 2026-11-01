"""Ch 28: hyperscaler cloud segment revenue growth by provider (data/ch28_cloud_segments.csv)."""
from chartlib import load, num, save, source_note, PALETTE, plt
import pandas as pd

SPEC = [
    ("AWS", PALETTE["orange"], "o"),
    ("Google Cloud", PALETTE["blue"], "s"),
    ("Microsoft Azure", PALETTE["sky"], "^"),
    ("Oracle OCI", PALETTE["vermillion"], "D"),
]


def make():
    d = load("ch28_cloud_segments")
    d["dt"] = pd.to_datetime(d["date"], errors="coerce")
    d["g"] = num(d["yoy_growth_pct"])
    d["rev"] = num(d["revenue_usd_b"])
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(12, 5.4), gridspec_kw={"width_ratios": [2.2, 1]})
    gap_start, gap_end = pd.Timestamp("2025-10-15"), pd.Timestamp("2026-08-15")
    ax.axvspan(gap_start, gap_end, color=PALETTE["grey"], alpha=0.08)
    ax.text(gap_start + (gap_end - gap_start) / 2, 128, "quarters not compiled\n(see chapter text)", ha="center",
            va="top", fontsize=7.5, color=PALETTE["grey"])
    for prov, color, marker in SPEC:
        s = d[(d["provider"] == prov) & d["g"].notna()].sort_values("dt")
        if s.empty:
            continue
        early = s[s["dt"] < gap_start]
        late = s[s["dt"] > gap_end]
        ax.plot(early["dt"], early["g"], marker=marker, color=color, linewidth=2, label=prov)
        if not late.empty and not early.empty:
            ax.plot([early["dt"].iloc[-1], late["dt"].iloc[0]], [early["g"].iloc[-1], late["g"].iloc[0]],
                    color=color, linewidth=1.2, linestyle=":")
            ax.scatter(late["dt"], late["g"], marker=marker, color=color, s=55, zorder=3)
            r = late.iloc[-1]
            ax.annotate(f"{r['g']:.0f}%", (r["dt"], r["g"]), xytext=(7, -3), textcoords="offset points", fontsize=8)
    ax.set_ylim(0, 130)
    ax.set_ylabel("Year-over-year revenue growth (%)")
    ax.set_title("Cloud segment growth, quarterly, 2024–2026")
    ax.legend(fontsize=8, frameon=False, loc="upper left")
    # latest-quarter revenue bars
    latest = []
    for prov, color, _ in SPEC:
        s = d[(d["provider"] == prov) & d["rev"].notna()].sort_values("dt")
        if s.empty:
            continue
        r = s.iloc[-1]
        latest.append((prov, r["rev"], color, str(r["fiscal_period"]).split(" (")[0]))
    short = {"AWS": "AWS", "Google Cloud": "Google\nCloud", "Microsoft Azure": "Azure", "Oracle OCI": "OCI"}
    names = [f"{short[p]}\n{q}" for p, _, _, q in latest]
    vals = [v for _, v, _, _ in latest]
    bars = ax2.bar(names, vals, color=[c for _, _, c, _ in latest])
    for b, (p, _, _, q) in zip(bars, latest):
        if "2025" in q:  # stale quarter: hatch and flag
            b.set_hatch("//")
            b.set_alpha(0.55)
            ax2.text(b.get_x() + b.get_width() / 2, b.get_height() / 2, "a year\nearlier", ha="center", fontsize=7,
                     bbox=dict(facecolor="white", edgecolor="none", pad=1.5))
    for i, v in enumerate(vals):
        ax2.text(i, v + 0.6, f"${v:.1f}B", ha="center", fontsize=8)
    ax2.set_ylabel("Quarterly revenue, US$ billions")
    ax2.set_title("Latest compiled quarter")
    ax2.tick_params(axis="x", labelsize=7.5)
    ax2.set_ylim(0, 38)
    source_note(ax, "Source: data/ch28_cloud_segments.csv (Amazon, Alphabet, Microsoft, Oracle releases; Q3 2026 Google Cloud from "
                    "Alphabet 8-K; Azure Q1 FY2027 and OCI Q1 FY2027 press-reported). AWS latest quarter not compiled [VERIFY]. "
                    "Segments differ: Google Cloud includes Workspace and TPU sales; Azure growth is 'Azure and other cloud services'; "
                    "OCI is Oracle's IaaS line. Microsoft FY ends Jun 30, Oracle FY ends May 31. Retrieved 2026-11-01.")
    return [save(fig, "ch28_cloud_growth")]
