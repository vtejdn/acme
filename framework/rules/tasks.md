# Task Contracts and Lifecycle

## Task Records

Create a Task with its complete actual contract/decision, using the [Task template](../templates/task.md); the optional `material.py create --kind T --line F --file task.md` allocates its numbered T family under `mathematics/tasks/`.
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
The decision fields `review-status` and `role` belong only to Claims and are rejected in Task decisions.
Preserve concrete reviews, objections and their scopes in the responsible evidence; a gap alone does not make a Task blocked.
Claim review status and proof/refutation acceptance remain governed by the Claim rules.

A new Task states proposed or active explicitly in its initial decision.
Use active only for an actual assignment or existing exploration authorization, recorded in `authority` and `reason`.
An inert template and a proposed question do not grant execution permission.
Task creation starts no run and needs no fictitious setup review.

Tasks are not acquired material.
A source Task may locate useful C/R/U/L/J candidates, but neither the Task nor its execution authorization or completion is installed.
Actual local adoption and missing necessary inputs belong to the responsible mathematical consumer under the [intake rules](intake.md).

Change lifecycle with an explicit `### Decision key` block, optionally written through `material.py append-decision PATH --expect PATH#current --file decision.md`, or deliberately select an existing exact decision.
Every new Task decision records date, actual authority, meaningful reason and exact contract relation.
A paused or blocked decision explains its outstanding condition and resumption basis in its reason/responsible text.
Returning to active requires the actual applicable decision; elapsed time or a new agent session is insufficient.
Retirement preserves unfinished obligations; materially different targets receive an appropriate new Task.

An unchanged contract can retain its selected decision while ordinary meaningful history is added.
A completed Task with a substantive contract, supporting-selection or dependency change requires explicit reopening or a new applicable completion decision and review.
Harmless locator/layout maintenance retains its existing mathematics and completion scope.
Task reviews do not create an overall review-status label or manufacture a negative finding.

A completed decision selects its exact contract, actual fixed support/dependencies and an applicable fixed R/L review.
The review must explicitly bind the checked contract and every selected support/dependency using [Review bindings](../material-format.md#review-bindings-for-new-accepted-decisions).
An applicable fixed L self-review or unknown finding can supply its actual scope; independent findings belong only to fixed R.
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

The Task material owns its exact question, scope, completion criteria and authorization history.
Claim mathematical assessments stay with their selected C decisions; the [Claim index](../../mathematics/claims/index.md) derives their navigation.
Each S material owns its own route priority/disposition and Task association, with a derived [strategy index](../../mathematics/strategies/index.md).
Changes to target, quantifiers or criteria preserve the earlier contract and remain within actual human authorization.
A tractable special case must not silently replace the original question.

## Execution boundary

Every local Task family has one stable current E in every lifecycle state under the [execution rules](execution.md).
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

The existing renderer derives mathematics/tasks/index.md from fixed T families and selected decisions: identity/title, current contract/lifecycle and exact selected links.
T owns those facts.
The responsible publishing agent refreshes after relevant changes; agents never assign lifecycle through generated rows.

Round closeout checks the changed work and direct interfaces; fixing a result retains its exact mathematical/evidence scope.
Task completion instead checks the original contract and every completion criterion against the full support chain, reusing applicable accepted inputs and reviews.
Execution stop and Git delivery do not complete a Task.
