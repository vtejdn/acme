# Mathematical Manuscript Writing Rules

Apply the [common sentence-oriented source layout](organization.md#sentence-oriented-source-layout) to maintained prose, preserving mathematical and typesetting structure.
This shared format rule does not change the writing-choice hierarchy.

Apply these general mathematical writing rules and the responsible author's author-wide, applicable subfield and manuscript-specific choices under the [four writing layers](preferences.md#scope-and-adoption) to all maintained natural-language prose under [mathematics/manuscripts/](../../mathematics/manuscripts/), not only prose compiled into TeX.
This includes project and document `readme.md`, `writing.md`, `conventions.md`, `organization.md`, `review.md`, `citation.md` and prose in TeX sources; it governs terminology, notation and style in those records without changing their evidence, scope, findings or file responsibilities.
Structured metadata, BibTeX fields, formulas, code, exact source quotations, acquired originals and generated outputs retain their native or responsible rules, while prose surrounding them remains governed by these writing rules.

These general defaults apply to mathematical accuracy, necessary assumptions and conventions, logical justification and truthful attribution.
Follow the [project and document requirements](#projects-and-documents) and the [four writing layers](preferences.md#scope-and-adoption) for the responsible author's actual choices.
An author without a profile uses these general standards and any explicit manuscript choices; no other author's defaults are inherited.

The [definition index](../../mathematics/definitions/index.md) locates responsible mathematical definitions.
Canonical [references.bib](../../mathematics/literature/references.bib) owns shared bibliographic fields; local `mathematics/literature/registry.md` owns machine-local acquisition and artifact facts; U and source audits own inspected edition, passages and actual inspection scope.
Source observations in responsible source records are evidence, not an additional policy layer.
Keep a manuscript's choices at its existing [writing-choice home](#document-choices-and-final-review).

## Projects and Documents

Use one manuscript project per user-defined research goal by default, named by its assigned local Task family, such as `Author_T_F0001/`.
Another human's ordinary Task/E authority and manuscript projects are outside mathematical intake; own selected manuscripts may use [personal import](intake.md#personal-import).
Use the actual author-designated line and numeric serial from the [Task index](../../mathematics/tasks/index.md).
Omit a physical-version or topic suffix from the project root and put its title in the README.
Create a project when manuscript work is needed within the user's authorized scope; a recorded goal does not require an empty manuscript project.

A user may explicitly designate another home or directory name for a talk or presentation.
Preserve that choice and apply the same author, source, writing, build and review responsibilities there; a presentation does not require a new Task merely to obtain a Task-named directory.
For a [same-author Task transfer](intake.md#task-and-manuscript-collection), include its actual corresponding manuscript project by default, identifying that relationship from the project ownership, description and delivery purpose rather than a matching directory number.
After the Task pass, independently trace the manuscript's actual statements, proofs, definitions, computations and reviews to necessary support families, U and bibliography, adding inputs the Task pass missed.
Include the project's actual papers, supplements and research notes, project/document READMEs, main files, sections, bibliography, necessary figures, styles, other build inputs, writing choices and real review records.
Documents genuinely belonging to that project are within scope; unrelated projects remain outside it, and an explicit narrower human selection takes precedence.
Merge both passes without duplicate support or another copy of a shared manuscript.
If no corresponding project exists, create no empty directory or placeholder.
Own manuscript import uses an appropriate existing or designated receiving home without creating an unrequested Task.
Preserve document choices and actual review scope, adapt entrances and build paths, and run proportionate affected local build checks without treating a source build as a successful receiving build.
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
      main.pdf               # Generated output; ignored by default.
    supplement/
      readme.md
      main.tex
      main.pdf               # Generated output; ignored by default.
```

The document directory is the unit of compilation.
Files included with `\input` or `\include` are sections of that document and need no separate document directory.
A separately compiled supplement has its own directory; an appendix included in the paper belongs with the paper.

Keep the goal ID stable when the manuscript title changes.
If one manuscript draws substantively on several goals, choose one primary project and link the other goals with a brief explanation in its project README.
Do not duplicate the same manuscript under several goal directories.

<a id="project-and-document-records"></a>
## Project and Document Records

The project `readme.md` records the responsible human author, authorized local Task, primary goal, supporting goals and document entrances.
It gives a compact mapping from principal manuscript result labels to the authoritative mathematical arguments, responsible records and applicable proof reviews.
Expand the mapping only when a new substantive result needs its own provenance.

Each document's `readme.md` records its purpose and entry file, compilation instructions, required local inputs, and the latest build and manuscript-review evidence.
Link actual editorial choices from their existing conventions or designated writing-choice home.
Do not invent a model, fallback or extra adoption requirement for an author who has not chosen one.

The project or document's existing `review.md` records actual mathematical scrutiny of the manuscript's statements, hypotheses, proofs and inferences.
The manuscript's `citation.md` records actual external citation uses and links to their responsible source evidence.
Neither record replaces the current TeX, fixed mathematical/source evidence, canonical bibliography or manuscript-specific writing choices.

Task and Claim materials own mathematical decisions.
The canonical bibliography owns bibliographic fields.
The literature registry owns acquisition and artifact facts.
These records may be short.

Describe ignored output paths as inline code rather than permanent Markdown links because those files will not exist in a fresh clone.
Link to the tracked source directory and build instructions instead.

<a id="current-manuscript-authority"></a>
## Authority of the Current Manuscript

For manuscript drafting and revision, subject to the current explicit human instructions, the current working manuscript is authoritative for its content, notation, definitions, organization and proof exposition.
Read the relevant current sources before editing.
Memory, conversation summaries, earlier drafts, plans and historical review records may help locate context, but must not overwrite or revert content already updated in the current manuscript.
Check recalled formulas and choices against the current sources, and synchronize affected writing-choice and planning records when they lag behind the current manuscript or the human's new instruction.

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
**Make direct relationships between results explicit.**
When a theorem, proposition, lemma, corollary or remark directly applies, specializes, extends, compares or explains another result, identify that result and the relationship when introducing the statement, at the start of the proof, or at the step where it is used.
State the relevant hypotheses or substitution when needed to make the application clear.
Keep these explanations concise and avoid repeating a relationship already made explicit.

<a id="mathematical-comparisons"></a>
**Specify the aspect and strength of a mathematical comparison.**
When comparing results or formulas, identify whether the comparison concerns hypotheses, conclusions, variables and domains, expressions or proof methods.
Distinguish equality of extremal values, pointwise equality of expressions, changes of variables, inclusion of applicability domains and logical implication.
Where needed, support the comparison with explicit correspondences, equalities, inequalities or counterexamples; vague assertions of sameness, equivalence or relatedness do not replace an argument.

<a id="definition-environments"></a>
## Presentation of Definitions

Apply the responsible author's and manuscript's choices for definition environments, numbering, explanatory detail and audience.
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
The local `mathematics/literature/registry.md` owns this machine's acquisition, artifact/version and access facts, independently of shared manuscript evidence and review.
Role adoption and source observations link to those responsible materials.
Stylistic consultation and bibliography-only work follow the same source-registration and factual-processing duties, with inspection proportional to the actual use.

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

Before relying on needed literature, search existing definitions and source evidence, register any missing work in the canonical bibliography and its actual artifact/version in the registry, then inspect the needed passages.
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
The local literature registry owns this machine's acquisition and artifact/version facts; inspected editions, passages, findings and limits stay at their shared U/L or other adequate responsible home.
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
When a check corrects the current text, record that finding truthfully in the current review entry rather than retaining the superseded review as history.
No additional policy engine or per-term register is required.

## Document Choices and Final Review

Read the actual author, relevant subfield and manuscript choices before writing or revising.
Keep a choice at its responsible scope without duplicating it in a second location.
Keep manuscript-specific writing choices in the project's existing `writing.md` or `conventions.md`.
Keep selected mathematical content and order in `organization.md`.
Keep project identity, Task and document entrances, and the concise mathematical provenance map in the project `readme.md`.
Keep document purpose, source inputs, build instructions and latest build evidence in the document `readme.md`.
Keep manuscript-review findings and their limits in the existing `review.md`, and current external citation applications in `citation.md`.
Mathematical proof review and build/layout facts remain separate from personal presentation preferences.
Adopting these rules does not itself select a theorem or rewrite an existing manuscript.

<a id="writing-rule-execution"></a>
Manuscript drafting and revision have the following execution and completion requirements:

1. Before starting or resuming, the writing agent must determine the requirements applicable to the requested content and scope under the current human instructions and the four writing layers, and use them to make writing decisions.
   Reading rule files alone does not fulfill this obligation.
   Usage inherited from a draft or source, and the agent's own preferences, do not by themselves justify departing from an applicable rule.

2. Before reporting a drafting or revision task complete, check new and revised text and directly affected content against the applicable writing rules.
   Check mathematical meaning, object references, hypotheses, notation, citations and level of exposition as relevant to the change.
   As part of this review, assess each modifier's function in its sentence under the [modifier rule](#direct-results-and-modifiers), including noun modifiers and compound object names, and remove unnecessary wording while preserving mathematical meaning and clear references.
   Keyword searches can locate candidates but do not replace contextual judgment; no separate word blacklist or per-modifier register is required.
   Text adapted or adopted from earlier drafts or sources is included.
   Local work requires checks of its changes and direct effects; a requested whole-manuscript check requires that coverage.
   Compilation, formatting and link checks do not replace this review.

3. Correct violations found within the authorized scope before delivery and recheck the affected content.
   If a rule conflict, missing support or another concrete obstacle remains unresolved, state the issue, its effect and the resulting limit on the deliverable's status.
   Do not substitute reading the rules, pointing to an existing rule or a successful build for resolving a known violation.
   Do not report the requested revision complete while known violations within its scope remain unresolved.

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

When migrating existing documents, preserve useful historical build commands, checked revision/sections and actual run results.
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
That choice covers only the stated author, documents and PDF paths; non-PDF compilation products remain local.
Keep necessary editable figure sources, generation programs and reproducibility inputs in appropriate tracked source homes outside ignored workspace trees, and document how required local images are obtained or regenerated.

The [manuscript](../../mathematics/manuscripts/.gitignore) and [presentation](../../mathematics/presentations/.gitignore) collection ignore rules ignore files by default, keep directories traversable and admit `.tex`, `.bib`, `.sty`, `.cls`, `.md` and `.gitignore` source files.
Both `build/` and `figure/` directory trees at every document depth in `mathematics/manuscripts/` and `mathematics/presentations/` remain Git-ignored, including image resources regardless of extension.
Admit other necessary editable inputs, generation programs and build configuration through narrowly scoped negated paths in the document's local `.gitignore`.
For an actual author PDF choice, add only the selected PDF path to those local exceptions.
These exceptions must not reopen ignored workspace trees.
Do not change generic defaults into an all-author exception or force-add an output without an applicable author choice.
Read the actual responsible author and their selected preference before preparing files for delivery; extension and conventional directory alone do not decide permission.
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
Read the actual TeX and direct mathematical/source inputs before deciding what the manuscript records must contain.

The existing project or document `review.md` records mathematical scrutiny of the current manuscript exposition.
Each retained review entry identifies the mathematical object and TeX location, the exact scope checked in the current working-tree TeX, the reviewer or review method and relationship, the evidence consulted, actual findings or corrections, and unresolved points and limits.
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

When mapping a current citation in `citation.md`, check whether fixed source evidence covers the exact source edition and passages needed, and state any unresolved check honestly.
An adequate fixed U or complete relevant C/L source account supplies this evidence at its existing responsible home, without copying, relocation or an extra U solely for citation.
Use the [first-work citation route](literature.md#3-citations-elsewhere-in-the-repository) for the actual original or exact fixed inspection account, preserving the required prior acquisition outcome and failure report for newly received U.
Check its actual source edition, precise inspected passages, source statement or definition, hypotheses and normalization, inspection depth and unresolved limitations against the manuscript use.
A local result's proof status, a bare citation or a bibliography entry alone supplies no source-inspection evidence.
When an actual edition, passage or inspection gap remains, follow the existing [literature-acquisition](literature.md#literature-acquisition), [progressive-reading](literature.md#progressive-reading), and [source-audit](literature-audits.md#organization-and-stable-units) procedures for that gap and retain the necessary finding at its appropriate existing or new fixed U/C/L home under the [common content decision](records.md#substantive-material-retention).
U is the ordinary home for an independent reusable source-audit unit; an integrated project deduction or synthesis keeps its adequate C/L account and actual source/adaptation facts.
Acquisition-only work retains its bibliography/registry responsibility without creating a source unit.
Record every application actually cited in current TeX, linking adequate fixed evidence and applicable definition entries where available and keeping manuscript-specific applicability, claims, notation, terminology and gaps in the same citation map.
Adequate fixed source evidence is required before describing the application as verified or using it as established support at its claimed scope; adequate retained U/C/L evidence can suffice without a new local PDF.
If a source audit finds or checks a source not cited in the current TeX, retain any necessary finding at its responsible source-level home and do not add a `citation.md` entry.
Stylistic consultation and bibliography-only work follow the same source-preparation duties at their actual scope; only citations present in the current TeX receive citation-map entries.
It adds no approval step and does not broaden the source-audit scope required by existing literature rules.

The project `citation.md` maps every external citation use actually present in the current TeX, grouped by canonical citation key.
For a use supported by adequate fixed evidence, identify its manuscript claim or passage, TeX section and environment label or distinctive passage, source edition and precise inspected locator, relevant source hypotheses/normalization/setting and why they match, notation or terminology conversion, citation role and what it does not support, and the linked U unit or other exact source evidence with any unresolved point.
For unchecked or partially checked uses, plainly identify the actual TeX use, intended role, known edition/locator, evidence actually available, precise unresolved checks and resulting limitation.
Unknown edition, passage or evidence remains explicitly unknown; do not invent an inspected locator, fixed U link, inspected hypotheses/normalization or completed applicability check.
Use ordinary authored descriptions without a new status enum or lifecycle, then update the same entry when the actual gaps are resolved.
Pending verification alone does not require deleting a draft citation and supplies no proof acceptance.
The map is not an inventory of consulted works or uncited bibliography entries.
Do not copy source-audit evidence into the map or make the map the sole inspection record.
Source-only facts and inspection limits stay at their responsible source-level home; project C/L content retains its own mathematical responsibility.
Fixed mathematical and source records must not point back to a manuscript or describe its manuscript-specific use.
Citation use grants no prose-reuse permission and does not adopt source style, terminology or conventions; keep those choices in the responsible author policy, `writing.md` or `conventions.md`.

After every writing or review task, reconcile `review.md` and `organization.md` with the affected current TeX and update them only when their scope, evidence, findings or summary needs to change.
Reconcile `citation.md` after any task that checks, adds, changes or removes a manuscript citation.
This is a current-content check, not a per-task change log or no-op receipt.
A style-only edit, build, link check or citation-formatting check is not mathematical review.

Drafting that discovers a substantive mathematical change updates its responsible mathematical material before adoption.
Neither a successful build nor a manuscript-local verdict supplies a fixed mathematical review for Claim or Task acceptance.

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
Manuscript-specific reviews belong in the reviewed document README or an established project/document `review.md`, including independent manuscript reviews.
Actual manuscript citation applications belong in `citation.md`; source-inspection evidence remains at its adequate responsible fixed U/C/L home.
When drafting discovers a new substantive argument, changed hypothesis or mathematical error, update the responsible research record and assessment, then synchronize the manuscript.
Preserve the affected mathematical history and review scope.

Internal extraction of reusable results within an assigned Task is autonomous under the [Claim organization policy](claims.md#lemma-extraction-and-approval).
Main-theorem designation and objective changes retain their actual authorization boundary.
A manuscript organization proposal is not an implemented designation.
When an approved revision introduces a lemma-based proof, preserve the original complete Claim argument, identify the new proof version and update the manuscript provenance map to the version actually used.
This does not require retaining duplicate current TeX documents.

An audit of a Claim argument does not automatically review its manuscript presentation.
Before describing a manuscript as reviewed, compare its exact statements, assumptions, proof steps, citations and scope with the reviewed inputs.
Record the checked source revision and any remaining issues.
A successful TeX build is a separate fact from mathematical review.
Manuscript preparation does not reopen a completed research goal merely because writing or formatting remains.
The original goal contract determines whether manuscript delivery is a completion requirement.
Creating `mathematics/manuscripts/` assigns no new goal, manuscript or publication task.
