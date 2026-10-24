# Claim

Before creating or retaining content with this template, apply the [common content decision](../rules/records.md#substantive-material-retention), reuse an adequate responsible home, and then follow this kind's actual registration, reproduction, source or review obligations.
A template does not justify a process-only record.

## Claim Material Template

Use one numbered main-material family in `mathematics/claims/` for each formal Claim, under the [material format](../material-format.md).
The local author and independent C counter identify the family.
Allocate a new family under the current [`material_next` state](../material-format.md#material-family-allocation-state), without reusing an issued number after retirement.
Inherit only the letter from an actual selected Task.
A mathematical revision creates the next physical vN; an assessment or review adoption with unchanged mathematics adds an explicit decision to the existing material.

This is an inert open-Claim example.
Replace the author, date and mathematical content with actual information.
For a new decision, replace the illustrative date with its actual UTC minute timestamp under the [new-record timestamp rule](../rules/workflow.md#new-record-timestamps).
Do not use year/month/date-only values, add `Z`, a numeric offset, seconds or fractions for a genuinely new decision.
Reading or reselecting an existing historical decision preserves genuinely known calendar precision instead of inventing a time.
An open Claim needs no invented proof, review or dependency.

```markdown
---
author: Author
---
# Precise mathematical claim title

Context: actual Task or authorized mathematical question, with precise links when available.

## Statement
Exact hypotheses, quantifiers, definitions and conclusion.

## Current assessment
[Selected decision](#decision-initial)

## Assessment history
### Decision initial
| Field | Value |
| --- | --- |
| date | 2026-10-18T01:30 |
| status | open |
| reason | Actual reason for retaining this statement and its unresolved obligation. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact statement and hypotheses above. |
```

The optional writer `python scripts/material.py create --kind C --line F --file claim.md`, or `--task` with an actual Task material path, allocates and returns a canonical path.
The author header names the actual registered human author under the [identity rules](../rules/identity.md#collaboration-maintenance-and-conflicts); the optional writer defaults to the bound human.
Choosing `--author` grants no other human's authorship or correction rights.
A different human records a correction in that human's own material with an exact reference.
The agent chooses the material and judges content/review under the [common responsibility](../rules/workflow.md#agent-and-tool-responsibilities); structural success creates no result or review.
See the [write interface](../material-format.md#authoring-and-selecting-material) for fixed revisions, appending decisions and deliberately selecting an older decision.

When an argument exists, retain its reconstructible derivation, actual dependencies and precise scope in this or another applicable fixed C.
Do not leave the required proof in L behind a redirect or a support/dependency label.
Add argument/support/dependency relations to the decision that actually adopts them; keep earlier proofless decisions unchanged.
Use `open`, `proved` or `refuted` for the exact selected statement; a candidate awaiting sufficient review or a target using an unresolved necessary premise remains open.
An independently useful implication or special case can be registered and assessed at its own precise scope.
New proved or refuted decisions select actual fixed R findings and exact statement/argument [review bindings](../material-format.md#review-bindings-for-new-accepted-decisions).
Every R finding actually selected for a genuinely new acceptance also has a matching explicit allowed relationship row; missing does not mean historical/source `unknown`.
Each R finding owns its actual agent relationship and scope; C has no aggregate `review-status` field and this declaration rule does not require every finding to be independent.
A linked review or PASS text alone does not supply acceptance.

An alternative proof by the same author stays within this Claim family.
A different author's fixed proof remains at its own location and can be adopted with its applicable review, without reattribution or a duplicate Claim.
Programs and native data stay in J groups.
Preserve equation identifiers and actual review scope when extracting a Claim from a shared module; a whole-module review does not become a new per-file review.

Keep definitions, source hypotheses, extraction ancestry and unresolved obligations in the relevant mathematical sections.
Extraction ancestry is distinct from proof dependencies.
Internal extraction under an existing assignment needs no additional approval.
Protected main-theorem designation or objective changes retain the actual required authorization under the [result-organization policy](../rules/claims.md#lemma-extraction-and-approval).

For a complete revised proof, select its new fixed argument and adequate actual agent self-review finding; use proved only with resolved dependencies and no remaining applicable mathematical issue.
Do not carry an older independent review onto changed inputs or promote a label without a separate inspection.
Track the key-point and Task full-chain independent review obligation through the owning Task.
After an independently identified gap is repaired, the corrected proof needs independent review by a separate isolated agent; the repairer's self-check does not fulfill that obligation.
