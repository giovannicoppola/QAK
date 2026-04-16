# Phase 9a: AI-Generated Paper Summaries — Report

- **Date:** 2026-04-16
- **Papers processed:** 439
- **Summaries applied:** 411
- **Skipped (empty/non-scientific):** 28
- **Errors:** 0
- **Commit:** 950c33b

## Summary

Generated `# OBSummary_AI` sections for 411 paper notes that lacked human-written `#obs` blocks. Each summary is a dense, factual ~250-character paragraph prioritizing specific findings (sample sizes, effect sizes, gene names, p-values) over generic descriptions. Set `obs_source: "ai"` in YAML frontmatter for each.

131 papers with existing human summaries (`obs_source: human`) were left untouched. 180 papers with no content remain with blank `obs_source`.

## Summary Length Distribution

| Range | Count |
|-------|------:|
| < 150 chars | 11 |
| 150–200 chars | 41 |
| 200–250 chars | 161 |
| 250–300 chars | 177 |
| > 300 chars | 21 |

- **Average:** 242 chars
- **Min:** 77 chars
- **Max:** 361 chars

## obs_source Breakdown (all 722 papers)

| obs_source | Count | Description |
|------------|------:|-------------|
| `"human"` | 131 | Hand-written `#obs` block present |
| `"ai"` | 411 | AI-generated summary applied this phase |
| (blank) | 180 | No content / too minimal for summary |

## Skipped Papers (28)

Non-scientific books, image-only references, or papers with insufficient content:

| Filename | Reason |
|----------|--------|
| @Akinc2019-su.md | Image-only reference |
| @American Caesar, Douglas MacArthur.md | Book |
| @Bach Music in the Castle of Heaven.md | Book |
| @Bach by Schweitzer Volume 2.md | Book |
| @Bloodlands.md | Book |
| @Born to Run.md | Book |
| @Brainstorm.md | Book |
| @Breath from Salt.md | Book |
| @Conroy2022-mh.md | Only SNP rsIDs, no findings |
| @Crime and Punishment.md | Book |
| @Davies2019-gu.md | Image-only, no extractable content |
| @Infinite Jest.md | Book |
| @Infinite Powers.md | Book |
| @Late Bloomers.md | Book |
| @Narasimhan2024-by.md | Image-only |
| @Rachel Maddow.md | Non-scientific |
| @Significant Figures.md | Book |
| @THe Biggest Ideas in the Universe.md | Book |
| @The Big Picture.md | Book |
| @The Brothers Karamazov.md | Book |
| @The Conquering Tide.md | Book |
| @The Gates of Europe.md | Book |
| @The Idiot.md | Book |
| @The Invention of Miracles.md | Book |
| @The Making of the Atomic Bomb.md | Book |
| @The Man from the Future.md | Book |
| @The Medici.md | Book |
| @Think Again.md | Book |
