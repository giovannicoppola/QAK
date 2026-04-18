# Background and Rationale
- I want to be able to generate from my obsidian vault a knowledge database (either JSON or sqlite) which I then plan to query via Alfred. This is around diseases, genes, and literature, and also projects. The database would be built periodically through a dedicated script, so it it fine if it requires some processing. One example: for a disease: ALS I want to be able to access quickly: epidemiology (number of patients in the US), the genes that have been reported, the most recent genetic paper, the largest GWAS and its sample size, projects I am currently working on related to this disease. Initially I thought to create a spreadsheet with this information, but it would be more efficient to compile this information from one (or more) obsidian vaults. 
- In previous thinking and discussions with LLM, I came up with a combination of properties (YAML frontmatter) and in-note content that can be used for this purpose. 
I usually codify note type with the title: notes starting with @ are papers (or books), with ^ are genes, if they include `target` are referred to target programs, and the `project` etc.
- database should be sqlite (faster and more efficient)
- the main sources of information are: 
1) diseases (currently disease name in the note name), 
2) genes (note name starting with `^`)
3) papers (note name starting with `@`)
4) therapeutic strategies, clinical trials (just migrated from roam, will need to reorganize)


# Features to implement
## Use cases
- if I look for the largest GWAS or Exome study, or number of loci, or genes, the paper citekey should be listed in parentehses
- the papers have multiple results (apparently one per property), there is no need for that. I just want the paper (with the title) and upon actioning the short summary (which is already there). Maybe we can add the abstract if actioning with
  shift. 
- there are still some papers without title (e.g. chabriat2009-zh)
- for each paper, we should also record (and show in the subtitle) the reason it is in the database, or whatever 'distinction' it has: for example: largest GWAS for AMD, or 'pathogenesis of glaucoma' etc., so that if it comes up as a result in a
  search I know why it is there
- for each disease add 'disease_duration' property (numerical in years)
- actioning "GWAS loci", or "WES loci" should provide a list of these loci, if such a list exists in the disease note, perhaps under a `## WES genes` section under `Genes`, which would include all genes implicated in this disease, including those
  with no genetic evidence (other therapeutic targets etc.). actioning a gene should link to the gene resources as usual.

# Bugs to fix


 # Implemented Features (no need to revisit)



Main goal is to plan a reorganization of the content of this vault (and possibly others) in a way that will facilitate the creation of the database described above, plus a general improvement in access and content management. Please review
this document, then review all files in the `gitvault` Obsidian vault (`/Users/giovanni.coppola/Library/CloudStorage/OneDrive-RegeneronPharmaceuticals,Inc/MyScripts/myGitHubRepos/gitVault`) and come up with a strategy for reorganization described in a markdown document. Please detail the YAML properties and the text recurrent sections you propose for each note type. Estimate the number of disease, gene, paper etc. notes this reorg would affect. do not make any changes to notes just now, let's come up with a plan first, then try them. 


## for diseases
1. review a few examples (notes: Alzheimer's Disease, ALS (which I have already start to convert), AMD, glaucoma, etc) and propose a system that organizes the information currently included in these notes (and connected ones) using the combination of YAML properties and note text headers. 
## for genes  (starting with `^`)
1. propose an organization that will allow the script to capture the papers, diseases, ongoing therapeutic strategies etc. 
## For papers (starting with `@`). 
1. if there is a block with the #obs tag, put it under a `# OBSummary` header and put this block (header and one-block summary) at the end of the document so that it does not impact the other headers. 
2. add properties using the template
3. if you infer that specific loci are discussed, put them under the `## Loci` header.
4. if there is an abstract block or paragraph (with the #abstract label) put it under a `# Abstract` header making sure it does not interfere with the rest of the note (i.e. if there is content after that, put it under a generic header,
   which could be the citekey (`# myCitekey`)
5. add a `citekey` property with the citekey (which is typically the file name, without the `@`) 

also, in Roam I had zettelkasten notes, key facts to remember, that started with `z:` which I think it has been variably converted (`:` removed because not allowed in file names etc), however they should all start with a z. How would you reorg these? In the alfred app, i envision havind a separate query that searches them for easy access

