# Interpretation rules for the new experiment

This run addresses a narrower question than the full proposed FAccT study: how one available local model responds to a fixed set of authored complaints under controlled synthetic-context and instruction changes.

## Eligible claims after completion

- These are newly generated outputs, with a recorded model digest and full requests/responses.
- Primary-category scores compare each output with the existing author's designated category. Invalid or truncated outputs remain category errors.
- Any quoted numeric source detail in the complaint_facts field is a reproducible literal-marker observation. Its denominator and output-validity selection must be reported.
- Baseline/guard comparisons pair the same scenario, representation and context. Descriptive differences do not establish a general safety improvement.

## Claims this run cannot support

- A new held-out corpus, native-speaker-validated dataset, or completed human expert annotation.
- An expert-confirmed factual-intrusion or hallucination rate. Marker echo can be negated, quoted, or correctly disclaimed; marker absence can miss paraphrase.
- A comparison of the original Llama3, Hex-1, and Sarvam systems. Only llama3.2:1b is used.
- End-to-end retrieval quality from the Kannada court corpus. Supporting contexts here are short, analyst-constructed English illustrative cases.
- Improved referral validity, user outcomes, institutional recourse, population fairness, or resolution of prior-publication eligibility.

## Failures and sensitivity

Do not remove failures from all-attempt accuracy. For marker-policy comparisons, show how many scenarios have valid outputs in both policies, because conditioning on valid pairs can select an easier subset. Absence of valid paired outputs is missing evidence, not zero intrusion. No automatic parser label should be rebranded as a human annotation.

A no-context condition can expose spontaneous marker generation, but does not validate the factual content of otherwise marker-free responses. Conditions adding source details also add tokens; the content-versus-length mechanism is not isolated. Baseline and guard instructions likewise differ in length and emphasis.

The main configuration follows two preserved infrastructure smoke tests that truncated at the earlier token limit. This budget change must be disclosed. The model's current outputs should not be used to tune prompts and then describe the same cases as an untouched test set.

The relevant synthetic context is built directly from the English scenario gloss. It may therefore act as an oracle semantic scaffold, especially for Tulu queries. This design supports controlled output comparisons but must not be represented as naturally retrieved legal evidence or a realistic estimate of deployed RAG performance.
