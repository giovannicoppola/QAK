#!/usr/bin/env python3
"""
Phase 8: Index Note Migration Script
Adds YAML frontmatter to index/table-of-contents notes in the gitVault.
No text is deleted. No body restructuring — index stays as-is.
"""

import re
from pathlib import Path
from datetime import datetime

VAULT = Path("/Users/giovanni.coppola/Library/CloudStorage/OneDrive-RegeneronPharmaceuticals,Inc/MyScripts/myGitHubRepos/gitVault/gitVault-notes")

# Index notes — manually curated list
INDEX_NOTES = [
    ("Alzheimer's  Index.md", "Alzheimer's Disease", "disease"),
    ("Parkinson's Disease Index.md", "Parkinson's Disease", "disease"),
    ("Huntington's Disease – Index.md", "Huntington's Disease (HD)", "disease"),
    ("APOE index.md", "APOE", "gene"),
    ("APP index.md", "APP", "gene"),
    ("tau – index.md", "tau/MAPT", "gene"),
    ("Hearing loss – index.md", "Hearing loss", "disease"),
    ("Multiple sclerosis - index.md", "Multiple Sclerosis", "disease"),
    ("diabetic retinopathy index.md", "diabetic retinopathy", "disease"),
    ("Examples – index.md", "Examples", "misc"),
    # Note: "Cognitive Function Index (CFI).md" is a clinical instrument, NOT a navigation index
]


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


def build_index_yaml(existing_fm, subject, subject_type):
    """Build the index YAML frontmatter dict."""
    fm = {}
    fm["type"] = "index"
    fm["created"] = existing_fm.get("created", "")
    fm["updated"] = existing_fm.get("updated", "")

    tags = existing_fm.get("tags", [])
    if not isinstance(tags, list):
        tags = [tags] if tags else []
    if "index" not in tags:
        tags.insert(0, "index")
    fm["tags"] = tags

    fm["subject"] = subject
    fm["subject_type"] = subject_type

    return fm


def yaml_dump_frontmatter(fm):
    """Dump frontmatter dict to YAML string."""
    key_order = ["type", "created", "updated", "tags", "subject", "subject_type"]
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
                lines.append(f"{key}:")
                for item in val:
                    lines.append(f"  - {item}")
            elif val is None or val == "":
                lines.append(f"{key}: ")
            else:
                lines.append(f"{key}: {val}")

    return "---\n" + "\n".join(lines) + "\n---"


def migrate_index_note(filepath, subject, subject_type):
    """Migrate a single index note."""
    changes = []
    warnings = []

    if not filepath.exists():
        return "skipped", [], [f"File not found: {filepath.name}"]

    content = filepath.read_text(encoding="utf-8")
    existing_fm, body = parse_existing_frontmatter(content)

    new_fm = build_index_yaml(existing_fm, subject, subject_type)

    if existing_fm.get("type") != "index":
        changes.append("+type: index")
    changes.append(f"+subject: {subject}")
    changes.append(f"+subject_type: {subject_type}")

    new_yaml = yaml_dump_frontmatter(new_fm)
    new_content = new_yaml + "\n" + body

    filepath.write_text(new_content, encoding="utf-8")
    return "modified", changes, warnings


def main():
    report_dir = Path("/Users/giovanni.coppola/Library/CloudStorage/OneDrive-RegeneronPharmaceuticals,Inc/MyScripts/myGitHubRepos/QAK/reports")
    report_dir.mkdir(exist_ok=True)

    print(f"Processing {len(INDEX_NOTES)} index notes\n")

    results = {}
    for note_name, subject, subject_type in INDEX_NOTES:
        filepath = VAULT / note_name
        try:
            status, changes, warnings = migrate_index_note(filepath, subject, subject_type)
            results[note_name] = (status, changes, warnings)
            print(f"  {status:>8}  {note_name}  subject={subject}")
        except Exception as e:
            results[note_name] = ("error", [], [str(e)])
            print(f"  {'error':>8}  {note_name}  {e}")

    # Report
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    modified = sum(1 for s, _, _ in results.values() if s == "modified")
    skipped = sum(1 for s, _, _ in results.values() if s == "skipped")
    errors = sum(1 for s, _, _ in results.values() if s == "error")

    lines = [
        f"# Phase 8: Index Notes — Migration Report\n",
        f"- **Date:** {now}",
        f"- **Notes processed:** {len(results)}",
        f"- **Notes modified:** {modified}",
        f"- **Notes skipped:** {skipped}",
        f"- **Errors:** {errors}\n",
        "## Summary\n",
        "Added `type: index` YAML frontmatter to index/table-of-contents notes. ",
        "Set subject and subject_type for each. No body restructuring — indexes stay as-is.\n",
        "## Changes by Note\n",
        "| Note | Status | Subject | Subject Type | Warnings |",
        "|------|--------|---------|--------------|----------|",
    ]

    for name, (status, changes, warnings) in sorted(results.items()):
        subj = next((c.split(": ", 1)[1] for c in changes if c.startswith("+subject:") and "type" not in c), "—")
        stype = next((c.split(": ", 1)[1] for c in changes if c.startswith("+subject_type:")), "—")
        wr = "; ".join(warnings) if warnings else "—"
        lines.append(f"| {name} | {status} | {subj} | {stype} | {wr} |")

    report = "\n".join(lines)
    report_path = report_dir / "phase-8-indexes.md"
    report_path.write_text(report, encoding="utf-8")
    print(f"\nReport written to: {report_path}")
    print(f"\nDone: {modified} modified, {skipped} skipped, {errors} errors")


if __name__ == "__main__":
    main()
