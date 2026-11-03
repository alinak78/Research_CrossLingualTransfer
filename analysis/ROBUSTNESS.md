# Post-hoc robustness and provenance audit

No new model calls, expert annotations, demographic observations, or court excerpts. These checks narrow claims; they do not validate complaint fidelity.

## Missing-output bounds

All 16 attempts per policy remain in the estimand. Each invalid output can have either marker outcome. Bounds describe an unknown full-output literal-marker outcome, not intrusion or an estimate of what a longer generation would produce. They are identification bounds, not confidence intervals.

| Query | Context | Baseline echo / valid | Guard echo / valid | Guard minus baseline bound (pp) |
|---|---|---|---|---|
| english | relevant_source_details | 11/16 | 5/12 | [-37.50, -12.50] |
| english | irrelevant_source_details | 2/15 | 3/10 | [+0.00, +43.75] |
| romanized | relevant_source_details | 7/16 | 3/16 | [-25.00, -25.00] |
| romanized | irrelevant_source_details | 7/15 | 6/16 | [-12.50, -6.25] |
| kannada | relevant_source_details | 1/9 | 2/9 | [-37.50, +50.00] |
| kannada | irrelevant_source_details | 1/7 | 1/11 | [-56.25, +31.25] |

A bound excluding zero concerns this finite sample and literal marker only, without sampling uncertainty. It does not override nonsignificant paired tests or establish a safeguard effect.

## Completion by representation and policy

| Query | Policy | Invalid / attempts |
|---|---|---|
| english | baseline | 4/64 |
| english | fidelity_guard | 13/64 |
| romanized | baseline | 1/64 |
| romanized | fidelity_guard | 0/64 |
| kannada | baseline | 26/64 |
| kannada | fidelity_guard | 32/64 |

## Category leverage

All-attempt scoring retains invalids as errors. Omission is a descriptive sensitivity analysis, not a new statistical test. Category groups are stress-test strata, not verified authoring templates.

| Query | Context | Guard minus baseline (pp) | Leave one scenario range | Leave one category range |
|---|---|---|---|---|
| english | none | +6.25 | [0.0, 6.666666666666667] | [0.0, 7.142857142857143] |
| english | relevant | +12.50 | [6.666666666666667, 13.333333333333334] | [7.142857142857143, 14.285714285714286] |
| english | relevant_source_details | -6.25 | [-13.333333333333334, 0.0] | [-14.285714285714286, 0.0] |
| english | irrelevant_source_details | +6.25 | [0.0, 6.666666666666667] | [0.0, 7.142857142857143] |
| romanized | none | +0.00 | [0.0, 0.0] | [0.0, 0.0] |
| romanized | relevant | +0.00 | [0.0, 0.0] | [0.0, 0.0] |
| romanized | relevant_source_details | +0.00 | [-6.666666666666667, 6.666666666666667] | [-7.142857142857143, 7.142857142857143] |
| romanized | irrelevant_source_details | +0.00 | [0.0, 0.0] | [0.0, 0.0] |
| kannada | none | +0.00 | [0.0, 0.0] | [0.0, 0.0] |
| kannada | relevant | -25.00 | [-26.666666666666668, -20.0] | [-28.571428571428573, -14.285714285714286] |
| kannada | relevant_source_details | +6.25 | [0.0, 6.666666666666667] | [0.0, 7.142857142857143] |
| kannada | irrelevant_source_details | +0.00 | [0.0, 0.0] | [0.0, 0.0] |

## Archive lexical dependence stress test

English glosses are lowercased and tokenized to letter-only sets. Undirected edges join Jaccard scores at or above the threshold; connected components are deterministic stress-test groups. Transitivity can merge dissimilar endpoints. These are not validated semantic or authoring-template clusters. No independence claim, cluster p-value, or population interval is attached. The archived Llama3 D_full minus E_full difference is -36.67 pp.

| Threshold | Components | Largest | Equal-component-weight delta (pp) | Leave one component range |
|---|---|---|---|---|
| 0.3 | 54 | 3 | -37.04 | [-38.983050847457626, -34.48275862068966] |
| 0.4 | 59 | 2 | -37.29 | [-38.983050847457626, -35.59322033898305] |
| 0.5 | 60 | 1 | -36.67 | [-38.983050847457626, -35.59322033898305] |
| 0.7 | 60 | 1 | -36.67 | [-38.983050847457626, -35.59322033898305] |
| 1.0 | 60 | 1 | -36.67 | [-38.983050847457626, -35.59322033898305] |

## Corpus and representation boundaries

{
  "source_file": "kannada_legal_corpus_list.jsonl",
  "sha256": "cc182c88cc5725df2bb17805cf39e053eee90b4aa0c02ddb2b46fa3e20e6b3ad",
  "record_count": 18,
  "extraction_verification": "not independently verified; source reports model-assisted correction",
  "personal_information": "known risk; not copied into this audit",
  "redistribution_rights": "unresolved; corpus excluded from public package",
  "new_local_experiment_uses_corpus": false,
  "release_gate": "Do not distribute court text until rights, redaction, and extraction checks are completed."
}

No speaker demographics, dialect balance, linguistic equivalence, category validity, or legal routes are inferred. Review status remains unverified. The original 60 cases and the selected 16 are authored development materials, not samples of 60 or 16 participants. Pinned local metadata improves auditability of the new run but does not reconstruct historical services.
