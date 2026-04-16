#!/usr/bin/env python3
"""
Phase 4: Clinical Trial Note Migration Script
Adds YAML frontmatter to clinical trial notes in the gitVault.
Identifies trials by: (1) template bullet fields (sampleSize:, clinicalTrialsURL:, etc.)
and (2) "trial" or "study" in filename with trial-like content.
No text is deleted — only YAML properties are added/updated.
"""

import re
from pathlib import Path
from datetime import datetime

VAULT = Path("/Users/giovanni.coppola/Library/CloudStorage/OneDrive-RegeneronPharmaceuticals,Inc/MyScripts/myGitHubRepos/gitVault/gitVault-notes")

# Known disease name mapping for indications
DISEASE_MAP = {
    "AD": "Alzheimer's Disease",
    "Alzheimer": "Alzheimer's Disease",
    "probable AD": "Alzheimer's Disease",
    "mild-to-moderate AD": "Alzheimer's Disease",
    "preclinical AD": "Alzheimer's Disease",
    "early AD": "Alzheimer's Disease",
    "ALS": "ALS",
    "SOD1-ALS": "ALS",
    "AMD": "AMD",
    "wet AMD": "AMD",
    "nAMD": "AMD",
    "DME": "diabetic retinopathy",
    "HD": "Huntington's Disease (HD)",
    "Huntington": "Huntington's Disease (HD)",
    "PD": "Parkinson's Disease",
    "Parkinson": "Parkinson's Disease",
    "FTD": "Frontotemporal Dementia",
    "PSP": "Progressive Supranuclear Palsy (PSP)",
    "MS": "Multiple Sclerosis",
    "multiple sclerosis": "Multiple Sclerosis",
    "schizophrenia": "Schizophrenia",
    "PNH": "Paroxysmal Nocturnal Hemoglobinuria (PNH)",
    "ATTR": "hereditary transthyretin amyloidosis (ATTR)",
    "glaucoma": "Glaucoma",
}

# Template bullet fields to extract
TEMPLATE_FIELDS = [
    "sampleSize", "drug", "dose", "trialDuration", "primaryEndpoint",
    "papers", "EstimatedCompletionDate", "status", "phase",
    "clinicalTrialsURL", "indications",
]

# Files to skip — these are infrastructure/template/meta notes, not actual trials
SKIP_FILES = {
    "templates – clinical trials.md",
    "clinical trials.md",
    "clinicalTrials.md",
    "clinicalTrialsURL.md",
    "trialDuration.md",
    "trialOutcome.md",
    "ClinicalTrials Alfred workflow.md",
    "queries – aducanumab trials.md",
    "queries – clinical trials.md",
    "comparing aducanumab and lecanemab trials.md",
    "ongoing clinical trials in preclinical AD.md",
    "preclinical AD trial-ready cohorts.md",
    "recent schizophrenia trials (2023).md",
    "phase.md",
    "phase I.md",
    "phase Ib.md",
    "phase II.md",
    "phase IIa.md",
    "phase III.md",
    "Phase IV.md",
}

# Observational studies / cohorts — NOT clinical trials, skip
COHORT_FILES = {
    "3C study.md",
    "Australian Imaging, Biomarkers and Lifestyle (AIBL) study.md",
    "Beaver Dam Eye Study.md",
    "BioFINDER study.md",
    "Cache County Study.md",
    "COMPASS-ND Study.md",
    "EPIC-Norfolk study.md",
    "FINGER study.md",
    "Framingham Heart Study.md",
    "Genetic Links To Anxiety and Depression (GLAD) Study.md",
    "Imaging Dementia-Evidence for Amyloid Scanning (IDEAS) study.md",
    "Japanese Trial-Ready Cohort (J-TRC).md",
    "Johns Hopkins University (JHU) Biomarkers for Older Controls at Risk for Dementia (BIOCARD) Study.md",
    "LIFE-Adult-Study.md",
    "Mayo Clinic Study of Aging.md",
    "Memento study.md",
    "Prospective Imaging Study of Ageing Genes, Brain and Behaviour (PISA).md",
    "Rotterdam Study.md",
    "Trial-Ready Cohort for Down Syndrome (TRC-DS).md",
    "TrialMatch.md",
    "Whitehall II Study.md",
    "Washington University (WU) Adult Children Study (ACS).md",
    "WU Healthy Aging and Senile Dementia (HASD) study.md",
    "APT webstudy and Trial Ready Cohort TRC-PAD.md",
    "Anti-Amyloid Treatment in Asymptomatic Alzheimer disease (A4) Study.md",
    "Aducanumab clinical trials – Nov 2020.md",
    "Aducanumab clinical trials.md",
    "tofersen – clinical trials.md",
}


def parse_existing_frontmatter(content):
    """Parse existing YAML frontmatter manually."""
    if not content.startswith("---"):
        return {}, content
    end = content.find("\n---", 3)
    if end == -1:
        return {}, content

    fm_text = content[4:end].strip()
    body = content[end + 4:]
    if body.startswith("\n"):
        body = body[1:]

    fm = {}
    current_key = None
    current_list = None

    for line in fm_text.split("\n"):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        if stripped.startswith("- ") and current_key:
            val = stripped[2:].strip()
            if current_list is not None:
                current_list.append(val)
            continue

        m = re.match(r'^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)', line)
        if m:
            if current_list is not None and current_key:
                fm[current_key] = current_list
            current_key = m.group(1)
            val = m.group(2).strip()
            if val == "" or val == "[]":
                current_list = []
            elif val.startswith("[") and val.endswith("]"):
                items = [x.strip().strip('"').strip("'") for x in val[1:-1].split(",") if x.strip()]
                fm[current_key] = items
                current_list = None
            else:
                val = val.strip('"').strip("'")
                try:
                    if "." in val:
                        fm[current_key] = float(val)
                    else:
                        fm[current_key] = int(val)
                except (ValueError, TypeError):
                    fm[current_key] = val
                current_list = None

    if current_list is not None and current_key:
        fm[current_key] = current_list

    return fm, body


def extract_bullet_field(body, field_name):
    """Extract value of a bullet-point template field like 'sampleSize:272'."""
    # Match: * field:value or * field: value (with optional wiki-link brackets)
    pattern = rf'^\s*\*\s*{re.escape(field_name)}\s*:\s*(.*)$'
    m = re.search(pattern, body, re.MULTILINE)
    if m:
        val = m.group(1).strip()
        if val:
            return val
    return ""


def strip_wikilinks(text):
    """Strip wiki-link brackets: [[text]] -> text, [[target|display]] -> display."""
    text = re.sub(r'\[\[([^\]|]+?)\|([^\]]+?)\]\]', r'\2', text)
    text = re.sub(r'\[\[([^\]]+?)\]\]', r'\1', text)
    return text.strip()


def extract_nct_id(url):
    """Extract NCT ID from clinicaltrials.gov URL."""
    m = re.search(r'(NCT\d{8,})', url)
    return m.group(1) if m else ""


def normalize_phase(phase_text):
    """Normalize phase text to standard format."""
    phase_text = strip_wikilinks(phase_text).strip()
    phase_map = {
        "phase I": "Phase 1",
        "phase 1": "Phase 1",
        "Phase 1": "Phase 1",
        "phase Ib": "Phase 1b",
        "phase 1b": "Phase 1b",
        "Phase 1b": "Phase 1b",
        "phase II": "Phase 2",
        "phase 2": "Phase 2",
        "Phase 2": "Phase 2",
        "phase IIa": "Phase 2a",
        "phase 2a": "Phase 2a",
        "phase IIb": "Phase 2b",
        "phase 2b": "Phase 2b",
        "phase III": "Phase 3",
        "phase 3": "Phase 3",
        "Phase 3": "Phase 3",
        "phase IV": "Phase 4",
        "phase 4": "Phase 4",
        "Phase 4": "Phase 4",
    }
    for k, v in phase_map.items():
        if phase_text.lower() == k.lower():
            return v
    return phase_text


def infer_outcome_from_filename(filename):
    """Infer trial outcome from emoji suffix in filename."""
    if "❌" in filename:
        return "negative"
    if "✅" in filename:
        return "positive"
    if "➡️" in filename:
        return "pending"
    if "†" in filename:
        return "negative"  # dagger typically means discontinued
    return ""


def extract_trial_name(filename):
    """Extract clean trial name from filename."""
    name = filename.replace(".md", "")
    # Remove emoji suffixes
    for emoji in ["❌", "✅", "➡️", "†", "✅️"]:
        name = name.replace(emoji, "")
    return name.strip()


def map_disease(indication_text, body):
    """Map indication text to canonical disease names."""
    diseases = []
    seen = set()

    # Check indication field
    if indication_text:
        text = strip_wikilinks(indication_text)
        for pattern, canonical in DISEASE_MAP.items():
            if pattern.lower() in text.lower() and canonical not in seen:
                seen.add(canonical)
                diseases.append(canonical)

    # Check body text for disease wiki-links
    wikilinks = re.findall(r'\[\[([^\]|#]+?)(?:\||\]\]|#)', body)
    for link in wikilinks:
        link = link.strip()
        for pattern, canonical in DISEASE_MAP.items():
            if link.lower() == pattern.lower() and canonical not in seen:
                seen.add(canonical)
                diseases.append(canonical)
                break

    # Infer from body text if still empty
    if not diseases:
        body_lower = body.lower()
        for pattern, canonical in DISEASE_MAP.items():
            if pattern.lower() in body_lower and canonical not in seen:
                seen.add(canonical)
                diseases.append(canonical)

    return diseases


def extract_genes_from_body(body):
    """Extract gene symbols from [[^GENE]] wiki-links."""
    genes = re.findall(r'\[\[\^([A-Za-z0-9_]+?)(?:\||\]\])', body)
    seen = set()
    result = []
    for g in genes:
        if g not in seen:
            seen.add(g)
            result.append(g)
    return result


def is_clinical_trial(filename, body):
    """Determine if a file is an actual clinical trial note."""
    if filename in SKIP_FILES or filename in COHORT_FILES:
        return False

    # Has template fields
    has_template = any(
        re.search(rf'^\s*\*\s*{re.escape(f)}\s*:', body, re.MULTILINE)
        for f in TEMPLATE_FIELDS
    )
    if has_template:
        return True

    # Has "trial" or "study" in name AND mentions phase/drug/endpoint
    name_lower = filename.lower()
    if "trial" in name_lower or "study" in name_lower:
        trial_markers = ["phase", "drug", "endpoint", "randomized", "placebo", "N=", "sampleSize"]
        if any(marker.lower() in body.lower() for marker in trial_markers):
            return True

    return False


def build_trial_yaml(existing_fm, body, filename):
    """Build the clinical trial YAML frontmatter dict."""
    trial_name = extract_trial_name(filename)

    fm = {}
    fm["type"] = "clinical_trial"
    fm["created"] = existing_fm.get("created", "")
    fm["updated"] = existing_fm.get("updated", "")
    fm["trial_name"] = trial_name

    tags = existing_fm.get("tags", [])
    if not isinstance(tags, list):
        tags = [tags] if tags else []
    if "clinical-trial" not in tags:
        tags.insert(0, "clinical-trial")
    fm["tags"] = tags

    # Extract from bullet template
    url_raw = extract_bullet_field(body, "clinicalTrialsURL")
    fm["nct_id"] = existing_fm.get("nct_id", extract_nct_id(url_raw) if url_raw else "")
    fm["clinicaltrials_url"] = existing_fm.get("clinicaltrials_url", url_raw if url_raw else "")

    phase_raw = extract_bullet_field(body, "phase")
    fm["phase"] = existing_fm.get("phase", normalize_phase(phase_raw) if phase_raw else "")

    status_raw = extract_bullet_field(body, "status")
    fm["status"] = existing_fm.get("status", strip_wikilinks(status_raw) if status_raw else "")

    fm["outcome"] = existing_fm.get("outcome", infer_outcome_from_filename(filename))

    drug_raw = extract_bullet_field(body, "drug")
    fm["drug"] = existing_fm.get("drug", strip_wikilinks(drug_raw) if drug_raw else "")

    fm["modality"] = existing_fm.get("modality", "")

    dose_raw = extract_bullet_field(body, "dose")
    fm["dose"] = existing_fm.get("dose", dose_raw if dose_raw else "")

    fm["company"] = existing_fm.get("company", "")

    indication_raw = extract_bullet_field(body, "indications")
    fm["diseases"] = existing_fm.get("diseases", map_disease(indication_raw, body))

    fm["indication_detail"] = existing_fm.get("indication_detail",
                                              strip_wikilinks(indication_raw) if indication_raw else "")

    size_raw = extract_bullet_field(body, "sampleSize")
    if size_raw and not existing_fm.get("n_enrolled"):
        # Parse number from text like "272" or "1,638"
        cleaned = size_raw.replace(",", "").strip()
        m = re.match(r'(\d+)', cleaned)
        fm["n_enrolled"] = int(m.group(1)) if m else None
    else:
        fm["n_enrolled"] = existing_fm.get("n_enrolled", None)

    ep_raw = extract_bullet_field(body, "primaryEndpoint")
    fm["primary_endpoint"] = existing_fm.get("primary_endpoint",
                                             strip_wikilinks(ep_raw) if ep_raw else "")

    fm["secondary_endpoints"] = existing_fm.get("secondary_endpoints", [])

    dur_raw = extract_bullet_field(body, "trialDuration")
    fm["duration"] = existing_fm.get("duration", dur_raw if dur_raw else "")

    ecd_raw = extract_bullet_field(body, "EstimatedCompletionDate")
    fm["estimated_completion"] = existing_fm.get("estimated_completion", ecd_raw if ecd_raw else "")

    fm["target_genes"] = existing_fm.get("target_genes", extract_genes_from_body(body))
    fm["therapeutic_strategy"] = existing_fm.get("therapeutic_strategy", "")

    papers_raw = extract_bullet_field(body, "papers")
    if papers_raw and not existing_fm.get("results_paper"):
        citekeys = re.findall(r'\[\[@([A-Za-z0-9_-]+?)(?:#|\||\]\])', papers_raw)
        fm["results_paper"] = citekeys[0] if citekeys else ""
    else:
        fm["results_paper"] = existing_fm.get("results_paper", "")

    return fm


def yaml_dump_frontmatter(fm):
    """Dump frontmatter dict to YAML string."""
    key_order = [
        "type", "created", "updated", "trial_name", "tags",
        "nct_id", "clinicaltrials_url",
        "phase", "status", "outcome",
        "drug", "modality", "dose", "company",
        "diseases", "indication_detail", "n_enrolled",
        "primary_endpoint", "secondary_endpoints",
        "duration", "estimated_completion",
        "target_genes", "therapeutic_strategy", "results_paper",
    ]
    lines = []
    for key in key_order:
        if key not in fm:
            continue
        val = fm[key]
        if isinstance(val, list):
            if not val:
                lines.append(f"{key}: []")
            else:
                lines.append(f"{key}:")
                for item in val:
                    item_str = str(item)
                    if any(c in item_str for c in [':', '#', '{', '}', '[', ']', ',', '&', '*', '?', '|', '-', '<', '>', '=', '!', '%', '@', '`', "'", '"']):
                        item_str = item_str.replace('"', '\\"')
                        lines.append(f'  - "{item_str}"')
                    else:
                        lines.append(f"  - {item_str}")
        elif val is None or val == "":
            lines.append(f"{key}: ")
        elif isinstance(val, str):
            if any(c in str(val) for c in [':', '#', '{', '}', '[', ']', ',', '&', '*', '?', '|', '-', '<', '>', '=', '!', '%', '@', '`']):
                lines.append(f'{key}: "{val}"')
            else:
                lines.append(f"{key}: {val}")
        else:
            lines.append(f"{key}: {val}")

    for key in fm:
        if key not in key_order:
            val = fm[key]
            if isinstance(val, list):
                if not val:
                    lines.append(f"{key}: []")
                else:
                    lines.append(f"{key}:")
                    for item in val:
                        lines.append(f"  - {item}")
            elif val is None or val == "":
                lines.append(f"{key}: ")
            else:
                lines.append(f"{key}: {val}")

    return "---\n" + "\n".join(lines) + "\n---"


def migrate_trial_note(filepath):
    """Migrate a single trial note."""
    changes = []
    warnings = []

    content = filepath.read_text(encoding="utf-8")
    existing_fm, body = parse_existing_frontmatter(content)

    if not is_clinical_trial(filepath.name, body):
        return "skipped", [], ["Not identified as a clinical trial note"]

    new_fm = build_trial_yaml(existing_fm, body, filepath.name)

    # Track changes
    if existing_fm.get("type") != "clinical_trial":
        changes.append("+type: clinical_trial")
    if new_fm.get("nct_id") and not existing_fm.get("nct_id"):
        changes.append(f"+nct_id: {new_fm['nct_id']}")
    if new_fm.get("phase") and not existing_fm.get("phase"):
        changes.append(f"+phase: {new_fm['phase']}")
    if new_fm.get("drug") and not existing_fm.get("drug"):
        changes.append(f"+drug: {new_fm['drug']}")
    if new_fm.get("n_enrolled") and not existing_fm.get("n_enrolled"):
        changes.append(f"+n_enrolled: {new_fm['n_enrolled']}")
    if new_fm.get("outcome") and not existing_fm.get("outcome"):
        changes.append(f"+outcome: {new_fm['outcome']}")
    if new_fm.get("diseases") and not existing_fm.get("diseases"):
        changes.append(f"+diseases: {new_fm['diseases']}")

    # Warnings
    if not new_fm.get("phase"):
        warnings.append("phase not found")
    if not new_fm.get("drug"):
        warnings.append("drug not found")
    if not new_fm.get("diseases"):
        warnings.append("diseases empty")
    if not new_fm.get("n_enrolled"):
        warnings.append("n_enrolled not found")

    new_yaml = yaml_dump_frontmatter(new_fm)
    new_content = new_yaml + "\n" + body

    filepath.write_text(new_content, encoding="utf-8")
    return "modified", changes, warnings


def generate_report(results, skipped_infra):
    """Generate the Phase 4 migration report."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    modified = sum(1 for s, _, _ in results.values() if s == "modified")
    skipped = sum(1 for s, _, _ in results.values() if s == "skipped")
    errors = sum(1 for s, _, _ in results.values() if s == "error")
    total = len(results)

    lines = [
        f"# Phase 4: Clinical Trial Notes — Migration Report\n",
        f"- **Date:** {now}",
        f"- **Notes scanned:** {total + len(skipped_infra)}",
        f"- **Notes modified (trials):** {modified}",
        f"- **Notes skipped (not a trial):** {skipped}",
        f"- **Infrastructure/meta notes excluded:** {len(skipped_infra)}",
        f"- **Errors:** {errors}\n",
        "## Summary\n",
        "Added `type: clinical_trial` YAML frontmatter to trial notes. Parsed bullet-point template ",
        "fields (sampleSize, drug, phase, clinicalTrialsURL, etc.) into YAML properties. Extracted ",
        "NCT IDs from URLs, normalized phase names, inferred outcome from emoji suffixes, and mapped ",
        "indications to canonical disease names. All original body text preserved.\n",
        "## Changes by Note\n",
        "| Note | Status | Changes | Warnings |",
        "|------|--------|---------|----------|",
    ]

    for name, (status, changes, warnings) in sorted(results.items()):
        ch = "; ".join(changes) if changes else "—"
        wr = "; ".join(warnings) if warnings else "—"
        lines.append(f"| {name} | {status} | {ch} | {wr} |")

    if skipped_infra:
        lines.append("\n## Excluded Infrastructure Notes\n")
        for name in sorted(skipped_infra):
            lines.append(f"- {name}")

    error_items = [(name, warnings) for name, (status, _, warnings) in sorted(results.items()) if status == "error"]
    if error_items:
        lines.append("\n## Errors\n")
        lines.append("| Note | Error |")
        lines.append("|------|-------|")
        for name, warnings in error_items:
            lines.append(f"| {name} | {'; '.join(warnings)} |")

    return "\n".join(lines)


def main():
    report_dir = Path("/Users/giovanni.coppola/Library/CloudStorage/OneDrive-RegeneronPharmaceuticals,Inc/MyScripts/myGitHubRepos/QAK/reports")
    report_dir.mkdir(exist_ok=True)

    # Candidate files: anything with "trial", "study", or known trial template fields
    candidates = set()
    skipped_infra = set()

    for f in VAULT.glob("*.md"):
        name = f.name
        if name.startswith("@") or name.startswith("^") or name.startswith("z "):
            continue  # Already handled in other phases
        name_lower = name.lower()
        if "trial" in name_lower or "study" in name_lower:
            if name in SKIP_FILES or name in COHORT_FILES:
                skipped_infra.add(name)
            else:
                candidates.add(f)
        # Check for template markers
        elif f.stat().st_size < 50000:
            try:
                content = f.read_text(encoding="utf-8")
                if any(re.search(rf'^\s*\*\s*{re.escape(tf)}\s*:', content, re.MULTILINE) for tf in ["sampleSize", "clinicalTrialsURL", "primaryEndpoint"]):
                    if name in SKIP_FILES or name in COHORT_FILES:
                        skipped_infra.add(name)
                    else:
                        candidates.add(f)
            except Exception:
                pass

    print(f"Found {len(candidates)} candidate trial notes (excluded {len(skipped_infra)} infrastructure/cohort notes)\n")

    results = {}
    for filepath in sorted(candidates):
        note_name = filepath.name
        try:
            status, changes, warnings = migrate_trial_note(filepath)
            results[note_name] = (status, changes, warnings)
            short_changes = "; ".join(changes[:3]) if changes else ""
            if len(changes) > 3:
                short_changes += f"; ... (+{len(changes)-3} more)"
            print(f"  {status:>8}  {note_name}  {short_changes}")
        except Exception as e:
            results[note_name] = ("error", [], [str(e)])
            print(f"  {'error':>8}  {note_name}  {e}")

    report = generate_report(results, skipped_infra)
    report_path = report_dir / "phase-4-trials.md"
    report_path.write_text(report, encoding="utf-8")
    print(f"\nReport written to: {report_path}")

    modified = sum(1 for s, _, _ in results.values() if s == "modified")
    skipped = sum(1 for s, _, _ in results.values() if s == "skipped")
    errors = sum(1 for s, _, _ in results.values() if s == "error")
    print(f"\nDone: {modified} modified, {skipped} skipped, {errors} errors")


if __name__ == "__main__":
    main()
