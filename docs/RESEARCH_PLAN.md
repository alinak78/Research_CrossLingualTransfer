# FAccT 2027 research direction

## Selected niche and claim

**Complaint fidelity under institutional context in minority-language legal intake.**

Working title: *Whose Facts Count? Complaint Fidelity and Language Equity in Cross-Lingual Legal Intake*.

Primary FAccT focus area: **Evaluations and evaluation practices**. Secondary: **System development and deployment**, if the final paper evaluates the proposed safeguards. Do not select Experiences and interactions without a corresponding human study, or Law and policy merely because the application domain is legal.

The novel question is whether official-looking retrieved context causes a system to attribute facts to a complainant that the complainant never supplied, and whether this differs across independently validated script representations. A true source fact can still be false as a description of the current complaint. Evaluate that distinction separately from category accuracy and citation existence.

This direction retains the Tulu/Kannada setting, complaint-classification task, and existing pipeline as pilot infrastructure. It changes the central construct, evaluation design, annotation, and institutional interpretation. Script and RAG accuracy alone were already central to the prior work; do not claim those observations as new.

## Publication boundary

The user confirms that the source paper is accepted or published. A new title, conference format, theoretical framing, or statistical reanalysis alone does not establish compliance with FAccT's prior-publication policy. Determine the venue, archival status, proceedings record, and published main-paper length. Non-archival workshop publications and published short papers of at most four pages are the guide's relevant exceptions. A full archival conference paper cannot simply be resubmitted as a reframed study. Non-archival FAccT registration is not a general exemption.

The current manuscript is an exploratory adaptation draft using prior pilot data. It is not certified eligible or submission-ready. For a genuinely distinct paper, make the complaint-fidelity intervention and independent linguistic/legal validation the main evidence, describe the old experiment as prior work, and disclose overlap accurately. New experiments do not automatically establish sufficient distinctness; assess the complete paper against the policy. Do not invent new results, hide the prior publication, or claim that the offline reanalysis is an independent replication.

## Constructs and evidence

| Construct | Operationalization | Available now | Needed for the distinct study |
|---|---|---|---|
| Primary-category reproduction | Exact match to authored primary label | Complete archived outputs | Independently checked labels and acceptable alternatives |
| Complaint fidelity | No unsupported claim about complaint actors, events, relations, or circumstances | Rationales available, no independent annotation | Double-coded propositions and evidence spans |
| Source-fact intrusion | Output asserts a fact found only in supplied context as part of the complaint | Not systematically measured | Context interventions and source-to-output traceability |
| Appropriate referral | Locally justified destination given the account | Not measured | Legal-aid experts and actual routing rules |
| Correction burden | Effort needed to correct an output or referral | Not measured | Reviewed institutional or participant study |
| Script-associated disparity | Matched difference after semantic equivalence validation | Exploratory script comparisons | Native-language review; no demographic inference |

## Distinct study protocol: not yet executed

1. **Validate the setting.** Work with compensated Tulu-language reviewers and a local legal-aid practitioner to define a concrete intake decision and permissible category alternatives. Document which service would consume the label and what a wrong route changes. Do not assert community endorsement without evidence. Human participation, consent, compensation, and ethics review must be settled before recruitment.
2. **Construct and split cases.** Use the 60 archived scenarios for development only. Build a separately authored held-out set of approximately 200 scenarios, subject to resources and precision planning. Split by underlying situation/template to prevent parallel scripts from crossing development/test boundaries. This is a target, not a completed dataset or a guaranteed adequate sample size. Preserve regional and orthographic variation only where reviewers confirm validity.
3. **Validate representations.** Have two independent fluent reviewers check romanized and Kannada-script forms against scenario intent; record uncertainty and disagreement. English glosses serve as diagnostic references, not unquestioned gold. Tamil/Malayalam forms stay exploratory until independently validated. Do not force users to adopt whichever script scores highest.
4. **Create controlled contexts.** Use rights-cleared, minimized passages or legally reviewed synthetic vignettes, explicitly separating the two. For each held-out scenario provide (a) no context, (b) relevant context without conflicting personal facts, (c) equally relevant context containing a deliberately different actor/event detail, and (d) irrelevant context matched approximately for length. Matched synthetic contexts provide control at the cost of ecological validity; retain an independently checked natural-document subset for a separate replication.
5. **Separate metadata effects.** First test context without source category tags, names, or similarity scores. In a secondary experiment cross metadata presence with identical context text. Any authority cue must be accurately described; do not falsely label a synthetic passage as a real court judgment. Compare a neutral document label with accurate provenance metadata. Keep passage text fixed when estimating the metadata effect.
6. **Hold the intervention stable.** Present the exact same context to both script versions for the primary experiment. Estimate end-to-end retrieval effects separately, since changing the query can change retrieved content. Pin model identifiers, prompts, temperature, token limits, retrieval index, and order. Log failures before any retry and keep repeated generations nested within scenario. Do not rerun all combinations before choosing primary contrasts.
7. **Annotate fidelity.** Two independent reviewers label factual assertions about the complaint as supported by complaint, source-only, unsupported by both, or ambiguous. Attach evidence spans and separate legal propositions from personal facts. Blind condition metadata where feasible; text may still reveal the intervention, so describe partial blinding honestly. Report raw agreement and adjudication. Do not use an LLM judge as sole ground truth.
8. **Measure referral validity separately.** Legal reviewers judge acceptable destinations for the complaint before seeing model output. Revisit ambiguous labels rather than coding every deviation as harm. Consequence weights require local justification; do not invent a universal severity scale.
9. **Evaluate a safeguard.** Compare ordinary classification with a prompt requiring complaint evidence spans for each asserted complaint fact and explicit separation of source facts. A second candidate requests clarification or human review when the evidence is insufficient. No safeguard is currently validated. A change in prompt length is a confound to document. A staffed human route and its coverage must be considered before recommending abstention.
10. **Freeze the analysis before held-out inference.** Select primary model/contrast, sample size justification, exclusions, and multiplicity family in a dated protocol. Existing pilot observations remain exploratory. Add repeated generation only under a plan that treats the scenario, not the output row, as the independent sampling unit.

### Primary estimands

Primary outcome: fraction of scenarios with at least one **source-only personal fact asserted as belonging to the complaint**, comparing conflicting-relevant context against relevant nonconflicting context, with the exact contexts held fixed across scripts. Estimate the matched risk difference and a confidence interval obtained by resampling scenarios, preserving all their paired outputs.

Primary disparity contrast: difference in that context effect between independently validated Kannada and romanized Tulu representations. This is an interaction, not a comparison of two p-values or an inference from one significant and one nonsignificant result. Report it with uncertainty. Treat model comparisons and metadata variants as secondary unless selected in advance.

Secondary outcomes: primary-label accuracy; locally acceptable routing; false factual assertions despite correct label; correct-to-incorrect reversals; invalid outputs; clarification/escalation rate; selective risk at matched coverage for safeguards. If multiple claims are confirmatory, specify a correction family. Report all planned conditions and failed runs.

A held-out sample of 200 has only about +/-7 percentage points of unpaired worst-case binomial precision before considering paired gains, interactions, clustering, or multiplicity. Use actual pilot discordance and a minimally meaningful effect to plan power; an interaction may require substantially more cases. Do not promise definitive fairness conclusions from that target.

## Scope of claims

Supported now: complete archived prediction accounting; matched exploratory script contrasts; model-specific retrieval reversals; a documented absence of an English no-RAG control.

Not supported now: quantified factual intrusion; causal attribution to model internals; real user burden; improved access to justice; population discrimination; effective human fallback; community validation; clinical/legal safety; a distinct eligible submission from the existing publication.

## How the paper changes from the workshop version

| Source emphasis | FAccT emphasis | Additional evidence |
|---|---|---|
| Low-resource comprehension | Institutional recognition of a complainant's account | Validated representations and situated intake task |
| Script advantage | Conditional access and orthographic design choices | Paired validated cases, no population shortcut |
| RAG accuracy change | Source-fact intrusion and referral risk | Controlled context interventions and independent annotation |
| Generated reasoning | Observable explanation fidelity | Evidence spans and adjudicated codebook |
| Global accuracy | Separate accuracy, fidelity, acceptable route, and fallback coverage | Explicit constructs and uncertainty |
| Mitigation returns to baseline | Fidelity-preserving assistance and meaningful escalation | Comparative evidence at matched coverage |

## Paper budget

Aim for 12-14 single-column main pages once new evidence is available: introduction (1), setting and related work (2), constructs and study design (3), results (3), institutional implications (1.5), limitations and conclusion (1.5). References are excluded. Ethics/adverse impacts and required AI disclosure can occupy the dedicated extra endmatter page. Appendices go in the same PDF after references. The rewritten manuscript has 14 main-content pages. It integrates the framework, completed pilot reanalysis, and prospective controlled study while keeping their evidentiary status explicit.

## Verified publication record

The user supplied https://openreview.net/forum?id=2hoq4EUdbP; OpenReview could not be retrieved through the web tool. Independent primary-source verification found the matching publication in the [ACL Anthology](https://aclanthology.org/2026.oracle-main.8/): Shetty, Setty, Kapanova, and Vidra, ORACLE 2026, pages 107-133, Association for Computational Linguistics. This is a formal proceedings publication exceeding four pages. The workshop/non-archival and short-paper exceptions therefore do not cover resubmitting this same work. Develop a genuinely distinct study and assess the overlap; no eligibility approval has been obtained. The local source README's NLLP-submission description is stale relative to this published record.
