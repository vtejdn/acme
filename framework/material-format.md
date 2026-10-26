# Material-owned input format

This document specifies the material-owned input and acquisition format.
The reader and explicit material authoring commands use the responsible materials, fixed decisions and recorded evidence without a C/T JSON record resolver.

Use the [agent/tool responsibility](rules/workflow.md#agent-and-tool-responsibilities) for content, home, review and authority judgments.
Commands are optional writers and scoped factual checks of supplied inputs, not semantic preservation gates.

## Machine-readable declarations

Designated input headings and table headers, separators and rows must be actual Markdown structures outside examples.
Table headers and delimiter rows must occupy adjacent eligible physical lines; data rows belong to that same uninterrupted pipe-table block.
A blank line, prose, heading or other non-row structure ends the block, so a later orphan row supplies no field, relationship or binding to it.
Recognize complete table structure before decoding cells, and apply an explicit finding selection before decoding unrelated data rows within it.
An isolated pipe-starting orphan or explanatory fragment supplies no declaration, regardless of whether it has a closing pipe.
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
Authoring, explicit material reading, intake and onward transfer read the same declarations, without adding acquisition or inventing historical bindings.
Existing physical material and acquisition evidence remain unchanged.

## Identity and author header

Local fixed C/T/R/L materials use `Author_Kind_F0001_v1.md`.
The author chooses the line letter.
Serial numbers have at least four digits and grow numerically: F9999, F10000, F10001.
Each author/origin/kind/line owns its own counter.
A Task-derived address inherits the selected Task's letter, not its digits.
Imported C/T/R/L/J use explicitly chosen receiving classification, research line, family serial and physical version; original classification, line, family and version remain in provenance.

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

An imported original additionally carries receiving `source_repository` and, for one original document, exact original `source_material`, separately from immediate transport.
Its filename uses receiving authorN_repoN for C/T/R/L/J; U keeps its dedicated original-author/unit placement.
The local kind, line, serial and physical version describe prepared receiving content and need not equal the source identity.
A same-author combination omits a false sole source_material and retains all distinct source/local unit accounts in the existing intake operation.
The scalar author field occurs exactly once; lists and joint-author identities are invalid.
A source without known ACME provenance is not branded ACME by the receiving installation.
The human registry remains the authority for registered author spelling.

Read material kind, line, serial and version from the path and the title from its single main heading.
Do not copy them into metadata.
Fixed source units use the source-key identity below; definitions retain their separate naming boundary.

### Acquired receiving inputs in local revisions

A lawful same-human local C/T/R/L revision retains its external identity and source header while identifying the actual acquired receiving input under the [record rule](rules/records.md#acquired-inputs-and-local-revisions).
For L/R, use an ordinary `## Inputs` section containing an explicit Markdown link to the actual earlier fixed receiving input in the same family, any necessary anchor and prose explaining its adopted scope.
Other ordinary support links may share that section; the mechanical revision-input reader selects only explicitly linked earlier receiving versions in the same family.
For C/T, use the current selected decision's existing support or dependency relation to the actual earlier receiving version in the same family, with its meaningful applicability scope.
The designated input's source_repository and source_material must match the retained revision header exactly; matching family membership does not choose an input or permit a different original source version.
For example, an L revision may state:

```markdown
## Inputs

[Acquired input](author1_repo1_L_A0001_v1.md#retained-argument) supplies the retained argument; the additional argument below belongs to this local revision.
```

These are ordinary mathematical input references that the existing readers may interpret mechanically, rather than a revision registry, copy marker or intake-specific payload required by downstream readers.
A link outside the designated Inputs section or selected C/T relation does not by itself select an acquired input, and readers do not choose one from family order or surviving versions.
Existing acquisition facts remain about the acquired input, separately from the current local revision and its added content or review obligations.

### Material family allocation state

`repository/config.json` contains one compact `material_next` object of positive next unissued integers under the [allocation rule](rules/identity.md#allocation-and-concurrency).
A local C/T/R/L/J or continuing S key is `Author_Kind_Line`, such as `Alice_C_F`; a received C/T/R/L/J key is `authorN_repoN_Kind_Line`, such as `author3_repo2_R_G`.
These components identify the actual registered receiving author, original-repository correspondence, material kind and research line, not the immediate transport repository or source serial.
A U key is `U/SourceKey`, such as `U/Src26`, and owns that canonical citation key's unit positions across authors and origin prefixes.
D has no permanent entry because its retired working address can be reused after retention and consumer repair.

For example, `{"material_next": {"Alice_C_F": 8, "author3_repo2_R_G": 12, "U/Src26": 4}}` records only the next unissued positions in those illustrative namespaces.
An empty clean bootstrap uses `"material_next": {}` without inheriting the exporting repository's numbers.
Initialize an existing affected namespace from an agent-confirmed used-number upper bound before its first relevant allocation or retirement; surviving filenames alone cannot establish that no higher number was previously issued.
Under the existing short mutation lock, issue or explicitly install the new position and advance its bound without decreasing it after deletion or failure.
A fresh receiving number below that bound is unavailable even when its path is empty; gaps are acceptable.
An already established original family retains its receiving number across later physical versions, and an ordinary next vN revision allocates no new family.
Direct authoring maintains the same state; no per-retirement row, issue date, stub, history reconstruction or migration registry is introduced.

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
The original human still agrees with `source_material`; its actual input version remains provenance separately from the local prepared version.
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

For ordinary local source preparation, the artifact's [registry source association](rules/literature.md#artifact-source-association) owns selected/obtained addresses, edition facts, fingerprints computed from actual locally obtained bytes and necessary current limitations.
The agent establishes the association under the [common responsibility](rules/workflow.md#agent-and-tool-responsibilities).
Tools report actual fetch and byte facts; U prose, bibliography and URL spelling do not select a source or produce a work/edition verdict.
Inspect an unestablished response before local-file registration, reusing applicable prior judgments.

Explicit onward reception preserves complete necessary selected U content, original provenance, inspected edition/passages and inspection limits, with the chosen bibliography correspondence and receiving unit position/text.
It carries no original publications, private source accounts or literature fingerprints and establishes no receiver-local possession.
When original text is needed, use adequate receiver-local evidence or ordinary authorized local source preparation.

The [source-input rule](rules/literature.md#artifact-source-association) requires an explicitly supplied file for byte reuse; a bibliography key or missing source cannot select the receiver's file or replace its account.
Local registration of PDF, HTML and resources reports separate truthful obtained/unavailable results; these private sources are outside authored-material intake and its required material/J inputs.
Current literal fields alone declare addresses/edition: old source prose stays undeclared, without implying unavailable bytes or being rewritten during reading.

C/T `support` or `dependency` rows may select the exact U file and its unit anchor with their actual applicability scope.
A U file is not a C/T argument, an adopted R review or an independently selectable lifecycle decision.
`show`, `check` and `discover --kind U` expose its title and inspection scope without assigning a theorem status.
The mechanical position check reads sibling identity headers within the same source key; it does not review their mathematical bodies.
Ordinary prose links, adjacent units and cited PDFs do not expand mathematical checking or acquisition beyond the selected unit.

U is independently selectable by direct intake.
Retain original source, exact revision/unit, complete necessary selected content and actual inspection facts under the [common adaptation rule](rules/records.md#receiving-and-adapting-selected-content).
The agent chooses the existing/new bibliography target and receiving unit position, writes complete necessary U content and provenance, and inspects its actual declarations and references; reception does not endorse mathematical statements.
Prepared-text and mapping payloads are optional helper inputs rather than prerequisites for receiving that content.
Intake reads no sender-private PDF, HTML, resources or registry and creates no receiving Artifact account, fingerprint, availability assertion or holding.
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
| date | 2026-10-18T01:30 |
| status | open |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact statement and hypotheses above. |
```

Required fields are `date` and `status`.
Genuinely made new C/T decisions use their actual UTC minute timestamp `YYYY-MM-DDTHH:MM` under the [new-record timestamp rule](rules/workflow.md#new-record-timestamps), as illustrated above.
A year, month or date alone, a value with `Z`, a numeric offset, seconds or fractions is invalid for those new decisions.
Historical reading and genuine reselection of an existing decision retain genuinely known calendar precision; existing necessary full timestamps are normalized to UTC minutes under the maintenance handbook, and a new decision about older mathematics has its own current UTC minute time.
For C, `reason` and `authority` are optional when applicable; for T, both are required with their actual meaning.
`role` is an optional C-only field under the [Claim roles](rules/claims.md#claim-role); T rejects it.
New/current local C decisions reject the retired aggregate `review-status`; T also has no such field.
Claim statuses are `open`, `proved` and `refuted`, with their sole definitions in the [Claim status rule](rules/claims.md#separate-assessment-fields).
Actual historical/source retired states and fields stay readable as past facts, without new local authoring or reselection aliases.
Task statuses retain proposed, active, paused, blocked, completed and retired.

Relations are `statement`, `contract`, `argument`, `support`, `dependency` and `review`, each with one exact Markdown locator and a nonempty applicability scope.
Repeat relation rows for multiple actual inputs.
A Claim has one selected statement; a Task has one contract, both in that same material family and no later than the owning version.
Imported selections also match the decision owner's registered original repoN and exact source family; a matching display name alone establishes no identity.
An accepted Claim selects an argument and applicable fixed R findings; current/new local formal review relations use R.
Necessary historical exact L evidence and imported source bindings remain readable at their actual scopes without automatic remapping or new local adoption.
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
Every required selected anchor identifies exactly one occurrence; repeated explicit declarations or a heading/explicit-anchor collision are ambiguous.

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
An explicit `--line F` selects that series; `--task mathematics/tasks/Alice_T_F0001_v1.md` inherits only the Task's line letter.
If both are omitted, new local material uses A; Task inheritance precedes this fallback, and counters remain independent by author/kind/line.
C/T/R/L creation starts at physical v1, while S/D and a J directory use their adopted stable addresses.
New C/T/R/L/J and continuing S families use the current `material_next` bound; this operation does not infer an unissued number from surviving filenames, while D retains its reusable-address rule.
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
Apply the common [existing-decision boundary](rules/records.md#existing-and-newly-made-mathematical-decisions): the agent judges new mathematical acts from content rather than file or anchor addition.
Create/revise optionally accept repeated --new-decision ANCHOR to check explicitly selected actual new dates and acceptance bindings; append-decision explicitly makes its supplied new decision.
Preserve existing decision precision and review scope in actual material work and delivery, without retrospective bindings, an import marker or a history mechanism.

C/T revision, append and select require the exact current `--expect PATH#anchor`.
The command protects its actual material read, expectation/current-main check, modification and publication under the short write lock and rejects a stale expectation before writing.
Candidate appends read the fresh history even when the selector is unchanged, retaining all earlier decisions.
The command does not retry a supplied mathematical decision against a different predecessor.
Only the latest main material may be changed by the established same human under actual authority and fixed-version rules.
Local authors must match the actual operator; an external author representation requires explicit adopted local_human correspondence at its existing person record.
Another human's correction belongs in that human's own material with exact references, including when a proposed body edit is described as administrative.
Initial intake adaptation retains necessary mathematics and truthful author/source facts rather than source-byte equality.
Stable local S/D and J children remain ordinary owned edits, not artificial fixed publications.
Direct mathematical inputs must have a valid author/origin header.
A tracked J child uses its program group's `readme.md` header, without a separate material identity or repeated header.
An ignored output locates that same J program entrance, but its generation and attachment provenance remain explicit facts rather than inherited authorship or Git revision.

## Review bindings for new accepted decisions

A new proof acceptance in C or completed T decision must select R findings that explicitly cover its exact accepted inputs.
Every actually selected finding also needs its own matching explicit allowed [relationship row](#finding-level-review-relationships); a missing row cannot fall back to `unknown`.
Put these declarations in the selected fixed review material, in addition to the actual review findings and limitations:

```markdown
## Review relationships
| Review | Relationship |
| --- | --- |
| [Finding](#finding) | self-reviewed |

## Review bindings
| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Statement](../claims/Alice_C_F0001_v1.md#statement) | Exact hypotheses and conclusion checked. |
| [Finding](#finding) | [Argument](../claims/Alice_C_F0001_v1.md#argument) | Exact argument checked under those hypotheses. |
```

Each `Review` locator belongs to that same fixed R material.
Only the rows for the actually selected finding count; another finding in the file cannot lend its coverage.
Use its actual `self-reviewed`, `independently reviewed` or permitted historical/source `unknown` relationship, rather than copying the illustrative self-review value.
An explicit permitted `unknown` is distinguishable from omission; the structural rule neither requires all findings to be independent nor certifies mathematical sufficiency.
Targets match exact physical paths and anchors.
A new accepted C requires coverage of its statement and argument; a newly completed T requires coverage of its contract and every declared support/dependency.
A changed draft, contract, support or proof therefore cannot reuse a binding to an older input.
These are the review author's declared applicability boundaries, not a machine proof verdict or an inference from PASS text.

Existing historical decisions retain their actual historical evidence.
Reading or explicitly reselecting them does not invent retrospective binding tables or claim a new review.
An old fixed review lacking these bindings or a relationship declaration remains readable with that limitation; a genuinely new acceptance needs both explicit applicable declarations for its selected findings.
Do not modify someone else's review to manufacture that evidence.

A [pure Claim role change](rules/claims.md#claim-role) compares with the actual prior selected decision in the writer or selected Git view.
Unchanged mathematical status and exact relation sets, including declared scopes and support/dependencies, inherit that assessment without new proof acceptance or retrospective bindings.
Only the role and its date/reason/designation authority change; row order is irrelevant.
This does not upgrade a historical review or exempt a genuine status/input change.
Removing only the retired field from a current decision similarly preserves its assessment and exact relations/scopes without a new decision, mathematical version or backfilled bindings; first preserve necessary objections and limitations at their actual homes.

The agent reads actual changes to fixed R/L and retains the performed finding, inspected target version/anchor, declared scope and limits.
A substantive new or changed inspection uses the appropriate next physical version, with its actual date and limits, followed by the consuming decision when adopted.
Newly authored or actually revised formal findings declare their own explicit relationships at the actual new or revised finding scope, without requiring unchanged older findings in that file to be backfilled.
Same-object path maintenance may repair locators; adopting different mathematics requires judgment of its actual review applicability.
Tools check explicit input/target sets, fields and required references and expose differences; they do not infer scope preservation, equivalent relocations or review transfer.
Historical prose-only reviews stay readable without fabricated binding tables.

An R finding is explicitly selected by path, anchor and scope without a mandatory C or other target-kind whitelist.
The agent selects necessary actual targets, support and dependencies or adequate reuse, including T-only and J-only findings.
An already-local target uses explicit correspondence; a target being prepared is checked with the actual resulting receiving material without requiring either file to be published first or a dedicated batch interface.
C selection does not acquire R automatically.
The agent judges different-revision correspondence and writes the applicable receiving references; optional helpers may apply explicit local mappings and reuse exact original provenance without comparing normalized prose.
L remains a direct entry point for historical accounts and eligible selected scopes; an actual independent old finding needs prepared receiving R with its true scope and limitations under the [selected-L boundary](rules/intake.md#selected-legacy-findings).
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
Explicit field, reference and source readers use the actual chosen files or Git view, without local holding enrichment or private-source byte checks outside their stated scope.
Public U display retains local holding facts separately; optional [source checks](rules/literature.md#selected-source-checks) use their actual selected declarations and view.
See [commands](../scripts/readme.md) and [operation-level checks](rules/identity.md#explicit-material-checks).

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

Use one `execution/Author_E_F0001.md` per ordinary individual local Task family in every lifecycle state; a joint coordination T has no E.
Its sole `Field`/`Value` table requires `task` with an exact Task decision and `state` in `not-running`, `running`, `stopped` or `ended`.
Optional `threshold_percent` records an actual absolute threshold.
An effective incremental arrangement may instead retain `baseline_percent`, `limit_percent` and `window`, with `account`/`bucket` only where needed to identify that allowance.
Concise ordinary prose states the actual still-effective conditions.
Do not retain events, duplicate author/family/UID headers, reading series or routine timestamps in E.
Ordinary individual Task setup prepares a minimal non-running E, and all revisions of that family keep the same E address.
Current E updates are agent-prepared exact edits; checking validates fields and locators without authenticating authority.

## Direct acquisition

Intake is an [agent-completed receiving action](agent-actions.md#acquire-material-from-another-research-repository): read selected content and necessary candidates, judge adaptation and reuse, write actual receiving material and required provenance, and inspect the result and affected references.
Ordinary file operations and existing registration/allocation mechanisms suffice; a dedicated command, prepared-text payload, mapping plan or uniform batch protocol is not a receiving prerequisite.
The resulting identities and provenance below remain required; command payloads and publication protocols apply only when choosing the optional intake helper.

### Local external identities and prepared correspondence

Local authors retain their registered readable names.
External C/T/R/L/J authors and repositories use this database's canonical `authorN` and `repoN` records, beginning at 1; the current repository has no number or self entry.
`repository/repositories.json` contains `{"next": 1, "repositories": []}` initially.
Each repository record has `id`, `name`, optional `url`, agent-supplied identification `facts` and its `authors` list.
`repository/intake-people.json` contains `{"next": 1, "people": []}` initially.
Each external person has `id`, `source_repositories`, qualified `names` rows such as `{"repository": "repo2", "name": "Alice"}` and identification `facts`.
An optional local_human names an explicitly adopted same-human correspondence to one canonical registered local person; identification facts explain that actual correspondence, and absent or conflicting correspondence grants no direct-revision permission.
The two association lists agree; registration changes both affected ends under the existing short lock, and issued numbers are never reused.
Each table's `next` is a positive integer greater than every issued number retained in that table and cannot decrease across a checked change.
Record IDs are unique canonical numbers; repository `name` and both record types' `facts` are nonempty strings, and an optional `url` is a string or null.
`authors` and `source_repositories` are lists of unique canonical references; each qualified `names` row has a registered `repository` from that person's source list and a nonempty original `name`.
A qualified source/name pair belongs to one adopted author correspondence, without duplicate rows.
Names, URLs and foreign numbers are identification facts, not automatic correspondence decisions.
Registration operations retain their table constraints; the agent selects necessary reference maintenance under the [identity rule](rules/identity.md#explicit-material-checks), without a consumer-coverage claim from table success.
Explicit reference checks read the chosen view's material headers, shared source locators and decoded intake fields; accepted scheme case and JSON escape spelling do not change their reference meaning.

The optional intake helper takes `--source-repository repoN` for the registered immediate sender and an explicit `--correspondence FILE` object.
Its `repositories` map translates only selected sender-local repository tokens to receiving `repoN` records.
Its `authors` rows name receiving `repository`, original source-local `name` and receiving `author`, for example `{"repository": "repo2", "name": "Alice", "author": "author3"}`.
For a selected C/T/R/L/J, `local.number` is the prepared receiving family serial; the receiving kind, research line and physical version may differ from the original facts retained in provenance.
A fresh installation respects and advances the actual receiving namespace's `material_next` bound; it cannot reuse an issued identity simply because the path is absent.
Repeated acquisitions and later physical versions reuse the established same-original receiving family rather than allocating another family number.
A known original returning to its own repository is declined using the explicit selected `returning_original: true` fact, without a self number or semantic detector.
U retains its dedicated author/key/unit filename and `unit` contract, without an external-author-number requirement.

An operation's `transport.repository` and `source.repository` refer to receiving external repository records.
For C/T/R/L/J, `source.author` refers to the receiving external author; `source.author_name` retains the qualified original source-local name.
`source.path`, `revision` and `anchor` retain the original selected material scope, while `local.path` and `anchor` name the actual receiving material.
`files` pairs retain sender-local `source` and receiving `local` paths; earlier omitted J files keep their prior operation's original revision.
An acquired J pair may add `original: {repository, revision, path}` only when its original facts differ from the item's defaults, preserving each file's actual provenance through onward transfer.
Those facts must identify the same original J; an earlier file is not relabelled with a newer entrance or transport revision.
The original path stays safely within that original J group and may differ from both transport and receiving filenames.
Imported C/T/R/L/J headers contain receiving `author`, `source_repository` and a truthful single-origin `source_material` when applicable; combined units retain their distinct sources in the same operation.
No UID field or new identity registry is part of the contract.
An unselected sender-local `acme-source://repoN/...` address needs the supplied repository mapping to become a receiving locator.
Without that mapping, preserve its exact raw address as unacquired source-context text qualified by the known sender and fixed sending revision.

### Selected objects


Select explicit C/U/L/J units, useful R findings, needed S/D mathematics for adaptation or a necessary joint T contract at a full fixed source commit.
No C-to-R or source-artifact expansion occurs.
R uses its actual finding anchor and retains actual targets and review limitations, with necessary references explicitly prepared or mapped.
An external T must be an actual necessary joint contract and has no E; another human's ordinary Task/E authority is excluded.
For callers choosing the [intake command](../scripts/readme.md#cross-repository-intake), save its JSON selection list containing `path`, `anchor` and `scope`; C uses an exact decision anchor, U its exact unit anchor.
The following selection fields, prepared-text inputs and publication protocol describe that optional interface rather than a compulsory receiving pipeline.
For a newly selected L finding, read its designated locator and declared relationship through the shared reader.
An actual independent historical finding needs complete prepared receiving R with its true targets, scope and limitations; leaving it in receiving L is refused before publication, without requiring a source-repository upgrade.
Whole historical L documents and unselected old declarations remain readable; a document selection does not implicitly select every finding or retrospectively invalidate old operation reads.
When competing acquisition records leave an onward file's original ambiguous, the selection may supply `acquisition: {"selected/sender/file": "intake/Human/existing-record.json"}` to choose its actual existing correspondence.
Only that concrete ambiguity needs a record choice; timestamps at any precision, unselected files and filename or UUID order cannot resolve it.
A U supplies `bibliography: {"existing_key": "KEY"}` or `{"new_work": true}` with optional `chosen_key`.
The local literature store is excluded from intake; bibliography and source inspection are copied without opening the sender's PDF, HTML, resources or registry.
The retired `source_artifacts`, `source_bibliography`, `holding`, per-U `source_updates` and operation-level `--source-updates`/API `source_updates` inputs fail before private-store access or receiving publication.
Sender-local document links become explicit unacquired original-local references, with no receiver document, fixed-Git source-file claim or holding adoption.
Within the optional helper, prepare bibliography, selected authored materials and the operation before the short lock, then recheck captured inputs and U positions and publish together.
Every U selection also supplies unit with its chosen positive integer number and optional positive local version; its prepared text/edits may be supplied through unit or the common prepared input.
The number is the chosen receiving position within the canonical bibliography key across all authors/origin prefixes; retain an established original repoN/family's number for later physical versions.
`edits` is an ordered list of disjoint `{ "start": 0, "end": 1, "expected": "old", "replacement": "new" }` spans in the selected original's UTF-8 decoded text, using zero-based character offsets and retaining its original newlines.
The agent identifies the actual local anchor declaration and any other declarations or references needing localization; empty `edits` explicitly leaves the supplied text unchanged before exact locator rewriting.
Each span must match `expected`; stale edits fail without broad replacement.
Alternatively, `text` supplies the complete agent-prepared local Markdown, including its header, for a mixed document.
The tool then installs the original provenance header and applies exact selected/acquired or supplied locator mappings; it does not substitute source keys or anchors throughout the body.
An exact path/fragment mapping uses its supplied destination fragment; a whole-file correspondence changes the path while retaining the incoming fragment.
Supplied exact mappings precede generated same-operation exact and whole-file destinations; contradictory explicit mappings fail before publication.
Required resulting locators, including same-operation targets, are checked against the actual prepared postimage for existence and anchor uniqueness before publication.
External fixed locators, incidental tokens and literal examples remain intact unless precisely selected for an edit or exact mapping.
An occupied prepared position fails for fresh preparation; intake never silently renumbers the prepared text.
The [intake interface](../scripts/readme.md#cross-repository-intake) selects indispensable tracked J files and any explicit group refresh.
An occupied J refresh keeps the same registered original repository and J path/family, independently of the immediate transport repository.
The agent handles necessary consumer maintenance before a J refresh under the [intake rule](rules/intake.md#homes-and-independent-reuse).
Ignored output is selected separately through that J's `output_attachments`, with actual source/local file paths, scope and supplied provenance under the [attachment contract](rules/intake.md#computation-output-attachments).
Agent-decided original/local locator correspondences use the mapping input described in that interface.

Acquired mathematics uses its actual receiving typed home and complete necessary selected content under the common adaptation rule.
Only supplied explicit mappings and same-operation selected input correspondences resolve locally.
Unselected background references never trigger receiving acquisition-history lookup or an unselected C body/decision read.
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
New operation times use `YYYY-MM-DDTHH:MM` UTC; genuinely date-only facts retain calendar precision and existing necessary full timestamps are normalized under the maintenance handbook.
It stores no mathematics or current-use judgment.
A historical J anchor records the scope acquired at that operation; it need not remain in today's mutable J merely for provenance reading.
Newly prepared J selections check their current anchors against the actual postimage, while earlier operation scopes and anchors remain intact.
Local consumers state their real mathematical use in their existing support/dependency/decision fields.

### Finding-level review relationships

Every formal project-review account belongs to fixed R for self-review, independent review and genuine historical/source unknown relationships, including partial, negative, unresolved and unadopted findings.
R placement alone establishes no independence.
The R finding owns its checking relationship; the C/T decision owns its mathematical/lifecycle assessment and evidence adoption, without an aggregate review-status.
Use a `Review relationships` table with columns `Review` and `Relationship`, linking each finding to its real local anchor.
Allowed relationships are `self-reviewed`, `independently reviewed` and genuinely unestablished historical/source `unknown`; an omitted row is a missing declaration, distinct from explicit unknown.
Each new or substantively revised finding supplies its own matching row; a new acceptance requires the matching row for every R finding it actually selects, with the exact bindings above.
These requirements apply to the selected or authored finding scope, not every unchanged older finding in its container.
Explain the actual review arrangement and inspected scope in the finding's existing account.
Do not derive a finding's relationship from a consumer label or physical version.

Tools check exact supplied review bindings without selecting an independent-coverage mode from C or inferring an aggregate from mixed findings.
The agent judges the actual mathematical sufficiency and any required independent coverage at the precise scopes; complementary applicable independent findings can supply that coverage.
Each selected finding's relationship, exact input and authored scope appear individually in the existing Claim navigation; a missing declaration, source-only input and bad local locator remain different facts.
A new C/T physical version cannot turn a retained self-review into independent evidence.
Unknown historical relationships remain unknown and old assessments remain historical; supplement only evidence necessary for actual new adoption or required review.
Preserve known finding relationships and fixed scopes.
Corrections to a known finding use new review evidence, not a rewritten relationship.
This structural check does not certify mathematical correctness or require a new review registry.
An independent agent operates outside substantive proof development without inherited or shared mathematical discussion, summaries or prior conclusions; fixed statements, proofs and necessary dependencies are direct review inputs.
After an independently identified gap is repaired, a separate isolated agent independently rechecks the correction and affected chain; a substantive repair contributor cannot independently review that contribution.
All framework relationships describe agent reviews; human authorship, advice and authorization supply no framework review category or substitute finding.

Tracked J review inputs retain the owning program README's original identity and the exact acquired child path, revision and anchor.
Ignored output uses its exact local locator and explicitly supplied [attachment provenance](rules/intake.md#computation-output-attachments); it does not inherit the program's source revision or generator.
The group identity neither conflates distinct files nor acquires an omitted file.
Readers distinguish acquisition-time availability from current selected-view presence and report absent output without changing an old review verdict.
New authoring still requires its actual necessary inputs; a missing attachment cannot support a claim of complete acquisition or reproduction.
For U key maintenance, the agent judges actual work/edition, content and review applicability under the [common responsibility](rules/workflow.md#agent-and-tool-responsibilities);
tools update only explicitly designated key-derived anchors and references.


### Acquired findings

An acquired R/L finding retains its original checking relationship and selected coverage.
When relying on inherited source review evidence, a local accepted decision cites the actual acquired finding and supported local bindings.
A lawful same-human R revision may also contain a genuine locally performed finding, consumed at its current fixed version and anchor with its own explicit relationship and exact bindings under the [new-review and acceptance requirements](#review-bindings-for-new-accepted-decisions).
That local finding need not appear in its acquired input's historical operation; the input account remains limited to the actual acquired source scope rather than marking every finding in the revision as acquired.
For onward selection from that revision, the agent explicitly chooses the current source or the exact fixed Input finding whose acquired scope is retained, including an existing acquisition selector when necessary.
The optional helper uses `origin: "current"` or `origin: {"input": {"path": "EXACT_EARLIER_R.md", "anchor": "finding"}, "acquisition": "intake/Human/existing.json"}` with acquisition optional.
The inherited locator must occur in the actual declared Inputs, retain the same original family/header binding and name a finding covered by the chosen earlier operation.
An exact input anchor can differ from the selected current anchor when the agent has established that retained scope; spelling and ancestry alone establish no inheritance.
No inherited/new marker is persisted, and the original reviewed-target account remains separate from the current receiving bindings.
The acquired input supplies no relationship, reviewed-target coverage or verdict for a new local finding.
In a mixed R revision, a retained finding keeps its supported historical Target syntax at the explicit input's actual scope, while new or changed findings meet current declaration requirements.
The postimage may express retained targets as separate current-format rows without changing the fixed input or inventing another review.
For a genuinely new adoption, an acquired original missing a relationship row retains that limitation and needs adequate conforming evidence; do not rewrite its source declaration to manufacture coverage.
The [explicit selected-L restriction](rules/intake.md#selected-legacy-findings) applies at new acquisition, while whole historical documents and unselected old facts retain their original reading scope.
Unselected source-only targets cannot bind an unrelated local object.
Acquisition alone supplies no recipient review verdict; corrections and limitations belong to their responsible mathematical material.

## Prepared receiving units

This section specifies the optional intake helper's prepared-text interface; the agent may instead complete receiving through ordinary file operations under the [common adaptation rule](rules/records.md#receiving-and-adapting-selected-content).
For any eligible textual selection passed to that helper, prepared supplies either complete final local text as {"text": "..."} or precise expected-text edits under the existing links.edit_text contract.
Prepared text uses final receiving local links and anchors; exact acme-source locators may still use the explicit mapping input.
Without prepared, the existing whole-text path remains an explicit choice, without creating a whole-copy obligation.
The local object supplies positive number and may choose kind, line, physical version and local anchor appropriate to the content; source identity and selected input anchor remain unchanged provenance.
Needed S/D content requires an eligible fixed receiving kind rather than an invented source assessment.
An older unparseable local-source structure additionally supplies its actual source_author and complete prepared text; source correspondence and final receiving declarations remain validated.
Split scopes use distinct selected original anchors and local destinations.
Same-author combinations select their actual distinct source units with the same local destination and complete prepared final text; author, source association and every per-unit source/local account must agree.
When several original repositories are involved, local.source_repository may choose one existing associated receiving namespace for the single canonical external human; all actual original repositories remain distinct in the same operation's per-unit source facts.
Conflicting prepared outputs, authors, locators, source associations, occupied fixed positions and stale expected text fail before publication.
For explicitly selected tracked native J children, file_map names exact source-to-receiving file paths within that same receiving group, and file_preparations supplies chosen complete text or expected-text edits.
These fields never select additional files; preserve actual per-file originals and verify relevant behavior changes at the responsible author's scope.
Prepared Markdown uses final receiving links, while native code executes only through a separate actual reproduction action.
The operation retains each unit's exact original repository, author, revision, path, anchor and scope, and its actual receiving path and anchor.
An R source account also retains reviewed_targets with each originally declared path, anchor and inspected scope in that original review's repository/numbering context at its recorded revision.
For a genuine local finding in an acquired R revision, that context is the actual revising repository and fixed revised R; an inherited finding retains its established original target account separately from receiving bindings.
These original inspected inputs remain separate from receiving bindings, preserve onward scope and do not assert target acquisition or applicability to changed mathematics.
Neither intake nor personal import infers substantive deduplication, review applicability or permission from a successful check.

## Task coordination

Only T has an optional single task-level section named Task coordination with one Field/Value table, outside every lifecycle decision.

```markdown
## Task coordination

| Field | Value |
| --- | --- |
| task-type | joint |
```

Every physical version of a joint family declares task-type joint; the entire family has no E or directly associated S.
Absence denotes ordinary only within a consistently ordinary family, which retains its stable E in every lifecycle state.
Omitted/changed declarations and either direction of same-family type conversion remain invalid under the Task revision, import and execution rules, with the actual receiving inputs preserved.
Add no type-history register or inherited missing declaration.
An ordinary individual T may instead declare one joint-task row whose value is an exact Markdown link to an actual same-repository joint T physical version and its contract anchor.
The joint T has no parent; reject duplicate, self, nested, cyclic, wrong-kind, non-joint and absent-contract targets.
This link records fixed contract adoption, without changing type, authority, lifecycle, E or another participant's files.
See the [Task rule](rules/tasks.md#joint-tasks-and-participation) for shared-parent reception, standalone receiving contracts and mathematical completion.

## Personal import input

Personal import is an [agent-completed action](agent-actions.md#import-ones-own-selected-content) using ordinary reading, adaptation and file operations under the [personal-import rule](rules/intake.md#personal-import).
The plan and publication protocol below apply only to callers choosing the optional helper; a plan JSON, complete dependency graph, full input snapshot or uniform batch transaction is not a prerequisite for that action.
The optional material.py import --source SOURCE_ROOT --plan PLAN.json installs explicitly prepared own content independently of intake.
The plan contains roots (selected entry ids) and entries (unique id rows); dependencies explicitly name only agent-judged necessary forward inputs.
Repeated nodes and cycles are processed once, and unselected entries are not read or installed.
An own entry supplies source and local repository-relative file paths and optional prepared final text or exact edits.
For adapted older content, the helper reads necessary scalar author, origin, path and Task coordination/family-type facts separately from current receiving-schema validation.
Obsolete source headers or an older Task layout alone do not require a source upgrade; the prepared receiving result still satisfies its actual current format and author/type boundaries.
A differing existing rolling/profile/document file additionally supplies its exact expected receiving text; occupied fixed versions require adequate reuse or the appropriate new physical version.
A reuse entry supplies local and reuse true, retaining that exact adequate object without writing, conversion or another allocation.
An unavailable entry supplies the concrete unavailable dependency limitation, also stated by the agent at its actual consumer; no placeholder file is created.
The optional author_correspondence maps actual source names to the importing registered human from already established facts for this preparation only, without retained import provenance.
The actual importing author must match the operator; a chosen author argument or mere source-name equality authenticates no human.

For an ordinary T entry, its `execution` object supplies either `{"text": "complete final receiving E"}` or `{"edits": [...]}` using the existing exact expected-text edit contract against the source E.
The agent reads source and local conditions and chooses the final exact local Task-decision pointer, state and necessary effective conditions while omitting unrelated history.
When a source E exists and no receiving E exists, the helper requires that explicit `execution` preparation instead of automatically copying the source E.
When no source E exists, `execution` may be omitted and the helper prepares a minimal non-running E.
An existing receiving E remains byte-for-byte intact; supplying `execution` does not overwrite it.
A source assignment still running is refused even when the prepared receiving content is non-running, and a newly installed E cannot have state `running`.
The helper validates the prepared fields and pointer without classifying history or judging which conditions remain effective; these execution fields belong only to this optional interface.

```json
{
  "roots": ["task"],
  "entries": [
    {"id": "task", "source": "mathematics/tasks/Alice_T_F0008_v1.md", "local": "mathematics/tasks/Alice_T_A0001_v1.md", "dependencies": ["draft"]},
    {"id": "draft", "source": "mathematics/drafts/Alice_D_F0009.md", "local": "mathematics/drafts/Alice_D_A0001.md"}
  ]
}
```

Explicitly selected profile parts, manuscript sources, figures, bibliography, J programs, data and other constituent files each name their own source/local arrangement in the actual human's responsible home.
No directory or textual link implicitly expands the selection.
A reached foreign entry supplies intake with source_root, full revision, actual instruction, source_repository, correspondence, selections and any explicitly needed mapping/files under the existing intake contract.
Only those foreign branches create intake operations; within this optional interface, neutral publication validates all own and foreign final references together, then rechecks its captured inputs and publishes the selected set under the short lock.
Own import creates no external registration, source fields, source section, import-source record, persistent map, receipt or source archive.
Temporary plan/source bytes serve only preparation and freshness protection and are cleaned by their creator.
The agent reads the actual source and local execution conditions and prepares only necessary effective conditions under the [execution rule](rules/execution.md#current-contents-and-retained-limits); moving the ordinary T does not automatically copy its source E.
Existing stable E and effective conditions remain protected; a still-running source assignment must stop before a moved assignment can obtain another writer, and a new boundary remains non-running.
Import alone starts no research, creates no allowance, invents no mathematical decision or review and claims no successful local manuscript build.
