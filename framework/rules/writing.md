# Mathematical Manuscript Writing Rules

Apply the [common sentence-oriented source layout](organization.md#sentence-oriented-source-layout) to maintained prose, preserving mathematical and typesetting structure.
This shared format rule does not change the writing-choice hierarchy.

Apply these general mathematical writing rules and the effective single-writer or joint-document choices under the [four writing layers](preferences.md#scope-and-adoption) to all maintained natural-language prose under [mathematics/manuscripts/](../../mathematics/manuscripts/), not only prose compiled into TeX.
This includes project and document `readme.md`, `writing.md`, `conventions.md`, `organization.md`, `review.md`, `citation.md`, `revisions.md` and prose in TeX sources; it governs terminology, notation and style in those records without changing their evidence, scope, findings or file responsibilities.
Structured metadata, BibTeX fields, formulas, code, exact source quotations, acquired originals and generated outputs retain their native or responsible rules, while prose surrounding them remains governed by these writing rules.

Use these content standards within the [project and document requirements](#projects-and-documents) and the applicable single-writer or joint-document [writing choices](preferences.md#scope-and-adoption).

The [definition index](../../mathematics/definitions/index.md) locates responsible mathematical definitions.
Canonical [references.bib](../../mathematics/literature/references.bib) owns shared bibliographic fields; useful author edition/source explanations belong to the source README; U and source audits own inspected edition, passages and actual inspection scope.
Source observations in responsible source records are evidence, not an additional policy layer.
Keep a manuscript's choices at its existing [writing-choice home](#document-choices-and-final-review).

## TeX manuscripts and supporting records

ACME supports TeX manuscripts; Markdown and other source formats are not alternative manuscript formats.
Human authors use the TeX sources to guide the agent's writing or edit those sources themselves.
The actual current TeX manuscript is the writing and review object under the [current-manuscript rule](#current-manuscript-authority).
A request to write a manuscript is not fulfilled by delivering only Markdown prose while claiming the TeX manuscript is complete.

Markdown in a writing project supplies agent-facing instructions, project explanations, choices, organization, citation and review records, and necessary supporting working documents at their existing homes.
An assignment limited to those records needs no invented TeX manuscript or compilation merely to choose their location.
The [manuscript citation map](#manuscript-review-and-citation-records) retains its scope of actual external citation applications present in the current TeX, with source evidence, applicability, uncertainty and review-only write authority preserved.
Supporting Markdown does not create another manuscript citation map merely by containing citations; necessary source facts and mathematical findings retain their existing literature and retention duties.
Uncited bibliography entries and style-only consultation remain outside the manuscript citation map.

## Projects and Documents

An authorized writer may prepare and maintain manuscripts or presentations for any actual repository Task, including another human's ordinary Task or a joint Task.
No matching personal Task number, participation Task or separate permission from the Task creator is needed merely to select that writing subject.
A writer without a personal mathematical Task can receive the assignment.
The actual writing instruction supplies its scope; association transfers no Task authorship, lifecycle, participation, mathematical completion or E authority.
If writing exposes a gap requiring formal research beyond that assignment, apply the [inquiry-to-research boundary](workflow.md#from-an-inquiry-to-approved-research).

Use `mathematics/manuscripts/<writing-author>/<task-family>/` or `mathematics/presentations/<writing-author>/<task-family>/` by default for Task-associated projects.
The first component is the actual responsible writer's canonical human key.
The second is the complete actual local Task family, including its own author and any source namespace, without the physical `vN` suffix.
Use the actual Task identity from its responsible contract and [navigation](../../mathematics/tasks/index.md), without replacing its author with the writer or manufacturing a Task to make those keys agree.
For example, writer `Alice` can use `mathematics/manuscripts/Alice/Bob_T_A0002/paper/main.tex` or `mathematics/presentations/Alice/Bob_T_A0002/joint-results/main.tex`.
The project README identifies the actual Task and relevant contract/version; the directory creates no material identity.
When a Task changes lines, preserve the actual manuscript association and adapt its Task-family home and affected entrances together, preserving unrelated projects at occupied destinations.
Create a project only when authorized writing needs it; neither a Task nor a writer container requires an empty project, per-author index or README at every directory level.

For writing without a corresponding mathematical Task, use the responsible writer's container and a suitable purpose-named project, reusing adequate existing work without manufacturing T/E, mathematical completion criteria or a routine directory-choice approval.
Maintain the [actual project or document record](#project-and-document-records), preserving author choices, source accuracy, review and applicable build responsibilities.
This writing work starts no research or execution allowance.
An assignment limited to agent-facing project/document records needs no TeX manuscript or compilation merely for directory naming under the [supported writing scope](#tex-manuscripts-and-supporting-records).

A user may explicitly designate another home or directory name for a talk or presentation.
Preserve that choice and apply the same author, source, writing, build and review responsibilities there; a presentation does not require a new Task merely to obtain a Task-named directory.
An old project location alone supplies no exception to the [required upgrade migration](#upgrading-existing-writing-projects).

### Explicit joint writing

An explicit human assignment to joint writing permits the named responsible writers to maintain the shared manuscript or presentation sources and document-local writing records within that scope.
Use their canonical keys joined by underscores as the writing container, such as `Bob_Alice`, followed by the full Task family when one applies.
For example, use `mathematics/manuscripts/Bob_Alice/Bob_T_A0002/paper/main.tex` or `mathematics/presentations/Bob_Alice/Bob_T_A0002/joint-results/main.tex`.
Joint writing can concern an ordinary or joint Task; a joint Task, several mathematical contributors or a publication byline alone does not request joint editing.
Use the requested container label and order when supplied, otherwise choose a stable adequate order and reuse the same actual document; another ordering of the same keys does not justify a duplicate.

Keep the actual writers, collaboration scope, purpose and relevant Task in the existing project/document record.
The joined label is a location, never a human registration, mathematical-material author or Task/E identity.
Each writer retains their own working copy, operator binding and Git attribution under the [shared-writing exception](identity.md#collaboration-maintenance-and-conflicts), coordinating overlapping edits without a group account, signature collection, owner service or recurring per-writer permission.
Directory names grant no authority over unrelated documents, another human's research materials, fixed evidence or private settings.
Canonical C/T/S/D/R/L/U/J authorship and individual Task/E responsibility retain their existing boundaries.

Use the responsible writer's applicable choices for a single-writer document independently of the Task's author.
Joint documents use existing shared choices and common defaults under the [preference rule](preferences.md#scope-and-adoption), incorporating individual policies only when actually adopted for the document.
The writing container, responsible writers, Task creator and Git signatures determine no publication byline, speaker name or ordering; apply the existing [byline default](#document-choices-and-final-review) and actual human instructions.
Preserve real mathematical and source attribution.

### One actual document and selected transfer

Reuse an adequate existing project for the same actual document, including when the responding writer changes.
Explicit joint writing uses one shared home rather than synchronized per-writer copies.
Distinct papers or talks may have distinct purposes, and primary/supporting Task links state actual scope without another document copy or research permission.
Manuscript projects and another human's ordinary Task/E authority remain outside mathematical intake; selected personal documents use [personal import](intake.md#personal-import) under their actual single or joint writing assignment.
For a [same-author Task transfer](intake.md#task-and-manuscript-collection), include its actual corresponding manuscript project by default, identifying that relationship from the project ownership, description and delivery purpose rather than a matching directory number.
After the Task pass, independently trace the manuscript's actual statements, proofs, definitions, computations and reviews to necessary support families, U and bibliography, adding inputs the Task pass missed.
Include the project's actual papers, supplements and research notes, project/document READMEs, main files, sections, bibliography, necessary figures, styles, other build inputs, writing choices, real review records and existing unresolved manuscript revisions.
Documents genuinely belonging to that project are within scope; unrelated projects remain outside it, and an explicit narrower human selection takes precedence.
Merge both passes without duplicate support or another copy of a shared manuscript.
If no corresponding project exists, create no empty directory or placeholder.
Personal document transfer uses an appropriate single or expressly shared receiving home and preserves all actual responsible writers, without creating an unrequested Task or selecting unrelated Task/E, documents, private settings or original literature by association.
Preserve document choices and actual review scope, adapt entrances and build paths, and run proportionate affected local build checks without treating a source build as a successful receiving build.
Carry only the unresolved revision opinions attributable to the selected manuscript, with their necessary references, and check them against the received current text.
See the [revision-list rule](#manuscript-revisions).
Use the source review only within the scope that its evidence still covers after receiving changes.
Update project Task associations, mathematical source maps and build entrances to final local objects after reuse and numbering, retaining exact input versions and actual review limits.
Generated deliverables follow the explicit delivery scope; caches and ordinary compilation products are not default transfer contents.
Writing context and document navigation may link related authored documents, but authoritative C/L/U/R/J evidence remains independent of mutable presentation frames, draft theorem numbers and document-local review details.

Inside each project, give each independently compiled TeX document its own purpose-named directory, such as `paper/`, `supplement/` or `research-note/`.
Use lowercase English words and hyphens for descriptive names.
Keep the primary entry file `main.tex` inside that document's directory.

The following is a layout example, not a new goal or an assertion that these documents exist:

```text
mathematics/manuscripts/
  readme.md
  Writer/
    Author_T_F0001/
      readme.md
      paper/
        readme.md
        main.tex
        references.bib
        sections/
          introduction.tex
          main-result.tex
        figures/
        main.pdf             # Generated output; ignored by default.
      supplement/
        readme.md
        main.tex
        main.pdf             # Generated output; ignored by default.
```

The document directory is the unit of compilation.
Files included with `\input` or `\include` are sections of that document and need no separate document directory.
A separately compiled supplement has its own directory; an appendix included in the paper belongs with the paper.

Keep an existing Task family ID stable when the manuscript title changes.
If one manuscript draws substantively on several goals, choose one primary project and link the other goals with a brief explanation in its project README.
Do not duplicate the same manuscript under several goal directories.

### Upgrading existing writing projects

An upgrade adopting this layout must move and adapt all affected maintained manuscript and presentation projects, including old Task-only roots, before advancing the installed version or claiming completion.
Read each actual writing assignment, responsible project/document record and necessary content to establish the writer(s), purpose and Task correspondence.
Use a joint container only under an actual explicit joint-writing assignment; infer neither the writer from the old prefix or Task creator nor joint editing from a byline.
Reuse applicable instructions and clarify only a decisive missing fact while continuing independent authorized adaptation.

Move Task-associated projects under the actual writer or explicitly requested joint container and complete Task family; move genuine Task-free writing under its writer and purpose-named project.
Preserve necessary sources, styles, bibliography, figures, build inputs, choices, citation maps, actual reviews and unresolved revisions, including needed local untracked files and their output exclusions.
A Git-only rename must not lose those local files or force-add build products.
Inspect occupied destinations and resolve real collisions without overwriting an unrelated project, duplicating the manuscript or returning to the retired layout.
Repair affected indexes, incoming/outgoing links, source maps, build instructions, included-file paths and selected local ignore exceptions, then check the moved documents and direct consumers.
Relocation alone causes no mathematical renumbering, Task transfer, E move, source reattribution or fresh review.

Remove retired homes after preserving necessary content and repairing consumers, without old-path aliases, redirects, symlinks, shadow copies or compatibility readers.
Complete all affected project moves during the upgrade rather than defer them to a later writing request; an installation without projects needs no invented project or migration record.
The agent judges the necessary moves and preservation through ordinary reading and selected file/Git operations, without a mandatory migration tool, fingerprint, historical replay or per-file receipt.
If a required move or adaptation cannot be finished, preserve recoverable contents and report its exact incomplete scope under the [upgrade rule](../versioning.md#upgrading-an-installed-framework).
Apply that rule's incompatible-upgrade classification at closeout because affected installations require project restructuring and consumer adaptation.

## Project and Document Records

Use adequate existing homes, splitting out a companion file only for an actual independently maintained choice, organization, citation or evidence need.
The responsibilities below are not a package of files to precreate; a short document may use its adequate README for brief organization or choices, without requiring both `writing.md` and `conventions.md`.
Preserve sufficient citation and mathematical evidence at their actual homes rather than omitting it to reduce file count.

| Home | Responsibility |
| --- | --- |
| Current manuscript sources | The content, notation, structure and exposition currently maintained under the [current-manuscript rule](#current-manuscript-authority). |
| Project or adequate standalone-document `readme.md` | Actual responsible writer(s), single or expressly joint writing assignment and scope, purpose, necessary mathematical inputs and document entrances; actual Task/contract and primary/supporting goals only when they exist and apply. A compact map links principal result labels to responsible arguments and applicable proof reviews, expanding only for a substantive new result. |
| Document `readme.md` | Purpose, actual entry, required inputs, necessary current review evidence and writing-choice entrances; build instructions and latest build facts when compilation applies. Link an actual revisions file when needed without copying its opinions or declaring a closed state. |
| Existing `writing.md`, `conventions.md` or suitable choice home | Effective manuscript choices under the [preference rule](preferences.md#scope-and-adoption), without inventing a model or adoption requirement for an author who has chosen none. |
| Suitable organization record | Selected content and order; a separate `organization.md` only when the actual organization needs it. |
| Existing project/document `review.md` or adequate review home | Actual mathematical scrutiny of manuscript statements, hypotheses, proofs and inferences under the [mathematical-review rule](#manuscript-review-and-mathematical-provenance), with its true evidence and limits. |
| `citation.md` | Current external citation applications and their applicability evidence or gaps under the [citation-record rule](#manuscript-review-and-citation-records). |
| Manuscript `revisions.md` | Current writing opinions and links to proof findings that require manuscript revision when both reviews are requested. The assigned reviewer maintains the list for the selected manuscript under the [revision-list rule](#manuscript-revisions). |

Only inspect and maintain records actually affected by writing or review; unchanged files need no new "checked" entry or administrative update.
Do not bulk merge or delete old companion files during upgrade; any later authorized consolidation preserves necessary substance and consumers.
Task/Claim decisions, fixed mathematical evidence, source findings, canonical bibliography and true author source notes retain their own responsible homes, rather than becoming manuscript records.

Describe ignored output paths as inline code rather than permanent Markdown links because those files will not exist in a fresh clone.
Link to the tracked source directory and build instructions instead.

<a id="current-manuscript-authority"></a>
## Authority of the Current Manuscript

For drafting, revision and review, subject to current explicit human instructions, the current working manuscript establishes the content, notation, definitions, organization and proof exposition actually under consideration.
Read the relevant current sources before editing.
Memory, conversation summaries, earlier drafts, plans and historical review records may help locate context, but must not overwrite or revert content already updated in the current manuscript.
This factual authority neither approves a departure from effective writing rules nor authorizes changing a policy to fit the current draft.
Check recalled formulas against current sources; update a lagging writing-choice record only from actual explicit human instructions or adopted choices under the [choice-update rule](preferences.md#recording-and-updating).
Maintain an affected organization record from the actual authorized content and order, without turning manuscript usage into a policy.
Resolve a conflict between current text and effective choices within the actual instruction and writing layers, clarifying only a decisive remaining intent or authority gap while continuing independent work.

**Deleting an existing manuscript environment requires explicit human authorization for that deletion.**
Theorems, propositions, lemmas and corollaries have exactly the same protection as remarks.
This rule also covers definitions, examples, proofs and other environment-delimited passages, including abbreviated or custom environment names such as `thm`, `prop`, `lem` and `rem`, and both numbered and unnumbered forms.

A general instruction to rewrite, polish, shorten, simplify or reorganize does not authorize deleting an environment.
During an authorized rewrite, preserve each existing environment unless the human has explicitly authorized its removal, either directly or through an approved plan identifying that removal.
Omitting it from replacement text, absorbing it into another environment, or replacing it entirely with ordinary prose still counts as deletion; retaining some of its mathematical content elsewhere is not an exception.
Apparent redundancy, a stronger later result or lack of a later reference is not authorization: retain the environment and propose its removal instead.

Authorization to move an environment permits relocating the complete passage; it does not permit dropping it or deleting other environments.
Authorization to revise one passage does not authorize deleting another.
Existing explicit deletion authorization remains effective only within its stated scope.
Before delivering a rewrite, compare the affected environments with the pre-edit text and confirm that every removed environment has the required authorization.

This revision rule does not replace responsible mathematical records as the authority for proof status and provenance, or original sources as the authority for external claims and attribution.
A discrepancy requires checking the actual materials; memory alone is never a reason to restore an earlier manuscript version.

## General Mathematical Exposition

State the actual objects, hypotheses, quantifiers and conclusions.
Keep notation, domains, normalizations and convergence conventions consistent.
Make the distinction between definitions, adopted conventions, proved results, conjectures and exploratory questions clear.
A name or a change of notation does not establish a new mathematical object or originality.

Give sufficient justification for the deductions being claimed.
An external result must match the statement, hypotheses and application attributed to it; a source mention alone supplies no missing argument.
Describe contributions and comparisons truthfully.
A bounded literature search or a self-contained proof does not establish historical priority.

Judge coherence for the actual target reader and requested scope: the problem, contribution, applicable conditions, argument and limitations must form an understandable account for someone outside the research conversation.
Whole-manuscript work considers the contribution and each part's role; local work checks its connections to the surrounding argument and intended uses without authorizing a whole-manuscript rewrite.
Keep necessary explanation, hypotheses and reader navigation; word removal or a shorter manuscript alone is no quality measure.

<a id="precise-object-names"></a>
**Prefer precise object names.**
When describing mathematical objects, hypotheses and conclusions, prefer names that directly correspond to the definitions, notation or conditions.

When using a term, abbreviation or modifier, check which object actually has the stated property and keep the wording consistent with the definitions, symbols and proofs.
When revising terminology, check the mathematical meaning of the affected sentences and subsequent uses as well as the words themselves.

<a id="direct-results-and-modifiers"></a>
**State results directly and use modifiers only when needed.**
Prioritize the object, the main conclusion and the necessary hypotheses.
This requirement applies throughout the manuscript, including titles, abstracts, definitions, result statements, proofs and transitions, and covers noun modifiers and compound object names as well as adjectives and adverbs.
Retain a modifier only when needed to state a necessary hypothesis, identify an object or its domain, preserve the meaning of an established technical term, or make a relevant and supported distinction.

That a modifier describes a true property is not sufficient reason to retain it.
If removing it leaves the mathematical content, object references and necessary distinctions clear, omit it.
Omit information already conveyed by definitions, notation or the local setup.
Prior use in a draft or source, an explainable meaning, or an appearance of greater rigor does not by itself justify retention.
Avoid stacking modifiers or incorporating construction methods and proof steps into object names when they do not serve one of the stated functions.

When a modifier has substantive mathematical meaning, make its applicable object and basis clear.
Prefer stating the precise condition, construction or logical relation to using an evaluative or ambiguous label in its place.
Omit terminology that depends on a derivation not yet introduced, and place technical details where they are needed in definitions, theorem statements or proofs.
In removing modifiers, preserve necessary hypotheses, complete technical terms and applicable human-specified wording and naming conventions.

<a id="notation-in-context"></a>
**Introduce notation conventions in context.**
Place a notation convention close to the first expression that needs it, so the concrete use explains its purpose.
Do not collect all conventions in a preliminary notation paragraph when their use is not yet apparent.
When introducing a symbol, make its role clear where needed: for example, a variable, parameter, selected solution, extremizer or function value.
Then state its properties or explicit expression.
Do not repeat a role that is already clear.
Introduce a separate name or symbol only when it serves the exposition or subsequent argument.
If an object occurs only once and can be expressed clearly using existing notation, write the expression directly rather than introducing another symbol.

Repeated use alone does not justify another name.
If an existing expression is short and clear, prefer it when an alias would only require the reader to translate between symbols.
When unifying notation or adapting an earlier draft, reassess the usefulness of inherited aliases.
Separate symbols remain appropriate for new constructions, repeatedly used long expressions or objects whose names help organize the argument.

<a id="formulas-and-prose"></a>
**Use formulas for precise relations and prose for their role.**
When a short formula clearly expresses the relation between two quantities, state it directly and use concise prose to explain its purpose or consequences.
Avoid restating each operation, constant factor or normalization before or after the formula.
Explain particular steps when they present a real obstacle to understanding.
Explanations following a definition should help the reader understand the object or advance the argument.
Prefer useful mathematical properties and consequences to repeated normalization details or information already conveyed by the defining formula; retain conventions needed to determine the meaning or value of the object.

<a id="direct-result-connections"></a>
**Make necessary mathematical relationships explicit.**
When a theorem, proposition, lemma, corollary or remark directly applies, specializes, extends, compares or explains another result, identify that result and the relationship when introducing the statement, at the start of the proof, or at the step where it is used.
State the relevant hypotheses or substitution when needed to make the application clear.
Explanatory passages serving motivation, comparison, applicability or transition must likewise express the mathematical relationship needed to understand their role within the actual sentence group.
State necessary condition differences, applicability limits or implications when they are not already clear from nearby text, formulas or an explicit reference.
For example, failure to meet a cited theorem's hypotheses can limit its direct application; that fact alone establishes neither failure of its conclusion nor novelty of the present result.
Do not repeat an already clear relationship, explain every sentence's writing intention or expand ordinary reasoning that is already clear to the target reader.

<a id="mathematical-comparisons"></a>
**Specify the aspect and strength of a mathematical comparison.**
When comparing results or formulas, identify whether the comparison concerns hypotheses, conclusions, variables and domains, expressions or proof methods.
Distinguish equality of extremal values, pointwise equality of expressions, changes of variables, inclusion of applicability domains and logical implication.
Where needed, support the comparison with explicit correspondences, equalities, inequalities or counterexamples; vague assertions of sameness, equivalence or relatedness do not replace an argument.

<a id="definition-environments"></a>
## Presentation of Definitions

Apply the effective single-writer or joint-document choices for definition environments, numbering, explanatory detail and audience.
The general requirement is that the adopted definition and its use are mathematically unambiguous.
This framework does not prescribe a universal threshold for numbering a concept or explaining a familiar term.

<a id="definition-statements"></a>
## Mathematical Meaning of Definitions

Identify the objects, ambient structures, parameters, quantifiers and necessary conditions, directly or through an unambiguous standing setup.
Distinguish defining conditions from assertions about their consequences.
Existence, well-definedness, equivalence and independence claims require justification when they are not immediate from that setup.
Putting a claim in a definition does not prove it.

<a id="definition-citations"></a>
## Sources and Attribution

Make the source and mathematical role of adopted results, formulations and adaptations truthful.
State any local change that affects meaning or applicability.
A citation must support the formulation or assertion attributed to it; an exposition reference does not establish historical priority.
An assertion such as "introduced by", "first proved by" or "due to" requires evidence for that assertion.
Failure to find an antecedent does not establish originality.

Specific citation placement, first-use thresholds, familiarity exemptions and source-search procedures follow the applicable author, subfield and manuscript choices.
Whatever those choices, an exemption for explaining a term does not supply proof of a theorem or evidence for an attribution, and unusual conventions affecting an argument must remain explicit.

Where useful for understanding or verification, identify the theorem, definition or specific part of an external source actually used and explain its role in the current argument.
If different results from one source support different steps, make those correspondences explicit.
Distinguish terminology or background sources, mathematical results used in the argument and further deductions made in the present paper.
Do not repeat explanations where a citation's role is already clear.

## Community Conventions

Apply actual adopted audience and terminology choices through the [scope rules](preferences.md#scope-and-adoption).
Observing usage in one or several sources is evidence about those sources, not a mandatory convention for every author.
Do not create a second exemption table or infer a personal choice for an author without one.

<a id="style-selection"></a>
## Style and Terminology Sources

Use the actual model and terminology roles selected at the author's applicable scope.
Their selection order and fallback choices belong to personal or manuscript policy.
A role designation does not establish the source's mathematical claims or an unrecorded text-reuse permission; see [direct-text-reuse rules](#default-reuse-permission).

<a id="text-reuse"></a>
## Text Reuse and Mathematical Sources

Follow the actual author instructions and work/passage permissions governing any proposed reuse.
The two routes below supply the framework's reusable-text defaults under the [four writing layers](preferences.md#scope-and-adoption).

<a id="default-reuse-permission"></a>
### Direct Text Reuse: Profile Defaults and Manuscript Choices

An author may list their own or coauthored literature in `profiles/<author>/writing/readme.md` or the existing responsible writing-policy section, using canonical keys and links.
Listing a work in that capacity supplies the standing reuse default when writing for that author.
No separate reuse flag, additional work approval, repeated manuscript list or passage confirmation is required.

Any author, including an author without a profile, may designate further sources for direct reuse in the target manuscript's existing `writing.md` or `conventions.md`.
The designation may include explicit work, section or passage limits.
That instruction suffices within its scope.

Keep each concrete list or choice at its responsible home without duplicating full bibliographic records.
A subfield or manuscript choice overrides only the conflicting part of an author-wide default; a change of local operator does not import another person's list.
Preserve actual work, section and passage exceptions, including earlier valid authorizations.
Useful reuse does not require adopting the work as a style model or citing irrelevant passages.

Style models guide presentation.
A style-only designation does not by itself authorize prose reuse.
An author's separately adopted model-reuse preference remains at its personal scope.
Neither reorganization nor source-note membership expands or cancels permission.

<a id="use-and-reuse"></a>
### Community References: Use and Authority

A relevant passage can provide evidence of its authors' terminology, notation or presentation.
Apply the actual author's adopted community choices.
A community-reference designation grants no prose-reuse permission.
Use independently written explanation, while standard terms, notation, formulas and conventional short expressions remain usable.
State the convention selected when a mathematical difference matters.

Separate presentation guidance, prose-reuse permission and mathematical reliance.
Check that any reused formulation remains accurate in context and that its attribution is truthful.
A source role grants no permission to reuse embedded third-party text beyond the actual applicable permission.
Do not invent missing authorizations or promote a source to another role to bypass its limits.
Retain accurate mathematical attribution and distinguish earlier results from the current contribution.
No stylistic choice changes source facts, theorem hypotheses or the actual checked proof scope.

<a id="source-identity-and-storage"></a>
### Source Identity and Storage

The canonical [bibliography](../../mathematics/literature/references.bib) owns full bibliographic fields and persisted keys.
Concise author source notes identify useful editions, original links and use limitations, independently of actual manuscript inspection and review; no acquisition account or fingerprint is maintained.
Role adoption and source observations link to those responsible materials.
Stylistic consultation and bibliography-only work maintain necessary canonical bibliographic facts and useful edition/source explanations, with source validation and inspection proportional to the actual use and no original-file registration.

Use the existing case-sensitive citation key and exact retained artifact.
A new role does not require duplicating an adequate artifact.
Newly retained PDFs follow the [acquisition and version rules](literature.md#literature-acquisition).
A work may have several explicitly scoped uses with one source artifact.

<a id="maintaining-records"></a>
### Maintaining Source and Reuse Records

Record each current choice and applicable work/passage limits at its responsible scope without instruction/adoption dates, supersession narratives or implementation logs.
Update the affected choice directly; genuine source-inspection dates remain evidence.
Source records retain inspected passages, locators, observations and comparison limits at adequate U or compact source-reading homes.
Complete mathematical definitions, terminology and symbol usage remain at their adequate U/C/L homes and are registered through the [definition index](../../mathematics/definitions/index.md).
Actual author/subfield choices belong in their profile; manuscript-specific arrangements belong in their existing convention or writing-choice home.
Do not create a parallel writing-only source-note collection or treat an observed source practice as an adopted rule.

External source records follow the [manuscript reference boundary](#manuscript-reference-boundary), without manuscript-specific context or reverse pointers.
Preserve substantive distinctions, exact inspection scope and actual reuse permissions during maintenance.
The official starting repository contains unified source/definition guidance and empty definition navigation, without personal selections or live source notes.

<a id="source-preparation-for-writing"></a>
### Source preparation for research, audit and writing

Before relying on literature, reuse existing definitions and adequate source evidence, maintain necessary canonical bibliography and useful edition/source explanations, and inspect the needed passages when the actual use requires further source reading.
Follow [literature preparation](literature.md#source-preparation), including available-source, unavailable-source and searchable-contents duties at the actual scope.
Reuse adequate U evidence; fill only a real gap and state the edition, passages, applicability and inspection limits.
Register needed complete definitions, terminology and symbols through def without moving adequate U/C/L content.
Apply the actual writing choices only after the source meaning is clear, then prepare the manuscript and reconcile its actual citation uses.
Style consultation and bibliography-only work use this sequence proportionately; they require no full-paper proof audit merely to record presentation facts.
Missing PDF bytes do not block unrelated work, while an unavailable indispensable passage remains a specific unresolved input.
Neither registration nor a successful tool check establishes source identity, mathematical correctness, proof inspection or prose-reuse permission.

## Citations, Notation, and Versions

Use persisted canonical citation keys and complete bibliographic fields in the repository's [references.bib](../../mathematics/literature/references.bib).
A document's `references.bib` is a synchronized typesetting subset under the [bibliographic content boundary](literature.md#bibliography-content).
Retain an explicitly cited alternate edition and its actual scope, without copying acquisition/review logs or host paths.
Concise author source notes retain useful original links, edition differences and use limits; inspected passages, findings and checking limits stay at U/L or another adequate responsible home.
Prepare ordinary new literature, including papers hosted on GitHub, through the existing [source-preparation entrance](#source-preparation-for-research-audit-and-writing) and its literature rules, reusing adequate bibliography and source evidence.
Actually selected authored mathematical units from another research repository follow [mathematical intake](intake.md#scope-and-routing), including its real source, authorship, receiving preparation and provenance duties.
Judge the actual material and use rather than its host or a code package name; ordinary literature preparation creates no mathematical external identities or intake operation and requires no fixed Git commit merely to support a citation.

When choosing or checking citation labels, author-name display, sorting or reference-list structure, consult the [AMS, EMS and LMS bibliography guidance](../../mathematics/manuscripts/bibliography-guidelines.md) and apply the actual choices under the [four writing layers](preferences.md#scope-and-adoption).

Use the [definition index and naming rules](definitions.md) to locate adopted definitions and citation candidates.
Apply the [definition-citation policy](#definition-citations), [approved community conventions](#community-conventions) and the [author's terminology-familiarity rule](preferences.md#scope-and-adoption) when deciding what to recall or cite.
State the definitions and local parameters needed by the intended reader without reproducing the internal index.
Explicitly exempted background terms need no basic definition merely because they occur in the paper; their actual application hypotheses still belong in the manuscript.
A group of definitions may be organized together for exposition, but repeated use or multiple sources alone do not require a new project definition.
Known equivalence and well-definedness results can be cited under the external-input rules.
Apply [reuse before proof](knowledge-reuse.md#reuse-before-proof) before developing a new substantive argument while drafting.

Keep manuscript cross-references accurate under the author's chosen labeling convention.
Keep the mapping to repository Claim IDs in the project README or source comments; repository IDs need not appear in the reader-facing manuscript.

Keep one current source per document and use Git history for ordinary revisions.
Names such as `final2.tex` or dated copies of the same draft are not a versioning scheme.
Distinct standalone documents or substantively different presentations may have separate purpose-named directories, with their relationship documented.

<a id="whole-manuscript-definition-review"></a>
## Truthful Review Scope

Apply the author's actual writing and review procedures.
Record what was checked, against which current manuscript revision, with its limits and unresolved findings.
Claim whole-manuscript coverage only after that coverage was completed.
A local check, successful build or style exemplar cannot establish whole-manuscript citation completeness or mathematical proof validity.
Use the distinct [record responsibilities](#project-and-document-records) for mathematical evidence, writing-rule opinions and build facts, without a policy engine or per-term register.

## Document Choices and Final Review

The [preference rule](preferences.md#scope-and-adoption) owns writing-choice precedence and adoption; the [record responsibilities](#project-and-document-records) own their actual locations.

Omit the author byline by default when preparing a new TeX manuscript.
Leave a required TeX author field empty by default.
For a new or changed byline, use only what the responsible human specifies in the current instruction or through an applicable choice under the existing writing layers.
Preserve an established byline in routine revision unless the authorized assignment includes a change to it.
Keep project ownership, author keys, Task attribution and Git signatures separate from the byline choice.
Keep the actual responsible writer(s) in the existing project or document record, and preserve required citations and source attribution.

The two activities below use one common checking standard without adding a third role, approval or mandatory agent stage.
Adopting these rules selects no theorem, writing task, review, publication or research resumption.

<a id="writing-rule-execution"></a>
### Drafting and revision

Under the actual writing or correction instruction, read the current manuscript, responsible writer(s), effective choices and necessary direct inputs.
Read the records that own the findings selected for the current revision.
For writing opinions, use the [selected manuscript's revision list](#manuscript-revisions).
For proof findings, use [`review.md` or the adequate mathematical-review home](#manuscript-review-and-mathematical-provenance), including when the manuscript has no revision list.
For a revision covering both kinds, read each record at the scope of its selected findings.
Judge each finding against the current text, actual human requirements and applicable rules within the current writing authority.
Use the [common manuscript writing-rule checks](#manuscript-writing-rule-checks) before delivery of new, changed or adopted text and its direct effects, correcting required problems within actual writing and author authority and rechecking them.
Reading rules, pointing to an existing rule or compiling successfully does not resolve a known violation.
An optional suggestion may be adopted within actual authority and choices without per-suggestion approval; declining it alone does not make a revision incomplete.

Maintain affected mathematical/source evidence before adopting a substantive change, and reconcile only the actual affected manuscript records under their responsible rules.
Report the current result, actual completed scope and remaining mathematical, writing-rule, citation or build limitations; a known required problem in that scope prevents claiming that revision complete, although a partial result may be delivered with its gap explicit.
Report corrected review opinions through the normal reply without deleting reviewer-owned items or declaring their recheck passed.
A writing instruction alone starts no further review round; completed changes may truthfully await reviewer recheck.
Self-checks do not establish independent review, and ordinary writing does not require a separate reviewer unless an actual applicable arrangement calls for one.

<a id="manuscript-writing-rule-checks"></a>
### Common manuscript writing-rule checks

Writing self-checks and the writing part of an assigned manuscript review use this standard and procedure at their actual scope.
Check mathematical meaning, assumptions, object references, terminology, notation, definition and argument expression, citations and attribution, coherence, wording and actual human requirements under the applicable writing layers.
Apply the [modifier rule](#direct-results-and-modifiers) to each modifier's function in context, including noun modifiers and compound object names; preserve necessary mathematical distinctions and human choices rather than optimizing a word count.
Local work covers new, modified and adopted content and direct effects; requested whole-manuscript review requires actual whole-manuscript coverage.
Searches locate candidates and tools supply stated mechanical facts; reading rules, keyword matches, compilation, formatting and link checks do not replace contextual content judgment.

1. Determine the actual manuscript, responsible writer(s), requested scope and applicable choices, and whether the work is self-checking, assigned review or an already authorized recheck.
2. Read current source files and the mathematical, source, writing-choice and review evidence needed for the selected check.
   For review inputs, follow the relationship, purpose and reading order in the [manuscript review rule](#reviewing-a-manuscript).
3. Judge content and reader understanding in context, choosing necessary tool checks and direct consumers from the actual effects.
4. Distinguish required corrections, with their effective rule or concrete mathematical/source grounds, from optional suggestions with an expected reader or manuscript benefit; use the [problem-routing rule](records.md#mathematical-issues-and-reliance) and the record responsibilities above.
5. Act and recheck within the current role's authority, or deliver accurate findings and unfinished scope, reporting checking, correction and manuscript delivery as distinct facts.

Both uses include a reader-perspective rereading of explanatory passages in the checked scope.
If understanding their role requires a key mathematical relationship absent from the text and its explicit references, verify the relationship and its grounds.
The writer adds the necessary relationship within the writing authorization, and the reviewer records the needed correction in the selected manuscript's list.
If the relationship is unsupported or false, correct the associated assertion within authority or report the precise gap rather than inventing a connection.

| Actual change or deliverable | Necessary checks |
| --- | --- |
| Title or byline | Apply the [manuscript byline rule](#document-choices-and-final-review), including any applicable choice and preservation of an established byline in routine revision. |
| Local wording or expression | Mathematical meaning, object references and necessary context, without automatically repeating a whole proof review. |
| Terminology, notation, definition expression or TeX macros | Actual affected uses and consumers, including cross-section uses; a small character change need not have local impact. |
| Hypotheses, conclusions, proofs or a citation's mathematical role | Responsible mathematical/source materials, necessary dependencies and whether prior review still covers them, completing applicable correction and rechecking duties. |
| A built PDF for delivery | Build results from current sources, unresolved citations and cross-references, layout in the generated PDF and actual necessary inputs under the [build rule](#reproducible-local-builds); a source-only delivery follows its actual instruction and applicable build duties. |

Reuse a review while its inputs, reasoning and conclusions still apply; unrelated file or commit changes do not invalidate all review, and affected inputs do not retain coverage merely because an old verdict remains recorded.
Report build success, layout inspection, writing-rule review and mathematical scrutiny at their actual scopes without substituting one for another.
These checks add no checklist file, approval, state field or automatic agent stage, and grant no policy change, environment deletion, mathematical decision or extra research authority.
Required independent or fixed mathematical review retains its actual obligations; calling this same standard supplies no independent relationship.

<a id="manuscript-writing-rule-review"></a>
### Reviewing a manuscript

A human request or an applicable explicit review arrangement selects the current manuscript and the actual whole-manuscript, section or issue scope.
When the request and arrangement leave the review kind unspecified, review writing under the effective single-writer or joint-document choices in the four applicable layers.
For a request limited to proof, check that proof at the specified depth.
When both are requested, perform both checks in the same action and report their coverage separately.
Use the applicable review action for selected fixed Claims, Tasks, sources or computations.
See [Review specified work](../agent-actions.md#review-specified-work).

Determine the review relationship and purpose before selecting inputs.
Required independent writing review uses a reviewer outside substantive development of the reviewed exposition and structure, without inherited or shared substantive discussions or summaries of that development.
Apply the [proof review arrangements](proof-audits.md#review-arrangements) to independence from substantive proof development and its context.
When both kinds of independent review are required, determine qualification separately for each reviewed object.
The same reviewer may perform both when qualified for both, and an ordinary review may proceed directly under its actual arrangement.
For an independent initial review, form initial findings from the permitted current manuscript, actual human requirements and authorized scope, applicable rules and necessary dependencies before consulting existing opinions or prior conclusions in any form.
Compare earlier opinions after forming those findings and identify which evidence supports each part of the review.
For a targeted recheck, select inputs for the actual scope and review relationship and report the known findings and evidence used.

For writing review, apply the common checks and maintain the [selected manuscript's revision opinions](#manuscript-revisions).
Ground required opinions in the effective rule or actual mathematical or source issue and describe its specific effect.
Record a reviewer's preference as an optional suggestion.
For proof review, check the manuscript's hypotheses, reasoning and conclusions and record the scoped findings, evidence and limits in `review.md` or its adequate mathematical-review home.
See [Mathematical review evidence](#manuscript-review-and-mathematical-provenance).
When reviewing both, link a proof finding that requires manuscript revision from the corresponding opinion in `revisions.md` to its mathematical evidence.

Limit review-only writes to the selected review records and report any needed corrections to the text, writing policy, citation records or mathematical materials.
For mathematical errors or missing support, retain the precise problem and evidence locators for continuation within the actual authority over the responsible materials.
When the instruction also authorizes correction, carry out the authorized writing work and report inspection, correction and recheck separately with their actual relationships.
Complete the review assignment by delivering its findings, checked scope and limitations, including any unresolved opinions and their effect on manuscript conformity.

<a id="manuscript-revisions"></a>
### Current manuscript revision opinions

At the first actual writing review, establish or reuse one `revisions.md` for the selected manuscript in its own suitable or author-designated directory.
A paper can use `mathematics/manuscripts/Writer/Author_T_F0001/paper/revisions.md`, and a separately reviewed supplement uses its own directory.
Use one list for all sections of the same manuscript and keep common project materials in their existing project home.
Place new lists for independent manuscripts sharing a directory in dedicated manuscript subdirectories and identify the actual source in each list.
For independent TeX manuscripts `overview/main.tex` and `example/main.tex`, use `overview/revisions.md` and `example/revisions.md` respectively.
Included sections stay within their manuscript's list; supporting Markdown records acquire no manuscript-specific revision list merely from their extension or location.

If a valid single-manuscript list predates the shared directory use, identify the selected manuscript's unresolved opinions from the original manuscript, specific location and opinion content.
Until its dedicated list takes over, use those attributable opinions and necessary references at their existing location for writing, review and personal transfer.
When migration is needed, move only the selected manuscript's authorized unresolved opinions, maintain their necessary references and preserve the other content and uses of the old record.

Any manuscript move follows its actual writing authorization.
If `revisions.md` in the selected manuscript's directory serves another purpose, preserve that record in a suitable location and update its necessary references within actual authority before using the path.
Report the location conflict if the existing record's disposition falls outside that authority.
Refer to shared writing choices at their responsible homes and record only the action needed for the selected manuscript.

Use short ordinary prose to identify the current source file and section, environment label or recognizable wording, the concrete problem, effective rule or human requirement and necessary direction for correction.
Line numbers may help but are not the sole locator after edits; quote only enough text to locate the issue rather than copying the manuscript or its policies.
Group repeated instances of one issue with their actual scope, using a brief stable title or necessary evidence and limits when useful, without mandatory numbers, severity levels, status enums, dates, compliance tables or file fingerprints.
Mark required corrections and optional suggestions by their actual effect; an unadopted suggestion neither violates a rule nor independently blocks a correction task.

The currently assigned reviewer owns opinions, rulings and removal; the writer changes the manuscript and reports corrections through the normal reply.
Recheck directly when already covered by the human instruction or continuing review arrangement, not merely because a correction was submitted.
Reread changed text, applicable rules and necessary direct effects before updating unresolved portions or removing opinions actually resolved, withdrawn by an effective human choice or no longer applicable.
Do not close an opinion solely from the writer's "fixed" response or retain abandoned suggestions and closed-opinion history.
Limit recheck, cleanup and transfer to the actual manuscript selected and the authorized parts of its opinions and references.
When handling mixed legacy records within authority, move the selected manuscript's unresolved writing opinions to its own list and preserve other manuscripts' opinions, mathematical evidence and necessary references.
Keep only current unresolved items and facts needed for continuation.
When all opinions of the selected manuscript are resolved, clear its established list to zero bytes if it serves that manuscript alone and retain its entrance.
Report actual review coverage and unchecked limits normally; an empty file supplies no whole-manuscript verdict or independent qualification.

Necessary substantive evidence belongs at its [responsible mathematical or source home](records.md#mathematical-issues-and-reliance), with manuscript-side actions and exact links here rather than a duplicate proof or source-error account.
For mathematical manuscript scrutiny use `review.md`, for actual citation use `citation.md`, and for effective choices their existing home; revisions are no substitute Claim/Task assessment or sole evidence store.
Before removing an opinion containing uniquely needed mathematics or source evidence, preserve it under the [substantive-content rule](records.md#substantive-material-retention) and maintain necessary consumers, without archiving management history.
Keep unresolved substance and limitations, author rights, the [environment-deletion protection](#current-manuscript-authority) and actual research, Git and publication authority; writing or closing opinions does not change them.

## Reproducible Local Builds

Build each document from its own directory.
Record the actual engine, bibliography tool, relevant TeX distribution/package requirements, exact build command, working directory and any figure-generation step.
Do not mark a command tested until it has been run successfully.

Compile LaTeX directly in the directory containing `main.tex`, such as `paper/`, and keep its PDF and ordinary auxiliary files alongside the source.
Use the same output location for editor builds and command-line scripts.
Do not add `-outdir=build`, an equivalent output-directory override or a second synchronized reading copy unless the user explicitly authorizes an exception.
A standard command from that directory is `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.

Track `main.tex`, included TeX sections, `.bib` inputs, required source `.sty`/`.cls` files, editable figure sources and build configuration or scripts in appropriate source homes outside ignored `build/` and `figure/` trees.
Use relative paths and include or document every required input; avoid dependencies on absolute paths on one machine.
Give usable instructions for obtaining or regenerating required local images, and state an unavailable required input at the document home rather than claiming a successful reproducible build.
If documents share source files, keep those dependencies explicit and reproducible.
This convention applies to independently compiled LaTeX documents, including summaries and TeX supplements.
Page renders and other inspection artifacts may remain in an ignored `build/` subdirectory without making it a second TeX output location.

When migrating existing documents, retain usable current build conditions, truthful checked source revision and sections, actual results and continuing limitations.
Keep earlier commands or run facts at an adequate existing home only for necessary reproduction, evidence interpretation, actual comparison or current continuation.
Their execution, success or presence before migration alone creates no retention duty.
Remove obsolete build narration, repeated-run history and superseded check summaries without moving them to a README history appendix or another log.
Do not present an old successful run as a current build or a necessary historical fact as a current result.
Remove stored mathematical source/build/PDF digests and their retention obligations.
Verify a fresh build from current sources before cleanup of duplicate outputs; changing instructions alone does not establish a new successful build.
Before handing off a built manuscript, check compilation errors, unresolved citations and references, and layout problems in the generated PDF.
Record the result and source revision in the document README.
Fix substantive changes in the research records before updating their manuscript presentation; resolve typesetting issues in the manuscript sources.

### Computational Supplements and Independent Verifiers

A manuscript that depends on computational certificates carries in its supplement an independent, thoroughly commented, human-readable standalone verifier written for peer review.
The verifier re-derives the certificate conclusions from the paper's own statements and is self-contained.
The agent selects necessary publicly obtainable dependencies for mathematical suitability, reproducibility and peer-review use cost under the [computation-tool responsibility](computations.md#computation-tool-selection), without a package-category restriction.
Keep actual inputs, usable commands and relevant dependency information at the supplement's responsible home, with no repository-internal paths or internal IDs.
The verifier is part of the manuscript and is maintained and submitted with it.

The supplement verifier re-implements the argument rather than copying bytes.
Research scripts stay in `mathematics/computations/programs/<J>/` under the [computation rules](computations.md), and the two implementations evolve separately, with consistency shown by run results.
A computational supplement carries no manifest, retained verification-record requirement or frozen byte copies.
Its run products stay in the ignored `build/` workspace.
The supplement README or a paper appendix maps the paper's proposition and equation numbers to what each script verifies, how to run it and the expected output.
Certificate data, the machine-readable form of the paper's tables, travels with the manuscript attachment.

## Files Kept Local

Document PDFs and TeX compilation products stay local by default.
The responsible author may explicitly choose which manuscript or presentation PDFs are eligible for Git tracking in their applicable author-wide writing profile or more specific document choices under the [preference hierarchy](preferences.md#scope-and-adoption).
For joint writing, use an applicable shared document choice; without one, retain the common output exclusions rather than combine individual PDF exceptions.
That choice covers only the stated author, documents and PDF paths; non-PDF compilation products remain local.
Keep necessary editable figure sources, generation programs and reproducibility inputs in appropriate tracked source homes outside ignored workspace trees, and document how required local images are obtained or regenerated.

The [manuscript](../../mathematics/manuscripts/.gitignore) and [presentation](../../mathematics/presentations/.gitignore) collection ignore rules ignore files by default, keep directories traversable and admit `.tex`, `.bib`, `.sty`, `.cls`, `.md` and `.gitignore` source files.
Both `build/` and `figure/` directory trees at every document depth in `mathematics/manuscripts/` and `mathematics/presentations/` remain Git-ignored, including image resources regardless of extension.
Admit other necessary editable inputs, generation programs and build configuration through narrowly scoped negated paths in the document's local `.gitignore`.
For an actual author PDF choice, add only the selected PDF path to those local exceptions.
These exceptions must not reopen ignored workspace trees.
Do not change generic defaults into an all-author exception or force-add an output without an applicable author choice.
Read the actual responsible writer(s) and applicable single-writer or shared document choice before preparing files for delivery; extension and conventional directory alone do not decide permission.
Git ignore rules do not remove files already tracked, so inspect the selected filenames and correct accidental tracking without deleting needed local files.

TeX outputs and other generated file types remain ignored without an auxiliary-extension list.
Keep nonstandard inspection artifacts in an ignored `build/` subdirectory.
Another author-designated document home follows the same duty to exclude its `build/` and `figure/` trees and prepare its other applicable ignores before generation.
Personal PDF choices and document-local exceptions are outside common-framework copying.
The private literature/source-store exclusions remain unchanged and no author-document choice permits source-store publication.
Local compilation, PDF eligibility and source versioning do not authorize commit, push, journal submission or publication.

<a id="manuscript-review-and-mathematical-provenance"></a>
## Manuscript Review and Citation Records

For drafting and revision, the current working manuscript is authoritative for statements, notation, definitions, organization and proof exposition, subject to current explicit human instructions and the [current-manuscript rule](#current-manuscript-authority).
Read the current manuscript sources and direct mathematical and source inputs before deciding what the manuscript records must contain.

The existing project or document `review.md`, or its adequate mathematical-review home, records mathematical scrutiny of the current manuscript exposition.
Each retained review entry identifies the mathematical object and manuscript location, exact scope checked in the current sources, reviewer or review method and relationship, evidence consulted, actual findings or corrections, and unresolved points and limits.
These framework reviews describe actual agent inspection under the [review relationship and arrangement rules](proof-audits.md#review-arrangements); human authorship, suggestions and authorization are separate facts.
The current agent may directly undertake an ordinary or complete manuscript review without isolated context, another agent, a new Task or a fixed R solely for that review.
An explicitly required independent manuscript inspection meets the actual independent-context conditions, using the current reviewer directly when already qualified, while its findings retain their manuscript-local home.
An entry may review the complete written proof of an internal result whether or not an independent R exists.
A manuscript-local review does not replace fixed R evidence required by a separate Claim or Task acceptance workflow.
An audit of a fixed Claim does not automatically review its manuscript presentation.
Do not turn `review.md` into a build log, citation inventory, general prose-editing diary, fixed R review or substitute proof.
After a change, reconcile only the affected entries.
A scoped entry may remain while its reviewed text and conclusions still match the current authoritative manuscript; if the reviewed text has been superseded, review the current text and update the entry in place or remove it rather than retaining the former review as history.
Do not retain historical full-manuscript reviews or superseded-state summaries in `review.md`.
Before removing an entry, move any unique substantive mathematical result, argument, gap, counterexample or source finding to its responsible existing mathematical or source home under the [common content decision](records.md#substantive-material-retention).
Do not transfer administrative review chronology or add a deletion receipt.
Current build and layout facts belong in the document `readme.md`; do not retain historical build or visual summaries in `review.md`.

When mapping a current citation in `citation.md`, check whether actual source-inspection evidence covers the exact source edition and passages needed, and state any unresolved check honestly.
An adequate rolling U or complete relevant fixed C/L source account supplies this evidence at its existing responsible home, without copying, relocation or an extra U solely for citation.
Use the [first-work citation route](literature.md#3-citations-elsewhere-in-the-repository) for the actual original or adequate precise inspection evidence, retaining necessary selected original preparation and failure reporting for actual personal import or external intake.
Check its actual source edition, precise inspected passages, source statement or definition, hypotheses and normalization, inspection depth and unresolved limitations against the manuscript use.
A local result's proof status, a bare citation or a bibliography entry alone supplies no source-inspection evidence.
When an actual edition, passage or inspection gap remains, follow the existing [literature-acquisition](literature.md#literature-acquisition), [progressive-reading](literature.md#progressive-reading), and [source-audit](literature-audits.md#organization-and-stable-units) procedures for that gap and retain the necessary finding at its appropriate existing or new U or fixed C/L home under the [common content decision](records.md#substantive-material-retention).
U is the ordinary home for an independent reusable source-audit unit; an integrated project deduction or synthesis keeps its adequate C/L account and actual source/adaptation facts.
Acquisition-only work maintains necessary bibliography and useful edition/source notes without creating a source unit or acquisition account.
In authorized citation-map work, record every application actually cited in current TeX, linking adequate source evidence and applicable definition entries where available and keeping manuscript-specific applicability, claims, notation, terminology and gaps in the same citation map.
Uses sharing the same source, edition, mathematical role and hypothesis interface may share one applicability explanation with their actual TeX locations listed together, provided it covers the applicable conventions, representation conversions and inspection limits.
Distinguish different assumptions, editions, roles, adaptations and unresolved checks; an equal citation key or one verified use does not verify other uses.
Keep every actual use locatable and reuse sufficient source evidence without duplicating its inspection account for each occurrence.
Adequate source-inspection evidence is required before describing the application as verified or using it as established support at its claimed scope; adequate retained U/C/L evidence can suffice without a new local PDF.
If a source audit finds or checks a source not cited in the current TeX, retain any necessary finding at its responsible source-level home and do not add a `citation.md` entry.
Stylistic consultation and bibliography-only work follow the same source-preparation duties at their actual scope; only citations present in the current TeX receive citation-map entries.
It adds no approval step and does not broaden the source-audit scope required by existing literature rules.

The project `citation.md` maps every external citation use actually present in the current TeX, grouped by canonical citation key.
For a use supported by adequate source-inspection evidence, identify its manuscript claim or passage, TeX section and environment label or distinctive passage, source edition and precise inspected locator, relevant source hypotheses/normalization/setting and why they match, notation or terminology conversion, citation role and what it does not support, and the linked U unit or other exact source evidence with any unresolved point.
For unchecked or partially checked uses, plainly identify the actual TeX use, intended role, known edition/locator, evidence actually available, precise unresolved checks and resulting limitation.
Unknown edition, passage or evidence remains explicitly unknown; do not invent an inspected locator, U link, inspected hypotheses/normalization or completed applicability check.
Use ordinary authored descriptions without a new status enum or lifecycle, then update the same entry when the actual gaps are resolved.
Pending verification alone does not require deleting a draft citation and supplies no proof acceptance.
The map is not an inventory of consulted works or uncited bibliography entries.
Do not copy source-audit evidence into the map or make the map the sole inspection record.
Source-only facts and inspection limits stay at their responsible source-level home; project C/L content retains its own mathematical responsibility.
Fixed mathematical and source records must not point back to a manuscript or describe its manuscript-specific use.
Citation use grants no prose-reuse permission and does not adopt source style, terminology or conventions; keep choices in the applicable single-writer policy or document's existing `writing.md` or `conventions.md` under the preference rule.

When checking, adding, changing or removing a manuscript citation, reconcile `citation.md` within the current authorization to edit that record.
In review-only work, report citation discrepancies and needed corrections in the assigned review record.
The [record responsibilities](#project-and-document-records) and [common checks](#manuscript-writing-rule-checks) govern other affected records and review applicability without a per-task change log or no-op receipt.

## Manuscript Reference Boundary

Manuscripts may be revised freely and frequently.
Their project maps point forward to authoritative mathematics and source evidence.
Authoritative mathematical materials must not depend on mutable manuscript or presentation content in any author-designated writing home, including `mathematics/manuscripts/` and `mathematics/presentations/`, whether through links, paths, citations or ordinary prose.
This includes references to draft theorem, lemma or equation numbers, section or proof locations, and descriptions of how or where a mathematical input is used in a manuscript.
Do not retain manuscript-context explanations in external mathematical materials.

Preserve actual mathematical statements, necessary hypotheses, source conventions and review findings at their responsible Claim, source, ledger or other homes, and refer to those formulations.
Document-specific cross-references, source maps, writing choices and review accounts belong among the actual authored documents.
Writing-only context and navigation may connect related documents, including their stable project entrances, without creating a mathematical dependency or a new research Task.

From outside the actual writing home, only designated fixed entrance-navigation links may point into it.
Such links lead to the collection or stable project/document entrances without targeting or depending on internal sections, results, proofs, equations or review findings.
Ordinary mathematical records are not navigation entrances.

## Manuscript Index

`mathematics/manuscripts/index.md` manually links each project README and its independently compiled document entrances.
The project and document READMEs own goals, authorship, scope, source maps and document details.
The agent creating, retiring or changing a document updates only its affected navigation.

## Ambient Objects and Precise Operator Language

When introducing an operator or beginning an auxiliary operator argument, make its acting space and relevant operator algebra clear.
Distinguish membership in M from membership in B(H).
Specify the actual domain, representation, hypotheses and normalization when they affect the result.
Once explicit, the setup need not be mechanically repeated.
These mathematical clarity requirements apply without a personal profile; concrete presentation and wording preferences follow the applicable author, subfield and manuscript policies.

At each result or auxiliary argument, state the hypotheses it actually uses or give an unambiguous reference to an existing setup.
If results in the same section use different combinations of assumptions, make those differences explicit.
A common setup may remain where it applies throughout.
In a proof of an already stated theorem, its hypotheses need not be repeated in full.

<a id="mathematical-content-and-review"></a>
## Mathematical Content and Manuscript Review

Manuscripts present a coherent argument for readers who have not seen the exploration history.
Define the notation and hypotheses they need, give the proof or an appropriate precise citation, and distinguish proved results, conjectures, conditional statements and limitations using the [Claim rules](claims.md#separate-assessment-fields).
Internal record links alone do not replace a mathematical explanation in the paper.

Terminology, shorthand and presentation choices that originate in internal research materials, source notes or audits are exploration vocabulary.
They acquire standing in a manuscript only when its writing layers adopt them, and they are never attributed to a cited source.

Claim materials own project statements and actual arguments.
Formal project-mathematics review findings of every agent relationship belong to fixed R under [proof-audit rules](proof-audits.md); L retains discussion and ordinary local checks, and manuscript-local reviews retain their document responsibility.
For manuscript evidence, citation applications and revision opinions, use their distinct [responsible records](#project-and-document-records) rather than treating every review as mathematical scrutiny.
When writing or review discovers a substantive argument, changed hypothesis or mathematical error, use the [object-based routing rule](records.md#mathematical-issues-and-reliance), maintaining the responsible mathematics and applicable assessments before adopting the change in the manuscript.
Preserve necessary mathematical evidence, source facts and actual review scope under the existing repair/version duties.

Internal extraction of reusable results within an assigned Task is autonomous under the [Claim organization policy](claims.md#lemma-extraction-and-approval).
Main-theorem designation and objective changes retain their actual authorization boundary.
A manuscript organization proposal is not an implemented designation.
When an approved revision introduces a lemma-based proof, preserve the original complete Claim argument, identify the new proof version and update the manuscript provenance map to the version actually used.
This does not require retaining duplicate current TeX documents.

Use the [truthful-scope](#truthful-review-scope), [common-check](#manuscript-writing-rule-checks) and actual mathematical-review requirements for claims about a manuscript's review and coverage.
Manuscript preparation does not reopen a completed research goal merely because writing or formatting remains.
A mathematical Task's contract and completion criteria cover its mathematical objective and necessary review under the [Task rules](tasks.md#task-records).
Manuscript preparation, whole-manuscript review, builds and delivery follow the actual writing instruction and are not mathematical Task completion criteria.
When the human requests both a mathematical result and a manuscript, complete and report each assignment at its actual scope.
Mathematical Task completion does not finish that whole instruction while writing remains; unfinished writing does not prevent completion of a Task whose mathematical contract and necessary review are satisfied.
Creating `mathematics/manuscripts/` assigns no new goal, manuscript or publication task.
