# Prototype A — Smallest Useful DDx Test

Goal: confirm the LLM can produce a sensible ranked DDx from a real ambulatory note before we build any infrastructure.

## What it does

1. Pulls 10 MTSamples cases across mixed specialties
2. Strips the Assessment/Diagnosis section from each (so the model can't cheat)
3. Asks Claude to produce a top-5 ranked DDx
4. Uses an LLM judge to check whether the gold diagnosis appears in the top 5
5. Writes a scored `results.md`

No FHIR server, no Synthea, no Bedrock. ~500 lines of Python.

## Setup

```bash
cd ml/prototype_a
python -m venv .venv && source .venv/bin/activate
pip install -e .

cp .env.example .env
# edit .env, paste your Anthropic API key
```

## Run

```bash
python fetch_cases.py     # pulls 10 cases into cases/  (~30s, polite delays)
python prepare_cases.py   # strips Assessment, writes gold.json + prepared/
python ddx.py             # runs Haiku, scores, writes results.md
```

Optional flags:
```bash
python ddx.py --model sonnet         # try a stronger model
python ddx.py --case 03              # run a single case
python ddx.py --judge sonnet         # stricter synonym judging
```

## Outputs

- `cases/NN_slug.txt` — raw notes (gitignored)
- `prepared/NN_slug.input.txt` — chart with Assessment removed (gitignored)
- `gold.json` — extracted ground-truth diagnoses (gitignored)
- `results.md` — scored output, hit@1/3/5 + per-case detail (gitignored)

## Decision gate

- ≥7/10 hit@5 → Option A passes, proceed to Option B (full pipeline)
- <7/10 hit@5 → fix the prompt, try Sonnet, or rethink before building infrastructure

## Cost

Under $1 with Haiku. Roughly:
- 10 DDx calls × ~3K input + 800 output ≈ 30K in / 8K out
- 50 judge calls × ~100 in + 5 out ≈ 5K in / 250 out
- Total: pennies on Haiku, ~$0.50 on Sonnet, ~$3 on Opus

## File map

```
prototype_a/
├── fetch_cases.py        # MTSamples scraper
├── prepare_cases.py      # strips Assessment, builds gold.json
├── ddx.py                # main DDx loop + scoring
├── prompts/
│   └── ddx_v1.txt        # the DDx prompt template
├── cases/                # raw notes (gitignored)
├── prepared/             # stripped charts (gitignored)
├── gold.json             # ground truth (gitignored)
├── results.md            # output (gitignored)
├── pyproject.toml
└── .env.example
```
