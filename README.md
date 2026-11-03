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

The current PDF has 13 main pages, one endmatter page, one reference page, and eight appendix pages (23 total). Appendix B supplies five constructed examples and a reporting specification. Editable companion materials: [protocol examples](docs/PROTOCOL_EXAMPLES.md) and [reporting template](docs/protocol_reporting_template.json). Unmeasured fields remain null; these artifacts are not collected annotations or study results. The download ZIP includes the revised PDF, manuscript sources, audit code/results, and protocol materials.

The latest revision adds an explicit architecture analogy, a capacity-based condition for withholding consequential automated routing, and multilingual disagreement fields. The main-text page limit remains satisfied; appendices remain separate from main content.


## New model experiment: October 30, 2026

A new exploratory local-model run is complete: **384 calls** on **16 reused development scenarios**, with English-gloss, romanized-Tulu, and Kannada-script queries; four fixed English synthetic-context conditions; and baseline versus fidelity-guard prompts. The installed model is `llama3.2:1b` (1.2B, Q8_0), not the original pilot's three models. There are **308 valid structured outputs and 76 token-limit truncations**. Two earlier truncated smoke-test calls are preserved separately.

[Full experiment report](experiments/runs/2026-10-30_local1b_v2/EXPERIMENT_REPORT.md) · [Raw responses](experiments/runs/2026-10-30_local1b_v2/predictions.jsonl) · [Extracted answers](experiments/runs/2026-10-30_local1b_v2/answers.csv) · [Runner and reproduction instructions](experiments/README.md)

The prompt guard does not consistently improve the descriptive category scores; none of the secondary paired comparisons passes Holm correction. Literal numeric-marker echo is a screening observation, not an expert factual-intrusion label. No new held-out corpus, native-speaker/legal validation, or expert annotation was produced. The manuscript now incorporates these outputs in its abstract, methods, results, limitations, AI disclosure, and Appendix C, while distinguishing automated screening from expert fidelity measurement. These new outputs do not by themselves establish FAccT novelty or eligibility.

## Robustness revision: November 3, 2026

The current paper adds all-attempt missing-marker bounds, completion breakdowns, scenario/category omission diagnostics, lexical dependence stress tests, and a corpus provenance inventory. These are completed offline analyses, not expert validation or new model inference. Appendix D documents the methods and results; main content remains 14 pages. See [mitigations and unresolved gaps](docs/LIMITATION_MITIGATIONS.md) and [full robustness results](analysis/ROBUSTNESS.md). Run `python3 experiments/robustness_audit.py` before rebuilding the paper; the builder reads `analysis/robustness.json`.

## Focused manuscript revision

The current paper removes the historical benchmark tables, detailed script/priming comparisons and full historical statistical appendix from the PDF. Its research questions and main results now emphasize complaint fidelity, the 384 new generations, and institutional correction. Source-study attribution remains explicit; full historical audit files remain available. The latest PDF is 21 pages with 12 main pages. See [revision record](docs/FOCUSED_MANUSCRIPT_REVISION.md). This status supersedes earlier page counts above.

## Governance and contribution revision

The latest manuscript adds a proposed six-tag attribution typology, a five-stage institutional repair workflow, and Appendix E's interface/event specification. The protocol is an openly available candidate method rather than a validated standard. The reporting template is now candidate-2; observed annotation and recourse fields remain null. A separate [draft overlap disclosure](docs/COVER_LETTER_OVERLAP_DISCLOSURE.md) maps reused and additional material and includes a possible reviewer response; it has not been sent. See [revision record](docs/GOVERNANCE_REVISION.md). The checked PDF has 23 pages with 13 main pages; this supersedes earlier page counts. No new inference or expert annotation was performed in this revision.
