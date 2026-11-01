"""Ch 48: question counts by topic group, parsed from the chapter's own tags.

Each question in docs/07-conversation-toolkit/ch48-question-bank.md ends with a tag
of the form *[Topic: <topic> · Audience: <a>, <b>]*. This script counts questions per
topic (left panel) and question-audience tags per audience (right panel).
"""
import re
from collections import Counter

from chartlib import ROOT, PALETTE, plt, save, source_note

CHAPTER = ROOT / "docs" / "07-conversation-toolkit" / "ch48-question-bank.md"
TAG = re.compile(r"\*\[Topic: ([^·\]]+?) · Audience: ([^\]]+?)\]\*")
QLINE = re.compile(r"^\*\*\d+\.\*\*")

TOPIC_ORDER = ["architecture", "table formats", "pipelines", "governance", "AI data stack",
               "Databricks & Snowflake", "hyperscalers & apps", "business model", "valuation & M&A",
               "storage meets data", "founder diligence"]
AUDIENCE_ORDER = ["PM", "Engineer", "Partner manager", "Founder/CEO", "CFO/Finance", "Customer"]


def parse(path=CHAPTER):
    """Return a list of (topic, [audiences]) for every numbered question line."""
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not QLINE.match(line):
            continue
        m = TAG.search(line)
        if not m:
            raise ValueError(f"Question without a tag: {line[:80]}")
        rows.append((m.group(1).strip(), [a.strip() for a in m.group(2).split(",")]))
    return rows


def make():
    rows = parse()
    topics = Counter(t for t, _ in rows)
    auds = Counter(a for _, aa in rows for a in aa)
    t_order = [t for t in TOPIC_ORDER if t in topics] + sorted(set(topics) - set(TOPIC_ORDER))
    a_order = [a for a in AUDIENCE_ORDER if a in auds] + sorted(set(auds) - set(AUDIENCE_ORDER))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.6), gridspec_kw={"width_ratios": [1.6, 1]})
    vals = [topics[t] for t in t_order]
    colors = [PALETTE["vermillion"] if t == "storage meets data" else PALETTE["blue"] for t in t_order]
    ax1.barh(t_order[::-1], vals[::-1], color=colors[::-1])
    for i, v in enumerate(vals[::-1]):
        ax1.text(v + 0.2, i, str(v), va="center", fontsize=9)
    ax1.set_xlabel("Number of questions")
    ax1.set_title(f"Questions by topic group (total {len(rows)})")
    ax1.grid(axis="y", visible=False)

    avals = [auds[a] for a in a_order]
    ax2.barh(a_order[::-1], avals[::-1], color=PALETTE["orange"])
    for i, v in enumerate(avals[::-1]):
        ax2.text(v + 0.5, i, str(v), va="center", fontsize=9)
    ax2.set_xlabel("Questions tagged for this audience")
    ax2.set_title("Audience tags (a question can have several)")
    ax2.grid(axis="y", visible=False)

    source_note(ax1, "Source: tags parsed from docs/07-conversation-toolkit/ch48-question-bank.md by "
                     "scripts/charts/ch48_question_counts.py. Storage meets data (Everpure lens) highlighted. "
                     "Retrieved 2026-11-01.")
    fig.tight_layout()
    return [save(fig, "ch48_question_counts")]


def matrix_markdown():
    """Markdown topic x audience count table (used to fill the chapter's matrix)."""
    rows = parse()
    head = "| Topic group | Questions | " + " | ".join(AUDIENCE_ORDER) + " |"
    sep = "|---|---:|" + "---:|" * len(AUDIENCE_ORDER)
    out = [head, sep]
    for t in TOPIC_ORDER:
        sub = [aa for tt, aa in rows if tt == t]
        cells = [str(sum(a in aa for aa in sub)) for a in AUDIENCE_ORDER]
        out.append(f"| {t} | {len(sub)} | " + " | ".join(cells) + " |")
    tot = [str(sum(a in aa for _, aa in rows)) for a in AUDIENCE_ORDER]
    out.append(f"| **Total** | **{len(rows)}** | " + " | ".join(f"**{c}**" for c in tot) + " |")
    return "\n".join(out)


if __name__ == "__main__":
    print(matrix_markdown())
