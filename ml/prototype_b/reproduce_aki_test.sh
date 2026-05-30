#!/usr/bin/env bash
# Reproduce the KDIGO never-detected AKI benchmark end-to-end.
#
# Prerequisites:
#   - PhysioNet credentials (MIMIC-IV v3.1 + MIMIC-IV-Note 2.2) under physionet.org/
#   - ANTHROPIC_API_KEY in prototype_a/.env
#   - Python deps: pandas, anthropic, python-dotenv
#
# Runtime: ~12 min total. Cost: ~$1.56 in API calls.
#
# Expected headline result: 94% hit@15 at admit cutoff (n=100, Haiku 4.5).

set -euo pipefail
cd "$(dirname "$0")"

echo "[1/3] Selecting Tier 2 candidates from MIMIC-IV (~5 min)..."
python kdigo_aki_finder.py --sample-n 100 --seed 42

echo "[2/3] Building leak-safe chart inputs (~2 min)..."
python stitch_case.py \
  --selected selected_admissions_aki.json \
  --out-dir data_aki

echo "[3/3] Running Haiku DDx + scoring AKI hit rate (~5 min, ~\$1.56)..."
python aki_test.py --model haiku --cutoffs admit plus24h

echo
echo "Done. Results in results_aki_haiku.json and console table above."
