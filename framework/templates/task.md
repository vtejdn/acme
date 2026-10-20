# Task

## Task Material Template

This is an inert mathematical Task template, not an assignment or permission to run research.
Use a numbered T family in `mathematics/tasks/` and the [material format](../material-format.md).
Source-only audits and operational setup retain their own homes instead of becoming artificial mathematical Tasks.

Replace the author, date, question and authority with actual information.
For a new decision, replace the illustrative date with its actual offset-bearing minute timestamp under the [new-record timestamp rule](../rules/workflow.md#new-record-timestamps).
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
| date | 2026-10-18T09:30+08:00 |
| status | proposed |
| authority | Actual human instruction or attributed proposal, with its scope. |
| reason | Actual reason for proposing this mathematical question. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Contract](#contract) | Exact question, hypotheses and completion criteria above. |
```

The optional writer `python scripts/material.py create --kind T --line F --file task.md` checks the supplied registered author and allocates the independent T counter.
The agent chooses the Task's contract, authority and lifecycle under the [common responsibility](../rules/workflow.md#agent-and-tool-responsibilities).
Use active only with actual assignment authority.
See the [write interface](../material-format.md#authoring-and-selecting-material) for revisions and decisions.
A new completed decision needs [review bindings](../material-format.md#review-bindings-for-new-accepted-decisions) for the actual contract and selected support/dependencies; an old review of different inputs cannot complete them.

Use precise links to relevant Claims, reviews and routes.
The route owns its Task associations and current route disposition; generated navigation supplies the Task's continuation entrance without a separate route-status list.
A Task with no route is valid.
Keep full arguments and counterexamples at their responsible mathematical homes, including meaningful earlier failures and reopening conditions.

Every local Task family has one stable current [E boundary](../rules/execution.md) in every lifecycle state.
Setup prepares a minimal non-running E without execution authority or allowance.
The actual Task may include one unanchored operational link to execution/Author_E_F0001.md, outside mathematical support/review relations.
All physical versions share that address; completed Tasks retain their ended/non-running boundary.
Use ordinary prepared exact E edits for currently applicable conditions, without observations, events or history.
Task revision leaves E unchanged unless a separate applicable exact update is prepared, and never resumes a stop implicitly.
Apply actual human continuation authority and the responsible operator's [personal policy](../rules/preferences.md#scope-and-adoption) before research advancement.
