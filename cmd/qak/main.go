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

// Database path resolution
func dbPath() string {
	if p := os.Getenv("QAK_DB"); p != "" {
		return p
	}
	home, _ := os.UserHomeDir()
	return filepath.Join(home,
		"Library/CloudStorage/OneDrive-RegeneronPharmaceuticals,Inc/MyScripts/myGitHubRepos/QAK/qak.db")
}

func vaultPath() string {
	if p := os.Getenv("QAK_VAULT"); p != "" {
		return p
	}
	return "gitVault"
}

func obsidianURI(filename string) string {
	name := strings.TrimSuffix(filename, ".md")
	return fmt.Sprintf("obsidian://open?vault=%s&file=%s", vaultPath(), name)
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
	like := "%" + q + "%"
	rows, err := db.Query(`
		SELECT d.name, d.filename, d.n_patients_us, d.prevalence_per_100k, d.gwas_loci,
		       d.lifetime_risk, d.omim,
		       (SELECT COUNT(*) FROM disease_gene dg WHERE dg.disease_id = d.id),
		       (SELECT COUNT(*) FROM disease_paper dp WHERE dp.disease_id = d.id),
		       (SELECT COUNT(*) FROM disease_trial dt WHERE dt.disease_id = d.id)
		FROM diseases d
		WHERE d.name LIKE ? OR d.filename LIKE ?
		      OR CAST(d.omim AS TEXT) LIKE ? OR CAST(d.mondo AS TEXT) LIKE ?
		ORDER BY (SELECT COUNT(*) FROM disease_paper dp WHERE dp.disease_id = d.id) DESC
		LIMIT 20`, like, like, like, like)
	if err != nil {
		return nil
	}
	defer rows.Close()

	var items []AlfredItem
	for rows.Next() {
		var name, filename string
		var nUS, gwas, nGenes, nPapers, nTrials sql.NullInt64
		var prev sql.NullFloat64
		var risk, omim sql.NullString
		rows.Scan(&name, &filename, &nUS, &prev, &gwas, &risk, &omim, &nGenes, &nPapers, &nTrials)

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

		items = append(items, AlfredItem{
			Title:    "🦠 " + name,
			Subtitle: sub,
			Arg:      obsidianURI(filename),
			UID:      "disease:" + name,
			Text:     &AlfredText{Copy: name, Largetype: name + "\n" + sub},
		})
	}
	return items
}

// -----------------------------------------------------------------------
// Search: genes
// -----------------------------------------------------------------------

func searchGenes(db *sql.DB, q string) []AlfredItem {
	like := "%" + q + "%"
	rows, err := db.Query(`
		SELECT g.symbol, g.filename, g.full_name, g.chromosome, g.protein_length,
		       g.therapeutic_notes,
		       (SELECT COUNT(*) FROM disease_gene dg WHERE dg.gene_id = g.id),
		       (SELECT COUNT(*) FROM gene_paper gp WHERE gp.gene_id = g.id)
		FROM genes g
		WHERE g.symbol LIKE ? OR g.full_name LIKE ? OR g.filename LIKE ?
		      OR g.therapeutic_notes LIKE ?
		ORDER BY (SELECT COUNT(*) FROM gene_paper gp WHERE gp.gene_id = g.id) DESC
		LIMIT 20`, like, like, like, like)
	if err != nil {
		return nil
	}
	defer rows.Close()

	var items []AlfredItem
	for rows.Next() {
		var symbol, filename string
		var fullName, chrom, therNotes sql.NullString
		var protLen, nDiseases, nPapers sql.NullInt64
		rows.Scan(&symbol, &filename, &fullName, &chrom, &protLen, &therNotes, &nDiseases, &nPapers)

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

		items = append(items, AlfredItem{
			Title:    "🧬 " + symbol,
			Subtitle: sub,
			Arg:      obsidianURI(filename),
			UID:      "gene:" + symbol,
			Text:     &AlfredText{Copy: symbol, Largetype: symbol + "\n" + sub},
		})
	}
	return items
}

// -----------------------------------------------------------------------
// Search: papers
// -----------------------------------------------------------------------

func searchPapers(db *sql.DB, q string) []AlfredItem {
	like := "%" + q + "%"
	rows, err := db.Query(`
		SELECT p.citekey, p.filename, p.first_author, p.year, p.study_type,
		       p.n_total, p.n_loci, p.obs_summary, p.obs_source, p.title, p.journal
		FROM papers p
		WHERE p.citekey LIKE ? OR p.first_author LIKE ? OR p.title LIKE ?
		      OR p.obs_summary LIKE ? OR p.study_type LIKE ? OR p.journal LIKE ?
		      OR p.filename LIKE ?
		ORDER BY p.year DESC
		LIMIT 20`, like, like, like, like, like, like, like)
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
		largetype := displayTitle + "\n" + sub
		if summaryText != "" {
			largetype += "\n\n" + summaryText
		}

		item := AlfredItem{
			Title:    "📄 " + displayTitle,
			Subtitle: sub,
			Arg:      obsidianURI(filename),
			UID:      "paper:" + citekey,
			Text:     &AlfredText{Copy: citekey, Largetype: largetype},
		}
		if summaryText != "" {
			item.Mods = map[string]AlfMod{
				"cmd": {Arg: summaryText, Subtitle: "⌘: Copy summary"},
			}
		}
		items = append(items, item)
	}
	return items
}

// -----------------------------------------------------------------------
// Search: clinical trials
// -----------------------------------------------------------------------

func searchTrials(db *sql.DB, q string) []AlfredItem {
	like := "%" + q + "%"
	rows, err := db.Query(`
		SELECT ct.trial_name, ct.filename, ct.drug, ct.phase, ct.outcome,
		       ct.status, ct.n_enrolled, ct.modality, ct.company,
		       ct.primary_endpoint, ct.indication_detail,
		       GROUP_CONCAT(DISTINCT d.name) as diseases
		FROM clinical_trials ct
		LEFT JOIN disease_trial dt ON ct.id = dt.trial_id
		LEFT JOIN diseases d ON d.id = dt.disease_id
		WHERE ct.trial_name LIKE ? OR ct.drug LIKE ? OR ct.modality LIKE ?
		      OR ct.company LIKE ? OR ct.nct_id LIKE ? OR ct.primary_endpoint LIKE ?
		      OR ct.indication_detail LIKE ? OR ct.filename LIKE ?
		      OR d.name LIKE ?
		GROUP BY ct.id
		ORDER BY ct.trial_name
		LIMIT 20`, like, like, like, like, like, like, like, like, like)
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

		largetype := trialName + "\n" + sub
		if s := orEmpty(endpoint); s != "" {
			largetype += "\nEndpoint: " + s
		}

		items = append(items, AlfredItem{
			Title:    "💊 " + trialName,
			Subtitle: sub,
			Arg:      obsidianURI(filename),
			UID:      "trial:" + trialName,
			Text:     &AlfredText{Copy: trialName, Largetype: largetype},
		})
	}
	return items
}

// -----------------------------------------------------------------------
// Search: therapeutic strategies
// -----------------------------------------------------------------------

func searchStrategies(db *sql.DB, q string) []AlfredItem {
	like := "%" + q + "%"
	rows, err := db.Query(`
		SELECT ts.name, ts.filename, ts.modality,
		       GROUP_CONCAT(DISTINCT d.name) as diseases,
		       GROUP_CONCAT(DISTINCT g.symbol) as genes
		FROM therapeutic_strategies ts
		LEFT JOIN disease_strategy ds ON ts.id = ds.strategy_id
		LEFT JOIN diseases d ON d.id = ds.disease_id
		LEFT JOIN strategy_gene sg ON ts.id = sg.strategy_id
		LEFT JOIN genes g ON g.id = sg.gene_id
		WHERE ts.name LIKE ? OR ts.modality LIKE ? OR ts.filename LIKE ?
		      OR d.name LIKE ? OR g.symbol LIKE ?
		GROUP BY ts.id
		ORDER BY ts.name
		LIMIT 20`, like, like, like, like, like)
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

		items = append(items, AlfredItem{
			Title:    "🎯 " + name,
			Subtitle: sub,
			Arg:      obsidianURI(filename),
			UID:      "strategy:" + name,
			Text:     &AlfredText{Copy: name, Largetype: name + "\n" + sub},
		})
	}
	return items
}

// -----------------------------------------------------------------------
// Search: zettels
// -----------------------------------------------------------------------

func searchZettels(db *sql.DB, q string) []AlfredItem {
	like := "%" + q + "%"
	rows, err := db.Query(`
		SELECT z.fact, z.filename, z.category,
		       GROUP_CONCAT(DISTINCT d.name) as diseases,
		       GROUP_CONCAT(DISTINCT g.symbol) as genes
		FROM zettels z
		LEFT JOIN disease_zettel dz ON z.id = dz.zettel_id
		LEFT JOIN diseases d ON d.id = dz.disease_id
		LEFT JOIN zettel_gene zg ON z.id = zg.zettel_id
		LEFT JOIN genes g ON g.id = zg.gene_id
		WHERE z.fact LIKE ? OR z.category LIKE ? OR z.filename LIKE ?
		      OR d.name LIKE ? OR g.symbol LIKE ?
		GROUP BY z.id
		ORDER BY z.fact
		LIMIT 20`, like, like, like, like, like)
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

		items = append(items, AlfredItem{
			Title:    fact,
			Subtitle: sub,
			Arg:      obsidianURI(filename),
			UID:      "zettel:" + filename,
			Text:     &AlfredText{Copy: fact, Largetype: fact},
		})
	}
	return items
}

// -----------------------------------------------------------------------
// Wide search: all entity types
// -----------------------------------------------------------------------

func searchAll(db *sql.DB, q string) []AlfredItem {
	var items []AlfredItem
	items = append(items, searchDiseases(db, q)...)
	items = append(items, searchGenes(db, q)...)
	items = append(items, searchPapers(db, q)...)
	items = append(items, searchTrials(db, q)...)
	items = append(items, searchStrategies(db, q)...)
	items = append(items, searchZettels(db, q)...)

	// Cap total results
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
		os.Exit(1)
	}

	// --zk flag for backwards compat with the zk Alfred keyword
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
			Subtitle: "Type freely, or use d: g: p: t: s: z: to filter by type",
		})
	} else if query == "" && filter != "" {
		// Show hint for the filter
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

	output := AlfredOutput{Items: items}
	enc := json.NewEncoder(os.Stdout)
	enc.SetEscapeHTML(false)
	enc.Encode(output)
}
