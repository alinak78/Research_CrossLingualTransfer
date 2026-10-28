# Complaint-fidelity annotation codebook (prospective)

No new expert labels have been collected. This is a protocol for a distinct study.

Unit: a factual proposition in the model's explanation that describes the current complaint. Segment compound statements into separate propositions when their support differs. Treat a statement about a court case as a source statement unless the output explicitly or implicitly transfers it to the present complaint. Distinguish quotation, hypothesis, uncertainty, and assertion.

| Code | Meaning | Required evidence |
|---|---|---|
| COMPLAINT_SUPPORTED | Current-complaint assertion follows from the complaint | Complaint span, with reviewer rationale for any paraphrase |
| SOURCE_ONLY_INTRUSION | Current-complaint assertion comes from context but has no support in the complaint | Context span plus absence-of-support explanation; do not label a correctly attributed source summary as intrusion |
| UNSUPPORTED_BOTH | Assertion about the complaint is unsupported by complaint and context | Reviewed complaint/context with explanation |
| AMBIGUOUS | Support cannot be decided, including disputed translation | Disputed span and reviewer explanation |
| NOT_COMPLAINT_FACT | Legal proposition, advice, label, or source-only summary correctly attributed | Record separately; requires different legal evaluation |

The primary case outcome is any SOURCE_ONLY_INTRUSION in asserted personal facts. Report unsupported-both separately. Do not infer a mental mechanism from these labels. Do not infer that every unsupported statement is false in the world; the question is whether the provided evidence supports attributing it to this complaint.

Reviewers independently code before discussion. Retain both original labels, evidence spans, and adjudication. Record reviewer language competency and relevant legal expertise without publishing identifying information in the review artifact. Report raw agreement and category-specific disagreements; rare events can make aggregate agreement misleading. Where a legal claim is assessed, record jurisdiction, date, authority, and specialist judgment separately.

For a source-only detail intervention, the primary contrast is within scenario and script. The script interaction must compare the two context effects directly. Hold retrieved text fixed for the representation experiment and distinguish it from a separate end-to-end retrieval experiment.
