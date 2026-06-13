"""Pilot v2 pass 3 — re-verify scrubbed charts and report any remaining REDACTs.

Reads chart.txt (already through 2 redaction passes) and runs the same Stage 3
prompt again. Saves remaining_leaks to pass3_verification.json per case.

Does NOT auto-apply — user reviews and decides.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

from anthropic import Anthropic
from dotenv import load_dotenv

# Reuse the same prompt + helpers from pilot_v2_redact
sys.path.insert(0, str(Path(__file__).parent))
from pilot_v2_redact import STAGE3_PROMPT, call_with_retry, extract_json, MODEL  # noqa: E402

ROOT = Path(__file__).resolve().parent
V2 = ROOT / "pilot_hide_one_v2"

CASES = [20514903, 28898389, 22501264, 24420954, 28255293,
         21318246, 22669030, 23793305, 21452016]


def verify_pass3(client, hadm: int, scrubbed: str, hidden_title: str) -> dict:
    prompt = STAGE3_PROMPT.format(hidden=hidden_title, chart=scrubbed)
    resp = call_with_retry(lambda: client.messages.create(
        model=MODEL, max_tokens=2500,
        messages=[{"role": "user", "content": prompt}],
    ))
    parsed = extract_json(resp.content[0].text)
    candidates = parsed.get("candidates", [])
    redacts = [c for c in candidates if isinstance(c, dict) and c.get("action") == "REDACT"]
    keeps = [c for c in candidates if isinstance(c, dict) and c.get("action") == "KEEP"]
    return {"all_candidates": candidates, "remaining_leaks": redacts,
            "explicit_keeps": keeps, "n_remaining": len(redacts)}


def main() -> None:
    load_dotenv(ROOT.parent / "prototype_a" / ".env", override=True)
    if not os.getenv("ANTHROPIC_API_KEY"):
        sys.exit("ANTHROPIC_API_KEY not set")
    client = Anthropic()

    print(f"Pass 3 verification on {len(CASES)} cases …\n")
    rows = []
    for h in CASES:
        d = V2 / str(h)
        chart = (d / "chart.txt").read_text()
        hidden = json.loads((d / "hidden_dx.json").read_text())["title"]
        print(f"  [{h}] checking …", flush=True)
        try:
            v = verify_pass3(client, h, chart, hidden)
            (d / "pass3_verification.json").write_text(json.dumps(v, indent=2))
            print(f"    → {v['n_remaining']} REDACT remaining, {len(v['explicit_keeps'])} KEEP",
                  flush=True)
            rows.append((h, hidden, v["n_remaining"]))
        except Exception as e:
            print(f"    ERROR: {type(e).__name__}: {e}", flush=True)
            rows.append((h, hidden, -1))

    print(f"\n=== Pass 3 summary ===")
    print(f"{'hadm_id':<11} {'hidden':<52} {'remaining'}")
    print("-" * 80)
    for h, hid, n in rows:
        mark = "✅" if n == 0 else ("⚠️ " if n > 0 else "❌")
        print(f"{h:<11} {hid[:51]:<52} {n if n >= 0 else 'ERROR'}  {mark}")
    n_clean = sum(1 for _, _, n in rows if n == 0)
    print(f"\nClean after pass 3: {n_clean}/{len(rows)}")


if __name__ == "__main__":
    main()
