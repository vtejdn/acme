# Repository Organization

Locally authored research records, framework rules, reports and code comments use English by default.
Official non-English human-facing translations maintained alongside their responsible originals are permitted in any language and explain the same framework without becoming a competing rule authority.
Existing Chinese guides retain that role; planned German, French, Japanese and later editions gain navigation entries only when their actual files are added.
An arbitrary non-English research note is not an official translation.
Other explicitly authorized document-language scopes retain their actual instructions and role boundaries; original quotations and acquired material retain their source-preservation rules.
Directory names use short lowercase English words without spaces; registered citation keys keep their case.

The root README is an entry point.
`framework/` owns portable rules/templates, `repository/` owns repository identity and human registration, `profiles/<human>/` owns applicable personal choices, and `mathematics/` owns research.
`execution/` is persistent local state, ignored by Git and excluded from framework copying and temporary cleanup; prepare a stable E only for an ordinary Task actually selected for local execution.
Its on-demand runtime notes have a separate [machine-local purpose](#machine-local-runtime) and create no Task or E.
Joint coordination Tasks have no E, and destination execution state is preserved when copying framework files.
`intake/<initiator>/` holds concise operation provenance.
Classified runtime tools belong in `scripts/acme/`, with thin command entries in `scripts/`.

Keep `mathematics/readme.md` as a short, stable directory entrance to Tasks, Claims, strategies and their responsible materials.
It carries no rolling cross-Task progress narrative or refresh/completion-edit duty.
An index is needed only to navigate a growing collection of actual research materials.
For such a collection, the directory readme explains its purpose, governing rules and use, while the index locates the actual materials.
Reuse an adequate responsible catalog instead of adding another list of the same objects.
Fixed framework, rule, function, configuration and profile explanations, readme-only or single-document directories and rolling drafts need no index.
A growing presentation collection uses the root and actual-author readme/index pairs, while an individual document readme keeps its substantive content; neither arrangement requires an index in every directory.
Indexes confer no mathematical, review, lifecycle or execution authority.
No directory classifier, exhaustive directory register or mandatory index in every folder is introduced.
A directory's existence alone requires no README; create one only for a distinct necessary purpose, keeping operative rules at their governing framework homes.
Live readings and execution disposition belong in E, with actual defaults selected by the [personal-policy rules](preferences.md).

Do not duplicate authority: current assessments live in exact Claim/Task decisions; statements and proofs in their materials; reviews in audit records; shared bibliographic fields in mathematics/literature/references.bib and machine-local acquisition/artifact facts in its local registry.md.
Machine-local paths and secrets are not framework defaults.
Link the responsible record when summarizing it.

## Sentence-oriented source layout

Write maintained natural-language prose with one complete natural sentence per physical source line by default.
Start the next complete sentence on a new line.
For a sentence that is too long for comfortable source reading, break after suitable existing punctuation and keep that punctuation on the preceding line.
Choose breaks from the actual sentence and logical relationship, without changing words, adding punctuation or dividing an indivisible expression.
Do not wrap at an arbitrary column, word or citation boundary; there is no mandatory character count.
This concerns saved physical lines, not an editor's visual soft wrapping.

A single source newline normally continues the same paragraph; a blank line separates paragraphs.
Preserve paragraph boundaries, explicit hard breaks and language-specific whitespace.
The rule applies to framework documentation, research prose, mathematical statements and proofs, reviews, manuscripts and explanatory list bodies.
Preserve hypotheses, quantifiers, argument relationships, decisions, review scope and attribution.
Substantive changes follow their own authorization, version and review rules.

- Keep inline mathematics, code, commands, citations, link targets and other indivisible expressions intact.
  Surrounding prose still follows the sentence rule.
- Displayed mathematics follows its mathematical and typesetting structure.
  A formula can complete a sentence introduced by surrounding prose; preserve its punctuation and logical connection.
- Programs, fenced code, verbatim regions, comments, string literals and structured data follow their native syntax.
  Authored prose outside these regions follows this rule.
- Headings, short labels, declared fields, bibliography entries, link definitions and Markdown table rows retain their structure.
  Do not break a row or use a structural container merely to avoid prose layout.
- List continuations retain indentation and item boundaries.
  Preserve Markdown hard breaks, HTML structure, TeX comments, command boundaries and meaningful whitespace.
- Authorized receiving preparation follows the common [adaptation rule](records.md#receiving-and-adapting-selected-content), preserving necessary mathematics, human authorship and actual provenance without source-format or whole-copy constraints.
  Faithful quotations or transcriptions retain necessary source layout; local introductions and commentary follow this rule.
  Generated numerical output and third-party formats are outside prose migration.

Every editing agent, including a coordinating agent, inspects the actual new or changed prose before delivery.
Check sentence and paragraph boundaries, suitable punctuation breaks and the relevant document syntax.
Role permissions still apply; this rule does not grant access to another role's protected documents.
Encode chosen sentence boundaries directly in templates and prose-producing writers.
Mechanical tools may apply explicitly chosen line changes, but cannot decide sentence completeness or mathematical equivalence.
Do not introduce a sentence parser, punctuation splitter, semantic layout linter, compliance register or approval step.
Neither a passing tool nor a newline-only diff establishes preserved meaning.

<a id="machine-local-locators"></a>
## Durable locators and private setup

Use repository-relative program/data paths and document-relative links in durable public content.
Obtain the actual checkout root from runtime context; do not hardcode it or add a second root setting in secrets.
Private settings and local original holdings remain local and do not travel through normal Git collaboration under the [default collaboration scope](identity.md#collaboration-maintenance-and-conflicts).
The same boundary covers `mathematics/literature/registry.md`: keep actual local bytes, omit it from source framework copying and preserve a destination's actual local account.
Do not create or restore an empty registry during installation, cloning or bibliography-only work; ordinary framework copying changes no Git metadata.
When authorized maintenance ends tracking of an existing account, retain its local bytes and any necessary unique shared evidence at its adequate existing home before repairing consumers and using native Git for that exact path.
This does not rewrite history, adopt another author's holdings or create a migration register.
Do not assume another human's private settings or private originals exist in the current human's local working copy.
Credentials, sensitive access parameters and private resource locators belong only in the responsible human's existing ignored `profiles/<human>/secrets.md`, under a concise resource section; nonsensitive runtime choices use the [runtime home](#machine-local-runtime).
Public guidance names that file/section in inline code and any relative suffix; it does not copy the private value or link to the private file.
A public Markdown link to a private profile file is a public-document error: use inline-code lookup instructions instead.
Classify the normalized, decoded target before opening its contents or checking an anchor, with the same diagnostic whether the private file exists, is absent or cannot be decoded.
Public references to the local literature registry follow that same access-before-reading refusal; name its lookup path in inline code and use shared bibliography, contents or U for shared source facts.
Read only the needed private section when an actually authorized resource-dependent operation uses it.
Missing setup limits that resource-dependent work, without blocking unrelated work or creating a new permission gate.

Source PDFs keep the logical `mathematics/literature/pdf/` entrance and flat filenames.
The entrance is an ordinary directory or one top-level directory junction, and its files remain local only, excluded from Git/GitHub and cross-repository intake.
Original HTML and explicitly retained related files use contained canonical work-key groups under the same entrance, following the [source-storage rule](literature.md#original-html-sources).
General traversal, copying, publication and cleanup skip the whole source mount; group access does not make it a C/T/J output home.
A needed durable external mount target belongs only in private setup.
Concrete source operations use real paths for resolution, containment and junction checks; generic public links retain logical source navigation without resolving or reading the mount.
Local navigation rejects Windows source-prefix/ancestor and protected-component aliases before target access under the [source rule](literature.md#local-pdf-storage); normal material operations inspect their actually selected paths without resolving an unselected source root.
Fixed Git names, source URIs and recorded original paths retain their literal identities, independently of local Windows refusal rules.
An acquisition record's local paths belong to that record's repository and selected view; reading it from fixed Git does not select the same-named physical checkout objects.
Necessary fixed inputs use their selected ordinary Git entries and blobs, while actual local source and receiving operations retain containment, reparse, occupation and stale-input checks.
Do not serialize host values into public reports.
General public traversal and common-framework copying exclude `profiles/*/secrets.md` before reading; a deliberately tracked/staged secret is a publication error.

Record relative commands and the runtime/dependency details that affect actual reproduction, instead of installation paths.
The [computation rule](computations.md) gives no generic execution-environment archive duty.
Normalize historical installation/root portions while preserving necessary relative suffixes, program/argument identity, dates, outcomes, parameters, payloads and limitations;
identify normalized commands as such, without claiming a new run or literal original argv.
Discard obsolete host locations without creating a secrets inventory.
Public URLs/DOIs, original source identities, actual locally computed literature-file fingerprints, quoted source text, fictional controls, mathematical notation and agent names retain their actual roles.
Locator cleanup does not rewrite Git history or weaken fixed-mathematics preservation.

<a id="machine-local-runtime"></a>
## Machine-local runtime notes

Installation, initialization, environment probing or a successful local command does not authorize adding this machine's interpreter, virtual environment, OS or system-software versions, installation status or tool locations to the root README, AGENTS, common framework rules, shared configuration or other public entrances.
Relative paths and nonsensitive values remain machine choices rather than portable requirements.
Maintain actual framework runtime requirements in the responsible public tool documentation from implementation and verification; one machine's version or failed interpreter supplies no minimum-version rule.
Preserve project prose and genuinely portable reproduction requirements when adapting an actual machine-specific paragraph, rather than replacing a whole README or scanning the library for keywords.

Use `execution/runtime/readme.md` only when this working copy has a continuing need to retain nonsensitive runtime choices, tool entrances, necessary commands and actual limits.
Reuse the ignored, persistent execution directory without synchronization, placeholders, a machine identifier, fixed fields or an environment inventory.
Organize concise notes by actual purpose and state necessary command working directories, obtaining the repository root from runtime context without a second root setting.
Native Git configuration, checkout binding, environment metadata and dependency files keep their existing homes; runtime notes do not mirror them or private resource values.
Literature acquisition accounts, E conditions and personal research or writing choices likewise retain their own responsibilities.

The actual virtual environment belongs to `.venv/` and its native environment tools.
An optional `.venv/readme.md` is only an environment-specific explanation when one is needed, not a required file or the sole durable home for necessary choices.
Avoid duplicate facts in it and runtime notes; before an authorized environment removal or rebuild, retain any still-needed information at runtime or another adequate home.
No environment or note is created merely to fill a directory.
Keep portable dependencies, build inputs and tool conditions that affect mathematics, results or reproduction at J, the manuscript or another responsible public material, rather than hiding them in local notes.

At actual tool use, reuse sufficient available capabilities and read only the relevant runtime notes and needed private resource section.
Direct invocation of a selected interpreter is sufficient when suitable; activation, a new environment, a complete inventory and a fixed preflight sequence are not prerequisites.
Missing notes are normal, and a resource failure limits the affected work without authorizing a system installation or blocking independent authorized work.
Maintain a continuing choice or repair a stale entrance only when needed, without probe history, routine timestamps, fingerprints or duplicate accounts.
Temporary diagnostics and installation output use the normal reply or existing temporary storage and creator cleanup, rather than becoming runtime history.
Move a duplicated nonsensitive choice from private setup only when actually maintaining that item, without a bulk private-file migration.

Creating or maintaining runtime notes is local setup or maintenance, creates no Task/E and grants no research start, resumption or allowance.
E keeps its flat Task-family address and selected check; runtime is not E and is not recursively validated with it.
Local cleanup handles the selected notes or environment, preserving neighboring E files and their effective stops and limits rather than clearing execution/.
Installation, upgrades, framework copying and default material transfer exclude the source's entire execution/ and .venv/ while preserving the destination's E, runtime and environment.
A new clone normally lacks these local files; prepare actual resources rather than restoring another machine's settings from Git or a sending worktree.
An explicitly authorized personal backup or move uses ordinary selected file operations, without an environment synchronization or relocation mechanism.

Public lookup guidance uses inline-code paths; public links into execution/runtime/ or to .venv/readme.md are refused by normalized role before target resolution, existence, contents or anchors.
This public-reference boundary leaves explicitly authorized local reading available and does not turn every ignored path into a prohibited byte target.

## Material Responsibilities

Before selecting or creating C/J/R/L/U or another mathematical/evidence home, apply the [common content decision](records.md#substantive-material-retention).
Reuse adequate existing content, preserve unique necessary mathematics and evidence, and remove redundant routine process only after consumers are coherent.
Directory organization and valid links do not establish this content judgment.

Strategies own the current mechanism, optional parent, allocation and route lessons.
Reusable arguments, failed findings and reviewed constructions remain in their responsible mathematical materials.
Search and cite these by the actual conclusion and applicability; no separate method type or mandatory feedback workflow is used.

Retained computation programs, verification programs, required original inputs and concise accounts use `mathematics/computations/programs/<J>/` under the [computation rules](computations.md).
Generated results, certificates and verification data use the Git-ignored `mathematics/computations/outputs/<J>/`.
Both homes preserve the same registered J identity, including receiving authorN/repoN and the established receiving serial for acquired groups.
The collection entrance/index remains at `mathematics/computations/`.
The program README supplies navigation, actual input/output locators and reproduction context, without a second assessment or review.
Generic discovery and common-framework copying skip live output; explicit contained reads and selected transfers remain available.
Keep logs only for troubleshooting and checkpoints only for useful continuation, preserving necessary mathematics and consumers before cleanup.

Source inspection belongs in mathematics/audits/literature/.
Project Claim statements, selected assessments and arguments belong in C: select the actual reasoning in the same or another applicable fixed C.
L retains exploration, useful failures, comparisons, syntheses and ordinary checks needed for that discussion; important substantial arguments belong in C and formal project-review findings of every agent relationship belong in R.
Independent project-review accounts belong only in fixed R under mathematics/audits/reviews/, with exact inputs, scope and relationship.
Source U inspection supplies no adopted project-proof review.
All L materials live in mathematics/ledger/, including literature-related L.

The canonical bibliography is mathematics/literature/references.bib.
Definition entries point to authoritative formulations under the definition rules.
Manuscript sources use mathematics/manuscripts/Author_T_SERIAL/<document>/ under an authorized local Task, with the actual author-designated line and serial.
An explicitly user-designated talk or presentation home preserves its actual path and follows the same writing, source, build and review duties without requiring a new Task or research identity.
Document navigation may connect related writing, while authoritative mathematical evidence remains independent of mutable writing outputs in every such home.
Own Tasks and selected manuscripts use personal import; intake excludes another human's ordinary Task/E authority and manuscript projects, with a narrow necessary joint-contract exception.
Project titles belong in the README.
Link to the responsible claims and reviews.
Their writing choices do not change those assessments.

Writing choices follow the [four-layer hierarchy](preferences.md).
Source observations remain in adequate U or compact source-reading accounts; complete U/C/L definitions are registered through the concept index, and manuscript-specific choices stay with the manuscript.

## Material maintenance worklist

The sole rolling coordination document for the [three local material maintenance actions](records.md#local-material-maintenance) is `mathematics/maintenance.md`.
Create it only when actually needed, with no mathematical material number, template, empty initialization placeholder or extra Task/E.
In a Git repository it is normally tracked and synchronized with the related authorized material work; personal use without Git remains local and requires no Git initialization or remote setup.
Installation, upgrades and framework copying preserve the destination's existing worklist and contents, exclude the source's live worklist and never overwrite issues with an empty template.
Once established, the file remains at zero bytes when all issues and necessary continuation scope have been resolved; its contents and cleanup follow the responsible record rule rather than a second assessment or evidence account.

<a id="temporary-storage"></a>
## Temporary Operational Storage

Use only root `.tmp/` for repository-managed disposable operational work; root `tmp/` is retired.
Create a purpose-specific child only when needed.
Permitted uses include isolated framework/Git/installation fixtures, deliberate corruption controls on copies, one-time migration helpers, transient diagnostics and derived PDF text or page images used by a tool.
Source PDFs, research programs, mathematical outputs and continuing proof drafts keep their responsible homes.
A derived extraction is disposable only when its source remains available and any useful finding is recorded where it belongs.

Ordinary mathematics needs no temporary-directory stage.
Create or reuse a responsible D at the start of a substantive argument, stating author, title, current question and starting scope.
No result, Claim or completed review is required.
`python scripts/material.py create --kind D --line G --file -` reads the starting text directly from stdin and returns its allocated path.
Reviewers read that material directly.
Continuing arguments use D; reusable or continued programs and their outputs use J; substantive findings, failures and source observations use the applicable mathematical material.
Small interactive trials need no new material merely because they were run.
Status is stated by the material, not by moving a file out of `.tmp/`.
No current proof, review, reproduction command or handoff may depend on a file that exists only in `.tmp/`.

Files placed in `.tmp/` are one-use operational inputs or byproducts.
The creating operation/session deletes them immediately after that use, including after failure once the needed diagnostic has been extracted; cleanup normally completes before the operation returns or the session hands off.
Do not leave them for a later research round, possible reuse .
Use automatic cleanup/finally where practical; after an abrupt interruption, the responsible session removes its abandoned temporary work when it next resumes.
Reusable tools and necessary findings belong in their responsible locations instead of being retained here.

Delete only the creator's own completed or abandoned work, not another active session's files.
No cleanup approval, temporary-file registry or per-file report is required.
Before cleaning pre-existing temporary content, distinguish unique necessary material from already incorporated copies and disposable tooling.
Historical mentions do not require retaining a duplicate; preserve the event and actual review scope without promising that an obsolete temporary path remains available.

OS-managed temporary directories, third-party caches, atomic-write siblings, J-local progress and manuscript build directories retain their actual technical roles.
They are not alternative root scratch areas and need not be forced into `.tmp/`.
Temporary contents are neither committed nor copied into the official framework starting repository.

Manuscripts consume mathematical evidence, may change freely and frequently, and retain their own manuscript-review records.
Mathematical materials outside `mathematics/manuscripts/` do not point to documents or specific internal content in that directory through links, paths, citations, internal numbering or prose explanations of manuscript context.
Preserve mathematical statements, necessary hypotheses, source conventions and review findings at their authoritative C/U/L or other responsible homes, and cite those formulations.
Keep manuscript-specific context and review details inside the manuscript project.
From outside the manuscript directory, only designated fixed entrance-navigation links may lead to the collection or stable project/document entrances; they do not target internal content.
See the [manuscript reference boundary](writing.md#manuscript-reference-boundary).
