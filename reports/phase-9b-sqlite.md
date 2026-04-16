# Phase 9b: SQLite Database — Build Report

- **Date:** 2026-04-16
- **Database:** qak.db (444 KB)
- **Script:** scripts/build_qak_db.py

## Table Row Counts

| Table | Rows |
|-------|-----:|
| diseases | 57 |
| genes | 269 |
| papers | 722 |
| clinical_trials | 38 |
| therapeutic_strategies | 32 |
| zettels | 24 |
| indexes | 10 |
| **Total** | **1,152** |

## Junction Table Links

| Junction Table | Links |
|----------------|------:|
| disease_paper | 340 |
| gene_paper | 261 |
| disease_trial | 70 |
| disease_gene | 52 |
| strategy_gene | 20 |
| disease_strategy | 18 |
| disease_zettel | 15 |
| zettel_gene | 8 |
| trial_gene | 3 |
| zettel_paper | 1 |

## Coverage

- Papers linked to at least one disease: 297/722 (41%)
- Genes linked to at least one disease: 45/269 (17%)
- Genes linked to at least one paper: 144/269 (53%)
- Paper summaries available: 541/722 (131 human + 411 AI)

## Top 5 Diseases by Paper Count

| Disease | Papers |
|---------|-------:|
| Alzheimer's Disease | 161 |
| Multiple Sclerosis | 26 |
| Huntington's Disease (HD) | 23 |
| ALS | 18 |
| AMD | 14 |

## Top 5 Genes by Paper Count

| Gene | Papers |
|------|-------:|
| APOE | 21 |
| TREM2 | 12 |
| LRRK2 | 8 |
| ALDH2 | 6 |
| GJB2 | 6 |

## Notes

- The builder re-creates the database from scratch each run (idempotent).
- Junction table links use fuzzy disease name matching (case-insensitive, substring) to resolve cross-references between note types.
- Many gene notes lack explicit disease annotations — disease-gene link count (52) is lower than expected. These links come from both disease notes' `genes` field and gene notes' `diseases` field.
- The `obs_summary` column is populated from `# OBSummary_AI` body sections or inline human `#obs` blocks.
