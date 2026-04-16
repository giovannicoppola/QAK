# QAK Vault Reorganization Plan

## Overview

This document describes a reorganization plan for the **gitVault** Obsidian vault to enable automated extraction of a queryable SQLite knowledge database (QAK). The vault currently contains **6,339 markdown files**, of which the reorganization targets four primary note types:

| Note Type | Prefix/Pattern | Estimated Count | Current YAML Coverage |
|-----------|---------------|----------------:|----------------------|
| Diseases  | plain name    | ~30-40          | ~10 notes (partial)  |
| Genes     | `^`           | 269             | minimal              |
| Papers    | `@`           | 722             | minimal              |
| Zettels (key facts) | `z ` prefix | ~24     | created/updated only |
| Therapeutic Strategies | mixed | ~20-25   | none                 |
| Clinical Trials | trial name | ~45-50    | template exists (bullet-style) |
| Index Notes | `* Index` / `* – index` | ~11 | created/updated only |

**Total notes affected: ~1,120-1,140** (plus ~256 files touched by Roam link repair)

The remaining ~5,250 notes (daily notes, books, general knowledge, etc.) are out of scope for this phase.

---

## 1. Design Principles

1. **YAML frontmatter is the primary structured data source** for the SQLite builder script. Every queryable field must exist as a YAML property.
2. **Markdown headers organize human-readable content** within the note body. The builder script can also parse headers to extract specific sections (e.g., epidemiology blocks, loci lists).
3. **No text is deleted** — reorganization moves and reformats content, but never removes it. Even if content appears redundant after migration (e.g., stats in both YAML and body text), the original text is preserved in place. Cleanup of redundancies is left to manual review.
4. **Bidirectional linking** between diseases, genes, papers, clinical trials, and therapeutic strategies is enforced at the YAML level (not just inline wiki-links), so the database can build relationship tables.
5. **Incremental adoption** — each note type can be migrated independently. The ALS note serves as the reference implementation for diseases.
6. **Structured lists over tables** — information that would naturally fit a table (gene lists, variant catalogs, trial comparisons) is presented as **nested bullet lists** instead of markdown tables, for better rendering consistency across Obsidian themes and easier keyboard navigation in the editor (see section 1.2).

### 1.1 Handling Roam Block References

The vault contains two types of Roam-era block references (~520 occurrences across ~290 files):

**Type A — Block anchors** (trailing `^blockID` at end of a line, ~230 occurrences):
```
* AbbVie stopped the Phase 2 study in PSP after futility analysis ^XyThuxBdK
```
These mark a line so it can be deep-linked from elsewhere. **Action: leave in place.** They are valid Obsidian block IDs and do not interfere with rendering. The builder script should ignore them (strip `^[A-Za-z0-9_-]+` suffixes when parsing text).

**Type B — Block reference links** (`[[note#^blockID|display text]]`, ~290 occurrences):
```
[[@Serrano-Pozo2021-ft#^nFi2aqJQZ|APOE4 promotes the seeding of Aβ...]]
```
These deep-link into a specific block in another note, with quoted text as the display alias. **Action: leave in place.** They function as valid Obsidian links (the target block anchor must exist in the referenced note). The builder script should:
- Recognize these as links to the referenced note (strip the `#^blockID` to get the note name).
- Not attempt to resolve the block ID itself — treat it as an opaque anchor.

**In both cases, no text is deleted.** If a block anchor's target note no longer has the referenced block (e.g., after content was reorganized), the link will still render in Obsidian as plain text — this is acceptable and can be cleaned up manually.

### 1.2 Lists vs. Tables

Markdown tables have drawbacks in Obsidian: inconsistent rendering across themes, poor keyboard navigation in the editor, and difficulty editing wide cells. For structured data within notes, use **nested bullet lists** instead:

**Instead of:**
```markdown
| Gene | Role | Key Paper |
|------|------|-----------|
| SOD1 | 2% of all ALS; ~20% of familial | @Al-Chalabi2012-lo |
| C9orf72 | Most common genetic cause | @DeJesus-Hernandez2011-xx |
```

**Use:**
```markdown
- [[^SOD1]] — 2% of all ALS; ~20% of familial
  - Key paper: [[@Al-Chalabi2012-lo]]
- [[^C9orf72]] — most common genetic cause
  - Key paper: [[@DeJesus-Hernandez2011-xx]]
```

**Instead of:**
```markdown
| Variant | Effect | Disease | Paper |
|---------|--------|---------|-------|
| R47H | risk (OR 2.9) | AD | @Guerreiro2013-xx |
```

**Use:**
```markdown
- R47H — risk (OR 2.9), AD
  - [[@Guerreiro2013-xx]]
- R62H — risk, AD
  - [[@Jonsson2013-yy]]
```

This applies to all hand-curated note types — gene lists in disease notes, variant catalogs in gene notes, and approach lists in therapeutic strategy notes. The builder script parses bullet structure rather than table syntax.

Tables are instead generated as **auto-built summary notes** (see section 1.3).

### 1.3 Auto-Built Summary Notes

The builder script generates a separate set of **read-only summary notes** that present data as markdown tables. These are distinct from hand-curated notes: they are overwritten on every build, never hand-edited, and exist purely for quick reference and as starting points for slides (manual or agentic).

**Naming convention:** `QAK — <topic>.md`

The `QAK —` prefix makes them easy to find in Obsidian search and signals that they are auto-generated. They live in the same vault folder as the curated notes so that wiki-links between summary and curated notes work naturally.

**YAML frontmatter:**
```yaml
---
type: qak_summary
last_updated: "2026-04-16T10:30:00"
source_query: "clinical_trials WHERE disease = 'ALS'"
generated_by: "QAK builder v1.0"
tags:
  - qak-summary
  - auto-generated
---
```

- `last_updated` — timestamp of when this note was last regenerated, so you know how fresh the data is.
- `source_query` — describes what DB query produced this summary (useful for debugging or regenerating).
- `generated_by` — script version, for traceability.

**Proposed summary notes:**

| Summary note | Content | Source tables |
|---|---|---|
| `QAK — Disease Overview.md` | All diseases with epi stats, gene count, GWAS size, trial count | diseases + joins |
| `QAK — Trials for <Disease>.md` (one per disease) | All trials for a disease: phase, drug, status, outcome, endpoints, N | clinical_trials + disease_trial |
| `QAK — Gene Overview.md` | All genes with disease count, paper count, therapeutic status | genes + joins |
| `QAK — Trials by Phase.md` | All trials grouped by phase, with disease, drug, outcome | clinical_trials |
| `QAK — Trials by Target.md` | All trials grouped by target gene | clinical_trials + trial_gene |
| `QAK — Strategies for <Disease>.md` (one per disease) | Therapeutic strategies with linked trials and their outcomes | therapeutic_strategies + strategy_trial |
| `QAK — Papers for <Disease>.md` (one per disease) | Key papers for a disease: study type, sample size, loci | papers + disease_paper |
| `QAK — Failed Trials.md` | Trials with outcome = negative, grouped by disease | clinical_trials |

**Example — `QAK — Trials for ALS.md`:**
```markdown
---
type: qak_summary
last_updated: "2026-04-16T10:30:00"
source_query: "clinical_trials WHERE disease = 'ALS'"
generated_by: "QAK builder v1.0"
tags:
  - qak-summary
  - auto-generated
---

# Clinical Trials for ALS
> Auto-generated by QAK builder. Last updated: 2026-04-16. Do not edit manually.

## Active Trials

| Trial | Drug | Target | Phase | N | Primary Endpoint | Status |
|-------|------|--------|-------|---|------------------|--------|
| [[ATLAS trial]] | tofersen | [[^SOD1]] | Phase 3 | 150 | ALSFRS-R | Recruiting |
| ... | ... | ... | ... | ... | ... | ... |

## Completed Trials

| Trial | Drug | Target | Phase | N | Outcome | Results |
|-------|------|--------|-------|---|---------|---------|
| [[VALOR trial]] | tofersen | [[^SOD1]] | Phase 3 | 183 | Mixed | [[@Miller2022-xx]] |
| ... | ... | ... | ... | ... | ... | ... |

## Summary
- Total trials: 8
- Active: 3 | Completed: 4 | Discontinued: 1
- Targets: SOD1 (3), C9orf72 (2), FUS (1), ATXN2 (1), broad (1)
```

**Example — `QAK — Disease Overview.md`:**
```markdown
---
type: qak_summary
last_updated: "2026-04-16T10:30:00"
source_query: "diseases overview"
generated_by: "QAK builder v1.0"
tags:
  - qak-summary
  - auto-generated
---

# Disease Overview
> Auto-generated by QAK builder. Last updated: 2026-04-16. Do not edit manually.

| Disease | US Patients | Prevalence /100k | Genes | GWAS Loci | Active Trials |
|---------|------------|------------------|-------|-----------|---------------|
| [[Alzheimer's Disease]] | 6,700,000 | 1,100 | 42 | 75 | 12 |
| [[ALS]] | 30,000 | 4.5 | 15 | 15 | 8 |
| [[AMD]] | 11,000,000 | 3,400 | 8 | 34 | 6 |
| ... | ... | ... | ... | ... | ... |
```

**Build behavior:**
- Summary notes are regenerated from the SQLite DB on every builder run.
- Existing `QAK —` notes are **overwritten entirely** — they are never merged.
- If a summary note is manually edited, changes will be lost on next build (the `Do not edit manually` banner makes this clear).
- The builder emits a log of which summary notes were created/updated.

---

## 2. Disease Notes (~30-40 notes)

### 2.1 YAML Frontmatter Template

```yaml
---
type: disease
created: 2020-06-23 10:45:15
updated: 2024-07-25 15:23:54
aliases:
  - MND
  - Lou Gehrig's disease
tags:
  - disease
  - neurodegenerative        # disease category
  - motor-neuron              # sub-category (optional)

# Epidemiology
prevalence_per_100k: 4.5
incidence_per_100k: 2.0
n_patients_us: 30000
lifetime_risk: "1:350"

# Ontology IDs
omim: "105400"
mondo: "MONDO:0004976"
orphanet: "803"

# Genetics summary
gwas_largest_n: 27000
gwas_loci: 15
gwas_paper: "Van_Rheenen2021-eh"    # citekey of the largest GWAS
wes_largest_n: 3800
wes_loci: 2
wes_paper: "Farhan2019-vu"          # citekey of the largest WES/WGS study

# Heritability
heritability_twin: "38-78%"
heritability_gwas: "18%"

# Related entities (for DB joins)
genes:
  - SOD1
  - C9orf72
  - TARDBP
  - NEK1
  - DNAJC7

# Active QAK projects
projects: []
---
```

**Key decisions:**
- `genes` lists gene symbols (not `^`-prefixed note names) for cleaner DB queries. The script maps them to `^GENE` note files.
- `gwas_paper` / `wes_paper` store citekeys (not `@`-prefixed), matching the `citekey` property on paper notes.
- Ontology IDs are quoted strings to avoid YAML number-parsing issues.
- `projects` is an array of project note names for DB linking.

### 2.2 Note Body Sections

After the frontmatter, disease notes follow this header structure:

```markdown
# Quick Reference
<!-- One-line stats block for at-a-glance lookup -->
- US patients: 30,000
- Prevalence: ~5/100,000
- Lifetime risk: 1:350
- Largest GWAS: 27k, 15 loci (@Van_Rheenen2021-eh)
- Largest WES: 3.8k, 2 loci (@Farhan2019-vu)

# Epidemiology
<!-- Detailed prevalence, incidence, demographic breakdowns -->

# Genetics
## Known Genes
<!-- Associated genes with brief role -->
- [[^SOD1]] — 2% of all ALS; ~20% of familial
  - Key paper: [[@Al-Chalabi2012-lo]]
- [[^C9orf72]] — most common genetic cause
  - Key paper: ...

## GWAS
<!-- GWAS history, loci details -->

## Rare Variant Studies
<!-- WES/WGS findings -->

# Pathogenesis
<!-- Disease mechanisms, pathways -->

# Biomarkers

# Therapeutic Strategies
<!-- Overview of therapeutic approaches -->

# Clinical Trials
<!-- Active and notable past trials -->

# Mouse Models

# Notes
<!-- Unstructured notes, historical observations, imported Roam content -->
```

**Migration rules:**
- Existing bullet-point stats at the top of notes are **copied** (not moved) into `# Quick Reference`. The original text stays where it is.
- Scattered `#epidemiology` tagged content is placed under `# Epidemiology`. Original inline tags are preserved.
- Roam-style sub-page links (`[[Roam/.../ALS/biomarkers|ALS/biomarkers]]`) are kept as-is (they still render in Obsidian). New section headers are added alongside them, not as replacements.
- Roam block references (`^blockID` anchors and `#^blockID` links) are left untouched (see section 1.1).
- Content that doesn't fit a defined header goes under `# Notes`.
- **No text is deleted**, even if it becomes redundant with YAML properties or new headers.

---

## 3. Gene Notes (~269 notes)

### 3.1 YAML Frontmatter Template

```yaml
---
type: gene
created: 2020-06-23 10:45:15
updated: 2024-07-25 15:23:54
symbol: TREM2
full_name: "Triggering Receptor Expressed on Myeloid Cells 2"
aliases:
  - TREM-2
tags:
  - gene

# Genomic location
chromosome: "6"
cytoband: "6p21.1"

# Protein
protein_length: 230           # amino acids (if known)

# Key associations
diseases:
  - Alzheimer's Disease
  - Nasu-Hakola disease

# Therapeutic relevance
targeted_by: []               # list of drug/therapy names if any
therapeutic_notes: ""         # brief status, e.g., "Phase 2 — Denali DNL919"

# Key papers (citekeys)
key_papers:
  - Guerreiro2013-xx
  - Jonsson2013-yy
---
```

**Key decisions:**
- `symbol` is the canonical HGNC gene symbol (e.g., `TREM2`, not `^TREM2`).
- `diseases` lists disease note names for bidirectional linking.
- `targeted_by` enables the DB to answer "what drugs target this gene?"
- `key_papers` lists the most important citekeys — the full paper list is inferred from inline `[[@...]]` links by the builder script.

### 3.2 Note Body Sections

```markdown
# Function
<!-- Protein function, pathways, cell-type expression -->

# Expression
<!-- Tissue and cell-type expression patterns -->

# Mutations & Variants
<!-- Known pathogenic/risk variants with effects -->
- R47H — risk (OR 2.9), AD
  - [[@Guerreiro2013-xx]]
- R62H — risk, AD
  - [[@Jonsson2013-yy]]

# Disease Associations
<!-- Per-disease subsections if needed -->

# Therapeutic Strategies
<!-- Drug programs targeting this gene -->

# Mouse Models
<!-- KO, KI, transgenic phenotypes -->

# Notes
<!-- Unstructured content, imported Roam material -->
```

**Migration rules:**
- Existing `#expression` tagged content is placed under `# Expression`. Original inline tags are preserved.
- `#mutations` content is placed under `# Mutations & Variants`.
- `#mouseModels` content is placed under `# Mouse Models`.
- `#therapeutic strategies` content is placed under `# Therapeutic Strategies`.
- Sub-page links (e.g., `[[^TREM2/function]]`) are kept as-is; new headers are added alongside them.
- Roam block references (`^blockID` anchors and `#^blockID` links) are left untouched.
- **No text is deleted**, even if redundant with new YAML properties.

---

## 4. Paper Notes (~722 notes)

### 4.1 YAML Frontmatter Template

```yaml
---
type: paper
created: 2020-06-23 10:45:15
updated: 2024-07-25 15:23:54
citekey: Holstege2020-ky
title: "Exome sequencing identifies rare damaging variants in ATP8B4 and ABCA1 as risk factors for Alzheimer's disease"
tags:
  - paper

# Study metadata
study_type: exome             # gwas, exome, wgs, review, meta-analysis, clinical-trial, functional, other
diseases:
  - Alzheimer's Disease
genes:
  - ATP8B4
  - ABCA1

# Sample sizes (for genetic studies)
n_cases: 0
n_controls: 0
n_total: 0
n_loci: 0

# Author/journal (optional, for display)
first_author: Holstege
year: 2020
journal: "Nature Genetics"
---
```

**Key decisions:**
- `citekey` matches the filename without `@` — this is the join key used by disease and gene notes.
- `study_type` is a controlled vocabulary for filtering (gwas, exome, wgs, review, meta-analysis, clinical-trial, functional, other).
- `diseases` and `genes` enable the DB to link papers to diseases and genes bidirectionally.
- `n_cases`/`n_controls`/`n_loci` enable queries like "largest GWAS for ALS".

### 4.2 Note Body Sections

```markdown
# Citation
<!-- Full bibliographic citation -->

# Abstract
<!-- Abstract text, migrated from #Abstract or #abstract tagged blocks -->

# Key Findings
<!-- Main results, stats, figures -->

## Loci
<!-- If specific loci/genes are discussed, list them here -->
- [[^ATP8B4]] — p.Val1712Leu (OR 1.95)
- [[^ABCA1]] — multiple rare variants

# Methods
<!-- Study design notes if relevant -->

# Highlights
<!-- Migrated from #myHighlights -->

# Comments
<!-- Migrated from #myComments -->

# OBSummary
<!-- Migrated from #obs tagged blocks — always placed at end of document -->

# OBSummary_AI
<!-- AI-generated one-block summary (~255 chars). Only present if no #obs block exists. -->
```

### 4.3 Specific Migration Rules (from roadmap)

1. **`#obs` blocks**: Any block with the `#obs` tag is **copied** under a `# OBSummary` header, placed at the **end** of the document so it does not interfere with other headers. The original `#obs` tagged text remains in its original location.
2. **`#abstract` / `#Abstract` blocks**: Placed under `# Abstract` header. If there is content after the abstract that would be displaced, that content goes under a generic header using the citekey (e.g., `# Holstege2020-ky`). Original text is preserved.
3. **Loci inference**: If specific gene loci are discussed in the paper, they are listed under `## Loci` with wiki-links to gene notes.
4. **`citekey` property**: Added to YAML, value is the filename without `@` prefix (e.g., `Holstege2020-ky`).
5. **`#myHighlights`** content is placed under `# Highlights`. Original tags preserved.
6. **`#myComments`** content is placed under `# Comments`. Original tags preserved.
7. **Roam block references** (`^blockID` anchors and `#^blockID` links) are left untouched.
8. **No text is deleted** — content may appear in both its original location and under a new header until manually cleaned up.

### 4.4 AI-Generated Summaries (`# OBSummary_AI`)

For paper notes that **do not** have a `#obs` block (i.e., no human-written one-block summary), the migration script generates an AI summary and places it under a `# OBSummary_AI` header at the end of the document (after `# OBSummary` position, or in its place if no `# OBSummary` exists).

**Rules:**
- **Only generated when `#obs` is absent.** If the note already has a `#obs` block (and therefore a `# OBSummary`), no AI summary is added.
- **Distinct header** — `# OBSummary_AI` (not `# OBSummary`) so it is immediately clear the summary was not written by the user.
- **Length target: ~255 characters** — a single dense block, roughly 2-3 lines. Think of it as the text you'd put on a slide or read in an Alfred result.
- **Content:** Synthesized from whatever is available in the note — title, abstract, citation, key findings, highlights, inline content. Focus on: what was studied, main finding, sample size/method if notable.
- **YAML flag:** Add `obs_source: "ai"` to the paper's YAML frontmatter when the summary is AI-generated (vs. `obs_source: "human"` when a `#obs` block exists). This lets the builder script and queries distinguish the two.

**Example:**
```markdown
# OBSummary_AI
Exome sequencing of ~13k AD cases and ~15k controls identified rare damaging variants in ATP8B4 (OR 1.95) and ABCA1 as new AD risk genes, implicating lipid metabolism and microglial pathways.
```

**For the SQLite DB:** The `papers` table gets an `obs_summary` column (text) and an `obs_source` column (`"human"` or `"ai"`), so Alfred queries can display the summary regardless of origin and flag AI-generated ones if desired.

**Scope:** ~131 of 722 paper notes currently have a `#obs` block. The remaining ~591 would get an AI-generated summary.

**Generation approach:**
- During migration, an LLM call (or batch API) is made for each paper note lacking `#obs`.
- The prompt includes: title, abstract (if present), key findings, highlights, and any inline content from the note.
- Output is constrained to ~255 characters.
- Generated summaries are written to the note file and are **not deleted** on subsequent runs — they become part of the note. If the user later writes a `#obs` block, the `# OBSummary_AI` section remains (no text deletion) but `obs_source` in YAML is updated to `"human"` and the `# OBSummary` section takes precedence in the DB.

---

## 5. Zettel Notes — Key Facts (~24 notes)

Zettelkasten-style notes originating from Roam where they were prefixed `z:`. After migration to Obsidian the colon was dropped, so they now start with `z ` (lowercase z followed by a space). The filename *is* the fact — most have empty bodies or just supporting references. These are quick-recall atomic facts (prevalence figures, allele frequencies, mechanistic one-liners, etc.).

**Current state:** 24 notes matching `z *.md`. Examples:
- `z AMD prevalence is 1.5% after 40, 14% after 80, 6.6% overall worldwide.md`
- `z In EUR, APOE4 allelic frequency is about 14%, corresponding to ~24% carriers...md`
- `z only 0.01-0.1% of systemically administered antibodies reach the brain.md`

### 5.1 YAML Frontmatter Template

```yaml
---
type: zettel
created: 2020-08-07 06:52:36
updated: 2020-08-07 06:52:36
tags:
  - zettel

# The fact itself (duplicated from filename for DB querying)
fact: "AMD prevalence is 1.5% after 40, 14% after 80, 6.6% overall worldwide"

# What this fact is about (for joins and Alfred filtering)
diseases:
  - AMD
genes: []
papers: []                     # citekeys of supporting papers, if referenced in body

# Category for Alfred grouping
category: "epidemiology"       # epidemiology, genetics, mechanism, pharmacology, clinical, other
---
```

**Key decisions:**
- `fact` duplicates the filename (minus `z ` prefix and `.md` suffix) as a YAML string, because filenames are awkward to query in SQLite. This is the primary search field for Alfred.
- `diseases` / `genes` / `papers` are inferred from the filename content and any inline links in the body (e.g., `#^APOE` → gene APOE, `#@Mathys2019-ho` → paper).
- `category` is a lightweight classifier. The builder script can auto-assign based on keywords: "prevalence", "incidence", "patients" → `epidemiology`; "frequency", "allele", "carriers" → `genetics`; "mechanism", "gain of function", "pathway" → `mechanism`; etc. Manual override is always possible.

### 5.2 Note Body

Zettel notes are intentionally minimal. **No headers are added** — the body stays as-is (empty, or supporting references/quotes). The fact lives in the filename and in the `fact` YAML property.

If the body contains references (wiki-links to papers, block reference links), they are preserved untouched and the builder script extracts paper/gene citekeys from them to populate the YAML arrays.

### 5.3 Naming Convention

Keep the `z ` prefix — it is the identifier for this note type, just as `@` is for papers and `^` for genes.

If any zettel notes were converted with a different pattern (e.g., `z-` or `z_` instead of `z `), normalize them to `z ` during migration.

### 5.4 Alfred Integration

Zettels get a **dedicated Alfred keyword** (e.g., `zk` or `zfact`) that searches only the `zettels` table. This is separate from the main QAK query because the use case is different: you want to recall a specific fact fast, not browse a disease or gene profile.

**Alfred behavior:**
- Typing `zk AMD` matches all zettels where `fact` or `diseases` contain "AMD".
- Typing `zk prevalence` matches all zettels where `fact` or `category` = epidemiology.
- The result list shows the fact text directly (no need to open the note).
- Pressing Enter opens the note in Obsidian (for supporting references).
- Pressing Cmd+C copies the fact text to clipboard (for pasting into slides/emails).

---

## 6. Therapeutic Strategy Notes (~20-25 notes)

Therapeutic strategy notes describe a class of approach against a disease or target — e.g., "complement inhibition in AMD" or "antisense oligonucleotides in ALS". They sit above individual clinical trials and link downward to them.

### 5.1 YAML Frontmatter Template

```yaml
---
type: therapeutic_strategy
created: 2020-06-23 10:45:15
updated: 2024-07-25 15:23:54
tags:
  - therapeutic-strategy

# What this strategy targets
diseases:
  - AMD
target_genes:
  - CFH
  - CFB
  - C3
modality: "antibody"           # controlled vocabulary (see below)

# Linked trials (note names, without .md)
clinical_trials:
  - TENAYA trial
  - LUCERNE trial
  - PULSAR trial
---
```

**Controlled vocabulary for `modality`:**
`small-molecule` | `antibody` | `gene-therapy` | `antisense` | `sirna` | `cell-therapy` | `vaccine` | `enzyme-replacement` | `other`

### 5.2 Note Body Sections

```markdown
# Rationale
<!-- Biological rationale and mechanism of action for this therapeutic class -->

# Approaches
<!-- List of specific drugs/programs within this strategy -->
- pozelimab + cemdisiran (Regeneron) — antibody + siRNA, Phase 2
  - [[PHOTON trial]]
- pegcetacoplan (Apellis) — peptide inhibitor, Approved
  - [[DERBY trial]]

# Clinical Evidence
<!-- Summary of efficacy signals across trials in this strategy -->

# Notes
```

**Key decisions:**
- `clinical_trials` in YAML provides the DB with strategy-to-trial linkage.
- `modality` is at the strategy level because a strategy typically uses one class of modality; individual trials inherit it but can override.
- `target_genes` captures the molecular target(s), enabling queries like "what strategies target C3?"

---

## 7. Clinical Trial Notes (~45-50 notes)

The vault already has ~45-50 dedicated trial notes (VALOR, LAURIET, TENAYA, PHOTON, etc.) with an established bullet-point template. These are promoted to a first-class note type with proper YAML frontmatter.

### 6.1 YAML Frontmatter Template

```yaml
---
type: clinical_trial
created: 2022-05-02 15:17:07
updated: 2024-06-11 12:56:00
trial_name: "LAURIET"
tags:
  - clinical-trial

# Registration
nct_id: "NCT03828747"
clinicaltrials_url: "https://www.clinicaltrials.gov/ct2/show/NCT03828747"

# Trial design
phase: "Phase 2"               # Phase 1, Phase 1b, Phase 2, Phase 3, Phase 4
status: "Completed"            # Recruiting, Active, Completed, Discontinued, Unknown
outcome: ""                    # positive, negative, mixed, pending (empty if ongoing)

# Intervention
drug: "semorinemab"            # drug/therapy note name
modality: "antibody"           # inherits vocabulary from therapeutic_strategy
dose: "IV Q4W"
company: "Genentech"

# Population
diseases:
  - Alzheimer's Disease
indication_detail: "probable AD, mild-to-moderate"  # finer-grained than disease name
n_enrolled: 272

# Endpoints
primary_endpoint: "ADAS-Cog11, ADCS-ADL"
secondary_endpoints: []

# Duration
duration: "48-60w"
estimated_completion: "2021-07-20"

# Molecular targets
target_genes:
  - MAPT                       # tau

# Linked strategy
therapeutic_strategy: ""       # note name of parent strategy, if any

# Results paper (citekey)
results_paper: ""
---
```

**Key decisions:**
- `drug` is the note name of the drug/compound, enabling the DB to join to drug notes if they exist.
- `diseases` is an array (a trial can study multiple indications) and uses the same disease names as disease notes for DB joins.
- `target_genes` captures the molecular target(s) of the intervention, not just the disease-associated genes. This enables queries like "trials targeting SOD1" or "trials targeting tau".
- `modality` is repeated here (not just inherited from strategy) because some trials test novel modalities within a broader strategy.
- `therapeutic_strategy` links upward to the parent strategy note, enabling the DB to group trials by approach.
- `outcome` uses a controlled vocabulary (`positive`, `negative`, `mixed`, `pending`) to enable filtering successful vs. failed trials.
- `results_paper` links to the publication of results via citekey.

### 6.2 Note Body Sections

```markdown
# Design
<!-- Study design: randomized, double-blind, placebo-controlled, etc. -->
<!-- Inclusion/exclusion criteria if notable -->

# Endpoints
## Primary
<!-- Primary endpoint definition and rationale -->

## Secondary
<!-- Secondary and exploratory endpoints -->

# Results
<!-- Key efficacy and safety results -->
<!-- Embedded figures/tables if available -->

# Biomarkers
<!-- Biomarker data collected or reported (e.g., NfL, amyloid PET, tau PET) -->

# Safety
<!-- Adverse events, tolerability -->

# Notes
<!-- Unstructured content, personal commentary -->
```

### 6.3 Migration Rules

The existing trial notes already use a bullet-point template:
```
* sampleSize: 272
* drug: [[semorinemab]]
* phase: [[phase II]]
* clinicalTrialsURL: https://...
```

Migration approach (existing bullet-point content is **preserved in the note body** even after values are extracted into YAML — no text is deleted):

1. **Parse existing bullet fields** into YAML properties using the mapping:
   | Existing bullet | YAML property |
   |----------------|---------------|
   | `sampleSize` | `n_enrolled` |
   | `drug` | `drug` (strip wiki-link brackets) |
   | `dose` | `dose` |
   | `trialDuration` | `duration` |
   | `primaryEndpoint` | `primary_endpoint` |
   | `secondaryEndpoints` | `secondary_endpoints` |
   | `EstimatedCompletionDate` | `estimated_completion` |
   | `status` | `status` |
   | `phase` | `phase` (strip wiki-link brackets, normalize to "Phase N") |
   | `clinicalTrialsURL` | `clinicaltrials_url` |
   | `indications` | `diseases` (map to canonical disease names) |

2. **Extract NCT ID** from the URL if present (pattern: `NCT\d{8,}`).
3. **Infer `target_genes`** from the drug's mechanism (e.g., tofersen → SOD1, semorinemab → MAPT).
4. **Infer `outcome`** from emoji suffixes in filenames if present (pass/fail/arrow emojis).
5. **Move remaining bullet content** into appropriate body sections.
6. **Preserve** any narrative content, images, and links below the bullet block.

### 6.4 Status Emoji Convention

The vault uses emoji suffixes on trial note names to indicate outcome:
- ` ❌` = failed/discontinued → `outcome: "negative"`
- ` ✅` = positive/approved → `outcome: "positive"`
- ` ➡️` = ongoing → `outcome: "pending"`
- no emoji → `outcome: ""` (unknown/not yet assessed)

The migration script should parse these and populate the `outcome` field, then optionally clean the emoji from the filename (keeping the info in YAML instead).

---

## 8. SQLite Database Schema (Target)

The builder script will produce a SQLite database with the following core tables:

```
diseases
  id, name, prevalence_per_100k, incidence_per_100k, n_patients_us,
  lifetime_risk, omim, mondo, orphanet, gwas_largest_n, gwas_loci,
  gwas_paper, wes_largest_n, wes_loci, wes_paper,
  heritability_twin, heritability_gwas

genes
  id, symbol, full_name, chromosome, cytoband, protein_length

papers
  id, citekey, title, study_type, n_cases, n_controls, n_total,
  n_loci, first_author, year, journal,
  obs_summary, obs_source          -- obs_source: "human" or "ai"

therapeutic_strategies
  id, name, modality

clinical_trials
  id, trial_name, nct_id, phase, status, outcome,
  drug, modality, dose, company,
  indication_detail, n_enrolled,
  primary_endpoint, duration, estimated_completion,
  results_paper, therapeutic_strategy_id

zettels
  id, fact, category

projects
  id, name, status

-- Relationship tables (many-to-many)

disease_gene
  disease_id, gene_id

disease_paper
  disease_id, paper_id

gene_paper
  gene_id, paper_id

disease_strategy          -- which diseases does a strategy address
  disease_id, strategy_id

strategy_gene             -- which genes does a strategy target
  strategy_id, gene_id

strategy_trial            -- which trials belong to a strategy
  strategy_id, trial_id

disease_trial             -- which diseases does a trial study
  disease_id, trial_id

trial_gene                -- which genes does a trial's intervention target
  trial_id, gene_id

disease_zettel            -- which diseases does a zettel reference
  disease_id, zettel_id

zettel_gene               -- which genes does a zettel reference
  zettel_id, gene_id

zettel_paper              -- which papers support a zettel
  zettel_id, paper_id

disease_project
  disease_id, project_id

-- Auto-generated summary tracking
qak_summaries
  id, note_name, source_query, last_updated, generated_by
```

### Example Alfred Queries This Schema Supports

| Query | What it returns |
|-------|----------------|
| "ALS" | Epidemiology, gene list, latest GWAS, active trials, projects |
| "TREM2" | Associated diseases, key papers, trials targeting this gene |
| "largest GWAS for Alzheimer's" | Papers sorted by `n_total` where disease = AD |
| "Phase 3 trials in AMD" | Clinical trials filtered by phase + disease |
| "antisense trials" | Trials where modality = antisense |
| "SOD1 trials" | Trials linked to SOD1 via `trial_gene` |
| "failed Alzheimer's trials" | Trials where disease = AD and outcome = negative |
| "complement strategies in AMD" | Strategies where disease = AMD and target_genes include complement genes |
| "tofersen" | Trial details, linked disease (ALS), target gene (SOD1), results paper |
| `zk prevalence` | All zettel facts containing "prevalence" — shown inline, copy-to-clipboard |
| `zk APOE` | Zettel facts about APOE allele frequencies, PAF, etc. |

---

## 9. Migration Strategy

### Pre-migration checkpoint

A checkpoint commit was created before any changes:

```
Commit: e35ad0d
Branch: main (gitVault repo)
Message: "Checkpoint before QAK reorg"
Date: 2026-04-16
```

**To revert the entire vault to pre-reorg state:**
```bash
git -C '/Users/giovanni.coppola/Library/CloudStorage/OneDrive-RegeneronPharmaceuticals,Inc/MyScripts/myGitHubRepos/gitVault' reset --hard e35ad0d
```

**To revert selectively** (e.g., undo only gene note changes):
```bash
git -C '/Users/giovanni.coppola/Library/CloudStorage/OneDrive-RegeneronPharmaceuticals,Inc/MyScripts/myGitHubRepos/gitVault' checkout e35ad0d -- 'gitVault-notes/^*.md'
```

It is recommended to create additional checkpoint commits between phases (e.g., after Phase 1 completes, before Phase 2 starts) so that partial rollback is possible without losing work from earlier phases.

### Phase 1: Disease Notes (smallest set, highest value)
1. Use ALS as the reference template (already partially converted).
2. Migrate the ~10 best-documented disease notes first (Alzheimer's, AMD, glaucoma, MS, PD, etc.).
3. Validate the builder script can extract YAML and produce correct SQLite rows.
4. Extend to remaining disease notes.

### Phase 2: Gene Notes
1. Apply YAML template to all 269 `^`-prefixed notes.
2. Populate `diseases` and `key_papers` arrays from existing inline links.
3. Reorganize body content under standard headers.

### Phase 3: Paper Notes
1. Apply YAML template to all 722 `@`-prefixed notes.
2. Execute the `#obs` → `# OBSummary` migration (move to end of doc).
3. Execute the `#abstract` → `# Abstract` migration.
4. Infer and populate `## Loci` sections.
5. Populate `diseases` and `genes` arrays from inline links and context.

### Phase 4: Clinical Trials (good automation candidate)
1. Parse existing bullet-point template fields into YAML properties (see field mapping in section 7.3).
2. Extract NCT IDs from URLs.
3. Infer `target_genes` from drug mechanism where possible.
4. Map `indications` to canonical disease names.
5. Parse emoji suffixes into `outcome` field.
6. Move remaining content into standard body sections.
7. Link trials to therapeutic strategy notes where a parent strategy exists.

### Phase 5: Therapeutic Strategies
1. Identify strategy notes (currently named like "AMD — Therapeutic Strategies", "complement inhibition in AMD", etc.).
2. Apply YAML template, populate `diseases`, `target_genes`, `modality`.
3. Populate `clinical_trials` array by linking to migrated trial notes from Phase 4.

### Phase 6: Zettels (quick win)
1. Identify all `z *.md` notes (currently 24). Check for variant prefixes (`z-`, `z_`, etc.) and normalize to `z `.
2. Add YAML frontmatter: extract `fact` from filename, infer `diseases`/`genes`/`papers` from filename content and body links.
3. Auto-assign `category` from keyword matching (epidemiology, genetics, mechanism, etc.).
4. Body content left untouched — no headers added.

### Phase 7: Roam Link Repair (run after note migration)
1. Run the repair script (section 11.3) across all ~256 affected files.
2. Category B (paper references) and Category A (sub-topic links) are repaired automatically.
3. Category C (daily notes) repaired where target exists, flagged otherwise.
4. Category D (Roam infrastructure) left as-is.
5. Each repaired file gets an audit comment at the end.
6. Manual review of any links the script couldn't resolve.

### Phase 8: Index Notes
1. Add YAML frontmatter (`type: index`) to the ~11 index notes.
2. Verify their links were repaired in Phase 7.
3. Leave body structure as-is — no headers imposed.

### Phase 9: Builder Script, Summary Notes & Alfred Integration
1. Write the Python script that parses vault → SQLite.
2. Generate `QAK —` summary notes from the database (see section 1.3).
3. Generate AI summaries (`# OBSummary_AI`) for the ~591 papers without `#obs` (see section 4.4).
4. Build Alfred workflow with two keywords:
   - Main QAK keyword — searches diseases, genes, papers, trials, strategies.
   - `zk` keyword — searches zettels only, shows fact text inline, Cmd+C to copy.
5. Set up periodic rebuild (cron or Obsidian plugin trigger).
6. Each rebuild regenerates both the SQLite DB and all summary notes, updating `last_updated` timestamps.

---

## 10. Naming Convention Cleanup

| Issue | Current State | Proposed Fix |
|-------|--------------|--------------|
| Disease name variants | "Alzheimer's Disease", "Alzheimers Disease" | Standardize to canonical name; add variants as `aliases` |
| Roam-style nested links | `[[Roam/giov-.../ALS/biomarkers\|ALS/biomarkers]]` | Replace with in-note `# Biomarkers` header or standalone note |
| Therapeutic strategy notes | Mixed naming patterns | Prefix with disease name: `ALS — Therapeutic Strategies.md` |
| Gene sub-pages | `^TREM2/function` | Consolidate into main `^TREM2.md` under `# Function` header |
| Clinical trial names | Mixed: some use trial name, some use drug name + "trial" | Standardize to `TRIALNAME trial.md` (e.g., `VALOR trial.md`); for trials without an acronym use `drug — phase N trial.md` |
| Trial emoji suffixes | `VALOR trial ❌.md`, `ATLAS trial ➡️.md` | Migrate outcome to YAML `outcome` field; remove emoji from filename |

---

## 11. Index Notes & Roam Link Repair

### 11.1 Index Notes (~11 notes)

The vault has hand-curated index/table-of-contents notes:

| Index note | Type | Links |
|---|---|---|
| `Alzheimer's  Index.md` | disease | AD genetics, biomarkers, therapeutic strategies |
| `Parkinson's Disease Index.md` | disease | clinical, biomarkers, genetics by gene |
| `Huntington's Disease – Index.md` | disease | (currently empty) |
| `APOE index.md` | gene | history, function, variants, mouse models, therapeutics |
| `APP index.md` | gene | mutations, function, therapeutics |
| `tau – index.md` | gene/protein | function, structure, biomarkers, imaging, therapeutics |
| `Hearing loss – index.md` | disease | epidemiology, GWAS, WES |
| `Multiple sclerosis - index.md` | disease | (not examined) |
| `diabetic retinopathy index.md` | disease | (not examined) |
| `Examples – index.md` | misc | (not examined) |
| `Cognitive Function Index (CFI).md` | instrument | (clinical scale, not a navigation index) |

These are navigation hubs — curated tables of contents linking to subtopics. Almost all their links are broken Roam sub-page links (`[[Roam/giov-2026-01-29-19-08-45/ALS/biomarkers|ALS/biomarkers]]`) that point to pages that don't exist as Obsidian files.

**Recommendation: keep them, repair links, and let the builder generate auto-summaries alongside them.**

Rationale:
- They represent curated organizational thinking — which subtopics matter and how they relate. This is harder to auto-generate than raw data tables.
- After link repair, they become useful navigation entry points in Obsidian's graph view.
- The auto-generated `QAK —` summary notes (section 1.3) serve a different purpose: tabular data for quick reference and slides. The index notes serve as narrative/hierarchical navigation.

**YAML frontmatter:**
```yaml
---
type: index
created: 2020-10-15 10:10:57
updated: 2024-04-18 06:41:02
tags:
  - index
subject: "Alzheimer's Disease"    # the disease/gene/topic this index covers
subject_type: "disease"            # disease, gene, protein, topic
---
```

**No body restructuring** — the index stays as-is after link repair. The user may choose to evolve these manually.

### 11.2 Roam Sub-Page Link Repair

The vault contains **226 unique broken Roam sub-page targets** across **~256 files**. These are links of the form:
```
[[Roam/giov-2026-01-29-19-08-45/ALS/biomarkers|ALS/biomarkers]]
```

They fall into four categories, each with a different repair strategy:

**Category A — Sub-topic links pointing to note sections (~120 targets)**
```
^APOE/function → [[^APOE#Function]]
ALS/biomarkers → [[ALS#Biomarkers]]
Alzheimer's Disease/GWAS → [[Alzheimer's Disease#GWAS]]
^GRN/Therapeutic Strategies → [[^GRN#Therapeutic Strategies]]
```
These map 1:1 to headers that will exist in the reorganized notes. The repair script rewrites them as **section links** (`[[Note#Header]]`), preserving the display alias.

Before: `[[Roam/giov-2026-01-29-19-08-45/^APOE/function|^APOE/function]]`
After: `[[^APOE#Function|^APOE/function]]`

**Category B — Paper references with block anchors (~65 targets)**
```
[[Roam/giov-2026-01-29-19-08-45/@Raulin2022-kh#^Si-wB4Bt4|display text]]
```
These point to specific blocks in paper notes. The paper note itself exists (as `@Raulin2022-kh.md`), the Roam prefix is just extra. Repair: strip the `Roam/giov-2026-01-29-19-08-45/` prefix.

Before: `[[Roam/giov-2026-01-29-19-08-45/@Raulin2022-kh#^Si-wB4Bt4|text]]`
After: `[[@Raulin2022-kh#^Si-wB4Bt4|text]]`

**Category C — Daily note references (~6 targets)**
```
[[Roam/giov-2026-01-29-19-08-45/2020-06-17-Wed#^jsN0q7pAK|text]]
```
These point to daily notes. If the daily note exists in `dailyNotes/`, repair by stripping the prefix and adjusting the path. If not, leave the link as-is (it will render as unresolved, flagging it for manual review).

**Category D — Miscellaneous/non-mappable (~35 targets)**
```
roam/comments, roam/css, roam/js, yaanki/logic, etc.
```
These are Roam-specific infrastructure references with no Obsidian equivalent. Leave as-is — they are inert but serve as historical context. No text deleted.

### 11.3 Repair Script Logic

```
For each file containing [[Roam/giov-2026-01-29-19-08-45/...]]:
  For each such link:
    1. Extract the target path (everything after the Roam prefix)
    2. If target starts with @ → Category B: strip Roam prefix, keep block anchor and alias
    3. If target matches YYYY-MM-DD → Category C: strip prefix, check if daily note exists
    4. If target contains / (sub-page pattern):
       a. Split into parent/subtopic
       b. Check if parent note exists (e.g., ^APOE.md, ALS.md)
       c. If yes → Category A: rewrite as [[parent#subtopic|original alias]]
       d. If no → leave as-is (manual review)
    5. Otherwise → Category D: leave as-is
```

**Important:** The original Roam link text is preserved as the display alias so the rendered note looks identical. Only the link target changes. A comment is added at the end of the file listing which links were repaired, for auditability:

```markdown
<!-- QAK link repair: 5 Roam links repaired on 2026-04-16 -->
```

---

## 12. Validation Checklist (per note)

Before marking a note as migrated:

**All note types:**
- [ ] YAML frontmatter present with `type` field
- [ ] All required properties populated (see templates above)
- [ ] `diseases`/`genes`/`key_papers` arrays reflect actual note content
- [ ] Body organized under standard headers (using nested bullet lists, not tables)
- [ ] All original text preserved — no deletions, even if redundant with YAML
- [ ] Roam block anchors (`^blockID`) and block reference links (`#^blockID`) untouched
- [ ] Existing wiki-links preserved and functional

**Papers only:**
- [ ] `#obs` content at end of document under `# OBSummary`
- [ ] `#abstract` content under `# Abstract`
- [ ] `citekey` property matches filename (minus `@`)

**Clinical trials only:**
- [ ] `nct_id` extracted from URL (if URL present)
- [ ] `phase` normalized to "Phase N" format (not wiki-linked)
- [ ] `diseases` mapped to canonical disease note names
- [ ] `drug` is plain text (wiki-link brackets stripped)
- [ ] `outcome` populated from emoji suffix (if present) or content
- [ ] `target_genes` populated where mechanism is known
- [ ] Bullet-point template fields fully migrated to YAML (no duplicated data)

**Zettels only:**
- [ ] Filename starts with `z ` (normalized from `z:`, `z-`, `z_` variants)
- [ ] `fact` property matches filename content (minus `z ` prefix and `.md`)
- [ ] `category` assigned (epidemiology, genetics, mechanism, pharmacology, clinical, other)
- [ ] `diseases`/`genes`/`papers` populated from filename keywords and body links
- [ ] Body content untouched — no headers added

---

## 13. Estimated Effort

| Phase | Notes/Files | Complexity | Approach |
|-------|------:|------------|----------|
| 1. Diseases | ~35 | High (manual review per note) | Semi-automated with manual QA |
| 2. Genes | ~269 | Medium (template application + link parsing) | Script-assisted |
| 3. Papers | ~722 | Medium (pattern-based migration) | Largely automated |
| 4. Clinical Trials | ~45 | Low-Medium (existing template → YAML mapping) | Largely automated |
| 5. Therapeutic Strategies | ~20 | Medium (identification + template + trial linking) | Semi-automated |
| 6. Zettels | ~24 | Low (filename → YAML, no body changes) | Fully automated |
| 7. Roam Link Repair | ~256 files | Medium (pattern matching + section mapping) | Automated with manual review of ~35 unresolvable |
| 8. Index Notes | ~11 | Low (YAML only, no body changes) | Mostly automated |
| 9. Builder + Alfred | — | High (new code) | Manual development |

Phase 6 (zettels) and Phase 4 (clinical trials) are the best automation candidates. Phase 7 (link repair) should run **after** the note migration phases (1-6) so the target headers exist when sub-topic links are rewritten. Phases 2-3 are also good scripting targets. Phases 1 and 5 require the most manual attention due to varied note structures.

---

## 14. Migration Reports

Each migration phase produces a markdown report saved to the QAK repo at `reports/phase-N-<name>.md`. These are generated after the phase completes, not during — they document what actually happened, not what was planned.

### 14.1 Report Template

```markdown
# Phase N: <Phase Name> — Migration Report

- **Date:** 2026-04-17
- **Notes processed:** 269
- **Notes modified:** 245
- **Notes skipped:** 24 (reason breakdown below)
- **Errors:** 3

## Summary

<!-- 2-3 sentence overview of what this phase did -->

## Changes by Note

| Note | Changes Applied | Warnings |
|------|----------------|----------|
| ^APOE.md | +YAML (type, symbol, diseases, key_papers), +headers (Function, Expression, Mutations, ...) | `full_name` left empty — not inferrable |
| ^TREM2.md | +YAML (type, symbol, diseases, key_papers), +headers | — |
| ... | ... | ... |

## YAML Properties Populated

| Property | Populated | Left Empty | Notes |
|----------|----------:|----------:|-------|
| type | 269/269 | 0 | — |
| symbol | 269/269 | 0 | extracted from filename |
| diseases | 198/269 | 71 | inferred from inline links |
| key_papers | 142/269 | 127 | only set when [[@...]] links found |
| ... | ... | ... | ... |

## Skipped Notes

| Note | Reason |
|------|--------|
| ^TREM119.md | Already migrated (type: gene in YAML) |
| ... | ... |

## Errors

| Note | Error | Resolution |
|------|-------|------------|
| ^C9orf72.md | YAML parse failure — existing frontmatter malformed | Skipped, flagged for manual fix |
| ... | ... | ... |

## Items Requiring Manual Review

- [ ] ^APOE.md — `full_name` not set, multiple aliases found
- [ ] ^GBA.md — `diseases` list may be incomplete (only 1 disease linked but note mentions 3)
- [ ] ...
```

### 14.2 Phase-Specific Report Additions

Beyond the common template, some phases add extra sections:

**Phase 3 (Papers):**
- Count of `#obs` blocks found vs. `# OBSummary_AI` generated
- List of papers where `study_type` could not be inferred

**Phase 4 (Clinical Trials):**
- Bullet field → YAML mapping success rate per field
- List of trials where `target_genes` could not be inferred from drug name
- Emoji suffix parsing results

**Phase 7 (Roam Link Repair):**
- Breakdown by category (A/B/C/D) with counts
- List of unresolvable links (Category D + failed Category A/C) for manual review
- Per-file count of links repaired

**Phase 9 (Builder):**
- SQLite table row counts
- Summary note generation list
- AI summary generation stats (count, avg length, any failures)

### 14.3 Report Index

A top-level `reports/README.md` is maintained with links to all phase reports and a running summary:

```markdown
# QAK Migration Reports

| Phase | Date | Notes | Modified | Errors | Manual Review |
|-------|------|------:|----------:|-------:|---:|
| 1. Diseases | 2026-04-17 | 35 | 33 | 0 | 4 |
| 2. Genes | 2026-04-18 | 269 | 245 | 3 | 12 |
| ... | ... | ... | ... | ... | ... |
```
