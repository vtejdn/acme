# Source Audit Rules

## Default Audit Scope

Literature intake and source audits **exclude associated Lean code by default**.
Include Lean compilation, code/proof inspection, theorem-to-paper comparison or axiom/trust checks only when explicitly requested.
A request to audit a paper, including its full proof, does not by itself request an audit of accompanying Lean code.
Apply the requested depth to the source's mathematical exposition and proof; a link to code or the source's claim of formal verification does not establish a local Lean audit.

If a conclusion relies on an unchecked Lean step, identify that dependency and limit the assessment to the evidence actually inspected; do not silently expand the audit to code or claim that step was verified.
An explicitly requested Lean audit follows the [proof-audit rules](proof-audits.md).
This default adds no mandatory Lean checklist or report to ordinary source audits.

## Organization and Stable Units

Before creating or retaining U, apply the [common content decision](records.md#substantive-material-retention), reusing adequate mathematical/source evidence.
Preserve actual definitions/results/mechanisms, inspected editions and passages, applicability and uninspected-proof limits.
Bibliographic identity stays in references.bib; useful source/edition explanations stay in the source README, without an acquisition account.

A local rolling U uses mathematics/audits/literature/SourceKey/Author_U001.md, with one real human author and necessary stable anchors.
An acquired U retains its necessary registered original-repository prefix, for example Bob_repo1_U001.md, and exact original provenance.
It has no physical _vN, current pointer, fixed copy or snapshot account; arXiv v2 or a publication edition remains a distinct source fact.
Each source-key and human-author namespace starts at 001 independently, with necessary original-source distinctions retained.
Yin_U001.md and Ma_U001.md in the same source directory are separate units; Yin's next number is 002 and Ma consumes none of Yin's sequence.
Use the existing author-specific [allocation state](../material-format.md#material-family-allocation-state), not a shared directory-wide upper bound or a new unit register.
Full author/origin/path identity distinguishes units; SourceKey-U001 alone is not a cross-author identity.
The lowercase sourcekey-u001 anchor is file-local, so equal anchors in different authors' files are legal.
Check real same-namespace occupancy and explicit original correspondence without reading unrelated authors' bodies; necessary sibling identity-header reads stop at their header byte/decoding boundary.

The author and that author's agents maintain U under actual authority, correcting or extending its current useful content without an edit-history log.
A collaborator may write their own supplement/correction in the same source directory, cite the affected U and reuse sufficient existing work.
Substantive corrections to another author's U remain that author's responsibility; agent roles and equal names transfer no authorship.
Source README may contain concise author sections for useful preprint/publication editions, public addresses, logical originals, page correspondences, edition differences, use limitations and U navigation.
Do not require an empty author section, field table, complete bibliography duplicate or holding assertion.
Each human maintains cross-machine validity of their links with agent assistance in actual scope; private setup stays private without path synchronization or availability certification.

U points precisely enough to the edition explanation actually inspected and identifies the passages, conditions and actual checks/limits in ordinary prose.
A changed current source link does not alter the edition inspected earlier; preserve still-used edition explanations.
No Source and inspection table or enumerated coverage state is required or interpreted as a mathematical verdict.
Define units by mathematical purpose, reusing adequate complete U/C/L rather than creating a file per definition, search hit or downloaded source.
Process complete definitions, terminology and symbols under the [definition rules](definitions.md), retaining objects, hypotheses, domains, normalization and formulation differences.
New substantive project deductions keep their adequate fixed C or other responsible home.

### Unit granularity and maintenance

One source inspection may create no new U, one U or several U, according to its actual content and useful responsible homes.
When existing U/C/L is sufficient, reuse it; retain any necessary new findings, actual checking scope and limitations without a record merely stating that another inspection occurred.
An inspection round, session, agent, chapter, theorem count or source page count does not determine the number of units.

The default order is to reuse sufficient material, maintain a suitable existing U, and create a new unit when independent organization, reference or human-author attribution actually requires one.
For the same author and topic, corrections, details, hypotheses, notation, application limits and deeper inspection normally update the existing U.
Moving from statement reading to proof inspection does not itself issue a new number, adopt later content for old consumers or expand an earlier R's actual review scope.
Keep still-useful mathematical reasons for errors, failures and limitations without retaining every edit's process history.

Closely connected definitions, results and proof mechanisms may share sections and stable anchors within one U.
Separate independently understandable and reusable topics when doing so improves their organization or citation, without requiring one U per paper or one U per theorem.
Split a mixed unit or merge redundant or excessively fragmented units only for an actual understanding, reference or maintenance benefit, preserving necessary content and repairing affected consumers.
For another author's substantive supplement, correction or useful checking evidence, prefer that author's suitable existing U and create their own unit when needed, citing the original rather than taking over its substantive body.

A changed source-edition label does not automatically create U.
Compare the adopted statements, hypotheses, proof interfaces and inspection objects; pure page, numbering or layout changes maintain source notes and locators.
When substantively different editions remain useful, keep their actual source and application ranges explicit and judge any need for separate U from that content.
New project arguments retain their adequate C or other responsible home and can be cited from U.
Apply the author, provenance and downstream-maintenance boundaries below; a stable link does not freeze the current rolling body as historical evidence.
No count, length or similarity threshold, granularity field, required decision table, new approval, automatic classifier or compulsory tool is introduced, and this rule triggers no whole-library reorganization or renumbering.

When editing, combining, splitting, moving or adapting U, identify and repair actual downstream references, including source notes, other U, definition indexes, mathematical materials, reviews and manuscripts.
Locator-only repair preserving actual objects, meaning and adoption/review scope is shared maintenance under actual authorization, including references in another author's material.
This grants no substantive author takeover or development-role exception.
True changes to an adopted input require corresponding reasoning and assessment work; later U checks are not retroactively part of old R.
Formal arguments identify sufficiently precise external statements, hypotheses, edition, locators and adopted scope; a stable U link does not freeze its entire current body.
Retain necessary earlier mathematical and review facts at their responsible home without recreating U snapshot history.

The source index and source README provide concise navigation by author and full path, not another assessment, availability or acquisition authority.
For an unchanged-source key correction, maintain paths, anchors, author-specific allocation and actual consumers together under [coordinated maintenance](literature.md#coordinated-key-renaming).
Preserve real source/transport facts and actually inspected scope, comparing affected uses before carrying checks to a revised external edition.
Same-repository reuse prepares originals only when further reading is necessary; actual personal import and external intake complete selected necessary original preparation and report true failures under the [literature rule](literature.md#acquisition-before-u-reception).

## Content and Verification

Every reusable unit must expose its mathematical meaning without depending on chat history.
State or link the definitions and dependencies needed to understand it.
Give the actual hypotheses and quantifiers, including the mathematical setting, normalization, domains, and convergence conventions that affect use.

Separate the source statement from local notation conversions, direct specializations, and additional deductions.
Record each adaptation and why its assumptions apply.
If an adaptation needs a substantive new argument, put the actual reasoning in a fixed C material under its canonical Claim identity and link its [Claim entrance](../../mathematics/claims/index.md).
A source citation does not establish the stronger local conclusion by itself.

Apply [reuse before proof](knowledge-reuse.md#reuse-before-proof) before developing such an argument.
Known equivalence, existence, uniqueness or well-definedness results can be accepted and cited under the external-input rules below; they need neither a duplicate project Claim nor a reconstructed proof solely because a definition relies on them.
Record any still-needed extension separately from the established input.

Explain the proof mechanism and the depth of inspection: statement only, selected proof steps, or a specified full-proof review.
Identify steps and dependencies not checked.
Record direct reading versus secondary reporting, source access limitations, edition/version, errata considered, and what evidence supports each verification fact.
Do not infer an independent proof check from the presence of a theorem in a published source.
Framework source reviews concern agent inspection; an independent classification requires the separate isolated mathematical context in the [review arrangements](proof-audits.md#review-arrangements), while the source author's assertions and human instructions remain distinct facts.

When a source unit supports a [goal](tasks.md), route, or project claim, link the relevant IDs and say what the unit supplies.
Identify limitations and conditions it does not supply.
If a gap or misquotation is found, record the failed implication, correct the unit, and reassess affected claims and audits downstream.

<a id="accepted-external-inputs"></a>

## Accepted External Theorems and Unresolved Dependencies

These acceptance rules cover external literature, including GitHub-hosted sources.
Identifiable ACME materials use [approved intake and inherited review](intake.md).
Third-party sources stored in ACME repositories remain external literature.
Local deductions from cited literature do not import the source repository's record identity or review status.

An agent may accept an established external theorem as a mathematical input within the authorized research scope after checking its exact statement and version in an identified primary source, verifying its hypotheses and applicability to the current argument, and addressing any concrete objection affecting that use.
Record the citation and locator, why the input applies, the decision to accept it, and the actual depth of proof inspection in the source record or the consuming argument.
An ordinary established theorem need not have its original proof re-audited solely because it is used.

Such an accepted input can count as a resolved mathematical dependency in the responsible [Claim material and decision](claims.md#dependencies-and-corrections).
Acceptance for use does not imply that the source proof was independently checked or expand the recorded inspection scope.
Explicitly state when the original proof was not reviewed.
A retained foundational theorem is not an unresolved mathematical premise merely because its proof lies outside the current review.

When an agent recognizes a known result, apply the [source-check trigger](knowledge-reuse.md#recognized-known-results) even if a complete local proof is already available.
Record the source's role under the [dependency distinctions](claims.md#dependencies-and-corrections).
Recognition from memory, a theorem name, and local proof review do not themselves verify a bibliographic attribution.
A verified source may identify the known result without being a premise of that particular proof.
If attribution remains unverified, retain that follow-up explicitly while assessing a complete, independently supported local argument on its own evidence; a missing attribution alone does not make that mathematical argument unresolved.
An argument actually relying on the unverified theorem still has an unresolved mathematical input.

Keep an input unresolved when its statement lacks adequate source evidence, its applicability is unchecked, a relevant objection remains, or a required local extension has not been proved.
Claims whose conclusions require those unresolved obligations remain open.
Detailed proof review is required when a suspected error, critical nonstandard input, incompatible conventions, a local extension requiring new reasoning, a relevant version discrepancy, or the explicit task makes statement and applicability checks insufficient.
Inspect the affected steps and necessary dependencies without automatically reviewing the entire source or every reference.

This distinction concerns mathematical reliance.
It does not itself supply a proof-assistant theorem or establish formal verification; formalization must record the actual checked artifacts and dependencies under the [proof-audit rules](proof-audits.md).
Existing source and project assessments change only after review of their concrete evidence, not automatically because this policy is clarified.

## Searches and Dependency Follow-Up

Apply the [autonomous search triggers and stopping rules](literature-search.md#autonomous-literature-search) when source access, a critical secondary citation, unclear hypotheses, suspected errors, or version differences require outside evidence.
Trace the exact external input used in the argument before deciding how deeply to inspect its proof.
Optional related results need not become required audit tasks merely because the source cites them.

Record consequential searches in the source-specific audit, following the [search evidence fields](literature-search.md#search-evidence).
Link the inspected source and exact version, distinguish located statements from checked proofs, and retain the scope of unsuccessful searches.
Useful source/edition explanations belong in concise author source notes under the [literature rule](literature.md#literature-acquisition); do not create a second bibliography or infer an inspection from acquisition.

When a search resolves or challenges a dependency, update the authoritative unit and assess its actual downstream consumers.
If the search is paused with the dependency unresolved, preserve that limitation.
A locally verified repair does not require indefinite searching for author confirmation.

<a id=coverage-states></a>

## Actual inspection scope

Describe the work/edition, passage, statement, hypotheses, proof steps and dependency interfaces actually inspected, with truthful limitations.
Distinguish located leads, statement reading, selected proof checks and a genuinely complete scoped inspection in ordinary prose, without an enumerated state or required three-field table.
A source-level index links actual units and cannot label a whole monograph checked from a few results.
A source author's assertion, acquisition, U presence, complete field list or successful tool check establishes no independent proof inspection.
Formal verification requires its own actual successful proof-assistant evidence.

Keep useful findings, actual dates and reviewer relationships at the responsible inspection, without inventing unknown dates or retaining every edit/search process.
On an edition change, compare passages, hypotheses and dependency interfaces actually used before carrying the assessment forward.
On a discovered gap, correct its actual author's material and reassess affected consumers under the maintenance and author boundaries above.
An unsuccessful search or a pause establishes neither nonexistence nor novelty.

## Record Template

Use the inert [record template](../templates/mathematics/source-unit.md), replacing placeholders with actual evidence.
A template is neither authorization nor a completed record.

Manuscript-specific review belongs with its document under the [manuscript review rules](writing.md#manuscript-review-and-mathematical-provenance).
Project-mathematics R findings retain their actual C/T/computation targets and coverage.

## Source audit index

mathematics/audits/literature/index.md links source-unit identities and exact authoritative reading records, with a concise scope label where needed.
Summaries link the units rather than create another acquisition or assessment record.
The source-record author/maintainer updates affected manual entries after registration or relevant changes.
