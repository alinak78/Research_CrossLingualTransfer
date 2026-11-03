## Latest governance revision - November 3, 2026

The current PDF has 23 pages: main 1-13, ethics/AI 14, references 15, Appendix A 16, B 17-18, C 19-20, D 21-22, and new E 23. Added a proposed six-tag attribution typology, five-stage repair workflow, interface/event specification and candidate-2 template. These are unvalidated design tools; no new expert labels, service observations or inference were added. The separate cover-letter overlap disclosure is drafted but unsent. All 23 pages were rendered and visually checked; no clipping, unresolved citations, overfull boxes, identifying author metadata or author-repository links were found. Inference and robustness artifact hashes are unchanged. See GOVERNANCE_REVISION.md and COVER_LETTER_OVERLAP_DISCLOSURE.md. Earlier build descriptions below are historical.

---

## Latest manuscript focus revision - November 3, 2026

The current PDF has 21 pages: main 1-12, ethics/AI 13, references 14, appendices A-D 15-21. Historical benchmark tables, detailed script/priming results and the full archival comparison appendix have been removed from the PDF; raw data and complete audit artifacts remain. Attribution is retained. Research questions and main results center on the complaint-fidelity framework and new 384-call experiment. All pages were visually checked, with no unresolved citations or overfull boxes. See FOCUSED_MANUSCRIPT_REVISION.md. Earlier page counts and descriptions below are historical.

---

## Current revision: November 3, 2026 robustness audit

This revision supersedes earlier page counts: 24 total pages, main content 1-14, ethics/AI 15, references 16, appendices A-D 17-24. Completed offline sensitivity analyses add all-attempt missing-marker bounds, truncation breakdowns, case/category omission, lexical grouping stress tests and a hash-only corpus inventory. See LIMITATION_MITIGATIONS.md for what is improved and what remains unresolved. There are still 384 main-run model calls, 308 valid structures, 76 truncations, two separate smoke calls and no expert labels, new participants or new inference. Independent linguistic/legal validation, demographic coverage, true template provenance, natural retrieval and multiple-model/repeated-generation evidence remain absent. The latest 24 pages were rendered and visually checked; no clipping, unresolved citations, overfull boxes, or identifying author metadata were found. Missing-outcome bound formulas passed exhaustive attainable-extrema checks for group sizes 1-4, and every lexical partition covers exactly the 60 distinct cases. Original model-call counts and request hashes remain verified. Earlier checks and planning notes below are historical.

---

## Current status: October 31, 2026 experiment integration

This status supersedes earlier build counts and statements that no new model calls were made. The paper now incorporates 384 fresh local llama3.2:1b calls on 16 reused development scenarios in the abstract, introduction, methods, results, framework evidence table, limitations, conclusion, ethics, AI disclosure, and Appendix C. There are 308 valid structured outputs and 76 token-limit truncations. Two earlier smoke calls remain separate. No expert annotations, independent linguistic/legal validation, participant data, or referral outcomes were added. Automated literal-marker screening is not an expert intrusion measure; no secondary comparison passes its Holm correction. Publication eligibility remains unresolved.

The compiled anonymous ACM PDF has 22 pages: main content 1-14, ethics/AI disclosure 15, references 16, Appendix A 17-18, Appendix B 19-20, and new Appendix C 21-22. All pages were rendered and visually inspected. No clipping, missing glyphs, undefined references, overfull boxes, unresolved table markers, identifying author metadata, or author-repository links were found. The final PDF matches the compiled file. The remaining acmart warning concerns the suppressed reference strip. The experiment packaging script verifies all 384 scheduled unique requests, raw-response payload hashes, 24 complete conditions, explicit denominators, and 18 secondary paired comparisons. Original inference inputs/responses are preserved. Nothing was submitted to OpenReview.

---

Historical notes and prospective requirements follow; their earlier experiment/page status is superseded above.

# Validation record

Checked October 27, 2026.

## Data and analysis

- All 10 main-experiment CSVs contribute 3,420 unique predictions: three models x 19 conditions x 60 authored scenarios.
- Each model-condition group contains all 60 scenario IDs. Primary labels match the consolidated source JSONL, and recomputed correctness matches saved `hits1` on every row.
- Thirty-three explicit invalid primary outputs are counted as errors.
- Six matched contrasts per model yield 18 exploratory tests. Two-sided exact McNemar/binomial tests and Holm correction are recorded in `analysis/results.json`; input files have SHA-256 hashes.
- Exact-test edge checks pass: no discordant cases gives p=1; 0 versus 5 discordant cases gives p=0.0625 in either direction. Adjusted p-values lie between raw p and 1.
- There were no new model calls. No new human annotations or participant data were created. Existing results are reused pilot evidence.

## Manuscript

- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex` completes successfully.
- Final PDF: 17 pages: 14 main-content pages, one dedicated ethics/AI-disclosure page, one references page, and one appendix page. Main content is within the initial 14-page limit.
- Final rendered pages were inspected in five contact sheets covering all 17 pages. No clipping, overlapping text, broken tables, or missing glyphs observed. Citations resolve; no undefined-reference or overfull-box warnings.
- Anonymous review class is enabled. PDF author metadata is absent; PDF subject metadata contains CCS concepts. Prior publication is cited in the third person rather than hidden.
- ACM bibliography uses `ACM-Reference-Format`. The class emits a reference-strip warning because `printacmref=false` suppresses the bottom-page ACM reference strip; the FAccT guide explicitly allows removing this information for initial submissions. This is separate from bibliography styling.
- The working-draft notice is visible on page 1 and says the proposed distinct study has not been executed. The default ACM template footer says “Manuscript submitted to ACM”; this is template wording, not evidence of a submission. Nothing was uploaded to OpenReview.

## Source and policy verification

- Official FAccT 2027 CFP and author guide were checked online. They supply date values absent from the supplied extract.
- The user confirmed the prior study was accepted/published and supplied an OpenReview link. The web tool could not retrieve that link. The matching formal publication was independently verified in ACL Anthology: ORACLE 2026, pages 107-133.
- The prior work therefore does not qualify for the guide's non-archival-workshop or at-most-four-page publication exceptions. This adaptation is not a compliant resubmission of that same work. Eligibility of a future distinct study remains subject to the actual overlap and conference policy.

## Remaining substantive work

Execute the distinct controlled-context experiment and independent linguistic/legal validation described in `RESEARCH_PLAN.md`; obtain required human review; validate historical model metadata, corpus rights and extraction; and update the manuscript and abstract with genuinely new evidence. These are scientific and policy requirements, not formatting defects that can be resolved by editing the present text.

## Full section rewrite

The manuscript was rewritten throughout around complaint fidelity and language equity. It contains a new title and abstract, 10 main sections, ethics/adverse impacts, AI-use disclosure, seven cited references, and an appendix with all 18 paired contrasts. Four main-text tables define the framework and conditions and report accuracy and reversals. Prose is edited in `paper/manuscript_source.md`; the build script generates editable Markdown and ACM LaTeX with tables derived from `analysis/results.json`. The main body is 14 pages, within the initial 14-page limit. No new empirical fidelity results were invented.

## Reviewer-pushback revision

The abstract, introduction, and prior-work comparison now prioritize the epistemological/methodological contribution and explicitly subordinate the reused accuracy results to a diagnostic role. Section 7 is a candidate reusable evaluation protocol, with minimum reporting requirements and constructed tests of adequacy; it claims neither community endorsement nor empirical validation. Section 8 allocates correction burdens and proposed institutional repair responsibilities, with observable recourse outcomes. Limitations distinguish conceptual adequacy from annotation reliability, contextual validity, and ecological transfer.

Final PDF: 17 pages. Main content 1-14; ethics and AI disclosure 15; references 16; complete paired-comparison appendix 17. Anonymous review settings and third-person prior-study citations remain in place. No PDF author metadata, undefined references, unresolved table markers, or overfull boxes were found. All final pages were rendered and visually inspected. The only class warning concerns the suppressed ACM reference strip, allowed for initial FAccT submissions. No empirical result, expert review, or publication-eligibility approval was added.

## Actionable-protocol improvement

Current PDF: 19 pages, with main text 1-14, endmatter 15, references 16, paired-comparison appendix 17, and worked examples/reporting specification 18-19. All pages rendered and visually reviewed. Added five explicitly constructed boundary examples; all-attempt and substantive-only denominators; ambiguity bounds; measurable correction stages and owners; limitations on omissions and uncertainty; and a null-valued portable reporting template. Appendix numbering advances A to B correctly. No new empirical evidence is claimed. The refreshed ZIP was checked for archive integrity and for containing the current PDF.

## Architecture, feasibility, and multilingual disagreement revision

The abstract now opens explicitly as a normative and methodological intervention. The introduction links document retrieval to tool-mediated agent workflows while denying empirical generalization from the pilot to cross-domain agent harms. Related work distinguishes ordinary factual misattribution from adversarial prompt injection using Zhan et al. (Findings ACL 2024), verified against ACL Anthology.

Section 8.2 treats funded review capacity, language support, escalation ownership, and limits as preconditions for consequential automated routing. Where these are unavailable, the proposed system should be withheld from that role; this is a normative feasibility test, not an observed legal-aid cost/staffing finding. Section 7.4 and Appendix B retain code-switching, competing pragmatic readings, original spans, alternative glosses, and reviewer competence as annotation evidence. An English gloss does not adjudicate disagreements by default. The reporting template includes these fields and an explicit capacity assessment.

Final build: 14 main pages, ethics/AI page 15, eight references on page 16, appendices on pages 17-19. Anonymous metadata and all external links checked; no author-repository links, undefined references, unresolved markers, or overfull boxes. All 19 pages rendered and visually inspected. No empirical fidelity results, consensus endorsement, or publication eligibility approval is implied. Download ZIP refreshed with this exact PDF and updated protocol materials.
