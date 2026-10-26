# Definitions and Concept Organization

## General Definitions and Their Instances

Index general mathematical definitions by concept group, using standard terminology where available.
A group may collect a definition, its known equivalent formulations and closely related conventions, with exact links that distinguish them.
Group membership is navigation, not an assertion that every listed construction is equivalent.

Parameter substitution, notation changes and different theorem hypotheses do not create additional definitions or definition versions.
For example, division closure for a ring inclusion $A\subseteq B$ is one general definition; choosing $B=M$ or $B=\mathcal U(M)$ is an application of it, even when the resulting sets differ.
The particular ambient algebra, generators, state or trace, domain assumptions and use of adjoints belong in the consuming statement or proof.

Distinguish definitions when their mathematical constructions or meanings differ, rather than merely because their instances or notation differ.
Do not force unrelated constructions into an artificial general definition just to reduce the number of entries.
Known equivalences can be cited within one concept group without creating project claims to reprove them.

## Complete content and registration

Research, source audit and manuscript preparation register reusable mathematical definitions, terminology and associated symbols through the concept index.
Reuse an adequate complete U/C/L entry without moving or copying its body.
At that home, retain objects and setting, parameters and quantifiers, defining condition or construction, domains, conventions, terminology or aliases, and symbols and normalizations.
Link its exact stable entry and source edition/passages, with meaningful local adaptations and unresolved limits.
An incomplete terminology row or an observed name without a complete definition remains an identified gap.
Register genuinely different meanings or normalizations distinctly; letters and parameter instances alone do not create definitions.
Existence, uniqueness, equivalence and well-definedness assertions keep their theorem and inspection status.

## Locations and Naming

Source definitions remain at their adequate U/C/L homes, with the source version, exact locator and actual inspection scope retained in the responsible source record under the [literature-audit rules](literature-audits.md).
The group index links to those precise entries instead of copying their full text.

A project-specific construction or formulation stays in its responsible mathematical material, in a clearly marked **Definition** paragraph or section with a stable semantic anchor.
Use the owning Claim when the definition belongs to its statement, or a fixed L account when it needs separate durable exposition.
State its parameters, construction and necessary conventions there, and identify the source or local adaptation when applicable.
Direct adoption of an existing definition needs only a precise reference and the applicable parameter choices at the point of use; it does not require rewriting the definition in the ledger.
Use established terminology first, then a descriptive name where needed; mark a tentative name as provisional.
Local introduction, combined references or failure to locate an earlier formulation does not establish originality.

A coherent standalone fixed account uses the author’s existing L convention, such as `mathematics/ledger/Author_L_F0001_v1.md`, with its verified author, actual research line and necessary source/adaptation scope.
The definition index links to that exact home; collection files in `mathematics/definitions/` keep their standard navigation names.
Multiple sources or frequent use alone neither require a new definition nor require moving an existing one.
Choose one authoritative home for the adopted formulation and link to it elsewhere.
A definition does not by itself require a new Claim, Task, registry or material kind.
Use the numeric identity of its actual C/L/source-unit home, with a descriptive heading and stable anchor.
Associated substantive assertions follow the existing [Claim rules](claims.md#claim-registration).

## Exact Entries and Consumer Links

Keep group entries small and record only the information needed to identify and use the definition:

| Field | Required content |
| --- | --- |
| Concept and entry | General definition name and, where useful, established aliases or the distinction between listed formulations. |
| Exact home | A link to the authoritative Definition paragraph, source audit entry or equivalent precise location, using a stable anchor. |
| Source and adopted convention | For a sourced definition, link the audit record identifying the edition/version and definition, section or page locator. State any local departure from that formulation. Do not duplicate an already precise source record. |
| Consumer navigation | Summarize actual forward references from Claims or their proof artifacts, distinguishing statement/hypothesis use, use in an identified proof version, and discussion/comparison only. Leave this empty when no such references are recorded. |

The forward reference in the consuming statement or proof is authoritative for its use of a definition.
The index provides reverse navigation derived from those references, not a second authoritative list of dependencies.
Keep the actual parameter choices and applicable restrictions with the consumer.
A discussion link does not establish a proof dependency, and a definition used only in one historical proof is not automatically an input to the current proof.
Source inspection depth and current claim assessments remain in their responsible audit and status records.

## Citation Purposes

An entry may include citation candidates when this helps manuscript preparation; this field is optional.
Use existing citation keys and bibliographic identity from the canonical [references.bib](../../mathematics/literature/references.bib), with precise locators and purpose labels such as `origin`, `current formulation`, `notation`, `standard` or `exposition`.
Select inspected artifact or version facts from the [registry](../../mathematics/literature/registry.md) when needed.
The manuscript record should identify the chosen citation's purpose when the distinction matters, following the [citation and notation rules](writing.md#citations-notation-and-versions).
Different uses may appropriately cite different sources for the same definition.

For manuscript presentation, follow the [definition-citation rules](writing.md#definition-citations) and [explicit user terminology and citation preferences](preferences.md#scope-and-adoption).
Those rules decide when a definition should be recalled or cited for the intended audience; the [definition index](../../mathematics/definitions/index.md) continues to identify its mathematical formulation and source candidates.
An approved background-term exemption does not remove the need to specify local hypotheses or to cite an external result.
Do not duplicate the community exemption table here or infer a new exemption from the absence of a citation in an exemplar.

A source used for the current formulation, notation or exposition is not thereby evidence of historical priority.
An `origin` label requires evidence for the asserted origin; distinguish independently checked historical evidence from a source's attribution, and leave priority unresolved when appropriate.
The oldest reference found in a bounded search does not establish first introduction.
Do not maintain a separate bibliography or require a priority investigation merely to use a standard definition.

## Known Facts and Project Arguments

Before proving well-definedness, existence, equivalence of formulations or another intermediate assertion, follow [reuse before proof](knowledge-reuse.md#reuse-before-proof).
Use existing audited knowledge first, consult local literature when that is insufficient, and continue to an appropriate external source under the [search policy](literature-search.md#autonomous-literature-search) when the needed input remains unresolved.
Stop when a sufficiently identified input supplies the required statement and its hypotheses apply.

Established literature results may be used as [accepted external inputs](literature-audits.md#accepted-external-inputs), with the source version, exact statement, applicability and inspection depth made clear.
They do not automatically require new C IDs, a local reproof or a fresh audit of the original proof.
Explain a direct notation change or parameter specialization at its point of use.
If a purported adaptation requires a substantive argument beyond the available inputs, record that project Claim deduction in C and apply the existing claim and review rules at its useful mathematical scope.
Neither an unsuccessful search nor a local proof establishes novelty.

## Mathematical Changes and Historical Proofs

An actual change to a definition's construction, meaning or adopted convention that affects mathematical statements or arguments follows the [substantive-operation rules](ledger.md#substantive-mathematical-operations).
Record the change and affected uses in an appropriate existing section when that suffices.
Preserve the definition or convention used by a historical proof under the [proof-version rules](claims.md#proof-versions); do not silently replace it and thereby change what an earlier review covered.
Different parameter choices or hypotheses in different applications do not by themselves require definition versions.
Formatting, navigation, link repair and faithful indexing do not require separate mathematical-operation records.

These rules create no additional approval process.
If an operation also entails lemma extraction or theorem designation, the existing [approval rule](claims.md#lemma-extraction-and-approval) still applies to that operation.

## Record Template

Use the inert [record template](../templates/mathematics/definition-entry.md), replacing placeholders with actual evidence.
A template is neither authorization nor a completed record.

Consumer navigation identifies the authoritative mathematical use from its forward references, never a manuscript TeX file, convention or review.
Manuscript projects maintain their own forward source maps.
The agent changing a formulation or its actual mathematical consumer updates the affected concept-group entry; unchanged definitions are not reorganized solely for index formatting.
