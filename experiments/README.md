# New local controlled-context experiments

These are new generations on an exploratory, category-balanced subset of the existing development scenarios. They are **not** a newly collected dataset, a held-out validation, or expert complaint-fidelity annotation. The user requested experiments only; no expert labels are produced.

## Design

- Locally available model: `llama3.2:1b`. This is different from the original pilot's three models.
- Sixteen existing scenarios: two sampled per primary category with a fixed seed.
- Three query representations: English gloss, romanized Tulu, and Kannada-script Tulu.
- Four English synthetic-context conditions: no context; a relevant illustrative case; the same relevant case plus source-only age/year details; and a different-category illustrative case with those details.
- Two instruction policies: baseline and complaint-fidelity guard.
- 384 cells, one generation per cell, shuffled before inference. This is a fixed-context diagnostic, **not** end-to-end retrieval from the original Kannada corpus.

Two initial real smoke-test calls (`v1`) were truncated at 180 generated tokens; they are preserved. The separate main run (`v2`) uses a 512-token cap. Scenario selection, context assignment, prompts, order, model metadata/digest, request hashes, full responses, truncation and failures are logged. No paid API, new model download, or real court-document upload is used.

## Reproduction

Requires Python 3 standard library, an accessible local Ollama server, the installed model, and the sibling `Research-TuluLegalRAG/data/tulu_legal_60_consolidated.jsonl` to prepare new schedules. Existing frozen schedules can run without that source file.

```sh
python3 experiments/controlled_context.py prepare --run-dir experiments/runs/NEW_RUN
python3 experiments/controlled_context.py run --run-dir experiments/runs/NEW_RUN
python3 experiments/analyze_controlled.py experiments/runs/NEW_RUN
```

`run` resumes completed record IDs and refuses a model-digest change. It appends each response immediately and stops on a transport error; errors and invalid outputs remain recorded. Start a new run directory for an intentional rerun. Do not overwrite the source manifest or relabel changed runs as the same frozen experiment.

## What the outputs establish

Primary-category correctness is reproducible against existing authored labels, whose validity remains unreviewed. Exact numeric marker echo (`47` or `2019`) in the structured `complaint_facts` field is only an automatic screen; it can occur in a negation or quotation, and it misses paraphrases. It is **not** an expert source-fact-intrusion label or harm measure. Paired marker comparisons require valid outputs in both conditions and must retain their coverage denominator.

The English gloss may contain ambiguity. Tulu script equivalence and all synthetic contexts remain unreviewed. Relevant/source-detail comparisons also differ in length. Prompt-policy comparisons differ in instruction length. A single 1B model and a small reused sample cannot establish general multilingual effectiveness, fairness, or publication eligibility.

The existing paper is a separate version; do not replace its pending validation claims with an assertion that expert review occurred. New outputs should be reviewed and scoped before integration into the manuscript.

Output-validity and nonempty-fact-array counts are structural checks, not human judgments that a response is substantively useful. Marker denominators use valid structured outputs; these denominators must not be described as a validated assistance-coverage measure.

The relevant synthetic context is built directly from the English scenario gloss. It may therefore act as an oracle semantic scaffold, especially for Tulu queries. This design supports controlled output comparisons but must not be represented as naturally retrieved legal evidence or a realistic estimate of deployed RAG performance.

After completion, `EXPERIMENT_REPORT.md` and `RESULTS.md` contain the canonical analyzed report, `analysis.json` contains counters, comparisons and hashes, and `answers.csv` contains extracted responses. Full original responses remain in `predictions.jsonl`. The analysis-script hash is recorded separately from the pre-inference runner hash.

## Completed run

The v2 run completed all 384 planned calls: 308 valid structured outputs and 76 token-limit truncations. There were no transport failures. All 24 condition cells contain 16 attempts. None of the secondary paired comparisons passes its Holm correction. See `runs/2026-10-30_local1b_v2/EXPERIMENT_REPORT.md` for the full table, per-condition validity, marker denominators, and limitations.

The exact captured model metadata is preserved privately under the repository's ignored `tmp/` directory. The shareable metadata replaces local home-directory names only, retains model digest/template/parameters, and records a hash of the exact capture. Model responses and prompts are unchanged. Run `python3 experiments/package_completed.py` only after completion to verify and package the artifacts.

## Offline robustness audit

Run `python3 experiments/robustness_audit.py` from the repository root. It reads existing responses and source scenarios, produces `analysis/robustness.json` and `analysis/ROBUSTNESS.md`, and makes no inference calls. It adds all-attempt missing-marker bounds, completion counts, category-score leverage and deterministic lexical grouping stress tests; none is expert annotation or demographic validation. The completed-package command now reruns this audit and includes its outputs.
