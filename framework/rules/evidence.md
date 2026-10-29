# Claims and Evidence

## Claims and Evidence

Label substantive claims so that their evidential status is visible.
Use the following distinctions, or equally explicit wording:

| Label | Meaning |
| --- | --- |
| Source-verified result | A statement checked in an identified source, with a precise locator and the relevant hypotheses. This does not imply that its proof has been independently checked. |
| Conjecture | A precise statement whose truth remains open in the current investigation. |
| Proof draft | A proposed argument awaiting review or containing explicitly identified gaps. |
| Checked proof | A complete argument whose recorded review found no unresolved gaps under the stated hypotheses. Record who or what performed the check and its scope; this is not a claim of formal verification. |
| Computational observation | Evidence from a specified computation, with its parameters and limitations. |
| Refuted claim | A statement contradicted by a verified counterexample or argument, with the evidence linked. |

An incomplete argument remains a proof draft even when experiments support its conclusion.
Reserve "formally verified" for claims actually checked by an identified proof assistant, with the artifact, environment, and successful check recorded.

For project claims, distinguish provenance, the three-state mathematical assessment and individual R finding relationships under the [Claim assessment rules](claims.md#separate-assessment-fields), without an aggregate review-status.
Human-specified [ordinary labels](claims.md#claim-role) in titles or prose describe use independently of these assessments, without a decision field or proof-adoption action.
Separate extraction provenance from actual proof dependencies, and preserve the original complete proof when introducing a new lemma-based proof under the [proof-version rules](claims.md#proof-versions).
These descriptive labels do not replace assessment fields.
In particular, a source-verified statement need not have an independently reviewed proof; a complete candidate awaiting sufficient review keeps the exact registered Claim open.

Before treating a new result as established in the research status, perform a separate review of its assumptions, dependencies, and proof.
Prefer an independent reviewer when available; otherwise disclose that the review was a self-review.
Every formal project review belongs to fixed R, whether self-review, independent review or a genuinely unknown older/source relationship; ordinary checks may stay with their argument or discussion.
Unchecked dependencies remain explicit conditions on downstream conclusions.

A complete substantively revised proof with resolved dependencies and an adequate actual agent self-review can support proved, with its relationship and scope in R.
Earlier independent review does not transfer to changed inputs, and changing a label supplies no new inspection.
Separately organized independent review is required at key mathematical points and for the full logical chain after Task completion; assign that work through the existing Task workflow and retain its actual scope and any pending obligation.
This does not require independent approval of every intermediate Claim.

For substantial multi-lemma results, use the [completion-audit procedure](proof-audits.md).
Work backward from the conclusion and forward through the construction, verify each hypothesis interface, rule out dependency cycles, and compare the final scope with the original task, including temporary restrictions and boundary cases.
Review findings and the achieved scope determine completion; a checklist of attempts or artifact builds does not.


### Finding-level review relationships

The R finding owns its actual agent checking relationship; the C/T decision owns adoption and mathematical/lifecycle assessment without an aggregate review-status.
Use a `Review relationships` table with columns `Review` and `Relationship`, linking each finding to its real local anchor.
Allowed relationships are `self-reviewed`, `independently reviewed` and genuinely unestablished historical/source `unknown`; an omitted row is a missing declaration, distinct from explicit unknown.
Explain the actual review arrangement and inspected scope in the finding's existing account.
Do not derive a finding's relationship from a consumer label or physical version.

Tools check the exact supplied binding coverage without deriving an aggregate independent level from C or mixed findings.
The agent determines mathematical sufficiency and actual required independent coverage under the [agent/context boundary](proof-audits.md#review-arrangements).
An isolated separate agent can read the fixed proof and dependencies directly but must not inherit proof-development discussion, summaries or prior verdicts.
After an independent finding identifies a gap and the proof is repaired, independent re-review of the correction and affected chain remains necessary; a repair contributor's self-check does not fulfill it.
A new C/T physical version cannot turn a retained self-review into independent evidence.
Unknown historical relationships remain unknown and old assessments remain historical;
supplement only evidence necessary for actual new adoption or required review.
Preserve known finding relationships and fixed scopes.
Corrections to a known finding use new review evidence, not a rewritten relationship.
This structural check does not certify mathematical correctness or require a new review registry.
