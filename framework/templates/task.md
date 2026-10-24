# Task

## Task Material Template

This is an inert mathematical Task template, not an assignment or permission to run research.
Use a numbered T family in `mathematics/tasks/` and the [material format](../material-format.md).
Source-only audits and operational setup retain their own homes instead of becoming artificial mathematical Tasks.
Use series A for an unspecified new Task; keep a continuing Task's series or the human's explicit choice.
New family allocation maintains its actual [`material_next` namespace](../material-format.md#material-family-allocation-state); a new physical contract version stays in that family.

Replace the author, date, question and authority with actual information.
For a new decision, replace the illustrative date with its actual UTC minute timestamp under the [new-record timestamp rule](../rules/workflow.md#new-record-timestamps).
A year, month or date alone, a value with `Z`, a numeric offset, seconds or fractions is invalid for a genuinely added decision; historical reading and existing-decision reselection retain genuinely known calendar precision.
A substantive contract change creates a new physical vN; an unchanged-contract lifecycle decision belongs in its current material, with the exact selected contract and evidence.

```markdown
---
author: Author
---
# Mathematical task title

## Contract
### Original question
Precise mathematical question, hypotheses, quantifiers and intended conclusion.

### Scope and exclusions
Objects and parameter ranges; separate questions outside this Task.

### Completion criteria
The proof, rigorous counterexample, classification or other mathematical result that resolves this exact question, and its required review.

## Current decision
[Selected decision](#decision-initial)

## Lifecycle and completion
### Decision initial
| Field | Value |
| --- | --- |
| date | 2026-10-18T01:30 |
| status | proposed |
| authority | Actual human instruction or attributed proposal, with its scope. |
| reason | Actual reason for proposing this mathematical question. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Contract](#contract) | Exact question, hypotheses and completion criteria above. |
```

The optional writer `python scripts/material.py create --kind T --file task.md` checks the supplied registered author and allocates the independent T counter.
The agent chooses the Task's contract, authority and lifecycle under the [common responsibility](../rules/workflow.md#agent-and-tool-responsibilities).
Use active only with actual assignment authority.
See the [write interface](../material-format.md#authoring-and-selecting-material) for revisions and decisions.
A genuinely new completed decision needs [review bindings](../material-format.md#review-bindings-for-new-accepted-decisions) for the actual contract and selected support/dependencies, and a matching explicit relationship row for every R finding it actually selects.
An omitted row differs from permitted historical/source `unknown`; an old review of different inputs cannot complete the Task.

Use precise links to relevant Claims, reviews and routes.
The route owns its Task associations and current route disposition; generated navigation supplies the Task's continuation entrance without a separate route-status list.
A Task with no route is valid.
Keep full arguments and counterexamples at their responsible mathematical homes, including meaningful earlier failures and reopening conditions.

Every ordinary local Task family has one stable current [E boundary](../rules/execution.md) in every lifecycle state; a joint coordination T has no E.
Setup prepares a minimal non-running E without execution authority or allowance.
The actual Task may include one unanchored operational link to execution/Author_E_F0001.md, outside mathematical support/review relations.
All physical versions share that address; completed Tasks retain their ended/non-running boundary.
Use ordinary prepared exact E edits for currently applicable conditions, without observations, events or history.
Task revision leaves E unchanged unless a separate applicable exact update is prepared, and never resumes a stop implicitly.
Apply actual human continuation authority and the responsible operator's [personal policy](../rules/preferences.md#scope-and-adoption) before research advancement.

For a joint contract, add the following task-level section outside the lifecycle history and explicitly retain it in every physical family version:

```markdown
## Task coordination

| Field | Value |
| --- | --- |
| task-type | joint |
```

For an ordinary individual participating in that common goal, use one exact adopted parent instead:

```markdown
## Task coordination

| Field | Value |
| --- | --- |
| joint-task | [Adopted common contract](Author_T_A0001_v1.md#contract) |
```

Replace the example parent with an actual joint T contract in this repository.
Keep the individual's own human authority, participation scope, extra constraints and completion criteria unambiguous.
Its strategies and stable E remain individual, and its parent link retains the adopted fixed version until explicitly revised under actual authority.
See [joint Tasks](../rules/tasks.md#joint-tasks-and-participation) for family type, one-layer validity, receiving and completion.
