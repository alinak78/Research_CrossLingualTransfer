# New controlled-context experiment results

Status: completed. 384/384 calls recorded; 308 structurally valid outputs; 76 invalid/error outputs.

Model: `llama3.2:1b`; digest `baf6a787fdffd633537aa2eb51cfd54cb93ff08e28040095462bb63daf552878`. 16 existing development scenarios, two per existing category. New model generations, not a new held-out dataset. No expert annotations.

## Design

Three query representations (English gloss, romanized Tulu, Kannada-script Tulu), four English synthetic-context conditions, and baseline versus fidelity-guard instruction. Context is identical across query representations. `relevant_source_details` adds age 47 and year 2019 to a separate illustrative case. These are absent from selected complaint glosses. The irrelevant condition uses a different category. No real court documents were sent to the model.

One generation per cell, fixed seed and temperature. Order and all 384 inputs were frozen before this run. Two earlier 180-token smoke-test calls truncated; they remain in the v1 directory. The main v2 generation budget is 512. This is exploratory, not an independent replication of the original three models.

## Condition summary

| Query | Context | Policy | Attempts | Valid | Correct primary | Literal marker echo / valid |
|---|---|---|---:|---:|---:|---|
| english | irrelevant_source_details | baseline | 16 | 15 | 3 | 2/15 |
| english | irrelevant_source_details | fidelity_guard | 16 | 10 | 4 | 3/10 |
| english | none | baseline | 16 | 14 | 7 | 0/14 |
| english | none | fidelity_guard | 16 | 15 | 8 | 0/15 |
| english | relevant | baseline | 16 | 15 | 7 | 0/15 |
| english | relevant | fidelity_guard | 16 | 14 | 9 | 0/14 |
| english | relevant_source_details | baseline | 16 | 16 | 8 | 11/16 |
| english | relevant_source_details | fidelity_guard | 16 | 12 | 7 | 5/12 |
| kannada | irrelevant_source_details | baseline | 16 | 7 | 0 | 1/7 |
| kannada | irrelevant_source_details | fidelity_guard | 16 | 11 | 0 | 1/11 |
| kannada | none | baseline | 16 | 10 | 0 | 0/10 |
| kannada | none | fidelity_guard | 16 | 6 | 0 | 0/6 |
| kannada | relevant | baseline | 16 | 12 | 4 | 0/12 |
| kannada | relevant | fidelity_guard | 16 | 6 | 0 | 0/6 |
| kannada | relevant_source_details | baseline | 16 | 9 | 1 | 1/9 |
| kannada | relevant_source_details | fidelity_guard | 16 | 9 | 2 | 2/9 |
| romanized | irrelevant_source_details | baseline | 16 | 15 | 0 | 7/15 |
| romanized | irrelevant_source_details | fidelity_guard | 16 | 16 | 0 | 6/16 |
| romanized | none | baseline | 16 | 16 | 2 | 0/16 |
| romanized | none | fidelity_guard | 16 | 16 | 2 | 0/16 |
| romanized | relevant | baseline | 16 | 16 | 7 | 0/16 |
| romanized | relevant | fidelity_guard | 16 | 16 | 7 | 0/16 |
| romanized | relevant_source_details | baseline | 16 | 16 | 4 | 7/16 |
| romanized | relevant_source_details | fidelity_guard | 16 | 16 | 4 | 3/16 |

Invalid outputs count as category errors. Marker results are not expert-annotated intrusion rates; inspect raw facts and denominators. Rows with no source details are negative-control screens, not exposure contrasts.

## Paired exploratory prompt comparisons

Differences are fidelity guard minus baseline. Accuracy retains all 16 attempts per cell; marker comparisons require both structured outputs to be valid. Holm correction is separate for the 12 accuracy and six marker comparisons when complete. Negative marker differences mean fewer literal echoes, not proven safer assistance.

| Query | Context | Metric | Paired n | Baseline only | Guard only | Delta pp | Exact p | Holm p |
|---|---|---|---:|---:|---:|---:|---:|---:|
| english | none | primary_correct | 16 | 0 | 1 | +6.2 | 1.00000 | 1.00000 |
| english | relevant | primary_correct | 16 | 0 | 2 | +12.5 | 0.50000 | 1.00000 |
| english | relevant_source_details | primary_correct | 16 | 2 | 1 | -6.2 | 1.00000 | 1.00000 |
| english | relevant_source_details | literal_marker_echo | 12 | 4 | 1 | -25.0 | 0.37500 | 1.00000 |
| english | irrelevant_source_details | primary_correct | 16 | 0 | 1 | +6.2 | 1.00000 | 1.00000 |
| english | irrelevant_source_details | literal_marker_echo | 9 | 1 | 3 | +22.2 | 0.62500 | 1.00000 |
| romanized | none | primary_correct | 16 | 0 | 0 | +0.0 | 1.00000 | 1.00000 |
| romanized | relevant | primary_correct | 16 | 0 | 0 | +0.0 | 1.00000 | 1.00000 |
| romanized | relevant_source_details | primary_correct | 16 | 1 | 1 | +0.0 | 1.00000 | 1.00000 |
| romanized | relevant_source_details | literal_marker_echo | 16 | 5 | 1 | -25.0 | 0.21875 | 1.00000 |
| romanized | irrelevant_source_details | primary_correct | 16 | 0 | 0 | +0.0 | 1.00000 | 1.00000 |
| romanized | irrelevant_source_details | literal_marker_echo | 15 | 3 | 2 | -6.7 | 1.00000 | 1.00000 |
| kannada | none | primary_correct | 16 | 0 | 0 | +0.0 | 1.00000 | 1.00000 |
| kannada | relevant | primary_correct | 16 | 4 | 0 | -25.0 | 0.12500 | 1.00000 |
| kannada | relevant_source_details | primary_correct | 16 | 0 | 1 | +6.2 | 1.00000 | 1.00000 |
| kannada | relevant_source_details | literal_marker_echo | 7 | 0 | 1 | +14.3 | 1.00000 | 1.00000 |
| kannada | irrelevant_source_details | primary_correct | 16 | 0 | 0 | +0.0 | 1.00000 | 1.00000 |
| kannada | irrelevant_source_details | literal_marker_echo | 7 | 1 | 0 | -14.3 | 1.00000 | 1.00000 |

## Interpretation boundaries

- Existing development scenarios, not held-out or new human-authored data.
- English contexts held fixed across representations; not original Kannada-corpus RAG.
- Source-detail addition changes context length; content and length are not isolated.
- Baseline and guard prompts differ in length and instructions.
- Marker echo is an automatic screening signal, not expert intrusion annotation.
- One local 1B model, one generation per cell, no population or agent-workflow claims.
- No expert annotations or linguistic/legal validation performed.
- Marker comparisons condition on valid paired outputs and can be selection-biased.
- Exact literal screening misses spelled-out equivalents, paraphrase and untranslated numeric representations.
- Markers in complaint_facts can be negated or quoted; the signal does not establish attribution or hallucination.
- Post-generation analysis; no confirmatory preregistration or validated causal fidelity measurement.
- Exact paired tests assume independent scenario units; shared authoring templates can violate this assumption, and the 16 cases are not population-representative.
- All-attempt accuracy requires both complete valid structure and label agreement; it conflates output completion with classification and cannot diagnose comprehension alone.
- Relevant synthetic context repeats the scenario English gloss and can act as an oracle semantic scaffold; it is not naturally retrieved evidence.

The manuscript incorporates these outputs as an exploratory development diagnostic, not validated fidelity evidence. Human fidelity labels and referral outcomes remain absent.
