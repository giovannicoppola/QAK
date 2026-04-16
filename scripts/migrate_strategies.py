#!/usr/bin/env python3
"""
Phase 5: Therapeutic Strategy Note Migration Script
Adds YAML frontmatter to therapeutic strategy notes in the gitVault.
No text is deleted — only YAML properties are added/updated.
"""

import re
from pathlib import Path
from datetime import datetime

VAULT = Path("/Users/giovanni.coppola/Library/CloudStorage/OneDrive-RegeneronPharmaceuticals,Inc/MyScripts/myGitHubRepos/gitVault/gitVault-notes")

# Therapeutic strategy notes — manually curated list from vault exploration
STRATEGY_NOTES = [
    "AMD - Therapeutic Strategies.md",
    "AMD Therapeutic strategies – complement.md",
    "ALS therapeutic strategies.md",
    "APOE Therapeutic Strategies.md",
    "APP therapeutic strategies.md",
    "Alzheimer's  Therapeutic Strategies.md",
    "Alzheimers Disease Therapeutic Strategies.md",
    "C9orf72  Therapeutic Strategies.md",
    "GBA therapeutic strategies.md",
    "GRN Therapeutic Strategies.md",
    "Glaucoma Therapeutic Strategies.md",
    "Huntington' Disease – Therapeutic Strategies.md",
    "MYOC Therapeutic Strategies.md",
    "Migraine Therapeutic Strategies.md",
    "Multiple Sclerosis – Therapeutic Strategies.md",
    "Multiple system atrophy - Therapeutic Strategies.md",
    "Pulmonary Arterial Hypertension PAH Therapeutic Strategies.md",
    "Rheumatoid Arthritis  Therapeutic Strategies.md",
    "SCA3 therapeutic strategies.md",
    "SCN10A – Therapeutic Strategies.md",
    "SCN9A – Therapeutic Strategies.md",
    "SNCA – Therapeutic Strategies.md",
    "SOD1 therapeutic strategies.md",
    "Schizophrenia –  Therapeutic strategies.md",
    "TREM2 therapeutic strategies.md",
    "Therapeutic Strategies.md",
    "Therapeutic strategies targeting complement in AMD.md",
    "diabetic retinopathy therapeutic strategies.md",
    "hereditary transthyretin amyloidosis (ATTR) –  therapeutic strategies.md",
    "microglia – therapeutic strategies.md",
    "smoking – therapeutic strategies.md",
    "tau – Therapeutic Strategies.md",
]

# Disease mapping from strategy note names
DISEASE_FROM_NAME = {
    "AMD": "AMD",
    "ALS": "ALS",
    "Alzheimer": "Alzheimer's Disease",
    "Glaucoma": "Glaucoma",
    "Huntington": "Huntington's Disease (HD)",
    "Migraine": "Migraine",
    "Multiple Sclerosis": "Multiple Sclerosis",
    "Multiple system atrophy": "Multiple System Atrophy",
    "Pulmonary Arterial Hypertension": "Pulmonary Arterial Hypertension (PAH)",
    "Rheumatoid Arthritis": "Rheumatoid Arthritis",
    "SCA3": "SCA3",
    "Schizophrenia": "Schizophrenia",
    "diabetic retinopathy": "diabetic retinopathy",
    "transthyretin amyloidosis": "hereditary transthyretin amyloidosis (ATTR)",
    "ATTR": "hereditary transthyretin amyloidosis (ATTR)",
}

# Gene mapping from strategy note names
GENE_FROM_NAME = {
    "APOE": "APOE",
    "APP": "APP",
    "C9orf72": "C9orf72",
    "GBA": "GBA",
    "GRN": "GRN",
    "MYOC": "MYOC",
    "SCN10A": "SCN10A",
    "SCN9A": "SCN9A",
    "SNCA": "SNCA",
    "SOD1": "SOD1",
    "TREM2": "TREM2",
    "tau": "MAPT",
    "complement": "C3",
}

# Modality keywords
MODALITY_KEYWORDS = {
    "antibody": ["antibody", "antibodies", "mAb", "monoclonal"],
    "antisense": ["antisense", "ASO", "oligonucleotide"],
    "small-molecule": ["small molecule", "small-molecule", "inhibitor", "kinase inhibitor"],
    "gene-therapy": ["gene therapy", "gene-therapy", "AAV", "adeno-associated"],
    "sirna": ["siRNA", "RNAi", "RNA interference"],
    "cell-therapy": ["cell therapy", "cell-therapy", "CAR-T", "stem cell"],
    "vaccine": ["vaccine", "immunization"],
    "enzyme-replacement": ["enzyme replacement", "ERT"],
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


def infer_diseases(filename, body):
    """Infer diseases from filename and body content."""
    diseases = []
    seen = set()

    for pattern, canonical in DISEASE_FROM_NAME.items():
        if pattern.lower() in filename.lower() and canonical not in seen:
            seen.add(canonical)
            diseases.append(canonical)

    # Also check body wiki-links
    from_links = re.findall(r'\[\[([^\]|#]+?)(?:\||\]\]|#)', body)
    known = list(DISEASE_FROM_NAME.values())
    for link in from_links:
        for disease in known:
            if link.strip().lower() == disease.lower() and disease not in seen:
                seen.add(disease)
                diseases.append(disease)

    return diseases


def infer_target_genes(filename, body):
    """Infer target genes from filename and body content."""
    genes = []
    seen = set()

    for pattern, gene in GENE_FROM_NAME.items():
        if pattern.lower() in filename.lower() and gene not in seen:
            seen.add(gene)
            genes.append(gene)

    # From body [[^GENE]] links
    body_genes = re.findall(r'\[\[\^([A-Za-z0-9_]+?)(?:\||\]\])', body)
    for g in body_genes:
        if g not in seen:
            seen.add(g)
            genes.append(g)

    return genes


def infer_modality(body):
    """Infer modality from body content."""
    body_lower = body.lower()
    for modality, keywords in MODALITY_KEYWORDS.items():
        for kw in keywords:
            if kw.lower() in body_lower:
                return modality
    return ""


def extract_trials(body):
    """Extract linked trial names from body."""
    trials = []
    # Look for wiki-links containing "trial" or "study"
    links = re.findall(r'\[\[([^\]|]+?)(?:\||\]\])', body)
    for link in links:
        link_clean = link.strip()
        if "trial" in link_clean.lower() or "study" in link_clean.lower():
            if not link_clean.startswith("@") and not link_clean.startswith("Roam/"):
                trials.append(link_clean)
    return list(dict.fromkeys(trials))  # dedupe preserving order


def build_strategy_yaml(existing_fm, body, filename):
    """Build the therapeutic strategy YAML frontmatter dict."""
    name = filename.replace(".md", "")

    fm = {}
    fm["type"] = "therapeutic_strategy"
    fm["created"] = existing_fm.get("created", "")
    fm["updated"] = existing_fm.get("updated", "")

    tags = existing_fm.get("tags", [])
    if not isinstance(tags, list):
        tags = [tags] if tags else []
    if "therapeutic-strategy" not in tags:
        tags.insert(0, "therapeutic-strategy")
    fm["tags"] = tags

    fm["diseases"] = existing_fm.get("diseases", infer_diseases(filename, body))
    fm["target_genes"] = existing_fm.get("target_genes", infer_target_genes(filename, body))
    fm["modality"] = existing_fm.get("modality", infer_modality(body))
    fm["clinical_trials"] = existing_fm.get("clinical_trials", extract_trials(body))

    return fm


def yaml_dump_frontmatter(fm):
    """Dump frontmatter dict to YAML string."""
    key_order = [
        "type", "created", "updated", "tags",
        "diseases", "target_genes", "modality", "clinical_trials",
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


def migrate_strategy_note(filepath):
    """Migrate a single therapeutic strategy note."""
    changes = []
    warnings = []

    if not filepath.exists():
        return "skipped", [], [f"File not found: {filepath.name}"]

    content = filepath.read_text(encoding="utf-8")
    existing_fm, body = parse_existing_frontmatter(content)

    new_fm = build_strategy_yaml(existing_fm, body, filepath.name)

    if existing_fm.get("type") != "therapeutic_strategy":
        changes.append("+type: therapeutic_strategy")
    if new_fm.get("diseases") and not existing_fm.get("diseases"):
        changes.append(f"+diseases: {new_fm['diseases']}")
    if new_fm.get("target_genes") and not existing_fm.get("target_genes"):
        changes.append(f"+target_genes: {new_fm['target_genes']}")
    if new_fm.get("modality") and not existing_fm.get("modality"):
        changes.append(f"+modality: {new_fm['modality']}")
    if new_fm.get("clinical_trials") and not existing_fm.get("clinical_trials"):
        changes.append(f"+clinical_trials: {len(new_fm['clinical_trials'])}")

    if not new_fm.get("diseases"):
        warnings.append("diseases empty")
    if not new_fm.get("target_genes"):
        warnings.append("target_genes empty")

    new_yaml = yaml_dump_frontmatter(new_fm)
    new_content = new_yaml + "\n" + body

    filepath.write_text(new_content, encoding="utf-8")
    return "modified", changes, warnings


def generate_report(results):
    """Generate the Phase 5 migration report."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    modified = sum(1 for s, _, _ in results.values() if s == "modified")
    skipped = sum(1 for s, _, _ in results.values() if s == "skipped")
    errors = sum(1 for s, _, _ in results.values() if s == "error")

    lines = [
        f"# Phase 5: Therapeutic Strategy Notes — Migration Report\n",
        f"- **Date:** {now}",
        f"- **Notes processed:** {len(results)}",
        f"- **Notes modified:** {modified}",
        f"- **Notes skipped:** {skipped}",
        f"- **Errors:** {errors}\n",
        "## Summary\n",
        "Added `type: therapeutic_strategy` YAML frontmatter to strategy notes. Inferred diseases ",
        "and target genes from filenames and body links. Detected modality from keywords. ",
        "Extracted linked trial names. All original body text preserved.\n",
        "## Changes by Note\n",
        "| Note | Status | Changes | Warnings |",
        "|------|--------|---------|----------|",
    ]

    for name, (status, changes, warnings) in sorted(results.items()):
        ch = "; ".join(changes) if changes else "—"
        wr = "; ".join(warnings) if warnings else "—"
        lines.append(f"| {name} | {status} | {ch} | {wr} |")

    skipped_items = [(n, w) for n, (s, _, w) in sorted(results.items()) if s == "skipped"]
    if skipped_items:
        lines.append("\n## Skipped Notes\n")
        for name, warnings in skipped_items:
            lines.append(f"- {name}: {'; '.join(warnings)}")

    return "\n".join(lines)


def main():
    report_dir = Path("/Users/giovanni.coppola/Library/CloudStorage/OneDrive-RegeneronPharmaceuticals,Inc/MyScripts/myGitHubRepos/QAK/reports")
    report_dir.mkdir(exist_ok=True)

    print(f"Processing {len(STRATEGY_NOTES)} therapeutic strategy notes\n")

    results = {}
    for note_name in STRATEGY_NOTES:
        filepath = VAULT / note_name
        try:
            status, changes, warnings = migrate_strategy_note(filepath)
            results[note_name] = (status, changes, warnings)
            short_changes = "; ".join(changes[:3]) if changes else ""
            print(f"  {status:>8}  {note_name}  {short_changes}")
        except Exception as e:
            results[note_name] = ("error", [], [str(e)])
            print(f"  {'error':>8}  {note_name}  {e}")

    report = generate_report(results)
    report_path = report_dir / "phase-5-strategies.md"
    report_path.write_text(report, encoding="utf-8")
    print(f"\nReport written to: {report_path}")

    modified = sum(1 for s, _, _ in results.values() if s == "modified")
    skipped = sum(1 for s, _, _ in results.values() if s == "skipped")
    errors = sum(1 for s, _, _ in results.values() if s == "error")
    print(f"\nDone: {modified} modified, {skipped} skipped, {errors} errors")


if __name__ == "__main__":
    main()
