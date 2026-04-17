package main

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"os"
	"path/filepath"
	"strings"

	_ "github.com/mattn/go-sqlite3"
)

// Alfred Script Filter JSON types

type AlfredItem struct {
	Title        string            `json:"title"`
	Subtitle     string            `json:"subtitle"`
	Arg          string            `json:"arg"`
	Icon         *AlfredIcon       `json:"icon,omitempty"`
	Autocomplete string            `json:"autocomplete,omitempty"`
	Text         *AlfredText       `json:"text,omitempty"`
	Mods         map[string]AlfMod `json:"mods,omitempty"`
	UID          string            `json:"uid,omitempty"`
}

type AlfredIcon struct {
	Path string `json:"path"`
}

type AlfredText struct {
	Copy      string `json:"copy,omitempty"`
	Largetype string `json:"largetype,omitempty"`
}

type AlfMod struct {
	Arg      string `json:"arg"`
	Subtitle string `json:"subtitle"`
}

type AlfredOutput struct {
	Items []AlfredItem `json:"items"`
}

// Paths

func dbPath() string {
	if p := os.Getenv("QAK_DB"); p != "" {
		return p
	}
	if exe, err := os.Executable(); err == nil {
		return filepath.Join(filepath.Dir(exe), "qak.db")
	}
	return "qak.db"
}

func vaultDir() string {
	if p := os.Getenv("QAK_VAULT_PATH"); p != "" {
		return p
	}
	home, _ := os.UserHomeDir()
	return filepath.Join(home,
		"Library/CloudStorage/OneDrive-RegeneronPharmaceuticals,Inc/MyScripts/myGitHubRepos/gitVault/gitVault-notes")
}

func vaultName() string {
	if p := os.Getenv("QAK_VAULT"); p != "" {
		return p
	}
	return "gitVault"
}

func obsidianURI(filename string) string {
	name := strings.TrimSuffix(filename, ".md")
	return fmt.Sprintf("obsidian://open?vault=%s&file=%s", vaultName(), name)
}

func readNoteBody(filename string) string {
	path := filepath.Join(vaultDir(), filename)
	data, err := os.ReadFile(path)
	if err != nil {
		return ""
	}
	content := string(data)
	if strings.HasPrefix(content, "---") {
		end := strings.Index(content[3:], "\n---")
		if end != -1 {
			content = strings.TrimSpace(content[end+7:])
		}
	}
	return content
}

// Helper formatters

func orEmpty(s sql.NullString) string {
	if s.Valid && s.String != "" {
		return s.String
	}
	return ""
}

func fmtNum(n sql.NullInt64) string {
	if !n.Valid {
		return ""
	}
	v := n.Int64
	if v >= 1000000 {
		return fmt.Sprintf("%.1fM", float64(v)/1e6)
	}
	if v >= 1000 {
		return fmt.Sprintf("%dk", v/1000)
	}
	return fmt.Sprintf("%d", v)
}

func fmtFloat(f sql.NullFloat64) string {
	if !f.Valid {
		return ""
	}
	if f.Float64 == float64(int64(f.Float64)) {
		return fmt.Sprintf("%d", int64(f.Float64))
	}
	return fmt.Sprintf("%.1f", f.Float64)
}

func join(parts []string) string {
	var nonEmpty []string
	for _, p := range parts {
		if p != "" {
			nonEmpty = append(nonEmpty, p)
		}
	}
	return strings.Join(nonEmpty, " · ")
}

func truncate(s string, max int) string {
	if len(s) > max {
		return s[:max] + "\n\n[truncated]"
	}
	return s
}

// Build an item where Enter = note text, Shift+Enter = open in Obsidian
func makeItem(title, subtitle, filename, uid string) AlfredItem {
	body := readNoteBody(filename)
	clipText := truncate(body, 10000)

	return AlfredItem{
		Title:    title,
		Subtitle: subtitle,
		Arg:      clipText,
		UID:      uid,
		Text:     &AlfredText{Copy: clipText, Largetype: clipText},
		Mods: map[string]AlfMod{
			"shift": {Arg: obsidianURI(filename), Subtitle: "⇧↵ Open in Obsidian"},
		},
	}
}

// -----------------------------------------------------------------------
// Fuzzy multi-word WHERE clause builder
// -----------------------------------------------------------------------
// Splits query into words, builds:
//   (col1 LIKE '%w1%' OR col2 LIKE '%w1%' ...) AND (col1 LIKE '%w2%' OR col2 LIKE '%w2%' ...)
// Each word must match at least one column. Word order doesn't matter.

func fuzzyWhere(query string, columns []string) (clause string, args []interface{}) {
	words := strings.Fields(query)
	if len(words) == 0 {
		return "1=1", nil
	}

	var wordClauses []string
	for _, word := range words {
		like := "%" + word + "%"
		var colClauses []string
		for _, col := range columns {
			colClauses = append(colClauses, col+" LIKE ?")
			args = append(args, like)
		}
		wordClauses = append(wordClauses, "("+strings.Join(colClauses, " OR ")+")")
	}
	clause = strings.Join(wordClauses, " AND ")
	return
}

// Tag prefixes for focused search
var tagPrefixes = map[string]string{
	"disease:":  "disease",
	"d:":        "disease",
	"gene:":     "gene",
	"g:":        "gene",
	"paper:":    "paper",
	"p:":        "paper",
	"trial:":    "trial",
	"t:":        "trial",
	"strategy:": "strategy",
	"s:":        "strategy",
	"zettel:":   "zettel",
	"zk:":       "zettel",
	"z:":        "zettel",
}

func parseQuery(raw string) (filter string, query string) {
	raw = strings.TrimSpace(raw)
	for prefix, kind := range tagPrefixes {
		if strings.HasPrefix(strings.ToLower(raw), prefix) {
			return kind, strings.TrimSpace(raw[len(prefix):])
		}
	}
	return "", raw
}

// -----------------------------------------------------------------------
// Search: diseases
// -----------------------------------------------------------------------

func searchDiseases(db *sql.DB, q string) []AlfredItem {
	where, args := fuzzyWhere(q, []string{
		"d.name", "d.filename", "CAST(d.omim AS TEXT)", "CAST(d.mondo AS TEXT)",
	})
	rows, err := db.Query(`
		SELECT d.name, d.filename, d.n_patients_us, d.prevalence_per_100k, d.gwas_loci,
		       (SELECT COUNT(*) FROM disease_gene dg WHERE dg.disease_id = d.id),
		       (SELECT COUNT(*) FROM disease_paper dp WHERE dp.disease_id = d.id),
		       (SELECT COUNT(*) FROM disease_trial dt WHERE dt.disease_id = d.id)
		FROM diseases d
		WHERE `+where+`
		ORDER BY (SELECT COUNT(*) FROM disease_paper dp WHERE dp.disease_id = d.id) DESC
		LIMIT 20`, args...)
	if err != nil {
		return nil
	}
	defer rows.Close()

	var items []AlfredItem
	for rows.Next() {
		var name, filename string
		var nUS, gwas, nGenes, nPapers, nTrials sql.NullInt64
		var prev sql.NullFloat64
		rows.Scan(&name, &filename, &nUS, &prev, &gwas, &nGenes, &nPapers, &nTrials)

		sub := join([]string{
			func() string {
				if s := fmtNum(nUS); s != "" {
					return s + " US patients"
				}
				return ""
			}(),
			func() string {
				if s := fmtFloat(prev); s != "" {
					return s + "/100k"
				}
				return ""
			}(),
			func() string {
				if gwas.Valid && gwas.Int64 > 0 {
					return fmt.Sprintf("%d GWAS loci", gwas.Int64)
				}
				return ""
			}(),
			fmt.Sprintf("%d genes, %d papers, %d trials", nGenes.Int64, nPapers.Int64, nTrials.Int64),
		})

		items = append(items, makeItem("🦠 "+name, sub, filename, "disease:"+name))
	}
	return items
}

// -----------------------------------------------------------------------
// Search: genes
// -----------------------------------------------------------------------

func searchGenes(db *sql.DB, q string) []AlfredItem {
	where, args := fuzzyWhere(q, []string{
		"g.symbol", "g.full_name", "g.filename", "g.therapeutic_notes",
	})
	rows, err := db.Query(`
		SELECT g.symbol, g.filename, g.full_name, g.chromosome, g.protein_length,
		       (SELECT COUNT(*) FROM disease_gene dg WHERE dg.gene_id = g.id),
		       (SELECT COUNT(*) FROM gene_paper gp WHERE gp.gene_id = g.id)
		FROM genes g
		WHERE `+where+`
		ORDER BY (SELECT COUNT(*) FROM gene_paper gp WHERE gp.gene_id = g.id) DESC
		LIMIT 20`, args...)
	if err != nil {
		return nil
	}
	defer rows.Close()

	var items []AlfredItem
	for rows.Next() {
		var symbol, filename string
		var fullName, chrom sql.NullString
		var protLen, nDiseases, nPapers sql.NullInt64
		rows.Scan(&symbol, &filename, &fullName, &chrom, &protLen, &nDiseases, &nPapers)

		sub := join([]string{
			orEmpty(fullName),
			func() string {
				if s := orEmpty(chrom); s != "" {
					return "chr" + s
				}
				return ""
			}(),
			fmt.Sprintf("%d diseases, %d papers", nDiseases.Int64, nPapers.Int64),
		})

		items = append(items, makeItem("🧬 "+symbol, sub, filename, "gene:"+symbol))
	}
	return items
}

// -----------------------------------------------------------------------
// Search: papers
// -----------------------------------------------------------------------

func searchPapers(db *sql.DB, q string) []AlfredItem {
	where, args := fuzzyWhere(q, []string{
		"p.citekey", "p.first_author", "p.title", "p.obs_summary",
		"p.study_type", "p.journal", "p.filename",
	})
	rows, err := db.Query(`
		SELECT p.citekey, p.filename, p.first_author, p.year, p.study_type,
		       p.n_total, p.n_loci, p.obs_summary, p.obs_source, p.title, p.journal
		FROM papers p
		WHERE `+where+`
		ORDER BY p.year DESC
		LIMIT 20`, args...)
	if err != nil {
		return nil
	}
	defer rows.Close()

	var items []AlfredItem
	for rows.Next() {
		var citekey, filename string
		var author, studyType, summary, obsSource, title, journal sql.NullString
		var year, nTotal, nLoci sql.NullInt64
		rows.Scan(&citekey, &filename, &author, &year, &studyType, &nTotal, &nLoci,
			&summary, &obsSource, &title, &journal)

		displayTitle := citekey
		if s := orEmpty(author); s != "" {
			displayTitle = s
			if year.Valid {
				displayTitle += fmt.Sprintf(" (%d)", year.Int64)
			}
		}

		sub := join([]string{
			orEmpty(studyType),
			func() string {
				if s := fmtNum(nTotal); s != "" {
					return "N=" + s
				}
				return ""
			}(),
			func() string {
				if nLoci.Valid && nLoci.Int64 > 0 {
					return fmt.Sprintf("%d loci", nLoci.Int64)
				}
				return ""
			}(),
			func() string {
				if s := orEmpty(obsSource); s != "" {
					return "summary:" + s
				}
				return ""
			}(),
		})

		summaryText := orEmpty(summary)
		body := readNoteBody(filename)

		argText := summaryText
		if argText == "" {
			argText = body
		}
		argText = truncate(argText, 10000)

		largeText := ""
		if summaryText != "" {
			largeText = "SUMMARY:\n" + summaryText + "\n\n---\n\n" + body
		} else {
			largeText = body
		}
		largeText = truncate(largeText, 10000)

		item := AlfredItem{
			Title:    "📄 " + displayTitle,
			Subtitle: sub,
			Arg:      argText,
			UID:      "paper:" + citekey,
			Text:     &AlfredText{Copy: argText, Largetype: largeText},
			Mods: map[string]AlfMod{
				"shift": {Arg: obsidianURI(filename), Subtitle: "⇧↵ Open in Obsidian"},
				"cmd":   {Arg: truncate(body, 10000), Subtitle: "⌘↵ Copy full note"},
			},
		}
		items = append(items, item)
	}
	return items
}

// -----------------------------------------------------------------------
// Search: clinical trials
// -----------------------------------------------------------------------

func searchTrials(db *sql.DB, q string) []AlfredItem {
	where, args := fuzzyWhere(q, []string{
		"ct.trial_name", "ct.drug", "ct.modality", "ct.company",
		"ct.nct_id", "ct.primary_endpoint", "ct.indication_detail",
		"ct.filename", "d.name",
	})
	rows, err := db.Query(`
		SELECT ct.trial_name, ct.filename, ct.drug, ct.phase, ct.outcome,
		       ct.status, ct.n_enrolled, ct.modality, ct.company,
		       ct.primary_endpoint, ct.indication_detail,
		       GROUP_CONCAT(DISTINCT d.name) as diseases
		FROM clinical_trials ct
		LEFT JOIN disease_trial dt ON ct.id = dt.trial_id
		LEFT JOIN diseases d ON d.id = dt.disease_id
		WHERE `+where+`
		GROUP BY ct.id
		ORDER BY ct.trial_name
		LIMIT 20`, args...)
	if err != nil {
		return nil
	}
	defer rows.Close()

	var items []AlfredItem
	for rows.Next() {
		var trialName, filename string
		var drug, phase, outcome, status, modality, company sql.NullString
		var endpoint, indication, diseases sql.NullString
		var nEnrolled sql.NullInt64
		rows.Scan(&trialName, &filename, &drug, &phase, &outcome, &status,
			&nEnrolled, &modality, &company, &endpoint, &indication, &diseases)

		sub := join([]string{
			orEmpty(drug),
			orEmpty(phase),
			orEmpty(outcome),
			func() string {
				if s := fmtNum(nEnrolled); s != "" {
					return "N=" + s
				}
				return ""
			}(),
			orEmpty(diseases),
		})

		items = append(items, makeItem("💊 "+trialName, sub, filename, "trial:"+trialName))
	}
	return items
}

// -----------------------------------------------------------------------
// Search: therapeutic strategies
// -----------------------------------------------------------------------

func searchStrategies(db *sql.DB, q string) []AlfredItem {
	where, args := fuzzyWhere(q, []string{
		"ts.name", "ts.modality", "ts.filename", "d.name", "g.symbol",
	})
	rows, err := db.Query(`
		SELECT ts.name, ts.filename, ts.modality,
		       GROUP_CONCAT(DISTINCT d.name) as diseases,
		       GROUP_CONCAT(DISTINCT g.symbol) as genes
		FROM therapeutic_strategies ts
		LEFT JOIN disease_strategy ds ON ts.id = ds.strategy_id
		LEFT JOIN diseases d ON d.id = ds.disease_id
		LEFT JOIN strategy_gene sg ON ts.id = sg.strategy_id
		LEFT JOIN genes g ON g.id = sg.gene_id
		WHERE `+where+`
		GROUP BY ts.id
		ORDER BY ts.name
		LIMIT 20`, args...)
	if err != nil {
		return nil
	}
	defer rows.Close()

	var items []AlfredItem
	for rows.Next() {
		var name, filename string
		var modality, diseases, genes sql.NullString
		rows.Scan(&name, &filename, &modality, &diseases, &genes)

		sub := join([]string{
			orEmpty(modality),
			orEmpty(diseases),
			func() string {
				if s := orEmpty(genes); s != "" {
					return "targets: " + s
				}
				return ""
			}(),
		})

		items = append(items, makeItem("🎯 "+name, sub, filename, "strategy:"+name))
	}
	return items
}

// -----------------------------------------------------------------------
// Search: zettels
// -----------------------------------------------------------------------

func searchZettels(db *sql.DB, q string) []AlfredItem {
	where, args := fuzzyWhere(q, []string{
		"z.fact", "z.category", "z.filename", "d.name", "g.symbol",
	})
	rows, err := db.Query(`
		SELECT z.fact, z.filename, z.category,
		       GROUP_CONCAT(DISTINCT d.name) as diseases,
		       GROUP_CONCAT(DISTINCT g.symbol) as genes
		FROM zettels z
		LEFT JOIN disease_zettel dz ON z.id = dz.zettel_id
		LEFT JOIN diseases d ON d.id = dz.disease_id
		LEFT JOIN zettel_gene zg ON z.id = zg.zettel_id
		LEFT JOIN genes g ON g.id = zg.gene_id
		WHERE `+where+`
		GROUP BY z.id
		ORDER BY z.fact
		LIMIT 20`, args...)
	if err != nil {
		return nil
	}
	defer rows.Close()

	var items []AlfredItem
	for rows.Next() {
		var fact, filename string
		var category, diseases, genes sql.NullString
		rows.Scan(&fact, &filename, &category, &diseases, &genes)

		sub := join([]string{
			func() string {
				if s := orEmpty(category); s != "" {
					return "[" + s + "]"
				}
				return ""
			}(),
			orEmpty(diseases),
			orEmpty(genes),
		})

		body := readNoteBody(filename)
		argText := fact
		if body != "" {
			argText = fact + "\n\n" + body
		}
		argText = truncate(argText, 10000)

		items = append(items, AlfredItem{
			Title:    fact,
			Subtitle: sub,
			Arg:      argText,
			UID:      "zettel:" + filename,
			Text:     &AlfredText{Copy: fact, Largetype: argText},
			Mods: map[string]AlfMod{
				"shift": {Arg: obsidianURI(filename), Subtitle: "⇧↵ Open in Obsidian"},
			},
		})
	}
	return items
}

// -----------------------------------------------------------------------
// Search: properties (explodes entity fields into individual items)
// -----------------------------------------------------------------------

type propRow struct {
	entity   string // e.g. "ALS"
	label    string // e.g. "incidence"
	value    string // e.g. "2.0 /100k"
	unit     string // appended to value for display
	filename string
	icon     string
}

func searchProperties(db *sql.DB, q string) []AlfredItem {
	// Build property rows from diseases
	var rows []propRow

	diseaseRows, err := db.Query(`
		SELECT name, filename, prevalence_per_100k, incidence_per_100k,
		       n_patients_us, lifetime_risk, omim, mondo, orphanet,
		       gwas_largest_n, gwas_loci, gwas_paper,
		       wes_largest_n, wes_loci, wes_paper,
		       heritability_twin, heritability_gwas
		FROM diseases`)
	if err == nil {
		defer diseaseRows.Close()
		for diseaseRows.Next() {
			var name, filename string
			var prev, incid sql.NullFloat64
			var nUS, gwasN, gwasLoci, wesN, wesLoci sql.NullInt64
			var risk, omim, mondo, orphanet sql.NullString
			var gwasPaper, wesPaper, herTwin, herGwas sql.NullString
			diseaseRows.Scan(&name, &filename, &prev, &incid, &nUS, &risk,
				&omim, &mondo, &orphanet, &gwasN, &gwasLoci, &gwasPaper,
				&wesN, &wesLoci, &wesPaper, &herTwin, &herGwas)

			add := func(label, val, unit string) {
				if val != "" {
					rows = append(rows, propRow{name, label, val, unit, filename, "🦠"})
				}
			}
			add("prevalence", fmtFloat(prev), " /100k")
			add("incidence", fmtFloat(incid), " /100k")
			add("US patients", fmtNum(nUS), "")
			add("lifetime risk", orEmpty(risk), "")
			add("OMIM", orEmpty(omim), "")
			add("MONDO", orEmpty(mondo), "")
			add("Orphanet", orEmpty(orphanet), "")
			add("GWAS largest N", fmtNum(gwasN), "")
			add("GWAS loci", fmtNum(gwasLoci), "")
			add("GWAS paper", orEmpty(gwasPaper), "")
			add("WES largest N", fmtNum(wesN), "")
			add("WES loci", fmtNum(wesLoci), "")
			add("WES paper", orEmpty(wesPaper), "")
			add("heritability twin", orEmpty(herTwin), "")
			add("heritability GWAS", orEmpty(herGwas), "")
		}
	}

	// Gene properties
	geneRows, err := db.Query(`
		SELECT symbol, filename, full_name, chromosome, cytoband, protein_length
		FROM genes`)
	if err == nil {
		defer geneRows.Close()
		for geneRows.Next() {
			var symbol, filename string
			var fullName, chrom, cytoband sql.NullString
			var protLen sql.NullInt64
			geneRows.Scan(&symbol, &filename, &fullName, &chrom, &cytoband, &protLen)

			add := func(label, val, unit string) {
				if val != "" {
					rows = append(rows, propRow{symbol, label, val, unit, filename, "🧬"})
				}
			}
			add("full name", orEmpty(fullName), "")
			add("chromosome", orEmpty(chrom), "")
			add("cytoband", orEmpty(cytoband), "")
			add("protein length", fmtNum(protLen), " aa")
		}
	}

	// Paper properties
	paperRows, err := db.Query(`
		SELECT citekey, filename, study_type, first_author, year, journal,
		       n_cases, n_controls, n_total, n_loci
		FROM papers`)
	if err == nil {
		defer paperRows.Close()
		for paperRows.Next() {
			var citekey, filename string
			var studyType, author, journal sql.NullString
			var year, nCases, nControls, nTotal, nLoci sql.NullInt64
			paperRows.Scan(&citekey, &filename, &studyType, &author, &year,
				&journal, &nCases, &nControls, &nTotal, &nLoci)

			add := func(label, val, unit string) {
				if val != "" {
					rows = append(rows, propRow{citekey, label, val, unit, filename, "📄"})
				}
			}
			add("study type", orEmpty(studyType), "")
			add("first author", orEmpty(author), "")
			add("year", fmtNum(year), "")
			add("journal", orEmpty(journal), "")
			add("N cases", fmtNum(nCases), "")
			add("N controls", fmtNum(nControls), "")
			add("N total", fmtNum(nTotal), "")
			add("N loci", fmtNum(nLoci), "")
		}
	}

	// Trial properties
	trialRows, err := db.Query(`
		SELECT trial_name, filename, drug, phase, outcome, status,
		       n_enrolled, modality, company, primary_endpoint
		FROM clinical_trials`)
	if err == nil {
		defer trialRows.Close()
		for trialRows.Next() {
			var trialName, filename string
			var drug, phase, outcome, status, modality, company, endpoint sql.NullString
			var nEnrolled sql.NullInt64
			trialRows.Scan(&trialName, &filename, &drug, &phase, &outcome,
				&status, &nEnrolled, &modality, &company, &endpoint)

			add := func(label, val, unit string) {
				if val != "" {
					rows = append(rows, propRow{trialName, label, val, unit, filename, "💊"})
				}
			}
			add("drug", orEmpty(drug), "")
			add("phase", orEmpty(phase), "")
			add("outcome", orEmpty(outcome), "")
			add("status", orEmpty(status), "")
			add("N enrolled", fmtNum(nEnrolled), "")
			add("modality", orEmpty(modality), "")
			add("company", orEmpty(company), "")
			add("primary endpoint", orEmpty(endpoint), "")
		}
	}

	// Now filter rows using fuzzy matching
	words := strings.Fields(strings.ToLower(q))
	var items []AlfredItem

	for _, r := range rows {
		searchable := strings.ToLower(r.entity + " " + r.label + " " + r.value)
		match := true
		for _, w := range words {
			if !strings.Contains(searchable, w) {
				match = false
				break
			}
		}
		if !match {
			continue
		}

		displayVal := r.value + r.unit
		clipText := r.entity + " " + r.label + ": " + displayVal

		items = append(items, AlfredItem{
			Title:    r.icon + " " + r.entity + " — " + r.label + ": " + displayVal,
			Subtitle: "↵ copy · ⇧↵ open Obsidian",
			Arg:      clipText,
			UID:      "prop:" + r.entity + ":" + r.label,
			Text:     &AlfredText{Copy: clipText, Largetype: clipText},
			Mods: map[string]AlfMod{
				"shift": {Arg: obsidianURI(r.filename), Subtitle: "⇧↵ Open in Obsidian"},
			},
		})

		if len(items) >= 20 {
			break
		}
	}
	return items
}

// -----------------------------------------------------------------------
// Wide search: all entity types
// -----------------------------------------------------------------------

func searchAll(db *sql.DB, q string) []AlfredItem {
	var items []AlfredItem
	items = append(items, searchProperties(db, q)...)
	items = append(items, searchDiseases(db, q)...)
	items = append(items, searchGenes(db, q)...)
	items = append(items, searchTrials(db, q)...)
	items = append(items, searchStrategies(db, q)...)
	items = append(items, searchZettels(db, q)...)
	items = append(items, searchPapers(db, q)...)

	if len(items) > 40 {
		items = items[:40]
	}
	return items
}

// -----------------------------------------------------------------------
// Main
// -----------------------------------------------------------------------

func main() {
	if len(os.Args) < 2 {
		fmt.Fprintf(os.Stderr, "Usage: qak <query>\n")
		fmt.Fprintf(os.Stderr, "  Tags: disease: gene: paper: trial: strategy: zettel:\n")
		fmt.Fprintf(os.Stderr, "  Short: d: g: p: t: s: z:\n")
		fmt.Fprintf(os.Stderr, "\nActions:\n")
		fmt.Fprintf(os.Stderr, "  Enter       → copy note text to clipboard\n")
		fmt.Fprintf(os.Stderr, "  Cmd+L       → Large Type (full note)\n")
		fmt.Fprintf(os.Stderr, "  Shift+Enter → open in Obsidian\n")
		os.Exit(1)
	}

	raw := strings.Join(os.Args[1:], " ")
	if strings.HasPrefix(raw, "--zk ") {
		raw = "zk:" + raw[5:]
	} else if raw == "--zk" {
		raw = "zk:"
	}

	filter, query := parseQuery(raw)

	db, err := sql.Open("sqlite3", dbPath()+"?mode=ro")
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error opening database: %v\n", err)
		os.Exit(1)
	}
	defer db.Close()

	var items []AlfredItem

	if query == "" && filter == "" {
		items = append(items, AlfredItem{
			Title:    "Search QAK knowledge base…",
			Subtitle: "↵ copy text · ⇧↵ open Obsidian · ⌘L large type — Tags: d: g: p: t: s: z:",
		})
	} else if query == "" && filter != "" {
		items = append(items, AlfredItem{
			Title:    fmt.Sprintf("Search %ss…", filter),
			Subtitle: fmt.Sprintf("Type a keyword after %s:", filter),
		})
	} else {
		switch filter {
		case "disease":
			items = searchDiseases(db, query)
		case "gene":
			items = searchGenes(db, query)
		case "paper":
			items = searchPapers(db, query)
		case "trial":
			items = searchTrials(db, query)
		case "strategy":
			items = searchStrategies(db, query)
		case "zettel":
			items = searchZettels(db, query)
		default:
			items = searchAll(db, query)
		}
	}

	if len(items) == 0 {
		items = append(items, AlfredItem{
			Title:    "No results",
			Subtitle: fmt.Sprintf("No matches for \"%s\"", query),
		})
	}

	// Add x/N counter to each subtitle
	total := len(items)
	for i := range items {
		if items[i].Subtitle != "" {
			items[i].Subtitle = fmt.Sprintf("%d/%d %s", i+1, total, items[i].Subtitle)
		} else {
			items[i].Subtitle = fmt.Sprintf("%d/%d", i+1, total)
		}
	}

	output := AlfredOutput{Items: items}
	enc := json.NewEncoder(os.Stdout)
	enc.SetEscapeHTML(false)
	enc.Encode(output)
}
