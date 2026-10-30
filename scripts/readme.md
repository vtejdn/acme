# Framework commands

The standard-library runtime lives in classified `scripts/acme/` packages with thin root command entries.
The common scripts accompany the official starting repository and are usable after ordinary copying or cloning.
Run from the checkout root, or pass `--root ROOT`.
The [agent action guide](../framework/agent-actions.md) selects the work and governing rules; this document describes optional CLI interfaces and their actual side effects.

Use these optional tools for the chosen mechanical operation under the [agent/tool responsibility](../framework/rules/workflow.md#agent-and-tool-responsibilities).
A simple authorized edit can be made directly; no aggregate command or tool PASS replaces content judgment.

| Command | Purpose |
| --- | --- |
| `research.py init --username HUMAN --display-name "License name" --repository KEY` | Initialize repository identity and separately chosen human key/name |
| `research.py framework-update-check [--force] [--offline]` | Query or reuse daily official public version metadata; safely replace the ignored current cache |
| `research.py framework-update-notified VERSION --expected-notified-version OBSERVED` | Record a presented reminder only while its observed notification premise holds |
| `research.py identity-bind HUMAN` | Bind the operator in this checkout's Git worktree configuration |
| `research.py identity-add HUMAN --display-name "Actual name"` | Register a known human and supplied mappings; the empty unbound registry permits explicit first self-registration without automatic binding |
| `research.py profile --topic execution` | Locate the actual local operator's policy files; the agent applies them |
| `research.py profile --topic writing --author HUMAN --subfield free_probability` | Locate the actual author's writing layers |
| `material.py create --kind D --line G --file -` | Allocate a responsible draft directly from stdin |
| `material.py show PATH...` / `check PATH...` | Inspect explicit materials and direct required interfaces |
| `material.py discover --kind C` | Derive family entrances without another status register |
| `material.py import --source SOURCE_ROOT --plan PLAN.json` | Optional mechanical installation of explicitly prepared own content and agent-chosen forward dependencies; foreign branches separately use intake |
| `material.py indexes MATERIAL...` / `routes MATERIAL...` | Render bounded navigation as JSON |
| `render-research-navigation.py` | Regenerate the three local derived indexes |
| `execution.py check` | Check per-Task E documents and their recorded states |
| `material.py fetch-source --url ADDRESS --output LOCAL --format pdf` | Fetch supplied addresses and report actual response/byte facts without registration |
| `material.py register-source --file entry.bib --existing-key KEY --local-pdf LOCAL` | Apply exact supplied fields and register an agent-chosen local source association |
| `check-literature-storage.py` | Explicit whole-store registered-artifact inventory of presence, byte/format facts and recorded limitations |

Before repository or first-human setup, the agent collects the independent local path key and chosen License name under the [setup action](../framework/agent-actions.md#set-up-repository-or-human-identity).
`init --username KEY --display-name NAME --repository REPOSITORY` and `identity-add KEY --display-name NAME` preserve those separate supplied values in id and display_name.
Invalid keys and missing or whitespace-only/multiline names fail before identity setup; the agent requests an author-selected valid replacement instead of sanitizing or inferring a value.
The agent appends a missing, separately scoped project notice after the complete root LICENSE under the [identity rule](../framework/rules/identity.md#project-notices-during-setup), preserving upstream names/years and applicable notices; these tools neither generate credits nor complete the whole installation action.
`research.py init` is an optional Git-bootstrap helper with its actual Git prerequisite; ordinary personal-folder file and author-registration work need not invoke it or `identity-bind`.
Initialization supplies null repository_display_name and repository_abbr defaults; the agent records actual project choices and maintains the README heading through ordinary edits under the [identity rule](../framework/rules/identity.md#repository-names-and-use-environments).
The Python Repository.initialize and identity.initialize interfaces take display_name and optional Git identity arguments by keyword after repository.
The former init --url and Python URL arguments are retired and refused before initialization writes; project remote addresses remain in native Git configuration, while source-add --url and fetch-source --url retain their source-address roles.
For no-Git personal use, repository/config.json may omit repository or set it to null; a newly prepared unnamed configuration uses null without inventing a repository name.
Ordinary material reading, author registration, local creation/revision, source registration and current-E checks retain their actual duties without a target Git prerequisite.
Git research writing and delivery require the human-registered repository name and explicit checkout binding; read-only material inspection and necessary setup repair remain usable while a name is missing.
Repository names are validated separately from human path keys under the [name rule](../framework/rules/identity.md#repository-names-and-use-environments).
Git-backed source access and selected Git views require a Git executable and their actual named Git source/view; unavailable Git in a managed checkout does not select personal mode.

## Shared research with native Git

Shared Git research follows the [round-level collaboration rule](../framework/rules/tasks.md#shared-git-research) and [default joint-research permissions and integration responsibilities](../framework/rules/identity.md#shared-research-git-authority-and-integration) through ordinary native Git.
Actual human authorization to establish, advance or continue joint Task collaboration includes routine synchronization, commits and pushes within that scope by default, including through a participating individual T/E, without another delivery-mode adoption or push grant; explicit human limits take precedence.
The responsible main agent refreshes the agreed collaboration branch before each actual exploration round and judges useful progress for coherent authorized delivery, separately from the official framework version request.
Material helpers do not synchronize project branches, classify key progress or grant remote authority; ordinary local operations retain their actual scope without a new network preflight.

## Official framework version check

The [version module](acme/framework/version.py) owns the exact official repository, published ref and version-metadata address under the [version rule](../framework/versioning.md#official-version-check).
The two explicit research.py commands use the installed version metadata, repository setting, local cache and public version metadata without requiring an operator binding or Git remote.
They do not run automatically on Repository construction, mathematical reading or every tool invocation.

framework-update-check reads the repository Boolean setting, installed version metadata and ignored repository/framework-update-check.json.
Its normal action reuses today's result; --force requests an explicit same-day recheck, while --offline prevents a network attempt.
A new enabled attempt first safely publishes today's unavailable placeholder under the short repository lock, makes one bounded read-only version request outside the lock, and safely publishes only the actual result.
The same lock prepares one opaque current-request claim at .tmp/framework-update-request.json, separate from the four-field cache.
The latest started fresh request owns publication across processes; same-day reuse takes no ownership, and a later completed unavailable result supersedes an older response just as a success does.
Publication checks both that owner and the UTC-day cache, preserves the latest notification and returns superseded with cache_saved false for an older response.
The first claim lock reads the production UTC clock and current cache before writing a placeholder.
Even --force cannot replace a valid later UTC-day cache with an earlier supplied or delayed clock; this preclaim superseded result has attempted false and cache_saved false, without fetching or changing another request's claim.
Supersession after a request has claimed and fetched retains attempted true.
Normal completion removes only the caller's matching claim; an abandoned claim can be replaced by a later eligible request and introduces no attempt history or cache field.
The request uses a ten-second timeout, checks its elapsed budget between received blocks, limits the body to 256 KiB and refuses a redirect or a different actual URL.
No Git authentication, clone, replacement-file retrieval or source registry is involved.
Apply actual network permissions and explicit offline instructions; the [agent chooses relevant diagnostics](../framework/rules/identity.md#git-and-github-connection-checks), with no gh login, origin or optional-skill prerequisite for this public HTTPS read.

The JSON result exposes status, attempted, cache_reused, cache_saved, installed_version, official_repository, reminder_due and the four cache fields.
Status distinguishes success, unavailable, disabled, offline, configuration-error, local-error and superseded; an error or cache_error diagnostic is not persisted as history.
Superseded means this request no longer owns publication because a later fresh request or UTC-day cache has taken precedence, so its older response does not overwrite the current facts.
A null cache_saved means no write was needed; a false value with cache_error reports a publication limitation separately from any actually obtained metadata.
The cache itself retains only last_attempt_on, result, latest_version and notified_version.
Invalid version metadata, timeout, unavailable metadata and interruption never claim no update.
An unsuccessful current-day result is not automatically retried.

A reminder_due value is an agent action candidate, not notification or upgrade authorization.
Actually present the installed/newer versions, official repository link and upgrade choice to the human before recording the notification in the existing cache.
The optional `framework-update-notified VERSION --expected-notified-version OBSERVED` command requires the explicitly observed prior notified_version; use the literal `null` only for an actually observed empty field in a valid cache.
The callable requires `record_update_notification(root, VERSION, expected_notified_version=OBSERVED)`, using Python None for that observed null; omitted or malformed input has no unconditional fallback.
Under the existing short lock, the helper rereads a valid cache, compares only notified_version with the premise and preserves current attempt/result/version fields, whose independent changes do not invalidate that premise.
A stale premise returns status superseded, cache_saved false and the current notified_version without writing or retrying; absent valid cache or malformed input is refused.
The agent judges actual presentation order, so a later lower-version presentation can be recorded with the current premise when it remains newer than installed; command arrival and numeric magnitude do not establish that order.
Report an unsaved or uncertain fact truthfully without repeating a reminder merely to set the marker.
Adequate ordinary bounded maintenance may do the same under the [cache and concurrency rule](../framework/versioning.md#official-version-check), without making this command mandatory or adding cache fields, a second register or notification history.
The agent owns the wording and choice; the helper never installs a framework or changes research authority.

## Installation and setup

Use ordinary copying or cloning under the [installation action](../framework/agent-actions.md#install-the-framework).
First read the obtained framework version and entrances and distinguish an actual new research project from source inspection, backup, maintenance, an existing shared-project clone or upgrade using the human request and actual target contents.
For an actual new research project downloaded, copied, unpacked or Git-cloned from the official blank source, the agent first sets repository, repository_display_name and repository_abbr to actual human choices or null through ordinary bounded configuration edits.
This includes clearing an unchosen inherited repository key in a Git clone before treating it as a project registration; a human may explicitly choose or confirm the same acme key without a new name restriction.
Collect missing human key/name and project choices together, reusing supplied answers, then register the actual human, append the scoped project notice and complete necessary checkout binding.
Missing human key/name answers leave an authorless preparation copy; missing project choices remain null while independent authorized setup continues, and official-source inspection, backup or upgrade preparation does not select fresh setup.
Project identity and README content explicitly requested by the human are ordinary scoped edits; human registration and Git binding retain their separate explicit interfaces.
Setup preserves other project prose and does not authorize adding this machine's interpreter, .venv, OS versions, tool locations or installation status to public entrances or shared configuration, even as relative paths or nonsensitive facts.
Use `execution/runtime/readme.md` only for continuing nonsensitive local choices under the [runtime rule](../framework/rules/organization.md#machine-local-runtime), without an automatic note, environment inventory or environment creation.
Reuse sufficient available capabilities and invoke a selected interpreter directly when suitable; missing notes, activation or an environment are not routine setup failures.
Framework installation, upgrades and default material transfer exclude the whole source execution/ and .venv/ while preserving the destination's local contents; actual portable reproduction requirements stay at J, manuscript or other responsible public homes.
Without Git, use the supplied repository key or null when unnamed, without initializing Git; the actual official repository and existing named project clones keep their real registrations.
The agent may offer a non-blocking name update for the actually selected GitHub project remote; this is not an automatic comparison, remote rewrite or required CLI gate.
The optional init helper does not run over an already copied repository/config.json and is not an installation prerequisite.
Use the applicable existing registration/binding interface or ordinary authorized metadata edits and inspect people.json, LICENSE and necessary configuration/binding together; a successful identity-add or init result alone does not establish a completed project notice.
Human id, License display_name, project display name/abbreviation, registered Git/account mappings, checkout binding and effective Git signature are separate facts.
Registration and binding do not configure user.name or user.email; check the effective signature when a commit is needed and keep necessary changes local to that checkout.
Optional init success supplies no completed License notice, project display choices, README heading, effective commit signature or remote setup; report actual completed and missing items from the resulting files without a receipt or new status field.
Retain the complete upstream License and attribution years and append only a missing notice for actual project contributions; unknown display choices stay null, with the retained heading reported as incomplete project-title setup.
Existing research clones reuse their real project and human registrations and retain notices, while repeated setup and upgrades preserve scope and historical years without duplicate attribution or wholesale LICENSE replacement.
Agent-led upgrades may use fixed official public files and ordinary recovery copies without a Git executable, preserving named or unnamed local state and marking the installed version only after required adaptation succeeds.

## Material authoring

Material creation supports C/T/S/R/D/J/L.
`--task PATH` inherits only the Task's line instead of `--line`; omitting both uses A for new local material, after any Task inheritance.
C/T/R/L start at physical v1, S/D use stable paths, and J allocates a group README.
All L use `mathematics/ledger/`.
General creation does not allocate U.
The actual author is registered and must be the same human as the operator; an external representation needs explicit adopted local_human correspondence at its existing person record.
Choosing --author does not grant another human's authorship or correction rights.
Fixed C/T/R/L/J and continuing S families use the compact [`material_next` state](../framework/material-format.md#material-family-allocation-state) in `repository/config.json`; U uses its separate citation-key entry, and D remains reusable after its actual retirement duties.
For an already used namespace, initialize the state from an agent-confirmed issued-number upper bound before relevant allocation or retirement; surviving filenames alone do not justify resetting it.
Direct authoring maintains the same state, with no new migration command or automatic Git-history reconstruction.

`material.py check` checks material structure and direct required interfaces; public `show` additionally reads a U's explicit local holding and availability through the shared source reader.
Neither operation inspects private source bytes or native HTML anchors.
For J, `check` and `show` retain current structure, necessary inputs and original-identity checks without requiring every historical acquired anchor in current text.
The displayed acquisition scopes remain facts about their recorded revisions, rather than assertions of current availability.
Structured show and discovery results use status for the exact selected decision of either a local or externally identified C/T family, with selected_decision retaining its declaring physical path and anchor.
This replaces the former source_status field for externally identified materials; source and acquisition facts remain separate, and an unacquired selected source decision has null status rather than an inferred assessment.
A lawful same-human acquired C/T/R/L revision retains its external identity and source header and explicitly identifies its actual acquired receiving input under the [ordinary input format](../framework/material-format.md#acquired-receiving-inputs-in-local-revisions).
C/T/R/L use the physical revision's own ordinary Inputs section with exact Markdown links and adopted scopes, independently of current C/T decision selection.
The mechanical reader selects only explicitly linked earlier same-family receiving inputs whose source_repository and source_material exactly match the revision header; other ordinary support links remain ordinary support.
Selected-decision support/dependency relations retain their mathematical meaning and review coverage requirements; Inputs alone adds no such relation or coverage.
Arbitrary body links and earliest/latest family members do not select that input, and no new intake event or alteration of the old operation is required.
The existing source-information reader's material_info result keeps the current header in origin and reports inputs as rows containing path, anchor, scope and acquisitions.
Its top-level acquisitions aggregate the actual inputs' existing operation rows, whose local paths remain the acquired versions rather than being relabelled as the new local revision.
For onward intake from a fixed Git source, required configuration, identity, correspondence, materials and acquisition records all come from that selected tree, without WORKTREE or INDEX repairs.
These are derived response facts, without another persistent registry, copy marker or import-payload requirement.
For a supported R revision, finding_evidence and actual new-acceptance consumers keep acquired-input facts separate from a genuine current local finding's own relationship and exact bindings.
Use the local finding's current fixed R version and anchor under the [applicable review requirements](../framework/material-format.md#review-bindings-for-new-accepted-decisions), without requiring that anchor in the input's old acquisition operation or inheriting the source finding's verdict.
New accepted decisions retain the physical versions of their declared inputs; an unchanged source header cannot make a review of acquired v1 cover a local v2 statement, argument, contract or support.
Retained source findings keep their actual acquired scope, and missing current relationships, bad targets and genuine new-decision requirements remain observable.
For a mixed R revision, the writer and selected evidence reader reuse the existing comparison of explicit relationships, exact target locators and scopes against the agent-designated fixed input.
Supported retained syntax remains readable in that input and the revision, including a postimage normalized to separate target rows; new or changed declarations are checked with current syntax.
This comparison does not infer mathematical equivalence, date a review, select an ancestor or establish review applicability from unchanged declarations.

`material.py revise PATH --file revised.md` creates a new fixed version.
C/T require exact `--expect PATH#decision`; `append-decision` adds a real decision, and `select` selects an exact existing decision.
Stale predecessors and exclusive-create collisions require a fresh retry.
Family issuance checks the stored bound and current occupation under the existing short mutation lock, advances the next unissued value and exclusively publishes the destination.
Deletion or failure does not lower the bound; unused gaps are acceptable.
A revision preserves its existing family and advances only its physical version.
Task setup creates no E or operational link; actual selected ordinary execution prepares or reuses its local boundary, and a joint T has no E or direct S.
The optional Task coordination table declares task-type joint in every joint physical version, or one exact joint-task parent on an ordinary individual T under the [format](../framework/material-format.md#task-coordination).
Family type is invariant; omitted/changed joint declarations and either direction of same-family conversion fail before publication, preserving existing E and fixed contracts.
Revision reuses that E unchanged unless the agent prepares a separate applicable exact update; it never implicitly resumes a stop.

Develop substantive arguments directly in D or another responsible mathematical home.
A D may begin with author, title, question and scope; no result, Claim or prior review is required.
Continued programs and outputs belong in J.
Follow the [temporary-storage boundary](../framework/rules/organization.md#temporary-storage).

All parsed C decisions use open, proved or refuted and supported fields; old assessment wording remains ordinary source facts, without retired-state or historical-reading modes.
Genuinely new local formal review adoption uses R, whose findings own their actual agent relationship, exact input and scope.
Newly authored or actually revised formal findings declare their matching relationships at that finding scope, without demanding repairs to unchanged older findings in the same file.
For a genuinely new accepted C decision or completed T decision requiring review coverage, every actually selected R finding needs both its matching explicit relationship row and exact input bindings.
The shared table reader first recognizes a real header, adjacent delimiter and uninterrupted row block under the [declaration boundary](../framework/material-format.md#machine-readable-declarations).
Selected review readers then decode only the explicitly selected finding's data rows; isolated pipe-starting prose and orphan blocks declare nothing in selected or whole-container reading.
Real selected-row errors and malformed declarations within a requested whole table retain their ordinary errors.
Missing declarations do not fall back to `unknown`; explicit permitted historical/source unknown remains distinct, without requiring every finding to be independent or certifying mathematical sufficiency.
Claim navigation shows those findings separately, including missing declarations and source-only inputs, without an aggregate review grade or inferred mathematical verdict.
[Ordinary Claim labels](../framework/rules/claims.md#claim-role) use bounded title or prose edits without append-decision, select, proof-evidence reads or an assessment-comparison exemption.
Decision role fields, historical Claim modes and framework header fields are unsupported; their words may remain ordinary prose or examples.
Basic current C/T validity is independent of the optional new-decision list, which selects only actual new-date and acceptance checks.
Explicit select instead validates its chosen existing decision's current fields and references, preserving its actual date precision and evidence without treating reselection as a new review.
Selected-view checks use their actual prior view; a new decision anchor alone does not re-adopt a proof.
Actual acceptance or input changes retain the normal checks.
Removing only the retired field from an unchanged current decision is routine maintenance, without a new mathematical version, administrative decision or backfilled historical review binding.
Genuinely new C/T decisions require actual UTC minute timestamps: `YYYY-MM-DDTHH:MM`, without `Z`, numeric offsets, seconds or fractions.
A year, month or date alone or a value with a suffix does not satisfy new authoring, including a new decision about old mathematics.
The agent judges whether a mathematical decision is new; file/anchor addition and a missing Git preimage alone establish no new act.
Create/revise accept repeated --new-decision ANCHOR for optional checks of expressly chosen actual new decisions and review bindings; append-decision explicitly makes its supplied new decision.
Historical decisions retain real calendar precision and evidence through generic publication and all selected Git views without a copy marker or retrospective bindings.

## Current execution boundary

`execution.py check --task TASK_PATH` reads only the selected current local E and its exact local ordinary Task, identity and necessary fields.
Its required Task decision must be a declared decision with one unique target under the [existing anchor contract](../framework/material-format.md#claim-and-task-decisions); a unique older decision may remain selected independently of the Task's current selector.
There is no Git --view option or historical-state fallback; normal Task check/show/navigation and Git operations require no E and do not read execution state.
The common Task validator rejects links into the execution/ directory regardless of case or Windows trailing dots/spaces after URL decoding, before querying or reading E; inline-code addresses and similarly named ordinary directories retain their actual scope.
Prepare direct exact edits under the [execution rules](../framework/rules/execution.md), with the [current-E template](../framework/templates/execution/execution-run.md).
The interface has no event writer, history replay, authority inference or platform scheduler control.
Runtime notes under execution/runtime/ are not E; this selected check neither reads nor validates those notes or .venv/, and their absence or changes grant no authority or allowance.
The tools do not archive environments or create runtime notes automatically; explicit local maintenance needs no Task/E and preserves neighboring effective execution boundaries.

## Cross-repository intake

Intake is an [agent-completed receiving action](../framework/agent-actions.md#acquire-material-from-another-research-repository): read each selected file or unit and necessary context/candidates, judge what to retain, reuse, copy and adapt under current receiving rules, write actual receiving material and required provenance, and inspect the result and necessary direct consumers.
Verify the selected mathematics and claimed state for its intended use and the real original human and fixed-source facts, retaining exact content, useful failures, unresolved inputs and actual review limits.
Sender framework versions, current-format support or missing installation metadata alone do not bar adequate receiving preparation or require changing the source repository.
If the helper cannot handle a selected old filename, layout or input, report that interface limit and use an adequate ordinary path when necessary facts and a conforming local result can be established; its actual input and publication checks remain unchanged.
Keep per-unit original and transport correspondence in the existing one-operation provenance home without per-file approvals, checklists, receipts or duplicate accounts; format or tool success establishes no mathematical adoption, and later different-author corrections retain their own authorship boundary.
Ordinary file operations and existing registration/allocation mechanisms suffice without a dedicated command, prepared-text payload, mapping plan or uniform batch protocol.
The following payload, mapping and publication protocol applies only to callers choosing the optional helper.
Before receiving U through either ordinary file operations or this helper, the agent completes [acquisition for its inspected original](../framework/rules/literature.md#acquisition-before-u-reception) to its actual reused, obtained or failed outcome.
An actual failure is recorded at the responsible source home and directly reported to the human author with the work/edition, address when known, failure, availability and receiving limits.
The helper handles authored content and chosen bibliography; it neither fetches the original, imports sender-private source accounts nor certifies that the agent fulfilled those prior duties.

`material.py intake --source SOURCE --revision FULL_COMMIT --source-repository repoN --correspondence correspondence.json --selections - --instruction "Actual authorized scope"` reads the prepared JSON selection list from stdin.
This optional helper needs a Git executable and the selected full commit in a local Git checkout representing the identified public GitHub source, including its registered source repository name.
The receiving target may be an unnamed no-Git personal folder; source Git access supplies no target binding or naming requirement.
Ordinary agent-led receiving through authorized public fixed-source reads and file operations remains available without this helper or a Git executable.
Use the [complete acquisition-input contract](../framework/material-format.md#direct-acquisition) for eligible material/finding selections, bibliography targets, chosen U positions, exact expected-text edits or complete prepared text and retained provenance.
The command copies selected authored materials and bibliography, without citation-graph expansion or automatic adoption.
An explicitly selected actual independent finding in old L can be prepared in receiving fixed R with its true reviewer, targets, scope, relationship and limitations; retaining it as a current independent L finding is refused.
Whole historical L accounts and their unselected old rows remain readable, and historical operation validation does not retrospectively acquire that new-selection restriction.
R has no mandatory C target; the agent chooses actual necessary targets or limitations, including T-only and J-only findings, without selecting every binding or citation.
Within this helper, the agent explicitly designates necessary existing local inputs through --mapping; same-operation selections and neutral mixed publication supply the final receiving set, including an own imported T with another human's R.
An unmapped background link never triggers receiving-history lookup or an unselected C body/decision read.
Each actual Markdown file retains its own internal references at its receiving path, including included J documents, before cross-document exact mappings apply.
Unselected relative background links to actual tracked files in the selected sending tree become exact receiving registered sender-repoN/commit/path/anchor locators without reading linked bodies or tracing upstream provenance.
For an absent relative target, the helper preserves plain source-only reference context and reports the necessary input/correspondence adaptation, without manufacturing a fixed-commit file locator.
That mechanical tree-entry fact neither classifies the file as output nor establishes outside-tree availability or generation; the agent supplies actual content judgment and necessary adaptation.
Ordinary agent-led receiving remains valid without this helper or a prepared-text payload, using the sole current layout and retaining actual missing-input limits.
Already explicit foreign-number locators use prepared namespace correspondence or a sender-qualified local mapping.
Unmapped foreign locators become raw source context qualified by sender and fixed sending revision, without an active receiving-number link; selected originals still require their own provenance.
The private literature store and its registry/holding accounts are excluded; retired source/holding/update inputs fail before private access or receiving publication.
Sender-local document links retain unacquired original-local context.
Prepare the selected materials, bibliography and operation before the short lock, then recheck captured inputs and final U positions and publish them together.

Repeat `--include PATH` for indispensable chosen tracked J files; `--refresh-j` requests that explicit group's refresh.
`--refresh-j` permits replacement of selected files with the same registered original repository and J path/family, preserving fixed U/C/R/L versions.
Differing-byte replacement after receipt also requires adopted same-human authorship; a flag or chosen author alone does not authorize another human's correction.
The occupied group header, necessary acquisition evidence and native-file correspondence establish that identity; equal display names or the flag alone do not.
Same-original later revisions and onward transports remain eligible, with original and immediate transport identity recorded separately.
Each selected file keeps its actual original revision; an omitted earlier input is not relabelled with a newer entrance's revision.
The operation uses the shared item origin as its default and adds `files[].original: {repository, revision, path}` only for different per-file facts.
If competing existing acquisition records leave an onward file ambiguous, its selection may supply `acquisition: {"selected/sender/file": "intake/Human/existing-record.json"}` for the actual record that acquired it.
Timestamps at any precision, filename or UUID order, Git history and matching bytes do not choose the current file correspondence; differing unresolved original facts require that explicit choice.
An explicit per-file original path belongs safely to the original J group, independently of transport or local filenames, through onward transfer and occupied same-original refresh.
New selected J anchors are checked against the proposed postimage; earlier operation scopes remain unchanged and do not require their old anchors in today's J.
The agent first reads the proposed changes and maintains necessary inputs and actual consumers under the [intake rule](../framework/rules/intake.md#homes-and-independent-reuse).
Intake performs no implicit public-Markdown consumer scan, automatic anchor veto or consumer notice, and an unrelated unselected edit does not invalidate its publication snapshot.
J intake receives only selected fixed-commit programs, necessary inputs and explanations under the [J receiving rule](../framework/rules/intake.md#computation-programs-and-inputs).
It neither reads nor queries source outputs, copies or maps them, nor modifies destination outputs; output_attachments, including an empty array, is unsupported input.
Sending-output references retain visible source-only context without local links, output-byte claims or unavailable/incomplete attachment state; program receipt alone establishes no run, reproduction or review.
A prepared receiving-local link keeps its actual navigation contract, independently of the sending output.
Native code is copied unchanged unless its explicitly selected file_preparations supplies agent-judged permissible adaptation; file_map can arrange selected native children within the actual receiving J group.
The full manifest and input reads use literal selected Git keys and ordinary blobs, independently of missing, directory or junction objects at same-named sending worktree paths.
Fixed-view Reader/source_info and acquired-record validation use that view's identities, selected material and necessary file facts, including explicit local-revision inputs and onward provenance; a record's local paths belong to its owning repository/view.
Unselected operation items and historical J file lists establish no additional availability or byte-reading requirement, while a genuinely missing selected fixed input still refuses without worktree fallback.
Actual local import sources, receiving targets and Preparation/Batch publication retain Windows path, containment, reparse, occupation, expected-content and stale-input protections.
Preserve per-file originals and actual behavior/evidence limits; execute the actual acquired path and supply genuine cross-J dependencies through a separate reproduction action.
`--mapping mapping.json` supplies `{ "source": "acme-source://repoN/REV/path#anchor", "local": "PATH#anchor" }` rows for agent-decided fixed-material correspondence.
A foreign-number mapping also supplies sender: repoN for the selected sending-repository context.
Within source-reference context, supplied exact source/path/fragment mappings precede generated same-operation destinations, and contradictory explicit mappings fail before publication.
An explicit acme-source locator uses the ordinary supplied whole-file mapping after applicable repository-number translation when no exact mapping applies, retaining the incoming fragment even though it has no relative local destination.
Prepare C/T/R/L/J local.number and qualified author/repository correspondence under the [external format](../framework/material-format.md#local-external-identities-and-prepared-correspondence).
Any eligible text selection may supply prepared final local text or expected-text edits, with local kind, line, version and anchor appropriate to the content under [prepared receiving units](../framework/material-format.md#prepared-receiving-units).
Explicit source_author plus prepared selects ordinary raw R/L content without current-format parsing of its old review declarations.
For an actual selected finding, supply source_review with original reviewed_targets and any actually declared relationship under that input contract; its existing source account preserves original coordinates separately from the strictly checked receiving bindings, including on onward transfer.
Original reviewed_targets keep a source URI without any # separator in path and its fragment only in the separate anchor field; even equal duplicate fragments refuse at new input and selected-operation validation, while an empty anchor can still name an actual whole-file target.
Absent relationship facts remain undeclared rather than explicit unknown, and independently reviewed findings retain their actual relationship in fixed R without a new review or timestamp.
Prepared main materials, U text and native Markdown use receiving coordinates for local literature links through the declared source entrance.
Their ordinary local links retain final receiving objects and anchors without sending-source mapping lookup or generated source-path substitution; explicit acme-source locators and unprepared sending text retain their existing source-mapping contracts.
Source-root, group and named-file navigation receives lexical path checks without resolving the mount, testing source existence, reading private bytes, checking native fragments or certifying a holding; actual sending-private references remain source-only and no sender originals or holding accounts are copied.
Ordinary body directories retain path and existence checks without byte reads, and native fragments on non-Markdown files are preserved without binary decoding or Markdown-anchor matching.
Parents necessarily created by actual selected pending files count as directories in both initial navigation validation and its publication guard, without directory plan entries or preparatory creation.
Unselected entries and similar sibling names supply no such fact, and both checks refuse a file occupying the target directory or any necessary ancestor directory position inside the receiving repository before allocation or material/operation writes.
Declared mathematical inputs and review targets continue to use their strict required-file and material checks; generic navigation supplies no mathematical support or review coverage.
Prepared links and explicit mapping destinations are normalized and checked as public targets before any destination watch, content read or anchor check, including when the destination is planned in the same operation.
Prohibited private-profile targets receive the same existing diagnostic whether present, absent or invalid UTF-8; this boundary does not prohibit an authorized private-resource read through the general I/O interfaces.
Needed S/D mathematics is adapted into its actual fixed home; a received T must be an actual necessary joint contract with no E.
A new receiving family or U position respects and advances its actual `material_next` namespace bound, including an explicitly chosen number; a fresh number below the bound is not free merely because its path is absent.
An already established same-original receiving correspondence keeps its number across later physical versions, and an ordinary revision does not issue another family.
Complete necessary mathematics, original single human and actual source/evidence facts are retained without whole-source-container or byte-equality requirements.
Splits and same-author combinations retain complete per-unit provenance in the one concise intake operation, without an inaccurate sole-source header, archive or second mapping registry.
For onward selection containing a local revision's additions, use the actual revising repository and fixed local-revision path/anchor as that selected unit's source, while keeping its earlier acquired input reference and original acquisition facts distinct.
The earlier source or review does not thereby supply the locally added argument or its review.
A selected finding in a later acquired-input R revision supplies an explicit origin choice: `"origin": "current"` for the current source, or `"origin": {"input": {"path": "EXACT_EARLIER_R.md", "anchor": "finding"}}` for a retained finding.
The latter locator must be an actual declared fixed Input in the same original family and must be covered by its existing acquisition; optional `origin.acquisition` chooses that exact earlier operation when needed.
The selected current anchor may differ from the input anchor; the agent judges the retained scope and correspondence.
That explicit onward origin.input choice is not an ordinary write.revise or reader argument; an ordinary revision changing a retained finding's anchor uses separate current-format Target rows under the [revision rule](../framework/rules/records.md#acquired-inputs-and-local-revisions), preserving targets, scopes, relationship and fixed input without inventing a new review or acquisition.
Missing, ambiguous, undeclared or uncovered choices fail rather than guessing origin from an anchor spelling, related Inputs or revision ancestry.
This transient helper input selects existing facts; the stored operation has only its ordinary source/transport, local and scope accounts.
New acquisition times use `YYYY-MM-DDTHH:MM` UTC, without `Z`, numeric offsets, seconds or fractions; genuinely date-only facts retain calendar precision and existing necessary full timestamps are normalized under the [timestamp rule](../framework/rules/workflow.md#new-record-timestamps).

## Personal import

Personal import is an [agent-completed action](../framework/agent-actions.md#import-ones-own-selected-content): read, judge, adapt and write the selected own content and necessary dependencies, then inspect the result and affected references.
The same entrance covers export preparation; neither a public Git source nor a preliminary commit is required.
Before choosing this helper for Task transfer, the agent completes the [Task-family and independent manuscript passes](../framework/rules/intake.md#task-and-manuscript-collection), including all extant selected-family versions and actual project documents unless the human narrows the scope.
Concrete same-kind and cross-kind duplicates receive the [subagent comparison](../framework/rules/records.md#same-author-transfer-and-duplicate-comparison) before reduction and local-number allocation; unchanged text remains unchanged apart from necessary rule/address adaptation, confirmed reduction and affected consumers.
Ordinary file operations and existing registration/allocation mechanisms suffice without a dedicated command, plan JSON, complete dependency graph, full input snapshot or uniform batch transaction.
The following plan and publication protocol apply only when choosing this optional helper.
material.py import --source SOURCE_ROOT --plan PLAN.json [--author HUMAN] reads the [explicit own-content plan](../framework/material-format.md#personal-import-input); --plan - reads stdin.
The actual registered operator imports only that same human's selected content in ordinary local identities, with no external registration, source header, import-source record, intake operation, receipt or permanent map for own files.
Roots and explicit necessary dependency ids bound this helper's prepared traversal; repeated/cyclic nodes are handled once, without automatic family discovery, manuscript selection, reverse-consumer expansion or a whole U library.
Prepare every actual selected version and required project constituent explicitly when using it; the helper does not certify selection completeness, mathematical duplication or the two-pass judgment.
Its source is the supplied local-file preparation, so a selected fixed Git view must retain that view through adequate ordinary operations rather than current-worktree fallback.
Existing source/local entries, reuse, prepared edits and publication checks suffice without new fields, permanent source-number maps or an automatic transfer command.
Use source/local file entries for actual typed materials, chosen profile parts, manuscripts, native programs, data and constituents, and prepared final text or precise edits for adaptation.
The helper decodes receiving paths ending in lowercase `.md` for Markdown body checks; other constituent files retain their byte-copy scope without a Markdown-validation claim.
For an actual own maintained document with an incorrect extension spelling, prepare its canonical `.md` local path, correct contents and necessary direct references through ordinary editing or the existing explicit source/local and prepared-text interface.
Correct a prohibited public-to-private link as content maintenance as well; preserve actual source paths and fixed evidence, with no automatic case conversion or additional compatibility dispatch.
The helper reads necessary source author/origin/path and Task coordination/family-type facts separately from validating the adapted receiving result; obsolete source fields or an older Task layout alone require no source upgrade.
Existing fixed content is reused or given its appropriate physical revision; a differing rolling/profile/document target needs exact expected receiving text.
An explicitly selected own private settings file can retain internal section navigation, including a new file or exact expected update; public owners still reject private targets and no internal link selects another private file.
Before reading a selected source profile, including for prepared text or edits, the helper derives its human name from the actual safely resolved source path and checks the importing human or an already established author_correspondence.
This check supplies no path-alias compatibility; the agent confirms the intended object and corrects noncanonical input spellings when needed.
A reuse entry keeps an adequate actual local counterpart, including already-intaken own content, without conversion or duplication.
An unavailable entry describes the real missing input, which the agent retains at its actual consumer without a stub or unsupported completion claim.
Foreign necessary dependencies use explicitly reached intake entries and retain their separate authors and required provenance; within this optional interface, neutral publication checks the final selected set before writing.
Shared publication checks the actual located write destinations for case-insensitive collisions before prepared content writes, including conflicting updates to one existing file, while retaining expected, exclusive creation and rollback protections.
Ordinary Task import reads no source E and creates no local E; actual selected execution preparation or handoff separately judges effective conditions through direct edits or the optional explicit execution input.
Existing E and effective stops/allowances remain protected; actually selected new execution preparation uses a non-running boundary, while a joint parent has no E.
For an ordinary T entry, `execution` supplies either `{"text": "complete final receiving E"}` or `{"edits": [...]}` applying exact expected-text edits to the source E under the [input format](../framework/material-format.md#personal-import-input).
With execution omitted, import touches only selected material and preserves any local E; explicit complete text reads no source E, while exact edits select their source bytes.
An existing receiving E is preserved byte-for-byte and is not overwritten by `execution`.
New execution preparation remains non-running; a real execution handoff, rather than material copying alone, stops the former writer before another takes over.
The helper checks the chosen E structure and exact local Task pointer without classifying history or deciding which conditions are effective.
The agent chooses the shared-parent, exact-local-parent or complete standalone-contract disposition from the actual collaboration scope under the [Task rule](../framework/rules/tasks.md#joint-tasks-and-participation).
The tool authenticates no human identity, certifies no preservation/deduplication or review applicability, resumes no research and claims no manuscript build.

## Local source retrieval and registration

The following parameters, expected-text inputs and publication protocol apply to callers choosing these helpers.
Ordinary authorized retrieval, inspection, copying and registration edits remain available without a helper invocation or prepared JSON, retaining the same work/edition association, actual local-byte fingerprints, source facts, private storage and Git exclusions and affected-write coordination.

`material.py fetch-source --url ADDRESS --output LOCAL --format pdf|html` fetches at most two supplied addresses and returns actual requested/final URLs, byte length, format/decoding facts and digest.
Its digest is a transient response-byte fact, not a registered local baseline or source-identity verdict.
Fetching does not register a work/edition association.
Inspect a first or otherwise unestablished response before assigning it; tools do not classify identity or reject HTML by error/login keywords.
Use ordinary download tools when adequate, and keep disposable fetch output under the [temporary-storage rule](../framework/rules/organization.md#temporary-storage).

`material.py register-source --file entry.bib` requires `--existing-key KEY` or `--new-work`, with optional `--chosen-key KEY` for a chosen new identity.
Supplied fields are exact updates under the [bibliographic content boundary](../framework/rules/literature.md#bibliography-content); no automatic same-work decision or field fusion occurs.
Register an inspected local PDF with `--local-pdf FILE` and optional `--artifact-suffix=--arxiv-v2`, or original HTML with `--local-html FILE --html-name source.html`.
Explicitly name the actual file for local reuse.
A named path observed missing can record an unavailable artifact at a free destination, retaining supplied URLs and limitations without a fresh fingerprint.
For an existing absent artifact, retain its already recorded local baseline without a caller-supplied hash; an occupied file reports a conflict and keeps its existing bytes/account.
Neither an existing work key nor a receiver fingerprint supplies the missing bytes.
HTML filenames may have contained subdirectories; original bytes/native anchors remain intact.
`--selected-url`, `--obtained-url`, `--source-version` and `--limitation` supply facts.
Registration computes new PDF/HTML/resource fingerprints only from supplied actual local bytes and compares the selected existing registry baseline, preserving bytes/account on mismatch.
Fetch, registration and resource APIs accept no supplied expected hash; a prepared registry update cannot establish a fresh hash for absent bytes.
Registration does not fetch.
It generates no acquisition/access date from bytes, missing files or the current clock, and adds no substitute date or mandatory unknown-date field.
The agent maintains true known dates at their actual precision and necessary unknown source/date limits in the existing registry under the [literature rule](../framework/rules/literature.md#literature-acquisition), through ordinary edits or a selected registry_update.
Omitting both local options is bibliography-only and creates no artifact account.
Related resources use the same availability rule and explicit accounts, without a crawl or conversion.
For an existing account change, `--registry-update prepared.json` supplies `{"edits": [...]}` or `{"expected": "complete original text", "text": "complete prepared final text"}` for the actual registry.
Edit spans use the [expected-text input contract](../framework/material-format.md#direct-acquisition).
Choose the real account from its Artifact declaration and context, including comparison/contents/holding links; preparation must retain unrelated content and make its current facts agree with the supplied source facts.
An unchanged byte/fact registration preserves the current account without requiring this input; an explicitly chosen free account may append minimal supplied facts.
Competing accounts need explicit preparation, and a stale edit or inconsistent result fails before publication.
Expected old text is checked before evaluating a prepared resolution of an old primary ambiguity; strict reading applies to the selected prepared result and explicit necessary old byte constraints.
Registration returns facts read from the prepared persisted local account, which explicit local catalog/holding checks also observe; public U display does not consult it.

Use the [Artifact/Resource declarations](../framework/rules/literature.md#local-pdf-storage) and [holding contract](../framework/rules/literature.md#actual-source-holdings) for actual local source accounts.
Holding declarations use agent-prepared registry text and ordinary editing, with optional [exact maintenance](#scoped-checks-and-bibliography-maintenance) for batches or shared publication.
No dedicated holding writer is provided; an unchanged holding needs no invocation, and reading preserves its whole account.
Local registration and selected readers use the affected accounts and necessary relationships, preserving literal source facts, independent availability outcomes and limitations.
Unrelated malformed accounts do not block selected work; selected bad fields, byte conflicts and ambiguous primary candidates remain errors.
An explicitly requested whole-store inventory keeps its complete scope.
Unregistered preparatory PDFs produce no warning, substitute notice or pending-registration count; actual registered-source limits and path, link, format or byte conflicts retain their diagnostics.
For needed original-source discovery, follow the [registered-then-local-candidate order](../framework/rules/literature.md#source-preparation) before necessary external acquisition, without a whole-library prerequisite.
Reading, checking and Git delivery do not fetch sources or establish source identity, and mathematical intake copies no local source account.
Known-byte comparison and truthful unavailable outcomes follow the [source-association rule](../framework/rules/literature.md#artifact-source-association); neither extends U inspection.
An authorized retry uses explicit fetch/inspect/register.

## Shared publication

Family-number issuance, coupled identity registration and intake/U allocation use the OS lock at `repository/.lock`, as do explicitly selected navigation and bibliography helpers.
Ordinary bounded navigation and bibliography prose edits coordinate actual affected writes without universally requiring this helper lock or publication protocol.
C/T append/select and fixed-material revision protect their actual read, predecessor/current-main check and publication with the same short lock.
Preparation of mathematical decisions remains outside the lock; a stale predecessor fails without retrying against another decision.
An unselected candidate append reads fresh protected history and preserves every existing decision even when the selector has not changed.
Shared commands accept `--maintenance-wait SECONDS`, default 30; zero fails immediately.
Waiting is cancellable and emits one notice.
Re-read state after waiting; keep network, agent work and broad checks outside publication.
File existence alone does not indicate a held lock.
The shared publisher retains per-call atomic-write ownership information to recover a committed target even if its writer cannot return, while preserving competing targets and reporting any incomplete restoration.
This is an in-memory recovery aid for selected publication, without a persistent transaction record or an additional requirement on ordinary text maintenance.

## Source contents

After source preparation, the agent completes or reuses the selected edition's [searchable contents](../framework/rules/literature.md#searchable-contents) when a real contents list is supplied.
Use the common rule's PDF stem or complete native HTML path, retaining nested directories and the HTML extension before `.md`, and maintain its exact source links and necessary shared consumers together.
A local account may link to a transcription, without a shared backlink or prerequisite holding account.
For example, `pdf/WorkA/source.html` uses `contents/WorkA/source.html.md`; use actual native anchors rather than inapplicable PDF page fields.
Source acquisition success does not certify transcription completion.
Contents are navigation, not U findings; state edition and missing/unreadable transcription coverage in their existing shared account, while acquisition and local holding limits stay in the local registry.

## Scoped checks and bibliography maintenance

Use operation-local material, source and selected-reference readers for the explicitly chosen question and actual working files or Git view under the [check rules](../framework/rules/identity.md#explicit-material-checks).
Ordinary staging, committing and merging use native Git and agent inspection under the [delivery rules](../framework/rules/identity.md#submission-checks), without an aggregate history audit, preimage mapping or pass token.
The agent judges actual receiving, originals, contributors and author permissions from the real materials and instruction; useful business interfaces keep their own guards.
Material candidate enumeration precedes strict validation of the chosen kind, author/origin/kind/line sequence, selected family or actual Strategy ancestors and Task/E family.
Explicit full discovery/navigation still validates its complete promised scope.
Canonical external registration operations retain their row, allocation and necessary table-local correspondence checks under the [basic relation contract](../framework/rules/identity.md#explicit-material-checks).
Registration or selected-reference checks do not discover unchanged consumers or supply a consumer-coverage claim.
The agent identifies actual affected references and any coherent repair, choosing optional [selected reference reading](#selected-external-reference-reading) when useful.
For agent-led bibliography maintenance under the existing short shared lock, `acme.intake.addresses.rename(root, entries, mapping, files=[...], moves={"exact/source": "exact/destination"}, updates={...})` applies the prepared selection.
`mapping` uses complete parsed bibliography keys, retaining each supplied target spelling; only defined single-key `crossref` and `xref` values use the same exact lookup.
Key lists, mixed fields, file/URL values, other selected bibliographies and local references require explicit prepared edits; a shared prefix selects no work or file.
`moves` names complete repository-relative POSIX file pairs, including every selected source-store child, and preserves their bytes unless separately edited local text is supplied.
Each `updates` key names a selected Markdown, TeX, BibTeX or operation JSON file and supplies `{"edits": [...]}` or `{"expected": "complete original text", "text": "complete prepared final text"}`.
Edit spans use the [expected-text input contract](../framework/material-format.md#direct-acquisition); choose the actual local anchor separately from the bibliography key's spelling.
Prepare the selected operation item's local path, actual anchor and file/artifact correspondences together; the existing operation/material contracts validate the selected postimage before writing.
Affected U source-key namespaces include unmoved siblings and all same-batch targets after selected old positions are removed; cross-author/origin numeric occupancy and original-family continuity are checked before publication.
An explicitly mapped bibliography-key correction that keeps a U's human, original binding, unit number and physical version carries its old next-unissued bound, including retired positions, into the destination namespace while preserving monotone existing counters.
The agent selects actual citations, contents, writing records and local intake locators; literal examples and original-source/transport facts retain their exact scope and spelling.
Original/transport identities, revisions, paths, anchors, scope, availability and unselected items remain unchanged.
Only designated mixed-text citations, anchors and references change; selecting a file and key mapping performs no whole-body substitution.
Mixed bibliography notes and literal examples retain their original text unless explicitly edited.
The agent repairs actual active consumers and writing records; token lookup supplies no automatic active-citation refusal, completeness judgment or generic notice.
It does not infer unchanged mathematics, relocation equivalence or review transfer.
Valid J/E/intake maintenance emits no generic changed-file reminder.
Ordinary public-reference checks apply to chosen shared owners and reject a target in the local registry before accessing it; explicit local-account reads use their actual selected declarations without a public-body check or an implicit original-byte inventory.
The same public-target entrance rejects execution/runtime/ and .venv/readme.md as machine-local runtime notes before resolution, existence, contents or anchor access, with a runtime-specific diagnostic rather than literature or E attribution.
This role check is reused by selected-file inputs, receiving and import body links and their publication guards; it does not impose a global byte-reader prohibition on explicitly authorized local notes.
Outgoing-link checks do not discover unchanged incoming consumers or report reverse-reference coverage.
The agent selects necessary incoming files and exact target locators through scoped searches and reading, then checks them in the requested view with the shared readers.

The shared `acme.core.links.markdown_link_spans(text)` returns actual link destination spans in the original text, excluding the supported literal regions and comments.
`links.destinations(document, text)` and `acme.materials.runtime.Reader.destinations(document, text)` project those same links to local targets, with the material reader retaining source-reference validation.
For explicit working-file link checks, `links.check_files(root, selected_paths)` returns errors for the supplied public files; it does not discover consumers or assess mathematical dependencies.
An ordinary directory retains its actual role before Markdown file-anchor inspection even with a `.md` suffix and fragment; real Markdown files keep their missing and ambiguous anchor checks.
For a selected Git view, read the chosen consumers with `acme.core.git_views.Tree` and their destinations with the shared reader, then pass the designated local locators and `tree.bytes` to `acme.materials.validation.validate_locator_targets`.
WORKTREE preparation excludes the local literature registry by its existing private role before any account shape, existence or content query, including when an existing project's index still names it before authorized retirement from tracking.
It likewise excludes machine-local runtime notes and current or retired source-store roles before shape queries, while general traversal skips local runtime notes without entering them.
This shared-view boundary leaves INDEX and fixed-commit facts in their selected view, retains genuine public-input errors and adds no account-health precheck, automatic Git edit or restriction on explicit current local account and ordinary byte operations.
That required-file reader checks explicitly selected file inputs; the receiving and personal-import body-link pass instead uses validate_navigation_targets with the actual owner and prepared postimage.
The body-link reader returns a read-free guard for the existing publication lock to recheck ordinary target containment, existence and only the directory role needed by its actual prior check before allocation or writes.
Pending prepared files retain their existing expected-content protection; logical source navigation remains lexical, and unrelated changes or ordinary target content without an adopted Markdown anchor are not frozen.
Selected Markdown anchors must occur exactly once; a repair in another view does not cure that selected view.
Generic links into the logical literature root, group or source file receive containment and public-path checks without concrete source resolution, existence or native-anchor inspection.
Local navigation rejects Windows trailing-dot/space source-prefix and ancestor aliases and protected components after its existing single URL decoding, before resolve/reparse/existence queries or bytes, including inside otherwise canonical source paths.
The initial reader and publication guard preserve canonical source navigation without watching availability or contents; a source file's removal or change does not invalidate that navigation.
Ordinary material_path, preparation, import and publication checks no longer resolve unselected current or retired source roots, while actual selected paths keep containment, reparse, occupation, expected-content and stale-input protection.
Explicit source operations retain their concrete file/mount checks, and fixed Git keys, source URIs and original provenance paths retain their literal spelling without local alias rewriting.
The agent applies fixed-version and actual-review obligations under the [common maintenance boundary](../framework/rules/records.md#substantive-material-retention).
These explicit checks are not Git prerequisites and perform no delivery operation.

### Selected external reference reading

For explicit external-reference checks, use the existing Git-view reader and `acme.checks.scoped.external_references(tree, selections)` with an in-memory mapping of chosen repository-relative paths to field lists.
For example, with `root` bound to the actual checkout and the operation path chosen from that repository:

~~~python
from acme.core.git_views import Tree
from acme.checks.scoped import external_references

with Tree(root, 'INDEX') as tree:
    report = external_references(tree, {
        'mathematics/claims/author1_repo1_C_F0007_v1.md': ['identity'],
        'note.md': ['source_links'],
        'intake/Bob/Bob_I0001.json': ['transport.repository', 'items[0].source.author'],
    })
~~~

Use only actual selected paths; `WORKTREE` or an exact commit selects that postimage without an index/worktree fallback.
For Markdown, `identity` checks the shared header/prefix and necessary original-author correspondence; `source_links` checks all actual fixed source links through the shared Markdown/URL reader.
For intake JSON, choose `transport.repository`, `items[N].source.repository` or `items[N].source.author`, with actual zero-based item indices; attachment-status fields are not a supported selection interface.
Selecting `source.author` includes its necessary repository association and qualified original name; other operation fields remain outside that selection.
The shared JSON reader decodes the chosen object before field selection, so ordinary and Unicode-escaped spellings agree; the shared URL reader supplies its accepted scheme handling without a parallel prefix filter.
The result's `files` counts the selected objects read, `fields` counts checked identity/locator/provenance entries and `checked` lists their actual path/field, using source-text destination offsets for links.
No matching source links produces zero checked fields for that selected file; neither these counts nor a PASS covers unselected consumers.
This optional callable does not run full material/proof or intake-object validation, reconstruct old J objects/anchors, inspect private source bytes or create a durable selection record.

### Explicit selected source reading

The agent chooses any needed source check under the [source rule](../framework/rules/literature.md#selected-source-checks); a generic structural pass supplies no holding, edition, availability or byte verdict.
Registry and holding checks use explicitly selected current local facts; public U display exposes no source_holding or holding-derived notices.
With `root` bound to the actual checkout and the actual key substituted, an optional local account read uses existing APIs:

~~~python
from acme.core import paths
from acme.checks import literature
from acme.intake import bibliography

registry = paths.ordinary_path(root, literature.REGISTRY)
text = registry.read_text(encoding='utf-8-sig') if registry.exists() else ''
entries = bibliography.parse((root / bibliography.BIB).read_text(encoding='utf-8-sig'))
catalog = literature.source_catalog(text, entries, holding_keys=['ChosenKey'])
~~~

There is no registry INDEX/commit replay or worktree fallback contract; shared bibliography, materials and intake records retain their own explicitly selected Git views.
The local account reader also accepts explicit `artifact_names` for a chosen artifact scope; keep unchanged necessary declarations in the selected input.
An absent registry creates no file, account, warning or assertion that originals or shared evidence are absent.
Actual local-file availability and explicitly requested byte checks concern the selected physical originals, retaining recorded-baseline, path and publication protections.
No new command, scope file or automatic per-edit source-check requirement is introduced.

## Declaration and privacy checks

The [bounded declaration parser](../framework/material-format.md#machine-readable-declarations) prevents code, comments and HTML examples from supplying real decisions or review coverage.
Visible mathematical cells, escaped pipes and scope whitespace retain their meaning.
Structural checks do not establish mathematical sufficiency.

Public link and material-input checks classify normalized, decoded [private profile and local-registry targets](../framework/rules/organization.md#machine-local-locators) before body reads or anchor lookup.
They report a public-document error and request inline-code lookup instructions, independently of private-file existence or encoding.
Ordinary public anchors and tracked/staged-secret publication errors retain their checks.
Explicit resource use may still read its needed private section.
