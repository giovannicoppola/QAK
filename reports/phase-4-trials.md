# Phase 4: Clinical Trial Notes — Migration Report

- **Date:** 2026-04-16 12:57
- **Notes scanned:** 87
- **Notes modified (trials):** 38
- **Notes skipped (not a trial):** 11
- **Infrastructure/meta notes excluded:** 38
- **Errors:** 0

## Summary

Added `type: clinical_trial` YAML frontmatter to trial notes. Parsed bullet-point template 
fields (sampleSize, drug, phase, clinicalTrialsURL, etc.) into YAML properties. Extracted 
NCT IDs from URLs, normalized phase names, inferred outcome from emoji suffixes, and mapped 
indications to canonical disease names. All original body text preserved.

## Changes by Note

| Note | Status | Changes | Warnings |
|------|--------|---------|----------|
| AHEAD 3-45 study.md | modified | +type: clinical_trial; +diseases: ["Alzheimer's Disease", 'ALS', 'Multiple Sclerosis'] | phase not found; drug not found; n_enrolled not found |
| ATLAS trial ➡️.md | modified | +type: clinical_trial; +nct_id: NCT04856982; +phase: Phase 3; +drug: tofersen; +n_enrolled: 150; +outcome: pending; +diseases: ['ALS', 'Progressive Supranuclear Palsy (PSP)'] | — |
| BIIB076†.md | modified | +type: clinical_trial; +phase: * status:discontinued (2022-07); +outcome: negative; +diseases: ["Alzheimer's Disease", 'ALS'] | drug not found; n_enrolled not found |
| CANDELA trial.md | modified | +type: clinical_trial; +diseases: ["Alzheimer's Disease", 'AMD'] | phase not found; drug not found; n_enrolled not found |
| CENTAUR study.md | skipped | — | Not identified as a clinical trial note |
| CLARITY study.md | modified | +type: clinical_trial; +drug: lecanemab✅; +n_enrolled: 1795 | phase not found; diseases empty |
| DIAN-TU study.md | skipped | — | Not identified as a clinical trial note |
| EMERGE study ✅.md | modified | +type: clinical_trial; +nct_id: NCT02484547; +phase: Phase 3; +drug: aducanumab✅; +n_enrolled: 1638; +outcome: positive; +diseases: ["Alzheimer's Disease", 'ALS', 'Progressive Supranuclear Palsy (PSP)', 'Multiple Sclerosis'] | — |
| EMERGENT-2 trial.md | modified | +type: clinical_trial; +phase: * clinicalTrials:; +drug: KarXT (xanomeline); +n_enrolled: 252; +diseases: ['ALS'] | — |
| ENGAGE study†.md | modified | +type: clinical_trial; +drug: aducanumab✅; +n_enrolled: 1350; +outcome: negative; +diseases: ["Alzheimer's Disease", 'Progressive Supranuclear Palsy (PSP)', 'Multiple Sclerosis'] | phase not found |
| FOCUS C9 study.md | skipped | — | Not identified as a clinical trial note |
| GENERATION HD1.md | modified | +type: clinical_trial; +drug: tominersen†; +n_enrolled: 909 | phase not found; diseases empty |
| GRADUATE 1 Study.md | modified | +type: clinical_trial; +diseases: ["Alzheimer's Disease", 'ALS', "Parkinson's Disease"] | phase not found; drug not found; n_enrolled not found |
| GRADUATE 2 Study.md | skipped | — | Not identified as a clinical trial note |
| INFRONT-3 trial.md | modified | +type: clinical_trial; +nct_id: NCT04374136; +phase: Phase 3; +drug: AL001 (latozinemab); +n_enrolled: 110; +diseases: ["Alzheimer's Disease", 'ALS'] | — |
| Johns Hopkins University (JHU) Biomarkers for Older Controls  at Risk for Dementia (BIOCARD) Study.md | skipped | — | Not identified as a clinical trial note |
| LAURIET trial.md | modified | +type: clinical_trial; +nct_id: NCT03828747; +phase: Phase 2; +drug: semorinemab; +n_enrolled: 272; +diseases: ["Alzheimer's Disease"] | — |
| LU AF82422.md | modified | +type: clinical_trial; +diseases: ["Alzheimer's Disease", 'ALS', "Huntington's Disease (HD)", "Parkinson's Disease", 'Multiple Sclerosis'] | phase not found; drug not found; n_enrolled not found |
| LUCERNE trial.md | modified | +type: clinical_trial; +phase: * clinicalTrials:; +drug: faricimab; +n_enrolled: 671; +diseases: ['ALS'] | — |
| MEDI1341.md | modified | +type: clinical_trial; +diseases: ["Alzheimer's Disease", 'ALS', "Parkinson's Disease", 'Multiple Sclerosis'] | phase not found; drug not found; n_enrolled not found |
| Marguerite RoAD study.md | modified | +type: clinical_trial; +diseases: ["Alzheimer's Disease", 'ALS', "Parkinson's Disease"] | phase not found; drug not found; n_enrolled not found |
| NOTOXI trial.md | skipped | — | Not identified as a clinical trial note |
| PADOVA study.md | skipped | — | Not identified as a clinical trial note |
| PASADENA study.md | skipped | — | Not identified as a clinical trial note |
| PASSPORT trial ❌.md | modified | +type: clinical_trial; +nct_id: NCT03068468; +phase: Phase 2; +drug: gosuranemab†; +n_enrolled: 490; +outcome: negative; +diseases: ['ALS', 'Progressive Supranuclear Palsy (PSP)'] | — |
| PHOTON trial.md | modified | +type: clinical_trial; +diseases: ["Alzheimer's Disease", 'ALS'] | phase not found; drug not found; n_enrolled not found |
| PIVOT-HD trial.md | modified | +type: clinical_trial; +phase: Phase 2; +drug: PTC518 | diseases empty; n_enrolled not found |
| PROCLAIM phase1-2 trial.md | modified | +type: clinical_trial; +diseases: ['Frontotemporal Dementia'] | phase not found; drug not found; n_enrolled not found |
| PULSAR trial.md | modified | +type: clinical_trial | phase not found; drug not found; diseases empty; n_enrolled not found |
| SCarlet RoAD study.md | modified | +type: clinical_trial; +diseases: ["Alzheimer's Disease", 'ALS', 'Multiple Sclerosis'] | phase not found; drug not found; n_enrolled not found |
| SIENNA phase 3 clinical trial.md | modified | +type: clinical_trial; +diseases: ["Alzheimer's Disease", 'ALS', "Parkinson's Disease"] | phase not found; drug not found; n_enrolled not found |
| SIENNA trial.md | modified | +type: clinical_trial; +n_enrolled: 750; +diseases: ["Alzheimer's Disease", 'ALS', 'AMD'] | phase not found; drug not found |
| STELLAR trial.md | modified | +type: clinical_trial; +phase: Phase 3; +drug: sotatercept; +n_enrolled: 320; +diseases: ['ALS'] | — |
| TANGO trial ❌.md | modified | +type: clinical_trial; +nct_id: NCT03352557; +phase: Phase 2; +drug: gosuranemab†; +n_enrolled: 654; +outcome: negative; +diseases: ["Alzheimer's Disease"] | — |
| TAURIEL trial ❌.md | modified | +type: clinical_trial; +nct_id: NCT03289143; +phase: Phase 2; +drug: semorinemab; +n_enrolled: 457; +outcome: negative; +diseases: ["Alzheimer's Disease"] | — |
| TENAYA trial.md | modified | +type: clinical_trial; +phase: * clinicalTrials:; +drug: faricimab; +n_enrolled: 671; +diseases: ['ALS'] | — |
| TRAILBLAZER-ALZ study.md | modified | +type: clinical_trial; +phase: * clinicalTrialsURL:; +drug: donanemab✅️; +diseases: ["Alzheimer's Disease", 'ALS', 'Multiple Sclerosis'] | n_enrolled not found |
| TRAILBLAZER-ALZ2 study.md | skipped | — | Not identified as a clinical trial note |
| Transposon Therapeutics.md | modified | +type: clinical_trial; +nct_id: NCT05613868; +diseases: ["Alzheimer's Disease", 'ALS'] | phase not found; drug not found; n_enrolled not found |
| UCB0107.md | modified | +type: clinical_trial; +phase: * status:; +diseases: ['ALS'] | drug not found; n_enrolled not found |
| VALOR trial ❌.md | modified | +type: clinical_trial; +nct_id: NCT02623699; +phase: Phase 3; +drug: tofersen; +n_enrolled: 108; +outcome: negative; +diseases: ["Alzheimer's Disease", 'ALS', "Parkinson's Disease"] | — |
| WU  Healthy  Aging  and  Senile  Dementia  (HASD)  study.md | skipped | — | Not identified as a clinical trial note |
| Washington  University  (WU)  Adult  Children  Study  (ACS).md | skipped | — | Not identified as a clinical trial note |
| donanemab✅️.md | modified | +type: clinical_trial; +phase: Phase 3; +outcome: positive; +diseases: ["Alzheimer's Disease"] | drug not found; n_enrolled not found |
| gosuranemab†.md | modified | +type: clinical_trial; +phase: Phase 2; +outcome: negative; +diseases: ["Alzheimer's Disease", 'ALS', 'Progressive Supranuclear Palsy (PSP)'] | drug not found; n_enrolled not found |
| latozinemab.md | modified | +type: clinical_trial; +diseases: ['ALS'] | phase not found; drug not found; n_enrolled not found |
| prasinezumab.md | modified | +type: clinical_trial; +diseases: ["Alzheimer's Disease", 'ALS', "Parkinson's Disease", 'Multiple Sclerosis'] | phase not found; drug not found; n_enrolled not found |
| semorinemab.md | modified | +type: clinical_trial; +phase: Phase 2; +diseases: ["Alzheimer's Disease"] | drug not found; n_enrolled not found |
| solanezumab (†).md | modified | +type: clinical_trial; +outcome: negative; +diseases: ["Alzheimer's Disease", 'ALS', 'diabetic retinopathy', "Parkinson's Disease", 'Multiple Sclerosis'] | phase not found; drug not found; n_enrolled not found |

## Excluded Infrastructure Notes

- 3C study.md
- APT webstudy and Trial Ready Cohort TRC-PAD.md
- Aducanumab clinical trials – Nov 2020.md
- Aducanumab clinical trials.md
- Anti-Amyloid Treatment in Asymptomatic Alzheimer disease (A4) Study.md
- Australian Imaging, Biomarkers and Lifestyle (AIBL) study.md
- Beaver Dam Eye Study.md
- BioFINDER study.md
- COMPASS-ND Study.md
- Cache County Study.md
- ClinicalTrials Alfred workflow.md
- EPIC-Norfolk study.md
- FINGER study.md
- Framingham Heart Study.md
- Genetic Links To Anxiety and Depression (GLAD) Study.md
- Imaging Dementia-Evidence for Amyloid Scanning (IDEAS) study.md
- Japanese Trial-Ready Cohort (J-TRC).md
- LIFE-Adult-Study.md
- Mayo Clinic Study of Aging.md
- Memento study.md
- Prospective Imaging Study of Ageing Genes, Brain and Behaviour (PISA).md
- Rotterdam Study.md
- Trial-Ready Cohort for Down Syndrome (TRC-DS).md
- TrialMatch.md
- Whitehall II Study.md
- clinical trials.md
- clinicalTrials.md
- clinicalTrialsURL.md
- comparing aducanumab and lecanemab trials.md
- ongoing clinical trials in preclinical AD.md
- preclinical AD trial-ready cohorts.md
- queries – aducanumab trials.md
- queries – clinical trials.md
- recent schizophrenia trials (2023).md
- templates – clinical trials.md
- tofersen – clinical trials.md
- trialDuration.md
- trialOutcome.md