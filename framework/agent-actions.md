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
When actually selected content or input is incompatible with current rules, read it and autonomously choose and complete suitable bounded adaptation within the current assignment and existing authority.
Use ordinary reading, editing, current receiving preparation, direct-reference repair or another adequate tool path; an optional helper's refusal supplies a concrete limitation rather than a requirement to stop all work or upgrade the source repository.
Judge the needed scope, responsible home, retention/reuse, actual mathematical changes and checks under the [content and adaptation rule](rules/records.md#receiving-and-adapting-selected-content), preserving authorship, fixed evidence, true provenance and Task/E limits.
Pure metadata, layout or link maintenance creates no mathematical decision, version, review, acquisition or timestamp; genuine changes retain their applicable obligations.
Apply the [common literature registration and source-preparation rule](rules/literature.md#source-preparation) to works of confirmed identity and reference value identified during any authorized repository action or related discussion.
Apply the [common preparation-input responsibility](rules/workflow.md#prepared-work-and-input-applicability) when publishing declarations, associations or decisions that rely on earlier content.
When a repository question or discussion produces mathematics worth retaining, apply the same pre-delivery preservation rule as for an exploration round within the actual author and write scope.
See [Closing an Exploration Round](rules/workflow.md#exploration-round-closeout).
Clarify only remaining decisive intent, authority, identity correspondence or necessary facts while continuing independent authorized work, without a routine adaptation approval, whole-library cleanup or compatibility parser.

## Start a work round

Before starting or continuing affected work, read the current local [version metadata](version.json) and entrances, select the actual activity and apply the [current-rule reading duty](rules/workflow.md#proportionate-execution).
If the local version or applicable rule text has changed, or only an old summary, memory or uncertain prior reading is available, actually reread the current needed entrances and governing rules before dependent operations.
Do this independently of same-day query reuse, an unavailable result, disabled checks or an offline instruction.
Subagents reuse the main agent's metadata result and read the current rules needed for their own assignment.
A newer official version that remains uninstalled leaves the current local rules in force.

For ordinary first installation, apply the [empty-target conditions](#first-install-empty-target) before source preparation, target writes or project-branch integration.
Known nonempty targets stop that installation under its responsible action instead of entering the general work-start merge below.

For a Git-managed working repository with a configured remote, apply the [common work-start update](rules/workflow.md#shared-repository-work-starts) and its [target, authority and integration rule](rules/identity.md#shared-repository-updates-and-integration) after establishing the assignment, current branch and explicit limits from the necessary local entrances.
The main agent proactively determines the applicable project target and protected work, obtains fresh branch facts and needed commits, completes necessary authorized local integration, then reads affected current rules and inputs before substantive task work.
This covers single-human projects, ordinary and joint research, writing, literature work, transfer preparation, review, maintenance, framework development and upgrade preparation; continuous steps and subagents in that working copy reuse the actual result.
Without Git or a configured remote, perform no project update or automatic setup; explicit offline, read-only or fixed-input limits and actual failures follow the common rule.
Apply the [common connection-recovery responsibility](rules/workflow.md#connection-recovery) within the authorized update before treating a connection failure as an unresolved obstacle.
The daily framework query below and an earlier same-day project query do not replace that responsibility.
Authorized repository writing with an applicable project remote also follows the [common delivery default](rules/identity.md#submission-checks), within its actual scope and explicit human limits.

Apply the [official version-check rule](versioning.md#official-version-check) before the selected work.
Read repository/config.json and the ignored repository/framework-update-check.json; honor an explicit offline instruction and the repository Boolean setting.
Reuse the main agent's actual result in subagents and reuse a current UTC-day success or unavailable result without another request.
For an enabled new-day attempt, use the [bounded metadata helper](../scripts/readme.md#official-framework-version-check) or the same explicit read-only operation; its short cache coordination precedes one network request, never a clone or framework replacement.
The bounded public HTTPS metadata read requires no Git remote, gh login or optional connectivity skill; apply actual network permissions and explicit offline instructions.
If execution permissions deny an enabled, non-offline official metadata read, use the [official-query permission handling](versioning.md#official-version-check).
If the setting is invalid, the request fails or the cache cannot be saved, report the specific limitation and continue authorized work without claiming a confirmed public version.

When a verified newer version has not been presented, tell the human the installed and available versions, link the official repository and ask whether to arrange the upgrade.
Continue the current assignment while the choice is pending.
After actually presenting the reminder, record only that notification fact in the existing four-field cache through the optional helper or adequate ordinary maintenance under the [cache rule](versioning.md#official-version-check).
The agent judges the real presentation and its relation to current known facts; notification call arrival, numeric version order and reminder_due do not establish that order.
When choosing the helper, supply the explicitly observed notified_version premise through its [required input](../scripts/readme.md#official-framework-version-check), with null only for an actually observed empty field in a valid cache.
If the premise has changed, preserve the reported current fact and judge any necessary follow-up from actual knowledge, without automatic retry, repeated presentation, a network recheck or a new approval step.
Preserve concurrent cache changes and the actual attempt/result/version fields; do not blindly overwrite the cache or create another notification register.
On an explicit recheck, force a fresh bounded attempt while retaining the actual notification state.
On an explicit disable request, set framework_update_check to false in this repository's configuration, preserving other fields; on enable, set it to true.
Keep this repository setting out of personal profiles.

A request to upgrade selects separate framework-maintenance work under [instruction scope](rules/preferences.md#instruction-scope).
Identify the actual official version, local files and material-migration needs before applying it, preserving research content and current Task/E conditions.
A reminder, silence or metadata response does not authorize replacement files, version advancement, publication or research resumption.

## Install the framework

Before creating a target or source-staging directory, retrieving content, initializing Git or merging, determine the actual authorized purpose and final installation target from the human request, workspace and target contents.
An official page, repository name, example or empty registry alone supplies no installation or new-project instruction.
Use the actual selected project root, rather than creating an acme child project from the official repository name.
The shell's current subdirectory need not be that root; use actual project facts and, when available, native Git root information, applying the same protection to a .git directory or worktree pointer file.
Use an already clear target directly; preserve relevant contents and clarify only a decisive target, authority or intent conflict instead of silently changing the destination.

An existing ACME installation stays at its project root and follows the [upgrade action](#upgrade-installed-framework) when an upgrade is authorized, without an empty-target requirement; ordinary reading or use does not itself select an upgrade.
Joining existing research collaboration may clone that actual research repository and retain its history, identity and materials.
Framework development and actual explicit clone instructions retain their requested target and ordinary Git behavior; those uses neither recommend official cloning for ordinary installation nor require an exception approval.
Copying an existing research repository is not fresh framework setup and supplies no new identity, reattribution or intake exemption.
Source inspection, backup, review, upgrade preparation and framework maintenance keep their actual source purpose and identity, without treating a source copy as an installed project or creating a new-project registration or credit.

<a id="first-install-empty-target"></a>

For ordinary first installation, confirm that the actual local project root and any existing or explicitly selected target project remote are empty apart from Git setup, before source staging in `.tmp/`, extraction, copying, initialization or project integration.
An existing `.git` administration directory or worktree pointer and native Git configuration may remain; project commits, staged content and other actual files, including untracked or ignored files, make the local target nonempty.
A clean `git status` does not establish emptiness.
Use native Git facts and an allowed read-only query such as `git ls-remote` to determine whether the target project remote has project history or content, not merely whether it has an upstream or a branch matching the local branch.
Official source retrieval and reference-only remotes are not target project remotes for this condition.
Check only the local target when there is no applicable target project remote.
An explicitly specified target project remote still requires an allowed read-only check when the local directory has no Git setup or no Git executable is available.
Create no Git repository, remote or initial commit for this check.

As soon as either side is known to be nonempty, preserve files, index, configuration and both histories, stop this installation and report which side contains what project work to the human author.
No check of the other side is then required, and do not pull or merge, clear or move contents, or switch to a child or different directory to continue installation.
Handle connection failures under the [common recovery responsibility](rules/workflow.md#connection-recovery) within the empty-target check's authority.
If an applicable remote remains unconfirmed within the actual offline, tool, permission or query limits, preserve the target and report the unknown fact, resuming installation only with sufficient empty-target evidence.
Only after all applicable targets are confirmed empty, install the selected official version or fixed-commit files at that project root and complete necessary setup.
An explicitly selected new root that does not yet exist may be created after confirming any applicable remote condition.
When Git is wanted, use or establish the human project's own repository within actual setup authority, without adopting official history by default.

Obtain a snapshot or the needed files from the [official repository](https://github.com/vtejdn/acme) at the selected version or fixed commit, reusing adequate available contents when applicable.
Keep source retrieval distinct from final installation; a downloaded or unpacked outer directory does not determine the project root.
When temporary local source is needed, explicitly choose its download or extraction destination in a creator-owned child of the project's root .tmp/ under the [temporary-storage rule](rules/organization.md#temporary-storage), and clean it after use without leaving continuing work dependent on that copy.
Choose adequate retrieval tools for the actual comparison, source inspection or maintenance need, including Git when useful, without making cloning or a Git executable an installation prerequisite.
Read the selected source's version and applicable entrances before integration.
File installation carries no source .git, refs or official commit history into the project.
Preserve the confirmed empty target's own Git setup while copying the necessary README, AGENTS, ignore rules, complete LICENSE and other selected public files.
Without Git, install at the same confirmed empty project root without initializing a repository or remote merely for installation.
Never reset existing project identity, configuration or materials to manufacture an empty target; their presence stops ordinary first installation as above.

For an actual new research project, prepare repository, repository_display_name and repository_abbr in repository/config.json as that project's human-chosen or explicitly confirmed values, or null for each missing choice.
Apply this preparation to both Git and non-Git copies; a valid inherited acme key is not evidence of the human's project choice, although that same key remains valid when explicitly chosen or confirmed.
Then continue directly with the [setup action](#set-up-repository-or-human-identity): collect the missing human key/name and project choices together, register the actual human, append the scoped project notice and complete any necessary checkout binding.
Reuse answers already supplied for that setup; while the required human key or License name is missing, finish independent retrieval and preparation and leave the copy authorless, without inventing an identity or starting research.

A new research project does not inherit the official source's display choices or source remote as its own.
Without Git, retain a supplied repository key or null when unnamed; either permits local registration, research and receiving selected public material without uploading local research content.
Before research writing or Git delivery in a Git-managed project, obtain the human-chosen or explicitly confirmed repository name and complete the actual checkout binding, reusing an existing real project registration.
Apply the [repository name rule](rules/identity.md#repository-names-and-use-environments) through ordinary scoped configuration edits; maintain the README heading from the separate display name and abbreviation when both are known, preserving human keys, material identities and historical source facts.
Preserve the remaining project prose and framework explanation unless an actual explicit content request covers it; installing or selecting an interpreter does not authorize a public machine-environment appendix.
Retain a necessary continuing nonsensitive tool choice only at `execution/runtime/readme.md` under the [runtime rule](rules/organization.md#machine-local-runtime), without creating notes or a virtual environment by default.
Keep reading and necessary setup repair available while the name is missing, without reinitializing the project or inventing a name from the folder or author.
An existing shared-repository clone keeps its real identity, project display settings, README heading, registrations and materials.
Reuse the actual human's existing registration and bind the new Git checkout; supplement only genuinely missing human information and project notices, retaining existing authors and historical years under the [identity rules](rules/identity.md#stable-keys-and-local-attribution).
An authorless copy or clone remains preparation, with no selected research Task or execution authority.
Do not run research.py init over an already copied config.json or delete configuration merely to satisfy that optional Git-bootstrap helper.
Create .tmp/, intake/, profiles/, execution/ and local source storage only when actually needed under their responsible rules, without placeholder files to force Git to retain empty directories.
The ordinary guides and their diagrams remain alongside the common framework files; copying carries no personal profiles, private holdings or research authorization from the official blank source.
Cloning does not authorize pushing to an inherited remote or automatically changing that remote.

Before reporting installation complete, check framework/version.json, necessary framework files and usable entrances at the final project root, preservation of the permitted target Git setup, and exclusion of source Git metadata and history from file installation.
A version file in a temporary or unintended nested source copy, source-clone success or a command PASS alone does not establish installation at the requested root.
Check the locations actually created or modified, without a whole-workspace nested-repository scan or removal of legitimate subrepositories.
Insufficient permissions or necessary inputs remain concrete unfinished work; do not change the final project location to evade the limitation.
Any actual Git delivery follows the [existing delivery action](#commit-or-push-requested-work) on the project's own history, including actual outgoing-chain checks.
A preliminary commit or repeated connection probes are not installation steps; the first-installation target checks above remain prerequisites.

Publishing common files from a development repository to the official starting repository requires its actual maintenance and remote-operation authority.
Exclude the source's entire execution/ and .venv/ from framework copying and upgrades, including E, runtime notes and optional environment explanations; preserve the destination's actual local contents.
For authorized upgrades, project clones or development copying, preserve the complete root LICENSE and applicable upstream notices and retain destination project notices and their actual years when merging framework files under the [project-notice rule](rules/identity.md#project-notices-during-setup).
Inspect the selected content and keep development blueprints/tests, local profiles, temporary work, private holdings and actual research out of that starting tree.
Original literature remains local under the [source-storage rule](rules/literature.md#local-pdf-storage); clean setup creates no original-store placeholder or literature account.
Exclude the source's live `mathematics/maintenance.md`, `mathematics/erratum.md`, `mathematics/messages.md` and personal message archives, preserving destination contents under their [location and copying rule](rules/organization.md#material-maintenance-worklist), without empty placeholders.
Use ordinary copying and native Git without a permanent shipped-file inventory or installation receipt.

## Upgrade installed framework

Apply the [version and upgrade rule](versioning.md#upgrading-an-installed-framework) under an explicit upgrade assignment, separately from the daily metadata read and fresh installation.
Keep the actual installed project root as the destination; source retrieval prepares the selected files for that root.
Identify the installed version and selected official target; obtain its fixed source in owned root `.tmp/` and verify agreement among tag, commit, version metadata and target-version note.
Apply the [common connection-recovery responsibility](rules/workflow.md#connection-recovery) to authorized retrieval and delivery failures.
Without Git, use available public source evidence with an archive or selected fixed-source files and ordinary recovery copies; Git initialization or a local clone is not required.
Read applicable intervening notes, inspect their combined local paths and direct consumers, and prepare final target files with only genuinely ordered adaptations.
Preserve recoverable affected contents, local customizations, unrelated work, the actual named or unnamed configuration, research and effective Task/E conditions without requiring a clean worktree, stash, preliminary commit or empty reinitialization.
Merge any changed LICENSE content while retaining upstream and destination project notices, their scope and historical years; an upgrade does not repeat first registration or refresh attribution years.
Synchronize already published official human-document bodies under the [common upgrade contract](versioning.md#upgrading-an-installed-framework), merging actual local adaptations rather than limiting updates to links and version literals.
Judge mixed public-file merges and retired files by their actual local role, preserving authorship and the separate responsibility for new human-document authoring.
Finish required adaptation and checks before marking the target installed version; on failure restore this operation's changes or report actual incomplete restoration while preserving foreign work and necessary recovery content.
Reread new applicable rules before affected work continues; an upgrade grants no research resumption.
With an applicable project remote, complete the [authorized upgrade's scoped Git delivery](versioning.md#upgrading-an-installed-framework) before reporting its result or continuing the original task, including when upgrading before that task or under a separate upgrade assignment.
Use the [existing delivery action](#commit-or-push-requested-work), honoring explicit local-only, offline or postponed-push instructions and reporting any unfinished delivery distinctly.
Report actual from/to versions, target commit, checks, applicable Git delivery result and remaining limits, then perform existing creator cleanup.
Ordinary authorized retrieval, editing and selected checks need no additional routine approval or mandatory installer.

## Set up repository or human identity

Before first registration, ask: "What local author key should identify you in local literature and other authored-material paths, and what independently chosen name should appear in the repository's License attribution?"
Explain that a key such as Alice-Smith uses ASCII letters, digits and internal hyphens without spaces or underscores, while the License name such as Alice Smith may contain spaces and Unicode and is stored as display_name.
For a new Git research project, collect its human-chosen repository name with any missing key/name; an unnamed personal folder without Git may keep repository: null.
Collect any missing project display name and abbreviation during actual setup, reusing established choices independently of the repository key and human attribution name.
For a fresh official download or clone, prepare all three project settings as actual project choices or null before registration; an existing shared-project clone or upgrade retains its real project settings and authors.
Unknown display choices remain null and retain the existing heading while independent authorized work continues; ask for the missing choices only when forming the project heading is needed.
Reuse values explicitly supplied for the actual setup, ask only for missing values and request an author-selected valid replacement for an invalid key rather than changing it automatically.
Apply the [identity setup rule](rules/identity.md#stable-keys-and-local-attribution) before registering or binding, keeping the key, attribution name and supplied Git/GitHub identities separate.
Use existing registration interfaces or ordinary authorized metadata edits, then complete the selected root LICENSE project notice through a bounded edit under the [project-notice rule](rules/identity.md#project-notices-during-setup).
An existing corresponding notice is reused without duplicate attribution; preserve the supplied name exactly and do not replace or extend the upstream copyright line with it.
For an already registered actual human, reuse that identity and add only missing applicable information or notices; a new checkout needs its own Git binding, not a new human registration.
The optional init interface requires the independent --display-name; an authorless fresh copy or clone remains empty and unbound until actual registration.
An already copied config.json uses existing registration and scoped configuration edits, without rerunning init or deleting configuration.
Git registration stores supplied signature/account mappings without setting user.name or user.email; binding selects the checkout operator without setting the commit signature.
When a commit is actually needed, verify the effective Git signature against the actual contributor's registered mapping, reuse correct settings and limit necessary configuration to that checkout without changing global settings.
When both project display choices are known, use ordinary bounded editing to maintain the root readme.md heading as `# <repository_abbr>: <repository_display_name>`, with faithful Markdown escaping and all remaining contents preserved.
When choices are missing, report the missing project-title setup explicitly rather than presenting a retained template heading as a human choice.
Changing only the repository key leaves those independent choices and heading unchanged; no new init arguments, generator, Git setup or remote operation is required.
Requested README text means genuinely explicit content, not an environment section inferred from setup; keep machine choices out of public entrances and shared configuration under the [runtime rule](rules/organization.md#machine-local-runtime).
Inspect the resulting configuration, people.json, full root LICENSE and scoped project notice, README and necessary binding, then report the installed version, actual completed setup and specific missing information.
A successful init or registration result alone does not establish a completed project title, License notice, effective Git signature or remote setup; add no completion receipt or state field.
This setup selects no research Task or execution authority.
For personal use in a folder without Git, use one explicitly identified local human and existing author registration; no Git binding, signature or local multi-author arrangement is required.
Keep an authorless folder as preparation until that first registration, and use the folder's own human rather than an enclosing checkout's binding.
Ordinary local file, material and registration operations retain their actual author and source duties, including external originals' attribution and separately authored corrections.
Git-dependent helpers remain optional and state their actual prerequisites.

## Start or continue research

For an initial question, apply the [inquiry-to-research rule](rules/workflow.md#from-an-inquiry-to-approved-research): use relevant existing evidence and proportionate preliminary lookup, answering directly when sufficient.
When the question remains unanswered and further work needs formal research, report the findings, unresolved question and concrete proposed scope and wait for applicable human approval before dependent strategy exploration and Task advancement.
Reuse an existing explicit research instruction or approval for that objective and scope, without recurring approval because a lookup, round or session changes.
Explanation, bounded source work, maintenance and an explicitly limited plan keep their actual deliverable and scope.

After sufficient approval, read the [Task setup rules](rules/workflow.md#new-task-setup) and likely matching contracts, reuse an adequate same-human Task or establish the precise approved contract with its actual human author and initial active decision.
An explicitly requested registration awaiting research authorization uses proposed status.
The responsible responding agent takes main research responsibility by default under the [execution rule](rules/execution.md#main-agent-responsibility-and-exact-maintenance), coordinating with an existing executing main agent rather than starting overlapping writers.
Task setup alone creates no E; prepare or reuse the ordinary family's stable local boundary only when execution is actually selected under the [execution rule](rules/execution.md#responsibility-and-version-boundary).
The same approval may cover setup and first execution; a prepared E starts non-running and work starts only when that approval and effective conditions permit it.
A joint coordination T has no E, and setup alone creates no execution or fabricated review.

For continuation, read the selected T contract/decision, any existing stable E's effective conditions, applicable operator policy, current S and directly needed C/D/J/source evidence.
Read relevant existing `mathematics/maintenance.md`, `mathematics/erratum.md` and `mathematics/messages.md` for the actual author, Task and material scope under the [coordination rule](rules/records.md#shared-mathematical-coordination), completing applicable erratum lookup before mathematical reliance without a whole-library scan.
When that selected execution has no local E, follow the [on-demand preparation rule](rules/execution.md#responsibility-and-version-boundary) using adequate real instructions and conditions; absence neither resets limits nor grants resumption.
For a joint goal, first resolve the actual human's appropriate individual T and its adopted exact common contract under the [joint-Task rule](rules/tasks.md#joint-tasks-and-participation); clarify a real unresolved choice among several individual Tasks instead of starting several.
Complete or reuse the [common work-start update](rules/workflow.md#shared-repository-work-starts) before substantive research in a Git working repository with a configured remote, using relevant incoming work for mathematical reuse before any necessary external search.
Authorized research writing follows the [common delivery default](rules/identity.md#submission-checks).
Apply the [collaborative progress-sharing rule](rules/tasks.md#shared-git-research) to actual joint participation, including continuation through an already participating individual T/E.
Reuse the known project repository, branch and actual work scope, honoring explicit human limits.
Follow [execution rules](rules/execution.md#current-contents-and-retained-limits) before autonomous advancement.
Use one responsible main agent and one stable E for the Task family; a new chat, revision or policy expiry does not reset allowance or resume a stopped run.
An actually authorized continuation prepares the relevant exact Task reference and current conditions directly; a pointer update preserves stops unless actual resumption is authorized.
If a stop or missing authority prevents advancement, preserve current findings and report that actual boundary.
Method changes and strategy priorities may adapt within the assignment unless the human explicitly fixed them; they do not change the objective or completion criteria.
Use the [route-selection rules](rules/strategies.md#choosing-and-revising-a-route) for initial comprehensive exploration based on actual retained progress, then judge expected gains, decisive gaps and any inexpensive probes before substantial investment.
Choose useful breadth, depth and direct work or bounded delegation from the question and evidence, without a fixed route count or compulsory agent-S assignment.
If authorized work may proceed, carry out or explicitly assign a useful next investigation and use its result, retaining actual findings, failures, gaps and continuation points.
Task/S/E preparation or a strategy list alone does not fulfill an assignment to explore and advance research.
Under [research coordination](rules/workflow.md#research-coordination), try the complete argument at consequential points and adjust assignments as evidence changes.
Use ordinary research or [Preparation](rules/workflow.md#research-preparation) for clear next steps.
Use the [strategy delegation criteria](rules/strategies.md#choosing-and-revising-a-route) for a consequential choice or sustained lack of progress, and read [agent-S](rules/agent-S.md#when-to-delegate-and-assignment-boundaries) when assigning that role.
Follow an explicit human instruction to delegate within its actual scope, permissions and effective execution limits.
Put a candidate selected for continued work into an executable [investigation and follow-up](rules/workflow.md#candidate-research-follow-up).
When substantive work stalls on the original proposition, [reassess proof and refutation direction](rules/strategies.md#proof-and-refutation-direction).
The responsible agent records concrete literature work needing later handling under the [common worklist rule](rules/records.md#pending-literature-work); a restricted delegate supplies the item to that writer while the Draft retains its mathematical context and actual limits.
Keep shared Task/E limits and the actual [independent-review boundary](rules/proof-audits.md#review-arrangements).
For material problems found during this research, use the [research repair entrance](#repair-material-problems-found-during-research) and its common contract within the existing assignment and author authority.

## Develop, register or reorganize mathematics

Read the question, candidate material, actual inputs and likely existing homes before applying the [common content decision](rules/records.md#substantive-material-retention).
Then apply [work obligations](rules/workflow.md#work-obligations) and the actual kind's registration, version, source, reproduction and review rules.
Develop substantive arguments in D or another responsible mathematical material and continued programs directly in J.
Use existing adequate C/J/R/L/U content rather than creating another account for allocation or progress chronology.
Retain complete necessary arguments, hypotheses, meaningful failed approaches, native inputs, source applicability and actual unresolved obligations.

Before substantial proof investment, apply [knowledge reuse](rules/knowledge-reuse.md#reuse-before-proof); a recognized established result triggers its source-check duty even during exploration.
An open conjecture or conditional investigation need not already have a proof or completed review, but acceptance requires its real evidence and resolved applicable obligations.
Distinguish an actual new statement/contract, a substantive revision, an unchanged-mathematics decision and routine maintenance under the [record rules](rules/records.md#identity-and-versions).
Choose a family by its actual core mathematical topic and retain versions only for distinct research/evidence that needs separate preservation; pure logical repair may maintain current or older material in place under the [repair rule](rules/records.md#in-place-maintenance-and-logical-repair).
Register C with its real statement and author without fabricating an initial assessment; actual key C and the adopted completion chain require explicit applicable assessments under the [Claim rule](rules/claims.md#mathematical-assessment-and-review-findings).
For a new fixed or continuing S family, maintain its actual next unissued [allocation state](rules/identity.md#allocation-and-concurrency); revisions retain their family and D keeps its separate reusable-address boundary.
Actually added C/T decisions use their real UTC minute time, while reading or reselecting an existing decision preserves genuinely known calendar precision.
Keep fixed predecessors and exact decision anchors; navigation derives the responsible current selection.
Maintain human-specified Claim labels through ordinary bounded title or prose edits under the [label rule](rules/claims.md#claim-role), preserving the assessment and exact relations without a decision interface, evidence read or new version.
Return the resulting material and its actual status, with any missing evidence explicit.

## Close a round

Read the round's changed mathematics, computations, sources and directly affected consumers under the [workflow](rules/workflow.md) and common content decision.
Check the claims being delivered and relevant inputs, reusing adequate existing evidence; retain useful partial results and failures at responsible homes.
Repair actual references and maintain affected navigation after source edits settle, through ordinary bounded edits or optional rendering.
Navigation derives actual declarations and selected evidence metadata without checking or restoring native J payloads merely to display them; actual input recovery and mathematical adoption keep their own [computation](rules/computations.md#recovery-of-necessary-fixed-inputs) and [assessment](rules/claims.md#mathematical-assessment-and-review-findings) obligations.
Retire a redundant D only after checking its actual historical uses and preserving any necessary content under the [draft rule](rules/ledger.md#working-drafts-and-fixed-findings).
A setup-only residue whose mathematics is already fixed needs no replacement account or move receipt.
Before handoff, give still-effective literature follow-up its [maintenance entrance](rules/records.md#pending-literature-work) rather than leaving the only remaining action in a Draft or reply.
For authorized repository writing with an applicable project remote, assess remaining delivery at closeout and complete a useful coherent batch through the [delivery action](#commit-or-push-requested-work) under the [common default](rules/identity.md#submission-checks) and actual human limits.
Major progress may be shared during the round; preserve truthful status and local-only contents, and report any concrete unfinished delivery without extending research past an effective stop.
Return established results, remaining obligations and the next continuation point.
Round closeout neither resolves the whole Task nor resumes research after an instruction to stop at that boundary.

## Complete, pause or stop a Task

For completion, compare the actual deliverable with the original T hypotheses, quantifiers and every completion criterion under the [Task rules](rules/tasks.md#task-records).
Check the full support chain and applicable [completion review](rules/proof-audits.md#completion-and-verification-boundaries), reusing adequate fixed inputs and compatible reviews.
Arrange the required independent review at key proof points and for the full chain after completion; retain actual unfinished review obligations.
Check the explicit assessments and applicable support of C nodes actually adopted in that full chain, distinguishing unselected from open and actual premises from provenance, old review targets or merely retained argument bodies.
Record completion only when the actual contract is satisfied; otherwise state the precise unresolved criterion without enlarging the result.
If actual related own messages are proposed for archiving, apply the [archive action](#exchange-mathematical-messages-or-archive-own-correspondence): reuse applicable explicit instructions, or prepare the concrete selected scope for the human author's confirmation after actual completion.
Task completion itself supplies no archive authorization, and no archive question is needed when none is proposed.

For pause or stop, preserve available results and a usable handoff and record the actual instruction at its responsible E/T scope under the [execution rules](rules/execution.md).
Distinguish an execution stop, human lifecycle pause, blocked mathematical obligation and completion.
An instruction to finish the current work and then pause permits that closeout, not a fresh research round.

## Review specified work

Identify the actual source, manuscript, Claim, argument, computation or Task and the requested review depth.
For writing or proof review of a manuscript, use the manuscript action at the requested scope.
See [Review a manuscript](#review-a-manuscript).
Use this general action for selected fixed Claims, Tasks, sources or computations, including those used by a manuscript.
Determine whether the actual work requires independent inspection under the [review obligations](rules/proof-audits.md#independent-review-obligations) or an applicable explicit human requirement before choosing the arrangement.
Base any required isolation or delegation on the actual review relationship and obligations.
Read exact versions, hypotheses, arguments and dependencies and select prior findings according to the actual review arrangement.
Apply the [proof-review rules](rules/proof-audits.md) and any applicable [external-input and source-review depth rules](rules/literature-audits.md#accepted-external-inputs) to the selected input.
Inspect the requested whole scope; do not substitute structural checking for mathematical scrutiny or silently expand a narrow source inspection into a full proof audit.
Reproduce decisive computations or behavior where needed rather than mechanically repeating all prior tests.
For source audits, apply the [Lean scope and unchecked reliance rule](rules/literature-audits.md#default-audit-scope).
Keep formal project findings in R for every actual agent relationship and use the [source-evidence selection rule](rules/literature-audits.md#organization-and-stable-units) for source inspection.
New or substantively revised findings declare their actual relationships explicitly; a genuinely new C/T acceptance selects findings with both matching relationship rows and exact required bindings, without backfilling unchanged historical findings.
For required independent review use a reviewer outside substantive proof development and its inherited mathematical context; the current reviewer may act directly when already qualified under the [arrangement rule](rules/proof-audits.md#review-arrangements).
Supply fixed inputs, necessary dependencies, exact scope, applicable rules and actual human requirements directly without forwarding development discussion or its mathematical summary; another agent layer or the same context under a new label supplies no independence.
After an independently identified gap is repaired, arrange independent re-review of the correction and affected chain; a substantive repair contributor cannot independently review that repair.
Maintain successful necessary logical rechecks truthfully under the [rolling R rule](rules/proof-audits.md#rolling-review-repair), retaining real inputs, bindings, relationship, time and limits without automatically creating a new version or correction log.
If the required independent arrangement is unavailable, report the specific limit and retain the unfinished obligation at its existing Task or review home while continuing unaffected authorized work.
Return actionable findings, inspected scope and limitations, distinguishing source inspection, proof review, build success and formal verification.
A review request does not itself authorize substantive editing of another author's material; actual conflicts use the maintenance boundary below.

## Prepare or reuse literature

Follow [common source preparation](rules/literature.md#source-preparation) to reuse sufficient evidence, identify the actual work and edition, and inspect necessary passages.
Apply the [disclosure limits](rules/literature.md#unpublished-material) to the selected source and its use.
Maintain original links under the [local source-storage rules](rules/literature.md#local-pdf-storage).
Use the [searchable-contents rule](rules/literature.md#searchable-contents) when the selected source supplies contents, and follow [progressive reading](rules/literature.md#progressive-reading) at the needed depth.

When source evidence needs maintenance, choose an existing home or a rolling U under the [source-unit boundaries](rules/literature-audits.md#unit-granularity-and-maintenance).
Use the [source-audit rules](rules/literature-audits.md#content-and-verification) for actual inspection scope and [mathematical issue routing](rules/records.md#mathematical-issues-and-reliance) for problems with the source or its local use.

For personal import or external intake, follow the [original-preparation rule](rules/literature.md#acquisition-before-u-reception) before delivery.
For necessary acquisition, apply the [acquisition and failure rule](rules/literature.md#literature-acquisition) and record concrete remaining preparation in the [existing maintenance worklist](rules/records.md#pending-literature-work).
Use the optional [fetch or bibliography helper](../scripts/readme.md#local-source-retrieval-and-registration) only for its explicit mechanical operation, with the applicable containment, format and conflict checks.

## Write or revise a manuscript

Determine the actual responsible writer(s), writing assignment and purpose, any relevant Task and direct source/review inputs under the [writing rules](rules/writing.md), then read the actual current TeX manuscript and needed supporting records.
ACME supports TeX manuscripts; human authors use those sources to guide the agent or edit them directly under the [supported writing scope](rules/writing.md#tex-manuscripts-and-supporting-records).
A manuscript assignment calls for the actual TeX deliverable, while a request limited to agent-facing Markdown records keeps that scope without inventing a manuscript or compilation.
Any writer may write manuscripts or slides for any actual repository Task without a matching personal or participation Task; writing creates no research execution authority.
Reuse an adequate project and apply the [writer/full-Task layout](rules/writing.md#projects-and-documents), using a purpose-named project in the writer container when no Task corresponds.
Use a joined writer container only under an [explicit joint-writing assignment](rules/writing.md#explicit-joint-writing), preserving actual operator identities and the one actual document home.
Apply the actual single-writer or joint-document [writing layers and choice-update rule](rules/preferences.md#scope-and-adoption), preserving the [current manuscript and actual policy boundary](rules/writing.md#current-manuscript-authority).
For a gap requiring formal research beyond the writing assignment, apply the [inquiry-to-research boundary](rules/workflow.md#from-an-inquiry-to-approved-research) rather than inherit Task/E authority from the document association.
Read the evidence for the findings selected for revision under the [writing execution rule](rules/writing.md#writing-rule-execution).
Use the [manuscript's writing opinions](rules/writing.md#manuscript-revisions) for writing findings and the [manuscript's mathematical-review evidence](rules/writing.md#manuscript-review-and-mathematical-provenance) for proof findings.
Perform proportionate source preparation and definition registration; source observations remain evidence rather than a fifth writing layer.
Use actual own/coauthored source designations or manuscript-specific permissions under the [text-reuse rule](rules/writing.md#default-reuse-permission); a style-only reference grants no text reuse.

Before delivery, apply the [common manuscript writing-rule checks](rules/writing.md#manuscript-writing-rule-checks), correct required problems within authority and recheck their actual effects.
Route mathematical and source problems to their responsible homes, reconcile affected [mathematical review and citation evidence](rules/writing.md#manuscript-review-and-citation-records) and actual companion records, and compile or inspect layout as applicable to the delivery.
Select available build and inspection capabilities under the [host-capability responsibility](rules/workflow.md#agent-and-tool-responsibilities), reusing applicable project settings and the [local-build convention](rules/writing.md#reproducible-local-builds).
If a required build or check remains unavailable, report the specific affected scope, consequence and useful next action to the human author while continuing independent authorized work.
Return actual corrections and remaining mathematical, writing-rule, citation, build or layout limits, identifying review opinions still awaiting reviewer recheck under the execution rule without closing them as the writer.

<a id="review-a-manuscript-against-writing-rules"></a>
## Review a manuscript

Select writing review, proof review or both according to the requested scope and any applicable review arrangement.
When the request and arrangement leave the review kind unspecified, review writing under the responsible author's four layers.
See the [manuscript review rule](rules/writing.md#reviewing-a-manuscript).
Determine the relationship and purpose before reading prior opinions.
For an independent initial review, form initial findings from permitted inputs before reading prior opinions or conclusions.
For targeted rechecks, choose inputs by the actual scope and relationship and report their use.
Apply the manuscript review rule's writing independence criteria and the [proof review arrangements](rules/proof-audits.md#review-arrangements) to their respective objects.

Use the common checks and the selected manuscript's revision opinions for writing review.
See the [common checks](rules/writing.md#manuscript-writing-rule-checks) and [revision-list rule](rules/writing.md#manuscript-revisions).
For proof review, examine the manuscript's reasoning at the requested depth and retain the scoped evidence at its mathematical-review home.
See [Mathematical review evidence](rules/writing.md#manuscript-review-and-mathematical-provenance).
When both are requested, report their coverage separately and link any proof finding that requires manuscript revision from `revisions.md` to the mathematical evidence.
Limit review-only writes to the selected review records and use the actual correction authority for changes to the text, policy, citation records or mathematical materials.
Return the findings, inspected scope and limits, distinguishing review completion, manuscript conformity, completed corrections and build results.

## Develop or reproduce a computation

Read the actual J question, native programs/inputs, parameters, arithmetic mode, earlier useful results and consuming mathematical reduction under the [computation rules](rules/computations.md).
Choose suitable methods, runtimes, libraries and other tools under the [computation-tool responsibility](rules/computations.md#computation-tool-selection), respecting the actual assignment, project requirements and environment constraints.
Reuse sufficient actual capabilities, reading only relevant local runtime notes and necessary private resource sections under the [runtime rule](rules/organization.md#machine-local-runtime); notes, activation and a new environment are not prerequisites.
Keep continued programs in `mathematics/computations/programs/<J>/` and generated results in the ignored `mathematics/computations/outputs/<J>/`.
Retain generated data indispensable as fixed proof/check/computation input in the responsible J's tracked native inputs; an authorized recovery task may run its existing generator/verifier, check the actual object and finite scope, then repair input locators and consumers under the [recovery rule](rules/computations.md#recovery-of-necessary-fixed-inputs), without repeat approval or historical reconstruction.
When reproduction is needed, rerun the chosen output set in that same J after preserving necessary inputs, non-reconstructible witnesses and earlier results still consumed by the check.
Safe overwriting and removal of reproducible output are allowed with coherent consumers; ordinary reading or maintenance does not require rerunning it.
Use an acquired program's actual qualified J for self inputs/outputs and explicit paths for genuine cross-J dependencies.
Keep necessary reproduction context, meaningful failures and actual limits without persistent mathematical digest gates or an archive for every run.
Return the real command, inputs, result and checked scope; finite or floating-point observations do not prove an unrestricted theorem.

## Repair material problems found during research

Use the [research entrance to common problem handling](rules/records.md#entry-during-authorized-research) for problems found within the actual research assignment and author authority.
For conformity problems in the actual human author's own materials, repair personally or delegate according to actual complexity and capability, without separate maintenance authorization or a preliminary independent inspection.
Necessary research context may accompany delegated repair; discovery and diagnosis do not make the research agent a conformity inspector.
After a bounded conformity-repair batch, start an independent acceptance subagent under the [common acceptance contract](rules/records.md#accept-local-material-repairs) and [context rule](rules/workflow.md#material-maintenance-contexts).
For substantive mathematical errors, including reference errors affecting theorem applicability or logical dependencies, apply the common contract's actual mathematical version, assessment and review duties instead of treating them as pure locator repairs.
Use its common recording and cleanup rules for unfinished or accepted work, returning actual repairs, checks and remaining obligations without claiming self-checks establish acceptance.

## Inspect local mathematical materials under current rules

Enter the [explicit maintenance entrance](rules/records.md#local-material-maintenance) only under the actual human maintenance instruction and its scope and depth.
Perform the [read-only inspection action](rules/records.md#inspect-local-materials), with [stage-context isolation](rules/workflow.md#material-maintenance-contexts), recording supported unresolved problems and necessary continuation scope under the common contract.
Return actual inspected scope, findings and limits without repairing materials or inferring this action from ordinary research, proofreading, mechanical checks or framework use.

## Repair local mathematical materials

Under an actual explicit maintenance instruction, interpret worklist items by their actual needs, using the [common repair action](rules/records.md#repair-local-materials) for selected materials or issues, or otherwise recorded conformity items awaiting repair.
Ordinary literature preparation uses its [handling and confirmation rule](rules/records.md#pending-literature-work) within actual authority rather than acquiring conformity stages from its worklist location.
For conformity repair, meet the [stage-context rule](rules/workflow.md#material-maintenance-contexts); a direct repair assignment needs no preceding full inspection, and necessary diagnosis belongs inside repair.
Apply the applicable scope, author, mathematical, checking and disposition duties, returning actual handling, checks and remaining limits without clearing conformity items through self-checks.

## Accept repairs to local mathematical materials

Use the same [common acceptance action](rules/records.md#accept-local-material-repairs) for a research conformity-repair batch or an explicit conformity-maintenance acceptance instruction, within its actual scope.
For conformity acceptance without a narrower selection, accept submitted conformity repairs awaiting acceptance.
For that conformity work, meet the [context and arrangement rule](rules/workflow.md#material-maintenance-contexts), applying the common independent checks, failure handling, affected-author or receiving-side confirmation, and partial-cleanup duties without repairing the materials yourself.
An assigned check of ordinary literature completion follows its actual read-only limits and [confirmation and cleanup rule](rules/records.md#pending-literature-work), without conformity stages solely because the item is in maintenance.
Return the actual accepted or rejected scope, cleanup and remaining limits; acceptance supplies no mathematical proof-review relationship by itself.

## Maintain shared materials or resolve a conflict

Read the actual change, responsible material, consumers and [common content decision](rules/records.md#substantive-material-retention).
Apply the operative [collaboration and conflict rule](rules/identity.md#collaboration-maintenance-and-conflicts), including its preserved author, mathematical, source and review boundaries.
For an old review container, apply only the bounded [retirement exception](rules/proof-audits.md#review-retirement), preserving necessary evidence and historical adoption facts and preparing its non-reuse allocation bound before deletion.
Repair responsible shared registration and derived navigation directly, and apply that rule's locator-only exception to corresponding references in another author's material.
Other body or layout corrections keep the same-human and separately attributed correction boundary, without a per-author approval process.
Resolve an administrative conflict using the core principles and applicable topic rules; act directly when they determine the choice, and report only a remaining decisive gap requiring human intent, authority or facts.
For a substantive mathematical conflict, identify competing statements/evidence and affected materials and obtain approval for the scoped recheck before undertaking it, reusing existing explicit approval for that same scope.
That approval alone neither transfers authorship nor authorizes substantive editing of another author's material.
Preserve both sides' actual evidence, and keep substantive contributions in their responsible author's own materials.
Ordinary authorized research and reviews retain their existing authority; the conflict procedure is not a universal approval step.
Return the repaired administrative result or concrete remaining conflict and needed decision, preserving activity-specific roles and another human's Task/E.

## Exchange mathematical messages or archive own correspondence

Use the [coordination and mail rules](rules/records.md#shared-mathematical-coordination) within the actual represented human's research or explicit communication authority.
Look for relevant existing `mathematics/maintenance.md`, `mathematics/erratum.md` and `mathematics/messages.md` by the current author, Task, strategy and material scope; these lookup paths require no empty files or whole-library scan.
Register work under the [coordination and problem-routing rules](rules/records.md#shared-mathematical-coordination), preserving the actual local or external object, author attribution and necessary evidence.
Before mathematical adoption, inspect relevant erratum for the chosen input/version, including other-author inputs; substantive findings do not authorize changing another author's decisions or body.
Send concise mail-style messages and independent replies newest first with actual UTC-minute sending times, clear human sender/addressee and exact necessary reply/evidence locators, using applicable mathematical expression and author choices without a manuscript workflow.
Recipients judge, optionally reply or adopt, and maintain only their own follow-up; they cannot delete or rewrite the sender's original or infer that all recipients have finished.
Archive only selected own-sender messages under the [two human-authority entrances](rules/records.md#author-message-archives), creating `profiles/<human>/message-archive.md` only when an actual archive needs it.
After a genuinely completed own Task, prepare the related messages and destination for human confirmation if no applicable instruction already covers them; a direct explicit archive selection needs neither Task completion nor repeated approval.
Preserve complete original mail and actual sending order, changing only necessary same-object relative locators and checking affected replies/material links.
Keep a precise shared short entrance and concrete remaining request for actual unhandled recipients or follow-up; preserve other-sender replies, other Tasks and all unselected content.
Verify saved archive contents and necessary links before removing shared originals, rereading current input and existing archive on change, failure or retry to avoid loss, stale removal or duplicate copying.
Report actual moved messages, retained unresolved entrances and remaining limits without a new message service, approval register, historical cleanup account or changes to Task/E.

## Acquire material from another research repository

Use [intake](rules/intake.md#scope-and-routing) for distinct research repositories; another registered human in the same repository is direct collaboration.
Read each actually selected file or mathematical unit at the exact source commit, its intended scope, necessary inputs and receiving candidates before deciding what to copy, retain, reuse and adapt.
Check its mathematics and claimed state for the intended use and confirm the real original human and source facts, preserving precise content, useful failures, unresolved inputs and actual review limits rather than treating format or tool success as acceptance.
The intake source is an identified public GitHub repository at a full fixed Git commit; a receiving no-Git personal folder may remain unnamed.
Keep the actual fixed Git names and required entry/blob facts through manifest, selected acquired-record validation, local-revision inputs and onward transfer, without checking same-named sending worktree objects.
Prepare canonical receiving paths through actual correspondence, including an explicit native-child mapping when needed; fixed source names need no local alias resolution or renaming.
Actual local sources and receiving publication retain their physical protections under the [intake rule](rules/intake.md#scope-and-routing).
Use actual authorized public source reads and ordinary file operations when Git is unavailable; the optional Git-based source helper retains its own source-access prerequisite.
Apply the [common connection-recovery responsibility](rules/workflow.md#connection-recovery) within the selected fixed-source operation's authority.
First reuse adequate material and preserve conforming source prose under the [common preservation rule](rules/records.md#receiving-and-adapting-selected-content), adapting only actual receiving-rule differences in identity, classification, layout, numbering or references.
Inspect the resulting text, author correspondence, exact references and necessary direct consumers.
Sender framework versions, current-format support or missing installation metadata do not independently bar adequate receiving preparation or require a sender upgrade.
If the optional helper cannot handle the actual old layout or input, report its interface limit and use an adequate ordinary path when the necessary mathematics, original identity, fixed-source facts and conforming local result can be established; do not weaken selected-helper checks or add historical parsers merely for compatibility.
Keep conjectures, partial support, known failures and source assessments at their real state; established use or a new adoption retains its evidence and review duties without a whole-source reproof for ordinary receipt.
Resolve or report a real mathematics, author/source or access gap at the affected unit or use, and continue independent authorized receiving work.
Ordinary reading, editing, copying and existing registration/allocation mechanisms suffice; a dedicated command, prepared-text payload, mapping plan or uniform batch protocol is not a condition of valid intake.
R has no mandatory C target; choose actual necessary targets, reuse and limitations from the inspected finding, without acquiring every binding or citation.
Receive needed S/D mathematics in a suitable fixed home and a necessary joint T contract under the [Task rule](rules/tasks.md#joint-tasks-and-participation), without another human's ordinary Task/E authority.
Select bibliography targets and U positions within each actual source-key/author namespace, retaining necessary origin distinctions, then write the selected receiving content and provenance under the [material format](material-format.md#direct-acquisition).
Before finalizing U receipt or invoking the optional helper for it, first complete the ordinary [original-acquisition procedure](rules/literature.md#acquisition-before-u-reception) for the actual work and inspected edition.
Reuse an adequate receiver-local original or independently obtain and validate the needed work/edition; reuse an adequate same-work/edition outcome for several units.
Maintain necessary canonical bibliographic fields and useful edition/source notes without original-file registration or an acquisition account.
On failure, record the actual source/access outcome and directly report the work/edition, known address, failure, local availability and resulting limits to the human author; give any still-needed literature follow-up its [common maintenance entrance](rules/records.md#pending-literature-work).
Retain useful authorized U evidence and its inspection limits without transporting sender-private originals or accounts, inventing fingerprints or treating the failure as a mathematical verdict.
Check actual resulting files, references and affected U positions, and retain the operation once at its responsible intake home.
Coordinate affected writes only as needed for coherent results; optional helpers apply their input and publication protocols only when chosen.
Private original literature is outside intake; reject the retired source/holding/update inputs before opening a private file.
Preserve an established original registered repoN/family's local number across physical versions and reject an occupied prepared position without silently renumbering the body.
Fresh receiving positions respect and advance their actual next unissued namespace bound, rather than reusing a retired number or allocating another family for an existing correspondence.
An explicitly selected actual independent finding still in historical L needs complete prepared receiving R with its true targets, scope and limitations; available source content requires no source-repository upgrade.
Ordinary whole historical L reading and unselected old findings retain their scope.
Select only actual fixed-commit J programs, necessary inputs and explanations under the [J receiving rule](rules/intake.md#computation-programs-and-inputs); retain sending-output references as source-only context, without reading, mapping or receiving their bytes.
Judge any reproduction need separately under the actual computation authorization; program receipt alone establishes no generated result or adequate evidence.
Before an explicit J source refresh, confirm the same original, inspect the selected current scope and maintain necessary retained inputs and actual consumer references under the [intake rule](rules/intake.md#homes-and-independent-reuse).

Apply the common [adaptation rule](rules/records.md#receiving-and-adapting-selected-content), preserving complete necessary selected mathematics and the single original human through adapted text, local numbering, justified splits/combinations and onward transfer.
Keep the actual source version and selected scope separate from the receiving kind, line and version; use the existing operation for per-unit provenance.
For lawfully maintained C/R/L/J or rolling U transfer containing actual current-repository contributions or repairs, explicitly choose current origin under the [source-selection rule](rules/intake.md#homes-and-independent-reuse), even when physical version, path, anchor and receiving header remain unchanged.
Keep current J group and explicitly selected native-file provenance coherent with the selected fixed snapshot, preserving old records and unchanged selected old scopes at their actual original sources.
Read actual references and prepare necessary final receiving text using true source/local correspondence; background prose does not cause tool discovery, mapping or provenance tracing.
For targets absent from the selected sending Git tree, preserve useful source-only reference context and actual limits, without assigning unversioned bytes to the material's commit.
Obtain or reproduce necessary input within the actual authorization, or retain its unresolved need at the consumer; omit obsolete mentions with no remaining mathematical, evidence or reproduction purpose.
Complete adaptation through ordinary reading, editing and copying or an optional helper supported by the chosen actual inputs, without historical-layout recognition or another current output home.
Maintain each selected file's actual internal references at its receiving location and designate necessary existing inputs in their responsible declarations.
Translate an explicitly chosen source locator only through actual correspondence and include its result in the designated edit; preserve unresolved necessary source context truthfully.
Prepare external repoN/authorN records and explicit receiving C/T/R/L/J serials under the [external identity contract](material-format.md#local-external-identities-and-prepared-correspondence); another similarly named file is no substitute.
Retain authored inspection limits and actual missing necessary evidence at the consumer; report unfinished work directly without an automatic unmapped-reference account.
Sender-local document references remain explicitly unacquired original-local context; acquire needed original text independently through ordinary authorized source preparation.
Record the actual operation once in intake, preserving historical J scopes without asserting their current availability, automatic adoption, mathematical equivalence or imported execution authority.
Per-file handling retains necessary per-unit original and transport correspondence in that operation without per-file approvals, checklists, receipts, permanent mapping graphs or duplicate receiving accounts.
New reasoning, different-author synthesis or substantive correction belongs to its actual contributor's own responsible material with exact references; initial adaptation does not relax the post-receipt same-human and fixed-source boundaries.
For local maintenance, prepare the selected operation item's exact path, actual anchor and file/artifact correspondences together with its material; validate the selected postimage before publication and preserve original/transport facts, scope, availability and unselected items.
Return the chosen installed scope and limitations, preserving the source's actual inspection and review depth.

<a id="import-ones-own-selected-content"></a>

## Export or import one's own selected content

Start only under the actual human author's explicit instruction or authorization for this migration action under the [personal-transfer rule](rules/intake.md#personal-import).
A direct request to transfer selected own materials suffices; reuse applicable authority and let the agent choose necessary content, dependencies and execution details within its scope without per-file approvals.
General research authority, same-human identity, readable files or a helper plan alone does not initiate personal migration; clarify only a decisive missing action or scope while continuing independent authorized work.
Establish the actual same human, selected object, source view, receiver and any explicit narrowing under the [personal-transfer rule](rules/intake.md#personal-import), without a Git-source or preliminary-commit requirement.
For Task transfer, complete its [family collection and independent manuscript pass](rules/intake.md#task-and-manuscript-collection), including every extant selected fixed-family version and each version's necessary inputs before reducing content.
Include the actual corresponding project's documents and complete required source chains, then merge support missed by the Task pass without unrelated projects, reverse consumers or Git-history recovery.
Compare concrete duplicates within the collection and against adequate receiving candidates through the [subagent comparison rule](rules/records.md#same-author-transfer-and-duplicate-comparison), including cross-kind overlap; retain uncertainty and continue independent work when needed.
Decide reuse, retained homes and combinations before allocating local numbers, using current local identities for an export with no actual receiver.
Preserve prose by default and limit adaptation to current-rule compliance, final local paths/numbers, confirmed duplicate handling and affected consumers, keeping exact versions, anchors, Task/S associations and manuscript entrances coherent.
Keep actual authorship, meaningful versions, decisions, source/review and reproduction facts, without transfer-only source fields, original-number accounts or permanent mappings.
Prepare canonical receiving `.md` paths and final public contents; the optional helper decodes that text and checks applicable typed declarations, while the agent checks ordinary prose, actual references and affected consumers.
For explicit file checks, the optional [check-files interface](../scripts/readme.md#personal-import-preparation) checks selected bytes, views and responsible declarations without discovering prose references or installing materials.
Prepare actual final text or exact expected-text edits through ordinary maintenance and existing file publication, checking content and affected consumers directly.
Complete the action through ordinary reading, adaptation, editing, file copying and existing registration/allocation mechanisms, inspecting the actual resulting content and affected references.
No dedicated command, plan JSON, complete dependency graph, full input snapshot or uniform batch transaction is required.
Reuse adequate local or already-intaken own material without identity conversion, duplicate local copies or acquired-history cleanup.
Dispatch an actually needed other-author dependency separately through intake, including S/D mathematics, T-only/J-only R and a permitted joint parent.
Resolve a participant's exact joint parent or prepare its complete standalone contract under the Task rule; preserve real obligations, attribution, review scope and effective execution conditions.
Carry the chosen manuscript source chains and required native inputs with proportionate affected build checks; generated deliverables follow the actual request, and a source build does not establish a receiving build.
Keep default exclusions and explicit settings/execution choices at their actual [personal-transfer scope](rules/intake.md#personal-import), without an unrequested Task or source-repository cleanup.
Default material transfer excludes the whole source execution/ and .venv/, preserving destination E, runtime notes and environment; an explicitly authorized local backup or move remains ordinary selected file work, separate from research handoff.
For callers choosing the optional `material.py import` helper, its [input plan](material-format.md#personal-import-input) and publication protocol apply only to that interface.
Coordinate affected own and foreign writes only as needed for coherent final references.
Own content receives no external identity, intake operation, import-source record, permanent mapping or fabricated new decision.
Ordinary Task import creates no E, reads no source E and preserves local execution state.
If execution preparation or responsible handoff is actually selected, judge necessary effective conditions and prepare or reuse the stable local E under the [execution rule](rules/execution.md#current-contents-and-retained-limits), preserving known stops and shared limits without automatic source-E transport.
Preserve actual stops/allowances; import alone starts no research, grants no parallel allowance and selects no autonomous Task.
Return actual retained content, necessary adaptations, foreign acquisition scope, unavailable dependencies and real mathematical/build limits in the ordinary reply, without a separate export report or transfer receipt.

## Commit or push requested work

Use this action for ordinary delivery of an authorized repository writing task with an applicable project remote under the [common default](rules/identity.md#submission-checks), or for a direct commit/push instruction.
Proactively complete necessary scoped commit and push under that default without a separate routine request, choosing actual operations from the work ready for delivery.
Apply explicit human limits and the actual repository, branch and publishable scope.
Read [serial delivery](rules/identity.md#submission-checks), the human-registered repository name, selected paths, existing index, actual operator/signature and intended branch/tree.
Coordinate one stable delivery interval, preserve unrelated staged work and contributor identities, stage the intended deliverable, commit and confirm the actual resulting tree.
Reinspect the affected delivery scope if relevant bytes or the index change; draft work may be committed with truthful status.
For an authorized push, establish the actual target and account/channel under the [connection responsibilities](rules/identity.md#git-and-github-connection-checks) and verify the remote/base relationship.
Before publishing, inspect the whole outgoing commit chain, including its scope and contributor identities.
If the operation requires host approval, apply the [permission and refusal rules](rules/workflow.md#workspace-boundaries) using the actual human authority, destination and scope of this delivery.
Push the authorized tip and verify the remote result.
Apply the [common integration rule](rules/identity.md#shared-repository-updates-and-integration) and [delivery scope](rules/identity.md#submission-checks) to new remote commits, a rejected push or an unclear publication scope, preserving unrelated work and the existing pending-batch boundary.
Handle connection failures under the [common recovery responsibility](rules/workflow.md#connection-recovery) within the actual delivery authority.
At actual project-remote setup, a relevant target change or a remote operation needing fresh facts, apply the [non-blocking name suggestion](rules/identity.md#repository-names-and-use-environments) for that selected GitHub project.
Keep a differing local name unless the human chooses to update it; official-source, intake-source and reference-only upstream names do not select the repository name.
Ordinary delivery grants no force-push or history rewrite.
Apply pending-batch ordering and its smallest concrete blocker-repair exception within the authorized remote-delivery sequence defined by the [identity rule](rules/identity.md#submission-checks); unrelated unpushed commits impose no remote check on local-only work.
Plain commit/push performs delivery without launching framework regressions, whole-library scans, recursive proof review or source-store hashing.
Reuse applicable verification and perform separately requested checks at their actual scope.
Return the actual commit or confirmed remote result, remaining worktree state and any specific blocker or unpublished scope.

## Run an explicitly requested check

Identify the requested object and actual working files or Git view under the [operation-level check rules](rules/identity.md#explicit-material-checks).
Use the relevant [tool interface](../scripts/readme.md) when useful and inspect its actual results; an unstaged repair cannot fix a submitted view.
Select necessary incoming consumers and their exact target locators through scoped searches and reading; an outgoing-link check does not discover unchanged consumers.
For a source-relationship check, choose the needed keys or artifacts and actual view under the [source-check rule](rules/literature.md#selected-source-checks); an ordinary structural pass supplies no source verdict.
An explicitly requested whole-store inventory retains that scope, while ordinary selected source/link work does not acquire it implicitly.
Keep structural errors, source-byte facts, mathematical findings and review conclusions distinct; a structural pass certifies neither semantic preservation nor citation completeness.
Repair and recheck an actual uncovered defect at its affected scope without stacking unrelated scans after every write.
Return the inspected scope, actual findings and limits.
