# Phase 6: Zettel Notes — Migration Report

- **Date:** 2026-04-16 13:01
- **Notes processed:** 24
- **Notes modified:** 24
- **Notes skipped:** 0
- **Errors:** 0

## Summary

Added `type: zettel` YAML frontmatter to zettel notes. Extracted fact text from filename, 
inferred diseases and genes from fact content, assigned category by keyword matching. 
Body content left untouched — no headers added.

## Category Distribution

| Category | Count |
|----------|------:|
| epidemiology | 15 |
| genetics | 5 |
| mechanism | 2 |
| clinical | 1 |
| pharmacology | 1 |

## Changes by Note

| Note | Status | Changes | Warnings |
|------|--------|---------|----------|
| z 1-2% of all glaucoma patients are expected to carry MYOC mutations (3M cases in US, 30,000 MYOC).md | modified | +type: zettel; +fact (len=96); +category: epidemiology; +diseases: ['Glaucoma']; +genes: ['MYOC'] | — |
| z 600-1,800 cases of Juvenile Open-Angle Glaucoma in the US, 10-30% (60-540) MYOC.md | modified | +type: zettel; +fact (len=79); +category: epidemiology; +diseases: ['Glaucoma', 'Juvenile Open-Angle Glaucoma']; +genes: ['MYOC'] | — |
| z AMD prevalence is 1.5% after 40, 14% after 80, 6.6% overall worldwide.md | modified | +type: zettel; +fact (len=69); +category: epidemiology; +diseases: ['AMD'] | — |
| z Ankylosing Spondylitis prevalence 0.5-1% EUR, and 0.23% of Chinese.md | modified | +type: zettel; +fact (len=66); +category: epidemiology; +diseases: ['Ankylosing Spondylitis'] | — |
| z Ankylosing Spondylitis shows #epistasis between HLA-B27 and ERAP1 rs30187.md | modified | +type: zettel; +fact (len=73); +category: genetics; +diseases: ['Ankylosing Spondylitis']; +genes: ['HLA-B27', 'ERAP1'] | — |
| z FTD prevalence 50,000 to 60,000 people in the US and ~110,000 in the EU.md | modified | +type: zettel; +fact (len=71); +category: epidemiology; +diseases: ['Frontotemporal Dementia'] | — |
| z Gain of function is the most supported mechanism for MYOC glaucoma (aggregation due to incomplete proteolytic processing).md | modified | +type: zettel; +fact (len=121); +category: mechanism; +diseases: ['Glaucoma']; +genes: ['MYOC'] | — |
| z Glaucoma population prevalence ~2%.md | modified | +type: zettel; +fact (len=34); +category: epidemiology; +diseases: ['Glaucoma'] | — |
| z IOP levels in the UKB ~16±4 (so 3 SD range would be 4-28).md | modified | +type: zettel; +fact (len=57); +category: clinical | diseases empty |
| z In EUR, APOE2 allelic frequency is about 8%, corresponding to ~15% carriers (2pq=0.08.922), 0.6% homozygotes (0.08^2).md | modified | +type: zettel; +fact (len=117); +category: genetics; +genes: ['APOE', 'APOE2'] | diseases empty |
| z In EUR, APOE4 allelic frequency is about 14%, corresponding to ~24% carriers (2pq=0.14.862), 2% homozygotes (0.14^2).md | modified | +type: zettel; +fact (len=116); +category: genetics; +genes: ['APOE', 'APOE4'] | diseases empty |
| z MCI prevalence is ranging between 6.7% (60-64) and 25% (80-84). Estimated 65-74 9.2%.md | modified | +type: zettel; +fact (len=84); +category: epidemiology; +diseases: ['MCI'] | — |
| z Multiple System Atrophy prevalence estimated at 4-5-100,000, incidence 0.7-100,000 in Iceland.md | modified | +type: zettel; +fact (len=93); +category: epidemiology; +diseases: ['Multiple System Atrophy'] | — |
| z One in eight people in the United States (13 percent, or 30 million) aged 12 years or older has hearing loss in both ears, based on standard hearing examinations.md | modified | +type: zettel; +fact (len=161); +category: epidemiology; +diseases: ['Hearing loss'] | — |
| z The #prevalence of PD is approximately 1% of the individuals over age 60 years and 4% of the population older than age 85. ~4% are diagnosed before age 50. Men 1.5x more likely.md | modified | +type: zettel; +fact (len=176); +category: epidemiology; +diseases: ["Parkinson's Disease"] | — |
| z The estimated 2010 prevalence of Multiple Sclerosis in the US adult population cumulated over 10 years was 309.2 per 100,000 (95% confidence interval CI 308.1–310.1), representing 727,344 cases.md | modified | +type: zettel; +fact (len=193); +category: epidemiology; +diseases: ['Multiple Sclerosis'] | — |
| z age at UKB enrollment 57±8 (range 37-73) from 2006-2011.md | modified | +type: zettel; +fact (len=55); +category: epidemiology | diseases empty |
| z in addition to astrocytes, a subset of activated microglia express #^APOE (#@Mathys2019-ho and #@Zhou2020-rh).md | modified | +type: zettel; +fact (len=109); +category: mechanism; +genes: ['APOE'] | diseases empty |
| z only 0.01-0.1% of systemically administered antibodies reach the brain.md | modified | +type: zettel; +fact (len=70); +category: pharmacology | diseases empty |
| z population attributable fraction of APOE in Alzheimer's disease.md | modified | +type: zettel; +fact (len=63); +category: epidemiology; +diseases: ["Alzheimer's Disease"]; +genes: ['DjRyncAnV', 'sFZxl0Awc', 'APOE'] | — |
| z prevalence of Alzheimer's Disease AD 65-74 3%, 10% 65y, 14% 75, 37% 90.md | modified | +type: zettel; +fact (len=70); +category: epidemiology; +diseases: ["Alzheimer's Disease"] | — |
| z the incidence of Parkinson PD is 5-35-100,000 year, 21 in a study in Minnesota.md | modified | +type: zettel; +fact (len=78); +category: epidemiology; +diseases: ["Parkinson's Disease"] | — |
| z ~9% of GD patients present PD. GBA mutations are risk factors to develop PD (OR 3.7-5.4), accounting for 17-31% of PD cases in Ashkenazi and ~3% in non-Ashkenazi.md | modified | +type: zettel; +fact (len=161); +category: genetics; +diseases: ["Parkinson's Disease"]; +genes: ['GBA'] | — |
| z ~90% of AS patients Ankylosing Spondylitis are HLA-B27 carriers.md | modified | +type: zettel; +fact (len=63); +category: genetics; +diseases: ['Ankylosing Spondylitis']; +genes: ['HLA-B27'] | — |