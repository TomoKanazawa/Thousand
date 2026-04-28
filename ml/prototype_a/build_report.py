"""Build the executive PDF summarizing the DDx benchmark.

Page 1: headline + results table + methodology + caveats.
Page 2: five worked examples — chart snippet, gold answer, each model's top-3.
"""

import json
from datetime import date
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

ROOT = Path(__file__).parent
OUT = ROOT / "eval_report.pdf"

# ---- Styles ----------------------------------------------------------------

styles = getSampleStyleSheet()

TITLE = ParagraphStyle(
    "title",
    parent=styles["Title"],
    fontName="Helvetica-Bold",
    fontSize=15,
    leading=18,
    spaceAfter=4,
    alignment=TA_LEFT,
    textColor=colors.HexColor("#0f172a"),
)
SUBTITLE = ParagraphStyle(
    "subtitle",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=9,
    leading=11,
    textColor=colors.HexColor("#64748b"),
    spaceAfter=10,
)
H = ParagraphStyle(
    "h",
    parent=styles["Heading2"],
    fontName="Helvetica-Bold",
    fontSize=10,
    leading=12,
    textColor=colors.HexColor("#0f172a"),
    spaceBefore=8,
    spaceAfter=3,
)
BODY = ParagraphStyle(
    "body",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=8.5,
    leading=11,
    textColor=colors.HexColor("#0f172a"),
    spaceAfter=4,
)
SMALL = ParagraphStyle(
    "small",
    parent=BODY,
    fontSize=7.5,
    leading=10,
    textColor=colors.HexColor("#475569"),
)
HEADLINE = ParagraphStyle(
    "headline",
    parent=BODY,
    fontName="Helvetica-Bold",
    fontSize=9.5,
    leading=12,
    textColor=colors.HexColor("#0f172a"),
)


def hr() -> HRFlowable:
    return HRFlowable(
        width="100%",
        thickness=0.5,
        color=colors.HexColor("#cbd5e1"),
        spaceBefore=4,
        spaceAfter=4,
    )


# ---- Content ---------------------------------------------------------------

flow: list = []

flow.append(Paragraph("Differential Diagnosis Copilot — Prototype Eval", TITLE))
flow.append(
    Paragraph(
        f"MTSamples 37-case curated benchmark · Claude Haiku 4.5 / Sonnet 4.6 / Opus 4.7 · {date.today().isoformat()}",
        SUBTITLE,
    )
)

# Headline
flow.append(
    Paragraph(
        "<b>Headline.</b> On a human-curated, leak-free set of 37 ambulatory diagnostic encounters, "
        "Claude Sonnet 4.6 ranked the correct diagnosis first in <b>84%</b> of cases and inside the "
        "top 5 in <b>95%</b>, at a total run cost of <b>$0.38</b>. Claude Opus 4.7 cost 6.6× more and "
        "did not improve accuracy. Claude Haiku 4.5 reached 76% hit@1 at <b>$0.12</b> — strong enough "
        "for development iteration. The bigger model is not the bottleneck; data curation and prompting are.",
        BODY,
    )
)

# Results table
flow.append(Paragraph("Results", H))

table_data = [
    ["Metric", "Haiku 4.5", "Sonnet 4.6", "Opus 4.7"],
    ["hit@1 (correct dx ranked first)", "28 / 37  (76%)", "31 / 37  (84%)", "30 / 37  (81%)"],
    ["hit@3 (correct dx in top 3)", "34 / 37  (92%)", "35 / 37  (95%)", "35 / 37  (95%)"],
    ["hit@5 (correct dx in top 5)", "36 / 37  (97%)", "35 / 37  (95%)", "36 / 37  (97%)"],
    ["Complete misses", "1", "2", "1"],
    ["Input tokens (total)", "47,392", "47,392", "67,838"],
    ["Output tokens (total)", "14,076", "15,881", "20,084"],
    ["Run cost (USD)", "$0.12", "$0.38", "$2.52"],
    ["Cost per hit@1", "$0.004", "$0.012", "$0.084"],
]

t = Table(table_data, colWidths=[2.55 * inch, 1.35 * inch, 1.35 * inch, 1.35 * inch])
t.setStyle(
    TableStyle(
        [
            ("FONT", (0, 0), (-1, 0), "Helvetica-Bold", 8.5),
            ("FONT", (0, 1), (-1, -1), "Helvetica", 8.5),
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0f172a")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("BACKGROUND", (2, 1), (2, 3), colors.HexColor("#dcfce7")),  # Sonnet hits column
            ("BACKGROUND", (0, 7), (-1, 8), colors.HexColor("#fef9c3")),  # cost rows
            ("ALIGN", (1, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("LINEBELOW", (0, 0), (-1, 0), 0.5, colors.HexColor("#0f172a")),
            ("LINEBELOW", (0, 1), (-1, -2), 0.25, colors.HexColor("#e2e8f0")),
            ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ]
    )
)
flow.append(t)
flow.append(
    Paragraph(
        "Pricing reflects standard Anthropic API rates (no batch discount, no prompt caching). "
        "Both savings would compound the Sonnet cost advantage.",
        SMALL,
    )
)

# Methodology
flow.append(Paragraph("Methodology", H))
flow.append(
    Paragraph(
        "<b>Source.</b> Public MTSamples corpus of de-identified clinical transcription samples. "
        "199 cases fetched across 17 specialties, automatically filtered to remove procedure notes, "
        "follow-ups with pre-stated diagnoses, pediatric cases, trauma, and counseling visits.",
        BODY,
    )
)
flow.append(
    Paragraph(
        "<b>Sanitization.</b> Each chart was stripped of its Assessment / Impression / Plan section, "
        "the Sample-Name and Description preamble (which leak the diagnosis), and footer scaffolding. "
        "Charts without a real HPI / Chief Complaint / Reason-for-Consult section were dropped.",
        BODY,
    )
)
flow.append(
    Paragraph(
        "<b>Human curation.</b> 22 exact-content duplicates removed. The remaining 125 unique cases "
        "were read individually and labeled GOOD (37), ACCEPTABLE (35), or BAD (53). Only the 37 GOOD "
        "cases — which test a real differential rather than recall a stated diagnosis — were used in this run.",
        BODY,
    )
)
flow.append(
    Paragraph(
        "<b>Eval loop.</b> For each chart the model returned a ranked top-5 differential with "
        "one-line reasoning per item. A separate Haiku call judged whether each candidate matched "
        "any of the case's gold terms (extracted from the MTSamples keywords list plus the title-derived "
        "primary complaint). Lowest matching rank was recorded.",
        BODY,
    )
)

# Caveats
flow.append(Paragraph("What this proves — and what it doesn't", H))
flow.append(
    Paragraph(
        "<b>Proves.</b> The end-to-end loop works: chart in, ranked DDx out, automated scoring against "
        "ground truth. The frontier models reason capably about ambulatory presentations on this curated set, "
        "and Sonnet outperforms Opus at materially lower cost on this workload. Cost per case (~$0.01 with "
        "Sonnet) is well within budget for a real pilot.",
        BODY,
    )
)
flow.append(
    Paragraph(
        "<b>Does not prove.</b> n=37 is small — confidence intervals are wide. MTSamples is "
        "transcription-clean and English-stylized; real EHR notes are messier, longer, and contain "
        "copy-forwarded artifacts. Cases were curated for fairness; production charts will include "
        "follow-ups, multi-issue visits, and ambiguous presentations. The LLM-judge introduces "
        "synonym-matching noise; some near-misses may be true matches and vice-versa.",
        BODY,
    )
)
flow.append(
    Paragraph(
        "<b>Next.</b> Build the synthetic-EHR pipeline (Synthea + LLM-generated notes) for "
        "longitudinal stress-testing, run a hard-mode benchmark against NEJM Case Records, and seed "
        "the first design-partner pilot to evaluate on real de-identified ambulatory data.",
        BODY,
    )
)

flow.append(Spacer(1, 6))
flow.append(hr())
flow.append(
    Paragraph(
        "Reproducibility — all code, prompts, ground-truth labels, and per-case results are in the "
        "<font face='Courier'>ml/prototype_a/</font> directory of this repository. "
        "Raw MTSamples downloads are gitignored but regenerable with "
        "<font face='Courier'>python fetch_cases.py &amp;&amp; python prepare_cases.py</font>.",
        SMALL,
    )
)


# ---- Page 2+: Worked examples (chart in / Haiku answer out) ----------------

flow.append(PageBreak())

flow.append(Paragraph("Worked examples — what the LLM read &amp; what it answered", TITLE))
flow.append(
    Paragraph(
        "Two cases from the 37-case set: a routine ambulatory presentation and a complex "
        "multi-system reasoning challenge. For each, the full sanitized chart shown to the model "
        "appears verbatim in the gray panel; Haiku 4.5's ranked top-5 differential — exactly as "
        "returned, including its one-line reasoning per item — is shown below.",
        SUBTITLE,
    )
)

EXAMPLE_HEADERS = {
    "01": "Case 01 · Abdominal pain consult — clean hit at rank 1",
    "135": "Case 135 · Multi-system presentation — clean hit at rank 1",
}
EXAMPLE_GOLD = {
    "01": "diverticulitis (primary), sigmoid colon, lower quadrant pain",
    "135": "vasculitis / granulomatosis with polyangiitis, hemoptysis, polyarthralgia",
}


CHART_STYLE = ParagraphStyle(
    "chart",
    parent=BODY,
    fontName="Helvetica",
    fontSize=7,
    leading=9,
    textColor=colors.HexColor("#1e293b"),
    spaceAfter=0,
)
DDX_ROW = ParagraphStyle(
    "ddx_row",
    parent=BODY,
    fontSize=8,
    leading=10.5,
    spaceAfter=2,
)
WHITE_LABEL = ParagraphStyle(
    "white_label",
    parent=BODY,
    fontName="Helvetica-Bold",
    fontSize=8.5,
    textColor=colors.white,
)
SECTION_LABEL = ParagraphStyle(
    "section_label",
    parent=BODY,
    fontName="Helvetica-Bold",
    fontSize=8.5,
    leading=11,
    textColor=colors.HexColor("#0f172a"),
    spaceBefore=4,
    spaceAfter=2,
)


def parse_haiku_for(idx: str) -> dict:
    """Return Haiku's per-case row data: result string + ranked DDx with reasoning."""
    import re
    text = (ROOT / "results_haiku.md").read_text()
    pattern = re.compile(
        r"### Case " + re.escape(idx) + r" — \S+\n\n.*?\*\*Result:\*\* (.+?)\n\n\| Rank.*?\|\n\|.*?\|\n((?:\|.*?\n)+)",
        re.DOTALL,
    )
    m = pattern.search(text)
    if not m:
        return {"result": "—", "rows": []}
    result, table_rows = m.groups()
    rows = []
    for line in table_rows.strip().split("\n"):
        cols = [c.strip() for c in line.strip("|").split("|")]
        if len(cols) >= 3:
            rows.append({"rank": cols[0], "dx": cols[1], "reasoning": cols[2]})
    return {"result": result.replace("**", ""), "rows": rows}


def render_full_case(idx: str) -> list:
    parts: list = []

    # Header bar
    header = Table(
        [[Paragraph(EXAMPLE_HEADERS[idx], WHITE_LABEL)]],
        colWidths=[7.3 * inch],
    )
    header.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#0f172a")),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    parts.append(header)
    parts.append(Spacer(1, 4))

    # Gold answer
    parts.append(Paragraph(
        f"<b>Correct diagnosis (gold):</b> {EXAMPLE_GOLD[idx]}",
        CASE_BODY := ParagraphStyle("body8", parent=BODY, fontSize=8, leading=10.5, spaceAfter=4),
    ))

    # Chart panel — the "question" the LLM read
    parts.append(Paragraph("INPUT — sanitized chart shown to the model:", SECTION_LABEL))
    chart_text = (ROOT / "prepared").glob(f"{idx}_*.input.txt")
    chart_path = next(iter(chart_text))
    raw = chart_path.read_text(encoding="utf-8")
    # Convert to ReportLab paragraph-safe HTML: line breaks → <br/>, escape angle brackets
    safe = (raw.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
                 .replace("\n", "<br/>"))
    chart_para = Paragraph(safe, CHART_STYLE)
    chart_panel = Table([[chart_para]], colWidths=[7.3 * inch])
    chart_panel.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f1f5f9")),
        ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    parts.append(chart_panel)

    # Haiku output
    parts.append(Paragraph(
        f"OUTPUT — Haiku 4.5's ranked differential ({parse_haiku_for(idx)['result']}):",
        SECTION_LABEL,
    ))
    rows = parse_haiku_for(idx)["rows"]
    for r in rows:
        # Highlight rank 1 specially
        rank_color = "#16a34a" if r["rank"] == "1" else "#0f172a"
        parts.append(Paragraph(
            f"<font color='{rank_color}'><b>{r['rank']}. {r['dx']}</b></font> "
            f"&nbsp;<font color='#475569'>— {r['reasoning']}</font>",
            DDX_ROW,
        ))

    parts.append(Spacer(1, 8))
    return parts


for idx in ["01", "135"]:
    for el in render_full_case(idx):
        flow.append(el)


# ---- Build -----------------------------------------------------------------

doc = SimpleDocTemplate(
    str(OUT),
    pagesize=LETTER,
    leftMargin=0.6 * inch,
    rightMargin=0.6 * inch,
    topMargin=0.55 * inch,
    bottomMargin=0.55 * inch,
    title="Differential Diagnosis Copilot — Prototype Eval",
    author="Andy DDx Prototype",
)
doc.build(flow)
print(f"Wrote {OUT} ({OUT.stat().st_size / 1024:.1f} KB)")
