"""Pilot v2 — goal-oriented LLM redaction pipeline (Haiku).

Three stages:
  Stage 1: Haiku reads ORIGINAL chart + hidden dx + EXPLICIT BENCHMARK GOAL,
           returns list of exact leak substrings to redact.
           Saved to pilot_hide_one_v2/<hadm_id>/leak_strings.json.
  Stage 2: Deterministic build — applies regex scrub + literal string replace.
           Writes chart.txt + redaction_log.txt (for over-redaction review).
  Stage 3: Haiku reads SCRUBBED chart + hidden dx + same goal, returns any
           REMAINING leaks. Should be empty on clean cases.

The key change from before: every LLM call is explicitly told the BENCHMARK
GOAL so it can distinguish "clinical evidence to preserve" from "leak to
remove."

Usage:
  python3 pilot_v2_redact.py                 # all 9 cases
  python3 pilot_v2_redact.py --cases 20514903
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

from anthropic import APIError, Anthropic
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
V1 = ROOT / "pilot_hide_one"
V2 = ROOT / "pilot_hide_one_v2"
MODEL = "claude-haiku-4-5"

# Base regex patterns: catch the obvious dx-name spellings before LLM runs.
DEFAULT_PATTERNS_BY_HIDDEN: dict[str, list[str]] = {
    "Pneumonia, unspecified organism": [r"\bpneumonia\b", r"\bpna\b", r"pneumonic"],
    "Urinary tract infection, site not specified": [r"\buti\b", r"urinary tract infect", r"cystitis", r"pyelonephritis"],
    "Cellulitis of abdominal wall": [r"\bcellulitis\b"],
    "Acute diastolic (congestive) heart failure": [r"heart failure", r"\bchf\b", r"decompensat", r"congestive"],
    "Noninfective gastroenteritis and colitis, unspecified": [r"gastroenteritis", r"\bcolitis\b", r"\bgastritis\b"],
    "Other severe protein-calorie malnutrition": [r"malnutrition", r"malnourished", r"cachexia", r"cachectic"],
    "Other cholelithiasis without obstruction": [r"cholelith", r"gallstone"],
    "Infectious mononucleosis": [r"mononucleosis", r"\bmono\b", r"\bEBV\b", r"epstein", r"monospot"],
    "Syndrome of inappropriate secretion of antidiuretic hormone": [r"\bSIADH\b", r"antidiuretic", r"syndrome of inappropriate"],
}


GOAL_FRAMING = """\
WE ARE BUILDING A BENCHMARK to test whether an LLM can detect missed diagnoses from a clinical chart.

The benchmark works like this:
  - We hide ONE diagnosis from the chart.
  - A downstream LLM reads the chart and must infer the hidden diagnosis from the REMAINING CLINICAL EVIDENCE (labs, vitals, imaging findings, history, physical exam, urinalysis, etc.).
  - The benchmark is fair ONLY if the chart still contains the *evidence* pointing toward the diagnosis, but NEVER contains anything that reveals a clinician already recognized/suspected the diagnosis.

THE TEST (apply to every candidate string):
"Would this string still appear in the chart if NO clinician had ever recognized or suspected the hidden diagnosis?"

  • YES — it would still appear regardless of clinician awareness → KEEP. It's pathophysiology / evidence the benchmark NEEDS.
  • NO — it only appears because a clinician already recognized or suspected the dx → REDACT. It's a "tell" that short-circuits reasoning.

EXAMPLES (apply this test):

  KEEP (evidence — present regardless of clinician awareness):
  • Raw lab values: WBC 26, atypical lymphs 16%, serum osmolality 273, urine osm 877, urine Na 89, creatinine 3.4, K 5.4 — labs are ordered for general workup and the results report themselves; they appear whether or not anyone recognized the dx
  • Vital signs, oxygen sat, urine output, weights
  • Imaging FINDINGS (raw radiology observations): "opacity at left lung base", "cardiac silhouette enlarged", "echogenic foci in gallbladder", "filling defect in pulmonary artery", "leptomeningeal enhancement" — these describe what the radiologist actually saw on the image; they are reported regardless
  • Physical exam findings: erythema, warmth, decreased breath sounds, JVD, abdominal tenderness — observed regardless
  • Patient-reported symptoms and HPI (cough, dyspnea, fever, abdominal pain) — said by patient regardless
  • PMH and comorbidities unrelated to the hidden dx

  REDACT (clinician awareness / action — only present because the dx was recognized):
  • The diagnosis NAME, its abbreviations, or close synonyms anywhere in the chart
  • TREATMENTS that are specifically chosen for this dx: Nitrofurantoin (UTI-specific), TPN/amino acids IV (severe malnutrition), tPA (stroke/MI), thrombolytics (PE), specific narrow-spectrum antibiotics chosen after culture, RRT for AKI
  • SPECIALTY CONSULT notes whose reason references the dx (nephrology consult for AKI, ID consult for endocarditis)
  • Radiology IMPRESSIONS or CONCLUSIONS that interpret findings as the dx ("consistent with pneumonia", "diagnostic of cholelithiasis") — distinct from raw findings, these reveal radiologist recognition
  • Recorded STAGE/GRADE/SEVERITY for the hidden dx (KDIGO Stage 2, Killip class III)
  • Truncation stubs adjacent to prior [REDACTED] markers that telegraph the dx
  • DISEASE-SPECIFIC tests/imaging ordered only because clinician suspected the dx (q4h finger sticks → diabetes; "serial troponins for r/o MI"; flow cytometry panel CD3/CD4/CD20 etc. → lymphoid/EBV; gallbladder ultrasound → biliary disease; "Hep C antibody" → hep C)
  • The dx mentioned as the reason for any order, lab, or intervention

CRUCIAL: GENERIC VS DISEASE-SPECIFIC (the most common over-flagging error)

A test, exam, treatment, or monitoring is a REDACT only if it WOULD NOT have been done without suspicion of the hidden dx. If it's a routine/generic part of standard workup that would happen for many reasons, KEEP it. Apply this carefully:

  KEEP — GENERIC (would happen without dx suspicion):
  • Routine PHYSICAL EXAM components: RUQ/LUQ/RLQ/LLQ tenderness, JVD, edema check, breath-sound exam, neuro exam, skin exam — these are done on every patient with relevant complaints; the FINDING reports itself
  • Routine BLOOD WORK: CBC, BMP/CMP, LFTs, coags, lactate, ABG, magnesium, phosphorus, calcium — drawn on basically any sick admission
  • Routine URINALYSIS components (WBC, RBC, leukocytes, nitrite, bacteria, ketones) — UA is ordered for many reasons (altered mental status, fever, abdominal pain, admission); the components report themselves
  • Standard IMAGING (CXR, CT abd/pelvis, CT head, bedside US) when ordered for broad indications
  • Therapeutic drug MONITORING for any drug already running (vancomycin trough, digoxin level, tacro level) — these monitor what's been started, they don't reveal why it was started
  • Generic ELECTROLYTE REPLETION (KCl, MgSO4, calcium gluconate, IV fluids) — given for many causes of derangement
  • BROAD-SPECTRUM antibiotics with many indications: vancomycin, piperacillin-tazobactam, ceftriaxone (alone), levofloxacin (alone), meropenem
  • Routine prophylaxis: heparin SQ for DVT, PPI, bowel regimen

  REDACT — DISEASE-SPECIFIC (only happens because dx was suspected):
  • Tests with narrow indications: monospot, EBV serology, ferritin/prealbumin (if hidden dx is nutritional), TSH (if hidden dx is thyroid), echo (if hidden dx is cardiac), HbA1c (if hidden dx is diabetes), flow cytometry/immunophenotyping panel
  • Imaging chosen for one organ system that matches the hidden dx: dedicated gallbladder US, CT for r/o PE, MRI brain for stroke
  • Narrow-spectrum antibiotics chosen for one organism: nitrofurantoin (UTI), oseltamivir (flu), acyclovir (HSV/VZV)
  • Disease-specific interventions: jejunostomy/PEG tube (nutritional failure), IVC filter (PE), pacemaker (heart block)
  • Consults whose reason matches the dx: nephrology, infectious disease (when consult name reveals dx)
  • Clinical syndrome labels that ARE the dx: "failure to thrive" (≈malnutrition), "encephalopathy" (≈toxic/metabolic dx), "anuria" (≈AKI)

The principle: pathophysiology stays; clinician awareness/action goes. When borderline, ask "would this be in the chart of a sick patient EVEN IF this specific dx had never crossed anyone's mind?" If yes → KEEP. If it would only be there because someone suspected → REDACT.

HIDDEN DIAGNOSIS: {hidden}
"""


STAGE1_PROMPT = GOAL_FRAMING + """

Identify every candidate substring in the chart below that could plausibly be considered a "tell" for the hidden diagnosis. For EACH candidate, you must COMMIT to a binary action:

  • action = "REDACT" → this substring would NOT be in the chart if no clinician had recognized/suspected the hidden dx. It must be removed.
  • action = "KEEP"   → this substring WOULD still be in the chart even with no clinician awareness. It is evidence the benchmark needs.

You may NOT mark a string both — pick one.

Output STRICT JSON only — no commentary, no markdown:
{{
  "candidates": [
    {{"snippet": "exact verbatim substring", "action": "REDACT", "why": "one short sentence"}},
    {{"snippet": "exact verbatim substring", "action": "KEEP",   "why": "one short sentence"}}
  ]
}}

Rules:
- Quote VERBATIM from the chart so literal find-and-replace will match.
- Prefer the SHORTEST substring that captures the tell.
- If you cite a string as "KEEP" because it is evidence, that's fine and useful — but ONLY items with action="REDACT" will be removed.
- If nothing leaks, return {{"candidates": []}}.

CHART:
---
{chart}
---
"""


STAGE3_PROMPT = GOAL_FRAMING + """

The chart below has ALREADY been scrubbed. Your job: identify any REMAINING tells the previous pass missed. Apply the SAME counterfactual test ("would this appear if no clinician had ever recognized/suspected the dx?").

For each candidate, COMMIT to a binary action:
  • "REDACT" → real remaining tell that must be removed
  • "KEEP"   → looks suspicious but is actually evidence that should stay

Output STRICT JSON only:
{{
  "candidates": [
    {{"snippet": "exact substring", "action": "REDACT", "why": "one sentence"}},
    {{"snippet": "exact substring", "action": "KEEP",   "why": "one sentence"}}
  ]
}}

Only items with action="REDACT" count as remaining leaks. If you're not sure something is a tell, mark it "KEEP". Be honest — do NOT mark evidence as REDACT because it correlates with the dx.

SCRUBBED CHART:
---
{chart}
---
"""


def call_with_retry(fn, max_retries=5, initial_delay=4.0):
    delay = initial_delay
    for attempt in range(max_retries):
        try:
            return fn()
        except APIError as e:
            if attempt == max_retries - 1:
                raise
            wait = delay * (2 ** attempt)
            print(f"    retry after {wait:.0f}s ({type(e).__name__}: {e})", file=sys.stderr, flush=True)
            time.sleep(wait)


def extract_json(text: str) -> dict:
    text = text.strip()
    text = re.sub(r"^```(?:json)?|```$", "", text, flags=re.MULTILINE).strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    start = text.find("{")
    if start == -1:
        raise ValueError(f"no JSON: {text[:200]}")
    depth = 0
    end = -1
    for i in range(start, len(text)):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                end = i + 1
                break
    if end == -1:
        raise ValueError("unbalanced braces")
    return json.loads(text[start:end])


def stage1_detect(client, hadm_id: int, original_chart: str, hidden_title: str) -> tuple[list[str], list[dict]]:
    """Return (leak_strings_to_redact, full_candidate_list_for_logging)."""
    print(f"  [{hadm_id}] Stage 1: detecting leaks …", flush=True)
    prompt = STAGE1_PROMPT.format(hidden=hidden_title, chart=original_chart)
    resp = call_with_retry(lambda: client.messages.create(
        model=MODEL, max_tokens=3500,
        messages=[{"role": "user", "content": prompt}],
    ))
    parsed = extract_json(resp.content[0].text)
    candidates = parsed.get("candidates", [])
    seen = set()
    redact_strings = []
    for c in candidates:
        if not isinstance(c, dict):
            continue
        s = (c.get("snippet") or "").strip()
        if c.get("action") != "REDACT":
            continue
        if len(s) < 3 or s in seen:
            continue
        seen.add(s)
        redact_strings.append(s)
    return redact_strings, candidates


def stage2_build(hadm_id: int, original_chart: str, hidden_title: str,
                 leak_strings: list[str], out_dir: Path) -> dict:
    out_dir.mkdir(parents=True, exist_ok=True)
    base_patterns = DEFAULT_PATTERNS_BY_HIDDEN.get(hidden_title, [])

    # 1. Regex scrub: line-level, log redacted lines
    compiled = [re.compile(p, re.IGNORECASE) for p in base_patterns]
    original_lines = original_chart.splitlines()
    scrubbed_lines = []
    regex_log: list[dict] = []
    for i, line in enumerate(original_lines, 1):
        if any(rx.search(line) for rx in compiled):
            scrubbed_lines.append("[REDACTED]")
            regex_log.append({"line": i, "original": line.rstrip()[:200]})
        else:
            scrubbed_lines.append(line)
    text = "\n".join(scrubbed_lines)

    # 2. LLM string-replace: log each replacement with surrounding context
    string_log: list[dict] = []
    for s in sorted(set(leak_strings), key=lambda x: -len(x)):
        if not s:
            continue
        # Find offsets BEFORE replacing (for the log)
        offsets = []
        idx = 0
        while (pos := text.find(s, idx)) != -1:
            offsets.append(pos)
            idx = pos + 1
        if offsets:
            for pos in offsets:
                ctx_start = max(0, pos - 40)
                ctx_end = min(len(text), pos + len(s) + 40)
                string_log.append({
                    "substring": s,
                    "context": text[ctx_start:ctx_end].replace("\n", " ⏎ "),
                })
            text = text.replace(s, "[REDACTED]")
    return {
        "scrubbed_text": text,
        "regex_log": regex_log,
        "string_log": string_log,
    }


def stage3_verify(client, hadm_id: int, scrubbed_chart: str, hidden_title: str) -> dict:
    print(f"  [{hadm_id}] Stage 3: verifying scrubbed chart …", flush=True)
    prompt = STAGE3_PROMPT.format(hidden=hidden_title, chart=scrubbed_chart)
    resp = call_with_retry(lambda: client.messages.create(
        model=MODEL, max_tokens=2500,
        messages=[{"role": "user", "content": prompt}],
    ))
    parsed = extract_json(resp.content[0].text)
    candidates = parsed.get("candidates", [])
    redacts = [c for c in candidates if isinstance(c, dict) and c.get("action") == "REDACT"]
    keeps = [c for c in candidates if isinstance(c, dict) and c.get("action") == "KEEP"]
    return {
        "all_candidates": candidates,
        "remaining_leaks": redacts,
        "explicit_keeps": keeps,
        "n_remaining": len(redacts),
    }


def load_v1_cases() -> list[dict]:
    mf = json.loads((V1 / "manifest.json").read_text())
    cases = []
    for e in mf:
        # Include all batches (1, 2, 3) — 100 cases total
        cases.append({"hadm_id": e["hadm_id"], "hidden_title": e["hidden_title"]})
    out = []
    for c in cases:
        d = V1 / str(c["hadm_id"])
        out.append({
            **c,
            "visible": json.loads((d / "visible_dx.json").read_text()),
            "hidden": json.loads((d / "hidden_dx.json").read_text()),
        })
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cases", nargs="*", type=int, default=None)
    args = parser.parse_args()

    load_dotenv(ROOT.parent / "prototype_a" / ".env", override=True)
    if not os.getenv("ANTHROPIC_API_KEY"):
        sys.exit("ANTHROPIC_API_KEY not set")

    cases = load_v1_cases()
    if args.cases:
        cases = [c for c in cases if c["hadm_id"] in set(args.cases)]
    print(f"Processing {len(cases)} cases through v2 (Haiku, goal-oriented prompt) …\n")
    client = Anthropic()

    summary = []
    for c in cases:
        hadm = c["hadm_id"]
        out_dir = V2 / str(hadm)
        out_dir.mkdir(parents=True, exist_ok=True)
        original = (DATA / str(hadm) / "pre_discharge.input.txt").read_text()

        # Stage 1
        try:
            leak_strings, full_candidates = stage1_detect(client, hadm, original, c["hidden_title"])
        except BaseException as e:
            print(f"  [{hadm}] Stage 1 ERROR: {type(e).__name__}: {e}", flush=True)
            continue
        n_keeps = sum(1 for k in full_candidates if isinstance(k, dict) and k.get("action") == "KEEP")
        (out_dir / "leak_strings.json").write_text(json.dumps({
            "hidden_title": c["hidden_title"],
            "leak_strings": leak_strings,             # REDACT-only, used by Stage 2
            "all_candidates": full_candidates,        # both REDACT and KEEP, for review
        }, indent=2))
        print(f"    Stage 1 → {len(leak_strings)} REDACT, {n_keeps} KEEP", flush=True)

        # Stage 2
        build = stage2_build(hadm, original, c["hidden_title"], leak_strings, out_dir)
        (out_dir / "chart.txt").write_text(build["scrubbed_text"])
        (out_dir / "visible_dx.json").write_text(json.dumps(c["visible"], indent=2))
        (out_dir / "hidden_dx.json").write_text(json.dumps(c["hidden"], indent=2))
        # Save full redaction log for human review
        log_path = out_dir / "redaction_log.json"
        log_path.write_text(json.dumps({
            "hadm_id": hadm,
            "hidden_title": c["hidden_title"],
            "regex_redacted_lines": build["regex_log"],
            "string_replacements": build["string_log"],
            "n_regex_lines": len(build["regex_log"]),
            "n_string_replacements": len(build["string_log"]),
        }, indent=2))
        print(f"    Stage 2 → regex={len(build['regex_log'])} lines, "
              f"string-replace={len(build['string_log'])} matches", flush=True)

        # Stage 3
        try:
            verify = stage3_verify(client, hadm, build["scrubbed_text"], c["hidden_title"])
        except BaseException as e:
            print(f"    Stage 3 ERROR: {type(e).__name__}: {e}", flush=True)
            verify = {"error": str(e), "n_remaining": -1, "remaining_leaks": []}
        (out_dir / "verification.json").write_text(json.dumps(verify, indent=2))
        n_rem = verify["n_remaining"]
        status = "✅ clean" if n_rem == 0 else f"⚠️  {n_rem} remaining"
        print(f"    Stage 3 → {status}", flush=True)
        summary.append({
            "hadm_id": hadm,
            "hidden": c["hidden_title"],
            "n_leaks_found": len(leak_strings),
            "n_remaining": n_rem,
        })

    print(f"\n=== Summary ===")
    print(f"{'hadm_id':<11} {'hidden':<55} {'found':>6} {'remaining':>10}")
    print("-" * 90)
    for s in summary:
        mark = "✅" if s["n_remaining"] == 0 else "⚠️ "
        print(f"{s['hadm_id']:<11} {s['hidden'][:54]:<55} {s['n_leaks_found']:>6} {s['n_remaining']:>10}  {mark}")
    n_clean = sum(1 for s in summary if s["n_remaining"] == 0)
    print(f"\nClean after Stage 3: {n_clean}/{len(summary)}")


if __name__ == "__main__":
    main()
