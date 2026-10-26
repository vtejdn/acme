# Claim Records and Proof Versions

Choose the statement, responsible home, substantive revision and applicable review from actual mathematics under the [agent/tool responsibility](workflow.md#agent-and-tool-responsibilities).
Optional writers/checks handle supplied fields and locators; they do not decide mathematical sameness or completeness.

<a id="record-kinds"></a>
## Ledger Record Kinds and Ownership

| Record kind | What it owns | Organization |
| --- | --- | --- |
| Claim | Exact statement, assessment history and selected argument/review | One numbered C family, with precise mathematical anchors |
| Claim argument | Actual fixed reasoning, hypotheses and dependency interfaces | The same or another applicable fixed C material; no empty redirect to a proof left in L |
| Exploration or synthesis material | Useful attempts, comparisons, synthesis, failures and limitations | Fixed L; formal project review findings belong to R |
| Formal project review | Actual agent inspection of fixed mathematical inputs, with its relationship, scope, findings and limits | Fixed R for self-review, independent review and retained unknown relationships |
| Research operation | Mathematical reason, actual authorization when needed, extraction ancestry, before/after scope and outcome | A dated section at the responsible mathematical home; no separate operation-ID namespace |
| Exploration or checkpoint | Continuing attempts, provisional obligations and useful failed findings | Rolling D while continuing; preserve consequential findings at a fixed mathematical home |

Record kind describes function, separately from a Claim's optional `role` of lemma, theorem or corollary.
A material may contain clearly named sections with related functions.
Its path/header identifies authorship and its main heading names the mathematics.
Preserve actual dates, goal/Claim links and the location owning the selected assessment; do not create a side registry merely to classify text.

Use the numbered material paths in the [material format](../material-format.md), with physical `_vN` for fixed C/L and working paths for rolling D.
Retire D only after retaining its useful content in the responsible fixed home and moving actual consumers; its address may then be reused without inheriting earlier scope or authority.
Preserve old anchors and incoming references during a real move.
A mathematical operation is identified by its responsible section and date, without another Claim identity merely for recording the operation.

The operation section explains what changed and why; C supplies the substantial argument; R findings own actual formal checking; the C decision owns adoption, mathematical status and exact evidence.
Keep shared version maps at their responsible mathematical home and link them from affected decisions.
Do not duplicate full proofs or reviews in an operation log or let historical prose compete with the explicit Current assessment.

For each Claim, its explicit Current assessment selects an exact decision and the proof/review relations that decision adopts.
Later choices preserve older decisions and maps at their actual dates.
A filename, edit date or completed operation does not select the proof.
Role, mathematical status, finding relationships and operation outcome remain distinct.

<a id="claim-registration"></a>
## Claim Registration and Cross-References

First apply the [common content decision](records.md#substantive-material-retention) to the actual statement, argument and existing homes, including direct C creation.
Required candidate registration is not waived because related mathematics is already recorded; a process-only draft must not become an empty C.
Then apply the [exploration, registration and acceptance distinctions](workflow.md#work-obligations).
An exploratory question, temporary hypothesis or trial calculation does not require a Claim ID merely to proceed.
Register a precise conjecture or obligation when it needs a responsible material, and a substantive project statement when it is organized for reuse.
A completed proof or review is not a registration prerequisite: an important unresolved statement uses `open`, retaining its candidate argument, partial results and exact gaps.
Once registered, the ordinary material, dependency and version rules apply; exploratory use does not permit silent changes to fixed mathematical decisions or support.

- Complete the exact statement, initial decision and actual author header before registering the Claim; an open Claim needs no invented proof.
  The optional `python scripts/material.py create --kind C --line F --file claim.md` writer, or `--task PATH` inheriting only a selected Task's line, allocates the next author/origin/C/line number and returns its canonical path.
- Keep the statement, decision history and Current assessment in that C family.
  C/T JSON records and snapshots are not created.
  Derive navigation from those choices when the view is needed.
  Identity is independent of theorem numbering, priority and route.
- Coordinate concurrent allocation and preserve all allocated identities, including refuted/historical Claims.
  The optional writer provides exclusive allocation; examples reserve no numbers.
- Keep the family for a proof repair of the same statement; a materially different statement gets its appropriate new identity and relation to the original.
  Preserve correction history and incoming links.
- Task and route paths use their separate T and S counters.
  Source units retain citation-key identities such as Miy22-U001 and canonical fixed U files.
  Definitions retain their own rules and do not automatically become Claims.
- Direct source reuse, notation conversion and parameter substitution need no automatic project Claim.
  Register a substantive reusable local deduction when appropriate, with exact source/application scope.
  Apply [reuse before proof](knowledge-reuse.md#reuse-before-proof); an established external result need not have its original proof reconstructed.

<a id="claim-role"></a>
## Optional Claim Role

An authoritative claim record may include `role` of `lemma`, `theorem`, or `corollary` in its decision field table to describe its mathematical or expository use.
Omission leaves it an ordinary claim; it does not indicate an open or less reliable result.
Role is independent of provenance, mathematical status, review relationships, priority and Claim ID.
A role change alone does not allocate a new ID or promote a result to `proved`.

Adding, changing or removing only this role inherits the actual previously selected assessment; it does not re-adopt its proof.
Keep mathematical status, all statement/argument/review relations, support/dependencies and their exact resolved paths, physical versions, anchors and declared scopes unchanged.
Relation row order is immaterial.
A new decision date and necessary role reason/authority may record this organization.
The agent judges that the actual edit is only organizational; tools compare these declarations, retain ordinary reference/enum/stale-selection checks and require no retrospective Review bindings or new mathematical version.
Preserve historical unknown or omitted review facts without upgrading them.
Changed assessments or substantive inputs retain their normal acceptance obligations.

The user may specify a role, or an agent may select or propose one under the [result-organization policy](#lemma-extraction-and-approval).
That policy permits internal organization and retains the main-theorem/objective authorization boundary; an optional role field does not create an approval requirement for every Claim or intermediate deduction.
Apply the same action boundary to designations in titles and manuscripts.
Existing historical labels and faithful references to already designated results do not require retroactive approval.
Existing records need not be relabeled in bulk.

Keep the authoritative role in the selected Claim decision, with its justification and any required authorization linked from the mathematical record.
For a protected designation, record whether it was agent-proposed or user-specified and the applicable authorization; approving an agent proposal does not change its origin.
The Claim index may display or link the Role field when useful.
Lemmas use the existing C namespace; source units retain their separate citation-key namespace.

<a id="separate-assessment-fields"></a>
## Mathematical Assessment and Review Findings

Provenance describes origin, not validity: use `project deduction`, `source specialization`, or `mixed`, with explicit source and project-input links.
Do not infer novelty from this field.

| Mathematical status | Meaning |
| --- | --- |
| `open` | An important precise statement is unresolved; partial results, reductions or a candidate argument can exist without satisfying the complete proved/refuted conditions. |
| `proved` | A complete argument covers every hypothesis, quantifier and conclusion of the exact selected statement, its dependencies are resolved, and a recorded internal mathematical review found no remaining gap. This is project-level assessment. |
| `refuted` | A checked counterexample or argument disproves the exact registered statement in its stated scope, with resolved necessary dependencies and completed applicable internal review. |

An open Claim may have no argument relation: the selected statement does not imply a proof.
A restricted statement can be proved in full while a broader question remains unresolved: proving the assertion for every integer with `1 <= n <= 10` does not prove it for every positive integer.
Preserve the broader Claim's truthful assessment and retain the narrower result at an adequate responsible home; materially different statements follow the ordinary family/version rules.
A hypothesis stated in the exact theorem belongs to its scope and does not itself make the theorem unresolved.
If only H implies Q is established and a necessary H remains unresolved, the Claim stating Q stays open.
An independently useful implication H implies Q can have its own precise C statement and sufficient proof/review without establishing H or Q.
Register an unresolved H separately only when it merits an important stable statement.
Agents judge statement coverage and applicability; an enum check or status label alone cannot discharge a dependency.
Supply the actual status explicitly in its decision.
Proved or refuted judgments select complete actual reasoning in fixed C with precise scope.
Do not leave the necessary Claim argument in L behind an empty C redirect or relabel it as support/dependency.
A statement and argument may share a file only when the argument is explicitly selected.
An open Claim can retain partial work or a formulation review without implying a completed proof.
Intake preserves this distinction instead of fabricating support.

Current local C decisions have no aggregate `review-status` field or inferred review grade.
Each selected R finding owns its actual `self-reviewed`, `independently reviewed` or genuinely unestablished historical/source `unknown` relationship, exact reviewed inputs, scope, findings and limits.
An absent declaration differs from an explicit unknown relationship; no selected review means only that this decision selects no review evidence.
An unfinished check or negative finding remains at its responsible account, independently of the reviewer's relationship.
Describe the actual agent arrangement and isolated mathematical context under the [review rules](proof-audits.md#review-arrangements); human authorship or advice is not a framework review.

Use `proved` only with a completed self-review or independent review and no unresolved mathematical dependency.
A review can correctly find an unresolved premise, incomplete argument or refutation; its relationship label supplies no mathematical promotion.
A refutation also requires checked evidence.
External review, formal verification, and publication are additional facts linked from the relevant Claim, audit or manuscript records; they are not implied by these labels.

An [accepted external theorem](literature-audits.md#accepted-external-inputs) can count as a resolved dependency when its exact source statement, hypotheses, and applicability have been checked and no concrete objection affecting its use remains.
Record the acceptance and actual source-proof inspection depth; an accepted applicable external theorem can resolve the dependency without re-auditing its entire source proof.
Unchecked applicability, unsupported inputs, unresolved objections, and unproved adaptations remain mathematical obligations.
This distinction does not waive review of the project's own argument or imply formal verification.

The descriptive label `Checked proof` corresponds to `proved` with recorded review evidence.
`Computational observation` remains evidence, not an automatic promotion to `proved`; an exact finite statement may be established only within the scope of its checked certificate and mathematical reduction.
`Source-verified result` records source inspection and is managed at the source-unit level, without implying an independently checked source proof.

Retain actual past `proof draft`, `conditional` and aggregate-review fields as historical/source facts; new local decisions and explicit reselection use the three states without the retired field.
Removing only that field from a current local decision is routine maintenance when the mathematical assessment and all selected relations/scopes stay unchanged; preserve any necessary factual objection or limitation at its actual home first.
No new mathematical version, administrative decision or retrospective binding is needed solely for that removal.
When an open conjecture is refuted, retain its original fixed statement and refuted result instead of replacing it with a negation or weaker conjecture.

## Dependencies and Corrections

Distinguish the following relations in the authoritative record:

| Relation | Required content and meaning |
| --- | --- |
| Proof dependencies | For the identified proof version, list the direct input Claim IDs and source-unit IDs, or precise source citations if no unit exists. State the exact conclusion used, where it is applied and how its hypotheses hold; identify the supporting proof version when needed to reconstruct the chain. These are the logical dependency edges. |
| Source attribution for known results | Cite the checked source and exact matching statement even when the current proof establishes that result in full. State that the citation identifies an established result rather than supplying an unproved premise. If the argument invokes the theorem or imports its proof, also record the actual reliance under proof dependencies. A locally written proof does not establish novelty or remove attribution obligations. |
| Definition uses | Link the precise definitions adopted in the statement or identified proof version; distinguish comparison-only mentions. Keep the actual parameter choices and application hypotheses with the claim. These forward references supply the definition index's consumer links; they are not theorem dependencies. Any invoked equivalence or well-definedness result also belongs in the proof dependencies as an accepted source input or project Claim, as appropriate. |
| Extraction provenance | Identify the original claim, complete proof version or artifact, and exact sections from which a lemma or reorganized argument was extracted. This records origin and is not by itself a logical dependency. |
| Mathematical or expository relationships | Record specializations, corollary relationships and comparisons separately. If a proof actually invokes the parent theorem, also record that use as a proof dependency; the relationship label alone is not sufficient. |
| Review evidence | Link reviews to the versions and interfaces they actually inspected. A review link is evidence about a proof, not an additional mathematical premise. |

An extracted lemma must state its own assumptions and actual inputs.
For example, a lemma may originate in a claim's original complete proof while the claim's new proof uses that lemma.
Do not create a reverse dependency on the parent claim's conclusion merely to record that origin.
If the lemma really uses that conclusion, it cannot also supply a circular proof of it.

Keep dependencies separate for current, candidate, historical and alternative proof versions under the [proof-version rules](#proof-versions).
Do not merge all historical citations into one apparent current dependency graph.
Check a complete, well-founded choice of supporting proof versions; switching between alternatives must not conceal a cycle.
In the Claim index, identify the proof version or live version map supporting the current assessment; link other versions from the responsible proof/version record.
Mark unresolved inputs explicitly.
A source's bibliographic registration alone does not verify a theorem used from it.

Apply the [known-result source check](knowledge-reuse.md#recognized-known-results) when identifying an established theorem within a proof.
Record pending attribution separately from mathematical obligations: a missing reference does not invalidate an independently checked complete local proof, while an unsupported theorem invocation remains an unresolved proof dependency.
Resolve or retain the attribution follow-up explicitly; do not invent a dependency edge merely to track a citation.

Before promotion, check the transitive dependency chain for open obligations, incompatible assumptions, and circular reasoning.
The recorded boundaries of accepted external theorems need not be expanded into recursive audits of their original proofs unless a relevant objection or the task requires it.
When an input changes or fails, find its direct and indirect consumers, flag their review status, and inspect the affected implications.
Retain `proved` only if a recorded unaffected or adequately reviewed repaired argument still supports it; otherwise select open or refuted according to the actual exact statement and evidence.
Do not mechanically equate failure of one proof with falsity of its conclusion.

Update the responsible argument/review evidence first, then the affected material decisions, selections and dependencies, with actual Task/route consequences.
Substantive fixed mathematics gets a new physical version; unchanged-mathematics choices append a decision.
Check affected material/relationships and derive needed [Claim](../../mathematics/claims/index.md), Task or strategy navigation, optionally using `scripts/render-research-navigation.py` after the relevant batch settles.
Never change status by editing a generated row.
Retain earlier assessments and the reason for each change in their responsible materials; the stable mathematics entrance needs no progress refresh.

Use the ledger's [substantive mathematical-operation rules](ledger.md#substantive-mathematical-operations) to record the mathematical reason, before/after scope and consequences of a claim or proof change.
Link a shared operation/version record when several claims are affected; keep actual proof dependencies in their identified proof artifacts.
Registration, role assignment or proof selection is not complete merely because a summary row was edited.
Routine index maintenance that changes no mathematics needs no separate operation record.

<a id="lemma-extraction-and-approval"></a>
## Internal Claim Organization and Theorem Designation

Within an assigned Task, extraction, decomposition, Claim registration and proof/dependency reorganization are ordinary autonomous research work.
No separate extraction approval or explicit lemma Role is required.
Use ordinary mathematical titles and Claim identities: retain the ID for an unchanged statement, allocate appropriate IDs for genuinely different statements, and preserve the original obligation and relationships when splitting it.
Do not weaken the Task target or erase useful original arguments.

Organizational authority does not certify mathematics.
Record precise hypotheses, conclusions, actual dependencies and unresolved gaps; avoid circular reasoning.
Candidate arguments may proceed before acceptance.
Selecting reviewed support requires the applicable mathematical review of the argument and changed interfaces.
Preserve historical designations, original proofs and reviews at their actual scopes.

Main-theorem designation and changes to the assigned objective require their actual human authorization.
Use existing applicable instructions; ask only for uncovered scope, with a concrete proposal.
Internal extraction does not itself select a manuscript's main theorem.
No separate approval registry or per-Claim report is required.

For reuse, give a concise usable conclusion, hypotheses and material limitations in the Claim summary and link the Claim from its consuming argument or route.
Consult existing navigation and targeted searches before repeating an argument.
Add a method entry only for reusable methodological content, not every subresult.

<a id="proof-versions"></a>
## Original and Lemma-Based Proof Versions

Locator-only key/unit renaming follows [material maintenance](records.md#authoritative-files) and [coordinated literature renaming](literature.md#coordinated-key-renaming); repair affected references while preserving actual selected mathematics, original provenance and review findings.

Preserve the original complete proof when introducing a lemma-based version.
Give each version a stable label or anchor, date and exact artifact reference, its own dependency list and review links, and an explicit disposition such as current, candidate, historical or alternative.
Link both versions from the authoritative claim record.
These proof labels are local to the claim and are not new Claim IDs or mathematical-status values.

For a substantive mathematical rewrite, preserve the original fixed material and its argument, dependencies and review scope, and create the next appropriate physical version.
A different proof within the unchanged Claim stays in the same family.
Keep meaningful failed and alternative versions available even without a current consumer.
Meaning-preserving maintenance follows the separate in-place rule; byte changes alone do not create a new review obligation.

The new version states which lemmas replace which original steps and verifies every hypothesis interface.
Scope changes or strengthened extracted statements require their own justification; an older full-proof review does not automatically cover them.
Do not cite the parent's conclusion to prove a lemma that is then used to establish that conclusion.
Historical provenance and logical dependencies follow the [separate relation rules](#dependencies-and-corrections).

Until the new version and its assembly have passed the applicable review, retain the old reviewed proof as the support for the unchanged claim's assessment and mark the new version as a candidate.
After review, explicitly select the current proof and select its exact evidence in the responsible Claim decision; the original remains available as historical or alternative support.
A rejected reorganization does not invalidate an unaffected original proof.
If a review discovers a defect shared by the original argument, reassess every affected version and downstream use under the ordinary correction rules.

## Record Template

Use the inert [record template](../templates/mathematics/claim.md), replacing placeholders with actual evidence.
A template is neither authorization nor a completed record.

For partial ACME intake, the executing agent must examine necessary dependencies against the actual statement, argument and review scope.
Collection alone preserves the imported C's original selected decision, visibly attributed as a source assessment, while actual acquired scope and unavailable selected inputs remain in intake provenance/navigation.
Do not change the source status, append a receiving decision or invent a local consumer, duplicate C or assessment overlay.
An unmapped background reference is not automatically an indispensable missing premise.
When a real local consumer has an indispensable unsupported premise, state that limitation there; its exact unresolved Claim stays open without accepting an unconditional proved/refuted conclusion from unsupported input.
Do not relabel the source result or manufacture a narrower conditional theorem solely because an input was not acquired.
Explain adequate verified background or independent support in the consumer's existing dependency scope, following the [intake rules](intake.md); this is no new proof review or approval.

## Revised proofs and review continuity

A complete revised proof with resolved dependencies and an adequate actual agent self-review may support `proved`, with that finding's relationship recorded in R.
Publish the new fixed mathematical argument and exact finding bindings; an old independent review does not transfer to changed inputs.
Changing a review label alone supplies no independent inspection.
Later independent adoption selects the actual separately organized finding without requiring another mathematical version merely for that review.
Key proof points and the full logical chain after Task completion require separately organized independent review through the existing Task workflow; this is not a per-Claim approval gate.

## Claim navigation

The existing renderer derives mathematics/claims/index.md from the fixed C families and explicit selected decisions: identity/title, selected assessment and exact argument/evidence locators.
C owns every assessment and relation.
The same index shows each selected finding's own declared relationship, exact input and authored scope separately; it infers no aggregate review level or proof verdict from them.
The responsible publishing agent refreshes after relevant material changes; do not hand-edit generated rows.

Fixing a result requires its complete argument or counterexample, actual source/compute inputs and truthful review relationship at the selected scope.
Reuse applicable checked evidence; a new commit does not itself create new review obligations.
A changed proof or uncovered use requires the relevant additional review.
After an independent review identifies a gap and the proof is repaired, a separate context-isolated agent must independently review the correction and affected logical chain again.
The repairer's self-check does not discharge that obligation, and a reviewer who contributes the repair cannot independently review that contribution.
