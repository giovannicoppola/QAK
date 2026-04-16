# Phase 2: Gene Notes — Migration Report

- **Date:** 2026-04-16 12:47
- **Notes processed:** 269
- **Notes modified:** 269
- **Notes skipped:** 0
- **Errors:** 0

## Summary

Added `type: gene` YAML frontmatter to gene notes. Extracted gene symbol from filename, 
disease associations from wiki-links, paper citekeys from `[[@...]]` references, 
protein length and chromosome location from body text, and drug/therapy targets from 
`targetedBy` lines. All original body text preserved.

## YAML Properties Populated

| Property | Populated | Left Empty | Notes |
|----------|----------:|----------:|-------|
| type | 269/269 | 0 | always set to 'gene' |
| symbol | 269/269 | 0 | extracted from filename |
| full_name | 0/269 | 269 | needs manual entry |
| diseases | 26/269 | 243 | from wiki-links |
| key_papers | 38/269 | 231 | from [[@...]] links |
| chromosome | 9/269 | 260 | from body text |
| protein_length | 14/269 | 255 | from body text |
| targeted_by | 5/269 | 264 | from targetedBy lines |

## Changes by Note

| Note | Status | Changes | Warnings |
|------|--------|---------|----------|
| ^AAK1.md | modified | +type: gene; +tags: gene; +symbol: AAK1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^ABCA1.md | modified | +type: gene; +tags: gene; +symbol: ABCA1; +key_papers: 1 citekeys | diseases list empty — no disease links found; full_name left empty — needs manual entry |
| ^ABCA7.md | modified | +type: gene; +tags: gene; +symbol: ABCA7; +chromosome: 19 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^ADAM10.md | modified | +type: gene; +tags: gene; +symbol: ADAM10; +diseases: ["Alzheimer's Disease"]; +key_papers: 1 citekeys | full_name left empty — needs manual entry |
| ^ADH1B.md | modified | +type: gene; +tags: gene; +symbol: ADH1B | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^AIF1.md | modified | +type: gene; +tags: gene; +symbol: AIF1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^AKAP11.md | modified | +type: gene; +tags: gene; +symbol: AKAP11 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^AKT1.md | modified | +type: gene; +tags: gene; +symbol: AKT1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^ALDH2.md | modified | +type: gene; +tags: gene; +symbol: ALDH2; +chromosome: 4; +diseases: ['alcohol use disorder']; +key_papers: 5 citekeys | full_name left empty — needs manual entry |
| ^ANGPTL3.md | modified | +type: gene; +tags: gene; +symbol: ANGPTL3 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^ANGPTL7.md | modified | +type: gene; +tags: gene; +symbol: ANGPTL7; +protein_length: 346; +key_papers: 6 citekeys | diseases list empty — no disease links found; full_name left empty — needs manual entry |
| ^ANKRD11.md | modified | +type: gene; +tags: gene; +symbol: ANKRD11 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^ANKRD55.md | modified | +type: gene; +tags: gene; +symbol: ANKRD55 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^ANO4.md | modified | +type: gene; +tags: gene; +symbol: ANO4; +key_papers: 1 citekeys | diseases list empty — no disease links found; full_name left empty — needs manual entry |
| ^APOB.md | modified | +type: gene; +tags: gene; +symbol: APOB; +protein_length: 4563 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^APOC3.md | modified | +type: gene; +tags: gene; +symbol: APOC3 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^APOE.md | modified | +type: gene; +tags: gene; +symbol: APOE; +protein_length: 299; +diseases: ["Alzheimer's Disease"]; +key_papers: 4 citekeys | full_name left empty — needs manual entry |
| ^APOL1.md | modified | +type: gene; +tags: gene; +symbol: APOL1; +key_papers: 1 citekeys | diseases list empty — no disease links found; full_name left empty — needs manual entry |
| ^APP.md | modified | +type: gene; +tags: gene; +symbol: APP; +chromosome: 21; +protein_length: 770; +key_papers: 4 citekeys | diseases list empty — no disease links found; full_name left empty — needs manual entry |
| ^AQP4.md | modified | +type: gene; +tags: gene; +symbol: AQP4; +key_papers: 1 citekeys | diseases list empty — no disease links found; full_name left empty — needs manual entry |
| ^ASPA.md | modified | +type: gene; +tags: gene; +symbol: ASPA | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^ASXL.md | modified | +type: gene; +tags: gene; +symbol: ASXL | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^ATOH1.md | modified | +type: gene; +tags: gene; +symbol: ATOH1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^ATP7B.md | modified | +type: gene; +tags: gene; +symbol: ATP7B | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^ATP8B4.md | modified | +type: gene; +tags: gene; +symbol: ATP8B4 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^ATXN3.md | modified | +type: gene; +tags: gene; +symbol: ATXN3 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^AXL.md | modified | +type: gene; +tags: gene; +symbol: AXL | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^BDNF.md | modified | +type: gene; +tags: gene; +symbol: BDNF | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^BEST1.md | modified | +type: gene; +tags: gene; +symbol: BEST1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^BIN1.md | modified | +type: gene; +tags: gene; +symbol: BIN1; +diseases: ["Alzheimer's Disease"] | key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^BMPR2.md | modified | +type: gene; +tags: gene; +symbol: BMPR2 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^BRCA1.md | modified | +type: gene; +tags: gene; +symbol: BRCA1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^C1Q.md | modified | +type: gene; +tags: gene; +symbol: C1Q | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^C2.md | modified | +type: gene; +tags: gene; +symbol: C2 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^C3.md | modified | +type: gene; +tags: gene; +symbol: C3 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^C4A.md | modified | +type: gene; +tags: gene; +symbol: C4A | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^C4B.md | modified | +type: gene; +tags: gene; +symbol: C4B | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^C5.md | modified | +type: gene; +tags: gene; +symbol: C5 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^C9.md | modified | +type: gene; +tags: gene; +symbol: C9 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^C9orf72.md | modified | +type: gene; +tags: gene; +symbol: C9orf72; +key_papers: 1 citekeys | diseases list empty — no disease links found; full_name left empty — needs manual entry |
| ^CA2.md | modified | +type: gene; +tags: gene; +symbol: CA2 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^CALCA.md | modified | +type: gene; +tags: gene; +symbol: CALCA | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^CALCB.md | modified | +type: gene; +tags: gene; +symbol: CALCB | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^CBLB.md | modified | +type: gene; +tags: gene; +symbol: CBLB | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^CCL3.md | modified | +type: gene; +tags: gene; +symbol: CCL3 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^CCR5.md | modified | +type: gene; +tags: gene; +symbol: CCR5 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^CD2.md | modified | +type: gene; +tags: gene; +symbol: CD2 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^CD2AP.md | modified | +type: gene; +tags: gene; +symbol: CD2AP | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^CD33.md | modified | +type: gene; +tags: gene; +symbol: CD33; +chromosome: 19; +targeted_by: ['AL003†', 'Alector']; +key_papers: 4 citekeys | diseases list empty — no disease links found; full_name left empty — needs manual entry |
| ^CD40.md | modified | +type: gene; +tags: gene; +symbol: CD40; +diseases: ["Alzheimer's Disease"] | key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^CD52.md | modified | +type: gene; +tags: gene; +symbol: CD52 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^CD58.md | modified | +type: gene; +tags: gene; +symbol: CD58; +diseases: ['Multiple Sclerosis'] | key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^CD59.md | modified | +type: gene; +tags: gene; +symbol: CD59 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^CD68.md | modified | +type: gene; +tags: gene; +symbol: CD68 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^CD74.md | modified | +type: gene; +tags: gene; +symbol: CD74 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^CD83.md | modified | +type: gene; +tags: gene; +symbol: CD83 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^CFB.md | modified | +type: gene; +tags: gene; +symbol: CFB; +targeted_by: ['iptacopan'] | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^CFD.md | modified | +type: gene; +tags: gene; +symbol: CFD | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^CFH.md | modified | +type: gene; +tags: gene; +symbol: CFH; +key_papers: 6 citekeys | diseases list empty — no disease links found; full_name left empty — needs manual entry |
| ^CFHR5.md | modified | +type: gene; +tags: gene; +symbol: CFHR5 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^CFI.md | modified | +type: gene; +tags: gene; +symbol: CFI | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^CGRP.md | modified | +type: gene; +tags: gene; +symbol: CGRP; +key_papers: 1 citekeys | diseases list empty — no disease links found; full_name left empty — needs manual entry |
| ^CHD8.md | modified | +type: gene; +tags: gene; +symbol: CHD8 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^CHRNA3.md | modified | +type: gene; +tags: gene; +symbol: CHRNA3 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^CHRNA4.md | modified | +type: gene; +tags: gene; +symbol: CHRNA4 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^CHRNA5.md | modified | +type: gene; +tags: gene; +symbol: CHRNA5; +key_papers: 1 citekeys | diseases list empty — no disease links found; full_name left empty — needs manual entry |
| ^CHRNB2.md | modified | +type: gene; +tags: gene; +symbol: CHRNB2; +key_papers: 1 citekeys | diseases list empty — no disease links found; full_name left empty — needs manual entry |
| ^CHRNB3.md | modified | +type: gene; +tags: gene; +symbol: CHRNB3 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^CLEC7A.md | modified | +type: gene; +tags: gene; +symbol: CLEC7A | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^COL4A3.md | modified | +type: gene; +tags: gene; +symbol: COL4A3 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^COL4A4.md | modified | +type: gene; +tags: gene; +symbol: COL4A4 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^COL4A5.md | modified | +type: gene; +tags: gene; +symbol: COL4A5 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^CRB1.md | modified | +type: gene; +tags: gene; +symbol: CRB1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^CRX.md | modified | +type: gene; +tags: gene; +symbol: CRX | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^CSF1R.md | modified | +type: gene; +tags: gene; +symbol: CSF1R; +key_papers: 1 citekeys | diseases list empty — no disease links found; full_name left empty — needs manual entry |
| ^CST7.md | modified | +type: gene; +tags: gene; +symbol: CST7 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^CTSD.md | modified | +type: gene; +tags: gene; +symbol: CTSD | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^CX3CR1.md | modified | +type: gene; +tags: gene; +symbol: CX3CR1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^CYP1B1.md | modified | +type: gene; +tags: gene; +symbol: CYP1B1; +diseases: ['Glaucoma'] | key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^DAG1.md | modified | +type: gene; +tags: gene; +symbol: DAG1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^DNAJC7.md | modified | +type: gene; +tags: gene; +symbol: DNAJC7 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^EGFR.md | modified | +type: gene; +tags: gene; +symbol: EGFR; +key_papers: 1 citekeys | diseases list empty — no disease links found; full_name left empty — needs manual entry |
| ^EIF2B.md | modified | +type: gene; +tags: gene; +symbol: EIF2B | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^EPHA1.md | modified | +type: gene; +tags: gene; +symbol: EPHA1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^ESR1.md | modified | +type: gene; +tags: gene; +symbol: ESR1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^FAN1.md | modified | +type: gene; +tags: gene; +symbol: FAN1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^FBXO7.md | modified | +type: gene; +tags: gene; +symbol: FBXO7 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^FGF14.md | modified | +type: gene; +tags: gene; +symbol: FGF14 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^FLG.md | modified | +type: gene; +tags: gene; +symbol: FLG | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^FLNA.md | modified | +type: gene; +tags: gene; +symbol: FLNA; +diseases: ["Alzheimer's Disease"]; +key_papers: 1 citekeys | full_name left empty — needs manual entry |
| ^FOXI1.md | modified | +type: gene; +tags: gene; +symbol: FOXI1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^FOXO3.md | modified | +type: gene; +tags: gene; +symbol: FOXO3 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^FOXP3.md | modified | +type: gene; +tags: gene; +symbol: FOXP3 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^FUS.md | modified | +type: gene; +tags: gene; +symbol: FUS; +diseases: ['ALS'] | key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^Fcgr2.md | modified | +type: gene; +tags: gene; +symbol: Fcgr2 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^GALC.md | modified | +type: gene; +tags: gene; +symbol: GALC | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^GBA.md | modified | +type: gene; +tags: gene; +symbol: GBA; +chromosome: 1; +protein_length: 536 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^GDF5.md | modified | +type: gene; +tags: gene; +symbol: GDF5 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^GDF8.md | modified | +type: gene; +tags: gene; +symbol: GDF8 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^GFAP.md | modified | +type: gene; +tags: gene; +symbol: GFAP | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^GJA1.md | modified | +type: gene; +tags: gene; +symbol: GJA1; +chromosome: 6; +protein_length: 382 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^GJB2.md | modified | +type: gene; +tags: gene; +symbol: GJB2; +diseases: ['Hearing loss']; +key_papers: 3 citekeys | full_name left empty — needs manual entry |
| ^GJB3.md | modified | +type: gene; +tags: gene; +symbol: GJB3 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^GPR151.md | modified | +type: gene; +tags: gene; +symbol: GPR151 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^GPX1.md | modified | +type: gene; +tags: gene; +symbol: GPX1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^GRB2.md | modified | +type: gene; +tags: gene; +symbol: GRB2 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^GRIA3.md | modified | +type: gene; +tags: gene; +symbol: GRIA3 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^GRIK3.md | modified | +type: gene; +tags: gene; +symbol: GRIK3 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^GRIN2A.md | modified | +type: gene; +tags: gene; +symbol: GRIN2A | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^GRIN2B.md | modified | +type: gene; +tags: gene; +symbol: GRIN2B | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^GRM5.md | modified | +type: gene; +tags: gene; +symbol: GRM5 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^GRN.md | modified | +type: gene; +tags: gene; +symbol: GRN; +key_papers: 1 citekeys | diseases list empty — no disease links found; full_name left empty — needs manual entry |
| ^GRP94.md | modified | +type: gene; +tags: gene; +symbol: GRP94 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^GSK3B.md | modified | +type: gene; +tags: gene; +symbol: GSK3B | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^HDAC7.md | modified | +type: gene; +tags: gene; +symbol: HDAC7 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^HSPG2.md | modified | +type: gene; +tags: gene; +symbol: HSPG2 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^HTRA1.md | modified | +type: gene; +tags: gene; +symbol: HTRA1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^HTT.md | modified | +type: gene; +tags: gene; +symbol: HTT | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^IGF1R.md | modified | +type: gene; +tags: gene; +symbol: IGF1R | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^IL18RA.md | modified | +type: gene; +tags: gene; +symbol: IL18RA | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^IL1B.md | modified | +type: gene; +tags: gene; +symbol: IL1B | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^IL2RA.md | modified | +type: gene; +tags: gene; +symbol: IL2RA | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^INPP5D.md | modified | +type: gene; +tags: gene; +symbol: INPP5D | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^ITGA7.md | modified | +type: gene; +tags: gene; +symbol: ITGA7 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^ITGAM.md | modified | +type: gene; +tags: gene; +symbol: ITGAM | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^ITGB5.md | modified | +type: gene; +tags: gene; +symbol: ITGB5 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^ITM2B.md | modified | +type: gene; +tags: gene; +symbol: ITM2B | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^JAK1.md | modified | +type: gene; +tags: gene; +symbol: JAK1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^JAK3.md | modified | +type: gene; +tags: gene; +symbol: JAK3 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^KCNJ10.md | modified | +type: gene; +tags: gene; +symbol: KCNJ10 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^KCNK13.md | modified | +type: gene; +tags: gene; +symbol: KCNK13 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^KCNQ4.md | modified | +type: gene; +tags: gene; +symbol: KCNQ4; +key_papers: 1 citekeys | diseases list empty — no disease links found; full_name left empty — needs manual entry |
| ^KIF1A.md | modified | +type: gene; +tags: gene; +symbol: KIF1A | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^KIF5A.md | modified | +type: gene; +tags: gene; +symbol: KIF5A | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^LAMA2.md | modified | +type: gene; +tags: gene; +symbol: LAMA2 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^LBP.md | modified | +type: gene; +tags: gene; +symbol: LBP | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^LDLR.md | modified | +type: gene; +tags: gene; +symbol: LDLR | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^LOXHD1.md | modified | +type: gene; +tags: gene; +symbol: LOXHD1; +protein_length: 2211; +key_papers: 1 citekeys | diseases list empty — no disease links found; full_name left empty — needs manual entry |
| ^LOXL1.md | modified | +type: gene; +tags: gene; +symbol: LOXL1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^LPL.md | modified | +type: gene; +tags: gene; +symbol: LPL | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^LRP1.md | modified | +type: gene; +tags: gene; +symbol: LRP1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^LRRK2 and idiopathic Parkinson’s Disease.md | modified | +type: gene; +tags: gene; +symbol: LRRK2 and idiopathic Parkinson’s Disease; +key_papers: 2 citekeys | diseases list empty — no disease links found; full_name left empty — needs manual entry |
| ^LRRK2 – Therapeutic Strategies.md | modified | +type: gene; +tags: gene; +symbol: LRRK2 – Therapeutic Strategies; +diseases: ["Parkinson's Disease"]; +key_papers: 4 citekeys | full_name left empty — needs manual entry |
| ^LRRK2 – biomarkers.md | modified | +type: gene; +tags: gene; +symbol: LRRK2 – biomarkers; +diseases: ["Parkinson's Disease"]; +key_papers: 4 citekeys | full_name left empty — needs manual entry |
| ^LRRK2 – mouseModels.md | modified | +type: gene; +tags: gene; +symbol: LRRK2 – mouseModels | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^LRRK2.md | modified | +type: gene; +tags: gene; +symbol: LRRK2; +diseases: ["Crohn's Disease", 'leprosy', 'tuberculosis', "Parkinson's Disease"]; +key_papers: 8 citekeys | full_name left empty — needs manual entry |
| ^MARCKS.md | modified | +type: gene; +tags: gene; +symbol: MARCKS | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^MCI and APOE.md | modified | +type: gene; +tags: gene; +symbol: MCI and APOE; +diseases: ['MCI']; +key_papers: 4 citekeys | full_name left empty — needs manual entry |
| ^MECP2.md | modified | +type: gene; +tags: gene; +symbol: MECP2 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^MITF.md | modified | +type: gene; +tags: gene; +symbol: MITF | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^MLH1.md | modified | +type: gene; +tags: gene; +symbol: MLH1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^MN1.md | modified | +type: gene; +tags: gene; +symbol: MN1; +key_papers: 1 citekeys | diseases list empty — no disease links found; full_name left empty — needs manual entry |
| ^MND1.md | modified | +type: gene; +tags: gene; +symbol: MND1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^MS4A1.md | modified | +type: gene; +tags: gene; +symbol: MS4A1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^MS4A4A.md | modified | +type: gene; +tags: gene; +symbol: MS4A4A; +targeted_by: ['AL014'] | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^MS4A6A.md | modified | +type: gene; +tags: gene; +symbol: MS4A6A; +diseases: ["Alzheimer's Disease"] | key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^MSH3.md | modified | +type: gene; +tags: gene; +symbol: MSH3 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^MSR1.md | modified | +type: gene; +tags: gene; +symbol: MSR1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^MTFHR.md | modified | +type: gene; +tags: gene; +symbol: MTFHR | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^MYOC.md | modified | +type: gene; +tags: gene; +symbol: MYOC; +chromosome: y; +protein_length: 504; +diseases: ['Juvenile Open-Angle Glaucoma', 'Glaucoma']; +key_papers: 9 citekeys | full_name left empty — needs manual entry |
| ^MYRF.md | modified | +type: gene; +tags: gene; +symbol: MYRF | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^NEFL.md | modified | +type: gene; +tags: gene; +symbol: NEFL | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^NEGR1.md | modified | +type: gene; +tags: gene; +symbol: NEGR1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^NEK1.md | modified | +type: gene; +tags: gene; +symbol: NEK1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^NFE2L1.md | modified | +type: gene; +tags: gene; +symbol: NFE2L1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^NGFR.md | modified | +type: gene; +tags: gene; +symbol: NGFR | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^NLRC4.md | modified | +type: gene; +tags: gene; +symbol: NLRC4 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^NLRP12.md | modified | +type: gene; +tags: gene; +symbol: NLRP12 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^NLRP3.md | modified | +type: gene; +tags: gene; +symbol: NLRP3; +key_papers: 1 citekeys | diseases list empty — no disease links found; full_name left empty — needs manual entry |
| ^NLRP8.md | modified | +type: gene; +tags: gene; +symbol: NLRP8 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^NOD2.md | modified | +type: gene; +tags: gene; +symbol: NOD2 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^NOTCH3.md | modified | +type: gene; +tags: gene; +symbol: NOTCH3; +protein_length: 321 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^NOX4.md | modified | +type: gene; +tags: gene; +symbol: NOX4 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^NRXN1.md | modified | +type: gene; +tags: gene; +symbol: NRXN1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^NVL.md | modified | +type: gene; +tags: gene; +symbol: NVL | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^OCA2.md | modified | +type: gene; +tags: gene; +symbol: OCA2 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^OPN1LW.md | modified | +type: gene; +tags: gene; +symbol: OPN1LW | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^OPN1MW.md | modified | +type: gene; +tags: gene; +symbol: OPN1MW | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^OPN1SW.md | modified | +type: gene; +tags: gene; +symbol: OPN1SW | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^OPRM1.md | modified | +type: gene; +tags: gene; +symbol: OPRM1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^OPTN.md | modified | +type: gene; +tags: gene; +symbol: OPTN | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^OTOF.md | modified | +type: gene; +tags: gene; +symbol: OTOF; +key_papers: 2 citekeys | diseases list empty — no disease links found; full_name left empty — needs manual entry |
| ^P2RX3.md | modified | +type: gene; +tags: gene; +symbol: P2RX3 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^P2RY12.md | modified | +type: gene; +tags: gene; +symbol: P2RY12; +targeted_by: ['clopidogrel']; +key_papers: 1 citekeys | diseases list empty — no disease links found; full_name left empty — needs manual entry |
| ^P2RY13.md | modified | +type: gene; +tags: gene; +symbol: P2RY13 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^P2Y12.md | modified | +type: gene; +tags: gene; +symbol: P2Y12 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^PACS1 neurodevelopmental disorder.md | modified | +type: gene; +tags: gene; +symbol: PACS1 neurodevelopmental disorder | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^PANK2.md | modified | +type: gene; +tags: gene; +symbol: PANK2 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^PCSK9.md | modified | +type: gene; +tags: gene; +symbol: PCSK9 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^PECAM1.md | modified | +type: gene; +tags: gene; +symbol: PECAM1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^PICALM.md | modified | +type: gene; +tags: gene; +symbol: PICALM | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^PINK1.md | modified | +type: gene; +tags: gene; +symbol: PINK1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^PLCG2.md | modified | +type: gene; +tags: gene; +symbol: PLCG2 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^PLD2.md | modified | +type: gene; +tags: gene; +symbol: PLD2 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^PLP1.md | modified | +type: gene; +tags: gene; +symbol: PLP1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^PMS1.md | modified | +type: gene; +tags: gene; +symbol: PMS1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^POLD1.md | modified | +type: gene; +tags: gene; +symbol: POLD1; +diseases: ["Huntington's Disease (HD)"] | key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^PRF1.md | modified | +type: gene; +tags: gene; +symbol: PRF1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^PRKN.md | modified | +type: gene; +tags: gene; +symbol: PRKN | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^PRKRA.md | modified | +type: gene; +tags: gene; +symbol: PRKRA | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^PRNP.md | modified | +type: gene; +tags: gene; +symbol: PRNP | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^PSEN1.md | modified | +type: gene; +tags: gene; +symbol: PSEN1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^PSEN2.md | modified | +type: gene; +tags: gene; +symbol: PSEN2 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^PSMB5.md | modified | +type: gene; +tags: gene; +symbol: PSMB5 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^PSMB8.md | modified | +type: gene; +tags: gene; +symbol: PSMB8 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^PSMF1.md | modified | +type: gene; +tags: gene; +symbol: PSMF1; +key_papers: 2 citekeys | diseases list empty — no disease links found; full_name left empty — needs manual entry |
| ^PTPRC.md | modified | +type: gene; +tags: gene; +symbol: PTPRC | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^REST.md | modified | +type: gene; +tags: gene; +symbol: REST | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^RIPK1.md | modified | +type: gene; +tags: gene; +symbol: RIPK1; +diseases: ["Alzheimer's Disease", 'ALS'] | key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^RNF213.md | modified | +type: gene; +tags: gene; +symbol: RNF213 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^ROCK1.md | modified | +type: gene; +tags: gene; +symbol: ROCK1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^ROCK2.md | modified | +type: gene; +tags: gene; +symbol: ROCK2 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^RPE65.md | modified | +type: gene; +tags: gene; +symbol: RPE65 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^RPGR.md | modified | +type: gene; +tags: gene; +symbol: RPGR | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^RRAS.md | modified | +type: gene; +tags: gene; +symbol: RRAS | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^RS1.md | modified | +type: gene; +tags: gene; +symbol: RS1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^SARM1.md | modified | +type: gene; +tags: gene; +symbol: SARM1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^SCN10A.md | modified | +type: gene; +tags: gene; +symbol: SCN10A | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^SCN11A.md | modified | +type: gene; +tags: gene; +symbol: SCN11A; +key_papers: 1 citekeys | diseases list empty — no disease links found; full_name left empty — needs manual entry |
| ^SCN1A.md | modified | +type: gene; +tags: gene; +symbol: SCN1A | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^SCN2A.md | modified | +type: gene; +tags: gene; +symbol: SCN2A | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^SCN9A.md | modified | +type: gene; +tags: gene; +symbol: SCN9A; +protein_length: 1977 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^SETD1A.md | modified | +type: gene; +tags: gene; +symbol: SETD1A | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^SH2B3.md | modified | +type: gene; +tags: gene; +symbol: SH2B3 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^SLC26A2.md | modified | +type: gene; +tags: gene; +symbol: SLC26A2 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^SLC26A3.md | modified | +type: gene; +tags: gene; +symbol: SLC26A3 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^SLC26A4.md | modified | +type: gene; +tags: gene; +symbol: SLC26A4; +diseases: ['Pendred syndrome']; +key_papers: 2 citekeys | full_name left empty — needs manual entry |
| ^SLC2A1.md | modified | +type: gene; +tags: gene; +symbol: SLC2A1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^SNCA.md | modified | +type: gene; +tags: gene; +symbol: SNCA; +protein_length: 140 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^SOD1.md | modified | +type: gene; +tags: gene; +symbol: SOD1; +protein_length: 153 | key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^SORL1.md | modified | +type: gene; +tags: gene; +symbol: SORL1; +diseases: ["Alzheimer's Disease", 'Alzheimers Disease Early Onset–EOAD']; +key_papers: 9 citekeys | full_name left empty — needs manual entry |
| ^SORT1.md | modified | +type: gene; +tags: gene; +symbol: SORT1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^SOST.md | modified | +type: gene; +tags: gene; +symbol: SOST | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^SPP1.md | modified | +type: gene; +tags: gene; +symbol: SPP1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^STARD3.md | modified | +type: gene; +tags: gene; +symbol: STARD3 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^STAT3.md | modified | +type: gene; +tags: gene; +symbol: STAT3 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^STING1.md | modified | +type: gene; +tags: gene; +symbol: STING1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^STRC.md | modified | +type: gene; +tags: gene; +symbol: STRC; +chromosome: 15 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^SYNGAP1.md | modified | +type: gene; +tags: gene; +symbol: SYNGAP1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^Selplg.md | modified | +type: gene; +tags: gene; +symbol: Selplg | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^Slc2a5.md | modified | +type: gene; +tags: gene; +symbol: Slc2a5 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^TARDBP.md | modified | +type: gene; +tags: gene; +symbol: TARDBP; +diseases: ['ALS', 'Frontotemporal Dementia'] | key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^TBK1.md | modified | +type: gene; +tags: gene; +symbol: TBK1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^TCF4.md | modified | +type: gene; +tags: gene; +symbol: TCF4 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^TECTA.md | modified | +type: gene; +tags: gene; +symbol: TECTA | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^TFRC.md | modified | +type: gene; +tags: gene; +symbol: TFRC | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^TGFB1.md | modified | +type: gene; +tags: gene; +symbol: TGFB1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^TGFBI.md | modified | +type: gene; +tags: gene; +symbol: TGFBI | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^TMC1.md | modified | +type: gene; +tags: gene; +symbol: TMC1; +protein_length: 760; +key_papers: 2 citekeys | diseases list empty — no disease links found; full_name left empty — needs manual entry |
| ^TMEM106B.md | modified | +type: gene; +tags: gene; +symbol: TMEM106B | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^TMEM119.md | modified | +type: gene; +tags: gene; +symbol: TMEM119 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^TMEM175.md | modified | +type: gene; +tags: gene; +symbol: TMEM175 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^TMEM98.md | modified | +type: gene; +tags: gene; +symbol: TMEM98 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^TMPRSS3.md | modified | +type: gene; +tags: gene; +symbol: TMPRSS3 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^TNFRSF1A.md | modified | +type: gene; +tags: gene; +symbol: TNFRSF1A | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^TREM2.md | modified | +type: gene; +tags: gene; +symbol: TREM2; +chromosome: 6; +protein_length: 230; +diseases: ["Alzheimer's Disease"]; +targeted_by: ['AL002', 'Alector', 'Amgen', 'Denali']; +key_papers: 7 citekeys | full_name left empty — needs manual entry |
| ^TRIOBP.md | modified | +type: gene; +tags: gene; +symbol: TRIOBP | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^TRPM8.md | modified | +type: gene; +tags: gene; +symbol: TRPM8; +diseases: ['Migraine'] | key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^TRPV4.md | modified | +type: gene; +tags: gene; +symbol: TRPV4 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^TSHR.md | modified | +type: gene; +tags: gene; +symbol: TSHR | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^TYK2.md | modified | +type: gene; +tags: gene; +symbol: TYK2 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^TYROBP.md | modified | +type: gene; +tags: gene; +symbol: TYROBP | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^UBE3A.md | modified | +type: gene; +tags: gene; +symbol: UBE3A; +diseases: ['15q duplication (dup15q)', 'Angelman Syndrome'] | key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^UBQLN2.md | modified | +type: gene; +tags: gene; +symbol: UBQLN2 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^UNC13A.md | modified | +type: gene; +tags: gene; +symbol: UNC13A; +diseases: ['Frontotemporal Dementia'] | key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^USP30.md | modified | +type: gene; +tags: gene; +symbol: USP30 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^Usp18.md | modified | +type: gene; +tags: gene; +symbol: Usp18 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^VEGFA.md | modified | +type: gene; +tags: gene; +symbol: VEGFA | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |
| ^WFS1.md | modified | +type: gene; +tags: gene; +symbol: WFS1 | diseases list empty — no disease links found; key_papers empty — no paper references found; full_name left empty — needs manual entry |

## Items Requiring Manual Review

*(474 items — excludes full_name warnings since all need manual entry)*

- [ ] ^AAK1.md — diseases list empty — no disease links found
- [ ] ^AAK1.md — key_papers empty — no paper references found
- [ ] ^ABCA1.md — diseases list empty — no disease links found
- [ ] ^ABCA7.md — diseases list empty — no disease links found
- [ ] ^ABCA7.md — key_papers empty — no paper references found
- [ ] ^ADH1B.md — diseases list empty — no disease links found
- [ ] ^ADH1B.md — key_papers empty — no paper references found
- [ ] ^AIF1.md — diseases list empty — no disease links found
- [ ] ^AIF1.md — key_papers empty — no paper references found
- [ ] ^AKAP11.md — diseases list empty — no disease links found
- [ ] ^AKAP11.md — key_papers empty — no paper references found
- [ ] ^AKT1.md — diseases list empty — no disease links found
- [ ] ^AKT1.md — key_papers empty — no paper references found
- [ ] ^ANGPTL3.md — diseases list empty — no disease links found
- [ ] ^ANGPTL3.md — key_papers empty — no paper references found
- [ ] ^ANGPTL7.md — diseases list empty — no disease links found
- [ ] ^ANKRD11.md — diseases list empty — no disease links found
- [ ] ^ANKRD11.md — key_papers empty — no paper references found
- [ ] ^ANKRD55.md — diseases list empty — no disease links found
- [ ] ^ANKRD55.md — key_papers empty — no paper references found
- [ ] ^ANO4.md — diseases list empty — no disease links found
- [ ] ^APOB.md — diseases list empty — no disease links found
- [ ] ^APOB.md — key_papers empty — no paper references found
- [ ] ^APOC3.md — diseases list empty — no disease links found
- [ ] ^APOC3.md — key_papers empty — no paper references found
- [ ] ^APOL1.md — diseases list empty — no disease links found
- [ ] ^APP.md — diseases list empty — no disease links found
- [ ] ^AQP4.md — diseases list empty — no disease links found
- [ ] ^ASPA.md — diseases list empty — no disease links found
- [ ] ^ASPA.md — key_papers empty — no paper references found
- [ ] ^ASXL.md — diseases list empty — no disease links found
- [ ] ^ASXL.md — key_papers empty — no paper references found
- [ ] ^ATOH1.md — diseases list empty — no disease links found
- [ ] ^ATOH1.md — key_papers empty — no paper references found
- [ ] ^ATP7B.md — diseases list empty — no disease links found
- [ ] ^ATP7B.md — key_papers empty — no paper references found
- [ ] ^ATP8B4.md — diseases list empty — no disease links found
- [ ] ^ATP8B4.md — key_papers empty — no paper references found
- [ ] ^ATXN3.md — diseases list empty — no disease links found
- [ ] ^ATXN3.md — key_papers empty — no paper references found
- [ ] ^AXL.md — diseases list empty — no disease links found
- [ ] ^AXL.md — key_papers empty — no paper references found
- [ ] ^BDNF.md — diseases list empty — no disease links found
- [ ] ^BDNF.md — key_papers empty — no paper references found
- [ ] ^BEST1.md — diseases list empty — no disease links found
- [ ] ^BEST1.md — key_papers empty — no paper references found
- [ ] ^BIN1.md — key_papers empty — no paper references found
- [ ] ^BMPR2.md — diseases list empty — no disease links found
- [ ] ^BMPR2.md — key_papers empty — no paper references found
- [ ] ^BRCA1.md — diseases list empty — no disease links found
- [ ] ^BRCA1.md — key_papers empty — no paper references found
- [ ] ^C1Q.md — diseases list empty — no disease links found
- [ ] ^C1Q.md — key_papers empty — no paper references found
- [ ] ^C2.md — diseases list empty — no disease links found
- [ ] ^C2.md — key_papers empty — no paper references found
- [ ] ^C3.md — diseases list empty — no disease links found
- [ ] ^C3.md — key_papers empty — no paper references found
- [ ] ^C4A.md — diseases list empty — no disease links found
- [ ] ^C4A.md — key_papers empty — no paper references found
- [ ] ^C4B.md — diseases list empty — no disease links found
- [ ] ^C4B.md — key_papers empty — no paper references found
- [ ] ^C5.md — diseases list empty — no disease links found
- [ ] ^C5.md — key_papers empty — no paper references found
- [ ] ^C9.md — diseases list empty — no disease links found
- [ ] ^C9.md — key_papers empty — no paper references found
- [ ] ^C9orf72.md — diseases list empty — no disease links found
- [ ] ^CA2.md — diseases list empty — no disease links found
- [ ] ^CA2.md — key_papers empty — no paper references found
- [ ] ^CALCA.md — diseases list empty — no disease links found
- [ ] ^CALCA.md — key_papers empty — no paper references found
- [ ] ^CALCB.md — diseases list empty — no disease links found
- [ ] ^CALCB.md — key_papers empty — no paper references found
- [ ] ^CBLB.md — diseases list empty — no disease links found
- [ ] ^CBLB.md — key_papers empty — no paper references found
- [ ] ^CCL3.md — diseases list empty — no disease links found
- [ ] ^CCL3.md — key_papers empty — no paper references found
- [ ] ^CCR5.md — diseases list empty — no disease links found
- [ ] ^CCR5.md — key_papers empty — no paper references found
- [ ] ^CD2.md — diseases list empty — no disease links found
- [ ] ^CD2.md — key_papers empty — no paper references found
- [ ] ^CD2AP.md — diseases list empty — no disease links found
- [ ] ^CD2AP.md — key_papers empty — no paper references found
- [ ] ^CD33.md — diseases list empty — no disease links found
- [ ] ^CD40.md — key_papers empty — no paper references found
- [ ] ^CD52.md — diseases list empty — no disease links found
- [ ] ^CD52.md — key_papers empty — no paper references found
- [ ] ^CD58.md — key_papers empty — no paper references found
- [ ] ^CD59.md — diseases list empty — no disease links found
- [ ] ^CD59.md — key_papers empty — no paper references found
- [ ] ^CD68.md — diseases list empty — no disease links found
- [ ] ^CD68.md — key_papers empty — no paper references found
- [ ] ^CD74.md — diseases list empty — no disease links found
- [ ] ^CD74.md — key_papers empty — no paper references found
- [ ] ^CD83.md — diseases list empty — no disease links found
- [ ] ^CD83.md — key_papers empty — no paper references found
- [ ] ^CFB.md — diseases list empty — no disease links found
- [ ] ^CFB.md — key_papers empty — no paper references found
- [ ] ^CFD.md — diseases list empty — no disease links found
- [ ] ^CFD.md — key_papers empty — no paper references found
- [ ] ^CFH.md — diseases list empty — no disease links found
- [ ] ^CFHR5.md — diseases list empty — no disease links found
- [ ] ^CFHR5.md — key_papers empty — no paper references found
- [ ] ^CFI.md — diseases list empty — no disease links found
- [ ] ^CFI.md — key_papers empty — no paper references found
- [ ] ^CGRP.md — diseases list empty — no disease links found
- [ ] ^CHD8.md — diseases list empty — no disease links found
- [ ] ^CHD8.md — key_papers empty — no paper references found
- [ ] ^CHRNA3.md — diseases list empty — no disease links found
- [ ] ^CHRNA3.md — key_papers empty — no paper references found
- [ ] ^CHRNA4.md — diseases list empty — no disease links found
- [ ] ^CHRNA4.md — key_papers empty — no paper references found
- [ ] ^CHRNA5.md — diseases list empty — no disease links found
- [ ] ^CHRNB2.md — diseases list empty — no disease links found
- [ ] ^CHRNB3.md — diseases list empty — no disease links found
- [ ] ^CHRNB3.md — key_papers empty — no paper references found
- [ ] ^CLEC7A.md — diseases list empty — no disease links found
- [ ] ^CLEC7A.md — key_papers empty — no paper references found
- [ ] ^COL4A3.md — diseases list empty — no disease links found
- [ ] ^COL4A3.md — key_papers empty — no paper references found
- [ ] ^COL4A4.md — diseases list empty — no disease links found
- [ ] ^COL4A4.md — key_papers empty — no paper references found
- [ ] ^COL4A5.md — diseases list empty — no disease links found
- [ ] ^COL4A5.md — key_papers empty — no paper references found
- [ ] ^CRB1.md — diseases list empty — no disease links found
- [ ] ^CRB1.md — key_papers empty — no paper references found
- [ ] ^CRX.md — diseases list empty — no disease links found
- [ ] ^CRX.md — key_papers empty — no paper references found
- [ ] ^CSF1R.md — diseases list empty — no disease links found
- [ ] ^CST7.md — diseases list empty — no disease links found
- [ ] ^CST7.md — key_papers empty — no paper references found
- [ ] ^CTSD.md — diseases list empty — no disease links found
- [ ] ^CTSD.md — key_papers empty — no paper references found
- [ ] ^CX3CR1.md — diseases list empty — no disease links found
- [ ] ^CX3CR1.md — key_papers empty — no paper references found
- [ ] ^CYP1B1.md — key_papers empty — no paper references found
- [ ] ^DAG1.md — diseases list empty — no disease links found
- [ ] ^DAG1.md — key_papers empty — no paper references found
- [ ] ^DNAJC7.md — diseases list empty — no disease links found
- [ ] ^DNAJC7.md — key_papers empty — no paper references found
- [ ] ^EGFR.md — diseases list empty — no disease links found
- [ ] ^EIF2B.md — diseases list empty — no disease links found
- [ ] ^EIF2B.md — key_papers empty — no paper references found
- [ ] ^EPHA1.md — diseases list empty — no disease links found
- [ ] ^EPHA1.md — key_papers empty — no paper references found
- [ ] ^ESR1.md — diseases list empty — no disease links found
- [ ] ^ESR1.md — key_papers empty — no paper references found
- [ ] ^FAN1.md — diseases list empty — no disease links found
- [ ] ^FAN1.md — key_papers empty — no paper references found
- [ ] ^FBXO7.md — diseases list empty — no disease links found
- [ ] ^FBXO7.md — key_papers empty — no paper references found
- [ ] ^FGF14.md — diseases list empty — no disease links found
- [ ] ^FGF14.md — key_papers empty — no paper references found
- [ ] ^FLG.md — diseases list empty — no disease links found
- [ ] ^FLG.md — key_papers empty — no paper references found
- [ ] ^FOXI1.md — diseases list empty — no disease links found
- [ ] ^FOXI1.md — key_papers empty — no paper references found
- [ ] ^FOXO3.md — diseases list empty — no disease links found
- [ ] ^FOXO3.md — key_papers empty — no paper references found
- [ ] ^FOXP3.md — diseases list empty — no disease links found
- [ ] ^FOXP3.md — key_papers empty — no paper references found
- [ ] ^FUS.md — key_papers empty — no paper references found
- [ ] ^Fcgr2.md — diseases list empty — no disease links found
- [ ] ^Fcgr2.md — key_papers empty — no paper references found
- [ ] ^GALC.md — diseases list empty — no disease links found
- [ ] ^GALC.md — key_papers empty — no paper references found
- [ ] ^GBA.md — diseases list empty — no disease links found
- [ ] ^GBA.md — key_papers empty — no paper references found
- [ ] ^GDF5.md — diseases list empty — no disease links found
- [ ] ^GDF5.md — key_papers empty — no paper references found
- [ ] ^GDF8.md — diseases list empty — no disease links found
- [ ] ^GDF8.md — key_papers empty — no paper references found
- [ ] ^GFAP.md — diseases list empty — no disease links found
- [ ] ^GFAP.md — key_papers empty — no paper references found
- [ ] ^GJA1.md — diseases list empty — no disease links found
- [ ] ^GJA1.md — key_papers empty — no paper references found
- [ ] ^GJB3.md — diseases list empty — no disease links found
- [ ] ^GJB3.md — key_papers empty — no paper references found
- [ ] ^GPR151.md — diseases list empty — no disease links found
- [ ] ^GPR151.md — key_papers empty — no paper references found
- [ ] ^GPX1.md — diseases list empty — no disease links found
- [ ] ^GPX1.md — key_papers empty — no paper references found
- [ ] ^GRB2.md — diseases list empty — no disease links found
- [ ] ^GRB2.md — key_papers empty — no paper references found
- [ ] ^GRIA3.md — diseases list empty — no disease links found
- [ ] ^GRIA3.md — key_papers empty — no paper references found
- [ ] ^GRIK3.md — diseases list empty — no disease links found
- [ ] ^GRIK3.md — key_papers empty — no paper references found
- [ ] ^GRIN2A.md — diseases list empty — no disease links found
- [ ] ^GRIN2A.md — key_papers empty — no paper references found
- [ ] ^GRIN2B.md — diseases list empty — no disease links found
- [ ] ^GRIN2B.md — key_papers empty — no paper references found
- [ ] ^GRM5.md — diseases list empty — no disease links found
- [ ] ^GRM5.md — key_papers empty — no paper references found
- [ ] ^GRN.md — diseases list empty — no disease links found
- [ ] ^GRP94.md — diseases list empty — no disease links found
- [ ] ^GRP94.md — key_papers empty — no paper references found
- [ ] ^GSK3B.md — diseases list empty — no disease links found
- [ ] ^GSK3B.md — key_papers empty — no paper references found
- [ ] ^HDAC7.md — diseases list empty — no disease links found
- [ ] ^HDAC7.md — key_papers empty — no paper references found
- [ ] ^HSPG2.md — diseases list empty — no disease links found
- [ ] ^HSPG2.md — key_papers empty — no paper references found
- [ ] ^HTRA1.md — diseases list empty — no disease links found
- [ ] ^HTRA1.md — key_papers empty — no paper references found
- [ ] ^HTT.md — diseases list empty — no disease links found
- [ ] ^HTT.md — key_papers empty — no paper references found
- [ ] ^IGF1R.md — diseases list empty — no disease links found
- [ ] ^IGF1R.md — key_papers empty — no paper references found
- [ ] ^IL18RA.md — diseases list empty — no disease links found
- [ ] ^IL18RA.md — key_papers empty — no paper references found
- [ ] ^IL1B.md — diseases list empty — no disease links found
- [ ] ^IL1B.md — key_papers empty — no paper references found
- [ ] ^IL2RA.md — diseases list empty — no disease links found
- [ ] ^IL2RA.md — key_papers empty — no paper references found
- [ ] ^INPP5D.md — diseases list empty — no disease links found
- [ ] ^INPP5D.md — key_papers empty — no paper references found
- [ ] ^ITGA7.md — diseases list empty — no disease links found
- [ ] ^ITGA7.md — key_papers empty — no paper references found
- [ ] ^ITGAM.md — diseases list empty — no disease links found
- [ ] ^ITGAM.md — key_papers empty — no paper references found
- [ ] ^ITGB5.md — diseases list empty — no disease links found
- [ ] ^ITGB5.md — key_papers empty — no paper references found
- [ ] ^ITM2B.md — diseases list empty — no disease links found
- [ ] ^ITM2B.md — key_papers empty — no paper references found
- [ ] ^JAK1.md — diseases list empty — no disease links found
- [ ] ^JAK1.md — key_papers empty — no paper references found
- [ ] ^JAK3.md — diseases list empty — no disease links found
- [ ] ^JAK3.md — key_papers empty — no paper references found
- [ ] ^KCNJ10.md — diseases list empty — no disease links found
- [ ] ^KCNJ10.md — key_papers empty — no paper references found
- [ ] ^KCNK13.md — diseases list empty — no disease links found
- [ ] ^KCNK13.md — key_papers empty — no paper references found
- [ ] ^KCNQ4.md — diseases list empty — no disease links found
- [ ] ^KIF1A.md — diseases list empty — no disease links found
- [ ] ^KIF1A.md — key_papers empty — no paper references found
- [ ] ^KIF5A.md — diseases list empty — no disease links found
- [ ] ^KIF5A.md — key_papers empty — no paper references found
- [ ] ^LAMA2.md — diseases list empty — no disease links found
- [ ] ^LAMA2.md — key_papers empty — no paper references found
- [ ] ^LBP.md — diseases list empty — no disease links found
- [ ] ^LBP.md — key_papers empty — no paper references found
- [ ] ^LDLR.md — diseases list empty — no disease links found
- [ ] ^LDLR.md — key_papers empty — no paper references found
- [ ] ^LOXHD1.md — diseases list empty — no disease links found
- [ ] ^LOXL1.md — diseases list empty — no disease links found
- [ ] ^LOXL1.md — key_papers empty — no paper references found
- [ ] ^LPL.md — diseases list empty — no disease links found
- [ ] ^LPL.md — key_papers empty — no paper references found
- [ ] ^LRP1.md — diseases list empty — no disease links found
- [ ] ^LRP1.md — key_papers empty — no paper references found
- [ ] ^LRRK2 and idiopathic Parkinson’s Disease.md — diseases list empty — no disease links found
- [ ] ^LRRK2 – mouseModels.md — diseases list empty — no disease links found
- [ ] ^LRRK2 – mouseModels.md — key_papers empty — no paper references found
- [ ] ^MARCKS.md — diseases list empty — no disease links found
- [ ] ^MARCKS.md — key_papers empty — no paper references found
- [ ] ^MECP2.md — diseases list empty — no disease links found
- [ ] ^MECP2.md — key_papers empty — no paper references found
- [ ] ^MITF.md — diseases list empty — no disease links found
- [ ] ^MITF.md — key_papers empty — no paper references found
- [ ] ^MLH1.md — diseases list empty — no disease links found
- [ ] ^MLH1.md — key_papers empty — no paper references found
- [ ] ^MN1.md — diseases list empty — no disease links found
- [ ] ^MND1.md — diseases list empty — no disease links found
- [ ] ^MND1.md — key_papers empty — no paper references found
- [ ] ^MS4A1.md — diseases list empty — no disease links found
- [ ] ^MS4A1.md — key_papers empty — no paper references found
- [ ] ^MS4A4A.md — diseases list empty — no disease links found
- [ ] ^MS4A4A.md — key_papers empty — no paper references found
- [ ] ^MS4A6A.md — key_papers empty — no paper references found
- [ ] ^MSH3.md — diseases list empty — no disease links found
- [ ] ^MSH3.md — key_papers empty — no paper references found
- [ ] ^MSR1.md — diseases list empty — no disease links found
- [ ] ^MSR1.md — key_papers empty — no paper references found
- [ ] ^MTFHR.md — diseases list empty — no disease links found
- [ ] ^MTFHR.md — key_papers empty — no paper references found
- [ ] ^MYRF.md — diseases list empty — no disease links found
- [ ] ^MYRF.md — key_papers empty — no paper references found
- [ ] ^NEFL.md — diseases list empty — no disease links found
- [ ] ^NEFL.md — key_papers empty — no paper references found
- [ ] ^NEGR1.md — diseases list empty — no disease links found
- [ ] ^NEGR1.md — key_papers empty — no paper references found
- [ ] ^NEK1.md — diseases list empty — no disease links found
- [ ] ^NEK1.md — key_papers empty — no paper references found
- [ ] ^NFE2L1.md — diseases list empty — no disease links found
- [ ] ^NFE2L1.md — key_papers empty — no paper references found
- [ ] ^NGFR.md — diseases list empty — no disease links found
- [ ] ^NGFR.md — key_papers empty — no paper references found
- [ ] ^NLRC4.md — diseases list empty — no disease links found
- [ ] ^NLRC4.md — key_papers empty — no paper references found
- [ ] ^NLRP12.md — diseases list empty — no disease links found
- [ ] ^NLRP12.md — key_papers empty — no paper references found
- [ ] ^NLRP3.md — diseases list empty — no disease links found
- [ ] ^NLRP8.md — diseases list empty — no disease links found
- [ ] ^NLRP8.md — key_papers empty — no paper references found
- [ ] ^NOD2.md — diseases list empty — no disease links found
- [ ] ^NOD2.md — key_papers empty — no paper references found
- [ ] ^NOTCH3.md — diseases list empty — no disease links found
- [ ] ^NOTCH3.md — key_papers empty — no paper references found
- [ ] ^NOX4.md — diseases list empty — no disease links found
- [ ] ^NOX4.md — key_papers empty — no paper references found
- [ ] ^NRXN1.md — diseases list empty — no disease links found
- [ ] ^NRXN1.md — key_papers empty — no paper references found
- [ ] ^NVL.md — diseases list empty — no disease links found
- [ ] ^NVL.md — key_papers empty — no paper references found
- [ ] ^OCA2.md — diseases list empty — no disease links found
- [ ] ^OCA2.md — key_papers empty — no paper references found
- [ ] ^OPN1LW.md — diseases list empty — no disease links found
- [ ] ^OPN1LW.md — key_papers empty — no paper references found
- [ ] ^OPN1MW.md — diseases list empty — no disease links found
- [ ] ^OPN1MW.md — key_papers empty — no paper references found
- [ ] ^OPN1SW.md — diseases list empty — no disease links found
- [ ] ^OPN1SW.md — key_papers empty — no paper references found
- [ ] ^OPRM1.md — diseases list empty — no disease links found
- [ ] ^OPRM1.md — key_papers empty — no paper references found
- [ ] ^OPTN.md — diseases list empty — no disease links found
- [ ] ^OPTN.md — key_papers empty — no paper references found
- [ ] ^OTOF.md — diseases list empty — no disease links found
- [ ] ^P2RX3.md — diseases list empty — no disease links found
- [ ] ^P2RX3.md — key_papers empty — no paper references found
- [ ] ^P2RY12.md — diseases list empty — no disease links found
- [ ] ^P2RY13.md — diseases list empty — no disease links found
- [ ] ^P2RY13.md — key_papers empty — no paper references found
- [ ] ^P2Y12.md — diseases list empty — no disease links found
- [ ] ^P2Y12.md — key_papers empty — no paper references found
- [ ] ^PACS1 neurodevelopmental disorder.md — diseases list empty — no disease links found
- [ ] ^PACS1 neurodevelopmental disorder.md — key_papers empty — no paper references found
- [ ] ^PANK2.md — diseases list empty — no disease links found
- [ ] ^PANK2.md — key_papers empty — no paper references found
- [ ] ^PCSK9.md — diseases list empty — no disease links found
- [ ] ^PCSK9.md — key_papers empty — no paper references found
- [ ] ^PECAM1.md — diseases list empty — no disease links found
- [ ] ^PECAM1.md — key_papers empty — no paper references found
- [ ] ^PICALM.md — diseases list empty — no disease links found
- [ ] ^PICALM.md — key_papers empty — no paper references found
- [ ] ^PINK1.md — diseases list empty — no disease links found
- [ ] ^PINK1.md — key_papers empty — no paper references found
- [ ] ^PLCG2.md — diseases list empty — no disease links found
- [ ] ^PLCG2.md — key_papers empty — no paper references found
- [ ] ^PLD2.md — diseases list empty — no disease links found
- [ ] ^PLD2.md — key_papers empty — no paper references found
- [ ] ^PLP1.md — diseases list empty — no disease links found
- [ ] ^PLP1.md — key_papers empty — no paper references found
- [ ] ^PMS1.md — diseases list empty — no disease links found
- [ ] ^PMS1.md — key_papers empty — no paper references found
- [ ] ^POLD1.md — key_papers empty — no paper references found
- [ ] ^PRF1.md — diseases list empty — no disease links found
- [ ] ^PRF1.md — key_papers empty — no paper references found
- [ ] ^PRKN.md — diseases list empty — no disease links found
- [ ] ^PRKN.md — key_papers empty — no paper references found
- [ ] ^PRKRA.md — diseases list empty — no disease links found
- [ ] ^PRKRA.md — key_papers empty — no paper references found
- [ ] ^PRNP.md — diseases list empty — no disease links found
- [ ] ^PRNP.md — key_papers empty — no paper references found
- [ ] ^PSEN1.md — diseases list empty — no disease links found
- [ ] ^PSEN1.md — key_papers empty — no paper references found
- [ ] ^PSEN2.md — diseases list empty — no disease links found
- [ ] ^PSEN2.md — key_papers empty — no paper references found
- [ ] ^PSMB5.md — diseases list empty — no disease links found
- [ ] ^PSMB5.md — key_papers empty — no paper references found
- [ ] ^PSMB8.md — diseases list empty — no disease links found
- [ ] ^PSMB8.md — key_papers empty — no paper references found
- [ ] ^PSMF1.md — diseases list empty — no disease links found
- [ ] ^PTPRC.md — diseases list empty — no disease links found
- [ ] ^PTPRC.md — key_papers empty — no paper references found
- [ ] ^REST.md — diseases list empty — no disease links found
- [ ] ^REST.md — key_papers empty — no paper references found
- [ ] ^RIPK1.md — key_papers empty — no paper references found
- [ ] ^RNF213.md — diseases list empty — no disease links found
- [ ] ^RNF213.md — key_papers empty — no paper references found
- [ ] ^ROCK1.md — diseases list empty — no disease links found
- [ ] ^ROCK1.md — key_papers empty — no paper references found
- [ ] ^ROCK2.md — diseases list empty — no disease links found
- [ ] ^ROCK2.md — key_papers empty — no paper references found
- [ ] ^RPE65.md — diseases list empty — no disease links found
- [ ] ^RPE65.md — key_papers empty — no paper references found
- [ ] ^RPGR.md — diseases list empty — no disease links found
- [ ] ^RPGR.md — key_papers empty — no paper references found
- [ ] ^RRAS.md — diseases list empty — no disease links found
- [ ] ^RRAS.md — key_papers empty — no paper references found
- [ ] ^RS1.md — diseases list empty — no disease links found
- [ ] ^RS1.md — key_papers empty — no paper references found
- [ ] ^SARM1.md — diseases list empty — no disease links found
- [ ] ^SARM1.md — key_papers empty — no paper references found
- [ ] ^SCN10A.md — diseases list empty — no disease links found
- [ ] ^SCN10A.md — key_papers empty — no paper references found
- [ ] ^SCN11A.md — diseases list empty — no disease links found
- [ ] ^SCN1A.md — diseases list empty — no disease links found
- [ ] ^SCN1A.md — key_papers empty — no paper references found
- [ ] ^SCN2A.md — diseases list empty — no disease links found
- [ ] ^SCN2A.md — key_papers empty — no paper references found
- [ ] ^SCN9A.md — diseases list empty — no disease links found
- [ ] ^SCN9A.md — key_papers empty — no paper references found
- [ ] ^SETD1A.md — diseases list empty — no disease links found
- [ ] ^SETD1A.md — key_papers empty — no paper references found
- [ ] ^SH2B3.md — diseases list empty — no disease links found
- [ ] ^SH2B3.md — key_papers empty — no paper references found
- [ ] ^SLC26A2.md — diseases list empty — no disease links found
- [ ] ^SLC26A2.md — key_papers empty — no paper references found
- [ ] ^SLC26A3.md — diseases list empty — no disease links found
- [ ] ^SLC26A3.md — key_papers empty — no paper references found
- [ ] ^SLC2A1.md — diseases list empty — no disease links found
- [ ] ^SLC2A1.md — key_papers empty — no paper references found
- [ ] ^SNCA.md — diseases list empty — no disease links found
- [ ] ^SNCA.md — key_papers empty — no paper references found
- [ ] ^SOD1.md — key_papers empty — no paper references found
- [ ] ^SORT1.md — diseases list empty — no disease links found
- [ ] ^SORT1.md — key_papers empty — no paper references found
- [ ] ^SOST.md — diseases list empty — no disease links found
- [ ] ^SOST.md — key_papers empty — no paper references found
- [ ] ^SPP1.md — diseases list empty — no disease links found
- [ ] ^SPP1.md — key_papers empty — no paper references found
- [ ] ^STARD3.md — diseases list empty — no disease links found
- [ ] ^STARD3.md — key_papers empty — no paper references found
- [ ] ^STAT3.md — diseases list empty — no disease links found
- [ ] ^STAT3.md — key_papers empty — no paper references found
- [ ] ^STING1.md — diseases list empty — no disease links found
- [ ] ^STING1.md — key_papers empty — no paper references found
- [ ] ^STRC.md — diseases list empty — no disease links found
- [ ] ^STRC.md — key_papers empty — no paper references found
- [ ] ^SYNGAP1.md — diseases list empty — no disease links found
- [ ] ^SYNGAP1.md — key_papers empty — no paper references found
- [ ] ^Selplg.md — diseases list empty — no disease links found
- [ ] ^Selplg.md — key_papers empty — no paper references found
- [ ] ^Slc2a5.md — diseases list empty — no disease links found
- [ ] ^Slc2a5.md — key_papers empty — no paper references found
- [ ] ^TARDBP.md — key_papers empty — no paper references found
- [ ] ^TBK1.md — diseases list empty — no disease links found
- [ ] ^TBK1.md — key_papers empty — no paper references found
- [ ] ^TCF4.md — diseases list empty — no disease links found
- [ ] ^TCF4.md — key_papers empty — no paper references found
- [ ] ^TECTA.md — diseases list empty — no disease links found
- [ ] ^TECTA.md — key_papers empty — no paper references found
- [ ] ^TFRC.md — diseases list empty — no disease links found
- [ ] ^TFRC.md — key_papers empty — no paper references found
- [ ] ^TGFB1.md — diseases list empty — no disease links found
- [ ] ^TGFB1.md — key_papers empty — no paper references found
- [ ] ^TGFBI.md — diseases list empty — no disease links found
- [ ] ^TGFBI.md — key_papers empty — no paper references found
- [ ] ^TMC1.md — diseases list empty — no disease links found
- [ ] ^TMEM106B.md — diseases list empty — no disease links found
- [ ] ^TMEM106B.md — key_papers empty — no paper references found
- [ ] ^TMEM119.md — diseases list empty — no disease links found
- [ ] ^TMEM119.md — key_papers empty — no paper references found
- [ ] ^TMEM175.md — diseases list empty — no disease links found
- [ ] ^TMEM175.md — key_papers empty — no paper references found
- [ ] ^TMEM98.md — diseases list empty — no disease links found
- [ ] ^TMEM98.md — key_papers empty — no paper references found
- [ ] ^TMPRSS3.md — diseases list empty — no disease links found
- [ ] ^TMPRSS3.md — key_papers empty — no paper references found
- [ ] ^TNFRSF1A.md — diseases list empty — no disease links found
- [ ] ^TNFRSF1A.md — key_papers empty — no paper references found
- [ ] ^TRIOBP.md — diseases list empty — no disease links found
- [ ] ^TRIOBP.md — key_papers empty — no paper references found
- [ ] ^TRPM8.md — key_papers empty — no paper references found
- [ ] ^TRPV4.md — diseases list empty — no disease links found
- [ ] ^TRPV4.md — key_papers empty — no paper references found
- [ ] ^TSHR.md — diseases list empty — no disease links found
- [ ] ^TSHR.md — key_papers empty — no paper references found
- [ ] ^TYK2.md — diseases list empty — no disease links found
- [ ] ^TYK2.md — key_papers empty — no paper references found
- [ ] ^TYROBP.md — diseases list empty — no disease links found
- [ ] ^TYROBP.md — key_papers empty — no paper references found
- [ ] ^UBE3A.md — key_papers empty — no paper references found
- [ ] ^UBQLN2.md — diseases list empty — no disease links found
- [ ] ^UBQLN2.md — key_papers empty — no paper references found
- [ ] ^UNC13A.md — key_papers empty — no paper references found
- [ ] ^USP30.md — diseases list empty — no disease links found
- [ ] ^USP30.md — key_papers empty — no paper references found
- [ ] ^Usp18.md — diseases list empty — no disease links found
- [ ] ^Usp18.md — key_papers empty — no paper references found
- [ ] ^VEGFA.md — diseases list empty — no disease links found
- [ ] ^VEGFA.md — key_papers empty — no paper references found
- [ ] ^WFS1.md — diseases list empty — no disease links found
- [ ] ^WFS1.md — key_papers empty — no paper references found