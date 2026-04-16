#!/usr/bin/env python3
"""
Phase 6: Zettel Note Migration Script
Adds YAML frontmatter to z-prefixed zettel notes in the gitVault.
No text is deleted — only YAML properties are added/updated.
Body content left untouched — no headers added.
"""

import re
from pathlib import Path
from datetime import datetime

VAULT = Path("/Users/giovanni.coppola/Library/CloudStorage/OneDrive-RegeneronPharmaceuticals,Inc/MyScripts/myGitHubRepos/gitVault/gitVault-notes")

# Category keywords for auto-classification
CATEGORY_KEYWORDS = {
    "epidemiology": ["prevalence", "incidence", "cases", "patients", "population", "enrollment", "aged", "older"],
    "genetics": ["frequency", "allelic", "carriers", "homozygotes", "mutations", "variant", "HLA", "APOE", "allele", "epistasis", "GBA", "OR "],
    "mechanism": ["mechanism", "gain of function", "aggregation", "pathway", "express", "microglia", "astrocytes", "activated"],
    "pharmacology": ["antibodies", "administered", "brain", "drug", "therapy", "therapeutic"],
    "clinical": ["IOP", "CDR", "MMSE", "diagnosis", "clinical", "UKB", "hearing loss"],
}

# Disease name patterns for matching
DISEASE_PATTERNS = {
    "AMD": "AMD",
    "macular degeneration": "AMD",
    "Alzheimer": "Alzheimer's Disease",
    "AD ": "Alzheimer's Disease",
    "Parkinson": "Parkinson's Disease",
    "PD ": "Parkinson's Disease",
    "glaucoma": "Glaucoma",
    "Glaucoma": "Glaucoma",
    "ALS": "ALS",
    "Multiple Sclerosis": "Multiple Sclerosis",
    "Multiple System Atrophy": "Multiple System Atrophy",
    "MSA": "Multiple System Atrophy",
    "FTD": "Frontotemporal Dementia",
    "frontotemporal": "Frontotemporal Dementia",
    "Ankylosing Spondylitis": "Ankylosing Spondylitis",
    "MCI": "MCI",
    "hearing loss": "Hearing loss",
    "Juvenile Open-Angle Glaucoma": "Juvenile Open-Angle Glaucoma",
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


def extract_fact(filename):
    """Extract the fact text from filename (strip 'z ' prefix and '.md' suffix)."""
    name = filename
    if name.endswith(".md"):
        name = name[:-3]
    if name.startswith("z "):
        name = name[2:]
    return name


def classify_category(fact_text):
    """Auto-assign category based on keyword matching."""
    text_lower = fact_text.lower()
    scores = {}
    for cat, keywords in CATEGORY_KEYWORDS.items():
        score = sum(1 for kw in keywords if kw.lower() in text_lower)
        if score > 0:
            scores[cat] = score

    if scores:
        return max(scores, key=scores.get)
    return "other"


def extract_diseases(fact_text, body):
    """Extract disease names from fact text and body."""
    diseases = []
    seen = set()
    combined = fact_text + " " + body

    for pattern, canonical in DISEASE_PATTERNS.items():
        if pattern in combined and canonical not in seen:
            seen.add(canonical)
            diseases.append(canonical)

    return diseases


def extract_genes(fact_text, body):
    """Extract gene names from fact text and body."""
    genes = []
    seen = set()
    combined = fact_text + " " + body

    # Match #^GENE pattern (Roam-style inline gene reference)
    for g in re.findall(r'#\^([A-Za-z0-9_]+)', combined):
        if g not in seen:
            seen.add(g)
            genes.append(g)

    # Match [[^GENE]] wiki-links
    for g in re.findall(r'\[\[\^([A-Za-z0-9_]+?)(?:\||\]\])', combined):
        if g not in seen:
            seen.add(g)
            genes.append(g)

    # Match well-known gene symbols in fact text
    gene_patterns = ["MYOC", "APOE", "APOE2", "APOE4", "GBA", "HLA-B27", "ERAP1", "SOD1", "C9orf72"]
    for gp in gene_patterns:
        if gp in fact_text and gp not in seen:
            seen.add(gp)
            genes.append(gp)

    return genes


def extract_papers(body):
    """Extract paper citekeys from body content."""
    papers = []
    seen = set()

    # Match #@citekey pattern
    for p in re.findall(r'#@([A-Za-z0-9_-]+)', body):
        if p not in seen:
            seen.add(p)
            papers.append(p)

    # Match [[@citekey]] links
    for p in re.findall(r'\[\[@([A-Za-z0-9_-]+?)(?:#|\||\]\])', body):
        if p not in seen:
            seen.add(p)
            papers.append(p)

    return papers


def build_zettel_yaml(existing_fm, body, filename):
    """Build the zettel YAML frontmatter dict."""
    fact = extract_fact(filename)

    fm = {}
    fm["type"] = "zettel"
    fm["created"] = existing_fm.get("created", "")
    fm["updated"] = existing_fm.get("updated", "")

    tags = existing_fm.get("tags", [])
    if not isinstance(tags, list):
        tags = [tags] if tags else []
    if "zettel" not in tags:
        tags.insert(0, "zettel")
    fm["tags"] = tags

    fm["fact"] = fact
    fm["diseases"] = existing_fm.get("diseases", extract_diseases(fact, body))
    fm["genes"] = existing_fm.get("genes", extract_genes(fact, body))
    fm["papers"] = existing_fm.get("papers", extract_papers(body))
    fm["category"] = existing_fm.get("category", classify_category(fact))

    return fm


def yaml_dump_frontmatter(fm):
    """Dump frontmatter dict to YAML string."""
    key_order = ["type", "created", "updated", "tags", "fact", "diseases", "genes", "papers", "category"]
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


def migrate_zettel_note(filepath):
    """Migrate a single zettel note."""
    changes = []
    warnings = []

    content = filepath.read_text(encoding="utf-8")
    existing_fm, body = parse_existing_frontmatter(content)

    new_fm = build_zettel_yaml(existing_fm, body, filepath.name)

    if existing_fm.get("type") != "zettel":
        changes.append("+type: zettel")
    changes.append(f"+fact (len={len(new_fm['fact'])})")
    changes.append(f"+category: {new_fm['category']}")
    if new_fm.get("diseases"):
        changes.append(f"+diseases: {new_fm['diseases']}")
    if new_fm.get("genes"):
        changes.append(f"+genes: {new_fm['genes']}")

    if not new_fm.get("diseases"):
        warnings.append("diseases empty")

    new_yaml = yaml_dump_frontmatter(new_fm)
    new_content = new_yaml + "\n" + body

    filepath.write_text(new_content, encoding="utf-8")
    return "modified", changes, warnings


def generate_report(results):
    """Generate the Phase 6 migration report."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    modified = sum(1 for s, _, _ in results.values() if s == "modified")
    skipped = sum(1 for s, _, _ in results.values() if s == "skipped")
    errors = sum(1 for s, _, _ in results.values() if s == "error")

    # Category distribution
    categories = {}
    for name, (status, changes, _) in results.items():
        if status == "modified":
            for c in changes:
                if c.startswith("+category:"):
                    cat = c.split(": ", 1)[1]
                    categories[cat] = categories.get(cat, 0) + 1

    lines = [
        f"# Phase 6: Zettel Notes — Migration Report\n",
        f"- **Date:** {now}",
        f"- **Notes processed:** {len(results)}",
        f"- **Notes modified:** {modified}",
        f"- **Notes skipped:** {skipped}",
        f"- **Errors:** {errors}\n",
        "## Summary\n",
        "Added `type: zettel` YAML frontmatter to zettel notes. Extracted fact text from filename, ",
        "inferred diseases and genes from fact content, assigned category by keyword matching. ",
        "Body content left untouched — no headers added.\n",
        "## Category Distribution\n",
        "| Category | Count |",
        "|----------|------:|",
    ]
    for cat, count in sorted(categories.items(), key=lambda x: -x[1]):
        lines.append(f"| {cat} | {count} |")

    lines += [
        "",
        "## Changes by Note\n",
        "| Note | Status | Changes | Warnings |",
        "|------|--------|---------|----------|",
    ]

    for name, (status, changes, warnings) in sorted(results.items()):
        ch = "; ".join(changes) if changes else "—"
        wr = "; ".join(warnings) if warnings else "—"
        lines.append(f"| {name} | {status} | {ch} | {wr} |")

    return "\n".join(lines)


def main():
    report_dir = Path("/Users/giovanni.coppola/Library/CloudStorage/OneDrive-RegeneronPharmaceuticals,Inc/MyScripts/myGitHubRepos/QAK/reports")
    report_dir.mkdir(exist_ok=True)

    zettel_files = sorted(VAULT.glob("z *.md"))
    print(f"Found {len(zettel_files)} zettel notes to migrate\n")

    results = {}
    for filepath in zettel_files:
        note_name = filepath.name
        try:
            status, changes, warnings = migrate_zettel_note(filepath)
            results[note_name] = (status, changes, warnings)
            print(f"  {status:>8}  {note_name[:60]}...  cat={[c for c in changes if c.startswith('+category')][0] if any(c.startswith('+category') for c in changes) else '?'}")
        except Exception as e:
            results[note_name] = ("error", [], [str(e)])
            print(f"  {'error':>8}  {note_name[:60]}...  {e}")

    report = generate_report(results)
    report_path = report_dir / "phase-6-zettels.md"
    report_path.write_text(report, encoding="utf-8")
    print(f"\nReport written to: {report_path}")

    modified = sum(1 for s, _, _ in results.values() if s == "modified")
    errors = sum(1 for s, _, _ in results.values() if s == "error")
    print(f"\nDone: {modified} modified, {errors} errors")


if __name__ == "__main__":
    main()
