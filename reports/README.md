# QAK Migration Reports

| Phase | Date | Notes | Modified | Errors | Commit |
|-------|------|------:|----------:|-------:|--------|
| 1. Diseases | 2026-04-16 | 57 | 57 | 0 | ae9faae |
| 2. Genes | 2026-04-16 | 269 | 269 | 0 | a24570b |
| 3. Papers | 2026-04-16 | 722 | 722 | 0 | 1a19103 |
| 4. Clinical Trials | 2026-04-16 | 49 | 38 | 0 | 1c44b1c |
| 5. Therapeutic Strategies | 2026-04-16 | 32 | 32 | 0 | a1996ab |
| 6. Zettels | 2026-04-16 | 24 | 24 | 0 | 09d4f14 |
| 7. Roam Link Repair | 2026-04-16 | 255 | 119 | 0 | c7df0c7 |
| 8. Index Notes | 2026-04-16 | 10 | 10 | 0 | edea010 |
| 9a. AI Paper Summaries | 2026-04-16 | 439 | 411 | 0 | 950c33b |
| 9a+. AI Summaries (human comparison) | 2026-04-16 | 131 | 130 | 0 | 31c4d9a |
| 9b. SQLite Database | 2026-04-16 | 1,152 | — | 0 | — |
| 9c. Summary Notes | 2026-04-16 | — | 61 created | 0 | bb084ea |
| 9d. Alfred Workflow | 2026-04-16 | — | Go binary | 0 | — |

**Total notes modified: 1,812** (some files touched by multiple phases)
**QAK summary notes: 61** (auto-generated, overwritten each build)
**Total Roam links repaired: 197** (94 left as-is: infrastructure/unresolvable)
**AI summaries: 541 papers** (411 ai-only + 130 comparison alongside human)
**SQLite database: 1,152 rows across 7 tables, 788 junction links**
**Zero errors across all phases.**

## Pre-migration Checkpoint

```
Commit: e35ad0d (gitVault repo, main branch)
```

To revert everything:
```bash
git -C '/path/to/gitVault' reset --hard e35ad0d
```

## Phase Reports

- [Phase 1: Diseases](phase-1-diseases.md)
- [Phase 2: Genes](phase-2-genes.md)
- [Phase 3: Papers](phase-3-papers.md)
- [Phase 4: Clinical Trials](phase-4-trials.md)
- [Phase 5: Therapeutic Strategies](phase-5-strategies.md)
- [Phase 6: Zettels](phase-6-zettels.md)
- [Phase 7: Roam Link Repair](phase-7-roam-links.md)
- [Phase 8: Index Notes](phase-8-indexes.md)
- [Phase 9a: AI Paper Summaries](phase-9a-ai-summaries.md)
- [Phase 9b: SQLite Database](phase-9b-sqlite.md)
- Phase 9c: Summary Notes (61 auto-generated `QAK —` notes in vault)
- Phase 9d: Alfred Workflow (Go binary, `qak` + `zk` keywords)

## Usage

```bash
# Rebuild everything
make all

# Or step by step
make db          # Parse vault → qak.db
make summaries   # Regenerate QAK — summary notes
make build       # Compile Go binary

# Alfred keywords
qak <query>      # Search all: diseases, genes, papers, trials, strategies
zk <query>       # Search zettels only — Cmd+C copies the fact text
```
