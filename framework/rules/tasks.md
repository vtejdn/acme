# Task Contracts and Lifecycle

## Task Records

Create a Task with its complete actual contract/decision, using the [Task template](../templates/task.md); the optional `material.py create --kind T --file task.md` allocates its numbered T family under `mathematics/tasks/`.
Use line A for a new Task when the human has not designated a series, without a routine question or topic-based letter inference.
Continuation keeps the existing series; Task-derived material inherits its letter while retaining the author/kind/line's independent counter.
An explicit line choice takes precedence, and an independent local material without a Task or line uses the same A fallback.
Apply the [agent/tool responsibility](workflow.md#agent-and-tool-responsibilities) to question, completion and authorization.
Source-only audits and setup operations keep their appropriate homes instead of becoming artificial mathematical Tasks.
Use current canonical identities in historical accounts as well as current instructions; preserve historical meaning through a verified current identity or precise descriptive mathematics, without retired identifiers or aliases.

Distinguish user-assigned tasks from agent proposals.
A proposed question is not an active objective until it falls within an existing exploration authorization or the user authorizes it.
Ordinary methodological choices within an active task do not require another approval.

The selected Task decision owns lifecycle, authority, reason and exact contract/evidence:

| Lifecycle (`status` in the decision) | Meaning |
| --- | --- |
| `proposed` | A registered question awaiting activation under applicable authorization. |
| `active` | An authorized, continuing research objective; an Agent need not be executing it at this moment. |
| `paused` | Deliberately suspended for now, with an intention and condition for resuming. |
| `blocked` | An identified obstacle prevents the next required progress; name the missing input or condition. An unsolved mathematical question alone does not establish a block. |
| `completed` | The recorded completion criteria are met, with a review covering the current contract. |
| `retired` | A decision to stop pursuing this Task. Preserve the reason and unfinished obligations; retirement does not assert a mathematical resolution. |

Tasks have no overall review status, Claim role or correction flag.
The optional `role` field belongs only to Claims and is rejected in Task decisions; neither C nor T has an aggregate current review-status.
Preserve concrete reviews, objections and their scopes in the responsible evidence; a gap alone does not make a Task blocked.
Claim review status and proof/refutation acceptance remain governed by the Claim rules.

A new Task states proposed or active explicitly in its initial decision.
Use active only for an actual assignment or existing exploration authorization, recorded in `authority` and `reason`.
An inert template and a proposed question do not grant execution permission.
Task creation starts no run and needs no fictitious setup review.

Own selected Tasks may be personally imported under their actual human, contract, lifecycle and still-effective execution conditions.
External intake may receive a necessary joint contract for continuing shared research; it receives no other human's ordinary Task/E authority or local completion verdict.
Actual adoption and missing necessary inputs remain at the responsible consumer under the [intake/import rules](intake.md).

Change lifecycle with an explicit `### Decision key` block, optionally written through `material.py append-decision PATH --expect PATH#current --file decision.md`, or deliberately select an existing exact decision.
Every new Task decision records date, actual authority, meaningful reason and exact contract relation.
A paused or blocked decision explains its outstanding condition and resumption basis in its reason/responsible text.
Returning to active requires the actual applicable decision; elapsed time or a new agent session is insufficient.
Retirement preserves unfinished obligations; materially different targets receive an appropriate new Task.

An unchanged contract can retain its selected decision while substantive findings or necessary current conditions are updated.
A completed Task with a substantive contract, supporting-selection or dependency change requires explicit reopening or a new applicable completion decision and review.
Harmless locator/layout maintenance retains its existing mathematics and completion scope.
Task reviews do not create an overall review-status label or manufacture a negative finding.

A new completed decision selects its exact contract, actual fixed support/dependencies and applicable fixed R findings.
The review must explicitly bind the checked contract and every selected support/dependency using [Review bindings](../material-format.md#review-bindings-for-new-accepted-decisions).
Necessary historical exact L review evidence stays readable at its actual scope; new/current formal local review use selects R.
R placement alone does not establish independence.
C/T decisions own adoption; review findings own the actual checks and limits.
Preserve earlier completion and noncompletion findings rather than replacing their scope.

The executing reviewer must compare the actual conclusion with all current completion criteria.
Failed, inconclusive, setup-only and narrower reviews cannot support completion.
Structural checks verify explicit input/target sets and resolvable locators, rather than semantic correspondence or review sufficiency; no successful outcome is inferred merely from a file or a missing label.
Preserve self-review versus independent review as facts of the actual review.
Separately organize independent review at key proof points and of the full logical chain after Task completion, using the existing assignment and review workflow; record the responsible review arrangement and unfinished obligation at the Task.
This does not impose independent approval on every intermediate Claim or block an accurately self-reviewed complete proof.
New completion always records a new decision and applicable evidence.
Removing Task review labels never resumes a stopped run.

The Task material owns its exact question, scope, completion criteria, selected lifecycle and applicable authority.
Authorization history may be shortened or removed under the [common content decision](records.md#substantive-material-retention), keeping the current selected decision, effective conditions and necessary contract/evidence references coherent.
Claim mathematical assessments stay with their selected C decisions; the [Claim index](../../mathematics/claims/index.md) derives their navigation.
Each S material owns its own route priority/disposition and Task association, with a derived [strategy index](../../mathematics/strategies/index.md).
Changes to target, quantifiers or criteria preserve the earlier contract and remain within actual human authorization.
A tractable special case must not silently replace the original question.

## Execution boundary

Every ordinary local Task family has one stable current E in every lifecycle state under the [execution rules](execution.md); a joint coordination T has no E.
Setup prepares its minimal non-running E together with the initial Task, granting no execution or allowance.
Each physical Task version may retain one unanchored operational link to that same family E outside mathematical support/review relations.
The current exact Task decision, execution state and still-effective conditions are maintained directly there, without events or replay history.
Task revision leaves E unchanged unless an applicable exact update is prepared; a new Task pointer, active lifecycle or session supplies no resumption authority.
Completed Tasks retain the same concise ended/non-running E, reused only under actual later authorization.
Mathematical consumers other than the permitted Task entrance do not refer to E or administrative records.

## Record Template

Use the inert [record template](../templates/task.md), replacing placeholders with actual evidence.
A template is neither authorization nor a completed record.

Before closing a task, use the [completion review procedure](proof-audits.md) to compare the achieved conclusion with the original question.
Independent open routes and stronger auxiliary questions do not automatically remain requirements after the task's own criteria are met.
Record completion and its evidence in the responsible Task and reviews, then update affected generated navigation.
The stable mathematics entrance has no same-commit completion edit or progress-refresh duty.

A source Task completion does not complete a recipient Task or authorize recipient execution.
Check the recipient contract against its actually obtained support and applicable reviews; preserve any missing necessary input explicitly.

## Task navigation

The [joint-Task rule](#joint-tasks-and-participation) supplies the coordination exception and derived participation view.

The existing renderer derives mathematics/tasks/index.md from fixed T families and selected decisions: identity/title, current contract/lifecycle and exact selected links.
T owns those facts.
The responsible publishing agent refreshes after relevant changes; agents never assign lifecycle through generated rows.

Round closeout checks the changed work and direct interfaces; fixing a result retains its exact mathematical/evidence scope.
Task completion instead checks the original contract and every completion criterion against the full support chain, reusing applicable accepted inputs and reviews.
Execution stop and Git delivery do not complete a Task.

## Joint Tasks and participation

A joint Task is a coordination use of the ordinary numbered T material with one actual human author and a complete common mathematical contract.
The [material format](../material-format.md#task-coordination) owns its optional Task coordination table: task-type joint on a joint T, or one exact joint-task contract link on an ordinary participating T.
Ordinary versus joint is invariant across the whole T family.
Every joint physical version explicitly retains task-type joint; omission, ordinary-to-joint and joint-to-ordinary revisions or imports are inconsistent and must be refused before publication or E changes.
Use a suitable new family when a different type is actually needed, preserving earlier contracts, consumers and effective E conditions.
An ordinary Task's adoption of a joint parent changes neither its type nor its stable E.
Support one layer: a joint T has no parent and no directly associated S; an individual T has at most one exact same-repository joint contract parent.
Reject self, duplicate, nested, cyclic, missing, wrong-kind and ordinary-parent targets.

The common T owns the full shared question, hypotheses, quantifiers, domains, scope, completion criteria and selected overall lifecycle/evidence.
Each collaborator's individual T states actual human authority, participation scope, additional constraints and personal completion criteria, referencing the adopted exact common contract without duplicating its full text.
An explicitly partial subgoal remains partial; alternative methods belong in that individual's S.
Reuse an adequate existing authorized T and its E rather than manufacturing another assignment.
Creating a joint T creates no participants' Tasks, E, budgets or execution permission.
Derived navigation reads individual forward parent links and existing S-to-T associations; maintain no editable member list or synchronized status ledger.

Before advancing one's individual Task, compare relevant collaborators' strategies, usable results and informative failures.
Choose different routes where useful to reduce repeated work; independent verification, replication and cross-checking may deliberately overlap.
No allocation ceremony or semantic novelty test is required.
Keep every proof, computation, review and correction under its actual single human author and reuse adequate local mathematics through references, without intake merely because its local author differs.

Continuing a joint goal selects the actual human's appropriate authorized individual T/E and reads its adopted common contract and still-effective conditions.
An actual request to establish and continue that participation supplies its scope without a second formal activation approval; an unresolved choice among several actual Tasks needs clarification.
Viewing a joint T, a common active label or another collaborator's work selects no run and transfers no authority.
Joint and individual lifecycle decisions do not automatically change one another or any E.
Complete the joint T only when the exact whole common contract is met by the actual mathematical support and applicable fixed reviews.
One sufficient route can resolve the goal; combined contributions require their actual hypotheses and interfaces to close the full chain.
Partial completions, child counts and mechanical success supply no common completion verdict or unanimous group-approval requirement.

A changed common contract creates the appropriate next physical T version and preserves earlier contracts.
Individual references retain their exact adopted physical version and contract anchor; a later common file does not redirect them.
Adopting changed obligations belongs to the individual's actual authorized revision/decision and applicable review.

When shared collaboration continues in the receiving repository, reuse an adequate exact local parent or receive the necessary parent with the selected individual Tasks.
An own-authored parent uses personal import; another human's parent uses intake, retaining its actual author/source facts and joint/no-E type without acquiring unselected participants.
When that collaboration is not continuing locally, prepare the individual's standalone contract with all adopted common hypotheses, quantifiers, goal, personal scope, criteria and outstanding obligations, preserving attribution and actual review applicability.
Remove the inapplicable joint-task link and repair references; obtain necessary other-author contract content through intake rather than reauthoring their proof or finding.
Neither disposition resets execution conditions, creates an allowance or fabricates a new decision from relocation.
