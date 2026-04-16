# Phase 1: Disease Notes — Migration Report

- **Date:** 2026-04-16 12:38
- **Notes processed:** 58
- **Notes modified:** 57
- **Notes skipped:** 1
- **Errors:** 0

## Summary

Added `type: disease` YAML frontmatter to disease notes. Extracted epidemiological stats 
(prevalence, incidence, US cases), genetics summary (GWAS/WES size, loci, paper citekeys), 
and gene lists from body text into YAML properties. All original body text preserved.

## Changes by Note

| Note | Status | Changes | Warnings |
|------|--------|---------|----------|
| 15q duplication (dup15q).md | modified | +type: disease; +tags: disease | n_patients_us left empty — not found in body; gwas_largest_n left empty; genes list empty — no ^GENE links found in body |
| ALS.md | modified | +gwas_largest_n: 27000; +gwas_loci: 12; +gwas_paper: Van_Rheenen2021-eh; +wes_largest_n: 3800; +wes_loci: 2; +genes: ['NEK1', 'DNAJC7', 'SOD1', 'TARDBP'] | — |
| AMD.md | modified | +type: disease; +tags: disease; +gwas_loci: 60; +gwas_paper: Gorman2022-vi | n_patients_us left empty — not found in body; gwas_largest_n left empty; genes list empty — no ^GENE links found in body |
| Alzheimer's Disease.md | modified | +type: disease; +tags: disease; +gwas_largest_n: 90000; +gwas_loci: 38; +gwas_paper: Wightman2021-je; +wes_largest_n: 16000; +wes_loci: 3; +genes: ['TREM2', 'SORL1', 'ABCA7', 'ATP8B4', 'ABCA1'] | n_patients_us left empty — not found in body |
| Alzheimers Disease Early Onset–EOAD.md | modified | +type: disease; +tags: disease; +genes: ['PSEN1', 'APP'] | n_patients_us left empty — not found in body; gwas_largest_n left empty |
| Angelman Syndrome.md | modified | +type: disease; +tags: disease; +genes: ['UBE3A'] | n_patients_us left empty — not found in body; gwas_largest_n left empty |
| Ankylosing Spondylitis.md | modified | +type: disease; +tags: disease | n_patients_us left empty — not found in body; gwas_largest_n left empty; genes list empty — no ^GENE links found in body |
| Birdshot.md | modified | +type: disease; +tags: disease | n_patients_us left empty — not found in body; gwas_largest_n left empty; genes list empty — no ^GENE links found in body |
| CADASIL.md | modified | +type: disease; +tags: disease; +genes: ['NOTCH3'] | n_patients_us left empty — not found in body; gwas_largest_n left empty |
| Central Serous Chorioretinopathy (CSCR).md | modified | +type: disease; +tags: disease | n_patients_us left empty — not found in body; gwas_largest_n left empty; genes list empty — no ^GENE links found in body |
| Duchenne Dystrophy.md | modified | +type: disease; +tags: disease | n_patients_us left empty — not found in body; gwas_largest_n left empty; genes list empty — no ^GENE links found in body |
| Friedreich's Ataxia.md | modified | +type: disease; +tags: disease | n_patients_us left empty — not found in body; gwas_largest_n left empty; genes list empty — no ^GENE links found in body |
| Frontotemporal Dementia.md | modified | +type: disease; +tags: disease | n_patients_us left empty — not found in body; gwas_largest_n left empty; genes list empty — no ^GENE links found in body |
| Fuchs endothelial corneal dystrophy (FECD).md | modified | +type: disease; +tags: disease; +genes: ['TCF4'] | n_patients_us left empty — not found in body; gwas_largest_n left empty |
| Giant Cell Arteritis.md | modified | +type: disease; +tags: disease | n_patients_us left empty — not found in body; gwas_largest_n left empty; genes list empty — no ^GENE links found in body |
| Glaucoma.md | modified | +type: disease; +tags: disease; +gwas_largest_n: 34000; +gwas_loci: 127; +gwas_paper: Han2023-ks | n_patients_us left empty — not found in body; genes list empty — no ^GENE links found in body |
| Hearing loss.md | skipped | — | File not found: Hearing loss.md |
| Huntington's Disease (HD).md | modified | +type: disease | n_patients_us left empty — not found in body; gwas_largest_n left empty; genes list empty — no ^GENE links found in body |
| Juvenile Open-Angle Glaucoma.md | modified | +type: disease; +tags: disease; +genes: ['MYOC'] | n_patients_us left empty — not found in body; gwas_largest_n left empty |
| Juvenile X-linked Retinoschisis (XLRS).md | modified | +type: disease; +tags: disease; +genes: ['RS1'] | n_patients_us left empty — not found in body; gwas_largest_n left empty |
| Lewy Body Dementia.md | modified | +type: disease; +tags: disease | n_patients_us left empty — not found in body; gwas_largest_n left empty; genes list empty — no ^GENE links found in body |
| MCI.md | modified | +type: disease; +tags: disease; +genes: ['APOE'] | n_patients_us left empty — not found in body; gwas_largest_n left empty |
| Migraine.md | modified | +type: disease; +tags: disease; +gwas_largest_n: 102000; +gwas_loci: 123; +gwas_paper: Hautakangas2022-dg | n_patients_us left empty — not found in body; genes list empty — no ^GENE links found in body |
| Multiple Sclerosis.md | modified | +type: disease; +tags: disease; +gwas_largest_n: 47000; +gwas_loci: 156; +gwas_paper: International_Multiple_Sclerosis_Genetics_Consortium2019-cg; +wes_largest_n: 32000; +wes_loci: 4; +genes: ['HDAC7', 'PRF1', 'NLRP8', 'PRKRA'] | n_patients_us left empty — not found in body |
| Multiple System Atrophy.md | modified | +type: disease; +tags: disease | n_patients_us left empty — not found in body; gwas_largest_n left empty; genes list empty — no ^GENE links found in body |
| Neuromyelitis Optica.md | modified | +type: disease; +tags: disease; +genes: ['AQP4'] | n_patients_us left empty — not found in body; gwas_largest_n left empty |
| Parkinsonian-pyramidal syndrome.md | modified | +type: disease; +tags: disease; +genes: ['FBXO7', 'SNCA'] | n_patients_us left empty — not found in body; gwas_largest_n left empty |
| Paroxysmal Nocturnal Hemoglobinuria (PNH).md | modified | +type: disease; +tags: disease | n_patients_us left empty — not found in body; gwas_largest_n left empty; genes list empty — no ^GENE links found in body |
| Pendred syndrome.md | modified | +type: disease; +tags: disease; +genes: ['SLC26A4', 'FOXI1', 'KCNJ10'] | n_patients_us left empty — not found in body; gwas_largest_n left empty |
| Progressive Multifocal Leukoencephalopathy.md | modified | +type: disease; +tags: disease | n_patients_us left empty — not found in body; gwas_largest_n left empty; genes list empty — no ^GENE links found in body |
| Progressive Supranuclear Palsy (PSP).md | modified | +type: disease; +tags: disease | n_patients_us left empty — not found in body; gwas_largest_n left empty; genes list empty — no ^GENE links found in body |
| Psoriasis.md | modified | +type: disease; +tags: disease | n_patients_us left empty — not found in body; gwas_largest_n left empty; genes list empty — no ^GENE links found in body |
| Pulmonary Arterial Hypertension (PAH).md | modified | +type: disease; +tags: disease | n_patients_us left empty — not found in body; gwas_largest_n left empty; genes list empty — no ^GENE links found in body |
| Retinitis Pigmentosa.md | modified | +type: disease; +tags: disease | n_patients_us left empty — not found in body; gwas_largest_n left empty; genes list empty — no ^GENE links found in body |
| Rheumatoid Arthritis.md | modified | +type: disease; +tags: disease | n_patients_us left empty — not found in body; gwas_largest_n left empty; genes list empty — no ^GENE links found in body |
| SCA1.md | modified | +type: disease; +tags: disease | n_patients_us left empty — not found in body; gwas_largest_n left empty; genes list empty — no ^GENE links found in body |
| SCA3.md | modified | +type: disease; +tags: disease | n_patients_us left empty — not found in body; gwas_largest_n left empty; genes list empty — no ^GENE links found in body |
| Schizophrenia.md | modified | +type: disease; +tags: disease; +gwas_largest_n: 74000; +gwas_loci: 287; +gwas_paper: Trubetskoy2022-hx; +wes_largest_n: 24000; +wes_loci: 10 | n_patients_us left empty — not found in body; genes list empty — no ^GENE links found in body |
| Stargardt Disease.md | modified | +type: disease; +tags: disease | n_patients_us left empty — not found in body; gwas_largest_n left empty; genes list empty — no ^GENE links found in body |
| Subjective Cognitive Decline.md | modified | +type: disease; +tags: disease | n_patients_us left empty — not found in body; gwas_largest_n left empty; genes list empty — no ^GENE links found in body |
| Type III hyperlipoproteinemia.md | modified | +type: disease; +tags: disease; +genes: ['APOE'] | n_patients_us left empty — not found in body; gwas_largest_n left empty |
| Wilson's disease.md | modified | +type: disease; +tags: disease; +genes: ['ATP7B'] | n_patients_us left empty — not found in body; gwas_largest_n left empty |
| alcohol use disorder.md | modified | +type: disease; +tags: disease; +genes: ['ALDH2', 'ADH1B'] | n_patients_us left empty — not found in body; gwas_largest_n left empty |
| autism spectrum disorder.md | modified | +type: disease; +tags: disease; +gwas_loci: 5; +gwas_paper: Grove2019-aq; +wes_largest_n: 20000 | n_patients_us left empty — not found in body; gwas_largest_n left empty; genes list empty — no ^GENE links found in body |
| bipolar disorder.md | modified | +type: disease; +tags: disease; +gwas_largest_n: 42000; +gwas_loci: 64; +gwas_paper: Mullins2021-ik; +wes_largest_n: 14000; +wes_loci: 1; +genes: ['AKAP11'] | n_patients_us left empty — not found in body |
| chronic pain.md | modified | +type: disease; +tags: disease | n_patients_us left empty — not found in body; gwas_largest_n left empty; genes list empty — no ^GENE links found in body |
| depression.md | modified | +type: disease; +tags: disease; +gwas_largest_n: 340000; +gwas_loci: 178; +gwas_paper: Levey2021-dm; +wes_largest_n: 10000; +wes_loci: 1; +genes: ['SLC2A1'] | n_patients_us left empty — not found in body |
| diabetic neuropathy.md | modified | +type: disease; +tags: disease | n_patients_us left empty — not found in body; gwas_largest_n left empty; genes list empty — no ^GENE links found in body |
| diabetic retinopathy.md | modified | +type: disease; +tags: disease | n_patients_us left empty — not found in body; gwas_largest_n left empty; genes list empty — no ^GENE links found in body |
| eating disorders.md | modified | +type: disease; +tags: disease; +gwas_largest_n: 17000; +gwas_loci: 8; +gwas_paper: Watson2019-oc; +wes_largest_n: 2000 | n_patients_us left empty — not found in body; genes list empty — no ^GENE links found in body |
| hereditary transthyretin amyloidosis (ATTR).md | modified | +type: disease; +tags: disease | n_patients_us left empty — not found in body; gwas_largest_n left empty; genes list empty — no ^GENE links found in body |
| idiopathic epilepsy.md | modified | +type: disease; +tags: disease; +gwas_largest_n: 15000; +gwas_loci: 16; +gwas_paper: International_League_Against_Epilepsy_Consortium_on_Complex_Epilepsies2018-us; +wes_largest_n: 9000 | n_patients_us left empty — not found in body; genes list empty — no ^GENE links found in body |
| idiopathic intracranial hypertension.md | modified | +type: disease; +tags: disease | n_patients_us left empty — not found in body; gwas_largest_n left empty; genes list empty — no ^GENE links found in body |
| keratoconus.md | modified | +type: disease; +tags: disease | n_patients_us left empty — not found in body; gwas_largest_n left empty; genes list empty — no ^GENE links found in body |
| myopia.md | modified | +type: disease; +tags: disease | n_patients_us left empty — not found in body; gwas_largest_n left empty; genes list empty — no ^GENE links found in body |
| normal pressure hydrocephalus.md | modified | +type: disease; +tags: disease | n_patients_us left empty — not found in body; gwas_largest_n left empty; genes list empty — no ^GENE links found in body |
| stroke.md | modified | +type: disease; +tags: disease; +gwas_largest_n: 110000; +gwas_loci: 89; +gwas_paper: Debette2022-kd; +wes_largest_n: 15000; +wes_loci: 1 | n_patients_us left empty — not found in body; genes list empty — no ^GENE links found in body |
| uveitis.md | modified | +type: disease; +tags: disease | n_patients_us left empty — not found in body; gwas_largest_n left empty; genes list empty — no ^GENE links found in body |

## Items Requiring Manual Review

- [ ] 15q duplication (dup15q).md — n_patients_us left empty — not found in body
- [ ] 15q duplication (dup15q).md — gwas_largest_n left empty
- [ ] 15q duplication (dup15q).md — genes list empty — no ^GENE links found in body
- [ ] AMD.md — n_patients_us left empty — not found in body
- [ ] AMD.md — gwas_largest_n left empty
- [ ] AMD.md — genes list empty — no ^GENE links found in body
- [ ] Alzheimer's Disease.md — n_patients_us left empty — not found in body
- [ ] Alzheimers Disease Early Onset–EOAD.md — n_patients_us left empty — not found in body
- [ ] Alzheimers Disease Early Onset–EOAD.md — gwas_largest_n left empty
- [ ] Angelman Syndrome.md — n_patients_us left empty — not found in body
- [ ] Angelman Syndrome.md — gwas_largest_n left empty
- [ ] Ankylosing Spondylitis.md — n_patients_us left empty — not found in body
- [ ] Ankylosing Spondylitis.md — gwas_largest_n left empty
- [ ] Ankylosing Spondylitis.md — genes list empty — no ^GENE links found in body
- [ ] Birdshot.md — n_patients_us left empty — not found in body
- [ ] Birdshot.md — gwas_largest_n left empty
- [ ] Birdshot.md — genes list empty — no ^GENE links found in body
- [ ] CADASIL.md — n_patients_us left empty — not found in body
- [ ] CADASIL.md — gwas_largest_n left empty
- [ ] Central Serous Chorioretinopathy (CSCR).md — n_patients_us left empty — not found in body
- [ ] Central Serous Chorioretinopathy (CSCR).md — gwas_largest_n left empty
- [ ] Central Serous Chorioretinopathy (CSCR).md — genes list empty — no ^GENE links found in body
- [ ] Duchenne Dystrophy.md — n_patients_us left empty — not found in body
- [ ] Duchenne Dystrophy.md — gwas_largest_n left empty
- [ ] Duchenne Dystrophy.md — genes list empty — no ^GENE links found in body
- [ ] Friedreich's Ataxia.md — n_patients_us left empty — not found in body
- [ ] Friedreich's Ataxia.md — gwas_largest_n left empty
- [ ] Friedreich's Ataxia.md — genes list empty — no ^GENE links found in body
- [ ] Frontotemporal Dementia.md — n_patients_us left empty — not found in body
- [ ] Frontotemporal Dementia.md — gwas_largest_n left empty
- [ ] Frontotemporal Dementia.md — genes list empty — no ^GENE links found in body
- [ ] Fuchs endothelial corneal dystrophy (FECD).md — n_patients_us left empty — not found in body
- [ ] Fuchs endothelial corneal dystrophy (FECD).md — gwas_largest_n left empty
- [ ] Giant Cell Arteritis.md — n_patients_us left empty — not found in body
- [ ] Giant Cell Arteritis.md — gwas_largest_n left empty
- [ ] Giant Cell Arteritis.md — genes list empty — no ^GENE links found in body
- [ ] Glaucoma.md — n_patients_us left empty — not found in body
- [ ] Glaucoma.md — genes list empty — no ^GENE links found in body
- [ ] Huntington's Disease (HD).md — n_patients_us left empty — not found in body
- [ ] Huntington's Disease (HD).md — gwas_largest_n left empty
- [ ] Huntington's Disease (HD).md — genes list empty — no ^GENE links found in body
- [ ] Juvenile Open-Angle Glaucoma.md — n_patients_us left empty — not found in body
- [ ] Juvenile Open-Angle Glaucoma.md — gwas_largest_n left empty
- [ ] Juvenile X-linked Retinoschisis (XLRS).md — n_patients_us left empty — not found in body
- [ ] Juvenile X-linked Retinoschisis (XLRS).md — gwas_largest_n left empty
- [ ] Lewy Body Dementia.md — n_patients_us left empty — not found in body
- [ ] Lewy Body Dementia.md — gwas_largest_n left empty
- [ ] Lewy Body Dementia.md — genes list empty — no ^GENE links found in body
- [ ] MCI.md — n_patients_us left empty — not found in body
- [ ] MCI.md — gwas_largest_n left empty
- [ ] Migraine.md — n_patients_us left empty — not found in body
- [ ] Migraine.md — genes list empty — no ^GENE links found in body
- [ ] Multiple Sclerosis.md — n_patients_us left empty — not found in body
- [ ] Multiple System Atrophy.md — n_patients_us left empty — not found in body
- [ ] Multiple System Atrophy.md — gwas_largest_n left empty
- [ ] Multiple System Atrophy.md — genes list empty — no ^GENE links found in body
- [ ] Neuromyelitis Optica.md — n_patients_us left empty — not found in body
- [ ] Neuromyelitis Optica.md — gwas_largest_n left empty
- [ ] Parkinsonian-pyramidal syndrome.md — n_patients_us left empty — not found in body
- [ ] Parkinsonian-pyramidal syndrome.md — gwas_largest_n left empty
- [ ] Paroxysmal Nocturnal Hemoglobinuria (PNH).md — n_patients_us left empty — not found in body
- [ ] Paroxysmal Nocturnal Hemoglobinuria (PNH).md — gwas_largest_n left empty
- [ ] Paroxysmal Nocturnal Hemoglobinuria (PNH).md — genes list empty — no ^GENE links found in body
- [ ] Pendred syndrome.md — n_patients_us left empty — not found in body
- [ ] Pendred syndrome.md — gwas_largest_n left empty
- [ ] Progressive Multifocal Leukoencephalopathy.md — n_patients_us left empty — not found in body
- [ ] Progressive Multifocal Leukoencephalopathy.md — gwas_largest_n left empty
- [ ] Progressive Multifocal Leukoencephalopathy.md — genes list empty — no ^GENE links found in body
- [ ] Progressive Supranuclear Palsy (PSP).md — n_patients_us left empty — not found in body
- [ ] Progressive Supranuclear Palsy (PSP).md — gwas_largest_n left empty
- [ ] Progressive Supranuclear Palsy (PSP).md — genes list empty — no ^GENE links found in body
- [ ] Psoriasis.md — n_patients_us left empty — not found in body
- [ ] Psoriasis.md — gwas_largest_n left empty
- [ ] Psoriasis.md — genes list empty — no ^GENE links found in body
- [ ] Pulmonary Arterial Hypertension (PAH).md — n_patients_us left empty — not found in body
- [ ] Pulmonary Arterial Hypertension (PAH).md — gwas_largest_n left empty
- [ ] Pulmonary Arterial Hypertension (PAH).md — genes list empty — no ^GENE links found in body
- [ ] Retinitis Pigmentosa.md — n_patients_us left empty — not found in body
- [ ] Retinitis Pigmentosa.md — gwas_largest_n left empty
- [ ] Retinitis Pigmentosa.md — genes list empty — no ^GENE links found in body
- [ ] Rheumatoid Arthritis.md — n_patients_us left empty — not found in body
- [ ] Rheumatoid Arthritis.md — gwas_largest_n left empty
- [ ] Rheumatoid Arthritis.md — genes list empty — no ^GENE links found in body
- [ ] SCA1.md — n_patients_us left empty — not found in body
- [ ] SCA1.md — gwas_largest_n left empty
- [ ] SCA1.md — genes list empty — no ^GENE links found in body
- [ ] SCA3.md — n_patients_us left empty — not found in body
- [ ] SCA3.md — gwas_largest_n left empty
- [ ] SCA3.md — genes list empty — no ^GENE links found in body
- [ ] Schizophrenia.md — n_patients_us left empty — not found in body
- [ ] Schizophrenia.md — genes list empty — no ^GENE links found in body
- [ ] Stargardt Disease.md — n_patients_us left empty — not found in body
- [ ] Stargardt Disease.md — gwas_largest_n left empty
- [ ] Stargardt Disease.md — genes list empty — no ^GENE links found in body
- [ ] Subjective Cognitive Decline.md — n_patients_us left empty — not found in body
- [ ] Subjective Cognitive Decline.md — gwas_largest_n left empty
- [ ] Subjective Cognitive Decline.md — genes list empty — no ^GENE links found in body
- [ ] Type III hyperlipoproteinemia.md — n_patients_us left empty — not found in body
- [ ] Type III hyperlipoproteinemia.md — gwas_largest_n left empty
- [ ] Wilson's disease.md — n_patients_us left empty — not found in body
- [ ] Wilson's disease.md — gwas_largest_n left empty
- [ ] alcohol use disorder.md — n_patients_us left empty — not found in body
- [ ] alcohol use disorder.md — gwas_largest_n left empty
- [ ] autism spectrum disorder.md — n_patients_us left empty — not found in body
- [ ] autism spectrum disorder.md — gwas_largest_n left empty
- [ ] autism spectrum disorder.md — genes list empty — no ^GENE links found in body
- [ ] bipolar disorder.md — n_patients_us left empty — not found in body
- [ ] chronic pain.md — n_patients_us left empty — not found in body
- [ ] chronic pain.md — gwas_largest_n left empty
- [ ] chronic pain.md — genes list empty — no ^GENE links found in body
- [ ] depression.md — n_patients_us left empty — not found in body
- [ ] diabetic neuropathy.md — n_patients_us left empty — not found in body
- [ ] diabetic neuropathy.md — gwas_largest_n left empty
- [ ] diabetic neuropathy.md — genes list empty — no ^GENE links found in body
- [ ] diabetic retinopathy.md — n_patients_us left empty — not found in body
- [ ] diabetic retinopathy.md — gwas_largest_n left empty
- [ ] diabetic retinopathy.md — genes list empty — no ^GENE links found in body
- [ ] eating disorders.md — n_patients_us left empty — not found in body
- [ ] eating disorders.md — genes list empty — no ^GENE links found in body
- [ ] hereditary transthyretin amyloidosis (ATTR).md — n_patients_us left empty — not found in body
- [ ] hereditary transthyretin amyloidosis (ATTR).md — gwas_largest_n left empty
- [ ] hereditary transthyretin amyloidosis (ATTR).md — genes list empty — no ^GENE links found in body
- [ ] idiopathic epilepsy.md — n_patients_us left empty — not found in body
- [ ] idiopathic epilepsy.md — genes list empty — no ^GENE links found in body
- [ ] idiopathic intracranial hypertension.md — n_patients_us left empty — not found in body
- [ ] idiopathic intracranial hypertension.md — gwas_largest_n left empty
- [ ] idiopathic intracranial hypertension.md — genes list empty — no ^GENE links found in body
- [ ] keratoconus.md — n_patients_us left empty — not found in body
- [ ] keratoconus.md — gwas_largest_n left empty
- [ ] keratoconus.md — genes list empty — no ^GENE links found in body
- [ ] myopia.md — n_patients_us left empty — not found in body
- [ ] myopia.md — gwas_largest_n left empty
- [ ] myopia.md — genes list empty — no ^GENE links found in body
- [ ] normal pressure hydrocephalus.md — n_patients_us left empty — not found in body
- [ ] normal pressure hydrocephalus.md — gwas_largest_n left empty
- [ ] normal pressure hydrocephalus.md — genes list empty — no ^GENE links found in body
- [ ] stroke.md — n_patients_us left empty — not found in body
- [ ] stroke.md — genes list empty — no ^GENE links found in body
- [ ] uveitis.md — n_patients_us left empty — not found in body
- [ ] uveitis.md — gwas_largest_n left empty
- [ ] uveitis.md — genes list empty — no ^GENE links found in body

## Skipped Notes

| Note | Reason |
|------|--------|
| Hearing loss.md | File not found: Hearing loss.md |