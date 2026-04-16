#!/usr/bin/env python3
"""
Phase 1: Disease Note Migration Script
Adds YAML frontmatter to disease notes in the gitVault.
No text is deleted — only YAML properties are added/updated.
"""

import re
import os
from pathlib import Path
from datetime import datetime

VAULT = Path("/Users/giovanni.coppola/Library/CloudStorage/OneDrive-RegeneronPharmaceuticals,Inc/MyScripts/myGitHubRepos/gitVault/gitVault-notes")

# Disease notes to migrate (identified from vault exploration)
DISEASE_NOTES = [
    # Neurodegeneration/Dementia
    "ALS.md",
    "Alzheimer's Disease.md",
    "Alzheimers Disease Early Onset–EOAD.md",
    "Frontotemporal Dementia.md",
    "Lewy Body Dementia.md",
    "Progressive Supranuclear Palsy (PSP).md",
    "Multiple System Atrophy.md",
    "MCI.md",
    "Subjective Cognitive Decline.md",
    "normal pressure hydrocephalus.md",
    "Huntington's Disease (HD).md",
    "idiopathic epilepsy.md",
    # Vision/Ophthalmology
    "AMD.md",
    "Glaucoma.md",
    "Retinitis Pigmentosa.md",
    "Stargardt Disease.md",
    "Birdshot.md",
    "Central Serous Chorioretinopathy (CSCR).md",
    "Fuchs endothelial corneal dystrophy (FECD).md",
    "Juvenile Open-Angle Glaucoma.md",
    "Juvenile X-linked Retinoschisis (XLRS).md",
    "keratoconus.md",
    "idiopathic intracranial hypertension.md",
    "myopia.md",
    "uveitis.md",
    # Neurological/Movement Disorders
    "Multiple Sclerosis.md",
    "Migraine.md",
    "Schizophrenia.md",
    "stroke.md",
    "CADASIL.md",
    # Autoimmune/Inflammatory
    "Ankylosing Spondylitis.md",
    "Psoriasis.md",
    "Neuromyelitis Optica.md",
    "Giant Cell Arteritis.md",
    "Pendred syndrome.md",
    "Progressive Multifocal Leukoencephalopathy.md",
    "Pulmonary Arterial Hypertension (PAH).md",
    "Rheumatoid Arthritis.md",
    # Genetic/Metabolic
    "Friedreich's Ataxia.md",
    "Duchenne Dystrophy.md",
    "Wilson's disease.md",
    "Angelman Syndrome.md",
    "15q duplication (dup15q).md",
    "Type III hyperlipoproteinemia.md",
    "SCA1.md",
    "SCA3.md",
    # Hearing
    "Hearing loss.md",
    "Pendred syndrome.md",
    # Psychiatric/Behavioral
    "autism spectrum disorder.md",
    "bipolar disorder.md",
    "depression.md",
    "alcohol use disorder.md",
    "eating disorders.md",
    "chronic pain.md",
    # Rare/Other
    "Paroxysmal Nocturnal Hemoglobinuria (PNH).md",
    "diabetic retinopathy.md",
    "diabetic neuropathy.md",
    "hereditary transthyretin amyloidosis (ATTR).md",
    "Parkinsonian-pyramidal syndrome.md",
]

# Remove duplicates
DISEASE_NOTES = list(dict.fromkeys(DISEASE_NOTES))


def parse_existing_frontmatter(content):
    """Parse existing YAML frontmatter manually (no PyYAML dependency).
    Returns (frontmatter_dict, body)."""
    if not content.startswith("---"):
        return {}, content
    end = content.find("\n---", 3)
    if end == -1:
        return {}, content

    fm_text = content[4:end].strip()
    body = content[end + 4:]  # skip past closing ---
    if body.startswith("\n"):
        body = body[1:]

    fm = {}
    current_key = None
    current_list = None

    for line in fm_text.split("\n"):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        # List item
        if stripped.startswith("- ") and current_key:
            val = stripped[2:].strip()
            if current_list is not None:
                current_list.append(val)
            continue

        # Key: value pair
        m = re.match(r'^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)', line)
        if m:
            # Save previous list if any
            if current_list is not None and current_key:
                fm[current_key] = current_list

            current_key = m.group(1)
            val = m.group(2).strip()

            if val == "" or val == "[]":
                current_list = []
            elif val.startswith("[") and val.endswith("]"):
                # Inline list
                items = [x.strip().strip('"').strip("'") for x in val[1:-1].split(",") if x.strip()]
                fm[current_key] = items
                current_list = None
            else:
                # Strip quotes
                val = val.strip('"').strip("'")
                # Try to convert to number
                try:
                    if "." in val:
                        fm[current_key] = float(val)
                    else:
                        fm[current_key] = int(val)
                except (ValueError, TypeError):
                    fm[current_key] = val
                current_list = None

    # Save last list
    if current_list is not None and current_key:
        fm[current_key] = current_list

    return fm, body


def extract_number(text):
    """Extract a number from text like '30,000' or '5.8M' or '70M'."""
    if not text:
        return None
    text = text.strip().replace(",", "")
    # Handle M/k suffixes
    m = re.match(r'^([\d.]+)\s*[Mm]$', text)
    if m:
        return int(float(m.group(1)) * 1_000_000)
    m = re.match(r'^([\d.]+)\s*[Kk]$', text)
    if m:
        return int(float(m.group(1)) * 1_000)
    m = re.match(r'^([\d.]+)$', text)
    if m:
        try:
            return int(float(m.group(1)))
        except ValueError:
            return None
    return None


def extract_stat(body, patterns):
    """Search body for bullet-point stats matching patterns. Return first match value."""
    for pattern in patterns:
        m = re.search(pattern, body, re.IGNORECASE)
        if m:
            return m.group(1).strip()
    return None


def extract_genes_from_body(body):
    """Extract gene symbols from [[^GENE]] wiki-links in body."""
    genes = re.findall(r'\[\[\^([A-Za-z0-9_-]+?)(?:\||\]\])', body)
    # Deduplicate preserving order
    seen = set()
    result = []
    for g in genes:
        if g not in seen:
            seen.add(g)
            result.append(g)
    return result


def extract_papers_from_body(body):
    """Extract citekeys from [[@Paper]] wiki-links in body."""
    papers = re.findall(r'\[\[@([A-Za-z0-9_-]+?)(?:#|\||\]\])', body)
    seen = set()
    result = []
    for p in papers:
        if p not in seen:
            seen.add(p)
            result.append(p)
    return result


def extract_gwas_info(body):
    """Extract GWAS size, loci count, and paper citekey from body."""
    gwas_n = None
    gwas_loci = None
    gwas_paper = None

    # GWASsize patterns
    m = re.search(r'GWASsize\s*:\s*([^\n\(\[]+)', body)
    if m:
        val = m.group(1).strip().rstrip(',;')
        gwas_n = extract_number(val)

    # GWASloci patterns
    m = re.search(r'GWASloci\s*:\s*(\d+)', body)
    if m:
        gwas_loci = int(m.group(1))

    # largestGWAS or GWAS paper
    m = re.search(r'(?:largestGWAS|GWASsize)\s*:.*?\[\[@([A-Za-z0-9_-]+)', body)
    if m:
        gwas_paper = m.group(1)

    return gwas_n, gwas_loci, gwas_paper


def extract_wes_info(body):
    """Extract WES size, loci count, and paper citekey from body."""
    wes_n = None
    wes_loci = None
    wes_paper = None

    m = re.search(r'WESsize\s*:\s*([^\n\(\[]+)', body)
    if m:
        val = m.group(1).strip().rstrip(',;')
        wes_n = extract_number(val)

    m = re.search(r'WESloci\s*:\s*(\d+)', body)
    if m:
        wes_loci = int(m.group(1))

    m = re.search(r'(?:WESsize)\s*:.*?\[\[@([A-Za-z0-9_-]+)', body)
    if m:
        wes_paper = m.group(1)

    return wes_n, wes_loci, wes_paper


def build_disease_yaml(existing_fm, body, filename):
    """Build the disease YAML frontmatter dict."""
    disease_name = filename.replace(".md", "")
    fm = {}

    # Preserve existing created/updated
    fm["type"] = "disease"
    fm["created"] = existing_fm.get("created", "")
    fm["updated"] = existing_fm.get("updated", "")

    # Preserve existing aliases or initialize empty
    fm["aliases"] = existing_fm.get("aliases", [])

    # Tags — preserve existing, ensure 'disease' is present
    tags = existing_fm.get("tags", [])
    if not isinstance(tags, list):
        tags = [tags] if tags else []
    if "disease" not in tags:
        tags.insert(0, "disease")
    fm["tags"] = tags

    # Epidemiology — extract from body or preserve existing
    prevalence_raw = extract_stat(body, [
        r'prevalence\s*:\s*([^\n]+?)(?:\s*$|\s*\[)',
        r'prevalence_per_100k\s*:\s*([^\n]+)',
    ])
    fm["prevalence_per_100k"] = existing_fm.get("prevalence_per_100k", None)

    # Incidence
    fm["incidence_per_100k"] = existing_fm.get("incidence_per_100k", None)

    # US cases
    us_raw = extract_stat(body, [
        r'UScases\s*:\s*([^\n]+?)(?:\s*$|\s*\[)',
    ])
    if us_raw and not existing_fm.get("n_patients_us"):
        n = extract_number(us_raw)
        fm["n_patients_us"] = n
    else:
        fm["n_patients_us"] = existing_fm.get("n_patients_us", None)

    # Lifetime risk
    lt_raw = extract_stat(body, [
        r'lifetimeRisk\s*:\s*([^\n]+?)(?:\s*$|\s*\[)',
        r'lifetime_risk\s*:\s*([^\n]+)',
    ])
    fm["lifetime_risk"] = existing_fm.get("lifetime_risk", lt_raw if lt_raw else "")

    # Ontology IDs — preserve existing
    fm["omim"] = existing_fm.get("omim", "")
    fm["mondo"] = existing_fm.get("mondo", "")
    fm["orphanet"] = existing_fm.get("orphanet", "")

    # Genetics — extract from body
    gwas_n, gwas_loci, gwas_paper = extract_gwas_info(body)
    fm["gwas_largest_n"] = existing_fm.get("gwas_largest_n", gwas_n)
    fm["gwas_loci"] = existing_fm.get("gwas_loci", gwas_loci)
    fm["gwas_paper"] = existing_fm.get("gwas_paper", gwas_paper if gwas_paper else "")

    wes_n, wes_loci, wes_paper = extract_wes_info(body)
    fm["wes_largest_n"] = existing_fm.get("wes_largest_n", wes_n)
    fm["wes_loci"] = existing_fm.get("wes_loci", wes_loci)
    fm["wes_paper"] = existing_fm.get("wes_paper", wes_paper if wes_paper else "")

    # Heritability
    fm["heritability_twin"] = existing_fm.get("heritability_twin", "")
    fm["heritability_gwas"] = existing_fm.get("heritability_gwas", "")

    # Genes — extract from body wiki-links
    genes = extract_genes_from_body(body)
    fm["genes"] = existing_fm.get("genes", genes if genes else [])

    # Projects
    fm["projects"] = existing_fm.get("projects", [])

    return fm


def yaml_dump_frontmatter(fm):
    """Dump frontmatter dict to YAML string with clean formatting."""
    # Custom order for readability
    key_order = [
        "type", "created", "updated", "aliases", "tags",
        "prevalence_per_100k", "incidence_per_100k", "n_patients_us",
        "lifetime_risk", "omim", "mondo", "orphanet",
        "gwas_largest_n", "gwas_loci", "gwas_paper",
        "wes_largest_n", "wes_loci", "wes_paper",
        "heritability_twin", "heritability_gwas",
        "genes", "projects",
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
                    lines.append(f"  - {item}")
        elif val is None or val == "":
            lines.append(f"{key}: ")
        elif isinstance(val, str):
            # Quote strings that could be misinterpreted
            if any(c in str(val) for c in [':', '#', '{', '}', '[', ']', ',', '&', '*', '?', '|', '-', '<', '>', '=', '!', '%', '@', '`']):
                lines.append(f'{key}: "{val}"')
            else:
                lines.append(f"{key}: {val}")
        else:
            lines.append(f"{key}: {val}")

    # Add any extra keys from existing frontmatter not in our order
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


def migrate_disease_note(filepath):
    """Migrate a single disease note. Returns (status, changes, warnings)."""
    changes = []
    warnings = []

    if not filepath.exists():
        return "skipped", [], [f"File not found: {filepath.name}"]

    content = filepath.read_text(encoding="utf-8")
    existing_fm, body = parse_existing_frontmatter(content)

    # Check if already migrated
    if existing_fm.get("type") == "disease" and "genes" in existing_fm:
        return "skipped", [], ["Already migrated (type: disease with genes in YAML)"]

    # Build new frontmatter
    new_fm = build_disease_yaml(existing_fm, body, filepath.name)

    # Track what changed
    if existing_fm.get("type") != "disease":
        changes.append("+type: disease")
    if "tags" not in existing_fm or "disease" not in existing_fm.get("tags", []):
        changes.append("+tags: disease")
    if new_fm.get("n_patients_us") and not existing_fm.get("n_patients_us"):
        changes.append(f"+n_patients_us: {new_fm['n_patients_us']}")
    if new_fm.get("gwas_largest_n") and not existing_fm.get("gwas_largest_n"):
        changes.append(f"+gwas_largest_n: {new_fm['gwas_largest_n']}")
    if new_fm.get("gwas_loci") and not existing_fm.get("gwas_loci"):
        changes.append(f"+gwas_loci: {new_fm['gwas_loci']}")
    if new_fm.get("gwas_paper") and not existing_fm.get("gwas_paper"):
        changes.append(f"+gwas_paper: {new_fm['gwas_paper']}")
    if new_fm.get("wes_largest_n") and not existing_fm.get("wes_largest_n"):
        changes.append(f"+wes_largest_n: {new_fm['wes_largest_n']}")
    if new_fm.get("wes_loci") and not existing_fm.get("wes_loci"):
        changes.append(f"+wes_loci: {new_fm['wes_loci']}")
    if new_fm.get("genes") and not existing_fm.get("genes"):
        changes.append(f"+genes: {new_fm['genes']}")

    # Warnings for empty important fields
    if not new_fm.get("n_patients_us"):
        warnings.append("n_patients_us left empty — not found in body")
    if not new_fm.get("gwas_largest_n"):
        warnings.append("gwas_largest_n left empty")
    if not new_fm.get("genes"):
        warnings.append("genes list empty — no ^GENE links found in body")

    # Write back — new YAML + original body (no text deleted)
    new_yaml = yaml_dump_frontmatter(new_fm)
    new_content = new_yaml + "\n" + body

    filepath.write_text(new_content, encoding="utf-8")
    return "modified", changes, warnings


def generate_report(results):
    """Generate the Phase 1 migration report."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    modified = sum(1 for s, _, _ in results.values() if s == "modified")
    skipped = sum(1 for s, _, _ in results.values() if s == "skipped")
    errors = sum(1 for s, _, _ in results.values() if s == "error")
    total = len(results)

    lines = [
        f"# Phase 1: Disease Notes — Migration Report\n",
        f"- **Date:** {now}",
        f"- **Notes processed:** {total}",
        f"- **Notes modified:** {modified}",
        f"- **Notes skipped:** {skipped}",
        f"- **Errors:** {errors}\n",
        "## Summary\n",
        "Added `type: disease` YAML frontmatter to disease notes. Extracted epidemiological stats ",
        "(prevalence, incidence, US cases), genetics summary (GWAS/WES size, loci, paper citekeys), ",
        "and gene lists from body text into YAML properties. All original body text preserved.\n",
        "## Changes by Note\n",
        "| Note | Status | Changes | Warnings |",
        "|------|--------|---------|----------|",
    ]

    for name, (status, changes, warnings) in sorted(results.items()):
        ch = "; ".join(changes) if changes else "—"
        wr = "; ".join(warnings) if warnings else "—"
        lines.append(f"| {name} | {status} | {ch} | {wr} |")

    # Manual review section
    review_items = []
    for name, (status, changes, warnings) in sorted(results.items()):
        if warnings and status == "modified":
            for w in warnings:
                review_items.append(f"- [ ] {name} — {w}")

    if review_items:
        lines.append("\n## Items Requiring Manual Review\n")
        lines.extend(review_items)

    # Skipped section
    skipped_items = [(name, warnings) for name, (status, _, warnings) in sorted(results.items()) if status == "skipped"]
    if skipped_items:
        lines.append("\n## Skipped Notes\n")
        lines.append("| Note | Reason |")
        lines.append("|------|--------|")
        for name, warnings in skipped_items:
            reason = "; ".join(warnings) if warnings else "unknown"
            lines.append(f"| {name} | {reason} |")

    return "\n".join(lines)


def main():
    report_dir = Path("/Users/giovanni.coppola/Library/CloudStorage/OneDrive-RegeneronPharmaceuticals,Inc/MyScripts/myGitHubRepos/QAK/reports")
    report_dir.mkdir(exist_ok=True)

    results = {}
    for note_name in DISEASE_NOTES:
        filepath = VAULT / note_name
        try:
            status, changes, warnings = migrate_disease_note(filepath)
            results[note_name] = (status, changes, warnings)
            print(f"  {status:>8}  {note_name}  {'; '.join(changes) if changes else ''}")
        except Exception as e:
            results[note_name] = ("error", [], [str(e)])
            print(f"  {'error':>8}  {note_name}  {e}")

    # Write report
    report = generate_report(results)
    report_path = report_dir / "phase-1-diseases.md"
    report_path.write_text(report, encoding="utf-8")
    print(f"\nReport written to: {report_path}")

    # Summary
    modified = sum(1 for s, _, _ in results.values() if s == "modified")
    skipped = sum(1 for s, _, _ in results.values() if s == "skipped")
    errors = sum(1 for s, _, _ in results.values() if s == "error")
    print(f"\nDone: {modified} modified, {skipped} skipped, {errors} errors")


if __name__ == "__main__":
    main()
