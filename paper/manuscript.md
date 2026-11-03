# Whose Facts Count? Complaint Fidelity and Language Equity in Cross-Lingual Legal Intake

**Working manuscript. Development scenarios and supplementary archived evidence are reused from Shetty et al.; 384 new exploratory local-model calls are reported here. Expert fidelity validation remains unexecuted.**

## Abstract

This paper develops a normative and methodological framework for evaluating cross-lingual legal intake. It separates category reproduction, complaint fidelity, and locally appropriate referral, and assigns institutions responsibility for repairing unsupported personal attributions. Earlier Tulu/Kannada classification findings motivate the distinction; the methodological contribution concerns support for personal assertions and institutional correction. A new exploratory experiment partially instantiates the protocol: 384 local-model calls cross 16 reused development scenarios, three query representations, four English synthetic-context conditions, and two prompting policies. Of these, 308 yield valid structured outputs and 76 truncate. Literal source-marker echoes occur in structured complaint-fact fields, but automated screening does not establish factual intrusion. The prompt guard does not consistently improve category reproduction, and none of the secondary paired comparisons passes Holm correction. English contexts repeat scenario glosses and can act as oracle translation scaffolds; the experiment does not evaluate natural retrieval or independently validated Tulu understanding. The primary contribution is an evidentiary boundary, proposed attribution typology, and reusable protocol linked to an institutional repair workflow; these are candidate methods and design requirements, not validated interventions. A post-hoc audit adds missing-output bounds, case/category omission checks, and lexical-dependence stress tests. Expert proposition annotations, linguistic validation, and referral outcomes remain absent; these diagnostics do not validate the framework.

## Introduction

A person describes a problem in their own words. An intake system decides which category fits, what information to display, or which service to suggest. This transition from account to category is a consequential point of interpretation. The person may describe unpaid wages, money withheld by a landlord, or a disagreement over land without using the vocabulary of a legal institution. A system that recognizes the words but changes the relationship between the actors can produce a plausible explanation of the wrong problem. The concern is especially relevant when the complaint and the legal material used to interpret it are written in different languages.

This paper examines that problem through Tulu complaint classification with Kannada legal context. A related language and shared script can offer useful computational resources, but they also structure which representations a system handles well. Retrieval adds another intermediary: a document about someone else's dispute. Its legal relevance does not make its personal facts evidence about the current complainant. For intake, a system must preserve a boundary between interpreting the account and replacing it with a better documented account drawn from an institution's records.

We call the preservation of that boundary complaint fidelity. The term concerns whether the output's assertions about the current complaint are supported by what the person supplied, including uncertainty and ambiguity. It does not mean accepting every claim as legally established, deciding a dispute in the speaker's favor, or treating a model-generated explanation as a transcript of internal reasoning. It asks a prior question: does the system still describe the problem that was presented to it?

Our position is that category accuracy alone is insufficient for evaluating equitable legal intake. A label can match a reference category even when the explanation invents facts. A label can differ from a benchmark and still be an acceptable route in a particular service. An abstaining system can avoid an unsupported assertion while leaving the person without help. These outcomes involve different mechanisms and responsibilities. Combining them into a single accuracy score obscures both the limits of the evidence and the decisions required of a receiving institution.

Shetty and colleagues evaluated category prediction under script, priming, and retrieval interventions and identified fact substitution [prior]. Our central question is one of sociotechnical governance: what authorizes a personal assertion, and who bears responsibility for repairing it? The object is the institutionally usable account, not a higher leaderboard score. We reuse their development scenarios for an exploratory diagnostic; their classification findings motivate the question without measuring complaint fidelity or referral outcomes.

The paper addresses three questions. RQ1: What evidence should authorize an assertion about a complainant, separately from category agreement? RQ2: What do controlled-context generations and missing-output sensitivity reveal about the limits of automated attribution screening? RQ3: What validation and institutional correction responsibilities should a complaint-fidelity evaluation require?

The contribution has three parts: an evidentiary boundary between complaint facts and source facts; a candidate protocol specifying annotation, controlled comparisons, and claim-specific evidence; and institutional responsibilities for correcting unsupported attributions. Appendix B supplies worked examples and a reporting specification. A new controlled-context diagnostic supplies 384 generations from one local model on 16 reused development scenarios, with missing-output and leverage analyses. It partially instantiates the protocol without supplying expert fidelity labels, linguistic validation, or participant evidence. Detailed historical benchmarks are left to the source study and audit artifact rather than reproduced as this paper's main results.

The architectural question extends to agents that carry external content into forms, summaries, or routing calls: what authorizes each personal assertion? This case does not measure downstream actions or cross-domain harms. Intake support remains distinct from legal advice and adjudication; consequences depend on the institution.

## Setting: language, categories, and institutional recognition

### A multilingual intake problem

The pilot pairs Tulu descriptions of everyday legal problems with Kannada legal documents. We examine this intermediary without inferring speakers' preferred scripts, proficiency, or service experiences. Different people may use different conventions or switch languages. Better performance on one representation does not justify requiring speakers to adopt it; conversion can impose work or erase distinctions. Those costs require situated evidence.

Intake links eliciting an account, interpreting it, assigning categories, and selecting a next step. The archived task measures only category agreement against authored labels. It includes neither conversational elicitation nor a real service directory. Benchmark error, representation inconsistency, and unsuitable referral are different outcomes.

### Category systems as institutional choices

The source labels are adapted from the Stanford Legal Design Lab's Legal Issues Taxonomy, LIST. The originating project describes a taxonomy of legal problems in the United States [list]. The pilot's use of these categories does not establish their suitability for Indian legal-aid intake. We therefore describe the outcome as LIST-inspired primary-category reproduction. We do not describe the authored primary label as the uniquely correct legal interpretation of a complaint.

Consider a complaint that a landlord has not returned money. Housing and a money-related category can both describe part of the account. Whether either is an appropriate destination depends on a service's responsibilities and referral rules. This example illustrates a construct problem rather than resolving the legal classification of a real case. A specialist review would need to determine which distinctions affect assistance, which alternatives are acceptable, and which categories conceal a meaningful difference in circumstances.

The taxonomy therefore belongs inside the audit. It should not operate as an unquestioned standard against which a minority-language account is judged deficient. Label review must distinguish unclear wording, disagreement among qualified reviewers, and a category set that does not match the receiving institution. A model should not receive credit for reproducing an invalid category boundary merely because the benchmark encodes it consistently.

### Stakeholders and responsibilities

The relevant roles include the speaker, language reviewers, legal-aid staff, developers, and the receiving institution. Linguistic equivalence, legal routing, and technical diagnosis require distinct expertise. Developers cannot substitute model inspection for the institution's decisions about assistance and correction.

These responsibilities are proposed; no service partnership or completed consultation is asserted. Participants should be able to challenge the task, categories, and interface or decline automation. Supplying labels alone does not confer authority over these decisions.

## Related work and the gap addressed

### Fairness beyond a predictive label

Selbst and colleagues describe how technical abstraction loses social context [selbst]. Transforming a complaint into a category raises questions about faithful interpretation, institutional routing, and correction authority. A script-associated accuracy difference alone cannot answer them.

### Language inclusion and data documentation

Joshi and colleagues document uneven language representation in NLP [joshi]. Resource categories do not establish a model's Tulu exposure or an individual's capabilities. Bender and Friedman's data statements motivate documenting authored scenarios, script production, reviewer expertise, and generalization boundaries [bender]. Parallel scripts represent the same cases, not separate speaker populations.

### Authority over language resources

Bird critiques extractive approaches to language technology [bird]. Additional Tulu material should involve authority over use, interpretation, and release, rather than speaker review as a final quality check. The question is which decisions affected people can influence, without treating every language community as interchangeable.

### Retrieval and legal reliability

Magesh and colleagues evaluate reliability failures in commercial legal research tools that use retrieval [magesh]. That work supports examining outputs rather than relying on an assurance that retrieved sources prevent error. Its task differs from ours: finding or synthesizing legal information is not the same as interpreting a new complaint. Our concern is the transfer of factual content across that boundary. Even if a retrieved case and every citation are genuine, a model can misattribute its facts to the current speaker. Citation existence and complaint fidelity therefore require separate measurements. Zhan and colleagues study malicious external instructions in tool-integrated agents [injecagent]. Our concern differs: ordinary source facts can be misattributed without an attack. The architectural connection is the need to track what external content is authorized to determine, not an assertion that the pilot measures prompt injection.

### Relationship to the published Tulu study

Shetty and colleagues reported script-dependent classification, mixed retrieval effects, and fact substitution or confabulation [prior]. We retain those findings as motivation. The present proposal evaluates attributed propositions and institutional repair, rather than claiming those failure observations as new. Supplementary archived comparisons are not independent replication or fidelity validation.

## A complaint-fidelity framework

### Three outcomes that should remain separate

Category reproduction measures whether the predicted primary label equals the dataset's designated primary label. It is inexpensive to compute from the archive and permits a matched audit. Its meaning depends on the validity of the labels. In particular, a low score does not establish that a system denied a useful service, and a high score does not establish that the underlying account was preserved.

Complaint fidelity measures whether assertions about the current complainant's actors, events, relationships, and circumstances are supported by the complaint. Support includes justified paraphrase but not an invented detail made plausible by a retrieved case. It must also account for modality: an assertion that an event occurred is different from a question about whether it occurred. An explanation that clearly describes a source case as a source case should not be coded as intrusion merely because it contains facts absent from the complaint.

Referral validity measures whether a suggested next step is appropriate under a locally specified service arrangement. It requires legal and institutional judgment, potentially including multiple acceptable routes. The archived labels are not a substitute for those judgments. A referral can be valid despite a primary-label mismatch; a matching label can still lead to an unsuitable route if the service mapping is incorrect or outdated.

**Evaluation layers and the evidence needed to assess them.**

| Layer | Audit question | Evidence in this paper |
| --- | --- | --- |
| Category reproduction | Does the output match the designated primary label? | 384 new calls on reused development cases; labels not independently validated. |
| Complaint fidelity | Are assertions about this complaint supported by the account? | Protocol and literal-marker screen; no expert-labeled fidelity results. |
| Referral validity | Is the next step appropriate for a specified service? | Institutional validation proposed; no observed referral outcomes. |

### An evidence boundary for personal facts

Let a complaint, a retrieved context, and a model output be considered together. For each asserted proposition about the current complaint, an annotator asks whether the complaint supports it and whether the retrieved context supports it. Complaint-supported propositions preserve the relevant boundary. A proposition supported only by context becomes source-fact intrusion when the output attributes it to the present complaint. A proposition supported by neither is unsupported fabrication for this audit. Ambiguous cases remain explicit rather than being forced into either error type.

For illustration, imagine an authored complaint stating only that an employer withheld wages. A retrieved vignette concerns an unrelated employee dismissed after an absence. If the output states that the current complainant was dismissed for absence, it has imported a source fact. If it instead says that the retrieved vignette involves dismissal while the current complaint concerns unpaid wages, it has preserved attribution. This example is a methodological illustration created for the framework, not an observed model output or a legal determination.

The framework does not require a claim about internal knowledge conflict. The observable failure is an unsupported attribution, whatever combination of parsing, instruction following, retrieval, or generation produced it. This avoids treating a fluent generated rationale as reliable evidence of the model's reasoning process. A causal claim about why attribution changes requires controlled interventions and cannot be established from one explanation.

### Proposed typology of attribution errors

We separate what a proposition changes from where its support originates. Support labels remain complaint-supported, source-only, unsupported by both, ambiguous, or outside current-complaint attribution. The typology below adds nonexclusive content tags; it does not replace those labels. All examples are constructed, not findings from the 384 generations.

**Proposed nonexclusive content tags for attribution audit. Examples are hypothetical unsupported assertions, not observed outputs or statements of law.**

| Content tag | Constructed change to the account | Boundary to check |
| --- | --- | --- |
| Actor | An unnamed employer becomes the named defendant in a source case. | Whose action or identity is asserted? |
| Event / relationship | A wage complaint becomes dismissal after an absence. | Is this event or relation in the account? |
| Time / procedure | A source case filing date becomes the speaker's filing date. | Distinguish a source timeline from this case. |
| Amount / place | A source award or location becomes the speaker's loss or residence. | Do not transfer amounts or places. |
| Legal status | A source party's employment status is assigned to the speaker. | Separate factual premise from legal applicability. |
| Modality | A possible event becomes an established assertion. | Preserve uncertainty, negation, and questions. |

A source-only assertion about the current person can receive several content tags. A correctly attributed source summary, genuine clarification question, or general legal rule does not become intrusion merely by mentioning the same topic. Applying a doctrine to the person can instead require legal judgment even when its factual premise is complaint-supported; that question remains separate from fidelity. Omitted complaint facts are another dimension not covered by this intrusion typology. Independent multilingual application must test tag coverage, disagreements, and utility before reporting frequencies or claiming reliability.

### Language equity as a conditional evaluation target

We investigate whether representation choices systematically change the quality of the same account's treatment. A matched comparison is useful because it holds the authored situation constant. However, it depends on semantic equivalence between versions. A difference caused by faulty transliteration is a representation-pipeline problem, while a difference between independently validated representations is stronger evidence of model sensitivity. Both matter to a service, but they support different technical conclusions.

Equal error rates across scripts would not be sufficient for equitable intake: every version could perform poorly, and users could face unequal burdens in producing a version the system accepts. Conversely, unequal benchmark scores do not automatically establish unequal service outcomes. An evaluation should report absolute quality, differences across representations, unsupported factual assertions, and the availability of a meaningful correction route. These outcomes inform a normative assessment; they do not replace it with a single fairness score.

### A conditional pathway from error to harm

A plausible pathway begins with a change in representation or context, continues through an altered interpretation or category, and reaches an adverse consequence only if an institution acts on it in a consequential way. Inappropriate information, additional translation work, repeated explanation, or delay are possible consequences. They are hypotheses about a workflow in this study. We have neither measured them nor established which services would generate them.

Each link requires evidence: a category change may preserve the account, two labels may lead to the same service, or a distortion may be corrected before routing. Conversely, a small classification difference may matter under a rigid referral rule. Audits should identify where their evidence stops.

## Data provenance and controlled-context methods

### Reused development scenarios and motivating evidence

The source study provides 60 authored Tulu legal scenarios with English glosses, romanized and Kannada-script representations, and LIST-inspired primary categories [prior]. The new experiment uses a 16-scenario subset, not a new held-out dataset or a sample of speakers. Neither translation equivalence nor category validity has been independently established for this adaptation. We do not treat the English gloss as unquestioned linguistic ground truth or the category as a validated legal route.

The original study reports classification changes under script, priming, and retrieval interventions, along with fact-substitution examples [prior]. These motivate separate attribution measurement; a category change alone cannot establish source-fact intrusion. Its retrieved Kannada court records are not used as context in the new experiment. We retain one supplementary archive sensitivity analysis to assess whether a motivating decline is sensitive to simple lexical grouping; it does not validate fidelity. The complete historical audit remains in the artifact, with provenance summarized in Appendix A.

### New controlled-context diagnostic: design and measurement

We generate new outputs from the installed local llama3.2:1b model (metadata: 1.2B parameters, Q8_0), distinct from the historical pilot models. A fixed seed selects two scenarios per existing primary category, giving 16 reused development cases. Each has English-gloss, romanized-Tulu, and Kannada-script-Tulu queries, four contexts, and baseline or fidelity-guard instructions: 384 calls, one generation per cell. The guard asks the model to separate source facts from personal facts, assert only complaint-supported details, and retain uncertainty. It is a candidate intervention, not a validated safeguard.

Contexts are fixed English synthetic vignettes, identical across query representations and policies. No context supplies no vignette. Relevant context repeats the scenario's English gloss as an illustrative case about a different person. Relevant-with-details adds a separate claimant's age 47 and incident year 2019; irrelevant-with-details uses a different-category scenario with the same markers. These numerals are absent from the selected complaint glosses. Relevant context supplies an oracle semantic scaffold, potentially a translation aid; this is not natural retrieval from Kannada court records. Added details also change length. The design does not isolate semantic conflict from every wording or length effect.

Inputs and a randomized schedule were frozen before main inference, with temperature 0, seed 20261030, context budget 4096, and output budget 512 tokens. Two prior infrastructure smoke calls at 180 tokens both truncated and remain separately archived; the larger budget was selected afterward. This is exploratory, not preregistered. A JSON schema requests a category, up to three complaint facts, and an explanation. Requests, raw responses, model digest, options, input hashes, and timings are retained. Appendix C provides full condition and paired results.

All-attempt category scoring counts incomplete structures as errors. A literal screen checks valid complaint-fact fields for 47 or 2019; this is a marker echo, not adjudicated source-fact intrusion. Negation and quotation can trigger it, while paraphrase and spelled-out numbers can escape it. No expert labels are produced. Secondary guard-versus-baseline comparisons use two-sided exact McNemar tests, with separate Holm families of 12 category contrasts and six marker contrasts. Category comparisons retain all 16 attempts per cell; marker comparisons require both paired outputs to be valid and can therefore be selection-biased. No script-by-policy interaction or population effect is established. A post-hoc sensitivity audit bounds every unobserved marker outcome over all attempts and omits one scenario or category at a time for category-score contrasts. Lexical connected components of English glosses stress-test the archived Llama3 decline at five Jaccard thresholds; these groups are not verified templates. Appendix D gives definitions and complete bounds.

## Exploratory controlled-context results

### New generations: coverage, marker screening, and prompt comparison

All 384 scheduled calls completed: 308 produced valid structures and 76 reached the output-token limit with incomplete responses; there were no transport errors. Coverage varies across conditions, so apparent category differences combine label agreement and successful structure completion. The table reports the source-detail cells with explicit denominators; Appendix C includes all 24 cells, including no-context and relevant-context controls.

**New source-detail conditions: correct categories / attempts and literal echoes / valid outputs. E: English; T: romanized Tulu; K: Kannada script; RD: relevant details; ID: irrelevant details; B: baseline; G: guard. Echoes are not expert intrusion labels.**

| Query | Context | Correct B | Correct G | Echo B | Echo G |
| --- | --- | --- | --- | --- | --- |
| E | RD | 8/16 | 7/16 | 11/16 | 5/12 |
| E | ID | 3/16 | 4/16 | 2/15 | 3/10 |
| T | RD | 4/16 | 4/16 | 7/16 | 3/16 |
| T | ID | 0/16 | 0/16 | 7/15 | 6/16 |
| K | RD | 1/16 | 2/16 | 1/9 | 2/9 |
| K | ID | 0/16 | 0/16 | 1/7 | 1/11 |

Valid-output coverage is uneven: English has 4/64 baseline and 13/64 guard failures, romanized Tulu 1/64 and 0/64, and Kannada script 26/64 and 32/64. Thus Kannada-script conditions account for 58/76 failures. These are completion differences in this configuration, not independently validated language-comprehension differences.

For English relevant-with-details, echoes occur in 11/16 valid baseline outputs and 5/12 guard outputs. Allowing each missing marker outcome to take either value gives a guard-minus-baseline bound of [-37.5, -12.5] percentage points across all 16 attempts. Kannada relevant-with-details instead spans [-37.5, +50.0]. These are finite-sample missing-outcome bounds, not confidence intervals, intrusion estimates, or predictions of longer generations. They do not remove sampling uncertainty. Appendix D reports every source-detail bound rather than selecting favorable directions.

No secondary category or valid-pair marker contrast passes its separate Holm correction; all adjusted p-values are 1. Category effects remain mixed. Omitting any one category leaves the Kannada relevant-context guard-minus-baseline score between -28.6 and -14.3 points, while its relevant-with-details difference spans 0 to +7.1 points. These post-hoc leverage checks do not establish independence. For the archive, equal-weight lexical-group versions of the Llama3 full-priming retrieval decline range from -37.3 to -36.7 points across the tested thresholds; no cluster-based significance claim is made.

The sensitivity audits test how fragile screening summaries are to incomplete outputs and scenario weighting. They do not repair missing responses or establish independence. Reporting all bounds and perturbations exposes assumptions that a single valid-output score hides.

The fresh generations make the protocol's evidence boundary operational: category agreement, structured-output coverage, and literal source-marker presence yield different observations. They do not establish whether an assertion actually attributes a source fact to the complainant. No expert complaint-fidelity annotations, locally valid routing assessments, or observed assistance outcomes are available. The completed experiment is a development diagnostic, not independent validation of the framework or an estimate of harm prevalence.

## A reusable protocol for complaint-fidelity evaluation

### Methodological contribution and evidentiary status

The protocol translates institutional responsibility for justified personal assertions into auditable units, controls, outcomes, and repair requirements. It is a candidate method for administrative tools that interpret accounts using external documents. It is neither community-endorsed nor empirically validated; categories, language representations, and consequences require local review.

The specification and editable reporting artifacts are openly available as a candidate design tool for other administrative settings where institutional documents inform personal accounts, such as benefits intake. Transfer requires new language, category, and action validation; neither generalizability nor community endorsement follows from releasing code. We call this a reusable candidate protocol, not an established evaluation standard.

The new experiment implements only synthetic-context comparisons and screening. The full independently annotated study remains unexecuted; effectiveness, reliability, and feasibility are empirical questions. The reused scenarios remain development material because the protocol follows inspection of their outputs.

The primary question is whether conflicting but relevant context increases the fraction of outputs that attribute source-only personal facts to the current complaint. A second question is whether that context effect differs between independently validated Kannada-script and romanized Tulu. The latter requires estimating an interaction directly. One significant within-script effect and one nonsignificant effect would not establish that the effects differ.

### Independent linguistic and legal validation

Before a confirmatory multilingual study, independent fluent reviewers should assess each representation against the intended scenario. They should record alternative interpretations, orthographic variation, and uncertainty rather than silently normalizing every account toward one form. Separate legal-aid reviewers should assess the category set and acceptable routes under an explicitly described service arrangement. A representation can be linguistically equivalent while both versions inherit an invalid reference category.

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

### Proposed institutional repair workflow

We operationalize institutional responsibility as five stages, with explicit owners and exit conditions. This is a normative workflow specification; no institution has implemented or evaluated it here.

Stage 1, intake staff preserve a versioned original account and record language preferences under a defined access and retention policy. Stage 2, the interface separates that account, model assertions, and external context. Each asserted personal fact points to a complaint span or remains visibly unsupported; a model-generated support link is unverified until checked. Stage 3, unsupported or contested assertions place consequential routing on hold and enter a staffed review queue with an assigned owner. The speaker can request correction or decline automation without diagnosing the model.

Stage 4, language-competent staff resolve intended meaning with the speaker, while qualified service staff separately assess the route. They record unresolved disagreement and revised assertions rather than replacing the original account. Stage 5, the institution sends versioned corrections to affected destinations, verifies receipt, and communicates the outcome in an accessible form. A case closes only after required correction checks succeed or is recorded as unresolved. Queue delay and loss of assistance remain reportable costs. Without funded review capacity, consequential automated routing is withheld. Appendix E supplies a proposed interface and event record; neither is a tested deployment.

### Why simple fallback rules are insufficient

Disagreement between retrieval and no-retrieval branches can flag instability but does not reveal which answer is correct. A rule that always prefers the no-retrieval branch reproduces that branch's labels and inherits its mistakes. Likewise, a relevance judge can approve a passage that remains dangerous to attribute to the present account. Topic relevance and evidentiary relevance are different: a document can concern unpaid wages without establishing anything else about this complainant.

Abstention is therefore a workflow intervention with benefits and costs. It can prevent an unsupported assertion while increasing delays or leaving users without an available route. A service should evaluate selective risk alongside the proportion and distribution of cases that receive assistance, and assess what happens to escalated cases. The present pilot contains no evidence that a fallback rule or confidence threshold achieves those goals.

### Reporting and governance implications

An accountable report should document authoring and review roles, language transformations, category decisions, source checks, model configuration, release authority, and intended institution. Language reviewers assess representations; legal specialists assess categories and routes; developers investigate attribution and failures; service owners provide correction. These roles require reassessment when models or service mappings change. The framework identifies evidence and responsibilities a deployment argument would need.

## Limitations and research validity

The empirical demonstration comprises new exploratory generations on 16 development scenarios reused from a published 60-scenario study, plus supplementary sensitivity analyses of archived outputs. The 60 authored scenarios do not represent the diversity of Tulu speakers, dialects, scripts, literacy practices, or experiences with legal services. Potential template dependence limits inference even when paired tests are appropriate for the observed records. Significance on this sample does not establish prevalence in a population, and a nonsignificant result does not establish equivalence or absence of harm.

Linguistic equivalence and category validity remain independently unverified for this adaptation. Script contrasts can combine model sensitivity with representation defects, and full-priming contrasts include vocabulary overlapping the evaluation examples. The adapted taxonomy does not provide a locally validated account of legal-aid routing. These limitations affect the interpretation of correctness itself, not merely the number of decimal places in an accuracy score.

The small retrieval corpus contains model-corrected extraction, identifiable information, and unresolved redistribution rights. A hash-based inventory records its 18 entries and unverified extraction and rights status without copying court narratives; court text remains excluded from the release package. Retrieved content is bundled with metadata and source labels in the archived conditions. Historical model settings and changing services further constrain reproducibility. The present analysis documents the supplied records but cannot reconstruct undocumented outputs or establish why one model changes its classification.

The archive has no independently adjudicated complaint-fidelity labels or observed referral outcomes. It diagnoses a measurement gap without validating the proposed instrument. Worked examples assess conceptual separations, not annotator reliability or effectiveness. In particular, the protocol may miss omissions, mistranslated uncertainty, or consequences outside a chosen category system. Annotation reliability, intervention validity, institutional relevance, and cost require empirical testing. The new synthetic-context experiment improves some controls but uses only one 1.2B local model, one generation per cell, unvalidated representations, and English gloss-repeating contexts. Its 76 truncated outputs constrain scoring and induce selection in valid-pair marker comparisons. Missing-outcome bounds make that uncertainty explicit without recovering the absent facts. Lexical stress tests and omission ranges diagnose limited dependence and leverage; they neither identify true authoring templates nor justify treating cases as independent. Literal screening cannot replace proposition-level judgment; context length, translation assistance, and semantic relevance remain entangled. Natural-document and situated service evaluations are needed to assess transfer. The Tulu/Kannada case motivates the protocol, not its general applicability to every language or institution.

The reused scenarios and historical outputs originate in Shetty et al. [prior]; they are not new data produced by this manuscript. The framework, new exploratory generations, and post-hoc sensitivity analyses must be assessed on their own contributions and limitations. The independent, expert-annotated fidelity study remains unexecuted.

## Conclusion

Complaint fidelity separates support for personal assertions from category agreement and locally valid referral. The 384 new exploratory generations and sensitivity analyses illustrate the measurement distinctions without validating complaint fidelity. The protocol asks whether systems can justify their account of the person and institutions can repair it. Independent annotations and situated evaluation remain necessary.

## Ethical considerations and adverse impacts

The completed analysis uses authored scenarios, archived predictions, and new local generations with synthetic contexts rather than private legal-intake records. No real court documents were sent to the local model in the new experiment. The underlying court corpus nevertheless contains personal information. Public availability does not settle privacy, consent, or redistribution rights. This manuscript does not reproduce named court excerpts; a public replication package should minimize identifying material, verify rights, and document extraction checks before release.

No new participant recruitment, community endorsement, independent legal review, or ethics approval is claimed. The proposed extension requires appropriate review, informed participation, compensation, and terms governing data use and release. Reviewers should be able to challenge the task and its categories rather than only correct outputs. Findings about particular systems must not be presented as deficits of a language, script, or community. The pilot does not support a deployable legal service, and presenting it as one could misdirect people seeking assistance.

## Generative AI usage statement

OpenAI Codex, a GPT-6-based assistant, supported the framework, full manuscript drafting and section revisions, literature checks, analysis code, and LaTeX preparation. Code was executed against archived predictions, and assistant-supported code ran and analyzed 384 new local llama3.2:1b generations, with two earlier infrastructure smoke calls preserved separately. Generations are model outputs, not human judgments. No expert labels or participant observations were created for this manuscript. The source project reports Gemini-assisted correction of extracted legal documents; its precise model version and historical workflow require author verification. Human authors remain responsible for reviewing every claim, citation, analysis, and disclosure. Completion of that human review has not been asserted.

## References

[injecagent] Zhan et al. (2024). InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents. Findings of ACL, 10471-10506. [Source](https://aclanthology.org/2024.findings-acl.624/)

[prior] Shetty et al. (2026). Cross Lingual Transfer in Tulu Legal Comprehension: Script-Dependent Improvement and RAG-Induced Knowledge Conflict. ORACLE, 107-133. [Source](https://aclanthology.org/2026.oracle-main.8/)

[selbst] Selbst et al. (2019). Fairness and Abstraction in Sociotechnical Systems. FAT*, 59-68. [Source](https://doi.org/10.1145/3287560.3287598)

[joshi] Joshi et al. (2020). The State and Fate of Linguistic Diversity and Inclusion in the NLP World. ACL, 6282-6293. [Source](https://aclanthology.org/2020.acl-main.560/)

[bender] Bender and Friedman (2018). Data Statements for Natural Language Processing: Toward Mitigating System Bias and Enabling Better Science. TACL 6, 587-604. [Source](https://aclanthology.org/Q18-1041/)

[bird] Bird (2020). Decolonising Speech and Language Technology. COLING, 3504-3519. [Source](https://aclanthology.org/2020.coling-main.313/)

[magesh] Magesh et al. (2024). Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools. arXiv:2405.20362. [Source](https://arxiv.org/abs/2405.20362)

[list] Stanford Legal Design Lab. Legal Issues Taxonomy (LIST). Accessed October 27, 2026. [Source](https://betterinternet.law.stanford.edu/about-the-project/taxonomy-nsmiv2/)

## Appendix: provenance of reused evidence

Shetty et al. [prior] report the original Tulu classification study. The source archive contains 60 authored scenarios and 3,420 predictions across three models and 19 conditions. Repeated representations are not independent speakers or situations. None of these historical generations is counted among the 384 new local-model calls reported here.

The accompanying historical audit checks unique model-condition-scenario keys, completeness, source-label agreement, and consistency with stored scores; 33 explicit invalid primary outputs count as errors. It records 18 exploratory paired exact McNemar contrasts with Holm correction. Their full condition definitions, scores, transitions, and statistical tables remain in the machine-readable and Markdown audit artifacts, rather than being reproduced in this manuscript. They are neither independent replication nor expert complaint-fidelity annotation.

Appendix D retains a new lexical grouping stress test of one motivating archived contrast: Llama3 retrieval versus no retrieval under full Kannada-script priming. Before grouping, that contrast is 14/60 versus 36/60 designated-label matches. Its role is limited to sensitivity of the motivation; it does not estimate intrusion or referral harm. The court-text provenance inventory documents unresolved extraction, privacy, and rights questions without reproducing those records. The new controlled-context experiment uses English synthetic vignettes instead.

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

## Appendix: new controlled-context experiment and complete results

### Reproducibility and scope

The main run uses scenario identifiers 6, 11, 16, 20, 23, 24, 29, 31, 32, 36, 39, 48, 49, 52, 54, and 58. Selection and scheduling use seed 20261030. The full installed-model SHA-256 digest is retained in the artifact metadata (prefix baf6a787fdff). Main inference ran October 30-31, 2026 UTC. The artifact retains all 384 payloads and raw responses, code and input hashes, structured answers, failures, and model metadata. The two earlier truncated smoke calls are excluded from the 384-call results and preserved separately. There are no hidden inference retries.

Context codes N, R, RD, and ID mean none, relevant, relevant-with-details, and irrelevant-with-details. E, T, and K denote English gloss, romanized Tulu, and Kannada-script Tulu. B and G mean baseline and fidelity guard. Every condition attempts 16 cases. Correct counts require a complete valid structure and designated primary-label agreement; marker fractions use valid structured outputs only. Marker presence is a literal screen, not a source-attribution judgment. No expert fidelity or referral outcome is measured.

**All 24 new conditions, with 16 attempts each. Correct counts include invalid outputs as errors.**

| Query | Context | Policy | Valid | Correct | Echo / valid |
| --- | --- | --- | --- | --- | --- |
| E | ID | B | 15 | 3 | 2/15 |
| E | ID | G | 10 | 4 | 3/10 |
| E | N | B | 14 | 7 | 0/14 |
| E | N | G | 15 | 8 | 0/15 |
| E | R | B | 15 | 7 | 0/15 |
| E | R | G | 14 | 9 | 0/14 |
| E | RD | B | 16 | 8 | 11/16 |
| E | RD | G | 12 | 7 | 5/12 |
| K | ID | B | 7 | 0 | 1/7 |
| K | ID | G | 11 | 0 | 1/11 |
| K | N | B | 10 | 0 | 0/10 |
| K | N | G | 6 | 0 | 0/6 |
| K | R | B | 12 | 4 | 0/12 |
| K | R | G | 6 | 0 | 0/6 |
| K | RD | B | 9 | 1 | 1/9 |
| K | RD | G | 9 | 2 | 2/9 |
| T | ID | B | 15 | 0 | 7/15 |
| T | ID | G | 16 | 0 | 6/16 |
| T | N | B | 16 | 2 | 0/16 |
| T | N | G | 16 | 2 | 0/16 |
| T | R | B | 16 | 7 | 0/16 |
| T | R | G | 16 | 7 | 0/16 |
| T | RD | B | 16 | 4 | 7/16 |
| T | RD | G | 16 | 4 | 3/16 |

### Complete exploratory policy contrasts

Differences are guard minus baseline. Category contrasts retain all attempts; marker contrasts retain valid pairs only. Baseline-only and guard-only refer to the named metric, so a marker-only count is not a correct-answer count. Separate Holm families cover 12 category and six marker tests. All are secondary post-generation analyses; independent scenario assumptions may fail under shared templates. These tests do not assess the full context-by-script interaction.

**All 18 new paired policy comparisons, with separate multiplicity families by metric.**

| Q | C | Metric | n | B only | G only | Delta pp | Exact p | Holm p |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E | N | Category | 16 | 0 | 1 | +6.2 | 1.00000 | 1.00 |
| E | R | Category | 16 | 0 | 2 | +12.5 | 0.50000 | 1.00 |
| E | RD | Category | 16 | 2 | 1 | -6.2 | 1.00000 | 1.00 |
| E | RD | Marker | 12 | 4 | 1 | -25.0 | 0.37500 | 1.00 |
| E | ID | Category | 16 | 0 | 1 | +6.2 | 1.00000 | 1.00 |
| E | ID | Marker | 9 | 1 | 3 | +22.2 | 0.62500 | 1.00 |
| T | N | Category | 16 | 0 | 0 | +0.0 | 1.00000 | 1.00 |
| T | R | Category | 16 | 0 | 0 | +0.0 | 1.00000 | 1.00 |
| T | RD | Category | 16 | 1 | 1 | +0.0 | 1.00000 | 1.00 |
| T | RD | Marker | 16 | 5 | 1 | -25.0 | 0.21875 | 1.00 |
| T | ID | Category | 16 | 0 | 0 | +0.0 | 1.00000 | 1.00 |
| T | ID | Marker | 15 | 3 | 2 | -6.7 | 1.00000 | 1.00 |
| K | N | Category | 16 | 0 | 0 | +0.0 | 1.00000 | 1.00 |
| K | R | Category | 16 | 4 | 0 | -25.0 | 0.12500 | 1.00 |
| K | RD | Category | 16 | 0 | 1 | +6.2 | 1.00000 | 1.00 |
| K | RD | Marker | 7 | 0 | 1 | +14.3 | 1.00000 | 1.00 |
| K | ID | Category | 16 | 0 | 0 | +0.0 | 1.00000 | 1.00 |
| K | ID | Marker | 7 | 1 | 0 | -14.3 | 1.00000 | 1.00 |

## Appendix: robustness, provenance, and unresolved validation

### Missing-output identification bounds

For each source-detail condition and policy, let n be 16 attempts, v valid outputs, and e valid outputs with a literal marker. The all-attempt marker fraction lies between e/n and (e+n-v)/n if each missing outcome is permitted either value. Subtract the baseline upper bound from the guard lower bound for the difference's lower bound, and the baseline lower bound from the guard upper bound for its upper bound. Valid outcomes remain fixed; invalid outputs are unknown rather than coded marker-free. The bounds describe an unobserved complete-output marker outcome, not a longer-budget model run, latent comprehension, or expert fidelity. They assume no distribution for missing outcomes and do not supply confidence intervals. A bound excluding zero remains a finite-sample descriptive observation subject to sampling uncertainty.

**Literal-marker difference bounds over all 16 attempts per policy. Valid-output echo fractions are descriptive; bounds permit either outcome for every missing observation. Codes follow Appendix C.**

| Query | Context | Echo B / valid | Echo G / valid | Difference bound pp |
| --- | --- | --- | --- | --- |
| E | RD | 11/16 | 5/12 | [-37.50, -12.50] |
| E | ID | 2/15 | 3/10 | [+0.00, +43.75] |
| T | RD | 7/16 | 3/16 | [-25.00, -25.00] |
| T | ID | 7/15 | 6/16 | [-12.50, -6.25] |
| K | RD | 1/9 | 2/9 | [-37.50, +50.00] |
| K | ID | 1/7 | 1/11 | [-56.25, +31.25] |

### Scenario leverage and lexical dependence

The artifact reports all 12 category-policy contrasts after omitting each of 16 scenarios and each of eight categories. Every retained attempt keeps the failure-as-error scoring rule; omission is a leverage diagnostic, not a new hypothesis test. Category strata are not authoring-template labels. Repeated conditions and script variants are never counted as independent scenarios.

For the archived Llama3 full-priming retrieval contrast, lowercased English glosses are tokenized to sets of letter-only words. An undirected edge joins cases whose token-set Jaccard similarity meets a threshold; connected components form deterministic stress-test groups. We report all five post-hoc thresholds, 0.3, 0.4, 0.5, 0.7, and 1.0. Transitivity can merge unlike endpoints, and low lexical overlap does not exclude shared semantic templates. These groups are not linguistic validation or recovered authoring provenance.

**Post-hoc lexical grouping of the 60 archived scenarios: Llama3 retrieval minus no retrieval under full Kannada-script priming. Groups are stress tests, not validated templates.**

| Threshold | Groups | Largest | Group-weighted pp | Omission range pp |
| --- | --- | --- | --- | --- |
| 0.3 | 54 | 3 | -37.04 | [-38.98, -34.48] |
| 0.4 | 59 | 2 | -37.29 | [-38.98, -35.59] |
| 0.5 | 60 | 1 | -36.67 | [-38.98, -35.59] |
| 0.7 | 60 | 1 | -36.67 | [-38.98, -35.59] |
| 1.0 | 60 | 1 | -36.67 | [-38.98, -35.59] |

Group-weighted differences give each component equal weight after averaging its scenario differences. Omission ranges remove one component and retain scenario weights in the remainder. The difference stays negative under these particular perturbations; that does not establish template independence, a population effect, or a valid cluster-based p-value. No confirmatory inference is added by these post-hoc diagnostics.

### Provenance and unresolved evidence

The corpus inventory retains a file hash and record count without redistributing court text, names, or case narratives. Extraction fidelity, redaction adequacy, and redistribution rights remain unverified; the inventory is not a rights clearance. The new local experiment uses synthetic English contexts rather than this corpus. Pinned model metadata and raw responses support auditing the local run, while undocumented historical configurations remain unreconstructed.

Neither the 60 authored cases nor the selected 16 represent participant samples. Speaker demographics, dialect, literacy, and service experience were not collected and cannot be inferred from category balance or script coverage. Independent reviewers have not established translation equivalence, complaint support, acceptable labels, or valid routes. Consequently, this paper makes a methodological proposal with exploratory diagnostics, not a validated multilingual instrument, demographic fairness evaluation, or deployment recommendation. Addressing these remaining gaps requires additional evidence rather than relabeling automatic checks as expert review.

## Appendix: proposed interface and institutional repair record

### Interface separation and review actions

The following wireframe specifies three distinguishable regions. Text labels and reading order should preserve their separation without relying on color. A translated gloss is a separate version with a reviewer status, not a silent replacement of the original account. The layout is a constructed design proposal, not a usability-tested interface or an implementation used in the study.

**Proposed intake interface: three regions with distinct evidentiary roles. This is a specification, not a tested system.**

| Original account | Model interpretation | External legal context |
| --- | --- | --- |
| Speaker text, original language, version, and separately labeled translations. | Proposed assertions with complaint-span links; unverified or unsupported status visible. | Source case or rule, document/version ID, and explicit other-person attribution. |
| Request correction or language assistance without editing the archived version. | Contested assertions hold consequential routing for staffed review. | Source relevance never supplies a missing personal fact; legal applicability requires separate review. |

A separate action region displays the proposed destination, review status, assigned correction owner, and pending tasks. Actions include request correction, ask for language support, and use the staffed alternative. Receipt or translation review must not be represented as agreement with every assertion. The speaker's confirmation of intended meaning is not verification of disputed events or legal eligibility. A model's self-assigned confidence cannot release a held route.

### Event record and closure conditions

Each correction event has a case identifier, original-account version, assertion identifier, evidence-span pointers, external-source identifiers, support status, contested content tags, assigned owner, event time, review disposition, corrected version, destination receipts, and unresolved status. Public evaluation artifacts should contain only justified deidentified records; operational records require access control and a retention policy. The editable template keeps observed events and outcomes null because none were collected here.

The transition sequence is captured, pending review, meaning reviewed, route reviewed, correction propagated, and receipt verified. An unresolved interpretation or missing receipt prevents successful closure. A service records who bears translation, delay, and repeated-explanation costs. It must define staffing and escalation rules locally rather than deriving a service deadline from this manuscript. Empirical evaluation should test whether people can distinguish the regions, locate an unsupported addition, contest it in their language, and obtain a propagated correction. No such completion rates, staffing costs, or user outcomes are claimed.
