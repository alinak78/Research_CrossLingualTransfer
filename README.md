# Research_CrossLingualTransfer - ACM FAccT 2027

**Selected niche:** complaint fidelity and language equity in automated legal intake: when retrieved legal context displaces a Tulu speaker's account.

**Primary focus area:** Evaluations and evaluation practices. Secondary: System development and deployment if a safeguard is evaluated.

**Working title:** *Whose Facts Count? Complaint Fidelity and Language Equity in Cross-Lingual Legal Intake*.

## Publication status comes first

The source study is published in the [ORACLE 2026 proceedings](https://aclanthology.org/2026.oracle-main.8/), pages 107-133. It is not an unpublished NLLP draft, despite the old README description. FAccT's exceptions for non-archival workshop work and published papers of at most four pages do not permit resubmitting this same publication. A changed title, formatting, or reanalysis is insufficient.

This folder contains a concrete research adaptation and a clearly marked working manuscript, **not an eligible finished submission**. A distinct complaint-fidelity study with new interventions and validation is specified in the research plan. That study has not been run. Prior results are cited and identified as reused pilot evidence. No conference submission or message to organizers was sent.

## Contents

- [Working draft PDF](output/pdf/facct2027_working_draft.pdf): anonymous ACM single-column format, 14 main pages, one endmatter page, one reference page, and three appendix pages. Includes limitations, ethics/adverse impacts, and AI-use disclosure.
- [Editable manuscript](paper/manuscript.md) and [LaTeX source](paper/main.tex), with [bibliography](paper/references.bib).
- [Research plan](docs/RESEARCH_PLAN.md): niche, what is new, controlled context study, language/legal review, annotation, metrics, and overlap boundary.
- [Submission checklist](docs/SUBMISSION_CHECKLIST.md): verified dates, anonymity, page limits, authorship, review signup, and unresolved requirements.
- [Recomputed results](analysis/RESULTS.md) and [machine-readable results and source hashes](analysis/results.json).
- [Offline audit script](analysis/audit.py): analyzes existing predictions without API calls or extra packages.
- [Pilot abstract](docs/pilot_abstract_NOT_FOR_SUBMISSION.txt): working text only, not a suitable registration abstract for a distinct study.
- [Validation record](docs/VALIDATION.md).

## Reproduce

Run from this folder:

```sh
python3 analysis/audit.py
python3 paper/build_draft.py
```

Edit `paper/manuscript_source.md` for prose changes. `build_draft.py` generates `manuscript.md`, `main.tex`, data-derived tables, and the working abstract; changes to generated files alone will be overwritten. It creates the two manuscript sources and the working pilot abstract, not a PDF. PDF compilation requires a TeX installation with `acmart` and `latexmk`:

```sh
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex
```

The checked PDF is a snapshot of `paper/build/main.pdf`; after future changes copy and visually verify the updated PDF before sharing. The Python audit itself uses only the standard library. It requires the sibling source directory and fails if rows are duplicated, incomplete, or disagree with gold labels or saved scores.

## Immediate timeline

The official abstract cutoff is **October 27, 2026 at 11:59 p.m. Anywhere on Earth**; the full-paper cutoff is **November 3** at the same AoE time. Do not register the published pilot as new work. The final author list and archival/non-archival choice lock at abstract registration. Sources: [CFP](https://facctconference.org/2027/cfp.html), [Author Guide](https://facctconference.org/2027/authorguide.html), checked October 27, 2026.

## Protocol implementation materials

The current PDF has 14 main pages, one endmatter page, one reference page, and three appendix pages (19 total). Appendix B supplies five constructed examples and a reporting specification. Editable companion materials: [protocol examples](docs/PROTOCOL_EXAMPLES.md) and [reporting template](docs/protocol_reporting_template.json). Unmeasured fields remain null; these artifacts are not collected annotations or study results. The download ZIP includes the revised PDF, manuscript sources, audit code/results, and protocol materials.

The latest revision adds an explicit architecture analogy, a capacity-based condition for withholding consequential automated routing, and multilingual disagreement fields. The main-text page limit remains satisfied; appendices remain separate from main content.
