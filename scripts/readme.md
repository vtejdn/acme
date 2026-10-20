# Framework commands

The standard-library runtime lives in classified `scripts/acme/` packages with thin root command entries.
Every maintained runtime module is explicitly exported.
Run from the checkout root, or pass `--root ROOT`.
The [agent action guide](../framework/agent-actions.md) selects the work and governing rules; this document describes optional CLI interfaces and their actual side effects.

Use these optional tools for the chosen mechanical operation under the [agent/tool responsibility](../framework/rules/workflow.md#agent-and-tool-responsibilities).
A simple authorized edit can be made directly; no aggregate command or tool PASS replaces content judgment.

| Command | Purpose |
| --- | --- |
| `research.py init --username HUMAN --repository KEY` | Initialize repository identity and actual human registration |
| `research.py identity-bind HUMAN` | Bind the operator in this checkout's Git worktree configuration |
| `research.py identity-add HUMAN --display-name "Actual name"` | Register a known human and supplied mappings; the empty unbound registry permits explicit first self-registration without automatic binding |
| `research.py profile --topic execution` | Locate the bound operator's policy files; the agent applies them |
| `research.py profile --topic writing --author HUMAN --subfield free_probability` | Locate the actual author's writing layers |
| `material.py create --kind D --line G --file -` | Allocate a responsible draft directly from stdin |
| `material.py show PATH...` / `check PATH...` | Inspect explicit materials and direct required interfaces |
| `material.py discover --kind C` | Derive family entrances without another status register |
| `material.py indexes MATERIAL...` / `routes MATERIAL...` | Render bounded navigation as JSON |
| `render-research-navigation.py` | Regenerate the three local derived indexes |
| `execution.py check` | Check per-Task E documents and their recorded states |
| `check-research-submission.py` | Explicitly check INDEX; --working-tree or --commits BASE selects another material view |
| `material.py fetch-source --url ADDRESS --output LOCAL --format pdf` | Fetch supplied addresses and report actual response/byte facts without registration |
| `material.py register-source --file entry.bib --existing-key KEY --local-pdf LOCAL` | Apply exact supplied fields and register an agent-chosen local source association |
| `check-literature-storage.py` | Explicit whole-store registered-artifact inventory of presence, byte/format facts and recorded limitations |
| `export-framework.py DESTINATION --repository KEY` | Create a clean self-exportable repository outside the source checkout |

## Material authoring

Material creation supports C/T/S/R/D/J/L.
`--task PATH` inherits only the Task's line instead of `--line`.
C/T/R/L start at physical v1, S/D use stable paths, and J allocates a group README.
All L use `mathematics/ledger/`.
General creation does not allocate U.
The actual author is registered; substantive collaboration follows the [identity rule](../framework/rules/identity.md), without a technical author-equality gate.

`material.py check` checks material structure and direct required interfaces; public `show` additionally reads a U's explicit local holding and availability through the shared source reader.
Neither operation inspects private source bytes or native HTML anchors.
For J, `check` and `show` retain current structure, necessary inputs and original-identity checks without requiring every historical acquired anchor in current text.
The displayed acquisition scopes remain facts about their recorded revisions, rather than assertions of current availability.

`material.py revise PATH --file revised.md` creates a new fixed version.
C/T require exact `--expect PATH#decision`; `append-decision` adds a real decision, and `select` selects an exact existing decision.
Stale predecessors and exclusive-create collisions require a fresh retry.
Independent allocation does not take the shared-maintenance lock.
Task setup also prepares the family's minimal non-running E and one operational entrance.
Revision reuses that E unchanged unless the agent prepares a separate applicable exact update; it never implicitly resumes a stop.

Develop substantive arguments directly in D or another responsible mathematical home.
A D may begin with author, title, question and scope; no result, Claim or prior review is required.
Continued programs and outputs belong in J.
Follow the [temporary-storage boundary](../framework/rules/organization.md#temporary-storage).

For a [pure Claim role change](../framework/rules/claims.md#claim-role), `append-decision` inherits the actual selected assessment when its statuses and exact relation sets/scopes remain unchanged.
It checks ordinary fields, references and the expected selector without demanding new historical bindings.
Selected-view checks use their actual prior view; a new decision anchor alone does not re-adopt a proof.
Actual acceptance or input changes retain the normal checks.

## Current execution boundary

`execution.py check --task TASK_PATH [--view WORKTREE|INDEX|FIXED_REF]` checks the explicitly selected family's current E fields, state and exact Task decision in that actual view.
Prepare direct exact edits under the [execution rules](../framework/rules/execution.md), with the [current-E template](../framework/templates/execution-run.md).
The interface has no event writer, history replay, authority inference or platform scheduler control.

## Cross-repository intake

`material.py intake --source SOURCE --revision FULL_COMMIT --source-repository repoN --correspondence correspondence.json --selections - --instruction "Actual authorized scope"` reads the prepared JSON selection list from stdin.
Use the [complete acquisition-input contract](../framework/material-format.md#direct-acquisition) for eligible material/finding selections, bibliography targets, chosen U positions, exact expected-text edits or complete prepared text and retained provenance.
The command copies selected authored materials and bibliography, without citation-graph expansion or automatic adoption.
Unselected relative background links become exact receiving registered sender-repoN/commit/path/anchor locators without reading linked materials or tracing their upstream provenance.
Already explicit foreign-number locators use prepared namespace correspondence or a sender-qualified local mapping.
Unmapped foreign locators become raw source context qualified by sender and fixed sending revision, without an active receiving-number link; selected originals still require their own provenance.
The private literature store and its registry/holding accounts are excluded; retired source/holding/update inputs fail before private access or receiving publication.
Sender-local document links retain unacquired original-local context.
Prepare the selected materials, bibliography and operation before the short lock, then recheck captured inputs and final U positions and publish them together.

Repeat `--include PATH` for indispensable chosen tracked J files; `--refresh-j` requests that explicit group's refresh.
`--refresh-j` permits replacement of selected files with the same registered original repository and J path/family, preserving fixed U/C/R/L versions.
The occupied group header, necessary acquisition evidence and native-file correspondence establish that identity; equal display names or the flag alone do not.
Same-original later revisions and onward transports remain eligible, with original and immediate transport identity recorded separately.
New selected J anchors are checked against the proposed postimage; earlier operation scopes remain unchanged and do not require their old anchors in today's J.
The agent first reads the proposed changes and maintains necessary inputs and actual consumers under the [intake rule](../framework/rules/intake.md#homes-and-independent-reuse).
Intake performs no implicit public-Markdown consumer scan, automatic anchor veto or consumer notice, and an unrelated unselected edit does not invalidate its publication snapshot.
J programs use `mathematics/computations/programs/<J>/`; ignored output is selected separately with actual paths and provenance under the [output-attachment contract](../framework/rules/intake.md#computation-output-attachments).
Only supplied files are copied, with output availability recorded separately from commit-bound files.
Unselected ignored-output references retain visible source-only original context; an occupying local file supplies no correspondence.
Native code is copied without rewriting; execute its actual acquired path and supply genuine cross-J dependency paths explicitly.
`--mapping mapping.json` supplies `{ "source": "acme-source://repoN/REV/path#anchor", "local": "PATH#anchor" }` rows for agent-decided fixed-material correspondence.
A foreign-number mapping also supplies sender: repoN for the selected sending-repository context.
Prepare C/R/L/J local.number and qualified author/repository correspondence under the [external format](../framework/material-format.md#local-external-identities-and-prepared-correspondence).
Whole fixed documents remain intact, and one concise operation records the actual scope in `intake/<initiator>/`.

## Local source retrieval and registration

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
Omitting both local options is bibliography-only and creates no artifact account.
Related resources use the same availability rule and explicit accounts, without a crawl or conversion.
For an existing account change, `--registry-update prepared.json` supplies `{"edits": [...]}` or `{"expected": "complete original text", "text": "complete prepared final text"}` for the actual registry.
Edit spans use the [expected-text input contract](../framework/material-format.md#direct-acquisition).
Choose the real account from its Artifact declaration and context, including comparison/contents/holding links; preparation must retain unrelated content and make its current facts agree with the supplied source facts.
An unchanged byte/fact registration preserves the current account without requiring this input; an explicitly chosen free account may append minimal supplied facts.
Competing accounts need explicit preparation, and a stale edit or inconsistent result fails before publication.
Expected old text is checked before evaluating a prepared resolution of an old primary ambiguity; strict reading applies to the selected prepared result and explicit necessary old byte constraints.
Registration returns facts read from the prepared persisted account, which the selected catalog and local U holding display also observe.

Use the [Artifact/Resource declarations](../framework/rules/literature.md#local-pdf-storage) and [holding contract](../framework/rules/literature.md#actual-source-holdings) for actual local source accounts.
Holding declarations use agent-prepared registry text and ordinary editing, with optional [exact maintenance](#scoped-checks-and-bibliography-maintenance) for batches or shared publication.
No dedicated holding writer is provided; an unchanged holding needs no invocation, and reading preserves its whole account.
Local registration and selected readers use the affected accounts and necessary relationships, preserving literal source facts, independent availability outcomes and limitations.
Unrelated malformed accounts do not block selected work; selected bad fields, byte conflicts and ambiguous primary candidates remain errors.
An explicitly requested whole-store inventory keeps its complete scope.
Reading, checking and submission do not fetch sources or establish source identity, and mathematical intake copies no local source account.
Known-byte comparison and truthful unavailable outcomes follow the [source-association rule](../framework/rules/literature.md#artifact-source-association); neither extends U inspection.
An authorized retry uses explicit fetch/inspect/register.

## Shared publication

Identity registration, shared navigation, bibliography and intake/U allocation use the OS lock at `repository/.lock`.
C/T append/select and fixed-material revision protect their actual read, predecessor/current-main check and publication with the same short lock.
Preparation of mathematical decisions remains outside the lock; a stale predecessor fails without retrying against another decision.
An unselected candidate append reads fresh protected history and preserves every existing decision even when the selector has not changed.
Shared commands accept `--maintenance-wait SECONDS`, default 30; zero fails immediately.
Waiting is cancellable and emits one notice.
Re-read state after waiting; keep network, agent work and broad checks outside publication.
File existence alone does not indicate a held lock.

## Source contents

After source preparation, the agent completes or reuses the selected edition's [searchable contents](../framework/rules/literature.md#searchable-contents) when a real contents list is supplied.
Use the common rule's PDF stem or complete native HTML path, retaining nested directories and the HTML extension before `.md`, and publish its exact registry/source links together.
For example, `pdf/WorkA/source.html` uses `contents/WorkA/source.html.md`; use actual native anchors rather than inapplicable PDF page fields.
Source acquisition success does not certify transcription completion.
Contents are navigation, not U findings; state missing or unreadable coverage in the existing registry/handoff.

## Scoped checks and bibliography maintenance

Optional scoped checking reads actual WORKTREE, INDEX or BASE-to-HEAD bytes under the [submission rules](../framework/rules/identity.md#submission-checks) and reports explicit identity/field/reference/review-binding errors.
Material candidate enumeration precedes strict validation of the chosen kind, author/origin/kind/line sequence, selected family or actual Strategy ancestors and Task/E family.
Explicit full discovery/navigation still validates its complete promised scope.
Changes to either canonical external table check affected registration rows, allocation constraints and necessary table-local counterparts in the actual selected view under the [basic relation contract](../framework/rules/identity.md#explicit-material-checks).
`external_table_files` counts the changed tables checked; registration changes do not discover unchanged consumers or supply a consumer-coverage claim.
The agent identifies actual affected references and any coherent repair, choosing optional [selected reference reading](#selected-external-reference-reading) when useful.
For agent-led bibliography maintenance under the existing short shared lock, `acme.intake.addresses.rename(root, entries, mapping, files=[...], moves={"exact/source": "exact/destination"}, updates={...})` applies the prepared selection.
`mapping` uses complete parsed bibliography keys, retaining each supplied target spelling; only defined single-key `crossref` and `xref` values use the same exact lookup.
Key lists, mixed fields, file/URL values, other selected bibliographies and local references require explicit prepared edits; a shared prefix selects no work or file.
`moves` names complete repository-relative POSIX file pairs, including every selected source-store child, and preserves their bytes unless separately edited local text is supplied.
Each `updates` key names a selected Markdown, TeX, BibTeX or operation JSON file and supplies `{"edits": [...]}` or `{"expected": "complete original text", "text": "complete prepared final text"}`.
Edit spans use the [expected-text input contract](../framework/material-format.md#direct-acquisition); choose the actual local anchor separately from the bibliography key's spelling.
Prepare the selected operation item's local path, actual anchor and file/artifact correspondences together; the existing operation/material contracts validate the selected postimage before writing.
Affected U source-key namespaces include unmoved siblings and all same-batch targets after selected old positions are removed; cross-author/origin numeric occupancy and original-family continuity are checked before publication.
Original/transport identities, revisions, paths, anchors, scope, availability and unselected items remain unchanged.
Only designated mixed-text citations, anchors and references change; selecting a file and key mapping performs no whole-body substitution.
Mixed bibliography notes and literal examples retain their original text unless explicitly edited.
The agent repairs actual active consumers and writing records; token lookup supplies no automatic active-citation refusal, completeness judgment or generic notice.
It does not infer unchanged mathematics, relocation equivalence or review transfer.
Valid J/E/intake maintenance emits no generic changed-file reminder.
Generic submission checks registry prose and source links for ordinary public references, logical containment and forbidden tracking, without parsing source accounts or opening private source bytes.
Changed outgoing links and affected incoming links are checked separately in the requested view.
An incoming consumer's complete text supplies its actual links to affected public targets even when another part of that consumer changed; unchanged unrelated bad links stay outside that incoming scope.

The shared `acme.core.links.markdown_link_spans(text)` returns actual link destination spans in the original text, excluding the supported literal regions and comments.
`links.destinations(document, text)` and `acme.materials.runtime.Reader.destinations(document, text)` project those same links to local targets, with the material reader retaining source-reference validation.
For explicit working-file link checks, `links.check_files(root, selected_paths)` returns errors for the supplied public files; it does not discover consumers or assess mathematical dependencies.
The agent applies fixed-version and actual-review obligations under the [common maintenance boundary](../framework/rules/records.md#substantive-material-retention).
Checks are not Git prerequisites; `--push` is check context only and performs no network operation.

### Selected external reference reading

For explicit external-reference checks, use the existing Git-view reader and `acme.checks.scoped.external_references(tree, selections)` with an in-memory mapping of chosen repository-relative paths to field lists.
For example, with `root` bound to the actual checkout and the operation path chosen from that repository:

~~~python
from acme.checks.submission import Tree
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
For intake JSON, choose `transport.repository`, `items[N].source.repository`, `items[N].source.author` or `items[N].output_attachments[M].transport.repository`, with actual zero-based item/attachment indices.
Selecting `source.author` includes its necessary repository association and qualified original name; other operation fields remain outside that selection.
The shared JSON reader decodes the chosen object before field selection, so ordinary and Unicode-escaped spellings agree; the shared URL reader supplies its accepted scheme handling without a parallel prefix filter.
The result's `files` counts the selected objects read, `fields` counts checked identity/locator/provenance entries and `checked` lists their actual path/field, using source-text destination offsets for links.
No matching source links produces zero checked fields for that selected file; neither these counts nor a PASS covers unselected consumers.
This optional callable does not run full material/proof or intake-object validation, reconstruct old J objects/anchors, inspect private source bytes or create a durable selection record.

### Explicit selected source reading

The agent chooses any needed source check under the [source rule](../framework/rules/literature.md#selected-source-checks); a generic structural pass supplies no holding, edition, availability or byte verdict.
With `root` bound to the chosen checkout and the actual key substituted, an optional INDEX metadata read uses existing APIs:

~~~python
from acme.checks.submission import Tree
from acme.checks import literature
from acme.intake import bibliography

with Tree(root, 'INDEX') as tree:
    registry = tree.bytes(literature.REGISTRY.as_posix()).decode('utf-8-sig')
    entries = bibliography.parse(tree.bytes(bibliography.BIB).decode('utf-8-sig'))
    catalog = literature.source_catalog(registry, entries, holding_keys=['ChosenKey'])
~~~

Use `WORKTREE` or the actual commit postimage in `Tree` for that requested view; BASE-to-HEAD submission checks the final `HEAD` postimage.
The shared reader also accepts explicit `artifact_names` for a chosen artifact scope; keep unchanged necessary declarations in the selected input.
Actual local-file availability or explicitly requested byte checks concern physical files, independently of the Git metadata view.
No new command, scope file or automatic per-edit source-check requirement is introduced.

## Declaration and privacy checks

The [bounded declaration parser](../framework/material-format.md#machine-readable-declarations) prevents code, comments and HTML examples from supplying real decisions or review coverage.
Visible mathematical cells, escaped pipes and scope whitespace retain their meaning.
Structural checks do not establish mathematical sufficiency.

Public link and material-input checks classify normalized, decoded [private profile targets](../framework/rules/organization.md#machine-local-locators) before body reads or anchor lookup.
They report a public-document error and request inline-code lookup instructions, independently of private-file existence or encoding.
Ordinary public anchors and tracked/staged-secret publication errors retain their checks.
Explicit resource use may still read its needed private section.
