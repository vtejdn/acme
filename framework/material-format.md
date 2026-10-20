# Material-owned input format

This document specifies the material-owned input and acquisition format.
The reader and explicit material authoring commands use the responsible materials, fixed decisions and recorded evidence without a C/T JSON record resolver.

Use the [agent/tool responsibility](rules/workflow.md#agent-and-tool-responsibilities) for content, home, review and authority judgments.
Commands are optional writers and scoped factual checks of supplied inputs, not semantic preservation gates.

## Machine-readable declarations

Designated input headings and table headers, separators and rows must be actual Markdown structures outside examples.
Table headers and delimiter rows must occupy adjacent eligible physical lines; data rows belong to that same uninterrupted pipe-table block.
A blank line, prose, heading or other non-row structure ends the block, so a later orphan row supplies no field, relationship or binding to it.
Complete C/T field and relation tables can be separate blocks with ordinary spacing or explanation between them.
Sites requiring one table reject competing complete tables rather than merging them; missing required declarations retain their ordinary errors.
Fenced or indented code, backtick spans (including wrapped spans), HTML comments and the bounded HTML literal regions `pre`, `code`, `script`, `style` and `textarea` supply no declarations.
A real section heading does not make an enclosed example table authoritative.
Examples may remain as explanation without a cleanup or file-level rejection requirement.

Interpret those markers within their containing region.
A raw HTML block ends the preceding paragraph, so a backtick outside it cannot pair with one inside; fences, backticks and comment-like text inside the block cannot alter Markdown after its closing boundary.
Conversely, an HTML opener inside genuine code or a comment remains literal.
The bounded reader follows these [HTML block boundaries](https://spec.commonmark.org/0.31.2/#html-blocks) without adding a general HTML renderer.
Structural masks and semantic cell decoding derive from the same original source spans, before comments are removed.

This shared boundary applies to C/T decision histories, Review bindings and Review relationships, route and feedback associations, imported judgment tables, source inspection facts and bibliography tables used for source-key maintenance.
Registry holding/edition fields use the same literal masks and contiguous Field/Value tables at the selected account scope.
Once real table delimiters are identified, cells retain their visible inline code and mathematical content, escaped pipes and meaningful whitespace; invisible HTML comments do not become scope text.
Offset-based binding lookup uses the same semantic row under LF or CRLF.
Heading anchors retain their existing rules.

Example-only bindings cannot cover a new accepting decision, and an example-only independent-review label cannot establish independence.
Missing required coverage identifies the selected finding.
Authoring, submission, intake and onward transfer read the same declarations, without adding acquisition or inventing historical bindings.
Existing physical material and acquisition evidence remain unchanged.

## Identity and author header

Local fixed C/T/R/L materials use `Author_Kind_F0001_v1.md`.
The author chooses the line letter.
Serial numbers have at least four digits and grow numerically: F9999, F10000, F10001.
Each author/origin/kind/line owns its own counter.
A Task-derived address inherits the selected Task's letter, not its digits.
Imported C/R/L/J use an explicitly chosen receiving family serial and retain the original physical version and research line; exact source serial/family remains in provenance.

Rolling S and mutable D omit the version suffix.
D is a working address stable during current use and reusable after retirement, once useful content is fixed and actual consumers repaired.
A reused D inherits no earlier statement, scope, review or authority; fixed C/T/R/L/U/J and continuing S identities are not recyclable.
Every J computation has a numbered directory whose `readme.md` and native children share its identity.
Do not allocate a new identity to a computation's output file.

The leading header contains scalar author and applicable provenance fields only:

```yaml
---
author: Alice
framework: acme
---
```

An imported original additionally carries receiving `source_repository` and exact original `source_material`, identifying its original repository and exact original material path, rather than the immediate transport source.
Its filename uses receiving authorN_repoN for C/R/L/J; U keeps its dedicated original-author/unit placement.
A source without known ACME provenance is not branded ACME by the receiving installation.
The human registry remains the authority for registered author spelling.

Read material kind, line, serial and version from the path and the title from its single main heading.
Do not copy them into metadata.
Fixed source units use the source-key identity below; definitions retain their separate naming boundary.

## Fixed source-unit inputs

A reusable source-unit file uses `mathematics/audits/literature/<SourceKey>/<Author>_U001_v1.md`; an imported original uses `<Author>_repoN_U001_v1.md` in the same source-key directory.
`SourceKey-U001` and its lowercase `sourcekey-u001` anchor retain the existing source-unit identity.
The number has at least three digits and grows numerically within that source's existing unit sequence.
It is not a research line, a Task number or a new per-author allocation sequence.
General material creation does not allocate U numbers.
Coordinate actual source-unit identities through the existing source audit, then author the explicit fixed file.

The same short author/provenance header applies.
An imported `source_material` retains the exact original source key, unit number, author and physical material version, with explicitly translated original-repository correspondence through later transfers.
The recipient's canonical bibliography key and free local unit position may differ from that original path; its unit anchor follows the actual local position.
One position is the receiving source key and numeric unit, independent of author or origin prefix.
Different original families cannot share that position; physical versions of the same registered original repoN/family retain their established local number.
Original author and physical material version still agree with `source_material`.
The existing intake operation records the exact original/local correspondence, without replacing the original identity or adding a separate mapping registry.
Each file owns one actual unit anchor and one concise section:

```markdown
## Source and inspection
| Field | Value |
| --- | --- |
| source-version | Exact paper/book edition or artifact version actually used. |
| source-locator | Exact theorem, section and printed/PDF page scope. |
| inspection | Actual statement/hypothesis/proof checks and unexamined limits. |
```

These three nonempty facts describe performed inspection; parsing does not verify their mathematical truth or turn a checked statement into a proof audit.
The unit body owns the statement, hypotheses, definitions, adaptations and limits.
Material `vN` and the inspected external source version are distinct.
Changed substantive content gets a new fixed material version; source key or layout maintenance retains the ordinary coordinated-reference obligations.

The artifact's [registry source association](rules/literature.md#artifact-source-association) owns supplied selected/obtained addresses, edition facts, known fingerprints and necessary current limitations.
The agent establishes the association under the [common responsibility](rules/workflow.md#agent-and-tool-responsibilities).
Tools report actual fetch and byte facts; U prose, bibliography and URL spelling do not select a source or produce a work/edition verdict.
Inspect an unestablished response before local-file registration, reusing applicable prior judgments.

Explicit onward copying preserves those facts and the U's inspection scope.
A known fingerprint constrains exact bytes; successful copying and a new digest cannot resolve identity or coverage limits.
Separate artifacts keep separate availability outcomes, without a new confirmation field or source register.

The [source-input rule](rules/literature.md#artifact-source-association) requires an explicitly supplied file for byte reuse; a bibliography key or missing source cannot select the receiver's file or replace its account.
Registered PDF, HTML and resource attachments share truthful obtained/unavailable results, distinct from the authored-copy operation's required material/J inputs.
Current literal fields alone declare addresses/edition: old source prose stays undeclared, without implying unavailable bytes or being rewritten during reading.

C/T `support` or `dependency` rows may select the exact U file and its unit anchor with their actual applicability scope.
A U file is not a C/T argument, an adopted R/L review or an independently selectable lifecycle decision.
`show`, `check` and `discover --kind U` expose its title and inspection scope without assigning a theorem status.
The mechanical position check reads sibling identity headers within the same source key; it does not review their mathematical bodies.
Ordinary prose links, adjacent units and cited PDFs do not expand mathematical checking or acquisition beyond the selected unit.

U is independently selectable by direct intake.
Retain original source, exact revision/unit, whole fixed document and actual inspection facts.
Supply the chosen existing/new bibliography target and needed registered artifacts explicitly; copying does not endorse mathematical statements.
Canonical and typesetting bibliography fields follow the [bibliographic content boundary](rules/literature.md#bibliography-content); U/registry owns inspected-artifact identity and limits.
Work metadata does not authorize retrieving a different edition or rewriting the U merely to obtain a PDF.

## Claim and Task decisions

A C file has exactly one `## Current assessment` section containing exactly one Markdown link to a decision in its own family.
A T file instead uses `## Current decision`.
A decision may be in an older fixed material version.
The highest numeric main-material version is the family entrance; it does not automatically select the newest proof, review or assessment.
An alternative draft or an index row does not choose a decision.

Claims store their own decisions under `## Assessment history`; Tasks use `## Lifecycle and completion`.
Each decision starts with `### Decision <stable-key>`, giving the anchor `decision-<stable-key>`.
Use a field table and an optional relation table, for example:

```markdown
## Current assessment
[Selected decision](#decision-initial)

## Assessment history
### Decision initial
| Field | Value |
| --- | --- |
| date | 2026-10-18T09:30+08:00 |
| status | open |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact statement and hypotheses above. |
```

Required fields are `date` and `status`.
New C/T decisions use their actual offset-bearing minute timestamp under the [new-record timestamp rule](rules/workflow.md#new-record-timestamps), as illustrated above.
Retained historical dates keep their actual known precision (year, month, date, or timestamp with timezone); a new decision about older mathematics has its own current decision time.
For C, `reason` and `authority` are optional when applicable; for T, both are required with their actual meaning.
`review-status` and `role` are C-only fields, with the [Claim review classifications](rules/claims.md#separate-assessment-fields) and [Claim roles](rules/claims.md#claim-role).
Task decisions reject both fields; their concrete review relations retain their actual findings and scope.
Claim statuses are `open`, `proof draft`, `conditional`, `proved` and `refuted`, with their sole definitions in the [Claim status rule](rules/claims.md#separate-assessment-fields).
Task statuses retain proposed, active, paused, blocked, completed and retired.

Relations are `statement`, `contract`, `argument`, `support`, `dependency` and `review`, each with one exact Markdown locator and a nonempty applicability scope.
Repeat relation rows for multiple actual inputs.
A Claim has one selected statement; a Task has one contract, both in that same material family and no later than the owning version.
Imported selections also match the decision owner's registered original repoN and exact source family; a matching display name alone establishes no identity.
An accepted Claim selects an argument and an applicable fixed R/L review.
A completed Task selects its applicable review and actual support/dependencies; a review's mere existence does not complete it.
Preserve unresolved hypotheses and review limits in the named decision and the responsible mathematical sections.

A C `argument` relation selects actual reasoning in this or another applicable fixed C, including when resolving an original-source locator.
An L proof cannot be hidden behind a C redirect or relabeled support/dependency.
Fixed support and dependency relations cannot select mutable D or rolling S material.
Link the actual fixed mathematical evidence instead; method and route associations retain their separate navigation role.

An open proofless Claim requires neither an argument nor an invented Proof section.
A different author's fixed C argument can be adopted by exact locator; that does not change the argument's author or create a duplicate Claim.
The review remains separately selected.
R owns its actual checking relationship and conclusion, while C/T owns its adoption and applicability.

Only tables in the designated decision history and the designated selector are machine inputs.
Unrestricted mathematical prose, examples in code fences, PASS text and filenames do not assert acceptance.
Duplicate/missing selectors, unknown fields, missing necessary anchors and cross-family selections fail.
Keep mathematical exposition outside the small decision tables.
Decision and navigation tables share escaped-pipe handling, including Scope cells such as `$\|x\|<1$`.
Necessary anchors are read outside code blocks, code spans and comments; ATX headings may have zero to three leading spaces.

## Authoring and selecting material

### Preserved historical gaps

Some old physical Claim versions have no recorded assessment, and some earlier assessments lack an explicit argument or review selection.
Preserve those facts without supplying later evidence retroactively.
A noncurrent Claim material may use exactly this archival section instead of a Current assessment:

```markdown
## Historical material
No current assessment is selected for this physical material version.
```

Such a material has no adoptable decisions.
It is readable as fixed mathematical history and cannot serve as the latest family entrance.
Where an old assessment is recorded with incomplete selection information, retain its actual fields and relations under `## Historical assessments` and `### Historical assessment key`, using the same field/relation table syntax.
Its anchor is `historical-assessment-key`.
The reader exposes those facts separately and checks their actual locators; it does not invent absent proof/review relations or let a Current selector adopt that historical-only record.
New authoring commands reject archival material and historical-only records, so this preservation format cannot bypass new acceptance requirements.

### Explicit material writes

The optional `material.py create` allocates the next numeric address for the bound human author and chosen line.
Supply a complete Markdown document, including its author header, from `--file PATH` or standard input with `--file -`.
Use either `--line F` or `--task mathematics/tasks/Alice_T_F0001_v1.md`; the latter inherits only the Task's line letter.
C/T/R/L creation starts at physical v1, while S/D and a J directory use their adopted stable addresses.
No C/T record or snapshot is written.
Human registration, worktree identity and the existing write lock continue to apply.

```text
python scripts/material.py create --kind C --line F --file claim-input.md
python scripts/material.py revise mathematics/claims/Alice_C_F0001_v1.md --expect mathematics/claims/Alice_C_F0001_v1.md#decision-initial --file revised-claim.md
python scripts/material.py append-decision mathematics/claims/Alice_C_F0001_v2.md --expect mathematics/claims/Alice_C_F0001_v2.md#decision-initial --candidate --file candidate-decision.md
python scripts/material.py select mathematics/claims/Alice_C_F0001_v2.md --expect mathematics/claims/Alice_C_F0001_v2.md#decision-initial --decision mathematics/claims/Alice_C_F0001_v2.md#decision-reviewed
```

`revise` creates the next actual fixed C/T/R/L material version and preserves the old file.
A new C/T version contains an explicit local decision bound to its actual statement/contract; a carried-over old acceptance cannot silently approve changed mathematics.
`append-decision` takes one new `### Decision key` block.
It selects that decision unless `--candidate` is given.
`select` changes only the designated current selector and may adopt an exact older decision in the same family, preserving that decision's original evidence and scope.

C/T revision, append and select require the exact current `--expect PATH#anchor`.
The command protects its actual material read, expectation/current-main check, modification and publication under the short write lock and rejects a stale expectation before writing.
Candidate appends read the fresh history even when the selector is unchanged, retaining all earlier decisions.
The command does not retry a supplied mathematical decision against a different predecessor.
Only the latest local main material may be changed, preserving its actual author; a different bound operator is not a permission barrier.
Coordinate substantive contributions under the responsible human's own numbered material identity, without taking over another human's material or Task/E; imported originals retain their source author's bytes and use the recipient's concise acquisition metadata.
Stable local S/D and J children remain ordinary owned edits, not artificial fixed publications.
Direct mathematical inputs must have a valid author/origin header.
A tracked J child uses its program group's `readme.md` header, without a separate material identity or repeated header.
An ignored output locates that same J program entrance, but its generation and attachment provenance remain explicit facts rather than inherited authorship or Git revision.

## Review bindings for new accepted decisions

A new proof acceptance in C or completed T decision must select R/L findings that explicitly cover its exact accepted inputs.
Put this small table in the selected fixed review material, in addition to the actual review findings and limitations:

```markdown
## Review bindings
| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Statement](../claims/Alice_C_F0001_v1.md#statement) | Exact hypotheses and conclusion checked. |
| [Finding](#finding) | [Argument](../claims/Alice_C_F0001_v1.md#argument) | Exact argument checked under those hypotheses. |
```

Each `Review` locator belongs to that same fixed R/L material.
Only the rows for the actually selected finding count; another finding in the file cannot lend its coverage.
Targets match exact physical paths and anchors.
A new accepted C requires coverage of its statement and argument; a newly completed T requires coverage of its contract and every declared support/dependency.
A changed draft, contract, support or proof therefore cannot reuse a binding to an older input.
These are the review author's declared applicability boundaries, not a machine proof verdict or an inference from PASS text.

Existing historical decisions retain their actual historical evidence.
Reading or explicitly reselecting them does not invent retrospective binding tables or claim a new review.
An old fixed review lacking these bindings remains available at its preserved scope; a new acceptance needs explicit applicable review evidence.
Do not modify someone else's review to manufacture that evidence.

A [pure Claim role change](rules/claims.md#claim-role) compares with the actual prior selected decision in the writer or selected Git view.
Unchanged mathematical/review status and exact relation sets, including declared scopes and support/dependencies, inherit that assessment without new proof acceptance or retrospective bindings.
Only the role and its date/reason/designation authority change; row order is irrelevant.
This does not upgrade a historical review or exempt a genuine status/input change.

The agent reads actual changes to fixed R/L and retains the performed finding, inspected target version/anchor, declared scope and limits.
A substantive new or changed inspection uses the appropriate next physical version, with its actual date and limits, followed by the consuming decision when adopted.
Same-object path maintenance may repair locators; adopting different mathematics requires judgment of its actual review applicability.
Tools check explicit input/target sets, fields and required references and expose differences; they do not infer scope preservation, equivalent relocations or review transfer.
Historical prose-only reviews stay readable without fabricated binding tables.

A C-related R finding is explicitly selected by path, anchor and scope when its exact fixed C target is already acquired, explicitly mapped or selected in the same operation.
C selection does not acquire R automatically.
The agent judges different-revision correspondence and supplies a local mapping when applicable; tools reuse exact original provenance without comparing normalized prose.
L remains a direct entry point.
Retain original checking relationships and exact acquired inputs; other targets remain explicit original locators.
No acquired finding creates a recipient judgment or grants coverage outside its actual scope.

## Other material families

S owns its explicit Task associations and any route disposition/priority; navigation derives the reverse view.
R retains exact targets, original inspection date, checking relationship, findings and limits.
D/L contain their actual mathematics, and J uses the concise computation README.
They do not acquire a generic assessment lifecycle or C/T-style tables merely to have an address.

A J README or authored native Markdown may retain concise inspection facts under the [computation rule](rules/computations.md).
An optional `## Inspection summary` heading is ordinary prose, with no dedicated schema or protected semantic region.
Valid J maintenance and coherent reproducible-output cleanup add no generic change reminder in any selected Git view.
Apply the [common maintenance boundary](rules/records.md#substantive-material-retention); tools do not classify mathematical equivalence, lock summary prose or require acknowledgment.
Structural success is not mathematical review.
Keep useful facts in existing responsible materials and repair actual references when condensing or relocating reports.
Generated output and bulk tables follow their actual reproduction and retention duties.
Keep logs only for troubleshooting and checkpoints only for useful continuation, preserving necessary mathematics and consumers before cleanup.
Concrete identity/reference errors and separately fixed C/L/R mathematics and review bindings keep their existing checks.

## Explicit checks during construction

`material.py show/check/discover/indexes/routes` read the selected material and its direct interfaces.
Kind-specific discovery strictly checks only that kind; authoring checks the chosen sequence or family and actual selected Strategy ancestors or Task/E family.
Malformed address candidates in that namespace remain errors, while unrelated namespaces do not become prerequisites.
Explicit whole-material discovery and full-navigation regeneration retain their complete requested scope.
Source-assessed status remains attributed to its original author and exact acquired scope.
A missing unacquired original is an explicit source locator; a missing previously acquired local input is an error.
Scoped submission checks the actual working, staged or base-to-HEAD view, without local holding enrichment or private-source byte checks.
Public U display retains local holding facts separately; optional [source checks](rules/literature.md#selected-source-checks) use their actual selected declarations and view.
See [commands](../scripts/readme.md) and [identity checks](rules/identity.md#submission-checks).

## Route and feedback tables

The navigation foundation reads S's optional `## Task associations` table with columns `Task | Scope`, and `## Route` with `Field | Value` rows for `disposition` and `priority`, plus an optional `parent` row containing exactly one Markdown link to a writable local S and its existing stable anchor.
A root omits the row.
Reject duplicate parents, self-parenting, cycles, wrong kinds, ambiguous identities and unresolved local anchors.
Parent rows obey the same literal-region mask as the other declarations.
Exact Task versions/anchors are retained.
No association is inferred from matching research lines or serials.
Task families are local; conflicting selected source bindings fail before the requested view is returned.
S/L may contain `## Feedback and lineage` with `Relation | Source | Scope`, using `feedback` or `predecessor` and the exact source formulation.
Generated reverse discovery identifies the contributing author and scope; it does not alter source content, disposition or endorsement.
A predecessor identifies the historical formulation actually used; it is not the previous edit of the same S and does not require per-edit captures.

A child owns its one current parent; historical predecessor and source-selection predecessor relations keep their distinct meanings.
Bounded route rendering shows an omitted parent as external context and only derives children in the supplied scope.
A cross-Task child remains visible under each explicit Task association with its primary organization.
No parent or child disposition, Task lifecycle or execution authorization is computed from the hierarchy.

## Current execution boundary

Use one `execution/Author_E_F0001.md` per local Task family in every lifecycle state.
Its sole `Field`/`Value` table requires `task` with an exact Task decision and `state` in `not-running`, `running`, `stopped` or `ended`.
Optional `threshold_percent` records an actual absolute threshold.
An effective incremental arrangement may instead retain `baseline_percent`, `limit_percent` and `window`, with `account`/`bucket` only where needed to identify that allowance.
Concise ordinary prose states the actual still-effective conditions.
Do not retain events, duplicate author/family/UID headers, reading series or routine timestamps in E.
Task setup prepares a minimal non-running E, and all Task revisions keep the same family address.
Current E updates are agent-prepared exact edits; checking validates fields and locators without authenticating authority.

## Direct acquisition

### Local external identities and prepared correspondence

Local authors retain their registered readable names.
External C/R/L/J authors and repositories use this database's canonical `authorN` and `repoN` records, beginning at 1; the current repository has no number or self entry.
`repository/repositories.json` contains `{"next": 1, "repositories": []}` initially.
Each repository record has `id`, `name`, optional `url`, agent-supplied identification `facts` and its `authors` list.
`repository/intake-people.json` contains `{"next": 1, "people": []}` initially.
Each external person has `id`, `source_repositories`, qualified `names` rows such as `{"repository": "repo2", "name": "Alice"}` and identification `facts`.
The two association lists agree; registration changes both affected ends under the existing short lock, and issued numbers are never reused.
Each table's `next` is a positive integer greater than every issued number retained in that table and cannot decrease across a checked change.
Record IDs are unique canonical numbers; repository `name` and both record types' `facts` are nonempty strings, and an optional `url` is a string or null.
`authors` and `source_repositories` are lists of unique canonical references; each qualified `names` row has a registered `repository` from that person's source list and a nonempty original `name`.
A qualified source/name pair belongs to one adopted author correspondence, without duplicate rows.
Names, URLs and foreign numbers are identification facts, not automatic correspondence decisions.
Generic submission checks table constraints; the agent selects necessary reference maintenance under the [identity rule](rules/identity.md#explicit-material-checks), without a consumer-coverage claim from table success.
Explicit reference checks read the chosen view's material headers, shared source locators and decoded intake fields; accepted scheme case and JSON escape spelling do not change their reference meaning.

An intake supplies `--source-repository repoN` for the registered immediate sender and an explicit `--correspondence FILE` object.
Its `repositories` map translates only selected sender-local repository tokens to receiving `repoN` records.
Its `authors` rows name receiving `repository`, original source-local `name` and receiving `author`, for example `{"repository": "repo2", "name": "Alice", "author": "author3"}`.
For a selected C/R/L/J, `local.number` is the prepared receiving family serial; the original research line and physical version remain unchanged.
Repeated acquisitions and later versions reuse the established receiving family.
A known original returning to its own repository is declined using the explicit selected `returning_original: true` fact, without a self number or semantic detector.
U retains its dedicated author/key/unit filename and `unit` contract, without an external-author-number requirement.

An operation's `transport.repository` and `source.repository` refer to receiving external repository records.
For C/R/L/J, `source.author` refers to the receiving external author; `source.author_name` retains the qualified original source-local name.
`source.path`, `revision` and `anchor` retain the original selected material scope, while `local.path` and `anchor` name the actual receiving material.
`files` pairs retain sender-local `source` and receiving `local` paths; earlier omitted J files keep their prior operation's original revision.
Imported C/R/L/J headers contain receiving `author`, `source_repository` and exact original `source_material`; no UID field is part of any current identity or locator contract.
An unselected sender-local `acme-source://repoN/...` address needs the supplied repository mapping to become a receiving locator.
Without that mapping, preserve its exact raw address as unacquired source-context text qualified by the known sender and fixed sending revision.

### Selected objects


Select explicit C/U/L/J objects or eligible C-related R findings at a full fixed source commit.
No C-to-R or source-artifact expansion occurs.
R uses its actual finding anchor and requires its exact C already acquired, explicitly mapped or selected in the same operation.
T/S/D are excluded.
Save a JSON list containing `path`, `anchor` and `scope`; C uses an exact decision anchor, U its exact unit anchor.
Pass that list through the [intake command](../scripts/readme.md#cross-repository-intake).
A U supplies `bibliography: {"existing_key": "KEY"}` or `{"new_work": true}` with optional `chosen_key`.
The local literature store is excluded from intake; bibliography and source inspection are copied without opening the sender's PDF, HTML, resources or registry.
The retired `source_artifacts`, `source_bibliography`, `holding`, per-U `source_updates` and operation-level `--source-updates`/API `source_updates` inputs fail before private-store access or receiving publication.
Sender-local document links become explicit unacquired original-local references, with no receiver document, fixed-Git source-file claim or holding adoption.
Prepare bibliography, selected authored materials and the operation before the short lock, then recheck captured inputs and U positions and publish together.
Every U selection also supplies `unit` with its chosen positive integer `number` and either `edits` or `text`.
The number is the chosen receiving position within the canonical bibliography key across all authors/origin prefixes; retain an established original repoN/family's number for later physical versions.
`edits` is an ordered list of disjoint `{ "start": 0, "end": 1, "expected": "old", "replacement": "new" }` spans in the selected original's UTF-8 decoded text, using zero-based character offsets and retaining its original newlines.
The agent identifies the actual local anchor declaration and any other declarations or references needing localization; empty `edits` explicitly leaves the supplied text unchanged before exact locator rewriting.
Each span must match `expected`; stale edits fail without broad replacement.
Alternatively, `text` supplies the complete agent-prepared local Markdown, including its header, for a mixed document.
The tool then installs the original provenance header and applies exact selected/acquired or supplied locator mappings; it does not substitute source keys or anchors throughout the body.
External fixed locators, incidental tokens and literal examples remain intact unless precisely selected for an edit or exact mapping.
An occupied prepared position fails for fresh preparation; intake never silently renumbers the prepared text.
The [intake interface](../scripts/readme.md#cross-repository-intake) selects indispensable tracked J files and any explicit group refresh.
An occupied J refresh keeps the same registered original repository and J path/family, independently of the immediate transport repository.
The agent handles necessary consumer maintenance before a J refresh under the [intake rule](rules/intake.md#homes-and-independent-reuse).
Ignored output is selected separately through that J's `output_attachments`, with actual source/local file paths, scope and supplied provenance under the [attachment contract](rules/intake.md#computation-output-attachments).
Agent-decided original/local locator correspondences use the mapping input described in that interface.

Acquired mathematics retains its typed home and whole original fixed document, including unselected findings.
Only explicit mappings or already acquired exact inputs resolve locally.
An unselected relative background reference uses `acme-source://repoN/FULL_COMMIT/sender/path#anchor` using the receiving registered sender without opening the linked material or tracing its upstream original.
Translate an already explicit foreign-number locator through prepared correspondence only; an unmapped locator becomes qualified raw source context, without an active receiving-number link.
Unresolved references are reported as unmapped, rather than assumed necessary missing mathematics.
For an unselected unversioned output, retain ordinary visible text instead of a link, using its actual label and reference context:

```text
Required result (source-only unversioned output; not acquired; reference in sending repository named `Source` at material revision `FULL_COMMIT`; source path `mathematics/computation/outputs/Source_J_F0001/result.json#anchor`)
```

Its known reference context and anchor survive onward acquisition; no local same-named output or tracked-program revision supplies a binding.
Explicitly selected `output_attachments` retain their actual local destination, availability and separately supplied provenance.
The agent preserves actual missing-input limits at the consumer.
Original provenance never permits binding a similarly named file.
Onward transfer of a selected object preserves its original repository, source path/revision and inspection, even when the recipient has another bibliography key or U001 allocation.

One `intake/<initiator>/*.json` operation records the actual recorder, timestamp, instruction, original/transport provenance, selected scope, local locators and outcome.
It stores no mathematics or current-use judgment.
A historical J anchor records the scope acquired at that operation; it need not remain in today's mutable J merely for provenance reading.
Newly prepared J selections check their current anchors against the actual postimage, while earlier operation scopes and anchors remain intact.
Local consumers state their real mathematical use in their existing support/dependency/decision fields.

### Finding-level review relationships

Every independent project-review account belongs to fixed R, including partial, negative, unresolved and unadopted findings.
L may retain actual self-review or unknown findings; R placement alone establishes no independence.
The R/L finding owns its actual checking relationship; the C/T decision owns adoption and the aggregate assessment.
Use a `Review relationships` table with columns `Review` and `Relationship`, linking each finding to its real local anchor.
Allowed relationships are `self-reviewed`, `independently reviewed` and `unknown`; an omitted row means unknown, never independent.
Explain the actual review arrangement and inspected scope in the finding's existing account.
Do not derive a finding's relationship from a consumer label or physical version.

For a new independently reviewed acceptance, selected findings explicitly classified as independently reviewed must be in fixed R and together cover the exact required inputs through their Review bindings.
Complementary independent statement and argument findings can supply this coverage.
A self-reviewed aggregate does not turn its independently checked parts into self-reviews; a later independent argument finding can reuse an unchanged independent statement finding.
A new C/T physical version cannot turn a retained self-review into independent evidence.
Unknown historical relationships remain unknown and old assessments remain historical; supplement only evidence necessary for an actual new classification.
Preserve known finding relationships and fixed scopes.
Corrections to a known finding use new review evidence, not a rewritten relationship.
This structural check does not certify mathematical correctness or require a new review registry.

Tracked J review inputs retain the owning program README's original identity and the exact acquired child path, revision and anchor.
Ignored output uses its exact local locator and explicitly supplied [attachment provenance](rules/intake.md#computation-output-attachments); it does not inherit the program's source revision or generator.
The group identity neither conflates distinct files nor acquires an omitted file.
Readers distinguish acquisition-time availability from current selected-view presence and report absent output without changing an old review verdict.
New authoring still requires its actual necessary inputs; a missing attachment cannot support a claim of complete acquisition or reproduction.
For U key maintenance, the agent judges actual work/edition, content and review applicability under the [common responsibility](rules/workflow.md#agent-and-tool-responsibilities);
tools update only explicitly designated key-derived anchors and references.


### Acquired findings

An acquired R/L finding retains its original checking relationship and selected coverage.
A local accepted decision may cite it only at the actual acquired finding and supported local bindings.
Unselected source-only targets cannot bind an unrelated local object.
Acquisition alone supplies no recipient review verdict; corrections and limitations belong to their responsible mathematical material.
