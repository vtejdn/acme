# Proof and Completion Audit Rules

The reviewer applies the [agent/tool responsibility](workflow.md#agent-and-tool-responsibilities) to actual independence, coverage and applicability.
Optional tools check declared input/target sets, relationship values and required locators; they do not infer equivalent prose or certify review sufficiency.

## Review Scope and Records

Before recording review evidence, apply the [common content decision](records.md#substantive-material-retention) and use an adequate existing finding when applicable.
An actually performed new review of fixed mathematics can add necessary evidence even when its theorem is already in C; assignments, completion announcements and structural checks are not mathematical reviews.
Apply the [work-obligation rules](workflow.md#work-obligations): the review requirements here govern evidence registered for a Claim assessment, acceptance of a result, selection of reviewed support or Task completion.
Local checks can occur at any point during exploration and may be recorded with the attempt under its Task, route or question.
They need not wait for Claim registration or completion of a whole proof review.
Describe what was actually checked and retain gaps; a local check alone does not certify an unchecked argument or change its canonical assessment.
When a review is registered or relied on for acceptance, provide the exact statement, support and review bindings below.

Use an actual numbered fixed R material, such as `mathematics/audits/reviews/Author_R_F0001_v1.md`, with the short author header and exact input locators.
A compact self-review or genuinely unknown-relationship finding can instead be a clearly named finding in existing fixed L material; link the actual finding from the adopting C/T decision.
Every independent project-review account belongs to fixed R, including partial, negative, unresolved and unadopted findings about Claims, computations or Task completion.
Several findings may share one appropriate R; a standalone local review needs no invented C.
U inspections and J checker programs/outputs retain their own homes, with R linking the evidence and owning the independent conclusion.
Review identity is separate from the inspected Claim or Task's number and physical version.

Identify the timezone-bearing minute timestamp, human record author, reviewer or review method, self-review or independent-review relationship, and exact artifact reviewed.
A commit and file/anchor are useful when available; otherwise identify the dated revision and relevant sections.
State whether the review covers the whole argument, a particular interface, source use, computations, or completion.
An audit of an older revision does not automatically cover later substantive changes.

Before acceptance identify the exact statement/contract, complete argument, selected support and direct dependencies, with path/version/anchor and actual applicability scope.
New accepted C decisions select a fixed R/L finding whose [Review bindings](../material-format.md#review-bindings-for-new-accepted-decisions) cover the precise statement and argument; completed T decisions require coverage of contract and all declared support/dependencies.
The C/T decision owns adoption, and the review owns its actual checks and limits.
A review file, PASS text or unrelated finding in the same file does not select acceptance.
Identify reviewed mathematics by canonical paths, physical versions, anchors and available source revisions; remove persistent mathematical digest records.
Structural coverage cannot certify mathematical sufficiency or discover every omitted dependency.

Review bindings and finding relationships use the shared [declaration boundary](../material-format.md#machine-readable-declarations).
Tables inside code, comments or HTML literal regions are explanatory examples; they supply neither coverage nor independence, even under a real section heading.
Genuine cells retain inline code, mathematical content and their exact visible scope.
No historical review needs retrospective table cleanup or backfilled evidence.

A [pure Claim role action](claims.md#claim-role) inherits its previously selected assessment without a fresh proof adoption.
Appending that organizational decision does not require historical bindings to be supplied or unknown relationships to be relabelled; an actual status or input change still needs its applicable review evidence.
Task completion retains its own requirements.

Use the selected Claim decision's actual review states: `unreviewed`, `under review`, `self-reviewed`, `independently reviewed`, or `changes required`.
Report mathematical status separately from review status and provenance.
A complete candidate awaiting review remains a `proof draft`; a `conditional` result must list its open assumptions.
Promotion to `proved` requires a complete argument, resolved dependencies, and recorded internal review.
Independent review is preferred when available, but self-review is permitted and must be disclosed.

Evaluate external dependencies under the [accepted-input rules](literature-audits.md#accepted-external-inputs).
An established theorem with its statement, hypotheses, and applicability checked may be a resolved input even if its original proof was not re-audited; record that boundary.
Unresolved source evidence, objections, applicability, and local adaptations remain obligations.
Review the project's own reasoning and the interfaces it uses without turning every accepted textbook input into a new proof-audit task.

<a id="review-arrangements"></a>
### Review Arrangements and Disclosure

Describe this review activity briefly in its audit or indexed review section.
Keep human attribution under the [identity rules](identity.md), and state the actual human or agent review method in prose.
The framework does not require individual agent IDs, session IDs, model registration or an additional reviewer registry.
Human attribution fields alone establish neither personal human inspection nor independence of an agent review.

- Arrangement: describe the relationship to proof development, such as self-checking within the original reasoning or a separately organized review, and whether the purpose is an initial whole-proof review or a targeted recheck.
- Inputs: state whether exploration notes, proof-generation dialogue, author explanations or previous review conclusions were supplied in the review context or consulted before the initial findings.
  Reading the proof under review is a necessary input, distinct from these additional materials.
  Mark unknown or unrecorded input conditions as such; do not infer that no context was shared.
- Verification: identify the obligations and derivations actually rechecked, the scope of any prior review relied on, and what remains unchecked.
  Point to the corresponding findings rather than duplicating the argument.

Different sessions or models alone do not establish independence.
Shared additional material does not by itself invalidate a review, but its use and limits must be disclosed.
An `independently reviewed` classification needs an account of a separately organized review and the reasoning actually examined; agreement or a role label is insufficient.
Self-review remains permitted.
These descriptions introduce no new review states, independence grades, or mandatory multiple-agent or multiple-model review.

Preserve historical reviews at their recorded scope without inventing missing input conditions.
This clarification alone requires neither rewriting their evidence nor a new mathematical review.
A concrete unsupported independence claim or mathematical objection still follows the ordinary correction process.

### Extracted Lemmas and Reorganized Proofs

Follow the [result-organization policy](claims.md#lemma-extraction-and-approval): internal extraction and proof/dependency organization within an assigned Task need no separate approval or lemma label.
Main-theorem designation and objective changes retain their actual authorization boundary.
Review candidate arguments at their actual scope; organization is not evidence of mathematical correctness.
Selecting reviewed support requires the applicable argument and interface checks.

Identify the original complete proof artifact, extracted lemma artifact, and new consumer proof version.
Check the lemma's precise assumptions and actual inputs, distinguish its extraction provenance from logical dependencies, and inspect each changed invocation.
Reconstruct the complete supporting chain using identified proof versions; do not turn historical or comparison links into dependency edges or permit a cycle through alternative proofs.
An unchanged extraction may cite the old review and add a scoped interface review, but any generalization or new argument requires review at its new scope.
A substantial reassembly still needs the end-to-end review below.

Record separate findings for the extracted lemma and the new assembled proof.
Preserve the old review with its exact scope.
An unreviewed or failed candidate proof does not remove an unchanged claim's existing reviewed support; a defect affecting that support must trigger the normal correction and downstream-review process.

For a [substantive mathematical operation](ledger.md#substantive-mathematical-operations), distinguish the research-operation record explaining the change from the actual proof artifact under review.
The audit owns its findings; the operation record links those findings and records their implemented mathematical consequences or unresolved effects.
Do not duplicate the full review in a ledger history or treat a completed operation log as proof acceptance.
A small change can retain its history in the affected claim's existing section.

## Inherited ACME Reviews

Approved compatible ACME intake may reuse an exact source review at its actual recorded scope.
Preserve source material/decision locators, original authorship and registered source correspondence, review arrangement, findings, historical attestations and inspection limits through every transfer.
Label reuse inherited rather than a new local independent review.
Acquisition and current local use remain distinct from source assertion.
Check actual applicability and assess the actual inherited review applicability for substantive changes, concrete objections or affected policy requirements; incomplete acquisition cannot promote source drafts or erase a known limitation.

<a id="navigation-maintenance"></a>
## Navigation and Artifact Maintenance

Links, nearby ownership labels, layout, spelling and wording in reviewed documents may be updated in place when the mathematical content, dependency use and review conclusions are unchanged; this is the maintenance track and needs no new material or C/T version, mathematical review, or formal correspondence artifact solely for the edit.
Check actual meaning: a sign, quantifier or hypothesis correction, or a link invoking a different theorem or supporting argument, follows the substantive-change rules.
Administrative locations in another author's material may be repaired directly under the [collaboration boundary](identity.md#collaboration-maintenance-and-conflicts).
Its mathematical-conflict procedure requires approval for the actual scoped recheck without creating a blanket review gate or permission to substantively edit that author's material.
Routine maintenance leaves the coherent edits and Git history; no operation entry, standalone report or per-file correspondence record is required.
Keep the affected material decisions, locators and derived navigation coherent in place.
Check the actual diff and repair the incoming references instead of retaining an obsolete directory solely for compatibility.

Remove historical mathematical digest values and present byte-binding requirements while preserving the actual checked statement/argument, verdict, scope, limits and checking relationship.
An unchanged relocation may repair exact input locators without implying a review of later mathematics; a mathematical change still requires the ordinary version/review process.
A truthful historical account of a comparison may remain where useful, without a retained digest or retention promise.
Literature-file fingerprints computed from actual local bytes remain only at the sole source registry for accidental-damage checking; intake carries no literature baseline.
A maintained path alone does not promise a historical byte image, and a byte comparison does not certify mathematical harmlessness.

## Reviewing an Argument

For a first whole-proof review, preferably enumerate obligations from the exact statement and declared review scope before consulting previous review conclusions, check the argument and form initial findings, then compare with earlier findings and address discrepancies.
Reading old findings first is appropriate for a known-objection recheck, a changed-interface review or compatible inherited review; disclose the sequence used.
This is a recommended review method, not a mandatory blind-review procedure.

1. Start from the exact conclusion and work backward to enumerate the obligations and required inputs.
   Compare the conclusion with the original question; record any strengthening, weakening, or change of scope.
2. Read forward through the construction.
   Check that every invoked result's hypotheses are available where it is used, with the correct objects, parameters, constants, and domains.
   Follow substantive dependencies to their C arguments or [source units](literature-audits.md).
3. Check interfaces in both directions: the preceding result supplies what the next step requires, and the next step introduces no undisclosed assumption.
   Detect cycles, including disguised assumptions of the desired conclusion in a definition, existence assertion, or imported interface.
4. Check the mathematically relevant boundary and degenerate cases, admissibility, normalization, integrability, limit interchanges, and uniformity.
   Distinguish a formal identity or numerical pattern from the existence or general theorem being claimed.
5. Check source completeness as well as mathematical validity.
   For recognized named or established results, verify the recorded source identification, exact locator and hypothesis match under the [known-result rule](knowledge-reuse.md#recognized-known-results), including when the artifact contains a local proof.
   Distinguish actual theorem/proof inputs from attribution and comparisons.
   Review the argument's substantive uses and recognized results; do not launch a novelty search for every elementary identity.
6. Give the decisive argument or estimate for each finding.
   Reviewer agreement, script success, or a table of unchecked boxes does not establish an obligation.
   Record the failed implication and its consequences when a gap is found.

Independent verification does not require finding an alternative proof.
Checking only selected steps supports a partial review; a whole-proof conclusion requires coverage of all substantive obligations, dependencies and interfaces, identifying accepted inputs and applicable prior reviews used within their recorded scope.

Report mathematical validity and source completeness separately in the existing audit findings.
A passed proof review does not certify that attribution work was done.
If only a citation or identification remains unresolved while a complete local proof supplies the step, retain the supported mathematical assessment and record the source correction and follow-up.
If the proof instead relies on an unverified external assertion, retain an unresolved mathematical dependency.
A review cannot be described as covering source completeness while omitting a known outstanding attribution issue.
No additional status field, registry or full-source proof audit is required.

## Completion and Verification Boundaries

For manuscript reviews, apply the responsible author's actual writing and review procedures and the [truthful review-scope rule](writing.md#whole-manuscript-definition-review).
Report the checked revision, sections or whole-manuscript coverage, applicable exemptions, findings and unresolved scope.
Check mathematical meaning and source compliance separately; a formula may be clear while its standard name or citation is missing.
A targeted correction does not imply a whole-manuscript pass.
Preserve earlier evidence and add a dated correction if a later omission shows that its coverage claim was too broad.

A substantial result assembled from several claims needs an end-to-end completion audit before it is treated as proved or used to close its goal.
Check the goal's actual acceptance criteria.
For a theorem target, explicitly restore the original quantifiers and account for every temporary restriction, endpoint, and approximation step.
A proved special case is progress; it does not complete a broader target.
For a different kind of goal, evaluate its stated criteria rather than inventing a theorem requirement.

Report the checking methods, decisive evidence, supported conclusion and material limitations relevant to this review.
Omit irrelevant categories rather than filling not-applicable rows.
Disclose an unperformed check when it limits the claimed conclusion.
Mathematical, computational, build, formal and external checks do not substitute for one another; include each only when relevant.
No new review hash or extra standalone review file is required.

If formalization is undertaken, identify the theorem artifact, pinned environment, successful commands, remaining placeholders, and actual trusted axioms or external assumptions.
Distinguish a design or source/API inspection from implemented and checked code.
A successful build alone does not certify the intended theorem, its definitions, or its trust boundary.
This framework does not require formalization or prescribe a policy of accepting external mathematical axioms.

## Corrections and Reopening

A review outcome remains open to concrete objections.
Identify the failed implication, quantifiers, affected material and downstream uses.
Preserve the earlier finding and add the actual dated correction; correct substantive fixed mathematics through an appropriate new version and explicitly reconcile affected C/T decisions and support.
Check the actual changed interfaces and derive navigation when needed, optionally using `python scripts/render-research-navigation.py` after the relevant batch settles.
Never correct status only in a generated row; record the responsible material decision first.

Update the affected Task contracts and strategy records as needed.
Mark affected assessments as requiring recheck until the relevant dependencies and interfaces have been resolved.
A changed contract of a previously completed Task requires an explicit reopening decision or a new completion decision with an applicable review of that exact changed contract and selected support/dependencies.
Adopt the actual fixed R/L finding through the decision's `review` relation under the [Task lifecycle rule](tasks.md#task-records) and [review-binding contract](../material-format.md#review-bindings-for-new-accepted-decisions).
A newly written review alone does not select completion, and T has no overall `review-status` field.
Preserve the earlier completion decision and its true checked scope.
Do not silently weaken the original target to retain a completed label.

## Record Template

Use the inert [record template](../templates/proof-audit.md), replacing placeholders with actual evidence.
A template is neither authorization nor a completed record.

## Independent review obligations

At key proof points and after Task completion, separately organize an independent inspection of the relevant point and the complete logical chain, respectively.
Assign the reviewer or review arrangement through the existing Task/work workflow, retain exact input and finding links, and disclose any pending inspection.
A revised complete proof can first be `proved` with an actual `self-reviewed` finding; a changed label cannot manufacture independent evidence, and older independent findings do not cover revised inputs automatically.
No agent identity registry or independent approval for every intermediate Claim is required.


### Finding-level review relationships

The R/L finding owns its actual checking relationship; the C/T decision owns adoption and the aggregate assessment.
Use a `Review relationships` table with columns `Review` and `Relationship`, linking each finding to its real local anchor.
Allowed relationships are `self-reviewed`, `independently reviewed` and `unknown`; an omitted row means unknown, never independent.
Explain the actual review arrangement and inspected scope in the finding's existing account.
Do not derive a finding's relationship from a consumer label or physical version.

For a new independently reviewed acceptance, selected findings explicitly classified as independently reviewed must be in fixed R and together cover the exact required inputs through their Review bindings.
Complementary independent statement and argument findings can supply this coverage.
A self-reviewed aggregate does not turn its independently checked parts into self-reviews;
a later independent argument finding can reuse an unchanged independent statement finding.
A new C/T physical version cannot turn a retained self-review into independent evidence.
Unknown historical relationships remain unknown and old assessments remain historical;
supplement only evidence necessary for an actual new classification.
Preserve known finding relationships and fixed scopes.
Corrections to a known finding use new review evidence, not a rewritten relationship.
This structural check does not certify mathematical correctness or require a new review registry.

For acquired R/L findings, the adopting agent checks the original per-finding Review bindings and actual acquired/retained inputs.
An independent relationship does not broaden inspection to other inputs in the same acquisition.
Keep exact target versions, anchors and scope; local reference maintenance does not change the performed review.
Unknown legacy scope remains unknown through onward transfer.
Existing separate-review scope evidence remains usable.
See [intake rules](intake.md).

## Inherited-review applicability

Preserve recorded source/review framework context, original source identity, acquired scope, findings and limits.
The receiving installation or a generated index supplies no earlier review stamp or new verdict.
Compare unknown review-relevant differences before reliance: record harmless differences as reusable, or require the relevant supplementary review for actual additional obligations.
A concrete objection follows ordinary correction at the affected material and consumer.
A version alone neither certifies compatibility nor triggers a full re-audit; no obsolete parser, fingerprint registry or automated compatibility cascade is required.
Structural provenance checks neither authenticate a declaration nor prove mathematics.

Manuscript exposition, definition/citation use, document-wide consistency and build/layout review belong in the reviewed manuscript's document README or manuscript-local review record.
R reviews project mathematics: an actual C argument, T completion, computation or mathematical input separately assigned and checked.
Appearance in a manuscript does not change that distinction.
A manuscript finding about a possible proof defect stays local until the underlying mathematical object is separately reviewed; do not broaden the original review or redirect C/T acceptance to manuscript records.

## Project review index

mathematics/audits/reviews/index.md links fixed R identities/findings with a short title and actual scope sufficient to select the review.
R owns inputs, findings, relationships and limits.
The agent registering, revising or relocating a review maintains its manual entry after that operation; manuscript-local reviews are excluded.
