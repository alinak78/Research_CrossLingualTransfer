# Whose Facts Count? Complaint Fidelity and Language Equity in Cross-Lingual Legal Intake

**Working manuscript. Existing model results are reused from the published ORACLE 2026 pilot. The proposed direct complaint-fidelity study is not yet executed; publication eligibility is unresolved for any future distinct submission.**

## Abstract

This paper develops a normative and methodological framework for evaluating cross-lingual legal intake. Its premise is that a system should justify assertions attributed to the person seeking help and an institution should be able to repair unsupported ones. We distinguish category reproduction, complaint fidelity, and locally appropriate referral, and specify a candidate protocol using controlled contexts, proposition-level annotation, explicit denominators, and correction responsibilities. A published Tulu/Kannada pilot provides a diagnostic illustration, not new benchmark data or validation of the protocol. A matched reanalysis covers 60 authored scenarios, three models, 19 conditions, and 3,420 archived predictions. For Llama3 under full Kannada-script priming, retrieval changes accuracy from 36/60 to 14/60, with 26 correct-to-incorrect reversals and four recoveries; the exploratory contrast remains detectable after correction across 18 paired tests. These category changes identify a need for different evidence but establish neither factual intrusion nor realized referral harm. We connect the evidence boundary to retrieval and tool-mediated administrative architectures without claiming cross-domain empirical generalization. Worked examples, a reporting specification, and a capacity-based precondition for consequential automation make the proposal inspectable. The direct fidelity study remains unexecuted: reliability, feasibility, and effectiveness require independent linguistic and institutional validation.

## Introduction

A person describes a problem in their own words. An intake system decides which category fits, what information to display, or which service to suggest. This transition from account to category is a consequential point of interpretation. The person may describe unpaid wages, money withheld by a landlord, or a disagreement over land without using the vocabulary of a legal institution. A system that recognizes the words but changes the relationship between the actors can produce a plausible explanation of the wrong problem. The concern is especially relevant when the complaint and the legal material used to interpret it are written in different languages.

This paper examines that problem through Tulu complaint classification with Kannada legal context. A related language and shared script can offer useful computational resources, but they also structure which representations a system handles well. Retrieval adds another intermediary: a document about someone else's dispute. Its legal relevance does not make its personal facts evidence about the current complainant. For intake, a system must preserve a boundary between interpreting the account and replacing it with a better documented account drawn from an institution's records.

We call the preservation of that boundary complaint fidelity. The term concerns whether the output's assertions about the current complaint are supported by what the person supplied, including uncertainty and ambiguity. It does not mean accepting every claim as legally established, deciding a dispute in the speaker's favor, or treating a model-generated explanation as a transcript of internal reasoning. It asks a prior question: does the system still describe the problem that was presented to it?

Our position is that category accuracy alone is insufficient for evaluating equitable legal intake. A label can match a reference category even when the explanation invents facts. A label can differ from a benchmark and still be an acceptable route in a particular service. An abstaining system can avoid an unsupported assertion while leaving the person without help. These outcomes involve different mechanisms and responsibilities. Combining them into a single accuracy score obscures both the limits of the evidence and the decisions required of a receiving institution.

We develop this argument using the published pilot of Shetty and colleagues [prior]. That study investigated script, linguistic priming, and retrieval across three models on authored Tulu legal scenarios. We do not present those scenarios or model runs as new data. We reanalyze the archived predictions with matched comparisons, explicit accounting of invalid outputs, and correction for the selected family of tests. The reanalysis provides a concrete demonstration of classification instability; it cannot independently validate the complaint-fidelity construct or reproduce an observed legal-aid workflow.

The paper addresses three questions. RQ1: How do the archived classifications vary across script representations and after the addition of legal retrieval? RQ2: Which conclusions about the complainant's account and potential referral consequences are supported by these differences, and which require different evidence? RQ3: How should a direct audit of complaint fidelity separate contextual relevance, source-fact intrusion, script representation, and institutional routing?

The contribution has three parts: an evidentiary boundary between complaint facts and source facts; a candidate protocol specifying annotation, controlled comparisons, and claim-specific evidence; and institutional responsibilities for correcting unsupported attributions. Appendix B supplies worked examples and a reporting specification that make these distinctions inspectable. The completed reanalysis of 3,420 archived predictions and 18 paired comparisons is a diagnostic illustration of classification instability, not evidence validating fidelity. A clearer framing does not by itself establish novelty or satisfy prior-publication policy. No new participant study, linguistic validation, or model experiment is claimed.

The case illustrates an architectural boundary relevant beyond legal intake: external documents enter a model's working context, become candidate facts in an account, and may feed a downstream recommendation or action. An agent could carry an unsupported attribution into a form, summary, or routing call. The Tulu/Kannada pilot exposes classification sensitivity at one point in that chain; it does not measure those agent actions or prove a broader minority-language effect. Generalization concerns the evaluative question, not an estimated harm rate.

The application is intake support, not legal advice or rights adjudication. Error consequences depend on the receiving institution. We analyze conditional pathways to burden and exclusion without treating computational errors as documented adverse outcomes.

## Setting: language, categories, and institutional recognition

### A multilingual intake problem

The pilot pairs Tulu descriptions of everyday legal problems with Kannada legal documents. This pairing provides a concrete case in which the language of a person's account differs from the language of a supporting information resource. We use this relationship to investigate the design of an intermediary, rather than to make claims about the language abilities of all Tulu speakers or the language practices of all courts and legal services. The available material does not establish speakers' preferred scripts, proficiency in other languages, or experience seeking assistance.

An intake route also cannot be inferred directly from a language label. Different speakers may use different orthographic conventions or switch languages for different tasks. A system that performs better on one written representation has not thereby established that people should be required to adopt it. Requiring conversion could place additional work on the person seeking help and could erase distinctions that matter to their account. Whether these costs arise in practice requires evidence from the relevant users and service, which this pilot does not provide.

For analytical purposes, we model intake as four linked activities: eliciting the account, interpreting it, assigning one or more categories, and selecting a next step. The archived task directly evaluates only category assignment against authored labels. It contains neither a conversational elicitation process nor a real service directory. This boundary matters because a classifier can be consistently wrong against a benchmark, inconsistently wrong across representations, or differently categorized but serviceable for referral. Those are distinguishable findings.

### Category systems as institutional choices

The source labels are adapted from the Stanford Legal Design Lab's Legal Issues Taxonomy, LIST. The originating project describes a taxonomy of legal problems in the United States [list]. The pilot's use of these categories does not establish their suitability for Indian legal-aid intake. We therefore describe the outcome as LIST-inspired primary-category reproduction. We do not describe the authored primary label as the uniquely correct legal interpretation of a complaint.

Consider a complaint that a landlord has not returned money. Housing and a money-related category can both describe part of the account. Whether either is an appropriate destination depends on a service's responsibilities and referral rules. This example illustrates a construct problem rather than resolving the legal classification of a real case. A specialist review would need to determine which distinctions affect assistance, which alternatives are acceptable, and which categories conceal a meaningful difference in circumstances.

The taxonomy therefore belongs inside the audit. It should not operate as an unquestioned standard against which a minority-language account is judged deficient. Label review must distinguish unclear wording, disagreement among qualified reviewers, and a category set that does not match the receiving institution. A model should not receive credit for reproducing an invalid category boundary merely because the benchmark encodes it consistently.

### Stakeholders and responsibilities

The relevant roles include the speaker, language reviewers, legal-aid staff, developers, and the receiving institution. Linguistic equivalence, legal routing, and technical diagnosis require distinct expertise. Developers cannot substitute model inspection for the institution's decisions about assistance and correction.

These responsibilities are proposed; no service partnership or completed consultation is asserted. Participants should be able to challenge the task, categories, and interface or decline automation. Supplying labels alone does not confer authority over these decisions.

## Related work and the gap addressed

### Fairness beyond a predictive label

Selbst and colleagues examine the loss of social context when fairness problems are abstracted into technical systems [selbst]. Our framework applies that concern to a specific point of abstraction: transforming a complaint into a legal category. The relevant questions include what counts as a faithful interpretation, how a category becomes a route, and who can correct the transformation. We consequently avoid equating a script-associated accuracy difference with a complete measure of justice. The case motivates an audit of the surrounding decision process as well as the model output.

### Language inclusion and data documentation

Joshi and colleagues document uneven language representation in NLP resources and research [joshi]. This motivates scrutiny of which languages and scripts benefit from a computational intervention. It does not determine a particular model's exposure to Tulu or justify inferring individual users' capabilities from language-resource categories. Bender and Friedman propose data statements to clarify the populations and conditions represented in language datasets [bender]. We apply that documentation principle to authored scenarios, script production, reviewer expertise, and the boundaries of generalization. Parallel script versions are representations of the same cases, not evidence from separate speaker populations.

### Authority over language resources

Bird critiques approaches that treat language and community knowledge as resources available for extraction and emphasizes different relationships with knowledge holders [bird]. The implication for this study is procedural: a plan to collect additional Tulu examples should include authority over use, interpretation, and release, rather than treating speaker review as a final quality check. We do not assume that the history or status of every language community is interchangeable. The practical question is which decisions the people affected by this particular intake system can influence.

### Retrieval and legal reliability

Magesh and colleagues evaluate reliability failures in commercial legal research tools that use retrieval [magesh]. That work supports examining outputs rather than relying on an assurance that retrieved sources prevent error. Its task differs from ours: finding or synthesizing legal information is not the same as interpreting a new complaint. Our concern is the transfer of factual content across that boundary. Even if a retrieved case and every citation are genuine, a model can misattribute its facts to the current speaker. Citation existence and complaint fidelity therefore require separate measurements. Zhan and colleagues study malicious external instructions in tool-integrated agents [injecagent]. Our concern differs: ordinary source facts can be misattributed without an attack. The architectural connection is the need to track what external content is authorized to determine, not an assertion that the pilot measures prompt injection.

### Relationship to the published Tulu study

Shetty and colleagues already reported script-dependent classification, mixed retrieval effects, and examples characterized as fact substitution or confabulation in this setting [prior]. This paper retains those observations as prior evidence. It changes the object of evaluation from general cross-lingual comprehension to a set of observable relationships between complaint, context, output, and potential route. The additional paired accounting improves the description of the archived experiment; it is not an independent replication or a demonstration that the proposed fidelity audit has succeeded.

The earlier study asks when script, priming, and retrieval support category prediction and describes examples of fact substitution [prior]. The present framework asks which input authorizes each assertion about the complainant, even when the category is correct. Its proposed unit is the attributed proposition; its direct outcome is source-fact intrusion; its institutional question is who repairs an unsupported account and its downstream route. These differences specify the claimed intellectual contribution without treating a renamed failure mode or a corrected p-value as sufficient novelty. Whether that contribution clears prior-publication requirements remains a separate eligibility question.

## A complaint-fidelity framework

### Three outcomes that should remain separate

Category reproduction measures whether the predicted primary label equals the dataset's designated primary label. It is inexpensive to compute from the archive and permits a matched audit. Its meaning depends on the validity of the labels. In particular, a low score does not establish that a system denied a useful service, and a high score does not establish that the underlying account was preserved.

Complaint fidelity measures whether assertions about the current complainant's actors, events, relationships, and circumstances are supported by the complaint. Support includes justified paraphrase but not an invented detail made plausible by a retrieved case. It must also account for modality: an assertion that an event occurred is different from a question about whether it occurred. An explanation that clearly describes a source case as a source case should not be coded as intrusion merely because it contains facts absent from the complaint.

Referral validity measures whether a suggested next step is appropriate under a locally specified service arrangement. It requires legal and institutional judgment, potentially including multiple acceptable routes. The archived labels are not a substitute for those judgments. A referral can be valid despite a primary-label mismatch; a matching label can still lead to an unsuitable route if the service mapping is incorrect or outdated.

**Evaluation layers and the evidence needed to assess them.**

| Layer | Audit question | Evidence in this paper |
| --- | --- | --- |
| Category reproduction | Does the output match the designated primary label? | Completed on archived predictions; labels not independently validated. |
| Complaint fidelity | Are assertions about this complaint supported by the account? | Operational definition and prospective annotation; no expert-labeled fidelity results. |
| Referral validity | Is the next step appropriate for a specified service? | Institutional validation proposed; no observed referral outcomes. |

### An evidence boundary for personal facts

Let a complaint, a retrieved context, and a model output be considered together. For each asserted proposition about the current complaint, an annotator asks whether the complaint supports it and whether the retrieved context supports it. Complaint-supported propositions preserve the relevant boundary. A proposition supported only by context becomes source-fact intrusion when the output attributes it to the present complaint. A proposition supported by neither is unsupported fabrication for this audit. Ambiguous cases remain explicit rather than being forced into either error type.

For illustration, imagine an authored complaint stating only that an employer withheld wages. A retrieved vignette concerns an unrelated employee dismissed after an absence. If the output states that the current complainant was dismissed for absence, it has imported a source fact. If it instead says that the retrieved vignette involves dismissal while the current complaint concerns unpaid wages, it has preserved attribution. This example is a methodological illustration created for the framework, not an observed model output or a legal determination.

The framework does not require a claim about internal knowledge conflict. The observable failure is an unsupported attribution, whatever combination of parsing, instruction following, retrieval, or generation produced it. This avoids treating a fluent generated rationale as reliable evidence of the model's reasoning process. A causal claim about why attribution changes requires controlled interventions and cannot be established from one explanation.

### Language equity as a conditional evaluation target

We investigate whether representation choices systematically change the quality of the same account's treatment. A matched comparison is useful because it holds the authored situation constant. However, it depends on semantic equivalence between versions. A difference caused by faulty transliteration is a representation-pipeline problem, while a difference between independently validated representations is stronger evidence of model sensitivity. Both matter to a service, but they support different technical conclusions.

Equal error rates across scripts would not be sufficient for equitable intake: every version could perform poorly, and users could face unequal burdens in producing a version the system accepts. Conversely, unequal benchmark scores do not automatically establish unequal service outcomes. An evaluation should report absolute quality, differences across representations, unsupported factual assertions, and the availability of a meaningful correction route. These outcomes inform a normative assessment; they do not replace it with a single fairness score.

### A conditional pathway from error to harm

A plausible pathway begins with a change in representation or context, continues through an altered interpretation or category, and reaches an adverse consequence only if an institution acts on it in a consequential way. Inappropriate information, additional translation work, repeated explanation, or delay are possible consequences. They are hypotheses about a workflow in this study. We have neither measured them nor established which services would generate them.

Each link requires evidence: a category change may preserve the account, two labels may lead to the same service, or a distortion may be corrected before routing. Conversely, a small classification difference may matter under a rigid referral rule. Audits should identify where their evidence stops.

## Data and completed audit methods

### Published pilot material

The source dataset comprises 60 authored scenarios, each with an English gloss, romanized Tulu, and Kannada-, Tamil-, and Malayalam-script versions. Each scenario has a primary reference category and may have secondary categories. The scenario is the unit of analysis. Repeated representations and conditions do not turn these 60 scenarios into a larger independent sample of legal problems or speakers.

The source documentation describes automated Tamil and Malayalam transliteration without independent native-speaker verification. The main script comparisons here use Kannada and romanized forms, whose equivalence also requires independent review. We do not use the English gloss as unquestioned ground truth or infer that an English result represents what a Tulu speaker would achieve after translating a real complaint.

The retrieval resource contains 18 Kannada court documents. The original workflow reports model-assisted correction of extracted text. Correction against a source document can reduce some extraction errors, but it does not by itself establish a faithful legal transcription. The archived pipeline includes retrieved source metadata and category labels in context. Adding retrieval therefore changes both passage content and cues about its source; the archive does not isolate their effects.

Predictions come from Llama3, Hex-1, and Sarvam under 19 conditions spanning script, sparse or full linguistic priming, and retrieval. Full priming contains vocabulary that overlaps the scenarios. Gains in that condition cannot be interpreted solely as general grammar acquisition. The models also differ in configuration and service constraints. We treat each as a separate observed system rather than attributing differences causally to a training-language characteristic.

### Record integrity and scoring

We ingest all main-experiment CSVs and join records using model, condition, and scenario identifier. This produces 3,420 unique records, with 60 scenarios in each of 57 model-condition groups. Every stored primary reference label matches the consolidated JSONL dataset, and recomputing exact primary-label correctness matches the saved Hits@1 score for every row. Thirty-three primary outputs contain explicit error or parse-failure markers. They count as incorrect rather than disappearing from the denominator.

The analysis checks duplicate keys, scenario completeness, and agreement with reference labels and stored correctness. Input hashes are retained in a machine-readable manifest. These checks establish internal consistency of the supplied archive, not independent verification of the authoring process or legal validity of the labels. We do not rerun models, upload source documents, or reconstruct undocumented historical service settings.

### Matched contrasts

We select six comparisons per model. Three compare Kannada-script and romanized Tulu without retrieval, at unprimed, sparse-primed, and full-primed settings. Three compare retrieval against no retrieval for Kannada-script Tulu, holding the priming tier fixed. Table 2 defines the conditions used for these comparisons. The English condition is retained descriptively because the corresponding English no-retrieval condition is absent.

**Conditions used in the selected paired comparisons.**

| Code | Query representation | Priming | Retrieval |
| --- | --- | --- | --- |
| G / H | Romanized / Kannada-script Tulu | None | No |
| M_sparse / E_sparse | Romanized / Kannada-script Tulu | Sparse | No |
| M_full / E_full | Romanized / Kannada-script Tulu | Full | No |
| F | Kannada-script Tulu | None | Yes |
| D_sparse / D_full | Kannada-script Tulu | Sparse / full | Yes |
| A | English gloss | None | Yes |

For two conditions evaluated on the same scenarios, an accuracy difference can hide changes in opposite directions. We therefore count cases correct only in the first condition, cases correct only in the second, and all primary-label changes. In the retrieval comparisons, correct-to-incorrect reversals are cases correct without retrieval and incorrect with retrieval; recoveries are the reverse. Label changes additionally include transitions between two incorrect categories and should not be reported as newly introduced errors.

### Statistical scope

We use two-sided exact McNemar tests, equivalently exact binomial tests on the discordant correctness pairs, and Holm correction over the 18 selected comparisons. The contrasts were selected after inspecting the prior paper and are exploratory. Multiplicity correction within this family does not remove the effects of all prior analytic choices or make the analysis preregistered. Complete comparisons appear in the appendix and machine-readable artifact.

Descriptive Wilson intervals for individual condition accuracies are available in the artifact. They do not make a purposively authored dataset population-representative. Interpretation also assumes independent scenario units; shared templates or repeated situations can weaken that assumption. A future dataset should define and preserve template groups when estimating uncertainty. The archived outputs offer no repeated-generation estimate, so we cannot characterize stochastic variability or current API behavior from these records.

We do not treat the pilot's top-three overlap measure as interchangeable with primary-category correctness. Secondary labels can reveal ambiguity, but they do not establish a validated set of acceptable referrals. Similarly, a confidence value supplied by a model is not assumed calibrated, and a generated explanation is not assumed faithful to its internal computation. The completed analysis concerns recorded classifications under recorded conditions.

## Results: classification changes in the archived pilot

### Coverage and descriptive performance

All selected comparisons use the same 60 authored scenarios per model. Table 3 shows selected condition counts, retaining invalid outputs as errors. The complete 19-condition summary is preserved in the artifact. These are recomputed results from the published pilot, not newly collected experimental findings [prior].

**Correct primary labels out of 60 scenarios; all invalid outputs count as errors.**

| Model | H | G | E sparse | E full | F | D sparse | D full |
| --- | --- | --- | --- | --- | --- | --- | --- |
| llama3 | 28/60 | 10/60 | 31/60 | 36/60 | 15/60 | 16/60 | 14/60 |
| hex1 | 25/60 | 10/60 | 27/60 | 36/60 | 23/60 | 25/60 | 28/60 |
| sarvam | 29/60 | 20/60 | 28/60 | 40/60 | 32/60 | 33/60 | 36/60 |

These counts characterize particular configurations on authored cases, not a ceiling on Tulu comprehension. Glossary overlap and unvalidated language and category judgments constrain interpretation.

Effects remain disaggregated because model configurations differ and their descriptive directions vary. Pooling them would obscure this heterogeneity; the results do not rank model families by suitability for a community.

### Script representation

For unprimed inputs without retrieval, Llama3 classifies 28/60 Kannada-script scenarios correctly and 10/60 romanized scenarios correctly, a 30.0 percentage-point difference. The paired counts are 23 correct only in Kannada script and five correct only in romanized form, giving a Holm-adjusted p-value of 0.01283. Its primary labels differ between the scripts for 47 scenarios. The latter is a consistency measure, not the number of additional correct decisions.

Hex-1 has an unprimed difference of 25.0 points, with 21 Kannada-only correct cases and six romanized-only correct cases; its adjusted p-value is 0.05925. Sarvam has a difference of 15.0 points, with 16 Kannada-only correct cases and seven romanized-only correct cases; its adjusted p-value is 0.55884. The directions are descriptive evidence of representation sensitivity, but the corrected tests do not support claiming the same detectable effect for every model.

Under full priming, the Kannada-versus-romanized differences are 28.3 points for Llama3, 35.0 for Hex-1, and 26.7 for Sarvam. All three selected full-priming comparisons have adjusted p-values below 0.05. These comparisons still bundle a query representation with a script-matched priming block. They do not isolate a tokenizer effect, establish natural preference for one script, or show that mandatory script conversion would improve access for actual users.

### Retrieval reversals and recoveries

For Llama3 under full Kannada-script priming, adding retrieval changes accuracy from 36/60 to 14/60, a decline of 36.7 points. Twenty-six correct classifications become incorrect and four incorrect classifications become correct. The exact paired p-value is approximately 0.0000595 and the Holm-adjusted p-value is 0.00101. Primary labels change for 43 scenarios, including changes between two wrong categories.

The directional count matters for evaluation: retrieval can recover some errors while introducing more. Reporting only disagreement or a mean score conceals this exchange. Table 4 makes the distinction explicit for the full-priming comparison. The net score change is a summary of these transitions; it is not a measured rate of factual intrusion or a referral-harm estimate.

**Full-priming Kannada-script retrieval contrasts. Reversals become incorrect; recoveries become correct.**

| Model | Reversals | Recoveries | Label changes | Delta pp | Holm p |
| --- | --- | --- | --- | --- | --- |
| llama3 | 26 | 4 | 43 | -36.7 | 0.00101 |
| hex1 | 10 | 2 | 22 | -13.3 | 0.30859 |
| sarvam | 7 | 3 | 19 | -6.7 | 1.00000 |

Under sparse priming, Llama3 declines from 31/60 without retrieval to 16/60 with retrieval, with 20 correct-to-incorrect reversals and five recoveries. Its adjusted p-value is 0.04485. Without priming, its score declines from 28/60 to 15/60, with 18 reversals and five recoveries, but the adjusted p-value is 0.09560. Thus some large descriptive declines do not remain below 0.05 after correction across the selected family.

Hex-1 under full priming declines from 36/60 to 28/60, with ten reversals and two recoveries; its adjusted p-value is 0.30859. Sarvam declines from 40/60 to 36/60, with seven reversals and three recoveries; its adjusted p-value is 1.00000. Sarvam instead shows a descriptive increase under sparse priming, from 28/60 to 33/60. Failure to detect an effect is not an equivalence finding, and the small sample does not support declaring these configurations safe.

### English and claims the archive cannot identify

With an English gloss and retrieval, correct counts are 37/60 for Llama3, 52/60 for Hex-1, and 55/60 for Sarvam. These are descriptive reference values. Because English without retrieval was not run in the archive, there is no within-English retrieval contrast. Differences between this condition and Tulu conditions cannot establish that retrieval is more beneficial in English or estimate a language-by-retrieval interaction.

The archive also lacks independent proposition labels for complaint fidelity, a validated referral destination, and user outcomes. Consequently, the results cannot establish what fraction of reversals arose from imported source facts, whether the explanations preserved the account, or whether any person was misdirected. They identify settings in which direct fidelity evaluation is warranted and delimit the inferences that classification data alone can support.

## A reusable protocol for complaint-fidelity evaluation

### Methodological contribution and evidentiary status

This protocol specifies the minimum evidence needed to make a complaint-fidelity claim. Its normative premise is that institutions should justify assertions attributed to an applicant and provide a way to repair unsupported ones. The protocol translates that premise into auditable units, controls, outcomes, and reporting requirements. It is a candidate method for cross-lingual administrative tools that interpret personal accounts using external documents, not a community-endorsed standard or an empirically validated instrument. Applying it beyond legal intake requires validating the relevant categories, languages, and institutional consequences anew.

The controlled experiments and annotations below have not been executed. The completed contribution is the specification and its logical separation of claims; effectiveness, annotator reliability, and feasibility remain empirical questions. The archived 60 scenarios should serve as development material, not as held-out validation for a protocol designed after inspecting their outputs.

The primary question is whether conflicting but relevant context increases the fraction of outputs that attribute source-only personal facts to the current complaint. A second question is whether that context effect differs between independently validated Kannada-script and romanized Tulu. The latter requires estimating an interaction directly. One significant within-script effect and one nonsignificant effect would not establish that the effects differ.

### Independent linguistic and legal validation

Before new model inference, independent fluent reviewers should assess each representation against the intended scenario. They should record alternative interpretations, orthographic variation, and uncertainty rather than silently normalizing every account toward one form. Separate legal-aid reviewers should assess the category set and acceptable routes under an explicitly described service arrangement. A representation can be linguistically equivalent while both versions inherit an invalid reference category.

Reviewers should receive compensation and clear terms about data use and release. The study must establish appropriate ethics review and consent procedures before collecting participant input. Recruitment should not imply that a language reviewer speaks for an entire community. Nor should expert adjudication erase a meaningful disagreement between plausible legal interpretations. Review records should distinguish corrected errors, unresolved ambiguity, and changes to the task itself.

A target of approximately 200 newly authored scenarios offers a planning point, not a completed dataset or a guarantee of adequate power. The final size should follow a precision or power analysis using a minimally meaningful effect and scenario-level dependence. Split by underlying situation or template so that script variants and close paraphrases cannot leak from development into evaluation. Retain a documented balance of scenarios without claiming population representativeness merely from category balancing.

### Context interventions and attribution

For each held-out scenario, create a no-context condition, relevant context without conflicting personal facts, relevant context with a controlled personal-fact mismatch, and approximately length-matched irrelevant context. The personal-fact manipulation should preserve the legal topic while changing a detail whose attribution can be inspected, such as which actor performed an action. Source records or synthetic vignettes require legal review for this purpose; a vague statement that passages are relevant is insufficient.

The same context text should be shown to both script variants in the primary experiment. Otherwise, changing the script can change the retrieved passage and confound representation sensitivity with retrieval selection. A separate end-to-end experiment can permit query-dependent retrieval and evaluate the combined pipeline. Both questions matter, but their estimates answer different design decisions.

Source category labels, case names, and similarity scores should be absent from the primary content intervention. A secondary metadata experiment can add accurate provenance cues while holding passage text constant. Synthetic passages must remain clearly described as synthetic. Fabricating an official origin would introduce a different intervention and an avoidable ethical problem. Model versions, prompts, context order, token budgets, and failures should be logged so that a change in output can be linked to a defined treatment.

### Proposition-level annotation

The annotation unit is an asserted proposition about the current complaint. Two independent reviewers should label it as complaint-supported, source-only intrusion, unsupported by both complaint and source, ambiguous, or not a complaint fact. Each label should include an evidence span and a short justification. Source-only summaries correctly attributed to the retrieved case belong outside the intrusion category. Questions and conditional possibilities should be distinguished from assertions that a circumstance is true.

Reviewers should be blinded to condition metadata where feasible; text may reveal the manipulation. Preserve independent judgments and report agreement by language, script, and attribution type before adjudication. Code-switching, omitted arguments, and pragmatic intent can make literal translations underdetermine support. Record competing readings, disputed spans, and reviewer language competence; an English gloss must not settle disagreement by default. Unresolved cases remain ambiguous. Legal propositions require separate review: preserving personal facts does not establish legal correctness.

The primary case outcome is any asserted source-only personal fact attributed to the complaint. Report its count over all attempted cases alongside valid-output, substantive-response, and escalation counts; also report intrusion conditional on substantive responses. Invalid or empty responses are not successful assistance. Preserve unresolved annotation cases and report sensitivity bounds, treating them first as non-intrusion and then as intrusion. Retain proposition counts, unsupported-both assertions, and ambiguity so that lower verbosity cannot masquerade as improved fidelity.

### Analysis and safeguard evaluation

Estimate the matched difference in source-fact intrusion between conflicting-relevant and relevant-nonconflicting context. Estimate the difference in that effect across validated script representations. Resample scenario units with all their conditions and generations retained together when constructing scenario-bootstrap intervals; use larger situation clusters if dependence is introduced during authoring. Repeated generations are nested observations, not new legal situations. Freeze the primary contrast, model choice, exclusions, sample size rationale, and multiplicity family before held-out inference.

Two safeguards merit comparison: requiring complaint evidence spans for asserted personal facts, and requesting clarification or human review when the account does not support a decision. These are candidates, not validated fixes. Evaluate intrusion, classification, valid routing, invalid outputs, escalation rate, and task coverage together. A lower error rate obtained by refusing most cases is not the same result as preserving fidelity while providing appropriate assistance. Any proposed human route must be staffed and evaluated as part of the workflow.

### Minimum reporting requirements and tests of adequacy

An application should report the institutional action and acceptable alternatives; reviewed complaint representations; matched context interventions; proposition labels and evidence spans; and outcomes at stated assistance and escalation coverage. Appendix B defines worked cases and a portable reporting specification. Unmeasured outcomes must remain unmeasured, not zero. Claims of reduced intrusion require adjudicated support labels; claims of improved referral require locally justified destinations; claims of reduced burden require observed correction outcomes. Report these layers separately. Institutions and affected participants must justify consequence weights and thresholds; the protocol supplies no universal deployment threshold.

Three counterexamples test its conceptual adequacy. A correct label with an imported personal fact should fail fidelity despite passing category reproduction. A different but locally acceptable category should remain eligible to pass referral validity. An empty explanation should not be credited as successful faithful assistance solely because it contains no unsupported assertion. These are constructed tests of the measurement distinctions, not observed successes. Future applications can challenge the protocol by showing that reviewers cannot apply these distinctions reliably or that its outcomes miss consequences important to the receiving institution.

## Discussion: accountability for the account-to-route transition

### Interpretation as a source of institutional power

The pilot makes a technical sensitivity visible; the framework explains why that sensitivity can matter to an intake institution. A person's account can become legible only after the system converts it into categories already represented in institutional documents. If the model fills gaps using another case's facts, the resulting explanation may be easier for the institution to recognize while becoming less faithful to the speaker. This is a risk in the design of an intermediary, not evidence that the speakers' accounts are inherently deficient.

The appropriate response is not to treat the document corpus as a privileged description of the present complaint. It is to make provenance operational: complaint evidence supports assertions about the person, while legal sources support separately attributed information about law or comparable situations. That separation can be evaluated with spans and counterexamples. A display of citations without attribution boundaries leaves the central error untouched.

### Burdens of correction and meaningful recourse

Transparency should help someone locate a change to their account and contest it. For the proposed workflow, useful information includes the preserved original account, a plain explanation of the category, and the complaint spans used to support it. Retrieved material should be visibly separated from the speaker's claims. These requirements follow from the framework; whether a particular interface makes them understandable is a human-computer interaction question that remains untested here.

Source-fact intrusion can create a sequence of correction burdens. The speaker must first notice an alteration, distinguish it from legal terminology, dispute it in a language the service accepts, and ensure the correction reaches whoever uses the record. A person seeking help may have little time, legal familiarity, or access to translation. These are plausible vulnerability mechanisms, not characteristics measured in this dataset. A technically available appeal channel may therefore leave the practical cost of institutional error with the speaker.

We propose assigning repair responsibility to the receiving institution: preserve the original account, distinguish contested model additions from the speaker's assertions, offer correction in the preferred language, and route the dispute to a qualified person. The institution should confirm whether the correction reached downstream records and affected referrals. The speaker can correct what they intended to communicate without thereby settling disputed legal facts. Legal interpretation remains a specialist responsibility; neither role requires the speaker to diagnose the model or disprove another case. These are normative design requirements, not assertions about existing legal duties or a tested service.

Recourse evaluation should distinguish time to detect, acknowledge, correct, and propagate a correction, including translation and repeated explanation. The institution should name the owner of each step and verify downstream receipt; report unresolved cases and who bears each cost. Establishing these outcomes requires appropriately reviewed institutional or participant research.

These responsibilities are preconditions for consequential automation, not a demand that services absorb unlimited verification work. In a resource-constrained organization, interpretation, review, and follow-through compete with direct assistance. The capacity check should identify funded staff, language support, ownership, and escalation limits before model outputs control routing. If these cannot be provided, the proposed system should be withheld from that consequential role, preserving access through an existing non-automated route where available. A model's lower processing cost does not establish that the full service is affordable. Because our pilot studies no organization, this is a normative feasibility test, not an observed description of legal-aid staffing or a cost estimate.

### Why simple fallback rules are insufficient

Disagreement between retrieval and no-retrieval branches can flag instability but does not reveal which answer is correct. A rule that always prefers the no-retrieval branch reproduces that branch's labels and inherits its mistakes. Likewise, a relevance judge can approve a passage that remains dangerous to attribute to the present account. Topic relevance and evidentiary relevance are different: a document can concern unpaid wages without establishing anything else about this complainant.

Abstention is therefore a workflow intervention with benefits and costs. It can prevent an unsupported assertion while increasing delays or leaving users without an available route. A service should evaluate selective risk alongside the proportion and distribution of cases that receive assistance, and assess what happens to escalated cases. The present pilot contains no evidence that a fallback rule or confidence threshold achieves those goals.

### Reporting and governance implications

An accountable report should describe the roles and expertise of case authors and reviewers, linguistic transformations, category decisions, source-document checks, model configuration, and the institution for which a route is considered appropriate. Anonymous submissions should describe these roles without identifying researchers or participants. It should explain which materials may be released and who can authorize their reuse. An artifact that shares only prompts and an overall score leaves many of the decisive choices unaudited.

The resulting responsibilities are concrete. Language reviewers assess the account across representations; legal specialists assess categories and routes; developers investigate output attribution and failures; service owners provide correction and follow-through. These roles should be specified before deployment and revisited when models or service mappings change. The framework does not grant permission to automate intake; it identifies the evidence and responsibilities a deployment argument would need.

## Limitations and research validity

The completed evidence is a reanalysis of a small published pilot. The 60 authored scenarios do not represent the diversity of Tulu speakers, dialects, scripts, literacy practices, or experiences with legal services. Potential template dependence limits inference even when paired tests are appropriate for the observed records. Significance on this sample does not establish prevalence in a population, and a nonsignificant result does not establish equivalence or absence of harm.

Linguistic equivalence and category validity remain independently unverified for this adaptation. Script contrasts can combine model sensitivity with representation defects, and full-priming contrasts include vocabulary overlapping the evaluation examples. The adapted taxonomy does not provide a locally validated account of legal-aid routing. These limitations affect the interpretation of correctness itself, not merely the number of decimal places in an accuracy score.

The small retrieval corpus contains model-corrected extraction, identifiable information, and unresolved redistribution rights. Retrieved content is bundled with metadata and source labels in the archived conditions. Historical model settings and changing services further constrain reproducibility. The present analysis documents the supplied records but cannot reconstruct undocumented outputs or establish why one model changes its classification.

The archive has no independently adjudicated complaint-fidelity labels or observed referral outcomes. It diagnoses a measurement gap without validating the proposed instrument. Worked examples assess conceptual separations, not annotator reliability or effectiveness. In particular, the protocol may miss omissions, mistranslated uncertainty, or consequences outside a chosen category system. Annotation reliability, intervention validity, institutional relevance, and cost require empirical testing. A synthetic-context experiment would improve control while introducing ecological-validity limits; natural-document and situated service evaluations are needed to assess transfer. The Tulu/Kannada case motivates the protocol, not its general applicability to every language or institution.

The source study is already published in the ORACLE 2026 proceedings [prior]. This manuscript identifies reused evidence and does not claim that a new framing or statistical analysis alone satisfies FAccT's prior-publication requirements. The direct fidelity experiment is not yet executed. A future submission needs a genuinely distinct contribution, accurate overlap disclosure, and a complete assessment of eligibility; prose revision cannot substitute for those scientific requirements.

## Conclusion

Cross-lingual legal intake must preserve the relationship between a person's account and the category or route produced from it. Retrieved legal context can help interpret a problem, but its personal facts remain facts about another case. We have formalized that boundary through complaint fidelity and separated it from primary-category reproduction and referral validity.

The reanalysis diagnoses classification instability; it does not validate fidelity or resolve publication eligibility. The candidate protocol makes complaint evidence, external sources, and institutional actions separately inspectable. Its central question is whether the system can justify its account of the person and the institution can repair that account when it cannot.

## Ethical considerations and adverse impacts

The completed analysis uses authored scenarios and archived predictions rather than private legal-intake records. The underlying court corpus nevertheless contains personal information. Public availability does not settle privacy, consent, or redistribution rights. This manuscript does not reproduce named court excerpts; a public replication package should minimize identifying material, verify rights, and document extraction checks before release.

No new participant recruitment, community endorsement, independent legal review, or ethics approval is claimed. The proposed extension requires appropriate review, informed participation, compensation, and terms governing data use and release. Reviewers should be able to challenge the task and its categories rather than only correct outputs. Findings about particular systems must not be presented as deficits of a language, script, or community. The pilot does not support a deployable legal service, and presenting it as one could misdirect people seeking assistance.

## Generative AI usage statement

OpenAI Codex, a GPT-6-based assistant, supported the framework, full manuscript drafting and section revisions, literature checks, analysis code, and LaTeX preparation. Code was executed against archived predictions; no new model-inference results, expert labels, or participant observations were created for this manuscript. The source project reports Gemini-assisted correction of extracted legal documents; its precise model version and historical workflow require author verification. Human authors remain responsible for reviewing every claim, citation, analysis, and disclosure. Completion of that human review has not been asserted.

## References

[injecagent] Zhan et al. (2024). InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents. Findings of ACL, 10471-10506. [Source](https://aclanthology.org/2024.findings-acl.624/)

[prior] Shetty et al. (2026). Cross Lingual Transfer in Tulu Legal Comprehension: Script-Dependent Improvement and RAG-Induced Knowledge Conflict. ORACLE, 107-133. [Source](https://aclanthology.org/2026.oracle-main.8/)

[selbst] Selbst et al. (2019). Fairness and Abstraction in Sociotechnical Systems. FAT*, 59-68. [Source](https://doi.org/10.1145/3287560.3287598)

[joshi] Joshi et al. (2020). The State and Fate of Linguistic Diversity and Inclusion in the NLP World. ACL, 6282-6293. [Source](https://aclanthology.org/2020.acl-main.560/)

[bender] Bender and Friedman (2018). Data Statements for Natural Language Processing: Toward Mitigating System Bias and Enabling Better Science. TACL 6, 587-604. [Source](https://aclanthology.org/Q18-1041/)

[bird] Bird (2020). Decolonising Speech and Language Technology. COLING, 3504-3519. [Source](https://aclanthology.org/2020.coling-main.313/)

[magesh] Magesh et al. (2024). Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools. arXiv:2405.20362. [Source](https://arxiv.org/abs/2405.20362)

[list] Stanford Legal Design Lab. Legal Issues Taxonomy (LIST). Accessed October 27, 2026. [Source](https://betterinternet.law.stanford.edu/about-the-project/taxonomy-nsmiv2/)

## Appendix: complete exploratory paired comparisons

Each row compares the same 60 authored scenarios. The first three contrasts per model place Kannada script first and romanized Tulu second. The final three place retrieval first and no retrieval second, within Kannada script and a fixed priming tier. A-only and B-only count cases correct exclusively in that condition. Changes count all primary-label changes, including wrong-to-wrong transitions. Holm adjustment covers all 18 rows. These are exploratory reanalyses of the published pilot, not preregistered confirmation.

**All 18 selected paired comparisons. Positive differences favor condition A, the first condition in the pair.**

| Model | A vs B | A only | B only | Changes | Delta pp | Exact p | Holm p |
| --- | --- | --- | --- | --- | --- | --- | --- |
| llama3 | H vs G | 23 | 5 | 47 | +30.0 | 0.000912 | 0.012832 |
| llama3 | E_sparse vs M_sparse | 24 | 1 | 43 | +38.3 | 0.000002 | 0.000028 |
| llama3 | E_full vs M_full | 21 | 4 | 39 | +28.3 | 0.000911 | 0.012832 |
| llama3 | F vs H | 5 | 18 | 40 | -21.7 | 0.010622 | 0.095598 |
| llama3 | D_sparse vs E_sparse | 5 | 20 | 40 | -25.0 | 0.004077 | 0.044850 |
| llama3 | D_full vs E_full | 4 | 26 | 43 | -36.7 | 0.000059 | 0.001011 |
| hex1 | H vs G | 21 | 6 | 50 | +25.0 | 0.005925 | 0.059246 |
| hex1 | E_sparse vs M_sparse | 20 | 4 | 46 | +26.7 | 0.001544 | 0.018527 |
| hex1 | E_full vs M_full | 25 | 4 | 43 | +35.0 | 0.000104 | 0.001659 |
| hex1 | F vs H | 5 | 7 | 32 | -3.3 | 0.774414 | 1.000000 |
| hex1 | D_sparse vs E_sparse | 6 | 8 | 30 | -3.3 | 0.790527 | 1.000000 |
| hex1 | D_full vs E_full | 2 | 10 | 22 | -13.3 | 0.038574 | 0.308594 |
| sarvam | H vs G | 16 | 7 | 37 | +15.0 | 0.093140 | 0.558838 |
| sarvam | E_sparse vs M_sparse | 15 | 5 | 38 | +16.7 | 0.041389 | 0.308594 |
| sarvam | E_full vs M_full | 19 | 3 | 35 | +26.7 | 0.000855 | 0.012832 |
| sarvam | F vs H | 7 | 4 | 17 | +5.0 | 0.548828 | 1.000000 |
| sarvam | D_sparse vs E_sparse | 9 | 4 | 22 | +8.3 | 0.266846 | 1.000000 |
| sarvam | D_full vs E_full | 3 | 7 | 19 | -6.7 | 0.343750 | 1.000000 |


## Appendix: worked protocol examples and reporting specification

### Purpose and status

The examples below simplify attribution decisions in English for exposition. They do not reproduce Tulu pragmatics, code-switching, or variation across scripts. Applying the codebook requires language-competent reviewers and retention of competing interpretations, not translation of these examples as ready-made validation cases. They are not archived model outputs, legal advice, translated Tulu data, expert annotations, or new empirical evidence. All share a toy complaint: "My employer has not paid this month's wages." A synthetic context concerns a different employee dismissed after an absence. Topic relevance does not authorize attributing that absence or dismissal to the present complaint.

### Attribution examples and boundary cases

Example 1, category match with intrusion. An output assigns an employment category and states, "Your employer dismissed you after you were absent." The category can match while the personal-fact assertion is supported only by context. Code the asserted dismissal and absence as source-only intrusion. A matching label does not rescue their attribution.

Example 2, source distinction preserved. An output states, "The source concerns dismissal after absence; your account reports unpaid wages and does not mention dismissal." The source summary is not a current-complaint fact. The account summary is complaint-supported. No intrusion follows merely from mentioning the source, and this judgment does not certify legal correctness.

Example 3, fabricated detail. An output states, "You have gone unpaid for six months." Neither the complaint nor the toy context supports that duration. Code it unsupported by both, not source-only intrusion. Conflating these categories would obscure whether a controlled context supplied the asserted detail.

Example 4, uncertainty and clarification. An output asks, "Were you also dismissed?" A genuine question is not an assertion that dismissal occurred. Record clarification and assistance coverage. If later text presupposes dismissal as established, annotate that proposition separately. An empty or invalid response contains no asserted intrusion but does not count as successful faithful assistance.

Example 5, disputed routing. Suppose a hypothetical service's independently reviewed rules accept two different labels for the same wage-help route. A prediction can miss the dataset's designated label while satisfying that local route rule. This illustrates why reference-label accuracy and referral validity need separate evidence; no acceptable real-world legal destination is asserted by the example.

These examples communicate instructions, not evidence of agreement. A multilingual annotation record should preserve the original span, alternative glosses, pragmatic readings, whether code-switching affects the judgment, and each independent label. Disagreement is an auditable outcome, not noise to remove by forcing a literal translation. Report it by representation and keep unresolved interpretations visible in sensitivity bounds. Revise the distinctions if qualified reviewers cannot apply them reliably.

### Reporting specification and claim boundaries

A portable report should contain a study identifier and evidentiary status; the intended institutional action; dataset origin, languages, scripts, and review status; scenario and template identifiers; pinned model and prompt identifiers; context provenance and intervention; independent annotations and adjudication; outcome numerators and denominators; and a correction-owner record. Public reports should use non-identifying identifiers and omit personal narratives unless release is justified. Anonymized review material should not link to author-identifying repositories.

For every model and condition, record attempted cases, invalid outputs, substantive responses, escalations, confirmed intrusion, and unresolved labels. Report all-case intrusion and conditional intrusion among substantive responses together. An all-case estimate alone can reward silence; a conditional estimate alone can conceal excluded cases. Bound unresolved cases explicitly. Valid routes and correction outcomes remain null with status "not measured" until their respective evidence is collected; zero is reserved for an observed count of zero.

The accompanying reporting template and annotation examples implement this specification as editable artifacts. Their fields document requirements, not completed observations. They are a candidate reporting convention for adaptation and challenge, not an endorsed standard, certification, or deployment authorization.
