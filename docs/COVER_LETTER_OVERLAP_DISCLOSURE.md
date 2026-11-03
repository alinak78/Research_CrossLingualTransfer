# Draft overlap disclosure for the program chairs

Prepared for author review; not sent or submitted. Use only in a venue-permitted disclosure channel. Keep this separate from the anonymous manuscript and do not add identifying repository links to the review PDF.

Dear Program Chairs,

We disclose the relationship between “Whose Facts Count? Complaint Fidelity and Language Equity in Cross-Lingual Legal Intake” and Shetty et al., “Cross Lingual Transfer in Tulu Legal Comprehension: Script-Dependent Improvement and RAG-Induced Knowledge Conflict,” published in the ORACLE 2026 proceedings, pp. 107–133 ([publication record](https://aclanthology.org/2026.oracle-main.8/)).

The source study reports legal-category prediction across script, linguistic priming, and retrieval conditions, and already identifies fact substitution and confabulation. The current manuscript does not claim discovery of those phenomena. It reuses the source study's authored scenarios and labels, and cites its archived results as motivation. Its main results no longer reproduce the historical benchmark tables.

| Material | Relationship to the source study |
|---|---|
| 60 authored scenarios, script representations, English glosses, and reference categories | Reused development material; no new participant sample or independently validated dataset is claimed. |
| 3,420 historical predictions and original script/retrieval findings | Prior evidence; detailed benchmarks remain in the audit artifact, with provenance in Appendix A. |
| Complaint-fidelity framework and proposed attribution content tags | Developed in the current manuscript as a normative and methodological proposal; source-support judgments and legal routing remain distinct. No claim is made that all concepts are novel across the wider literature. |
| 384 local llama3.2:1b generations | New exploratory runs on 16 reused scenarios, crossing three representations, four synthetic English contexts, and two prompt policies. There are 308 valid structures and 76 truncations; two earlier smoke calls are separate. |
| Missing-output bounds, case/category omission, and lexical grouping stress tests | New post-hoc diagnostics relative to the source study; they do not establish validated factual intrusion or population effects. |
| Proposed institutional repair workflow, interface separation, and event record | Design requirements developed in this manuscript, not an implemented service or evidence of user benefit. |

The methodological contribution asks what authorizes a personal assertion and who must repair it, rather than whether a model improves category accuracy. The proposal is accompanied by worked examples, editable reporting artifacts, and a bounded computational demonstration. No expert complaint-fidelity annotations, independent linguistic/legal validation, observed referrals, or community endorsement are claimed. The current experiment uses one small local model and synthetic contexts that repeat scenario glosses; these limitations remain explicit.

We provide this disclosure so that the relationship and additional contribution can be assessed transparently. We do not assume that reframing, additional generations, or this disclosure alone establishes sufficient novelty or publication eligibility.

## Short response if reviewers raise reused-data concerns

The scenarios and historical predictions are reused and explicitly attributed. The original study already identifies fact substitution; we do not claim that observation as new. The current contribution specifies complaint-support judgments separately from category agreement and referral validity, proposes an attribution typology and institutional repair workflow, and supplies new controlled-context generations and post-hoc sensitivity analyses. These are an exploratory demonstration and methodological proposal, not independently adjudicated validation. We ask that the new contribution be assessed on those terms, with the overlap and unresolved limitations retained.
