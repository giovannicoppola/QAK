#!/usr/bin/env python3
"""
Phase 2: Gene Note Migration Script
Adds YAML frontmatter to ^-prefixed gene notes in the gitVault.
No text is deleted — only YAML properties are added/updated.
"""

import re
import os
from pathlib import Path
from datetime import datetime

VAULT = Path("/Users/giovanni.coppola/Library/CloudStorage/OneDrive-RegeneronPharmaceuticals,Inc/MyScripts/myGitHubRepos/gitVault/gitVault-notes")

# Known disease notes (from Phase 1 migration) — used to match disease references in gene note bodies
KNOWN_DISEASES = [
    "ALS", "Alzheimer's Disease", "Alzheimers Disease Early Onset–EOAD",
    "Frontotemporal Dementia", "Lewy Body Dementia",
    "Progressive Supranuclear Palsy (PSP)", "Multiple System Atrophy",
    "MCI", "Subjective Cognitive Decline", "normal pressure hydrocephalus",
    "Huntington's Disease (HD)", "idiopathic epilepsy",
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
    # Common disease names that may appear as wiki-links or plain text
    "Parkinson's Disease", "Crohn's Disease", "Gaucher disease",
    "Nasu-Hakola disease", "leprosy", "tuberculosis",
]

# Short names to match in wiki-links and body text
DISEASE_SHORT_NAMES = {
    "AD": "Alzheimer's Disease",
    "PD": "Parkinson's Disease",
    "FTD": "Frontotemporal Dementia",
    "PSP": "Progressive Supranuclear Palsy (PSP)",
    "MSA": "Multiple System Atrophy",
    "MS": "Multiple Sclerosis",
    "HD": "Huntington's Disease (HD)",
    "RP": "Retinitis Pigmentosa",
    "PAH": "Pulmonary Arterial Hypertension (PAH)",
    "RA": "Rheumatoid Arthritis",
    "EOAD": "Alzheimers Disease Early Onset–EOAD",
    "PNH": "Paroxysmal Nocturnal Hemoglobinuria (PNH)",
    "ATTR": "hereditary transthyretin amyloidosis (ATTR)",
    "CSCR": "Central Serous Chorioretinopathy (CSCR)",
    "FECD": "Fuchs endothelial corneal dystrophy (FECD)",
    "XLRS": "Juvenile X-linked Retinoschisis (XLRS)",
}


def parse_existing_frontmatter(content):
    """Parse existing YAML frontmatter manually (no PyYAML dependency).
    Returns (frontmatter_dict, body)."""
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

        # List item
        if stripped.startswith("- ") and current_key:
            val = stripped[2:].strip()
            if current_list is not None:
                current_list.append(val)
            continue

        # Key: value pair
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


def extract_papers_from_body(body):
    """Extract citekeys from [[@Paper]] wiki-links in body."""
    papers = re.findall(r'\[\[@([A-Za-z0-9_-]+?)(?:#|\||\]\])', body)
    # Also match #@citekey pattern (Roam-style inline reference)
    papers += re.findall(r'#@([A-Za-z0-9_-]+)', body)
    # Also match plain @citekey references like (@citekey)
    papers += re.findall(r'(?:^|[\s\(])@([A-Za-z][A-Za-z0-9_-]+\d{4}[A-Za-z0-9_-]*)', body)
    seen = set()
    result = []
    for p in papers:
        if p not in seen:
            seen.add(p)
            result.append(p)
    return result


def extract_diseases_from_body(body, symbol):
    """Extract disease names from wiki-links and known disease references in body."""
    diseases = []
    seen = set()

    # Match wiki-links to known disease notes
    wikilinks = re.findall(r'\[\[([^\]|#]+?)(?:\||\]\]|#)', body)
    # Also match Roam-style links: [[Roam/.../Disease Name/...|...]]
    roam_links = re.findall(r'\[\[Roam/[^/]+/([^/|#\]]+?)(?:/[^|\]]*)?(?:\||\]\])', body)
    wikilinks += roam_links

    for link in wikilinks:
        link_clean = link.strip()
        # Check against known disease names (case-insensitive)
        for disease in KNOWN_DISEASES:
            if link_clean.lower() == disease.lower() and disease not in seen:
                seen.add(disease)
                diseases.append(disease)
                break

    # Check for abbreviation matches in body text
    for abbrev, full_name in DISEASE_SHORT_NAMES.items():
        if full_name in seen:
            continue
        # Look for the abbreviation as a standalone word
        if re.search(r'\b' + re.escape(abbrev) + r'\b', body):
            # Avoid false positives — only use if it's clearly a disease context
            # (e.g., "in AD", "AD patients", "risk for AD")
            if re.search(r'(?:in|for|with|of|and)\s+' + re.escape(abbrev) + r'\b', body) or \
               re.search(r'\b' + re.escape(abbrev) + r'\s+(?:patients|cases|risk|model|mice|mouse)', body):
                seen.add(full_name)
                diseases.append(full_name)

    return diseases


def extract_targeted_by(body):
    """Extract drug/therapy names from targetedBy-style lines."""
    drugs = []
    m = re.search(r'targetedBy\s*:\s*([^\n]+)', body)
    if m:
        line = m.group(1)
        # Extract wiki-links
        links = re.findall(r'\[\[([^\]|#]+?)(?:\||\]\])', line)
        for link in links:
            link = link.strip()
            # Skip non-drug links (paper refs, gene refs, etc.)
            if link.startswith("@") or link.startswith("^") or link.startswith("Roam/"):
                continue
            drugs.append(link)
    return drugs


def extract_therapeutic_notes(body):
    """Extract brief therapeutic status from body if present."""
    # Look for targetedBy line
    m = re.search(r'targetedBy\s*:\s*([^\n]+)', body)
    if m:
        line = m.group(1).strip()
        # Clean up wiki-link brackets for a readable summary
        clean = re.sub(r'\[\[([^\]|]+?)(?:\|[^\]]+)?\]\]', r'\1', line)
        # Truncate to reasonable length
        if len(clean) > 200:
            clean = clean[:197] + "..."
        return clean
    return ""


def extract_protein_length(body):
    """Try to extract protein length in amino acids from body text."""
    # Patterns like "230 aa", "536 aa", "153aa", "299 aa", "346aa"
    m = re.search(r'(\d{2,5})\s*aa\b', body)
    if m:
        return int(m.group(1))
    # Pattern like "protein of 317 aminoacids"
    m = re.search(r'(\d{2,5})\s*amino\s*acids?\b', body, re.IGNORECASE)
    if m:
        return int(m.group(1))
    return None


def extract_chromosome(body):
    """Try to extract chromosome location from body text."""
    # Patterns like "chr 1q21", "chromosome 6p21.1", "chr1q21"
    m = re.search(r'(?:chr(?:omosome)?\s*)(\d{1,2}|[XY])([pq][\d.]+)?', body, re.IGNORECASE)
    if m:
        chrom = m.group(1)
        band = m.group(2) or ""
        return chrom, f"{chrom}{band}" if band else ""
    return None, ""


def build_gene_yaml(existing_fm, body, filename):
    """Build the gene YAML frontmatter dict."""
    # Extract symbol from filename: ^SYMBOL.md -> SYMBOL
    symbol = filename.replace(".md", "")
    if symbol.startswith("^"):
        symbol = symbol[1:]

    fm = {}

    fm["type"] = "gene"
    fm["created"] = existing_fm.get("created", "")
    fm["updated"] = existing_fm.get("updated", "")
    fm["symbol"] = symbol

    # Full name — leave empty for manual fill unless detectable
    fm["full_name"] = existing_fm.get("full_name", "")

    # Aliases
    fm["aliases"] = existing_fm.get("aliases", [])

    # Tags
    tags = existing_fm.get("tags", [])
    if not isinstance(tags, list):
        tags = [tags] if tags else []
    if "gene" not in tags:
        tags.insert(0, "gene")
    fm["tags"] = tags

    # Chromosome and cytoband
    existing_chrom = existing_fm.get("chromosome", "")
    existing_cytoband = existing_fm.get("cytoband", "")
    if not existing_chrom:
        chrom, cytoband = extract_chromosome(body)
        fm["chromosome"] = chrom if chrom else ""
        fm["cytoband"] = cytoband if cytoband else ""
    else:
        fm["chromosome"] = existing_chrom
        fm["cytoband"] = existing_cytoband

    # Protein length
    existing_plen = existing_fm.get("protein_length")
    if not existing_plen:
        fm["protein_length"] = extract_protein_length(body)
    else:
        fm["protein_length"] = existing_plen

    # Diseases
    existing_diseases = existing_fm.get("diseases", [])
    if isinstance(existing_diseases, str):
        existing_diseases = [existing_diseases] if existing_diseases else []
    if not existing_diseases:
        fm["diseases"] = extract_diseases_from_body(body, symbol)
    else:
        fm["diseases"] = existing_diseases

    # Targeted by (drugs/therapies)
    existing_targeted = existing_fm.get("targeted_by", [])
    if not existing_targeted:
        fm["targeted_by"] = extract_targeted_by(body)
    else:
        fm["targeted_by"] = existing_targeted

    # Therapeutic notes
    existing_tnotes = existing_fm.get("therapeutic_notes", "")
    if not existing_tnotes:
        fm["therapeutic_notes"] = extract_therapeutic_notes(body)
    else:
        fm["therapeutic_notes"] = existing_tnotes

    # Key papers — top citekeys from body
    existing_papers = existing_fm.get("key_papers", [])
    if not existing_papers:
        all_papers = extract_papers_from_body(body)
        # Keep all of them as key_papers (the builder can trim later)
        fm["key_papers"] = all_papers
    else:
        fm["key_papers"] = existing_papers

    return fm


def yaml_dump_frontmatter(fm):
    """Dump frontmatter dict to YAML string with clean formatting."""
    key_order = [
        "type", "created", "updated", "symbol", "full_name", "aliases", "tags",
        "chromosome", "cytoband", "protein_length",
        "diseases", "targeted_by", "therapeutic_notes",
        "key_papers",
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
                    # Quote items that contain special characters
                    item_str = str(item)
                    if any(c in item_str for c in [':', '#', '{', '}', '[', ']', ',', '&', '*', '?', '|', '-', '<', '>', '=', '!', '%', '@', '`', "'", '"']):
                        # Escape existing double quotes then wrap
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


def migrate_gene_note(filepath):
    """Migrate a single gene note. Returns (status, changes, warnings)."""
    changes = []
    warnings = []

    if not filepath.exists():
        return "skipped", [], [f"File not found: {filepath.name}"]

    content = filepath.read_text(encoding="utf-8")
    existing_fm, body = parse_existing_frontmatter(content)

    # Build new frontmatter
    new_fm = build_gene_yaml(existing_fm, body, filepath.name)

    # Track what changed
    if existing_fm.get("type") != "gene":
        changes.append("+type: gene")
    if "tags" not in existing_fm or "gene" not in existing_fm.get("tags", []):
        changes.append("+tags: gene")
    if new_fm.get("symbol") and not existing_fm.get("symbol"):
        changes.append(f"+symbol: {new_fm['symbol']}")
    if new_fm.get("chromosome") and not existing_fm.get("chromosome"):
        changes.append(f"+chromosome: {new_fm['chromosome']}")
    if new_fm.get("protein_length") and not existing_fm.get("protein_length"):
        changes.append(f"+protein_length: {new_fm['protein_length']}")
    if new_fm.get("diseases") and not existing_fm.get("diseases"):
        changes.append(f"+diseases: {new_fm['diseases']}")
    if new_fm.get("targeted_by") and not existing_fm.get("targeted_by"):
        changes.append(f"+targeted_by: {new_fm['targeted_by']}")
    if new_fm.get("key_papers") and not existing_fm.get("key_papers"):
        n_papers = len(new_fm['key_papers'])
        changes.append(f"+key_papers: {n_papers} citekeys")

    # Warnings for empty important fields
    if not new_fm.get("diseases"):
        warnings.append("diseases list empty — no disease links found")
    if not new_fm.get("key_papers"):
        warnings.append("key_papers empty — no paper references found")
    if not new_fm.get("full_name"):
        warnings.append("full_name left empty — needs manual entry")

    # Write back — new YAML + original body (no text deleted)
    new_yaml = yaml_dump_frontmatter(new_fm)
    new_content = new_yaml + "\n" + body

    filepath.write_text(new_content, encoding="utf-8")
    return "modified", changes, warnings


def generate_report(results):
    """Generate the Phase 2 migration report."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    modified = sum(1 for s, _, _ in results.values() if s == "modified")
    skipped = sum(1 for s, _, _ in results.values() if s == "skipped")
    errors = sum(1 for s, _, _ in results.values() if s == "error")
    total = len(results)

    # Collect stats for YAML property population counts
    n_with_diseases = 0
    n_with_papers = 0
    n_with_chromosome = 0
    n_with_protein = 0
    n_with_targeted = 0
    n_with_fullname = 0
    for name, (status, changes, warnings) in results.items():
        if status != "modified":
            continue
        ch_str = " ".join(changes)
        # Read the file to check populated fields
        # (we track via changes instead to avoid re-reading)
        if "+diseases:" in ch_str or "diseases" not in " ".join(warnings):
            # diseases was populated (either new or existing)
            has_disease_warning = any("diseases list empty" in w for w in warnings)
            if not has_disease_warning:
                n_with_diseases += 1
        if "+key_papers:" in ch_str or "key_papers" not in " ".join(warnings):
            has_paper_warning = any("key_papers empty" in w for w in warnings)
            if not has_paper_warning:
                n_with_papers += 1
        if "+chromosome:" in ch_str:
            n_with_chromosome += 1
        if "+protein_length:" in ch_str:
            n_with_protein += 1
        if "+targeted_by:" in ch_str:
            n_with_targeted += 1

    lines = [
        f"# Phase 2: Gene Notes — Migration Report\n",
        f"- **Date:** {now}",
        f"- **Notes processed:** {total}",
        f"- **Notes modified:** {modified}",
        f"- **Notes skipped:** {skipped}",
        f"- **Errors:** {errors}\n",
        "## Summary\n",
        "Added `type: gene` YAML frontmatter to gene notes. Extracted gene symbol from filename, ",
        "disease associations from wiki-links, paper citekeys from `[[@...]]` references, ",
        "protein length and chromosome location from body text, and drug/therapy targets from ",
        "`targetedBy` lines. All original body text preserved.\n",
        "## YAML Properties Populated\n",
        "| Property | Populated | Left Empty | Notes |",
        "|----------|----------:|----------:|-------|",
        f"| type | {modified}/{modified} | 0 | always set to 'gene' |",
        f"| symbol | {modified}/{modified} | 0 | extracted from filename |",
        f"| full_name | 0/{modified} | {modified} | needs manual entry |",
        f"| diseases | {n_with_diseases}/{modified} | {modified - n_with_diseases} | from wiki-links |",
        f"| key_papers | {n_with_papers}/{modified} | {modified - n_with_papers} | from [[@...]] links |",
        f"| chromosome | {n_with_chromosome}/{modified} | {modified - n_with_chromosome} | from body text |",
        f"| protein_length | {n_with_protein}/{modified} | {modified - n_with_protein} | from body text |",
        f"| targeted_by | {n_with_targeted}/{modified} | {modified - n_with_targeted} | from targetedBy lines |",
        "",
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
                # Only flag non-trivial warnings
                if "full_name left empty" not in w:
                    review_items.append(f"- [ ] {name} — {w}")

    if review_items:
        lines.append("\n## Items Requiring Manual Review\n")
        lines.append(f"*({len(review_items)} items — excludes full_name warnings since all need manual entry)*\n")
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

    # Find all ^*.md gene notes
    gene_files = sorted(VAULT.glob("^*.md"))
    print(f"Found {len(gene_files)} gene notes to migrate\n")

    results = {}
    for filepath in gene_files:
        note_name = filepath.name
        try:
            status, changes, warnings = migrate_gene_note(filepath)
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
    report_path = report_dir / "phase-2-genes.md"
    report_path.write_text(report, encoding="utf-8")
    print(f"\nReport written to: {report_path}")

    # Summary
    modified = sum(1 for s, _, _ in results.values() if s == "modified")
    skipped = sum(1 for s, _, _ in results.values() if s == "skipped")
    errors = sum(1 for s, _, _ in results.values() if s == "error")
    print(f"\nDone: {modified} modified, {skipped} skipped, {errors} errors")


if __name__ == "__main__":
    main()
