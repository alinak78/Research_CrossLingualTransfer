# Limitation mitigations - November 3, 2026

The revisions add completed sensitivity analyses, not substitute expert or community evidence. No new inference was run during this revision; the local Ollama endpoint was unavailable. Original prompts, schedules, predictions and historical analysis results remain unchanged.

| Concern | Completed improvement | Remaining evidence gap |
|---|---|---|
| No expert adjudication | Distinguish literal-marker bounds from fidelity; keep unmeasured expert and referral fields null. | Independent complaint-support judgments, reliability and legal routing review remain absent. |
| Demographic coverage | Explicitly document zero participants and uncollected dialect/literacy/service metadata; distinguish 60 authored cases from 60 speakers. | Representative or situated speaker evidence cannot be created retrospectively from these texts. |
| Template dependence | Deterministic lexical grouping across five thresholds; equal-group weighting and group omission for the archived Llama3 contrast; case/category omission for every new category-policy contrast. | Lexical groups and category strata do not identify true authoring templates. Tests do not establish independent sampling. |
| Unverified representations/categories | Separate observed completion from language comprehension; limit category results to designated-label agreement; change the proposed linguistic-review gate to precede a confirmatory study. | Independent fluent and legal review remain unperformed. |
| Corpus quality/privacy/rights | Record source hash, 18-record count and unresolved extraction/rights status without court excerpts; keep court text excluded from public artifacts; distinguish pinned new-run metadata from unreconstructed history. | Hashes prove file identity, not extraction accuracy, consent, redaction adequacy or redistribution rights. |
| Single-model synthetic experiment and truncation | Report completion by script/policy, all-attempt marker identification bounds and score leverage; retain invalid outputs and original paired tests; explicitly identify oracle-gloss and context-length confounds. | No additional model, repeated stochastic generations, longer-budget run, natural retrieval or translation validation was executed. |

## Key observations

- Kannada-script conditions contain 58/76 truncated outputs (26/64 baseline, 32/64 guard). English has 17 failures; romanized Tulu has one. This is a configuration-level completion result, not a validated language-comprehension assessment.
- All-attempt missing-marker bounds span [-37.5, +50.0] pp for Kannada relevant-with-details and [-56.25, +31.25] for Kannada irrelevant-with-details. These outcomes cannot determine a direction of marker reduction without assumptions.
- English relevant-with-details has a [-37.5, -12.5] pp finite-sample bound, but it is neither a confidence interval nor expert evidence of safer assistance. The existing paired significance findings are unchanged.
- The archive's Llama3 full-priming retrieval decline remains negative under the reported lexical stress tests; equal-group estimates range from -37.29 to -36.67 pp. This does not rule out semantic templates or validate population inference.

Reproduce with `python3 experiments/robustness_audit.py`. Complete results are in `analysis/ROBUSTNESS.md` and `analysis/robustness.json`; methods and bounds are in manuscript Appendix D. This is post-hoc analysis, not preregistered confirmation. No claim is made that all limitations have been resolved.
