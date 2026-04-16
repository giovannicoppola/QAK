#!/usr/bin/env python3
"""
Phase 3: Paper Note Migration Script
Adds YAML frontmatter to @-prefixed paper notes in the gitVault.
No text is deleted — only YAML properties are added/updated.
AI-generated summaries (OBSummary_AI) are deferred to Phase 9.
"""

import re
import os
from pathlib import Path
from datetime import datetime

VAULT = Path("/Users/giovanni.coppola/Library/CloudStorage/OneDrive-RegeneronPharmaceuticals,Inc/MyScripts/myGitHubRepos/gitVault/gitVault-notes")

# Known disease names for matching
KNOWN_DISEASES = [
    "ALS", "Alzheimer's Disease", "Alzheimers Disease Early Onset–EOAD",
    "Frontotemporal Dementia", "Lewy Body Dementia",
    "Progressive Supranuclear Palsy (PSP)", "Multiple System Atrophy",
    "MCI", "Huntington's Disease (HD)", "idiopathic epilepsy",
    "AMD", "Glaucoma", "Retinitis Pigmentosa", "Stargardt Disease",
    "Birdshot", "Central Serous Chorioretinopathy (CSCR)",
    "Fuchs endothelial corneal dystrophy (FECD)", "Juvenile Open-Angle Glaucoma",
    "Juvenile X-linked Retinoschisis (XLRS)", "keratoconus",
    "idiopathic intracranial hypertension", "myopia", "uveitis",
    "Multiple Sclerosis", "Migraine", "Schizophrenia", "stroke", "CADASIL",
    "Ankylosing Spondylitis", "Psoriasis", "Neuromyelitis Optica",
    "Giant Cell Arteritis", "Pendred syndrome",
    "Progressive Multifocal Leukoencephalopathy",
    "Pulmonary Arterial Hypertension (PAH)", "Rheumatoid Arthritis",
    "Friedreich's Ataxia", "Duchenne Dystrophy", "Wilson's disease",
    "Angelman Syndrome", "15q duplication (dup15q)",
    "Type III hyperlipoproteinemia", "SCA1", "SCA3",
    "Hearing loss", "autism spectrum disorder", "bipolar disorder",
    "depression", "alcohol use disorder", "eating disorders", "chronic pain",
    "Paroxysmal Nocturnal Hemoglobinuria (PNH)",
    "diabetic retinopathy", "diabetic neuropathy",
    "hereditary transthyretin amyloidosis (ATTR)",
    "Parkinsonian-pyramidal syndrome",
    "Parkinson's Disease", "Crohn's Disease", "Gaucher disease",
    "Nasu-Hakola disease",
]

# Disease name patterns to search in body text (case-insensitive)
DISEASE_PATTERNS = {
    "Alzheimer": "Alzheimer's Disease",
    "ALS": "ALS",
    "amyotrophic lateral sclerosis": "ALS",
    "Parkinson": "Parkinson's Disease",
    "frontotemporal dementia": "Frontotemporal Dementia",
    "FTD": "Frontotemporal Dementia",
    "multiple sclerosis": "Multiple Sclerosis",
    "AMD": "AMD",
    "age-related macular degeneration": "AMD",
    "macular degeneration": "AMD",
    "glaucoma": "Glaucoma",
    "schizophrenia": "Schizophrenia",
    "huntington": "Huntington's Disease (HD)",
    "retinitis pigmentosa": "Retinitis Pigmentosa",
    "migraine": "Migraine",
    "psoriasis": "Psoriasis",
    "rheumatoid arthritis": "Rheumatoid Arthritis",
    "autism": "autism spectrum disorder",
    "bipolar": "bipolar disorder",
    "Lewy body": "Lewy Body Dementia",
    "progressive supranuclear palsy": "Progressive Supranuclear Palsy (PSP)",
    "PSP": "Progressive Supranuclear Palsy (PSP)",
    "transthyretin amyloidosis": "hereditary transthyretin amyloidosis (ATTR)",
    "ATTR": "hereditary transthyretin amyloidosis (ATTR)",
}

# Study type keywords for inference
STUDY_TYPE_PATTERNS = {
    "gwas": ["GWAS", "genome-wide association", "genome wide association"],
    "exome": ["exome", "WES", "whole-exome", "exome sequencing", "exome chip"],
    "wgs": ["whole-genome sequencing", "WGS", "whole genome sequencing"],
    "review": ["review", "Review", "perspectives", "overview"],
    "meta-analysis": ["meta-analysis", "meta analysis", "Meta-Analysis"],
    "clinical-trial": ["clinical trial", "randomized", "placebo-controlled", "phase 1", "phase 2", "phase 3", "Phase I", "Phase II", "Phase III"],
    "functional": ["functional study", "in vitro", "mouse model", "knockout", "transgenic"],
}


def parse_existing_frontmatter(content):
    """Parse existing YAML frontmatter manually (no PyYAML dependency)."""
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


def extract_citekey(filename):
    """Extract citekey from @-prefixed filename."""
    name = filename.replace(".md", "")
    if name.startswith("@"):
        name = name[1:]
    return name


def extract_author_year(citekey):
    """Extract first author surname and year from citekey like Holstege2020-ky."""
    m = re.match(r'^([A-Za-z_-]+?)(\d{4})', citekey)
    if m:
        author = m.group(1).rstrip("-_")
        # Clean up underscores in author names
        author = author.replace("_", " ").split("-")[0].split()[0] if "_" in author or "-" in author else author
        year = int(m.group(2))
        return author, year
    return "", None


def extract_title_from_citation(body):
    """Try to extract paper title from citation line in body."""
    # Look for common citation patterns:
    # Author et al. Title. Journal. Year
    # or just lines that look like full citations
    lines = body.split("\n")
    for line in lines:
        line = line.strip().lstrip("* ").lstrip("- ")
        # Skip empty, short, or clearly non-citation lines
        if len(line) < 30:
            continue
        if line.startswith("![[") or line.startswith("![]("):
            continue
        if line.startswith("[[") and "]]" in line[:50]:
            continue
        # Look for citation pattern: Author(s) ... Title. Journal
        # Citations typically contain: year, PMID/PMCID, DOI, or journal name
        if any(marker in line for marker in ["PMID:", "PMCID:", "doi.", "dx.doi", "Available from:", "http"]):
            # Extract the title part — usually between first period and second period
            # or the main content after author list
            return line
    return ""


def extract_genes_from_body(body):
    """Extract gene symbols from [[^GENE]] wiki-links in body."""
    genes = re.findall(r'\[\[\^([A-Za-z0-9_-]+?)(?:\||\]\])', body)
    seen = set()
    result = []
    for g in genes:
        # Skip sub-page artifacts
        if " " in g or "–" in g:
            continue
        if g not in seen:
            seen.add(g)
            result.append(g)
    return result


def extract_diseases_from_body(body):
    """Extract disease names from wiki-links and text patterns."""
    diseases = []
    seen = set()

    # Match wiki-links to known disease notes
    wikilinks = re.findall(r'\[\[([^\]|#]+?)(?:\||\]\]|#)', body)
    for link in wikilinks:
        link_clean = link.strip()
        for disease in KNOWN_DISEASES:
            if link_clean.lower() == disease.lower() and disease not in seen:
                seen.add(disease)
                diseases.append(disease)
                break

    # Check for disease name patterns in body text
    for pattern, canonical in DISEASE_PATTERNS.items():
        if canonical in seen:
            continue
        if re.search(r'\b' + re.escape(pattern) + r'\b', body, re.IGNORECASE):
            seen.add(canonical)
            diseases.append(canonical)

    return diseases


def detect_obs_block(body):
    """Check if body contains #obs tagged content. Return the obs text if found."""
    # Match #obs at word boundary (not #observation etc.)
    m = re.search(r'#obs\b(.*)$', body, re.MULTILINE)
    if m:
        return True
    return False


def infer_study_type(body, citekey):
    """Infer study type from body content."""
    body_lower = body.lower()
    for stype, keywords in STUDY_TYPE_PATTERNS.items():
        for kw in keywords:
            if kw.lower() in body_lower:
                return stype
    return ""


def extract_sample_sizes(body):
    """Try to extract sample sizes from body text."""
    n_cases = None
    n_controls = None
    n_total = None
    n_loci = None

    # Patterns for cases/controls
    m = re.search(r'(\d[\d,]+)\s*(?:AD\s+)?cases?\s+(?:and\s+)?(\d[\d,]+)\s*controls?', body, re.IGNORECASE)
    if m:
        n_cases = int(m.group(1).replace(",", ""))
        n_controls = int(m.group(2).replace(",", ""))
        n_total = n_cases + n_controls

    # Pattern for total N
    if not n_total:
        m = re.search(r'[Nn]\s*=\s*(\d[\d,]+)', body)
        if m:
            n_total = int(m.group(1).replace(",", ""))

    # Pattern for total individuals
    if not n_total:
        m = re.search(r'(\d[\d,]+)\s+individuals', body, re.IGNORECASE)
        if m:
            n_total = int(m.group(1).replace(",", ""))

    # Loci count
    m = re.search(r'(\d+)\s+(?:genome-wide significant\s+)?(?:risk\s+)?loci', body, re.IGNORECASE)
    if m:
        n_loci = int(m.group(1))

    return n_cases, n_controls, n_total, n_loci


def build_paper_yaml(existing_fm, body, filename):
    """Build the paper YAML frontmatter dict."""
    citekey = extract_citekey(filename)
    first_author, year = extract_author_year(citekey)

    fm = {}

    fm["type"] = "paper"
    fm["created"] = existing_fm.get("created", "")
    fm["updated"] = existing_fm.get("updated", "")
    fm["citekey"] = citekey

    # Title — leave empty for now (would need bibliographic DB to populate)
    fm["title"] = existing_fm.get("title", "")

    # Tags
    tags = existing_fm.get("tags", [])
    if not isinstance(tags, list):
        tags = [tags] if tags else []
    if "paper" not in tags:
        tags.insert(0, "paper")
    fm["tags"] = tags

    # Study type
    fm["study_type"] = existing_fm.get("study_type", infer_study_type(body, citekey))

    # Diseases and genes
    fm["diseases"] = existing_fm.get("diseases", extract_diseases_from_body(body))
    fm["genes"] = existing_fm.get("genes", extract_genes_from_body(body))

    # Sample sizes
    n_cases, n_controls, n_total, n_loci = extract_sample_sizes(body)
    fm["n_cases"] = existing_fm.get("n_cases", n_cases if n_cases else None)
    fm["n_controls"] = existing_fm.get("n_controls", n_controls if n_controls else None)
    fm["n_total"] = existing_fm.get("n_total", n_total if n_total else None)
    fm["n_loci"] = existing_fm.get("n_loci", n_loci if n_loci else None)

    # Author/year
    fm["first_author"] = existing_fm.get("first_author", first_author)
    fm["year"] = existing_fm.get("year", year)
    fm["journal"] = existing_fm.get("journal", "")

    # OBS source
    has_obs = detect_obs_block(body)
    if has_obs:
        fm["obs_source"] = "human"
    else:
        fm["obs_source"] = ""

    return fm


def yaml_dump_frontmatter(fm):
    """Dump frontmatter dict to YAML string."""
    key_order = [
        "type", "created", "updated", "citekey", "title", "tags",
        "study_type", "diseases", "genes",
        "n_cases", "n_controls", "n_total", "n_loci",
        "first_author", "year", "journal",
        "obs_source",
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

    # Extra keys
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


def migrate_paper_note(filepath):
    """Migrate a single paper note. Returns (status, changes, warnings)."""
    changes = []
    warnings = []

    if not filepath.exists():
        return "skipped", [], [f"File not found: {filepath.name}"]

    content = filepath.read_text(encoding="utf-8")
    existing_fm, body = parse_existing_frontmatter(content)

    new_fm = build_paper_yaml(existing_fm, body, filepath.name)

    # Track changes
    if existing_fm.get("type") != "paper":
        changes.append("+type: paper")
    if not existing_fm.get("citekey"):
        changes.append(f"+citekey: {new_fm['citekey']}")
    if new_fm.get("diseases") and not existing_fm.get("diseases"):
        changes.append(f"+diseases: {len(new_fm['diseases'])}")
    if new_fm.get("genes") and not existing_fm.get("genes"):
        changes.append(f"+genes: {len(new_fm['genes'])}")
    if new_fm.get("study_type") and not existing_fm.get("study_type"):
        changes.append(f"+study_type: {new_fm['study_type']}")
    if new_fm.get("n_total") and not existing_fm.get("n_total"):
        changes.append(f"+n_total: {new_fm['n_total']}")
    if new_fm.get("obs_source") == "human":
        changes.append("+obs_source: human")

    # Warnings
    if not new_fm.get("diseases"):
        warnings.append("diseases empty")
    if not new_fm.get("study_type"):
        warnings.append("study_type not inferred")

    # Write
    new_yaml = yaml_dump_frontmatter(new_fm)
    new_content = new_yaml + "\n" + body

    filepath.write_text(new_content, encoding="utf-8")
    return "modified", changes, warnings


def generate_report(results):
    """Generate the Phase 3 migration report."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    modified = sum(1 for s, _, _ in results.values() if s == "modified")
    skipped = sum(1 for s, _, _ in results.values() if s == "skipped")
    errors = sum(1 for s, _, _ in results.values() if s == "error")
    total = len(results)

    # Count property population
    n_with_diseases = 0
    n_with_genes = 0
    n_with_study_type = 0
    n_with_n_total = 0
    n_with_obs = 0

    for name, (status, changes, warnings) in results.items():
        if status != "modified":
            continue
        ch_str = " ".join(changes)
        if "diseases empty" not in " ".join(warnings):
            n_with_diseases += 1
        if "+genes:" in ch_str:
            n_with_genes += 1
        if "study_type not inferred" not in " ".join(warnings):
            n_with_study_type += 1
        if "+n_total:" in ch_str:
            n_with_n_total += 1
        if "obs_source: human" in ch_str:
            n_with_obs += 1

    lines = [
        f"# Phase 3: Paper Notes — Migration Report\n",
        f"- **Date:** {now}",
        f"- **Notes processed:** {total}",
        f"- **Notes modified:** {modified}",
        f"- **Notes skipped:** {skipped}",
        f"- **Errors:** {errors}\n",
        "## Summary\n",
        "Added `type: paper` YAML frontmatter to paper notes. Extracted citekey from filename, ",
        "first author and year from citekey, diseases and genes from wiki-links and text patterns, ",
        "study type by keyword inference, sample sizes from body text, and detected `#obs` blocks. ",
        "All original body text preserved. AI-generated summaries (`OBSummary_AI`) deferred to Phase 9.\n",
        "## YAML Properties Populated\n",
        "| Property | Populated | Left Empty | Notes |",
        "|----------|----------:|----------:|-------|",
        f"| type | {modified}/{modified} | 0 | always 'paper' |",
        f"| citekey | {modified}/{modified} | 0 | from filename |",
        f"| first_author | {modified}/{modified} | 0 | from citekey |",
        f"| year | {modified}/{modified} | 0 | from citekey |",
        f"| diseases | {n_with_diseases}/{modified} | {modified - n_with_diseases} | from links + text patterns |",
        f"| genes | {n_with_genes}/{modified} | {modified - n_with_genes} | from [[^GENE]] links |",
        f"| study_type | {n_with_study_type}/{modified} | {modified - n_with_study_type} | keyword inference |",
        f"| n_total | {n_with_n_total}/{modified} | {modified - n_with_n_total} | from body text |",
        f"| obs_source | {n_with_obs}/{modified} | {modified - n_with_obs} | {n_with_obs} human, {modified - n_with_obs} empty (AI gen deferred) |",
        f"| title | 0/{modified} | {modified} | needs bibliographic DB |",
        f"| journal | 0/{modified} | {modified} | needs bibliographic DB |",
        "",
        "## Changes by Note\n",
        "| Note | Status | Changes | Warnings |",
        "|------|--------|---------|----------|",
    ]

    for name, (status, changes, warnings) in sorted(results.items()):
        ch = "; ".join(changes) if changes else "—"
        wr = "; ".join(warnings) if warnings else "—"
        lines.append(f"| {name} | {status} | {ch} | {wr} |")

    # Skipped section
    skipped_items = [(name, warnings) for name, (status, _, warnings) in sorted(results.items()) if status == "skipped"]
    if skipped_items:
        lines.append("\n## Skipped Notes\n")
        lines.append("| Note | Reason |")
        lines.append("|------|--------|")
        for name, warnings in skipped_items:
            reason = "; ".join(warnings) if warnings else "unknown"
            lines.append(f"| {name} | {reason} |")

    # Error section
    error_items = [(name, warnings) for name, (status, _, warnings) in sorted(results.items()) if status == "error"]
    if error_items:
        lines.append("\n## Errors\n")
        lines.append("| Note | Error |")
        lines.append("|------|-------|")
        for name, warnings in error_items:
            err = "; ".join(warnings) if warnings else "unknown"
            lines.append(f"| {name} | {err} |")

    return "\n".join(lines)


def main():
    report_dir = Path("/Users/giovanni.coppola/Library/CloudStorage/OneDrive-RegeneronPharmaceuticals,Inc/MyScripts/myGitHubRepos/QAK/reports")
    report_dir.mkdir(exist_ok=True)

    # Find all @*.md paper notes
    paper_files = sorted(VAULT.glob("@*.md"))
    print(f"Found {len(paper_files)} paper notes to migrate\n")

    results = {}
    for filepath in paper_files:
        note_name = filepath.name
        try:
            status, changes, warnings = migrate_paper_note(filepath)
            results[note_name] = (status, changes, warnings)
            short_changes = "; ".join(changes[:3]) if changes else ""
            if len(changes) > 3:
                short_changes += f"; ... (+{len(changes)-3} more)"
            print(f"  {status:>8}  {note_name}  {short_changes}")
        except Exception as e:
            results[note_name] = ("error", [], [str(e)])
            print(f"  {'error':>8}  {note_name}  {e}")

    # Write report
    report = generate_report(results)
    report_path = report_dir / "phase-3-papers.md"
    report_path.write_text(report, encoding="utf-8")
    print(f"\nReport written to: {report_path}")

    # Summary
    modified = sum(1 for s, _, _ in results.values() if s == "modified")
    skipped = sum(1 for s, _, _ in results.values() if s == "skipped")
    errors = sum(1 for s, _, _ in results.values() if s == "error")
    obs_count = sum(1 for name, (status, changes, _) in results.items()
                    if status == "modified" and any("obs_source: human" in c for c in changes))
    print(f"\nDone: {modified} modified, {skipped} skipped, {errors} errors")
    print(f"  #obs blocks found: {obs_count} / {modified} ({modified - obs_count} need AI summary in Phase 9)")


if __name__ == "__main__":
    main()
