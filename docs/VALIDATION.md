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
