#!/usr/bin/env python3
"""
Phase 9a: Write AI-generated summaries to paper notes.
Reads summaries from /tmp/ai_summaries.jsonl and writes them to the vault.
Each entry: {"filename": "@Paper.md", "summary": "..."}

Adds:
- # OBSummary_AI header + summary text at end of note
- obs_source: "ai" in YAML frontmatter
"""

import json
import re
from pathlib import Path
from datetime import datetime

VAULT = Path("/Users/giovanni.coppola/Library/CloudStorage/OneDrive-RegeneronPharmaceuticals,Inc/MyScripts/myGitHubRepos/gitVault/gitVault-notes")
SUMMARIES_FILE = Path("/tmp/ai_summaries.jsonl")


def apply_summary(filepath, summary):
    """Apply an AI summary to a paper note file."""
    content = filepath.read_text(encoding="utf-8")

    # Update obs_source in YAML frontmatter
    content = re.sub(r'^obs_source:\s*$', 'obs_source: "ai"', content, count=1, flags=re.MULTILINE)
    content = re.sub(r'^obs_source: \n', 'obs_source: "ai"\n', content, count=1, flags=re.MULTILINE)

    # Append OBSummary_AI at end of file
    summary_block = f"\n\n# OBSummary_AI\n{summary}\n"
    content = content.rstrip() + summary_block

    filepath.write_text(content, encoding="utf-8")


def main():
    if not SUMMARIES_FILE.exists():
        print(f"Error: {SUMMARIES_FILE} not found")
        return

    summaries = []
    with open(SUMMARIES_FILE) as fh:
        for line in fh:
            line = line.strip()
            if line:
                summaries.append(json.loads(line))

    print(f"Loaded {len(summaries)} summaries\n")

    applied = 0
    skipped = 0
    errors = 0

    for entry in summaries:
        filename = entry["filename"]
        summary = entry.get("summary", "").strip()

        if not summary:
            skipped += 1
            continue

        filepath = VAULT / filename
        if not filepath.exists():
            print(f"  SKIP  {filename} — file not found")
            skipped += 1
            continue

        try:
            apply_summary(filepath, summary)
            applied += 1
            if applied <= 10 or applied % 50 == 0:
                print(f"  OK    {filename} ({len(summary)} chars)")
        except Exception as e:
            print(f"  ERR   {filename} — {e}")
            errors += 1

    print(f"\nDone: {applied} applied, {skipped} skipped, {errors} errors")


if __name__ == "__main__":
    main()
