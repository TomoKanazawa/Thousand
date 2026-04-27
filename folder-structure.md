# Folder Structure (Rough Plan)

> ⚠️ **This is a rough plan, not final.** Expect to revise as the project takes shape — especially the `api/` layer (language TBD) and how `ml/shared/` evolves once both prototypes exist.

## Proposed layout

```
Andy/
├── README.md
├── docs/                       # all planning/strategy
│   ├── product-context.md
│   ├── dataset-strategy.md
│   ├── prototype-plan.md
│   ├── synth-ehr-build-plan.md
│   └── folder-structure.md     # this file
│
├── web/                        # Next.js frontend (existing app moves here)
│   ├── app/
│   ├── package.json
│   └── ...
│
├── api/                        # backend service (later, language TBD)
│
├── ml/                         # all Python / ML / data work
│   ├── prototype_a/            # Option A — smallest useful thing
│   │   ├── cases/              # MTSamples txt files
│   │   ├── gold.json
│   │   ├── ddx.py
│   │   └── results.md
│   ├── prototype_b/            # Option B — full pipeline at n=10
│   │   ├── generate_notes.py
│   │   ├── eval.py
│   │   └── ...
│   ├── shared/                 # prompts, eval harness, common utils
│   │   ├── prompts/
│   │   └── eval/
│   └── pyproject.toml
│
├── data/                       # gitignored — large, sensitive, regenerable
│   ├── mtsamples/
│   ├── mimic/                  # DUA-protected, never commit
│   ├── synthea/
│   └── synth_ehr_v0_1/
│
└── infra/                      # docker-compose, terraform (later)
    └── hapi-fhir/
```

## Three rules

1. **`data/` is always gitignored.** Datasets are large, often DUA-protected (MIMIC), and regenerable. Never commit.
2. **`ml/` is Python, `web/` is TypeScript, `api/` is TBD.** Don't cross the streams. Each gets its own dependency manifest.
3. **Prototypes are siblings, not nested.** `prototype_a` and `prototype_b` answer different questions and may diverge. Promote to `ml/shared/` only after both prototypes need the same thing.

## Migration steps

1. `mkdir -p docs web ml/prototype_a ml/prototype_b ml/shared data infra`
2. Move existing `app/`, `package.json`, `next.config.ts`, etc. into `web/`
3. Move all `*.md` planning docs into `docs/`
4. Add `data/` to `.gitignore`
5. Initialize `ml/pyproject.toml` (uv or poetry)

## Open questions

- **Backend language** — Python (shared with ML stack) vs TypeScript (shared with frontend)? Decide when API surface emerges.
- **Monorepo tooling** — npm workspaces / turborepo / nothing? Probably nothing until pain demands it.
- **Whether `ml/shared/` should be a real Python package** — defer until both prototypes import the same code.
- **Where prompts live** — `ml/shared/prompts/` vs versioned in each prototype. Likely shared once stable.
