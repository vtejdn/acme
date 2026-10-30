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

Before creating or retaining U content, apply the [common content decision](records.md#substantive-material-retention) to the actual source finding and existing units.
Preserve definitions/results/mechanisms, the inspected edition/passages, applicability and uninspected-proof limits.
Acquisition-only facts stay in the source registry/intake; neither a download nor existing theorem text substitutes for source-inspection evidence.
The registry is a machine-local account, while shared U/L and source contents retain actual work/edition, passages, mathematical findings and inspection limits without requiring another author's current holding or account.
Missing local registration neither invalidates shared evidence nor establishes missing originals; actual U reception still completes its own source-preparation outcome and failure reporting under the [literature rule](literature.md#acquisition-before-u-reception).

Keep source-level navigation in `<citation-key>/readme.md`.
New fixed reusable units use `<citation-key>/<Author>_U001_v1.md`, with `<Author>_<OriginalRepository>_U001_v1.md` for imported originals.
Use the existing `<citation-key>-U001` identity and lowercase unit anchor; do not allocate a research-line or Task number.
The source key's numeric positions are shared across authors/origin prefixes, with physical versions retaining their actual original-family correspondence.
For intake relocation, choose the receiving position and exact local edits explicitly while preserving original source identity, external fixed locators and unrelated literal examples.
The material version is separate from the inspected source edition.
Each fixed unit owns one unit anchor and the concise source-version, source-locator and inspection facts specified by the [material input format](../material-format.md#fixed-source-unit-inputs).
Organize units around definitions, results, proof mechanisms or tightly dependent result groups; file length and page count do not determine mathematical boundaries.
Existing multi-unit and historical files require a coordinated, information-preserving conversion; this naming rule does not authorize guessing an author or silently splitting their evidence.

Within the actual inspected scope, process explicit definitions and the terminology and symbol conventions needed to reuse the source.
Keep complete definitions at adequate U/C/L homes and register their precise stable entries through the [concept-group definition index](../../mathematics/definitions/index.md), following the [definition rule](definitions.md).
Retain objects, hypotheses, domains, normalization, source terminology and meaningful formulation differences; an empty locator or incomplete row does not supply a complete definition.
A whole-source audit handles definitions within its real coverage; a selected-passage audit does not claim unrelated chapters.
Reuse adequate inspected content without creating a unit for each definition or re-auditing an established theorem merely to register its interface.
An adequate complete fixed C/L account can retain integrated source inspection and adaptation evidence in place; a manuscript citation does not require copying it into an extra U.
Independent reusable source-audit units retain the ordinary U home, and an actual evidence gap follows the common content decision at its necessary scope.
A reusable definition may have its own anchor within an existing source unit; indexing does not require moving it, creating a unit for every definition, or registering each theorem's parameter substitution.
Source versions and locators stay with the source record.
Optional manuscript citation candidates follow the definition rules and the sole bibliography; historical attribution needs evidence separate from checking the definition's mathematical content.

For an unchanged-source key correction, rename unit IDs, anchors and consumers together under [coordinated renaming](literature.md#coordinated-key-renaming), preserving inspection content and scope.
Same-work revisions retain the citation key and explicit artifact/version locators.
Review coverage belongs to the inspected version and passages; before a consumer adopts a revised result, compare its affected statements, hypotheses and proof interfaces.
Acquisition alone does not transfer review or require new unit IDs.

Assign each unit an ID `<citation-key>-U001`, increasing the numeric part within that source without reusing an issued ID.
Preserve the registered citation key's case in the ID.
Give each unit an explicit lowercase HTML anchor, for example `<a id="miy22-u001"></a>` for `Miy22-U001`; links use `#miy22-u001`.
These are naming examples, not completed audits or allocated IDs.

The existing mathematics/audits/literature/index.md links unit IDs to their authoritative source records; it is navigation, not a second assessment or acquisition authority.
Check it and coordinate allocations before concurrent edits.
A source-specific `readme.md` supplies local navigation; keep verification facts in the unit record and summarize them by reference in indexes rather than maintaining competing assessments.

Retain unit IDs when moving or splitting files, and update all incoming links together.
Never reuse an ID for an unrelated statement.
Record dated corrections and the exact source version reviewed.
A new source version does not inherit an earlier verification automatically: compare its statement, hypotheses, locator, and relevant proof before carrying the assessment forward.
If a statement materially changes, preserve the old record and explicitly relate the replacement unit to it.

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
Acceptance for use does not imply that the source proof was independently checked and does not upgrade a reading-coverage state to `Audited within scope`.
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
Download and version metadata belong in the [literature registry](literature.md#literature-acquisition); do not create a second bibliography or infer a completed unit audit from acquiring a file.

When a search resolves or challenges a dependency, update the authoritative unit and assess its actual downstream consumers.
If the search is paused with the dependency unresolved, preserve that limitation.
A locally verified repair does not require indefinite searching for author confirmation.

<a id=coverage-states></a>

## Reading Coverage and Review State

Maintain states for a specified passage, chapter, result, or unit and exact artifact version.
A source-level index summarizes coverage by links; it must not label a whole monograph audited because selected results were checked.
Missing coverage defaults to unreviewed, not verified.

| State | Evidence required |
| --- | --- |
| Unsearched | No search for the specified topic and version has been performed. |
| Located | A potentially relevant passage has been identified; its mathematical content is not yet checked. |
| Read | The statement and surrounding conventions have been read; proof review is absent or partial. |
| Audited within scope | The specified statement, hypotheses, proof steps, and necessary dependency interfaces have been reviewed, with retained external inputs explicitly listed. |
| Questioned | A gap, conflict, suspected error, or inaccessible critical dependency remains; preserve the previous state and identify affected consumers. |

These workflow states supplement, rather than replace, the existing statement-check and proof-inspection fields.
An audited unit with retained external inputs does not imply independent verification of their proofs.
A statement-checked established theorem may be [accepted for use](#accepted-external-inputs) with its proof-inspection limit disclosed; an unaudited lead or unresolved applicability can support only a conditional route.
Keep the coverage state tied to work actually performed rather than the decision to use the input.
Formal verification requires a separately recorded successful proof-assistant check.
Do not retroactively relabel existing records without inspecting their evidence.

For lightweight discovery or reading, use this compact record in the source-specific audit; promote it to the full unit template when it becomes a reusable input:

```text
Source/version: <actual work, edition or artifact identity; suitable shared bibliography, same-edition contents or existing U/L evidence locator>
Scope/locator: <topic; chapter/result; printed and PDF pages where available, or actual HTML headings/labels/native anchors>
Trigger/intended use: <research question, dependency, discrepancy, or explicit request>
Date/reviewer and state: <actual work performed; self-review or independent review>
Finding and hypotheses: <candidate or checked statement, with conventions>
Dependencies/unchecked scope: <links and verification boundaries>
Search evidence: <queries/sections inspected; extraction limits; reason for stopping>
Open issues/next action: <specific gap or none; affected claims and required rechecks>
```

Keep the actual edition, chapters, original page labels and inspection limits at this shared home without requiring a local registry account or anchor.
An actual account lookup may be named as inline code; its legitimate one-way contents/source links do not require a shared backlink or a new U merely to supply a link.

On version changes, compare the passages and dependencies actually used before carrying their assessments forward.
On a discovered gap, record a dated correction and identify downstream claims requiring reassessment.
Neither an unsuccessful search nor a review pause establishes nonexistence or novelty.

## Record Template

Use the inert [record template](../templates/mathematics/source-unit.md), replacing placeholders with actual evidence.
A template is neither authorization nor a completed record.

Manuscript-specific review belongs with its document under the [manuscript review rules](writing.md#manuscript-review-and-mathematical-provenance).
Project-mathematics R findings retain their actual C/T/computation targets and coverage.

## Source audit index

mathematics/audits/literature/index.md links source-unit identities and exact authoritative reading records, with a concise scope label where needed.
Summaries link the units rather than create another acquisition or assessment record.
The source-record author/maintainer updates affected manual entries after registration or relevant changes.
