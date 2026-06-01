"""Reslice the 94% hit-rate result by:
  1. KDIGO severity (severe / moderate / mild) — already in results
  2. Tier 2 LLM verification verdict (NOT_MENTIONED only — cleaned set)
  3. Intersection (severe AND NOT_MENTIONED) — most defensible

Read-only over existing files; produces a console table + markdown report.
No API calls.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).parent
RESULTS = json.loads((ROOT / "results_aki_haiku.json").read_text())
VERDICTS = json.loads((ROOT / "tier2_verification.json").read_text())

# severity → set(hadm_id_str)
sel = json.loads((ROOT / "selected_admissions_aki.json").read_text())
sev_by_hadm = {}
for s in sel:
    h = str(s["hadm_id"])
    r = float(s.get("ratio") or 0)
    sev_by_hadm[h] = "severe" if r >= 3.0 else "moderate" if r >= 2.0 else "mild"

# verdict → set(hadm_id_str)
clean_ids = {h for h, v in VERDICTS.items() if v.get("verdict") == "NOT_MENTIONED"}
implied_ids = {h for h, v in VERDICTS.items() if v.get("verdict") == "IMPLIED"}

lines = ["# AKI Hit-Rate Reslice", ""]
lines.append("Source: `results_aki_haiku.json` × `tier2_verification.json` × `selected_admissions_aki.json`. No API calls.")
lines.append("")

for cutoff, cases in RESULTS.items():
    if not isinstance(cases, dict):
        continue
    lines.append(f"## Cutoff: `{cutoff}`")
    lines.append("")
    lines.append("| Slice | n | hit@5 | hit@15 |")
    lines.append("|---|---|---|---|")

    slices = {
        "All (original)": list(cases.items()),
        "Severe (KDIGO Stage 3)": [(h, c) for h, c in cases.items() if sev_by_hadm.get(h) == "severe"],
        "Moderate (KDIGO Stage 2)": [(h, c) for h, c in cases.items() if sev_by_hadm.get(h) == "moderate"],
        "Mild (KDIGO Stage 1)": [(h, c) for h, c in cases.items() if sev_by_hadm.get(h) == "mild"],
        "NOT_MENTIONED (clean)": [(h, c) for h, c in cases.items() if h in clean_ids],
        "Severe ∩ NOT_MENTIONED (most defensible)": [(h, c) for h, c in cases.items()
                                                       if sev_by_hadm.get(h) == "severe" and h in clean_ids],
    }

    for name, rows in slices.items():
        if not rows:
            lines.append(f"| {name} | 0 | — | — |")
            continue
        n = len(rows)
        h5 = sum(c.get("hit@5", False) for _, c in rows)
        h15 = sum(c.get("hit@15", False) for _, c in rows)
        lines.append(f"| {name} | {n} | {h5}/{n} ({h5/n:.0%}) | {h15}/{n} ({h15/n:.0%}) |")

    lines.append("")

# Distribution of verdicts within each severity
lines.append("## Verdict × severity distribution (n=100)")
lines.append("")
lines.append("| Severity | NOT_MENTIONED | IMPLIED | MENTIONED | Total |")
lines.append("|---|---|---|---|---|")
for sev in ["severe", "moderate", "mild"]:
    ids = [h for h, s in sev_by_hadm.items() if s == sev]
    n_clean = sum(1 for h in ids if h in clean_ids)
    n_imp = sum(1 for h in ids if h in implied_ids)
    n_men = sum(1 for h in ids if VERDICTS.get(h, {}).get("verdict") == "MENTIONED")
    lines.append(f"| {sev} | {n_clean} | {n_imp} | {n_men} | {len(ids)} |")

out_path = ROOT / "hit_rates_resliced.md"
out_path.write_text("\n".join(lines))

print("\n".join(lines))
print(f"\nSaved: {out_path}")
