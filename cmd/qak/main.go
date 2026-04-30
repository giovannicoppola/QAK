package main

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"math"
	"os"
	"path/filepath"
	"strconv"
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
	Valid        *bool             `json:"valid,omitempty"`
	Text         *AlfredText       `json:"text,omitempty"`
	Mods         map[string]AlfMod `json:"mods,omitempty"`
	Variables    AlfredVariables   `json:"variables,omitempty"`
	UID          string            `json:"uid,omitempty"`
}

type AlfredIcon struct {
	Path string `json:"path"`
}

type AlfredText struct {
	Copy      string `json:"copy,omitempty"`
	Largetype string `json:"largetype,omitempty"`
}

type AlfredVariables map[string]interface{}

type AlfMod struct {
	Arg       string          `json:"arg"`
	Subtitle  string          `json:"subtitle"`
	Variables AlfredVariables `json:"variables,omitempty"`
}

type AlfredOutput struct {
	Items         []AlfredItem    `json:"items"`
	Variables     AlfredVariables `json:"variables,omitempty"`
	SkipKnowledge bool            `json:"skipknowledge,omitempty"`
}

// Paths

func dbPath() string {
	if p := os.Getenv("QAK_DB"); p != "" {
		return p
	}
	// Try several candidate locations — the binary may be launched through
	// a symlinked Alfred workflow directory, so the invocation path can
	// point somewhere that doesn't contain qak.db.
	var candidates []string
	if exe, err := os.Executable(); err == nil {
		candidates = append(candidates, filepath.Dir(exe))
		if real, err := filepath.EvalSymlinks(exe); err == nil {
			candidates = append(candidates, filepath.Dir(real))
		}
	}
	arg0 := os.Args[0]
	if !filepath.IsAbs(arg0) {
		if wd, err := os.Getwd(); err == nil {
			arg0 = filepath.Join(wd, arg0)
		}
	}
	candidates = append(candidates, filepath.Dir(arg0))
	for _, dir := range candidates {
		p := filepath.Join(dir, "qak.db")
		if _, err := os.Stat(p); err == nil {
			return p
		}
	}
	return filepath.Join(candidates[0], "qak.db")
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

// -----------------------------------------------------------------------
// Flag-based autocomplete (--disease, --gene, etc.)
// -----------------------------------------------------------------------

type flagDef struct {
	flag     string // e.g. "disease"
	desc     string // shown in subtitle
	icon     string // emoji
	filter   string // maps to existing filter type
}

var flagDefs = []flagDef{
	{"disease", "Filter by disease", "🦠", "disease"},
	{"gene", "Filter by gene", "🧬", "gene"},
	{"paper", "Filter by paper", "📄", "paper"},
	{"trial", "Filter by clinical trial", "💊", "trial"},
	{"strategy", "Filter by therapeutic strategy", "🎯", "strategy"},
	{"zettel", "Filter by zettel", "📝", "zettel"},
}

func isTypingFlag(raw string) bool {
	trimmed := strings.TrimSpace(raw)
	return strings.HasSuffix(trimmed, "--")
}

func isPartialFlag(raw string) bool {
	if strings.HasSuffix(raw, " ") {
		return false
	}
	trimmed := strings.TrimSpace(raw)
	if !strings.Contains(trimmed, "--") {
		return false
	}
	idx := strings.LastIndex(trimmed, "--")
	after := trimmed[idx+2:]
	if after == "" {
		return false
	}
	return !strings.Contains(after, " ")
}

func getBaseQuery(raw string) string {
	idx := strings.LastIndex(raw, "--")
	if idx < 0 {
		return ""
	}
	return strings.TrimSpace(raw[:idx])
}

func getPartialFlagText(raw string) string {
	trimmed := strings.TrimSpace(raw)
	idx := strings.LastIndex(trimmed, "--")
	if idx < 0 {
		return ""
	}
	return strings.TrimSpace(trimmed[idx+2:])
}

func buildFlagSuggestions(raw string) []AlfredItem {
	base := getBaseQuery(raw)
	partial := ""
	if isPartialFlag(raw) {
		partial = strings.ToLower(getPartialFlagText(raw))
	}

	falseVal := false
	var items []AlfredItem
	for _, f := range flagDefs {
		if partial != "" && !strings.Contains(f.flag, partial) {
			continue
		}
		ac := "--" + f.flag + " "
		if base != "" {
			ac = base + " " + ac
		}
		items = append(items, AlfredItem{
			Title:        f.icon + " --" + f.flag,
			Subtitle:     f.desc,
			Autocomplete: ac,
			Valid:        &falseVal,
			UID:          "flag:" + f.flag,
		})
	}
	return items
}

func listEntityValues(db *sql.DB, filter, query string) []AlfredItem {
	switch filter {
	case "disease":
		return listDiseases(db, query)
	case "gene":
		return listGenes(db, query)
	case "paper":
		return listPapers(db, query)
	case "trial":
		return listTrials(db, query)
	case "strategy":
		return listStrategies(db, query)
	case "zettel":
		return listZettels(db, query)
	}
	return nil
}

func listDiseases(db *sql.DB, q string) []AlfredItem {
	var where string
	var args []interface{}
	if q != "" {
		where, args = fuzzyWhere(q, []string{"d.name"})
	} else {
		where = "1=1"
	}
	rows, err := db.Query(`
		SELECT d.name FROM diseases d WHERE `+where+`
		ORDER BY (SELECT COUNT(*) FROM disease_paper dp WHERE dp.disease_id = d.id) DESC
		LIMIT 30`, args...)
	if err != nil {
		return nil
	}
	defer rows.Close()
	falseVal := false
	var items []AlfredItem
	for rows.Next() {
		var name string
		rows.Scan(&name)
		items = append(items, AlfredItem{
			Title:        "🦠 " + name,
			Subtitle:     "Select to filter by this disease",
			Autocomplete: "--disease " + name + " ",
			Valid:        &falseVal,
			UID:          "pick:disease:" + name,
		})
	}
	return items
}

func listGenes(db *sql.DB, q string) []AlfredItem {
	var where string
	var args []interface{}
	if q != "" {
		where, args = fuzzyWhere(q, []string{"g.symbol", "g.full_name"})
	} else {
		where = "1=1"
	}
	rows, err := db.Query(`
		SELECT g.symbol FROM genes g WHERE `+where+`
		ORDER BY (SELECT COUNT(*) FROM gene_paper gp WHERE gp.gene_id = g.id) DESC
		LIMIT 30`, args...)
	if err != nil {
		return nil
	}
	defer rows.Close()
	falseVal := false
	var items []AlfredItem
	for rows.Next() {
		var symbol string
		rows.Scan(&symbol)
		items = append(items, AlfredItem{
			Title:        "🧬 " + symbol,
			Subtitle:     "Select to filter by this gene",
			Autocomplete: "--gene " + symbol + " ",
			Valid:        &falseVal,
			UID:          "pick:gene:" + symbol,
		})
	}
	return items
}

func listPapers(db *sql.DB, q string) []AlfredItem {
	var where string
	var args []interface{}
	if q != "" {
		where, args = fuzzyWhere(q, []string{"p.citekey", "p.first_author", "p.title"})
	} else {
		where = "1=1"
	}
	rows, err := db.Query(`
		SELECT p.citekey, p.first_author, p.year, p.title FROM papers p WHERE `+where+`
		ORDER BY p.year DESC LIMIT 30`, args...)
	if err != nil {
		return nil
	}
	defer rows.Close()
	falseVal := false
	var items []AlfredItem
	for rows.Next() {
		var citekey string
		var author, title sql.NullString
		var year sql.NullInt64
		rows.Scan(&citekey, &author, &year, &title)
		display := citekey
		if a := orEmpty(author); a != "" {
			display = a
			if year.Valid {
				display += fmt.Sprintf(" (%d)", year.Int64)
			}
		}
		if t := orEmpty(title); t != "" {
			if len(t) > 50 {
				t = t[:50] + "…"
			}
			display += " — " + t
		}
		items = append(items, AlfredItem{
			Title:        "📄 " + display,
			Subtitle:     "Select to filter by this paper",
			Autocomplete: "--paper " + citekey + " ",
			Valid:        &falseVal,
			UID:          "pick:paper:" + citekey,
		})
	}
	return items
}

func listTrials(db *sql.DB, q string) []AlfredItem {
	var where string
	var args []interface{}
	if q != "" {
		where, args = fuzzyWhere(q, []string{"ct.trial_name", "ct.drug", "ct.company"})
	} else {
		where = "1=1"
	}
	rows, err := db.Query(`
		SELECT ct.trial_name FROM clinical_trials ct WHERE `+where+`
		ORDER BY ct.trial_name LIMIT 30`, args...)
	if err != nil {
		return nil
	}
	defer rows.Close()
	falseVal := false
	var items []AlfredItem
	for rows.Next() {
		var name string
		rows.Scan(&name)
		items = append(items, AlfredItem{
			Title:        "💊 " + name,
			Subtitle:     "Select to filter by this trial",
			Autocomplete: "--trial " + name + " ",
			Valid:        &falseVal,
			UID:          "pick:trial:" + name,
		})
	}
	return items
}

func listStrategies(db *sql.DB, q string) []AlfredItem {
	var where string
	var args []interface{}
	if q != "" {
		where, args = fuzzyWhere(q, []string{"ts.name", "ts.modality"})
	} else {
		where = "1=1"
	}
	rows, err := db.Query(`
		SELECT ts.name FROM therapeutic_strategies ts WHERE `+where+`
		ORDER BY ts.name LIMIT 30`, args...)
	if err != nil {
		return nil
	}
	defer rows.Close()
	falseVal := false
	var items []AlfredItem
	for rows.Next() {
		var name string
		rows.Scan(&name)
		items = append(items, AlfredItem{
			Title:        "🎯 " + name,
			Subtitle:     "Select to filter by this strategy",
			Autocomplete: "--strategy " + name + " ",
			Valid:        &falseVal,
			UID:          "pick:strategy:" + name,
		})
	}
	return items
}

func listZettels(db *sql.DB, q string) []AlfredItem {
	var where string
	var args []interface{}
	if q != "" {
		where, args = fuzzyWhere(q, []string{"z.fact", "z.category"})
	} else {
		where = "1=1"
	}
	rows, err := db.Query(`
		SELECT z.fact FROM zettels z WHERE `+where+`
		ORDER BY z.fact LIMIT 30`, args...)
	if err != nil {
		return nil
	}
	defer rows.Close()
	falseVal := false
	var items []AlfredItem
	for rows.Next() {
		var fact string
		rows.Scan(&fact)
		items = append(items, AlfredItem{
			Title:        "📝 " + fact,
			Subtitle:     "Select to filter by this zettel",
			Autocomplete: "--zettel " + fact + " ",
			Valid:        &falseVal,
			UID:          "pick:zettel:" + fact,
		})
	}
	return items
}

// splitEntityAndQuery tries to split "Alzheimer's Disease prevalence gwas"
// into (entity="Alzheimer's Disease", query="prevalence gwas") by finding the
// longest prefix that matches an actual entity name in the DB.
func splitEntityAndQuery(db *sql.DB, flagName, fullVal string) (entity, query string) {
	if fullVal == "" {
		return "", ""
	}
	table := ""
	col := ""
	switch flagName {
	case "disease":
		table, col = "diseases", "name"
	case "gene":
		table, col = "genes", "symbol"
	case "paper":
		table, col = "papers", "citekey"
	case "trial":
		table, col = "clinical_trials", "trial_name"
	case "strategy":
		table, col = "therapeutic_strategies", "name"
	case "zettel":
		table, col = "zettels", "fact"
	default:
		return fullVal, ""
	}

	words := strings.Fields(fullVal)
	// Try longest prefix first (all words), then shrink
	for n := len(words); n >= 1; n-- {
		candidate := strings.Join(words[:n], " ")
		var count int
		db.QueryRow("SELECT COUNT(*) FROM "+table+" WHERE "+col+" = ?", candidate).Scan(&count)
		if count > 0 {
			rest := strings.TrimSpace(strings.Join(words[n:], " "))
			return candidate, rest
		}
	}
	// No exact match — treat everything as a fuzzy query
	return "", fullVal
}

// filterExactEntity removes same-type results whose UID doesn't match the
// exact entity name. E.g. for --disease ALS, drop disease:PSP but keep
// paper:* and prop:ALS:*.
func filterExactEntity(items []AlfredItem, flagName, entity string) []AlfredItem {
	prefix := flagName + ":"
	if flagName == "trial" {
		prefix = "trial:"
	}
	var filtered []AlfredItem
	for _, it := range items {
		if strings.HasPrefix(it.UID, prefix) {
			// Same entity type — keep only if UID matches exactly
			if it.UID == prefix+entity {
				filtered = append(filtered, it)
			}
		} else {
			// Different type (property, paper, etc.) — always keep
			filtered = append(filtered, it)
		}
	}
	return filtered
}

// parseFlags extracts --flag value pairs from query, returns remaining text and flag map
func parseFlags(raw string) (remaining string, flags map[string]string) {
	flags = make(map[string]string)
	parts := strings.Fields(raw)
	var rest []string
	i := 0
	for i < len(parts) {
		if strings.HasPrefix(parts[i], "--") {
			flagName := strings.TrimPrefix(parts[i], "--")
			valid := false
			for _, f := range flagDefs {
				if f.flag == flagName {
					valid = true
					break
				}
			}
			if valid && i+1 < len(parts) && !strings.HasPrefix(parts[i+1], "--") {
				// Collect all value words until next flag or end
				var valParts []string
				i++
				for i < len(parts) && !strings.HasPrefix(parts[i], "--") {
					valParts = append(valParts, parts[i])
					i++
				}
				flags[flagName] = strings.Join(valParts, " ")
				continue
			} else if valid {
				flags[flagName] = ""
				i++
				continue
			}
		}
		rest = append(rest, parts[i])
		i++
	}
	remaining = strings.Join(rest, " ")
	return
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

		item := makeItem("🦠 "+name, sub, filename, "disease:"+name)
		item.Mods["ctrl"] = AlfMod{
			Arg:      name,
			Subtitle: "⌃↵ Search ClinicalTrials.gov",
			Variables: AlfredVariables{"myMode": "cct"},
		}
		item.Mods["alt"] = AlfMod{
			Arg:      name,
			Subtitle: "⌥↵ GWAS Catalog (trait)",
			Variables: AlfredVariables{"myMode": "gwas_trait", "myENTRY_Q": name},
		}
		items = append(items, item)
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

		item := makeItem("🧬 "+symbol, sub, filename, "gene:"+symbol)
		item.Mods["alt"] = AlfMod{
			Arg:      symbol,
			Subtitle: "⌥↵ GWAS Catalog (gene)",
			Variables: AlfredVariables{"myMode": "gwas_gene", "myENTRY_Q": symbol},
		}
		item.Mods["cmd+alt"] = AlfMod{
			Arg:      symbol,
			Subtitle: "⌥⌘↵ Gene Browser",
			Variables: AlfredVariables{"myMode": "gene_browser", "myENTRY_Q": symbol},
		}
		items = append(items, item)
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
		       p.n_total, p.n_loci, p.obs_summary, p.obs_source, p.title, p.journal,
		       p.abstract, p.distinction
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
		var abstract, distinction sql.NullString
		var year, nTotal, nLoci sql.NullInt64
		rows.Scan(&citekey, &filename, &author, &year, &studyType, &nTotal, &nLoci,
			&summary, &obsSource, &title, &journal, &abstract, &distinction)

		displayTitle := citekey
		if s := orEmpty(author); s != "" {
			displayTitle = s
			if year.Valid {
				displayTitle += fmt.Sprintf(" (%d)", year.Int64)
			}
		}
		// Append paper title for context
		if t := orEmpty(title); t != "" {
			if len(t) > 60 {
				t = t[:60] + "…"
			}
			displayTitle += " — " + t
		}

		sub := join([]string{
			orEmpty(distinction),
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
		abstractText := orEmpty(abstract)

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

		// Cmd modifier: show abstract if available, else full note
		cmdArg := truncate(body, 10000)
		cmdSub := "⌘↵ Copy full note"
		if abstractText != "" {
			cmdArg = truncate(abstractText, 10000)
			cmdSub = "⌘↵ Copy abstract"
		}

		item := AlfredItem{
			Title:    "📄 " + displayTitle,
			Subtitle: sub,
			Arg:      argText,
			UID:      "paper:" + citekey,
			Text:     &AlfredText{Copy: argText, Largetype: largeText},
			Mods: map[string]AlfMod{
				"shift": {Arg: obsidianURI(filename), Subtitle: "⇧↵ Open in Obsidian"},
				"cmd":   {Arg: cmdArg, Subtitle: cmdSub},
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
		       heritability_twin, heritability_gwas, disease_duration
		FROM diseases`)
	if err == nil {
		defer diseaseRows.Close()
		for diseaseRows.Next() {
			var name, filename string
			var prev, incid, duration sql.NullFloat64
			var nUS, gwasN, gwasLoci, wesN, wesLoci sql.NullInt64
			var risk, omim, mondo, orphanet sql.NullString
			var gwasPaper, wesPaper, herTwin, herGwas sql.NullString
			diseaseRows.Scan(&name, &filename, &prev, &incid, &nUS, &risk,
				&omim, &mondo, &orphanet, &gwasN, &gwasLoci, &gwasPaper,
				&wesN, &wesLoci, &wesPaper, &herTwin, &herGwas, &duration)

			add := func(label, val, unit string) {
				if val != "" {
					rows = append(rows, propRow{name, label, val, unit, filename, "🦠"})
				}
			}
			add("prevalence", fmtFloat(prev), " /100k")
			add("incidence", fmtFloat(incid), " /100k")
			add("US patients", fmtNum(nUS), "")
			add("lifetime risk", orEmpty(risk), "")
			add("disease duration", fmtFloat(duration), " years")
			add("OMIM", orEmpty(omim), "")
			add("MONDO", orEmpty(mondo), "")
			add("Orphanet", orEmpty(orphanet), "")
			// GWAS/WES stats: append citekey in parentheses when available
			gwp := orEmpty(gwasPaper)
			if v := fmtNum(gwasN); v != "" {
				suffix := ""
				if gwp != "" { suffix = " (" + gwp + ")" }
				add("GWAS largest N", v, suffix)
			}
			if v := fmtNum(gwasLoci); v != "" {
				suffix := ""
				if gwp != "" { suffix = " (" + gwp + ")" }
				add("GWAS loci", v, suffix)
			}
			wep := orEmpty(wesPaper)
			if v := fmtNum(wesN); v != "" {
				suffix := ""
				if wep != "" { suffix = " (" + wep + ")" }
				add("WES largest N", v, suffix)
			}
			if v := fmtNum(wesLoci); v != "" {
				suffix := ""
				if wep != "" { suffix = " (" + wep + ")" }
				add("WES loci", v, suffix)
			}
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

		mods := map[string]AlfMod{
			"shift": {Arg: obsidianURI(r.filename), Subtitle: "⇧↵ Open in Obsidian"},
		}

		subtitle := "↵ copy · ⇧↵ open Obsidian"

		// For prevalence/incidence, add Cmd+Enter to drill into derived measures
		if r.label == "prevalence" || r.label == "incidence" {
			mods["cmd"] = AlfMod{
				Arg:      clipText,
				Subtitle: "⌘↵ Derived measures",
				Variables: AlfredVariables{
					"myIter": true,
					"myArg":  fmt.Sprintf("epi:%s:%s:%s", r.entity, r.label, r.value),
				},
			}
			subtitle = "↵ copy · ⌘↵ derived measures · ⇧↵ Obsidian"
		}

		// For GWAS/WES loci, add Cmd+Enter to drill into associated genes
		if r.label == "GWAS loci" || r.label == "WES loci" {
			mods["cmd"] = AlfMod{
				Arg:      clipText,
				Subtitle: "⌘↵ Show associated genes",
				Variables: AlfredVariables{
					"myIter": true,
					"myArg":  fmt.Sprintf("genes:%s", r.entity),
				},
			}
			subtitle = "↵ copy · ⌘↵ genes · ⇧↵ Obsidian"
		}

		items = append(items, AlfredItem{
			Title:    r.icon + " " + r.entity + " — " + r.label + ": " + displayVal,
			Subtitle: subtitle,
			Arg:      clipText,
			UID:      "prop:" + r.entity + ":" + r.label,
			Text:     &AlfredText{Copy: clipText, Largetype: clipText},
			Mods:     mods,
		})

		if len(items) >= 20 {
			break
		}
	}
	return items
}

// -----------------------------------------------------------------------
// Epi calculator: derive measures from a rate per 100k
// -----------------------------------------------------------------------

// Population reference data (approximate, 2024 estimates)
const (
	popUS       = 335_000_000
	popEU5      = 328_000_000 // DE+FR+IT+ES+UK
	popWorld    = 8_100_000_000
	birthsUS    = 3_600_000 // yearly US births
	birthsWorld = 140_000_000
)

// US Census 5-year age bands (2024 estimates, thousands → actual)
// Source: US Census Bureau population estimates
var censusUS = map[string]int64{
	"0-4": 19_400_000, "5-9": 20_200_000, "10-14": 21_300_000,
	"15-19": 21_600_000, "20-24": 21_800_000, "25-29": 23_000_000,
	"30-34": 23_100_000, "35-39": 22_200_000, "40-44": 21_000_000,
	"45-49": 20_400_000, "50-54": 20_600_000, "55-59": 21_200_000,
	"60-64": 21_500_000, "65-69": 19_600_000, "70-74": 16_400_000,
	"75-79": 11_900_000, "80-84": 7_400_000, "85+": 7_100_000,
}

// EU-5 5-year age bands (2024 estimates: DE+FR+IT+ES+UK)
var censusEU5 = map[string]int64{
	"0-4": 15_100_000, "5-9": 16_200_000, "10-14": 17_100_000,
	"15-19": 17_500_000, "20-24": 18_200_000, "25-29": 18_800_000,
	"30-34": 19_500_000, "35-39": 20_200_000, "40-44": 21_800_000,
	"45-49": 22_100_000, "50-54": 23_300_000, "55-59": 22_800_000,
	"60-64": 20_600_000, "65-69": 18_200_000, "70-74": 15_800_000,
	"75-79": 12_100_000, "80-84": 8_600_000, "85+": 7_200_000,
}

// Ordered list of 5-year band boundaries for range lookups
var ageBands = []struct {
	label    string
	lo, hi   int // hi = -1 means open-ended (85+)
}{
	{"0-4", 0, 4}, {"5-9", 5, 9}, {"10-14", 10, 14}, {"15-19", 15, 19},
	{"20-24", 20, 24}, {"25-29", 25, 29}, {"30-34", 30, 34}, {"35-39", 35, 39},
	{"40-44", 40, 44}, {"45-49", 45, 49}, {"50-54", 50, 54}, {"55-59", 55, 59},
	{"60-64", 60, 64}, {"65-69", 65, 69}, {"70-74", 70, 74}, {"75-79", 75, 79},
	{"80-84", 80, 84}, {"85+", 85, -1},
}

// popForRange returns the total population for an arbitrary age range
// by summing the 5-year bands that overlap. Supports: "65-74", "0-17", "85+", "80+"
func popForRange(ageRange string, census map[string]int64) int64 {
	ageRange = strings.TrimSpace(ageRange)
	var lo, hi int
	openEnded := false

	if strings.HasSuffix(ageRange, "+") {
		lo, _ = strconv.Atoi(strings.TrimSuffix(ageRange, "+"))
		hi = 999
		openEnded = true
	} else if parts := strings.SplitN(ageRange, "-", 2); len(parts) == 2 {
		lo, _ = strconv.Atoi(strings.TrimSpace(parts[0]))
		hi, _ = strconv.Atoi(strings.TrimSpace(parts[1]))
	} else {
		return 0
	}
	_ = openEnded

	var total int64
	for _, band := range ageBands {
		bandHi := band.hi
		if bandHi == -1 {
			bandHi = 999 // open-ended
		}
		// Band overlaps range if band.lo <= hi AND bandHi >= lo
		if band.lo <= hi && bandHi >= lo {
			total += census[band.label]
		}
	}
	return total
}

// parseAgeRates parses "65-74:5000, 75-84:14000, 85+:35000" into pairs
type ageRate struct {
	ageRange   string
	ratePer100k float64
}

func parseAgeRates(s string) []ageRate {
	s = strings.TrimSpace(s)
	if s == "" {
		return nil
	}
	var result []ageRate
	for _, part := range strings.Split(s, ",") {
		part = strings.TrimSpace(part)
		idx := strings.LastIndex(part, ":")
		if idx < 0 {
			continue
		}
		ageStr := strings.TrimSpace(part[:idx])
		rateStr := strings.TrimSpace(part[idx+1:])
		rate, err := strconv.ParseFloat(rateStr, 64)
		if err != nil {
			continue
		}
		result = append(result, ageRate{ageStr, rate})
	}
	return result
}

type epiRow struct {
	label string
	value string
}

func epiCalc(disease, rateType string, ratePer100k float64, ageRates []ageRate) []epiRow {
	var rows []epiRow

	// Original rate
	rows = append(rows, epiRow{
		label: fmt.Sprintf("%s per 100k", rateType),
		value: strconv.FormatFloat(ratePer100k, 'f', -1, 64),
	})

	// Per million
	perMillion := ratePer100k * 10
	rows = append(rows, epiRow{
		label: fmt.Sprintf("%s per million", rateType),
		value: strconv.FormatFloat(perMillion, 'f', -1, 64),
	})

	// 1:N notation
	if ratePer100k > 0 {
		oneIn := 100_000.0 / ratePer100k
		rows = append(rows, epiRow{
			label: fmt.Sprintf("%s (1 in N)", rateType),
			value: fmt.Sprintf("1:%s", fmtLargeInt(int64(math.Round(oneIn)))),
		})
	}

	// Absolute patient/case counts
	rate := ratePer100k / 100_000.0

	addPop := func(popName string, pop int64) {
		n := rate * float64(pop)
		rows = append(rows, epiRow{
			label: fmt.Sprintf("%s %s — %s", rateType, popName, disease),
			value: fmtLargeInt(int64(math.Round(n))),
		})
	}

	addPop("US", popUS)
	addPop("EU-5", popEU5)
	addPop("worldwide", popWorld)

	// Birth-based estimates (meaningful for both prevalence and incidence)
	addBirths := func(label string, births int64) {
		n := rate * float64(births)
		rows = append(rows, epiRow{
			label: fmt.Sprintf("%s %s — %s", rateType, label, disease),
			value: fmtLargeInt(int64(math.Round(n))),
		})
	}
	addBirths("yearly US births", birthsUS)
	addBirths("yearly births worldwide", birthsWorld)

	// Age-stratified rates
	if len(ageRates) > 0 {
		rows = append(rows, epiRow{label: "── by age ──", value: ""})
		for _, ar := range ageRates {
			usAge := popForRange(ar.ageRange, censusUS)
			eu5Age := popForRange(ar.ageRange, censusEU5)
			ageRate := ar.ratePer100k / 100_000.0

			nUS := int64(math.Round(ageRate * float64(usAge)))
			nEU5 := int64(math.Round(ageRate * float64(eu5Age)))

			rows = append(rows, epiRow{
				label: fmt.Sprintf("age %s: %s/100k", ar.ageRange, strconv.FormatFloat(ar.ratePer100k, 'f', -1, 64)),
				value: fmt.Sprintf("US %s · EU-5 %s", fmtLargeInt(nUS), fmtLargeInt(nEU5)),
			})
		}
	}

	return rows
}

func fmtLargeInt(n int64) string {
	if n >= 1_000_000_000 {
		return fmt.Sprintf("%.2fB", float64(n)/1e9)
	}
	if n >= 1_000_000 {
		return fmt.Sprintf("%.2fM", float64(n)/1e6)
	}
	if n >= 1_000 {
		return fmt.Sprintf("%s", commaFmt(n))
	}
	return fmt.Sprintf("%d", n)
}

func commaFmt(n int64) string {
	s := fmt.Sprintf("%d", n)
	if n < 0 {
		return "-" + commaFmt(-n)
	}
	if len(s) <= 3 {
		return s
	}
	var parts []string
	for len(s) > 3 {
		parts = append([]string{s[len(s)-3:]}, parts...)
		s = s[:len(s)-3]
	}
	parts = append([]string{s}, parts...)
	return strings.Join(parts, ",")
}

func epiDrillDown(db *sql.DB, disease, rateType string, ratePer100k float64) []AlfredItem {
	// Look up age-stratified data for this disease
	var ageRates []ageRate
	col := rateType + "_by_age" // prevalence_by_age or incidence_by_age
	var ageStr sql.NullString
	db.QueryRow("SELECT "+col+" FROM diseases WHERE name = ?", disease).Scan(&ageStr)
	if ageStr.Valid {
		ageRates = parseAgeRates(ageStr.String)
	}

	rows := epiCalc(disease, rateType, ratePer100k, ageRates)

	// Build "copy all age rows" text for Cmd modifier on age items
	var ageLines []string
	for _, r := range rows {
		if strings.HasPrefix(r.label, "age ") {
			ageLines = append(ageLines, disease+" "+r.label+": "+r.value)
		}
	}
	allAgeText := strings.Join(ageLines, "\n")

	var items []AlfredItem
	for _, r := range rows {
		// Separator row — "── by age ──" becomes the "copy all" row
		if r.value == "" {
			if len(ageLines) > 0 {
				items = append(items, AlfredItem{
					Title:    r.label,
					Subtitle: fmt.Sprintf("↵ copy all %d age ranges", len(ageLines)),
					Arg:      allAgeText,
					Text:     &AlfredText{Copy: allAgeText, Largetype: allAgeText},
					UID:      "epi:" + disease + ":all_ages",
				})
			} else {
				items = append(items, AlfredItem{
					Title: r.label,
				})
			}
			continue
		}
		clipText := disease + " " + r.label + ": " + r.value
		item := AlfredItem{
			Title:    "📊 " + r.label + ": " + r.value,
			Subtitle: "↵ copy",
			Arg:      clipText,
			UID:      "epi:" + disease + ":" + r.label,
			Text:     &AlfredText{Copy: clipText, Largetype: clipText},
		}
		items = append(items, item)
	}
	return items
}

// -----------------------------------------------------------------------
// Gene drill-down: show genes associated with a disease
// -----------------------------------------------------------------------

func genesDrillDown(db *sql.DB, disease string) []AlfredItem {
	rows, err := db.Query(`
		SELECT g.symbol, g.filename, g.full_name, g.chromosome, g.protein_length,
		       (SELECT COUNT(*) FROM gene_paper gp WHERE gp.gene_id = g.id)
		FROM genes g
		JOIN disease_gene dg ON g.id = dg.gene_id
		JOIN diseases d ON d.id = dg.disease_id
		WHERE d.name = ?
		ORDER BY (SELECT COUNT(*) FROM gene_paper gp WHERE gp.gene_id = g.id) DESC`,
		disease)
	if err != nil {
		return nil
	}
	defer rows.Close()

	var items []AlfredItem
	for rows.Next() {
		var symbol, filename string
		var fullName, chrom sql.NullString
		var protLen, nPapers sql.NullInt64
		rows.Scan(&symbol, &filename, &fullName, &chrom, &protLen, &nPapers)

		sub := join([]string{
			orEmpty(fullName),
			func() string {
				if s := orEmpty(chrom); s != "" {
					return "chr" + s
				}
				return ""
			}(),
			fmt.Sprintf("%d papers", nPapers.Int64),
		})

		item := makeItem("🧬 "+symbol, sub, filename, "gene:"+symbol)
		item.Mods["alt"] = AlfMod{
			Arg:      symbol,
			Subtitle: "⌥↵ GWAS Catalog (gene)",
			Variables: AlfredVariables{"myMode": "gwas_gene", "myENTRY_Q": symbol},
		}
		item.Mods["cmd+alt"] = AlfMod{
			Arg:      symbol,
			Subtitle: "⌥⌘↵ Gene Browser",
			Variables: AlfredVariables{"myMode": "gene_browser", "myENTRY_Q": symbol},
		}
		items = append(items, item)
	}

	if len(items) == 0 {
		items = append(items, AlfredItem{
			Title:    "No genes linked to " + disease,
			Subtitle: "Check disease_gene junction table",
		})
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

	db, err := sql.Open("sqlite3", dbPath()+"?mode=ro")
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error opening database: %v\n", err)
		os.Exit(1)
	}
	defer db.Close()

	// Check for recursive drill-down via Alfred variables
	myArg := os.Getenv("myArg")
	iterVal := os.Getenv("myIter")
	if myArg != "" && (iterVal == "1" || iterVal == "true") {
		// Parse epi drill-down: "epi:DISEASE:TYPE:RATE"
		if strings.HasPrefix(myArg, "epi:") {
			parts := strings.SplitN(myArg[4:], ":", 3)
			if len(parts) == 3 {
				disease := parts[0]
				rateType := parts[1]
				rate, err := strconv.ParseFloat(parts[2], 64)
				if err == nil {
					items := epiDrillDown(db, disease, rateType, rate)
					total := len(items)
					for i := range items {
						if items[i].Subtitle != "" {
							items[i].Subtitle = fmt.Sprintf("%s/%s %s", commaFmt(int64(i+1)), commaFmt(int64(total)), items[i].Subtitle)
						} else {
							items[i].Subtitle = fmt.Sprintf("%s/%s", commaFmt(int64(i+1)), commaFmt(int64(total)))
						}
					}
					output := AlfredOutput{Items: items, SkipKnowledge: true}
					enc := json.NewEncoder(os.Stdout)
					enc.SetEscapeHTML(false)
					enc.Encode(output)
					return
				}
			}
		}

		// Parse gene drill-down: "genes:DISEASE_NAME"
		if strings.HasPrefix(myArg, "genes:") {
			disease := myArg[6:]
			items := genesDrillDown(db, disease)
			total := len(items)
			for i := range items {
				if items[i].Subtitle != "" {
					items[i].Subtitle = fmt.Sprintf("%s/%s %s", commaFmt(int64(i+1)), commaFmt(int64(total)), items[i].Subtitle)
				} else {
					items[i].Subtitle = fmt.Sprintf("%s/%s", commaFmt(int64(i+1)), commaFmt(int64(total)))
				}
			}
			output := AlfredOutput{Items: items, SkipKnowledge: true}
			enc := json.NewEncoder(os.Stdout)
			enc.SetEscapeHTML(false)
			enc.Encode(output)
			return
		}
	}

	raw := strings.Join(os.Args[1:], " ")

	// Legacy --zk alias
	if strings.HasPrefix(raw, "--zk ") {
		raw = "zk:" + raw[5:]
	} else if raw == "--zk" {
		raw = "zk:"
	}

	var items []AlfredItem

	// Flag autocomplete: user is typing "--" or "--dis..." → show flag options
	if isTypingFlag(raw) || isPartialFlag(raw) {
		items = buildFlagSuggestions(raw)
		if len(items) == 0 {
			items = append(items, AlfredItem{
				Title:    "Unknown flag",
				Subtitle: "Available: --disease --gene --paper --trial --strategy --zettel",
			})
		}
	} else if strings.Contains(raw, "--") {
		_, flags := parseFlags(raw)

		if len(flags) == 1 {
			for flagName, flagVal := range flags {
				if flagVal == "" {
					// Just selected the flag, no value yet → show entity list
					items = listEntityValues(db, flagName, "")
				} else {
					// Try to split "ALS prevalence" into entity="ALS" + query="prevalence"
					entity, extra := splitEntityAndQuery(db, flagName, flagVal)

					if entity != "" {
						// Exact entity match found — search using a
						// simplified form of the entity name (first word
						// only, avoids multi-word/parenthesis issues) plus
						// any extra search terms.
						shortName := strings.Fields(entity)[0]
						q := shortName
						if extra != "" {
							q = shortName + " " + extra
						}
						items = searchAll(db, q)
						items = filterExactEntity(items, flagName, entity)
					} else {
						// No exact entity match → broad search across all types
						items = searchAll(db, flagVal)
					}
				}
			}
		}
	} else {
		// Original colon-prefix system still works
		filter, query := parseQuery(raw)

		if query == "" && filter == "" {
			items = append(items, AlfredItem{
				Title:    "Search QAK knowledge base…",
				Subtitle: "Type -- for filters · d: g: p: t: s: z: also work",
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
	}

	if len(items) == 0 {
		items = append(items, AlfredItem{
			Title:    "No results",
			Subtitle: fmt.Sprintf("No matches for \"%s\"", raw),
		})
	}

	// Add x/N counter to each subtitle (position in display order, with thousands separator)
	total := len(items)
	for i := range items {
		counter := fmt.Sprintf("%s/%s", commaFmt(int64(i+1)), commaFmt(int64(total)))
		if items[i].Subtitle != "" {
			items[i].Subtitle = counter + " " + items[i].Subtitle
		} else {
			items[i].Subtitle = counter
		}
	}

	output := AlfredOutput{Items: items, SkipKnowledge: true}
	enc := json.NewEncoder(os.Stdout)
	enc.SetEscapeHTML(false)
	enc.Encode(output)
}
