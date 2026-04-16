#!/usr/bin/env python3
"""
Phase 7: Roam Link Repair Script
Repairs broken [[Roam/giov-2026-01-29-19-08-45/...]] links in the gitVault.
No text is deleted — original display aliases preserved. An audit comment
is added at the end of each repaired file.

Categories:
A — Sub-topic links → section links: [[Note#Section|alias]]
B — Paper references → strip Roam prefix: [[@Paper#^blockID|alias]]
C — Daily note references → strip prefix if daily note exists
D — Miscellaneous/non-mappable → leave as-is
"""

import re
from pathlib import Path
from datetime import datetime

VAULT = Path("/Users/giovanni.coppola/Library/CloudStorage/OneDrive-RegeneronPharmaceuticals,Inc/MyScripts/myGitHubRepos/gitVault/gitVault-notes")
DAILY_NOTES = Path("/Users/giovanni.coppola/Library/CloudStorage/OneDrive-RegeneronPharmaceuticals,Inc/MyScripts/myGitHubRepos/gitVault/dailyNotes")
ROAM_PREFIX = "Roam/giov-2026-01-29-19-08-45/"

# Category D: infrastructure targets to leave as-is
CATEGORY_D_PATTERNS = [
    "roam/", "Roam/comments", "Roam/css", "Roam/js", "roam/comments",
    "yaanki/", "DONE", "TODO", "embed",
]


def classify_and_repair_link(target, alias, block_anchor):
    """
    Classify a Roam link and return (new_target, category, note).
    target: path after Roam prefix (e.g., "^APOE/function")
    alias: display text (e.g., "^APOE/function")
    block_anchor: optional #^blockID part
    Returns (new_link_text, category_letter, description)
    """

    # Category B: Paper references (starts with @)
    if target.startswith("@"):
        # Strip Roam prefix, keep the paper note reference + block anchor
        new_target = target
        if block_anchor:
            new_link = f"[[{new_target}{block_anchor}|{alias}]]"
        else:
            new_link = f"[[{new_target}|{alias}]]"
        return new_link, "B", f"paper ref → {new_target}"

    # Category C: Daily note references (YYYY-MM-DD pattern)
    m = re.match(r'^(\d{4}-\d{2}-\d{2})', target)
    if m:
        date_str = m.group(1)
        # Check if daily note exists
        daily_candidates = list(DAILY_NOTES.glob(f"{date_str}*.md")) if DAILY_NOTES.exists() else []
        if daily_candidates:
            daily_name = daily_candidates[0].stem
            if block_anchor:
                new_link = f"[[{daily_name}{block_anchor}|{alias}]]"
            else:
                new_link = f"[[{daily_name}|{alias}]]"
            return new_link, "C", f"daily note → {daily_name}"
        else:
            # Daily note doesn't exist — leave as-is but strip Roam prefix
            if block_anchor:
                new_link = f"[[{target}{block_anchor}|{alias}]]"
            else:
                new_link = f"[[{target}|{alias}]]"
            return new_link, "C", f"daily note (no file found) → {target}"

    # Category D: Infrastructure
    for pat in CATEGORY_D_PATTERNS:
        if pat.lower() in target.lower():
            return None, "D", f"infrastructure: {target}"

    # Category A: Sub-topic links (contains /)
    if "/" in target:
        parts = target.split("/", 1)
        parent = parts[0].strip()
        subtopic = parts[1].strip()

        # Check if parent note exists
        parent_file = VAULT / f"{parent}.md"
        if parent_file.exists():
            # Capitalize subtopic for header matching
            header = subtopic
            # Common header name mappings
            header_map = {
                "function": "Function",
                "therapeutic strategies": "Therapeutic Strategies",
                "therapeutic strategy": "Therapeutic Strategies",
                "biomarkers": "Biomarkers",
                "epidemiology": "Epidemiology",
                "GWAS": "GWAS",
                "genetics": "Genetics",
                "expression": "Expression",
                "mutations": "Mutations & Variants",
                "mouse models": "Mouse Models",
                "mousemodels": "Mouse Models",
                "Mouse models": "Mouse Models",
                "clinical": "Clinical",
                "pathogenesis": "Pathogenesis",
                "Intermediate alleles": "Intermediate alleles",
                "Mechanism": "Mechanism",
                "Christchurch": "Christchurch",
                "esophageal cancer": "esophageal cancer",
                "summary": "summary",
                "Index": "Index",
            }
            mapped_header = header_map.get(header, header_map.get(header.lower(), header))

            if block_anchor:
                new_link = f"[[{parent}#{mapped_header}{block_anchor}|{alias}]]"
            else:
                new_link = f"[[{parent}#{mapped_header}|{alias}]]"
            return new_link, "A", f"sub-topic → {parent}#{mapped_header}"
        else:
            # Parent doesn't exist — try without ^ prefix
            if parent.startswith("^"):
                parent_alt = parent
            else:
                parent_alt = f"^{parent}"
            parent_alt_file = VAULT / f"{parent_alt}.md"
            if parent_alt_file.exists():
                header = subtopic
                header_map = {
                    "function": "Function",
                    "therapeutic strategies": "Therapeutic Strategies",
                    "biomarkers": "Biomarkers",
                    "GWAS": "GWAS",
                    "expression": "Expression",
                    "mutations": "Mutations & Variants",
                    "mouse models": "Mouse Models",
                    "Mouse models": "Mouse Models",
                    "Intermediate alleles": "Intermediate alleles",
                    "Mechanism": "Mechanism",
                    "Christchurch": "Christchurch",
                }
                mapped_header = header_map.get(subtopic, header_map.get(subtopic.lower(), subtopic))
                if block_anchor:
                    new_link = f"[[{parent_alt}#{mapped_header}{block_anchor}|{alias}]]"
                else:
                    new_link = f"[[{parent_alt}#{mapped_header}|{alias}]]"
                return new_link, "A", f"sub-topic → {parent_alt}#{mapped_header}"

            # Parent still not found — leave as-is
            return None, "A-unresolved", f"parent not found: {parent}"

    # Simple target without / — just strip Roam prefix
    target_file = VAULT / f"{target}.md"
    if target_file.exists():
        if block_anchor:
            new_link = f"[[{target}{block_anchor}|{alias}]]"
        else:
            new_link = f"[[{target}|{alias}]]"
        return new_link, "A", f"simple → {target}"

    return None, "D", f"unresolvable: {target}"


def repair_file(filepath):
    """Repair all Roam links in a file. Returns (n_repaired, n_left, categories)."""
    content = filepath.read_text(encoding="utf-8")

    # Pattern to match [[Roam/giov-2026-01-29-19-08-45/target#^blockID|alias]]
    # or [[Roam/giov-2026-01-29-19-08-45/target|alias]]
    pattern = re.compile(
        r'\[\[Roam/giov-2026-01-29-19-08-45/([^\]#|]+?)'  # target
        r'(#\^[A-Za-z0-9_-]+)?'                            # optional block anchor
        r'\|([^\]]+?)\]\]'                                  # |alias]]
    )

    repairs = []
    left_alone = []

    def replace_match(m):
        target = m.group(1).strip()
        block_anchor = m.group(2) or ""
        alias = m.group(3)

        new_link, category, desc = classify_and_repair_link(target, alias, block_anchor)

        if new_link:
            repairs.append((category, desc))
            return new_link
        else:
            left_alone.append((category, desc))
            return m.group(0)  # Leave unchanged

    new_content = pattern.sub(replace_match, content)

    # Also handle links without alias: [[Roam/giov-2026-01-29-19-08-45/target]]
    pattern_no_alias = re.compile(
        r'\[\[Roam/giov-2026-01-29-19-08-45/([^\]#|]+?)'
        r'(#\^[A-Za-z0-9_-]+)?'
        r'\]\]'
    )

    def replace_no_alias(m):
        target = m.group(1).strip()
        block_anchor = m.group(2) or ""
        alias = target  # Use target as alias

        new_link, category, desc = classify_and_repair_link(target, alias, block_anchor)

        if new_link:
            repairs.append((category, desc))
            return new_link
        else:
            left_alone.append((category, desc))
            return m.group(0)

    new_content = pattern_no_alias.sub(replace_no_alias, new_content)

    # Add audit comment if any repairs were made
    if repairs:
        audit = f"\n<!-- QAK link repair: {len(repairs)} Roam links repaired on {datetime.now().strftime('%Y-%m-%d')} -->\n"
        new_content = new_content.rstrip() + audit

    if new_content != content:
        filepath.write_text(new_content, encoding="utf-8")

    # Collect category stats
    categories = {}
    for cat, _ in repairs + left_alone:
        categories[cat] = categories.get(cat, 0) + 1

    return len(repairs), len(left_alone), categories, repairs, left_alone


def generate_report(results):
    """Generate the Phase 7 migration report."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    total_files = len(results)
    files_repaired = sum(1 for r in results.values() if r[0] > 0)
    total_repaired = sum(r[0] for r in results.values())
    total_left = sum(r[1] for r in results.values())

    # Aggregate categories
    all_cats = {}
    for _, _, cats, _, _ in results.values():
        for cat, count in cats.items():
            all_cats[cat] = all_cats.get(cat, 0) + count

    lines = [
        f"# Phase 7: Roam Link Repair — Migration Report\n",
        f"- **Date:** {now}",
        f"- **Files scanned:** {total_files}",
        f"- **Files with repairs:** {files_repaired}",
        f"- **Total links repaired:** {total_repaired}",
        f"- **Total links left as-is:** {total_left}\n",
        "## Summary\n",
        "Repaired broken `[[Roam/giov-2026-01-29-19-08-45/...]]` links across the vault. ",
        "Category A (sub-topic) links rewritten as section links (`[[Note#Header|alias]]`). ",
        "Category B (paper) links had Roam prefix stripped. Category C (daily notes) stripped where target exists. ",
        "Category D (infrastructure/unresolvable) left as-is. Audit comments added to repaired files.\n",
        "## Category Breakdown\n",
        "| Category | Count | Description |",
        "|----------|------:|-------------|",
    ]
    cat_descriptions = {
        "A": "Sub-topic → section link",
        "A-unresolved": "Sub-topic — parent not found",
        "B": "Paper reference — prefix stripped",
        "C": "Daily note reference",
        "D": "Infrastructure/unresolvable — left as-is",
    }
    for cat in ["A", "B", "C", "D", "A-unresolved"]:
        if cat in all_cats:
            lines.append(f"| {cat} | {all_cats[cat]} | {cat_descriptions.get(cat, '')} |")

    lines += [
        "",
        "## Per-File Summary\n",
        "| File | Repaired | Left | Categories |",
        "|------|----------:|-----:|------------|",
    ]

    for name in sorted(results.keys()):
        n_rep, n_left, cats, _, _ = results[name]
        if n_rep > 0 or n_left > 0:
            cat_str = ", ".join(f"{cat}:{count}" for cat, count in sorted(cats.items()))
            lines.append(f"| {name} | {n_rep} | {n_left} | {cat_str} |")

    # Unresolved links
    unresolved = []
    for name, (_, _, _, _, left) in results.items():
        for cat, desc in left:
            if cat in ["A-unresolved", "D"]:
                unresolved.append(f"- {name}: [{cat}] {desc}")

    if unresolved:
        lines.append(f"\n## Unresolved Links ({len(unresolved)} items)\n")
        lines.extend(unresolved[:100])
        if len(unresolved) > 100:
            lines.append(f"\n... and {len(unresolved) - 100} more")

    return "\n".join(lines)


def main():
    report_dir = Path("/Users/giovanni.coppola/Library/CloudStorage/OneDrive-RegeneronPharmaceuticals,Inc/MyScripts/myGitHubRepos/QAK/reports")
    report_dir.mkdir(exist_ok=True)

    # Find all files with Roam links
    candidates = []
    for f in VAULT.glob("*.md"):
        try:
            content = f.read_text(encoding="utf-8")
            if ROAM_PREFIX in content:
                candidates.append(f)
        except Exception:
            pass

    print(f"Found {len(candidates)} files with Roam links to process\n")

    results = {}
    for filepath in sorted(candidates):
        name = filepath.name
        try:
            n_rep, n_left, cats, repairs, left = repair_file(filepath)
            results[name] = (n_rep, n_left, cats, repairs, left)
            if n_rep > 0:
                print(f"  repaired {n_rep:>3}, left {n_left:>2}  {name}")
            else:
                print(f"  no change        left {n_left:>2}  {name}")
        except Exception as e:
            results[name] = (0, 0, {}, [], [])
            print(f"     error  {name}: {e}")

    report = generate_report(results)
    report_path = report_dir / "phase-7-roam-links.md"
    report_path.write_text(report, encoding="utf-8")
    print(f"\nReport written to: {report_path}")

    total_repaired = sum(r[0] for r in results.values())
    total_left = sum(r[1] for r in results.values())
    files_repaired = sum(1 for r in results.values() if r[0] > 0)
    print(f"\nDone: {total_repaired} links repaired across {files_repaired} files, {total_left} left as-is")


if __name__ == "__main__":
    main()
