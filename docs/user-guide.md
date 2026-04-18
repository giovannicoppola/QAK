# QAK User Guide

QAK (Query Alfred Knowledge) is a search tool that lets you instantly query your gitVault Obsidian vault from Alfred. It searches across diseases, genes, papers, clinical trials, therapeutic strategies, and zettel facts.

## Quick Start

1. Open Alfred and type `qak` followed by your search term
2. Results appear instantly, grouped by type with emoji prefixes
3. Press **Enter** to copy the note text to clipboard (and paste it wherever you need)
4. Press **Cmd+L** to read the full note in Large Type without leaving Alfred
5. Press **Shift+Enter** to open the note in Obsidian

## Search Modes

### Wide Search (default)

Type `qak` followed by any keyword. QAK searches across **all text fields in all tables** simultaneously.

```
qak APOE           → genes, papers, trials, zettels mentioning APOE
qak tofersen        → the drug, its trials, and papers about it
qak antisense       → strategies, papers, trials involving antisense
qak Alzheimer       → the disease, all related papers, trials, strategies
qak meta-analysis   → papers with that study type
qak complement      → genes, strategies, papers about complement
```

Results are prioritized: **properties → diseases → genes → trials → strategies → zettels → papers**. Papers appear last so that quick-fact results (like prevalence or GWAS loci) surface first.

### Property Search

QAK also searches individual database fields as standalone items, so you can look up a specific fact without opening the full note.

```
qak als incid       → ALS incidence: 2 /100k     (copied to clipboard)
qak als prev        → ALS prevalence: 4.5 /100k
qak alz gwas loci   → Alzheimer's Disease GWAS loci: 38 (Wightman2021-je)
qak APP chrom       → APP chromosome: 21
qak GBA protein     → GBA protein length: 536 aa
```

Property results show as `🦠 ALS — incidence: 2 /100k`. Pressing Enter copies the full label and value to clipboard (e.g., `ALS incidence: 2 /100k`).

GWAS/WES loci and sample size properties include the paper citekey in parentheses for quick reference. Press **Cmd+Enter** on a GWAS/WES loci result to drill down into the associated genes.

Searchable properties include:
- **Diseases**: prevalence, incidence, US patients, lifetime risk, disease duration, OMIM/MONDO/Orphanet, GWAS/WES stats, heritability, prevalence by age
- **Genes**: full name, chromosome, cytoband, protein length
- **Trials**: drug, phase, outcome, status, enrollment, modality, company, endpoint

### Filtered Search

Prefix your query with a type tag to restrict results to one entity type.

| Tag | Short | What it searches |
|-----|-------|-----------------|
| `disease:` | `d:` | Disease names, OMIM/MONDO IDs |
| `gene:` | `g:` | Gene symbols, full names, therapeutic notes |
| `paper:` | `p:` | Citekeys, authors, titles, summaries, study types, journals |
| `trial:` | `t:` | Trial names, drugs, modalities, companies, NCT IDs, endpoints, diseases |
| `strategy:` | `s:` | Strategy names, modalities, diseases, target genes |
| `zettel:` | `z:` | Fact text, categories, diseases, genes |

Examples:

```
qak t:Phase 3       → only clinical trials mentioning "Phase 3"
qak p:gwas           → only papers with "gwas" in any field
qak d:AMD            → only diseases matching "AMD"
qak g:TREM2          → only gene entries matching "TREM2"
qak s:antibody       → only strategies with "antibody" in modality/name
qak z:prevalence     → only zettel facts about prevalence
```

### Zettel Keyword

If you set up a separate `zk` Alfred keyword, it works as a shortcut for zettel-only search:

```
zk prevalence        → zettel facts containing "prevalence"
zk APOE              → APOE-related facts (allele frequencies, PAF, etc.)
```

Cmd+C on a zettel result copies the fact text to clipboard.

## Result Types

Each result is prefixed with an emoji indicating its type:

| Emoji | Type | What you see |
|-------|------|-------------|
| `🦠` | Disease | Name, US patients, prevalence, GWAS loci, paper/trial counts |
| `🧬` | Gene | Symbol, full name, chromosome, disease/paper counts |
| `📄` | Paper | Author (year) — Title, distinction, study type, sample size, summary source |
| `💊` | Trial | Trial name, drug, phase, outcome, disease(s) |
| `🎯` | Strategy | Name, modality, disease(s), target genes |
| (none) | Zettel | Fact text, category, disease/gene tags |

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| **Enter** | Copy note text to clipboard (summary for papers, full body for others) |
| **Cmd+L** | Large Type — read the full note text in a floating overlay |
| **Cmd+C** | Quick copy while browsing (same as Enter) |
| **Shift+Enter** | Open the note in Obsidian |
| **Cmd+Enter** | Papers: copy abstract (or full note if no abstract). Properties: epi or gene drill-down |
| **Ctrl+Enter** | Search ClinicalTrials.gov (on disease results) |
| **Alt+Enter** | Search GWAS Catalog — by trait (diseases) or by gene (genes) |
| **Cmd+Alt+Enter** | Open Gene Browser (on gene results) |

The default action (Enter) is designed for quick information access without leaving your current app. For papers, it copies the summary; use Cmd+Enter if you want the full raw note instead.

### Epi Calculator

When viewing a prevalence or incidence property result, press **Cmd+Enter** to drill down into derived epidemiological measures:

- Rate per 100k and per million
- 1-in-N ratio
- Estimated US, EU-5, and worldwide patient counts
- Birth-based estimates (yearly US and worldwide births)
- **Age-stratified breakdown** (if `prevalence_by_age` data is available): shows estimated patient counts per age band for US and EU-5, using census population data

26 diseases currently have age-stratified prevalence data sourced from published meta-analyses (e.g., Tham 2014 for Glaucoma, Pringsheim 2014 for Parkinson's). Sources are cited in each disease note body.

### Cross-Workflow Bridges

QAK can hand off to external Alfred workflows using modifier keys:

| Modifier | Context | Target Workflow |
|----------|---------|----------------|
| **Ctrl+Enter** | Disease result | ClinicalTrials.gov search (alfred-clinicalTrials) |
| **Alt+Enter** | Disease result | GWAS Catalog trait search (alfred-GWAS) |
| **Alt+Enter** | Gene result | GWAS Catalog gene search (alfred-GWAS) |
| **Cmd+Alt+Enter** | Gene result | Gene Browser (lookup-gene) |

These require the corresponding Alfred workflows to be installed with External Triggers configured.

## Rebuilding the Database

When you add or edit notes in your vault, rebuild to pick up changes:

```bash
cd /path/to/QAK
make all          # rebuild DB + summary notes + binary
```

Or step by step:

```bash
make db           # parse vault YAML → qak.db
make summaries    # regenerate QAK — summary notes in vault
make build        # recompile Go binary (universal: arm64 + x86_64)
```

## QAK Summary Notes

QAK generates auto-updated summary notes in your vault, prefixed with `QAK —`. These are overwritten on each rebuild — do not edit them manually.

| Note | Content |
|------|---------|
| QAK — Disease Overview | All diseases with epi stats, gene/paper/trial counts |
| QAK — Gene Overview | All genes with disease/paper counts |
| QAK — Trials by Phase | All trials grouped by phase |
| QAK — Trials by Target | Trials grouped by target gene |
| QAK — Failed Trials | Trials with negative outcome |
| QAK — Papers for *Disease* | Papers linked to a specific disease |
| QAK — Trials for *Disease* | Trials for a specific disease |
| QAK — Strategies for *Disease* | Therapeutic strategies for a disease |

## Paper Summaries and Abstracts

Papers have two kinds of summaries:

- **Human** (`obs_source: human`) — hand-written observations from the original `#obs` block
- **AI** (`obs_source: ai`) — auto-generated ~250-character factual summaries

Both are searchable. In results, the subtitle shows `summary:human` or `summary:ai` so you know the source. Papers with human summaries also have an AI summary appended (`# OBSummary_AI`) for comparison.

GWAS papers with a known loci count have a `[Loci: N]` tag appended to the end of their AI summary for quick reference.

**Abstracts** are imported from the tsundo reference library during database builds. Press **Cmd+Enter** on a paper result to copy the abstract to clipboard. If no abstract is available, the full note body is copied instead.

**Distinctions** show why a paper is notable — e.g., "GWAS ref for ALS" or "key paper for APOE". These appear at the start of the subtitle so you can immediately see the paper's significance.

## Tsundo Integration

Paper titles and journals are enriched from the tsundo reference library (`library.db`) during database builds. The build script matches citekeys (case-insensitive) between QAK and tsundo, and:

- Fills in `title` and `journal` in the QAK database where the vault YAML is empty
- Adds a formatted citation line to paper notes that lack one (author, title, journal, year, PMID/DOI)

Papers whose vault citekey doesn't match tsundo are listed as mismatches during the build — rename the note file in Obsidian to fix them.

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `QAK_DB` | `~/Library/CloudStorage/.../QAK/qak.db` | Path to SQLite database |
| `QAK_VAULT` | `gitVault` | Obsidian vault name for URI links |

## Alfred Setup

### Main keyword (`qak`)

1. Create a new Workflow in Alfred
2. Add a **Script Filter** input:
   - Keyword: `qak`
   - Language: `/bin/bash`
   - Script: `'/path/to/QAK/qak' {query}`
   - "with input as {query}" (argument required)
3. Connect **two** output actions:
   - **Copy to Clipboard** (default Enter action) — pastes the note text
   - **Open URL** (Shift modifier) — receives `obsidian://` URIs

### Zettel keyword (`zk`)

1. Add another **Script Filter** input in the same workflow:
   - Keyword: `zk`
   - Language: `/bin/bash`
   - Script: `'/path/to/QAK/qak' --zk {query}`
2. Connect to the same **Copy to Clipboard** and **Open URL** actions

### How modifiers work in Alfred

The Script Filter returns different `arg` values depending on which modifier key is held:
- **No modifier (Enter)** → `arg` = note text (copied to clipboard)
- **Shift+Enter** → `mods.shift.arg` = `obsidian://` URI (opened as URL)
- **Cmd+Enter** → `mods.cmd.arg` = full note body (for papers)

Alfred routes each modifier to the connected action automatically.

Replace `/path/to/QAK/` with the actual path to the QAK repo on your machine.
