#!/usr/bin/env python3
"""
Phase 9b: QAK SQLite Builder
Parses YAML frontmatter from all typed notes in the gitVault and produces qak.db.

Tables: diseases, genes, papers, clinical_trials, therapeutic_strategies, zettels, indexes
Junction tables: disease_gene, disease_paper, gene_paper, disease_strategy, strategy_gene,
                 disease_trial, trial_gene, disease_zettel, zettel_gene, zettel_paper
"""

import re
import sqlite3
from pathlib import Path
from datetime import datetime

VAULT = Path("/Users/giovanni.coppola/Library/CloudStorage/OneDrive-RegeneronPharmaceuticals,Inc/MyScripts/myGitHubRepos/gitVault/gitVault-notes")
DB_PATH = Path("/Users/giovanni.coppola/Library/CloudStorage/OneDrive-RegeneronPharmaceuticals,Inc/MyScripts/myGitHubRepos/QAK/qak.db")
TSUNDO_DB = Path("/Users/giovanni.coppola/Library/CloudStorage/OneDrive-RegeneronPharmaceuticals,Inc/MyScripts/myGitHubRepos/tsundo/library.db")


# ---------------------------------------------------------------------------
# YAML parser (no PyYAML available)
# ---------------------------------------------------------------------------

def parse_frontmatter(content):
    """Parse YAML frontmatter from markdown content. Returns (dict, body)."""
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
            val = stripped[2:].strip().strip('"').strip("'")
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


def extract_obs_summary(body):
    """Extract the OBSummary_AI or #obs summary from body text."""
    # Try AI summary first
    m = re.search(r'# OBSummary_AI\n(.+?)(?:\n#|\Z)', body, re.DOTALL)
    if m:
        return m.group(1).strip()
    return ""


def s(val):
    """Coerce a value to string or None for SQLite."""
    if val is None or val == "" or val == []:
        return None
    if isinstance(val, list):
        return ", ".join(str(v) for v in val)
    return str(val)


def n(val):
    """Coerce a value to number or None for SQLite."""
    if val is None or val == "":
        return None
    if isinstance(val, (int, float)):
        return val
    try:
        return int(val)
    except (ValueError, TypeError):
        try:
            return float(val)
        except (ValueError, TypeError):
            return None


# ---------------------------------------------------------------------------
# Schema
# ---------------------------------------------------------------------------

SCHEMA = """
CREATE TABLE IF NOT EXISTS diseases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    filename TEXT,
    created TEXT,
    updated TEXT,
    prevalence_per_100k REAL,
    incidence_per_100k REAL,
    n_patients_us INTEGER,
    lifetime_risk TEXT,
    omim TEXT,
    mondo TEXT,
    orphanet TEXT,
    gwas_largest_n INTEGER,
    gwas_loci INTEGER,
    gwas_paper TEXT,
    wes_largest_n INTEGER,
    wes_loci INTEGER,
    wes_paper TEXT,
    heritability_twin TEXT,
    heritability_gwas TEXT,
    prevalence_by_age TEXT,
    incidence_by_age TEXT,
    disease_duration REAL
);

CREATE TABLE IF NOT EXISTS genes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol TEXT UNIQUE NOT NULL,
    filename TEXT,
    created TEXT,
    updated TEXT,
    full_name TEXT,
    chromosome TEXT,
    cytoband TEXT,
    protein_length INTEGER,
    therapeutic_notes TEXT
);

CREATE TABLE IF NOT EXISTS papers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    citekey TEXT UNIQUE NOT NULL,
    filename TEXT,
    created TEXT,
    updated TEXT,
    title TEXT,
    study_type TEXT,
    first_author TEXT,
    year INTEGER,
    journal TEXT,
    n_cases INTEGER,
    n_controls INTEGER,
    n_total INTEGER,
    n_loci INTEGER,
    obs_summary TEXT,
    obs_source TEXT,
    abstract TEXT,
    distinction TEXT
);

CREATE TABLE IF NOT EXISTS clinical_trials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    trial_name TEXT NOT NULL,
    filename TEXT,
    created TEXT,
    updated TEXT,
    nct_id TEXT,
    clinicaltrials_url TEXT,
    phase TEXT,
    status TEXT,
    outcome TEXT,
    drug TEXT,
    modality TEXT,
    dose TEXT,
    company TEXT,
    indication_detail TEXT,
    n_enrolled INTEGER,
    primary_endpoint TEXT,
    duration TEXT,
    estimated_completion TEXT,
    therapeutic_strategy TEXT,
    results_paper TEXT
);

CREATE TABLE IF NOT EXISTS therapeutic_strategies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    filename TEXT,
    created TEXT,
    updated TEXT,
    modality TEXT
);

CREATE TABLE IF NOT EXISTS zettels (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fact TEXT NOT NULL,
    filename TEXT,
    created TEXT,
    updated TEXT,
    category TEXT
);

CREATE TABLE IF NOT EXISTS indexes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT NOT NULL,
    filename TEXT,
    created TEXT,
    updated TEXT,
    subject_type TEXT
);

-- Junction tables

CREATE TABLE IF NOT EXISTS disease_gene (
    disease_id INTEGER REFERENCES diseases(id),
    gene_id INTEGER REFERENCES genes(id),
    PRIMARY KEY (disease_id, gene_id)
);

CREATE TABLE IF NOT EXISTS disease_paper (
    disease_id INTEGER REFERENCES diseases(id),
    paper_id INTEGER REFERENCES papers(id),
    PRIMARY KEY (disease_id, paper_id)
);

CREATE TABLE IF NOT EXISTS gene_paper (
    gene_id INTEGER REFERENCES genes(id),
    paper_id INTEGER REFERENCES papers(id),
    PRIMARY KEY (gene_id, paper_id)
);

CREATE TABLE IF NOT EXISTS disease_strategy (
    disease_id INTEGER REFERENCES diseases(id),
    strategy_id INTEGER REFERENCES therapeutic_strategies(id),
    PRIMARY KEY (disease_id, strategy_id)
);

CREATE TABLE IF NOT EXISTS strategy_gene (
    strategy_id INTEGER REFERENCES therapeutic_strategies(id),
    gene_id INTEGER REFERENCES genes(id),
    PRIMARY KEY (strategy_id, gene_id)
);

CREATE TABLE IF NOT EXISTS disease_trial (
    disease_id INTEGER REFERENCES diseases(id),
    trial_id INTEGER REFERENCES clinical_trials(id),
    PRIMARY KEY (disease_id, trial_id)
);

CREATE TABLE IF NOT EXISTS trial_gene (
    trial_id INTEGER REFERENCES clinical_trials(id),
    gene_id INTEGER REFERENCES genes(id),
    PRIMARY KEY (trial_id, gene_id)
);

CREATE TABLE IF NOT EXISTS disease_zettel (
    disease_id INTEGER REFERENCES diseases(id),
    zettel_id INTEGER REFERENCES zettels(id),
    PRIMARY KEY (disease_id, zettel_id)
);

CREATE TABLE IF NOT EXISTS zettel_gene (
    zettel_id INTEGER REFERENCES zettels(id),
    gene_id INTEGER REFERENCES genes(id),
    PRIMARY KEY (zettel_id, gene_id)
);

CREATE TABLE IF NOT EXISTS zettel_paper (
    zettel_id INTEGER REFERENCES zettels(id),
    paper_id INTEGER REFERENCES papers(id),
    PRIMARY KEY (zettel_id, paper_id)
);

-- Metadata
CREATE TABLE IF NOT EXISTS qak_meta (
    key TEXT PRIMARY KEY,
    value TEXT
);
"""


# ---------------------------------------------------------------------------
# Builders
# ---------------------------------------------------------------------------

def build_db():
    """Parse vault and build SQLite database."""
    if DB_PATH.exists():
        DB_PATH.unlink()

    conn = sqlite3.connect(str(DB_PATH))
    conn.executescript(SCHEMA)

    # Collect all typed notes
    notes = {}  # type -> list of (filename, fm, body)
    for f in sorted(VAULT.glob("*.md")):
        try:
            content = f.read_text(encoding="utf-8")
        except Exception:
            continue
        fm, body = parse_frontmatter(content)
        note_type = fm.get("type", "")
        if note_type:
            notes.setdefault(note_type, []).append((f.name, fm, body))

    # Lookup caches: name -> id
    disease_ids = {}
    gene_ids = {}
    paper_ids = {}
    strategy_ids = {}
    trial_ids = {}
    zettel_ids = {}

    # ---- Diseases ----
    for filename, fm, body in notes.get("disease", []):
        name = filename.replace(".md", "")
        conn.execute(
            """INSERT INTO diseases (name, filename, created, updated,
               prevalence_per_100k, incidence_per_100k, n_patients_us, lifetime_risk,
               omim, mondo, orphanet,
               gwas_largest_n, gwas_loci, gwas_paper,
               wes_largest_n, wes_loci, wes_paper,
               heritability_twin, heritability_gwas,
               prevalence_by_age, incidence_by_age, disease_duration)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (name, filename, s(fm.get("created")), s(fm.get("updated")),
             n(fm.get("prevalence_per_100k")), n(fm.get("incidence_per_100k")),
             n(fm.get("n_patients_us")), s(fm.get("lifetime_risk")),
             s(fm.get("omim")), s(fm.get("mondo")), s(fm.get("orphanet")),
             n(fm.get("gwas_largest_n")), n(fm.get("gwas_loci")), s(fm.get("gwas_paper")),
             n(fm.get("wes_largest_n")), n(fm.get("wes_loci")), s(fm.get("wes_paper")),
             s(fm.get("heritability_twin")), s(fm.get("heritability_gwas")),
             s(fm.get("prevalence_by_age")), s(fm.get("incidence_by_age")),
             n(fm.get("disease_duration")))
        )
        disease_ids[name] = conn.execute("SELECT last_insert_rowid()").fetchone()[0]

    print(f"  diseases:    {len(disease_ids)}")

    # ---- Genes ----
    for filename, fm, body in notes.get("gene", []):
        symbol = fm.get("symbol", filename.replace(".md", "").lstrip("^"))
        conn.execute(
            """INSERT INTO genes (symbol, filename, created, updated,
               full_name, chromosome, cytoband, protein_length, therapeutic_notes)
               VALUES (?,?,?,?,?,?,?,?,?)""",
            (symbol, filename, s(fm.get("created")), s(fm.get("updated")),
             s(fm.get("full_name")), s(fm.get("chromosome")), s(fm.get("cytoband")),
             n(fm.get("protein_length")), s(fm.get("therapeutic_notes")))
        )
        gene_ids[symbol] = conn.execute("SELECT last_insert_rowid()").fetchone()[0]

    print(f"  genes:       {len(gene_ids)}")

    # ---- Papers ----
    for filename, fm, body in notes.get("paper", []):
        citekey = fm.get("citekey", filename.replace(".md", "").lstrip("@"))
        obs_summary = extract_obs_summary(body) or s(fm.get("obs_summary"))
        conn.execute(
            """INSERT INTO papers (citekey, filename, created, updated,
               title, study_type, first_author, year, journal,
               n_cases, n_controls, n_total, n_loci,
               obs_summary, obs_source)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (citekey, filename, s(fm.get("created")), s(fm.get("updated")),
             s(fm.get("title")), s(fm.get("study_type")),
             s(fm.get("first_author")), n(fm.get("year")), s(fm.get("journal")),
             n(fm.get("n_cases")), n(fm.get("n_controls")),
             n(fm.get("n_total")), n(fm.get("n_loci")),
             obs_summary, s(fm.get("obs_source")))
        )
        paper_ids[citekey] = conn.execute("SELECT last_insert_rowid()").fetchone()[0]

    print(f"  papers:      {len(paper_ids)}")

    # ---- Enrich papers from tsundo library (title, journal, full reference) ----
    enriched = 0
    not_found = []
    if TSUNDO_DB.exists():
        tsundo = sqlite3.connect(f"file:{TSUNDO_DB}?mode=ro", uri=True)
        # Build case-insensitive lookup index from tsundo
        tsundo_keys = {}
        for row in tsundo.execute("SELECT citekey FROM entries"):
            tsundo_keys[row[0].lower()] = row[0]

        # Build normalized lookup: underscore → hyphen for fuzzy matching
        tsundo_norm = {}
        for lk, rk in tsundo_keys.items():
            tsundo_norm[lk.replace('_', '-')] = rk

        for citekey in paper_ids:
            real_key = tsundo_keys.get(citekey.lower())
            # Fuzzy fallbacks: underscore/hyphen normalization, suffix variations
            if not real_key:
                norm = citekey.lower().replace('_', '-')
                real_key = tsundo_norm.get(norm)
            if not real_key:
                # Try stripping last 2 suffix chars and matching prefix
                base = re.match(r'(.+\d{4})-(\w+)$', citekey.lower().replace('_', '-'))
                if base:
                    prefix = base.group(1) + "-"
                    for lk, rk in tsundo_norm.items():
                        if lk.startswith(prefix):
                            real_key = rk
                            break
            if not real_key:
                # Not a book (has hyphen suffix like Author2020-xx)
                if re.match(r'.+\d{4}-\w+$', citekey):
                    not_found.append(citekey)
                continue
            row = tsundo.execute(
                "SELECT title, journal, author, year, volume, issue, pages, doi, pmid, pmc, abstract "
                "FROM entries WHERE citekey = ?", (real_key,)
            ).fetchone()
            if not row:
                continue
            t, j, author, year, volume, issue, pages, doi, pmid, pmc, abstract = row
            if t:
                t = re.sub(r'[{}]', '', t)  # strip BibTeX braces

            # Build formatted reference string
            ref_parts = []
            if author:
                ref_parts.append(author.replace(" and ", ", "))
            if t:
                ref_parts.append(t + ".")
            if j:
                jref = j
                if year:
                    jref += f" ({year})"
                if volume:
                    jref += f";{volume}"
                    if issue:
                        jref += f"({issue})"
                if pages:
                    jref += f":{pages}"
                ref_parts.append(jref + ".")
            ids = []
            if pmid:
                ids.append(f"PMID: {pmid}")
            if pmc:
                ids.append(f"PMCID: {pmc}")
            if doi:
                ids.append(f"DOI: {doi}")
            if ids:
                ref_parts.append(" ".join(ids))
            full_ref = " ".join(ref_parts) if ref_parts else None

            conn.execute(
                "UPDATE papers SET title = COALESCE(NULLIF(title,''), ?), "
                "journal = COALESCE(NULLIF(journal,''), ?), "
                "abstract = COALESCE(NULLIF(abstract,''), ?) WHERE citekey = ?",
                (t, j, abstract, citekey))
            enriched += 1

            # Write full reference to vault note if body lacks a citation line
            if full_ref:
                fname = conn.execute(
                    "SELECT filename FROM papers WHERE citekey = ?", (citekey,)
                ).fetchone()
                if fname and fname[0]:
                    fpath = VAULT / fname[0]
                    if fpath.exists():
                        content = fpath.read_text(encoding="utf-8")
                        fm_end = content.find("\n---", 3)
                        if fm_end > 0:
                            body = content[fm_end+4:]
                            # Only add if body doesn't already contain a full citation
                            # (check for PMID, DOI, or journal name as proxy)
                            has_ref = False
                            body_lower = body[:500].lower()
                            if pmid and str(pmid) in body_lower:
                                has_ref = True
                            elif doi and doi.lower() in body_lower:
                                has_ref = True
                            elif j and j.lower() in body_lower:
                                has_ref = True
                            if not has_ref:
                                new_content = content[:fm_end+4] + "\n  * " + full_ref + "\n" + body
                                fpath.write_text(new_content, encoding="utf-8")

        tsundo.close()
        print(f"  tsundo enriched: {enriched}/{len(paper_ids)} papers (title, journal, abstract)")
        if not_found:
            print(f"  tsundo mismatches ({len(not_found)}):")
            for ck in sorted(not_found):
                print(f"    {ck}")
    else:
        print(f"  tsundo: library.db not found, skipping enrichment")

    # ---- Derive paper distinctions from disease references ----
    def add_distinction(ck, text):
        """Append a distinction tag to a paper, avoiding duplicates."""
        row = conn.execute("SELECT distinction FROM papers WHERE citekey = ?", (ck,)).fetchone()
        if not row:
            return
        current = row[0] or ""
        if text in current:
            return
        new_val = (current + "; " + text).lstrip("; ")
        conn.execute("UPDATE papers SET distinction = ? WHERE citekey = ?", (new_val, ck))

    distinctions = 0
    for dname, did in disease_ids.items():
        row = conn.execute(
            "SELECT gwas_paper, wes_paper FROM diseases WHERE id = ?", (did,)
        ).fetchone()
        if not row:
            continue
        gwas_p, wes_p = row
        if gwas_p and gwas_p in paper_ids:
            add_distinction(gwas_p, f"GWAS ref for {dname}")
            distinctions += 1
        if wes_p and wes_p in paper_ids:
            add_distinction(wes_p, f"WES ref for {dname}")
            distinctions += 1
    # Also mark papers linked via key_papers in gene notes
    for filename, fm, body in notes.get("gene", []):
        symbol = fm.get("symbol", filename.replace(".md", "").lstrip("^"))
        for ck in fm.get("key_papers", []):
            clean = ck.lstrip("@")
            if clean in paper_ids:
                add_distinction(clean, f"key paper for {symbol}")
                distinctions += 1
    print(f"  paper distinctions: {distinctions}")

    # ---- Clinical Trials ----
    for filename, fm, body in notes.get("clinical_trial", []):
        trial_name = fm.get("trial_name", filename.replace(".md", ""))
        conn.execute(
            """INSERT INTO clinical_trials (trial_name, filename, created, updated,
               nct_id, clinicaltrials_url, phase, status, outcome,
               drug, modality, dose, company,
               indication_detail, n_enrolled, primary_endpoint,
               duration, estimated_completion,
               therapeutic_strategy, results_paper)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (trial_name, filename, s(fm.get("created")), s(fm.get("updated")),
             s(fm.get("nct_id")), s(fm.get("clinicaltrials_url")),
             s(fm.get("phase")), s(fm.get("status")), s(fm.get("outcome")),
             s(fm.get("drug")), s(fm.get("modality")), s(fm.get("dose")), s(fm.get("company")),
             s(fm.get("indication_detail")), n(fm.get("n_enrolled")),
             s(fm.get("primary_endpoint")),
             s(fm.get("duration")), s(fm.get("estimated_completion")),
             s(fm.get("therapeutic_strategy")), s(fm.get("results_paper")))
        )
        trial_ids[trial_name] = conn.execute("SELECT last_insert_rowid()").fetchone()[0]

    print(f"  trials:      {len(trial_ids)}")

    # ---- Therapeutic Strategies ----
    for filename, fm, body in notes.get("therapeutic_strategy", []):
        name = filename.replace(".md", "")
        conn.execute(
            """INSERT INTO therapeutic_strategies (name, filename, created, updated, modality)
               VALUES (?,?,?,?,?)""",
            (name, filename, s(fm.get("created")), s(fm.get("updated")),
             s(fm.get("modality")))
        )
        strategy_ids[name] = conn.execute("SELECT last_insert_rowid()").fetchone()[0]

    print(f"  strategies:  {len(strategy_ids)}")

    # ---- Zettels ----
    for filename, fm, body in notes.get("zettel", []):
        fact = fm.get("fact", filename.replace(".md", ""))
        conn.execute(
            """INSERT INTO zettels (fact, filename, created, updated, category)
               VALUES (?,?,?,?,?)""",
            (fact, filename, s(fm.get("created")), s(fm.get("updated")),
             s(fm.get("category")))
        )
        zettel_ids[filename] = conn.execute("SELECT last_insert_rowid()").fetchone()[0]

    print(f"  zettels:     {len(zettel_ids)}")

    # ---- Indexes ----
    for filename, fm, body in notes.get("index", []):
        conn.execute(
            """INSERT INTO indexes (subject, filename, created, updated, subject_type)
               VALUES (?,?,?,?,?)""",
            (s(fm.get("subject")), filename, s(fm.get("created")), s(fm.get("updated")),
             s(fm.get("subject_type")))
        )

    print(f"  indexes:     {len(notes.get('index', []))}")

    # -----------------------------------------------------------------------
    # Junction tables
    # -----------------------------------------------------------------------

    def resolve_disease(name):
        """Find disease_id by name, trying fuzzy match."""
        if name in disease_ids:
            return disease_ids[name]
        # Try case-insensitive
        for d, did in disease_ids.items():
            if d.lower() == name.lower():
                return did
        # Try substring
        for d, did in disease_ids.items():
            if name.lower() in d.lower() or d.lower() in name.lower():
                return did
        return None

    def resolve_gene(symbol):
        """Find gene_id by symbol."""
        if symbol in gene_ids:
            return gene_ids[symbol]
        # Gene notes are stored without ^ prefix in the DB
        clean = symbol.lstrip("^")
        if clean in gene_ids:
            return gene_ids[clean]
        return None

    def resolve_paper(citekey):
        """Find paper_id by citekey."""
        clean = citekey.lstrip("@")
        if clean in paper_ids:
            return paper_ids[clean]
        return None

    junction_counts = {}

    # Disease-Gene links (from disease notes' genes field AND gene notes' diseases field)
    for filename, fm, body in notes.get("disease", []):
        dname = filename.replace(".md", "")
        did = disease_ids.get(dname)
        if not did:
            continue
        for gene_sym in fm.get("genes", []):
            gid = resolve_gene(gene_sym)
            if gid:
                try:
                    conn.execute("INSERT OR IGNORE INTO disease_gene VALUES (?,?)", (did, gid))
                    junction_counts["disease_gene"] = junction_counts.get("disease_gene", 0) + 1
                except sqlite3.IntegrityError:
                    pass

    for filename, fm, body in notes.get("gene", []):
        symbol = fm.get("symbol", filename.replace(".md", "").lstrip("^"))
        gid = gene_ids.get(symbol)
        if not gid:
            continue
        for disease_name in fm.get("diseases", []):
            did = resolve_disease(disease_name)
            if did:
                try:
                    conn.execute("INSERT OR IGNORE INTO disease_gene VALUES (?,?)", (did, gid))
                    junction_counts["disease_gene"] = junction_counts.get("disease_gene", 0) + 1
                except sqlite3.IntegrityError:
                    pass

    # Disease-Paper links
    for filename, fm, body in notes.get("paper", []):
        citekey = fm.get("citekey", filename.replace(".md", "").lstrip("@"))
        pid = paper_ids.get(citekey)
        if not pid:
            continue
        for disease_name in fm.get("diseases", []):
            did = resolve_disease(disease_name)
            if did:
                try:
                    conn.execute("INSERT OR IGNORE INTO disease_paper VALUES (?,?)", (did, pid))
                    junction_counts["disease_paper"] = junction_counts.get("disease_paper", 0) + 1
                except sqlite3.IntegrityError:
                    pass

    # Gene-Paper links
    for filename, fm, body in notes.get("paper", []):
        citekey = fm.get("citekey", filename.replace(".md", "").lstrip("@"))
        pid = paper_ids.get(citekey)
        if not pid:
            continue
        for gene_sym in fm.get("genes", []):
            gid = resolve_gene(gene_sym)
            if gid:
                try:
                    conn.execute("INSERT OR IGNORE INTO gene_paper VALUES (?,?)", (gid, pid))
                    junction_counts["gene_paper"] = junction_counts.get("gene_paper", 0) + 1
                except sqlite3.IntegrityError:
                    pass

    # Also link genes via key_papers field
    for filename, fm, body in notes.get("gene", []):
        symbol = fm.get("symbol", filename.replace(".md", "").lstrip("^"))
        gid = gene_ids.get(symbol)
        if not gid:
            continue
        for citekey in fm.get("key_papers", []):
            pid = resolve_paper(citekey)
            if pid:
                try:
                    conn.execute("INSERT OR IGNORE INTO gene_paper VALUES (?,?)", (gid, pid))
                    junction_counts["gene_paper"] = junction_counts.get("gene_paper", 0) + 1
                except sqlite3.IntegrityError:
                    pass

    # Disease-Strategy links
    for filename, fm, body in notes.get("therapeutic_strategy", []):
        sname = filename.replace(".md", "")
        sid = strategy_ids.get(sname)
        if not sid:
            continue
        for disease_name in fm.get("diseases", []):
            did = resolve_disease(disease_name)
            if did:
                try:
                    conn.execute("INSERT OR IGNORE INTO disease_strategy VALUES (?,?)", (did, sid))
                    junction_counts["disease_strategy"] = junction_counts.get("disease_strategy", 0) + 1
                except sqlite3.IntegrityError:
                    pass

    # Strategy-Gene links
    for filename, fm, body in notes.get("therapeutic_strategy", []):
        sname = filename.replace(".md", "")
        sid = strategy_ids.get(sname)
        if not sid:
            continue
        for gene_sym in fm.get("target_genes", []):
            gid = resolve_gene(gene_sym)
            if gid:
                try:
                    conn.execute("INSERT OR IGNORE INTO strategy_gene VALUES (?,?)", (sid, gid))
                    junction_counts["strategy_gene"] = junction_counts.get("strategy_gene", 0) + 1
                except sqlite3.IntegrityError:
                    pass

    # Disease-Trial links
    for filename, fm, body in notes.get("clinical_trial", []):
        tname = fm.get("trial_name", filename.replace(".md", ""))
        tid = trial_ids.get(tname)
        if not tid:
            continue
        for disease_name in fm.get("diseases", []):
            did = resolve_disease(disease_name)
            if did:
                try:
                    conn.execute("INSERT OR IGNORE INTO disease_trial VALUES (?,?)", (did, tid))
                    junction_counts["disease_trial"] = junction_counts.get("disease_trial", 0) + 1
                except sqlite3.IntegrityError:
                    pass

    # Trial-Gene links
    for filename, fm, body in notes.get("clinical_trial", []):
        tname = fm.get("trial_name", filename.replace(".md", ""))
        tid = trial_ids.get(tname)
        if not tid:
            continue
        for gene_sym in fm.get("target_genes", []):
            gid = resolve_gene(gene_sym)
            if gid:
                try:
                    conn.execute("INSERT OR IGNORE INTO trial_gene VALUES (?,?)", (tid, gid))
                    junction_counts["trial_gene"] = junction_counts.get("trial_gene", 0) + 1
                except sqlite3.IntegrityError:
                    pass

    # Disease-Zettel links
    for filename, fm, body in notes.get("zettel", []):
        zid = zettel_ids.get(filename)
        if not zid:
            continue
        for disease_name in fm.get("diseases", []):
            did = resolve_disease(disease_name)
            if did:
                try:
                    conn.execute("INSERT OR IGNORE INTO disease_zettel VALUES (?,?)", (did, zid))
                    junction_counts["disease_zettel"] = junction_counts.get("disease_zettel", 0) + 1
                except sqlite3.IntegrityError:
                    pass

    # Zettel-Gene links
    for filename, fm, body in notes.get("zettel", []):
        zid = zettel_ids.get(filename)
        if not zid:
            continue
        for gene_sym in fm.get("genes", []):
            gid = resolve_gene(gene_sym)
            if gid:
                try:
                    conn.execute("INSERT OR IGNORE INTO zettel_gene VALUES (?,?)", (zid, gid))
                    junction_counts["zettel_gene"] = junction_counts.get("zettel_gene", 0) + 1
                except sqlite3.IntegrityError:
                    pass

    # Zettel-Paper links
    for filename, fm, body in notes.get("zettel", []):
        zid = zettel_ids.get(filename)
        if not zid:
            continue
        for citekey in fm.get("papers", []):
            pid = resolve_paper(citekey)
            if pid:
                try:
                    conn.execute("INSERT OR IGNORE INTO zettel_paper VALUES (?,?)", (zid, pid))
                    junction_counts["zettel_paper"] = junction_counts.get("zettel_paper", 0) + 1
                except sqlite3.IntegrityError:
                    pass

    print(f"\n  Junction table links:")
    for table, count in sorted(junction_counts.items()):
        print(f"    {table}: {count}")

    # Metadata
    conn.execute("INSERT INTO qak_meta VALUES ('built', ?)", (datetime.now().isoformat(),))
    conn.execute("INSERT INTO qak_meta VALUES ('vault', ?)", (str(VAULT),))

    conn.commit()
    conn.close()
    print(f"\nDatabase written to: {DB_PATH}")
    print(f"Size: {DB_PATH.stat().st_size / 1024:.0f} KB")


def verify_db():
    """Run basic verification queries."""
    conn = sqlite3.connect(str(DB_PATH))

    print("\n--- Verification ---\n")

    # Row counts
    tables = ["diseases", "genes", "papers", "clinical_trials",
              "therapeutic_strategies", "zettels", "indexes"]
    for t in tables:
        count = conn.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
        print(f"  {t}: {count} rows")

    # Junction counts
    junctions = ["disease_gene", "disease_paper", "gene_paper",
                 "disease_strategy", "strategy_gene",
                 "disease_trial", "trial_gene",
                 "disease_zettel", "zettel_gene", "zettel_paper"]
    print()
    for t in junctions:
        count = conn.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
        if count > 0:
            print(f"  {t}: {count} links")

    # Sample queries
    print("\n--- Sample Queries ---\n")

    # Papers per disease (top 5)
    print("  Papers per disease (top 5):")
    rows = conn.execute("""
        SELECT d.name, COUNT(*) as n
        FROM disease_paper dp
        JOIN diseases d ON d.id = dp.disease_id
        GROUP BY d.name ORDER BY n DESC LIMIT 5
    """).fetchall()
    for name, n in rows:
        print(f"    {name}: {n}")

    # Genes with most papers
    print("\n  Genes with most papers (top 5):")
    rows = conn.execute("""
        SELECT g.symbol, COUNT(*) as n
        FROM gene_paper gp
        JOIN genes g ON g.id = gp.gene_id
        GROUP BY g.symbol ORDER BY n DESC LIMIT 5
    """).fetchall()
    for sym, n in rows:
        print(f"    {sym}: {n}")

    # Papers with summaries
    total = conn.execute("SELECT COUNT(*) FROM papers").fetchone()[0]
    with_summary = conn.execute("SELECT COUNT(*) FROM papers WHERE obs_summary IS NOT NULL AND obs_summary != ''").fetchone()[0]
    human = conn.execute("SELECT COUNT(*) FROM papers WHERE obs_source = 'human'").fetchone()[0]
    ai = conn.execute("SELECT COUNT(*) FROM papers WHERE obs_source = 'ai'").fetchone()[0]
    print(f"\n  Paper summaries: {with_summary}/{total} ({human} human, {ai} ai)")

    # Zettels by category
    print("\n  Zettels by category:")
    rows = conn.execute("SELECT category, COUNT(*) FROM zettels GROUP BY category ORDER BY COUNT(*) DESC").fetchall()
    for cat, n in rows:
        print(f"    {cat}: {n}")

    conn.close()


if __name__ == "__main__":
    print("Building QAK database...\n")
    build_db()
    verify_db()
