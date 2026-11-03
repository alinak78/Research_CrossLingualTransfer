## Latest governance revision - November 3, 2026

The current PDF has 23 pages: main 1-13, ethics/AI 14, references 15, Appendix A 16, B 17-18, C 19-20, D 21-22, and new E 23. Added a proposed six-tag attribution typology, five-stage repair workflow, interface/event specification and candidate-2 template. These are unvalidated design tools; no new expert labels, service observations or inference were added. The separate cover-letter overlap disclosure is drafted but unsent. All 23 pages were rendered and visually checked; no clipping, unresolved citations, overfull boxes, identifying author metadata or author-repository links were found. Inference and robustness artifact hashes are unchanged. See GOVERNANCE_REVISION.md and COVER_LETTER_OVERLAP_DISCLOSURE.md. Earlier build descriptions below are historical.

---

## Latest manuscript focus revision - November 3, 2026

The current PDF has 21 pages: main 1-12, ethics/AI 13, references 14, appendices A-D 15-21. Historical benchmark tables, detailed script/priming results and the full archival comparison appendix have been removed from the PDF; raw data and complete audit artifacts remain. Attribution is retained. Research questions and main results center on the complaint-fidelity framework and new 384-call experiment. All pages were visually checked, with no unresolved citations or overfull boxes. See FOCUSED_MANUSCRIPT_REVISION.md. Earlier page counts and descriptions below are historical.

---

## Current revision: November 3, 2026 robustness audit

This revision supersedes earlier page counts: 24 total pages, main content 1-14, ethics/AI 15, references 16, appendices A-D 17-24. Completed offline sensitivity analyses add all-attempt missing-marker bounds, truncation breakdowns, case/category omission, lexical grouping stress tests and a hash-only corpus inventory. See LIMITATION_MITIGATIONS.md for what is improved and what remains unresolved. There are still 384 main-run model calls, 308 valid structures, 76 truncations, two separate smoke calls and no expert labels, new participants or new inference. Independent linguistic/legal validation, demographic coverage, true template provenance, natural retrieval and multiple-model/repeated-generation evidence remain absent. Earlier checks and planning notes below are historical.

---

## Current status: October 31, 2026 experiment integration

This status supersedes earlier build counts and statements that no new model calls were made. The paper now incorporates 384 fresh local llama3.2:1b calls on 16 reused development scenarios in the abstract, introduction, methods, results, framework evidence table, limitations, conclusion, ethics, AI disclosure, and Appendix C. There are 308 valid structured outputs and 76 token-limit truncations. Two earlier smoke calls remain separate. No expert annotations, independent linguistic/legal validation, participant data, or referral outcomes were added. Automated literal-marker screening is not an expert intrusion measure; no secondary comparison passes its Holm correction. Publication eligibility remains unresolved.

The compiled anonymous ACM PDF has 22 pages: main content 1-14, ethics/AI disclosure 15, references 16, Appendix A 17-18, Appendix B 19-20, and new Appendix C 21-22. All pages were rendered and visually inspected. No clipping, missing glyphs, undefined references, overfull boxes, unresolved table markers, identifying author metadata, or author-repository links were found. The final PDF matches the compiled file. The remaining acmart warning concerns the suppressed reference strip. The experiment packaging script verifies all 384 scheduled unique requests, raw-response payload hashes, 24 complete conditions, explicit denominators, and 18 secondary paired comparisons. Original inference inputs/responses are preserved. Nothing was submitted to OpenReview.

---

Historical notes and prospective requirements follow; their earlier experiment/page status is superseded above.

# FAccT 2027 submission checklist

Rules checked October 27, 2026 against the official [CFP](https://facctconference.org/2027/cfp.html) and [Author Guide](https://facctconference.org/2027/authorguide.html). The supplied PDF/pasted text omitted date values; the live CFP supplies them.

## Dates and registration

| Milestone | Official date |
|---|---|
| Abstract registration | October 27, 2026, 11:59 p.m. Anywhere on Earth |
| Full paper | November 3, 2026, 11:59 p.m. Anywhere on Earth |
| Initial decision | December 22, 2026 |
| Revision and rebuttal | January 28, 2027 |
| Final decision | March 23, 2027 |
| Camera-ready | TBD |
| Conference | June 21-24, 2027 |

The abstract cutoff converts to October 28 at 7:59 a.m. America/New_York (EDT). The paper cutoff converts to November 4 at 6:59 a.m. America/New_York (EST), after the daylight-saving change. Use the official AoE cutoff as authoritative.

- Register a meaningful title/abstract and focus area by the abstract deadline; missing registration prevents full-paper submission.
- All human authors must agree to the author list; the registered author list cannot be changed after the abstract deadline. Do not infer the list from local files: PDF and LaTeX source author lists differ.
- Choose archival/non-archival at registration; the guide says this cannot be changed later. An archival choice remains conditional on prior-publication eligibility. The non-archival option does not bypass the general overlap policy.
- OpenReview accounts need verification; institutional affiliation affects verification time. No account creation or submission was performed in this task.
- Every author must complete the reviewer signup form; do not wait for an invitation to sign up. Reviewers are subsequently invited based on qualifications. Account and signup completion for individual authors remain unverified.

## Format and anonymity

- [x] Review source uses `\documentclass[manuscript,screen,review,anonymous]{acmart}`: single column, anonymous, line-numbered review format.
- [x] Local draft compiles; references resolve. See `VALIDATION.md` for final page counts.
- [x] Names, affiliations, identifying acknowledgements, positionality and competing-interest statements are absent from the review draft.
- [x] Current final PDF metadata, external links, annotations, attachments, third-person self-citations, and identifying sections checked; see `FINAL_CHECK.md`. Recheck supplemental files and any later author revisions.
- [x] Rewritten main content is 14 pages, including figures/tables, within the 14-page limit; no margin/font shrinking. Recheck after later revisions.
- [x] Ethics/adverse impacts and required AI-use statement are on page 15; methodological limitations stay in the main body.
- [x] Complete paired-comparison appendix is in the same PDF on page 17; the main paper reports central findings without requiring it.
- [x] Ethical considerations and AI-use disclosure are drafted. Authors must verify disclosure details, including Gemini version and extent of human review.
- [x] Use ACM-Reference-Format for the bibliography. Authors must still verify final bibliographic fields against originals.

## Evidence and eligibility: unresolved

- [x] Verify publication status: formal ORACLE 2026 proceedings, pages 107-133. The current adaptation cannot be resubmitted as the same work; assess overlap for any future distinct study.
- [ ] If the source is a full archival publication, obtain a genuinely distinct study and substantiate novelty; do not submit the current adaptation as new findings.
- [ ] Complete independent linguistic and legal validation, with consent/review appropriate to the work performed.
- [ ] Run and report the distinct complaint-fidelity study if it is the submission's claimed contribution. Do not put proposed findings in the abstract as completed work.
- [ ] Resolve corpus redistribution, personal information, extraction provenance, historical model versions, and label validity.
- [ ] Have all authors review manuscript, references, code, results, and AI-use statement.

## Presentation

If accepted, at least one author must register, attend, and present. The CFP anticipates in-person attendance with a virtual option for those unable to attend; details follow acceptance. Revision/accepted papers may use 15 main-content pages. Do not apply the extra main-content page to the initial submission.

The package is prepared for author review. It is not submitted, certified eligible, or ready to upload without the checks above.

## Verified publication record

The user supplied https://openreview.net/forum?id=2hoq4EUdbP; OpenReview could not be retrieved through the web tool. Independent primary-source verification found the matching publication in the [ACL Anthology](https://aclanthology.org/2026.oracle-main.8/): Shetty, Setty, Kapanova, and Vidra, ORACLE 2026, pages 107-133, Association for Computational Linguistics. This is a formal proceedings publication exceeding four pages. The workshop/non-archival and short-paper exceptions therefore do not cover resubmitting this same work. Develop a genuinely distinct study and assess the overlap; no eligibility approval has been obtained. The local source README's NLLP-submission description is stale relative to this published record.
