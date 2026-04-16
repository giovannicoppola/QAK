# QAK Technical Reference

## Architecture

QAK is a three-stage pipeline:

```
Obsidian Vault (6,400+ markdown files)
    │
    ▼
[1] Python: build_qak_db.py ──► qak.db (SQLite, 444 KB)
    │
    ▼
[2] Python: generate_summaries.py ──► 61 "QAK —" notes in vault
    │
    ▼
[3] Go binary: qak ──► Alfred Script Filter JSON ──► Obsidian URI
```

Stage 1 parses YAML frontmatter from typed notes and populates a relational database. Stage 2 queries that database to produce aggregated Obsidian notes. Stage 3 is a compiled binary that queries the database at runtime and emits Alfred-compatible JSON.

## Repository Structure

```
QAK/
├── cmd/qak/main.go          # Alfred workflow binary (Go, 857 lines)
├── scripts/
│   ├── migrate_diseases.py   # Phase 1: disease note migration
│   ├── migrate_genes.py      # Phase 2: gene note migration
│   ├── migrate_papers.py     # Phase 3: paper note migration
│   ├── migrate_trials.py     # Phase 4: clinical trial migration
│   ├── migrate_strategies.py # Phase 5: therapeutic strategy migration
│   ├── migrate_zettels.py    # Phase 6: zettel note migration
│   ├── repair_roam_links.py  # Phase 7: Roam sub-page link repair
│   ├── migrate_indexes.py    # Phase 8: index note migration
│   ├── write_ai_summaries.py # Phase 9a: apply AI summaries to vault
│   ├── build_qak_db.py       # Phase 9b: vault → SQLite builder
│   └── generate_summaries.py # Phase 9c: SQLite → QAK summary notes
├── reports/                  # Per-phase migration reports
├── docs/                     # This documentation
├── source/icons/             # Alfred workflow icons
├── go.mod, go.sum            # Go module files
├── Makefile                  # Build automation
├── .gitignore
├── qak.db                    # Generated (not committed)
└── qak                       # Compiled binary (not committed)
```

## Vault Note Types

Each note type is identified by a `type:` field in its YAML frontmatter. Notes were migrated in phases 1–8, adding standardized frontmatter to existing files without deleting any text.

### Identification by filename prefix

| Type | Prefix | Example |
|------|--------|---------|
| paper | `@` | `@Lambert2013-ax.md` |
| gene | `^` | `^APOE.md` |
| zettel | `z ` | `z FTD prevalence 50,000 to 60,000.md` |
| disease | (plain name) | `Alzheimer's Disease.md` |
| clinical_trial | (identified by template fields) | `VALOR trial ❌.md` |
| therapeutic_strategy | (curated list) | `ALS therapeutic strategies.md` |
| index | (curated list) | `Alzheimer's  Index.md` |
| qak_summary | `QAK — ` | `QAK — Disease Overview.md` |

### YAML frontmatter fields by type

**disease**
```yaml
type: disease
created, updated, aliases, tags
prevalence_per_100k, incidence_per_100k, n_patients_us, lifetime_risk
omim, mondo, orphanet
gwas_largest_n, gwas_loci, gwas_paper
wes_largest_n, wes_loci, wes_paper
heritability_twin, heritability_gwas
genes: []            # gene symbols associated with this disease
projects: []         # active research projects
```

**gene**
```yaml
type: gene
created, updated, tags
symbol                # gene symbol (e.g., "APOE"), extracted from filename
full_name, aliases
chromosome, cytoband, protein_length
diseases: []          # disease names this gene is associated with
targeted_by: []       # therapeutic agents targeting this gene
therapeutic_notes
key_papers: []        # citekeys of important papers
```

**paper**
```yaml
type: paper
created, updated, tags
citekey               # e.g., "Lambert2013-ax", from filename
title, first_author, year, journal
study_type            # gwas, exome, clinical-trial, review, etc.
diseases: [], genes: []
n_cases, n_controls, n_total, n_loci
obs_source            # "human" | "ai" | (blank)
```

Paper summaries are stored in the note body, not in YAML:
- `# OBSummary_AI` — AI-generated ~250-char summary (411 papers). GWAS papers with `n_loci` have a `[Loci: N]` tag appended to the summary.
- Inline `#obs` block — human-written observations (131 papers)

**clinical_trial**
```yaml
type: clinical_trial
created, updated, tags
trial_name
nct_id, clinicaltrials_url
phase, status, outcome  # outcome: positive | negative | pending | (blank)
drug, modality, dose, company
diseases: [], target_genes: []
indication_detail, n_enrolled
primary_endpoint, secondary_endpoints: []
duration, estimated_completion
therapeutic_strategy, results_paper
```

**therapeutic_strategy**
```yaml
type: therapeutic_strategy
created, updated, tags
diseases: [], target_genes: []
modality              # antibody, antisense, small-molecule, gene-therapy, etc.
clinical_trials: []
```

**zettel**
```yaml
type: zettel
created, updated, tags
fact                  # the fact text, extracted from filename (strip "z " prefix)
diseases: [], genes: [], papers: []
category              # epidemiology, genetics, mechanism, pharmacology, clinical, other
```

**index**
```yaml
type: index
created, updated, tags
subject               # what the index covers (e.g., "Alzheimer's Disease")
subject_type          # disease, gene, misc
```

## SQLite Schema

### Entity tables (7)

| Table | Rows | Primary key | Unique constraint |
|-------|------|-------------|-------------------|
| diseases | 57 | id (autoincrement) | name |
| genes | 269 | id | symbol |
| papers | 722 | id | citekey |
| clinical_trials | 38 | id | — |
| therapeutic_strategies | 32 | id | name |
| zettels | 24 | id | — |
| indexes | 10 | id | — |

### Junction tables (10)

| Table | Links | Source(s) |
|-------|------:|-----------|
| disease_paper | 340 | papers.diseases[] |
| gene_paper | 261 | papers.genes[] + genes.key_papers[] |
| disease_trial | 70 | clinical_trials.diseases[] |
| disease_gene | 52 | diseases.genes[] + genes.diseases[] (bidirectional) |
| strategy_gene | 20 | therapeutic_strategies.target_genes[] |
| disease_strategy | 18 | therapeutic_strategies.diseases[] |
| disease_zettel | 15 | zettels.diseases[] |
| zettel_gene | 8 | zettels.genes[] |
| trial_gene | 3 | clinical_trials.target_genes[] |
| zettel_paper | 1 | zettels.papers[] |

### Metadata table

```sql
qak_meta (key TEXT PRIMARY KEY, value TEXT)
-- keys: 'built' (ISO timestamp), 'vault' (vault path)
```

### Disease name resolution

Junction tables use fuzzy matching to resolve disease names across note types:
1. Exact match against `diseases.name`
2. Case-insensitive match
3. Substring match (bidirectional: query in name OR name in query)

This handles variations like "Alzheimer's Disease" vs "Alzheimer's" vs "AD".

## YAML Parser

PyYAML is unavailable (PEP 668 prevents `pip install` on macOS system Python). All scripts use a hand-written `parse_existing_frontmatter()` function that handles:

- String values (with or without quotes)
- Numeric values (int and float, auto-detected by presence of `.`)
- Lists (both `- item` block style and `[item1, item2]` flow style)
- Empty values (`key:` and `key: []`)
- Quoted strings with special characters

The parser splits on `\n---` to separate frontmatter from body. It does not handle nested objects, multi-line strings, or anchors/aliases — none are used in the vault.

## Alfred Workflow Binary

### Build

```bash
make build
# Produces universal binary (arm64 + x86_64) via:
#   go build → qak-arm64
#   go build → qak-amd64
#   lipo -create → qak
```

Dependencies: `github.com/mattn/go-sqlite3` (CGO-based SQLite binding).

### Invocation

```
qak <query>         # wide search across all tables
qak --zk <query>    # zettel-only (alias for z: prefix)
```

### Tag prefix parsing

The binary checks if the query starts with a known prefix (case-insensitive):

| Prefix | Alias | Routes to |
|--------|-------|-----------|
| `disease:` | `d:` | `searchDiseases()` |
| `gene:` | `g:` | `searchGenes()` |
| `paper:` | `p:` | `searchPapers()` |
| `trial:` | `t:` | `searchTrials()` |
| `strategy:` | `s:` | `searchStrategies()` |
| `zettel:` | `z:`, `zk:` | `searchZettels()` |
| (none) | — | `searchAll()` (all 6 functions) |

### Search behavior

Each search function runs a `SELECT ... WHERE col1 LIKE ? OR col2 LIKE ? ...` query against all text columns in its table, plus joined tables where relevant. The LIKE pattern is `%query%`.

Wide search (`searchAll`) calls all 7 functions sequentially and concatenates results, capped at 40 total items. Individual searches are capped at 20 per type. Result priority order: **properties → diseases → genes → trials → strategies → zettels → papers**. Papers are last so that quick-fact results surface first.

### Property search

`searchProperties()` explodes entity fields into individual searchable items. It loads all rows from diseases, genes, papers, and clinical_trials, then builds an in-memory list of `(entity, label, value)` tuples. Fuzzy matching runs against the concatenation of entity name + label + value, so "als incid" matches entity "ALS" + label "incidence".

Searchable properties:
- **Diseases** (15 fields): prevalence, incidence, US patients, lifetime risk, OMIM, MONDO, Orphanet, GWAS largest N/loci/paper, WES largest N/loci/paper, heritability twin/GWAS
- **Genes** (4 fields): full name, chromosome, cytoband, protein length
- **Papers** (8 fields): study type, first author, year, journal, N cases/controls/total, N loci
- **Trials** (8 fields): drug, phase, outcome, status, N enrolled, modality, company, primary endpoint

The clipboard text (`arg`) includes the full label: `ALS incidence: 2 /100k`. The title shows `🦠 ALS — incidence: 2 /100k`.

### Output format

Alfred Script Filter JSON:

```json
{
  "items": [
    {
      "title": "🧬 APOE",
      "subtitle": "3 diseases, 21 papers",
      "arg": "[full note body text]",
      "uid": "gene:APOE",
      "text": {"copy": "[note body]", "largetype": "[note body]"},
      "mods": {
        "shift": {"arg": "obsidian://open?vault=gitVault&file=^APOE", "subtitle": "⇧↵ Open in Obsidian"}
      }
    }
  ]
}
```

### Action model

| Action | `arg` source | What happens |
|--------|-------------|-------------|
| Enter | `arg` (note body / summary) | Text copied to clipboard |
| Cmd+L | `text.largetype` | Full note displayed in Large Type overlay |
| Cmd+C | `text.copy` | Same as Enter (quick copy while browsing) |
| Shift+Enter | `mods.shift.arg` | Opens `obsidian://` URI in Obsidian |
| Cmd+Enter | `mods.cmd.arg` (papers only) | Copies full raw note body |

For papers, the default `arg` is the summary (human or AI). Cmd+Enter gives the full raw note body instead. For all other types, `arg` is the full note body (frontmatter stripped).

The binary reads note files from the vault at query time to populate `arg` and `text` fields. File reads add ~5ms per result; total query time is 12–40ms for typical searches, up to ~250ms for broad terms that hit many results (e.g., "Alzheimer" across 40 notes).

- `uid` enables Alfred result ordering memory

## Migration Phases

All migrations were run on 2026-04-16 against the gitVault repo. A pre-migration checkpoint was created at commit `e35ad0d`.

| Phase | Script | Notes processed | Modified | Commit |
|-------|--------|----------------:|----------:|--------|
| 1 | migrate_diseases.py | 57 | 57 | ae9faae |
| 2 | migrate_genes.py | 269 | 269 | a24570b |
| 3 | migrate_papers.py | 722 | 722 | 1a19103 |
| 4 | migrate_trials.py | 49 | 38 | 1c44b1c |
| 5 | migrate_strategies.py | 32 | 32 | a1996ab |
| 6 | migrate_zettels.py | 24 | 24 | 09d4f14 |
| 7 | repair_roam_links.py | 255 | 119 | c7df0c7 |
| 8 | migrate_indexes.py | 10 | 10 | edea010 |
| 9a | write_ai_summaries.py | 439+131 | 541 | 950c33b, 31c4d9a |
| 9b | build_qak_db.py | 1,152 | — | — |
| 9c | generate_summaries.py | — | 61 | bb084ea |
| 9d | cmd/qak/main.go | — | — | 5cfa523 |

**Zero errors across all phases.**

### Phase details

**Phase 1–6** (note migrations): Each script reads all matching files from the vault, parses any existing YAML frontmatter, builds a new frontmatter dict with the standardized fields, extracts values from the note body using regex patterns (disease names, gene symbols, citekeys, sample sizes, etc.), and writes the updated file. No text is ever deleted — only YAML properties are added or updated.

**Phase 7** (Roam link repair): Finds `[[Roam/giov-2026-01-29-19-08-45/...]]` links and classifies them into 4 categories:
- A: Sub-topic links → `[[Note#Section|alias]]`
- B: Paper references → prefix stripped
- C: Daily note references → resolved if daily note exists
- D: Infrastructure/unresolvable → left as-is

197 links repaired across 119 files, 94 left as-is. Audit comments appended to repaired files.

**Phase 9a** (AI summaries): 440 papers with body content > 30 chars but no human `#obs` block were processed in 8 parallel batches. Each batch was handled by a separate Claude agent that read the note body and generated a ~250-character factual summary. Results were written to JSONL files, merged, and applied to vault files by `write_ai_summaries.py`. An additional 130 summaries were generated for papers that already had human summaries, for comparison — these were appended as `# OBSummary_AI` without changing `obs_source: human`.

## Rebuilding

The full pipeline is idempotent:

```bash
make all
```

This runs:
1. `build_qak_db.py` — deletes and recreates `qak.db` from vault YAML
2. `generate_summaries.py` — overwrites all `QAK —` notes from database
3. `go build` — recompiles the binary

The migration scripts (phases 1–8) are one-time operations and are not re-run by `make all`. The AI summary generation (phase 9a) is also one-time — summaries are stored in the note files and persist across rebuilds.

## Known Limitations

- **Disease-trial over-linking**: Phase 4 trial migration used aggressive disease pattern matching in body text, causing some trials to be linked to diseases they don't study (e.g., AD trials appearing under ALS). The YAML `diseases` field in trial notes should be manually reviewed.
- **Gene sub-page notes**: Roam-era sub-page files like `^LRRK2 – Therapeutic Strategies.md` have `symbol: "LRRK2 – Therapeutic Strategies"` which is incorrect. These are navigation pages, not gene entries.
- **Low junction coverage**: Only 45/269 genes are linked to a disease, and 297/722 papers to a disease. Many notes lack explicit cross-references in their YAML — the junction table is only as complete as the frontmatter.
- **No full-text search**: The Alfred binary uses SQL LIKE patterns, not FTS. For a 444 KB database this is fast enough (<15ms), but if the vault grows significantly, adding an FTS5 virtual table would be advisable.
- **YAML parser limitations**: The hand-written parser does not support nested objects, multi-line strings (`|`, `>`), anchors (`&`/`*`), or flow mappings (`{key: val}`). None of these are currently used in the vault.
