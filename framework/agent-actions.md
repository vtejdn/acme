# Agent Action Guide

Choose the function matching the actual human instruction, object and existing authorization under [AGENTS.md](../AGENTS.md).
Read its current governing rules and directly needed materials; reuse actual current-context reading only while its applicability remains established under the [current-rule duty](rules/workflow.md#proportionate-execution), without reading unrelated functions or the full human manual.
Topic rules own responsibilities and conditions, the [public material format](material-format.md) owns declarations and acquisition payloads, and [script documentation](../scripts/readme.md) owns optional interfaces and side effects.

## Scope and instruction handling

Apply the [core principles and interpretation](readme.md#core-principles-and-interpretation) to all actions and use them to resolve framework conflicts, omissions, ambiguity and discretionary choices.
Identify the responsible Task, material, manuscript, repository or selected paths before acting.
Interpret a continuation in that object's actual context, evaluate explicit conditions before dependent actions, and order requested work by its dependencies.
Clarify only missing information that determines the work while completing independent authorized work.
Apply [instruction and policy scope](rules/preferences.md#instruction-scope) when distinguishing a correction, a personal choice, a Task change or separately authorized framework maintenance.

## Start a work round

Before starting or continuing affected work, read the current local [version metadata](version.json) and entrances, select the actual activity and apply the [current-rule reading duty](rules/workflow.md#proportionate-execution).
If the local version or applicable rule text has changed, or only an old summary, memory or uncertain prior reading is available, actually reread the current needed entrances and governing rules before dependent operations.
Do this independently of same-day query reuse, an unavailable result, disabled checks or an offline instruction.
Subagents reuse the main agent's metadata result and read the current rules needed for their own assignment.
A newer official version that remains uninstalled leaves the current local rules in force.

Apply the [official version-check rule](versioning.md#official-version-check) before the selected work.
Read repository/config.json and the ignored repository/framework-update-check.json; honor an explicit offline instruction and the repository Boolean setting.
Reuse the main agent's actual result in subagents and reuse a current UTC-day success or unavailable result without another request.
For an enabled new-day attempt, use the [bounded metadata helper](../scripts/readme.md#official-framework-version-check) or the same explicit read-only operation; its short cache coordination precedes one network request, never a clone or framework replacement.
The bounded public HTTPS metadata read requires no Git remote, gh login or optional connectivity skill; apply actual network permissions and explicit offline instructions.
If the setting is invalid, the request fails or the cache cannot be saved, report the specific limitation and continue authorized work without claiming a confirmed public version.

When a verified newer version has not been presented, tell the human the installed and available versions, link the official repository and ask whether to arrange the upgrade.
Continue the current assignment while the choice is pending.
After actually presenting the reminder, record only that notification fact through the helper.
On an explicit recheck, force a fresh bounded attempt while retaining the actual notification state.
On an explicit disable request, set framework_update_check to false in this repository's configuration, preserving other fields; on enable, set it to true.
Keep this repository setting out of personal profiles.

A request to upgrade selects separate framework-maintenance work under [instruction scope](rules/preferences.md#instruction-scope).
Identify the actual official version, local files and material-migration needs before applying it, preserving research content and current Task/E conditions.
A reminder, silence or metadata response does not authorize replacement files, version advancement, publication or research resumption.

## Install the framework

For an authorized fresh installation, clone the [official starting repository](https://github.com/vtejdn/acme) or copy its files to the selected location using ordinary tools.
Copying without Git omits the source .git and does not initialize Git; cloning follows Git's ordinary history and configuration behavior.
Inspect the actual destination and selected files, preserving an existing checkout's .git, index, refs, configuration and unrelated files while resolving actual file conflicts.
An existing research installation follows the [upgrade action](#upgrade-installed-framework), without copying blank registries over its research state.
Copying an existing research repository is not fresh framework setup and supplies no new identity, reattribution or intake exemption.

For a new personal project copied from the official blank repository without Git, prepare repository: null unless the human supplied a name, and do not accidentally adopt the official acme repository name.
An absent or null name permits local registration, research and receiving selected public material without uploading local research content.
Before research writing or Git delivery in a Git-managed project, obtain the human-chosen or explicitly confirmed repository name and complete the actual checkout binding, reusing an existing real project registration.
Apply the [repository name rule](rules/identity.md#repository-names-and-use-environments) through ordinary scoped configuration and current README edits; preserve human keys, material identities and historical source facts.
Keep reading and necessary setup repair available while the name is missing, without reinitializing the project or inventing a name from the folder or author.
An existing shared-repository clone keeps its real identity, registrations and materials.
Complete human registration, any Git checkout binding and the independent License credit under the [setup action](#set-up-repository-or-human-identity).
An authorless copy or clone remains preparation, with no selected research Task or execution authority.
Do not run research.py init over an already copied config.json or delete configuration merely to satisfy that optional Git-bootstrap helper.
Create .tmp/, intake/, profiles/, execution/ and local source storage only when actually needed under their responsible rules, without placeholder files to force Git to retain empty directories.
The ordinary guides and their diagrams remain alongside the common framework files; copying carries no personal profiles, private holdings or research authorization from the official blank source.
Cloning does not authorize pushing to an inherited remote or automatically changing that remote.

Publishing common files from a development repository to the official starting repository requires its actual maintenance and remote-operation authority.
Inspect the selected content and keep development blueprints/tests, local profiles, temporary work, private holdings and actual research out of that starting tree.
Use ordinary copying and native Git without a permanent shipped-file inventory or installation receipt.

## Upgrade installed framework

Apply the [version and upgrade rule](versioning.md#upgrading-an-installed-framework) under an explicit upgrade assignment, separately from the daily metadata read and fresh installation.
Identify the installed version and selected official target; obtain its fixed source in owned root `.tmp/` and verify agreement among tag, commit, version metadata and target-version note.
Without Git, use available public source evidence with an archive or selected fixed-source files and ordinary recovery copies; Git initialization or a local clone is not required.
Read applicable intervening notes, inspect their combined local paths and direct consumers, and prepare final target files with only genuinely ordered adaptations.
Preserve recoverable affected contents, local customizations, unrelated work, the actual named or unnamed configuration, research and effective Task/E conditions without requiring a clean worktree, stash, preliminary commit or empty reinitialization.
Judge mixed public-file merges and retired files by their actual local role, preserving existing human-document and authorship boundaries.
Finish required adaptation and checks before marking the target installed version; on failure restore this operation's changes or report actual incomplete restoration while preserving foreign work and necessary recovery content.
Reread new applicable rules, report actual from/to versions, target commit, checks and remaining limits, then perform existing creator cleanup; an upgrade grants no research resumption.
Ordinary authorized retrieval, editing and selected checks need no additional routine approval or mandatory installer.

## Set up repository or human identity

Before first registration, ask: "What local author key should identify you in local literature and other authored-material paths, and what independently chosen name should appear in the repository's License attribution?"
Explain that a key such as Alice-Smith uses ASCII letters, digits and internal hyphens without spaces or underscores, while the License name such as Alice Smith may contain spaces and Unicode and is stored as display_name.
Reuse values explicitly supplied for the actual setup, ask only for missing values and request an author-selected valid replacement for an invalid key rather than changing it automatically.
Apply the [identity setup rule](rules/identity.md#stable-keys-and-local-attribution) before registering or binding, keeping the key, attribution name and supplied Git/GitHub identities separate.
After setup, use the selected name for the receiving License credit through a bounded text edit preserving the existing license and notices.
The optional init interface requires the independent --display-name; an authorless fresh copy or clone remains empty and unbound until actual registration.
This setup selects no research Task or execution authority.
For personal use in a folder without Git, use one explicitly identified local human and existing author registration; no Git binding, signature or local multi-author arrangement is required.
Keep an authorless folder as preparation until that first registration, and use the folder's own human rather than an enclosing checkout's binding.
Ordinary local file, material and registration operations retain their actual author and source duties, including external originals' attribution and separately authored corrections.
Git-dependent helpers remain optional and state their actual prerequisites.

## Start or continue research

For a new objective, read the [Task setup rules](rules/workflow.md#new-task-setup), likely existing contracts and actual human assignment.
Reuse an adequate existing Task or establish its precise question, hypotheses, quantifiers, scope, completion criteria and actual proposed/active decision.
Setup prepares an ordinary family's minimal non-running E; a joint coordination T has no E, and neither setup creates execution or a fabricated review.

For continuation, read the selected T contract/decision, its stable E's current stopped conditions, applicable operator policy, current S and directly needed C/D/J/source evidence.
For a joint goal, first resolve the actual human's appropriate individual T and its adopted exact common contract under the [joint-Task rule](rules/tasks.md#joint-tasks-and-participation); clarify a real unresolved choice among several individual Tasks instead of starting several.
Follow [execution rules](rules/execution.md#current-contents-and-retained-limits) before autonomous advancement.
Use one responsible main agent and one stable E for the Task family; a new chat, revision or policy expiry does not reset allowance or resume a stopped run.
An actually authorized continuation prepares the relevant exact Task reference and current conditions directly; a pointer update preserves stops unless actual resumption is authorized.
If authorized work may proceed, advance its next useful step and retain actual results, failures, gaps and continuation points.
If a stop or missing authority prevents advancement, preserve current findings and report that actual boundary.
Method changes and strategy priorities may adapt within the assignment unless the human explicitly fixed them; they do not change the objective or completion criteria.
Apply [research coordination and Preparation](rules/workflow.md#records-review-and-handoff): the main agent coordinates available harness subagents, dependencies, shared resources, writes, necessary review and required retention/closeout while maintaining an overall understanding of the authorized Task.
Delegate the current question, useful existing entrances and working Draft for Preparation; the subagent judges search, reading, applicability and sufficiency, retaining concise judgments and direct original-material locators in the [Draft](rules/ledger.md#working-drafts-and-fixed-findings).
Reuse applicable Preparation, allow the same subagent to continue Draft research within an initial or extended assignment, and arrange suitable parallel work requested through ordinary coordination messages.
Keep shared Task/E limits and the actual [independent-review boundary](rules/proof-audits.md#review-arrangements); proof development or inherited substantive development context prevents independent review of that proof.

## Develop, register or reorganize mathematics

Read the question, candidate material, actual inputs and likely existing homes before applying the [common content decision](rules/records.md#substantive-material-retention).
Then apply [work obligations](rules/workflow.md#work-obligations) and the actual kind's registration, version, source, reproduction and review rules.
Develop substantive arguments in D or another responsible mathematical material and continued programs directly in J.
Use existing adequate C/J/R/L/U content rather than creating another account for allocation or progress chronology.
Retain complete necessary arguments, hypotheses, meaningful failed approaches, native inputs, source applicability and actual unresolved obligations.

Before substantial proof investment, apply [knowledge reuse](rules/knowledge-reuse.md#reuse-before-proof); a recognized established result triggers its source-check duty even during exploration.
An open conjecture or conditional investigation need not already have a proof or completed review, but acceptance requires its real evidence and resolved applicable obligations.
Distinguish an actual new statement/contract, a substantive revision, an unchanged-mathematics decision and routine maintenance under the [record rules](rules/records.md#identity-and-versions).
For a new fixed or continuing S family, maintain its actual next unissued [allocation state](rules/identity.md#allocation-and-concurrency); revisions retain their family and D keeps its separate reusable-address boundary.
Actually added C/T decisions use their real UTC minute time, while reading or reselecting an existing decision preserves genuinely known calendar precision.
Keep fixed predecessors and exact decision anchors; navigation derives the responsible current selection.
For an organizational Claim-role change, preserve the selected assessment and exact input/review relations and scopes under the [role rule](rules/claims.md#claim-role), without a new proof version or retrospective review-binding retrofit.
Return the resulting material and its actual status, with any missing evidence explicit.

## Close a round

Read the round's changed mathematics, computations, sources and directly affected consumers under the [workflow](rules/workflow.md) and common content decision.
Check the claims being delivered and relevant inputs, reusing adequate existing evidence; retain useful partial results and failures at responsible homes.
Repair actual references and derive affected navigation after source edits settle.
Retire a redundant D only after checking its actual historical uses and preserving any necessary content under the [draft rule](rules/ledger.md#working-drafts-and-fixed-findings).
A setup-only residue whose mathematics is already fixed needs no replacement account or move receipt.
Return established results, remaining obligations and the next continuation point.
Round closeout neither resolves the whole Task nor resumes research after an instruction to stop at that boundary.

## Complete, pause or stop a Task

For completion, compare the actual deliverable with the original T hypotheses, quantifiers and every completion criterion under the [Task rules](rules/tasks.md#task-records).
Check the full support chain and applicable [completion review](rules/proof-audits.md#completion-and-verification-boundaries), reusing adequate fixed inputs and compatible reviews.
Arrange the required independent review at key proof points and for the full chain after completion; retain actual unfinished review obligations.
Record completion only when the actual contract is satisfied; otherwise state the precise unresolved criterion without enlarging the result.

For pause or stop, preserve available results and a usable handoff and record the actual instruction at its responsible E/T scope under the [execution rules](rules/execution.md).
Distinguish an execution stop, human lifecycle pause, blocked mathematical obligation and completion.
An instruction to finish the current work and then pause permits that closeout, not a fresh research round.

## Review specified work

Identify the actual source, manuscript, Claim, argument, computation or Task and the requested review depth.
Read exact versions, hypotheses, arguments, dependencies and existing findings under the applicable [proof-review](rules/proof-audits.md), [source-audit](rules/literature-audits.md) or [manuscript-review](rules/writing.md#manuscript-review-and-citation-records) rules.
Inspect the requested whole scope; do not substitute structural checking for mathematical scrutiny or silently expand a narrow source inspection into a full proof audit.
Reproduce decisive computations or behavior where needed rather than mechanically repeating all prior tests.
Source audits exclude associated Lean code unless expressly included; retain any reliance on unchecked code as a review limitation.
Keep formal project findings in R for every actual agent relationship, source inspection in U and manuscript-specific findings in their document review home.
New or substantively revised findings declare their actual relationships explicitly; a genuinely new C/T acceptance selects findings with both matching relationship rows and exact required bindings, without backfilling unchanged historical findings.
For independent review use a separate agent outside substantive proof development with isolated mathematical context; supply fixed inputs directly without the development discussion or its mathematical summary.
After an independently identified gap is repaired, arrange independent re-review of the correction and affected chain; a substantive repair contributor cannot independently review that repair.
Return actionable findings, inspected scope and limitations, distinguishing source inspection, proof review, build success and formal verification.
A review request does not itself authorize substantive editing of another author's material; actual conflicts use the maintenance boundary below.

## Prepare or reuse literature

Read existing responsible mathematical/source evidence, bibliography, registry, edition facts and any [searchable contents](../mathematics/literature/contents/readme.md) before obtaining missing material.
Apply the common [source-preparation workflow](rules/literature.md#source-preparation), [knowledge reuse](rules/knowledge-reuse.md) and [complete definition registration](rules/definitions.md).
Judge the actual work/edition, needed passages, source association and inspection depth; bibliography registration, a contents hit or a matching hash does not establish theorem applicability.
Choose available reading, extraction, rendering or OCR capabilities under the [host-capability responsibility](rules/workflow.md#agent-and-tool-responsibilities), checking an alternative source format's version and applicability when needed.
Report a capability-limited required inspection to the human author with its concrete scope, effect and remaining action, and continue unaffected work under the existing [progressive-reading](rules/literature.md#progressive-reading) and [temporary-storage](rules/organization.md#temporary-storage) duties.
Reuse an adequate complete U/C/L account in place and retain any unresolved edition, passage, hypothesis or inspection gap.

When acquisition is authorized, fetch supplied addresses and inspect an unestablished response before registering the explicitly supplied local bytes and chosen bibliography fields.
For first actual retention, inspect the logical source entrance and applicable private storage arrangement; if mathematics/literature/pdf/ is absent and unconfigured, create an ordinary ignored directory there and continue without another storage-choice question.
Preserve existing ordinary storage and valid top-level junctions; report a broken, conflicting or inaccessible entrance instead of replacing it or creating another store.
Search-only and bibliography-only work need no storage setup.
Keep requested/obtained literal URLs, fingerprints computed from actual locally obtained bytes, actual edition facts and limitations at the sole registry; bibliography owns publication identity.
Never-obtained artifacts have no fingerprint; preserve an established local baseline through later absence without adopting supplied or sender-local hashes.
Follow the [source-input boundary](rules/literature.md#artifact-source-association): missing input cannot borrow receiver bytes, and an occupied destination preserves its existing bytes/account while reporting the conflict.
Select actual accounts and necessary direct relationships before strict checks; ambiguous competing declarations require judgment from the concrete candidates.
For an account change, inspect the actual declarations and evidence, choose and explicitly prepare the needed edits, and preserve comparison, contents, holding context and qualifications.
Use the [Artifact/Resource contract](rules/literature.md#local-pdf-storage) and [holding declarations](rules/literature.md#actual-source-holdings), with optional [local-registration interfaces](../scripts/readme.md#local-source-retrieval-and-registration).
Inspect the persisted account and selected readers against the supplied current facts; resolve actual competing declarations before publication.
PDF, original HTML and resource availability are independent outcomes; required authored bodies and indispensable program inputs must exist.
Acquisition-only failure records known bibliography/access facts without a new U or invented inspection; preserve adequate existing source evidence at its actual scope.
Inspect actual HTML content and required resources without treating an error page or dynamic shell as an acquired source.
Preserve native sources and actual availability/readability limitations.

Prepare or reuse the actual edition's searchable contents when a real contents list is supplied, including future-use sources without a Task, and maintain exact registry/source links under the [contents rule](rules/literature.md#searchable-contents).
Inspect the actual edition and contribution extent when choosing a [complete or partial holding](rules/literature.md#actual-source-holdings); a complete contribution needs no redundant standalone PDF.
For bibliography maintenance, identify actual work correspondence and consumers, then prepare the chosen keys, file moves and necessary local reference edits under the [renaming rule](rules/literature.md#coordinated-key-renaming).
Confirm and correct a discovered naming misuse under the abbreviation rule, even for an established key, while preserving legitimate original year bases, allocations and collision suffixes.
Choose exact affected artifacts, U bounds and active citations; literal examples and original-source locators remain outside that selection unless actually adopted for change.
Preserve unselected examples and original-source locators, check active citations and update necessary writing records; structural checking does not decide citation completeness.
Return actual acquisition, inspection and contents results separately, including unavailable items and unchecked source-proof scope.

## Write or revise a manuscript

Read the actual active TeX, responsible author's applicable choices, manuscript purpose and direct source/review inputs under the [writing rules](rules/writing.md).
Keep an explicitly user-designated presentation home and its document choices; apply the same source, build and review responsibilities without creating a Task merely for directory naming.
Apply exactly four writing layers: general rules, author-wide policy, applicable subfield policy, then manuscript-specific choices, overriding only conflicting portions.
A changed local operator does not adopt another author's policies.
Perform proportionate source preparation and definition registration; source observations remain evidence rather than a fifth writing layer.
Use actual own/coauthored source designations or manuscript-specific permissions under the [text-reuse rule](rules/writing.md#default-reuse-permission); a style-only reference grants no text reuse.

Preserve precise mathematics and attribution, reconcile a discovered substantive proof change with its responsible mathematical material, and update actual citation uses, writing choices, review findings and latest build facts at their existing manuscript homes.
Map every current TeX citation use, including plainly unchecked or partially checked entries with actual evidence and gaps; verified application still requires adequate source evidence.
Reuse adequate fixed C/L source evidence directly without manufacturing a duplicate U; an unresolved support gap remains an obligation.
Use current TeX to determine actual citations, with exact designated edits for mixed text.
Compile or inspect layout as applicable to the requested work and actual author instructions, reporting exactly what was checked.
Select available build and inspection capabilities under the [host-capability responsibility](rules/workflow.md#agent-and-tool-responsibilities), reusing applicable project settings and the [local-build convention](rules/writing.md#reproducible-local-builds).
If a required build or check remains unavailable, report the specific affected scope, consequence and useful next action to the human author while continuing independent authorized work.
Return the manuscript result and remaining mathematical, citation, build or layout limitations; editing TeX does not by itself update a Claim or complete a Task.

## Develop or reproduce a computation

Read the actual J question, native programs/inputs, parameters, arithmetic mode, earlier useful results and consuming mathematical reduction under the [computation rules](rules/computations.md).
Choose suitable methods, runtimes, libraries and other tools under the [computation-tool responsibility](rules/computations.md#computation-tool-selection), respecting the actual assignment, project requirements and environment constraints.
Keep continued programs in `mathematics/computations/programs/<J>/` and generated results in the ignored `mathematics/computations/outputs/<J>/`.
When reproduction is needed, rerun the chosen output set in that same J after preserving necessary inputs, non-reconstructible witnesses and earlier results still consumed by the check.
Safe overwriting and removal of reproducible output are allowed with coherent consumers; ordinary reading or maintenance does not require rerunning it.
Use an acquired program's actual qualified J for self inputs/outputs and explicit paths for genuine cross-J dependencies.
Keep necessary reproduction context, meaningful failures and actual limits without persistent mathematical digest gates or an archive for every run.
Return the real command, inputs, result and checked scope; finite or floating-point observations do not prove an unrestricted theorem.

## Maintain shared materials or resolve a conflict

Read the actual change, responsible material, consumers and [common content decision](rules/records.md#substantive-material-retention).
Apply the operative [collaboration and conflict rule](rules/identity.md#collaboration-maintenance-and-conflicts), including its preserved author, mathematical, source and review boundaries.
For an old review container, apply only the bounded [retirement exception](rules/proof-audits.md#review-retirement), preserving necessary evidence and historical adoption facts and preparing its non-reuse allocation bound before deletion.
Repair responsible shared registration and derived navigation directly; authored bodies use the same-human and separately attributed correction boundary without a per-author approval process.
Resolve an administrative conflict using the core principles and applicable topic rules; act directly when they determine the choice, and report only a remaining decisive gap requiring human intent, authority or facts.
For a substantive mathematical conflict, identify competing statements/evidence and affected materials and obtain approval for the scoped recheck before undertaking it, reusing existing explicit approval for that same scope.
That approval alone neither transfers authorship nor authorizes substantive editing of another author's material.
Preserve both sides' actual evidence, and keep substantive contributions in their responsible author's own materials.
Ordinary authorized research and reviews retain their existing authority; the conflict procedure is not a universal approval step.
Return the repaired administrative result or concrete remaining conflict and needed decision, preserving activity-specific roles and another human's Task/E.

## Acquire material from another research repository

Use [intake](rules/intake.md#scope-and-routing) for distinct research repositories; another registered human in the same repository is direct collaboration.
Read the exact source commit, selected mathematical unit or useful R finding, intended scope, necessary inputs and actual original provenance before preparing explicit selections.
The intake source is an identified public GitHub repository at a full fixed Git commit; a receiving no-Git personal folder may remain unnamed.
Use actual authorized public source reads and ordinary file operations when Git is unavailable; the optional Git-based source helper retains its own source-access prerequisite.
Judge preservation, adaptation and reuse, write the receiving material and required source facts, and inspect the actual result and directly affected references.
Ordinary reading, editing, copying and existing registration/allocation mechanisms suffice; a dedicated command, prepared-text payload, mapping plan or uniform batch protocol is not a condition of valid intake.
R has no mandatory C target; choose actual necessary targets, reuse and limitations from the inspected finding, without acquiring every binding or citation.
Receive needed S/D mathematics in a suitable fixed home and a necessary joint T contract under the [Task rule](rules/tasks.md#joint-tasks-and-participation), without another human's ordinary Task/E authority.
Select bibliography targets and U positions across all authors/origin prefixes, then write the selected receiving content and necessary provenance under the [material format](material-format.md#direct-acquisition).
Before finalizing U receipt or invoking the optional helper for it, first complete the ordinary [original-acquisition procedure](rules/literature.md#acquisition-before-u-reception) for the actual work and inspected edition.
Reuse an adequate receiver-local original or obtain, validate and register it independently; reuse an adequate same-work/edition outcome for several units.
On failure, record the actual source/access outcome and directly report the work/edition, known address, failure, local availability and resulting limits to the human author.
Retain useful authorized U evidence and its inspection limits without transporting sender-private originals or accounts, inventing fingerprints or treating the failure as a mathematical verdict.
Check actual resulting files, references and affected U positions, and retain the operation once at its responsible intake home.
Coordinate affected writes only as needed for coherent results; optional helpers apply their input and publication protocols only when chosen.
Private literature documents and their local registry/holding accounts are outside intake; reject the retired source/holding/update inputs before opening a private file.
Preserve an established original registered repoN/family's local number across physical versions and reject an occupied prepared position without silently renumbering the body.
Fresh receiving positions respect and advance their actual next unissued namespace bound, rather than reusing a retired number or allocating another family for an existing correspondence.
An explicitly selected actual independent finding still in historical L needs complete prepared receiving R with its true targets, scope and limitations; available source content requires no source-repository upgrade.
Ordinary whole historical L reading and unselected old findings retain their scope.
Select indispensable J inputs and any [output attachments](rules/intake.md#computation-output-attachments) with actual provenance separately from the tracked program revision.
Before an explicit J source refresh, confirm the same original, inspect the selected current scope and maintain necessary retained inputs and actual consumer references under the [intake rule](rules/intake.md#homes-and-independent-reuse).

Apply the common [adaptation rule](rules/records.md#receiving-and-adapting-selected-content), preserving complete necessary selected mathematics and the single original human through adapted text, local numbering, justified splits/combinations and onward transfer.
Keep the actual source version and selected scope separate from the receiving kind, line and version; use the existing operation for per-unit provenance.
Localize only designated references or exact chosen mappings; unselected relative background links to actual tracked files retain exact sender-fixed locators without automatic upstream tracing.
For targets absent from the selected sending Git tree, preserve useful source-only reference context and actual limits, without assigning unversioned bytes to the material's commit.
Obtain or reproduce necessary input within the actual authorization, or retain its unresolved need at the consumer; omit obsolete mentions with no remaining mathematical, evidence or reproduction purpose.
Complete adaptation through ordinary reading, editing and copying or an optional helper supported by the chosen actual inputs, without historical-layout recognition or another current output home.
Keep each actual Markdown file's own internal locators at its receiving location, and designate necessary existing inputs explicitly rather than invoking receiving-history discovery for background links.
Translate explicit foreign-number locators only through prepared correspondence; unmapped ones remain raw context qualified by sender and fixed sending revision.
Prepare external repoN/authorN records and explicit receiving C/T/R/L/J serials under the [external identity contract](material-format.md#local-external-identities-and-prepared-correspondence); another similarly named file is no substitute.
Retain authored inspection limits, genuine unmapped references and actual missing necessary evidence at the consumer.
Sender-local document references remain explicitly unacquired original-local context; acquire needed original text independently through ordinary authorized source preparation.
Record the actual operation once in intake, preserving historical J scopes without asserting their current availability, automatic adoption, mathematical equivalence or imported execution authority.
For local maintenance, prepare the selected operation item's exact path, actual anchor and file/artifact correspondences together with its material; validate the selected postimage before publication and preserve original/transport facts, scope, availability and unselected items.
Return the chosen installed scope and limitations, preserving the source's actual inspection and review depth.

## Import one's own selected content

Establish the actual registered local human and explicitly selected own content under the [personal-import rule](rules/intake.md#personal-import).
Read selected units, actual constituents, necessary forward mathematical dependencies and adequate receiving candidates under the common adaptation and existing-decision rules.
Prepare ordinary local text, file arrangements and temporary locators; follow Task to needed S/C/L/R/D/J and other support to relevant U without reverse consumers or a whole-library expansion.
Complete the action through ordinary reading, adaptation, editing, file copying and existing registration/allocation mechanisms, inspecting the actual resulting content and affected references.
No dedicated command, plan JSON, complete dependency graph, full input snapshot or uniform batch transaction is required.
Reuse adequate local or already-intaken own material without identity conversion, duplicate local copies or acquired-history cleanup.
Dispatch an actually needed other-author dependency separately through intake, including S/D mathematics, T-only/J-only R and a permitted joint parent.
Resolve a participant's exact joint parent or prepare its complete standalone contract under the Task rule; preserve real obligations, attribution, review scope and effective execution conditions.
Install only chosen applicable settings, manuscript sources and required native files in their appropriate homes, with proportionate affected build checks and no unrequested Task.
For callers choosing the optional `material.py import` helper, its [input plan](material-format.md#personal-import-input) and publication protocol apply only to that interface.
Coordinate affected own and foreign writes only as needed for coherent final references.
Own content receives no external identity, intake operation, import-source record, permanent mapping or fabricated new decision.
Read the actual source and local execution conditions and prepare or reuse the stable E under the [execution rule](rules/execution.md#current-contents-and-retained-limits), choosing only necessary effective conditions rather than automatically transporting the source E.
Preserve actual stops/allowances; import alone starts no research, grants no parallel allowance and selects no autonomous Task.
Return actual retained content, foreign acquisition scope, unavailable dependencies and remaining mathematical/build obligations.

## Commit or push requested work

Read [serial delivery](rules/identity.md#submission-checks), the human-registered repository name, requested paths, existing index, actual operator/signature and intended branch/tree.
Coordinate one stable delivery interval, preserve unrelated staged work and contributor identities, stage the intended deliverable, commit and confirm the actual resulting tree.
Reinspect the affected delivery scope if relevant bytes or the index change; draft work may be committed with truthful status.
For an authorized push, establish the actual target and account/channel under the [connection responsibilities](rules/identity.md#git-and-github-connection-checks), verify the remote/base relationship and outgoing identities, push the intended tip and verify the remote result.
At actual project-remote setup, a relevant target change or a remote operation needing fresh facts, apply the [non-blocking name suggestion](rules/identity.md#repository-names-and-use-environments) for that selected GitHub project.
Keep a differing local name unless the human chooses to update it; official-source, intake-source and reference-only upstream names do not select the repository name.
Ordinary delivery grants no force-push or history rewrite.
Apply pending-batch ordering and its smallest concrete blocker-repair exception within the authorized remote-delivery sequence defined by the [identity rule](rules/identity.md#submission-checks); unrelated unpushed commits impose no remote check on local-only work.
Plain commit/push performs delivery without launching framework regressions, whole-library scans, recursive proof review or source-store hashing.
Reuse applicable verification and perform separately requested checks at their actual scope.
Return the actual commit or confirmed remote result and remaining worktree state.

## Run an explicitly requested check

Identify the requested object and actual working files or Git view under the [operation-level check rules](rules/identity.md#explicit-material-checks).
Use the relevant [tool interface](../scripts/readme.md) when useful and inspect its actual results; an unstaged repair cannot fix a submitted view.
Select necessary incoming consumers and their exact target locators through scoped searches and reading; an outgoing-link check does not discover unchanged consumers.
For a source-relationship check, choose the needed keys or artifacts and actual view under the [source-check rule](rules/literature.md#selected-source-checks); an ordinary structural pass supplies no source verdict.
An explicitly requested whole-store inventory retains that scope, while ordinary selected source/link work does not acquire it implicitly.
Keep structural errors, source-byte facts, mathematical findings and review conclusions distinct; a structural pass certifies neither semantic preservation nor citation completeness.
Repair and recheck an actual uncovered defect at its affected scope without stacking unrelated scans after every write.
Return the inspected scope, actual findings and limits.
