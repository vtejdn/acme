# Proof Audit

Before creating or retaining content with this template, apply the [common content decision](../rules/records.md#substantive-material-retention), reuse an adequate responsible home, and then follow this kind's actual registration, reproduction, source or review obligations.
A template does not justify a process-only record.

## Inline Audit Template

Use this structure in a numbered fixed R material for every independent project-review account.
A fixed L finding may use it only for actual self-review or an unknown checking relationship.
Partial, negative, unresolved and unadopted independent findings also belong to R; several findings may share an appropriate R.
The optional `material.py create --kind R --line F --file review.md` writer uses the real author and supplied evidence.
The reviewer judges actual coverage and applicability under the [common responsibility](../rules/workflow.md#agent-and-tool-responsibilities).
Expand only fields relevant to the argument while preserving necessary scope/evidence.
Follow the [review arrangements and disclosure rules](../rules/proof-audits.md#review-arrangements); no individual agent identity is required.
This template records the review; its field order does not prescribe when to read previous assessments.

```markdown
---
author: Author
---
# <Claim or goal> — <review scope>

- Date and human attribution: <timezone-bearing minute timestamp; record author and existing human attribution; known human reviewer where applicable>.
- Review arrangement: <actual human or agent review method; relationship to proof development; self-review or independent-review relationship and its basis; initial review or targeted recheck>.
- Inputs and sequence: <additional exploration notes, proof-generation dialogue, author explanations or earlier conclusions supplied or consulted before initial findings; when earlier findings were consulted; unknown conditions stated explicitly>.
- Verification and limits: <obligations and derivations actually rechecked; any prior review relied on and its scope; unchecked parts; details in the findings below>.
- Target and records: <exact Task/Claim material paths, physical versions, decision/statement/contract anchors and applicable route links>.
- Selected support: <statement, current proof artifacts and anchors, retained auxiliary material, direct dependencies with exact version references>.
- Review binding: <actual finding selected by the C/T decision; exact input paths/anchors and scope in the Review bindings table below; do not generate a review hash>.
- Artifact: <exact revision and sections reviewed>.
- Scope: <whole proof / named interfaces / supporting computation / completion>.
- Starting assessment: <mathematical status; review status; open conditions>.

## Review relationships
| Review | Relationship |
| --- | --- |
| [Finding](#outcome-and-follow-up) | unknown |

## Review bindings
| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#outcome-and-follow-up) | [Exact statement](../../claims/Author_C_F0001_v1.md#statement) | Actual hypotheses and conclusion inspected. |
| [Finding](#outcome-and-follow-up) | [Exact argument](../../claims/Author_C_F0001_v1.md#argument) | Actual argument and interface scope inspected. |

## Obligations and evidence

| Obligation | Proof/source evidence and decisive content | Required hypotheses and where supplied | Finding | Gap or corrective action |
| --- | --- | --- | --- | --- |

## Dependency and scope checks
<Backward obligations; forward construction; matched interfaces; absence of cycles;
original quantifiers and acceptance criteria; temporary restrictions and endpoints;
recognized known results, exact source matches, attribution versus proof reliance,
and any outstanding source corrections separately from mathematical gaps.>

## Verification facts and limits
<State relevant checks, decisive findings and material limitations.
Omit irrelevant categories; disclose unperformed checks only when they limit the supported conclusion.
Manuscript reviews use their document-local record under the manuscript rules, not this R template.>

## Outcome and follow-up
<Supported conclusion and remaining conditions; proposed mathematical/review status;
failed implications; affected downstream IDs; required correction or next action.>

## Revisions
<Dated corrections and superseded findings, with the revision rechecked.>
```

Replace the illustrative Claim rows with every actual required input.
For Task completion, bind the exact contract and each support/dependency.
Paths above assume an R under mathematics/audits/reviews/; rebase them for an L finding.
Include only the scope really reviewed; an unperformed check must not be implied by a template row.

Replace `unknown` only with the actual `self-reviewed` or `independently reviewed` relationship supported by the review account.
Classify each finding, not its consumer: complementary independent findings may cover an aggregate, and a self-reviewed aggregate does not reclassify its independently inspected parts.
