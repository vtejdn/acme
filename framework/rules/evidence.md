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
Choose independent inspection for an actual [independent-review obligation](proof-audits.md#independent-review-obligations) or a useful review purpose under the [review-arrangement rule](proof-audits.md#review-arrangements).
Reviewer availability alone creates no preference for independence, isolation or delegation.
Disclose the actual review relationship and scope, including self-review, and retain any unmet independent-review obligation.
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
Follow the [finding-level review rule](proof-audits.md#finding-level-review-relationships) for actual relationship declarations, exact inputs and bindings, and new-adoption requirements; the [material format](../material-format.md#finding-level-review-relationships) owns field syntax.
The [review-arrangement and independence rules](proof-audits.md#review-arrangements) govern actual agent relationships and required independent coverage; a consumer label or physical version establishes neither.
For a repaired finding, follow the [rolling R repair rule](proof-audits.md#rolling-review-repair) for necessary rechecking and historical consumers, without requiring a new R container, rewriting an earlier relationship or claiming that old evidence covered later repairs.
