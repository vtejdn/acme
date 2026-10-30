# Human Identity and Numbering

## Git and GitHub connection checks

The agent establishes the actual target, relevant account or authentication channel and authority for the intended remote operation.
Choose relevant connection checks using the actual transport and current evidence; an environment-local skill, gh login or a fixed preflight sequence is optional.
Reuse adequate evidence while the target, account, channel and execution context remain applicable; recheck after a relevant change, an actual failure or when fresh remote branch state is needed.
The authorized read itself may supply connection evidence.
A gh authentication check concerns that gh account, an SSH Git operation uses its actual SSH channel, and an anonymous public HTTPS read needs neither gh authentication nor a repository remote.
When useful, git ls-remote targets the selected remote or explicit URL, without assuming origin.
Check the actual behavior of any diagnostic described as read-only; avoid silently refreshing credentials or changing configuration.
On failure, report the relevant concrete error without exposing credentials and diagnose the actual environment and channel before inferring expiry or changing an account.
A sandbox's lack of credential access does not establish expired credentials.
Preserve higher-priority permissions and existing task authorization, asking only for a remaining decisive gap in facts or authority.
Connection success grants no push, force-push, branch deletion, PR creation or other remote mutation.
Local reading, edits, checks, commits and file copying require no network preflight.
The [daily metadata read](../versioning.md#official-version-check) retains its bounded public HTTPS endpoint, cache and separately authorized upgrade boundary.

## Stable keys and local attribution

Before first human setup, ask together for the author-selected local path key and the independently selected License attribution name, explaining both purposes.
Reuse values that the author explicitly supplied for this setup; ask for whichever value remains missing before registering, binding or adding that human's License credit.
For example, Alice-Smith is an ASCII path key used in local authored-material paths such as SourceKey/Alice-Smith_U001_v1.md, while Alice Smith is the selected License name stored in display_name.
Keys use the existing letters, digits and internal-hyphen grammar without spaces or underscores, and retain collision and reserved-name checks.
For an invalid key, explain its concrete restriction and ask the author to choose another; never sanitize, transliterate or infer a replacement.
The attribution name is nonempty single-line text, may contain spaces and Unicode and is independent of Git/GitHub identities.
Use the existing id and display_name fields, preserving the exact supplied name and the permanent key.
Complete a missing project credit through a bounded edit under the [project-notice rule](#project-notices-during-setup); registration itself does not write LICENSE, and needs no License generator or extra signature field.
An authorless copy or clone of the official blank repository is valid preparation; collect both values at first actual registration, without renaming existing identities or relicensing existing repositories.
Personal use without Git may keep an absent or null repository name; Git research writing and delivery require the human's chosen or confirmed repository name under the [repository name rule](#repository-names-and-use-environments).
An existing shared-repository clone preserves its identity, registrations and materials rather than repeating fresh setup.
Use ordinary registration and, when Git is present, explicit checkout binding; copying files alone neither initializes Git nor binds a human.

repository/people.json registers permanent human IDs, display names, accepted Git name/email pairs and associated GitHub logins.
New human/repository registrations contain no administrative registration timestamp; retained obsolete values are removed from maintained metadata rather than converted or kept as compatibility facts.
Local-human registrations contain no registered_by field or replacement registrar history; remove that retired field from maintained entries while preserving their other facts and actual checkout binding.
Human/repository keys use letters, digits and internal hyphens; underscores separate identifier fields.
Registration checks keys and GitHub logins without regard to case, rejects duplicate Git signature assignments, and retains canonical spelling.
Display-name changes do not rename records.
Correct mappings through traceable framework maintenance; never reassign a human key to somebody else.

### Project notices during setup

After obtaining the official blank framework to establish a new research project, continue with the [installation and setup action](../agent-actions.md#install-the-framework), reusing actual supplied answers and collecting only missing information.
An authorless copy remains preparation while the required human key or License name is missing; do not invent a name or replace an upstream notice.
Keep the root LICENSE in place, including its complete license text and applicable ACME and third-party notices, original names and years.
The upstream Copyright 2026 Sheng Yin is an actual notice, not a replaceable project-author placeholder.
Append the chosen project's notice after the complete existing text as a separate statement limited to that human's original contributions or actual modifications in this research project, excluding the upstream ACME framework and other authors' contributions.
Do not clear the upstream name, refresh its year to the installation year or combine the project author's name into its copyright line.
This addition changes no Apache 2.0 terms, established other license choices or authorship; see the [license's redistribution and additional-statement provisions](https://www.apache.org/licenses/LICENSE-2.0).
No additional NOTICE file, relocated license, fixed notice syntax or new attribution field is required.

For example, an actually supplied name and project-establishment year may yield this independently scoped addition after the full license:

```text
Additional project copyright notice

Copyright 2026 Alice Smith

This notice applies to original contributions made by Alice Smith
in this research project, excluding the upstream ACME framework.
```

Use the new project's actual current establishment year by default and preserve the independently supplied name exactly, including its supported spaces and Unicode.
Do not infer the attribution name from the upstream author, path key, Git signature or GitHub login, or produce an empty-name notice.
Reuse an existing notice for the same actual human and contribution scope; a matching name alone establishes neither identity nor that scope.
Preserve existing notices and historical years during repeated setup, collaboration, cloning, upgrades and calendar changes rather than duplicating or refreshing them.
An existing research-repository clone retains its actual project identity, registrations, materials and notices; reuse the actual human's registered identity, supplement only genuinely missing information or an applicable notice and bind that new checkout when Git is used.
Framework upgrades and copying merge any changed LICENSE text while retaining destination project notices and other applicable content, without repeating initial registration.
Official-source inspection, backup, review, upgrade preparation and maintenance of the official framework itself do not select a new research project or require an additional project notice.
The agent judges actual purpose, identity and contribution scope and inspects the final people.json, LICENSE, necessary configuration and binding; tools validate their explicitly supplied fields and mechanical writes without deciding copyright ownership or completing attribution on the agent's behalf.
Installation, registration, attribution and binding create no Task, E, profile shell or source store and grant no research-start or publication authority.

## Repository names and use environments

Determine Git management from the selected folder's actual .git marker, including a Git worktree file, rather than executable availability or an enclosing checkout.
Without Git management, one explicitly registered local human may research locally with an absent or null repository name, without uploading or publishing local research content.
Authorized reads of the official framework and identified public research sources retain their actual instruction, offline and version-check conditions.
No environment flag, placeholder repository name or second identity registry is needed.

For a newly prepared unnamed personal configuration, use repository: null in repository/config.json while retaining necessary settings and human registration.
Do not derive a repository name from a folder or author key.
When enabling Git, register the human-chosen or explicitly confirmed repository name and explicitly bind the actual checkout before research writing or delivery, preserving existing content, allocation bounds and Task/E conditions.
An existing actual named project needs no repeated first-project registration.
Read-only material inspection and necessary setup or configuration repair remain available before registration.
Repository names use ASCII letters, digits and internal hyphens without underscores or spaces; validate that choice separately from the independent human path key.
Ask the human for an invalid choice's replacement rather than sanitizing it.

A new project copied or cloned from the official blank source must distinguish the official acme name from its own registration.
After identifying the actual new-project purpose, prepare repository, repository_display_name and repository_abbr as the project's actual human choices or null in both downloaded and Git-cloned blank copies, before treating them as project registration.
An inherited valid acme key does not establish a human choice; the same key is permitted when the human explicitly chooses or confirms it, without an official-name detector or reserved-name ban.
Without Git, retain a supplied repository key or null when unnamed; in a Git project, obtain the human's repository name before research writing or delivery, while independent reading and setup remain available.
The actual official repository retains its name, and an existing research-project clone preserves its registered identity and materials.
Determine that purpose from the human request and actual contents, without resetting existing project configuration or materials or using an empty registry alone as a fresh-installation signal.
Source inspection, backup, framework maintenance and project upgrades retain their actual source or target identity and do not repeat new-project registration.
An actual name registration or human-chosen update changes the repository key and its direct current consumers, without automatically changing independently chosen display settings or the README heading.
Preserve the ACME framework name, human keys, material identities and historical source facts.

repository_display_name and repository_abbr in repository/config.json hold the human-chosen project display name and abbreviation, independently of the repository key, human display_name, Git signature and remote address.
Each known choice is nonempty single-line text, may contain spaces or Unicode and retains the human's actual spelling; missing choices are null.
Reuse established project choices or collect the missing choices during actual setup, without deriving them from a folder, author, remote or official framework title.
When both are known, the agent maintains the root readme.md heading as `# <repository_abbr>: <repository_display_name>` by ordinary bounded editing, escaping Markdown as needed to render the chosen text faithfully and retaining the remaining contents.
Changing a display choice updates that current heading, without rewriting the ACME framework name or historical source facts.
Missing choices retain null and the existing heading while independent authorized setup, reading and work continue; ask only for the missing choices when forming the project heading is needed.
Report the missing title choices explicitly; a retained template heading is not a selected project name or completed display setup.
A new research project copied or cloned from the official blank source starts with its own choices or null, rather than inheriting the official project's display settings.
An existing shared-project clone retains its actual settings and heading, and personal-folder use needs no Git or remote setup for these choices.
The optional init helper supplies null display defaults; ordinary configuration and README edits suffice, without new initialization arguments, a heading generator or synchronization mechanism.

Git use supports local research and native versioning without a GitHub account or remote.
An existing Git-managed checkout keeps its Git and binding requirements if the executable becomes unavailable, without falling back to a personal-folder operator.
Local Git operations require no network preflight; the separately configured daily public-version check keeps its own scope.

When first establishing the actual GitHub project remote, after a relevant target change or for a remote operation needing fresh facts, compare the selected remote's repository name component with the registered local name.
An official framework source, intake source or reference-only upstream is not automatically that project remote, and a GitHub login selects no repository.
A difference permits a non-blocking suggestion to update the local repository key; keep the local name unless the human chooses the change, and maintain independent display settings only under their own choices.
The mismatch alone blocks neither local research nor an otherwise authorized remote operation.
Do not automatically rename the remote repository, derive a local choice by sanitizing the remote name or rewrite remote configuration to remove a mismatch.
Use the actual target address, account/channel and authority independently of name matching, reusing still-applicable evidence without a reminder registry or comparison on each local read.

## Checkout binding and personal operators

Each Git working copy binds research.actor and its worktree scope in Git's config.worktree, located with git rev-parse --git-path config.worktree.
Sessions in the same checkout read the same binding; linked worktrees bind independently.
identity-bind enables extensions.worktreeConfig and confirms only the selected checkout.
It removes the legacy shared actor after installing that explicit binding.
A new clone, a newly added worktree or a deliberately changed operator needs identity-bind.
Unbound, unknown and automatically copied bindings refuse research writes.
Ordinary folder use requires no Git installation or initialization; determine its operator from the currently explicitly identified human and existing human registration.
Without Git, the default supported use is one local human working personally on local files, without local multi-author collaboration, checkout arbitration or signature/history checks.
An authorless folder remains preparation until its actual first human is registered; the personal folder then uses that one registered human without inheriting an enclosing checkout's Git binding.
Retain external originals' actual attribution, necessary provenance and the same-human or separately authored correction boundary when receiving them.
Git binding, signature and delivery requirements apply to Git workspaces, and Git-dependent tools retain their actual prerequisites.
Worktree scope uses Git's administration identity, so moving a working directory does not by itself change its operator.
The global Git configuration is not changed.

Before enabling the extension, the binding tool preserves main-worktree-only core.worktree and core.bare=true settings in the main worktree configuration.
It refuses conflicting dormant settings and restores the original configuration if enabling fails.
It does not infer the former operators of other worktrees from a shared legacy value.

```powershell
python scripts/research.py identity-bind HUMAN
python scripts/research.py identity-add Another-Human --display-name "Another Human"
```

Binding changes the operator; it does not change the Git name or email.
Registration stores supplied Git signature and account mappings without configuring user.name or user.email.
The effective Git signature must identify the actual contributor through the registered name/email mapping.
Check it when a commit is actually needed, reusing correct settings and limiting any necessary changes to the selected checkout rather than global configuration.
The author key, License display_name, project display settings, checkout operator, effective Git signature and selected remote retain their separate responsibilities; optional init success does not establish that all have been set.
The identity-add example is not authorization to register a collaborator.
Supply their actual Git/GitHub mappings through the options when available.
Establish a source creator's correspondence before intake; matching display names alone are insufficient.

New local materials identify their actual registered human author.
Apply the [collaboration and maintenance boundary](#collaboration-maintenance-and-conflicts) to cross-author work.
Original imported authorship and exact source binding remain provenance through the receiving repository's registered external identities.
Git registration checks the current checkout operator without retaining a registrar history.
Acquisition and execution record their actual operator; reviews retain their actual checking relationship, and unknown historical attribution remains unknown.

<a id="collaboration-maintenance-and-conflicts"></a>
## Direct collaboration, maintenance and conflicts

Registered human collaborators use their own machines and local working copies of the shared research repository, synchronizing through GitHub or another Git hosting platform with push, pull and merge.
References to the shared repository and its existing checkout mean each human's own local working copy.
Different humans sharing one machine, operating-system account, physical working copy or private storage are outside the default supported scope.
Apply this scope without machine identification, isolation certification, private-file inventories or mandatory environment preflight.
Private settings and originals retain their [local-only boundary](organization.md#machine-local-locators).
Additional parallel research copies for one human are not recommended; this framework defines no coordination or management workflow for them.
Within each human's working copy, the actual operator binding remains shared by its chats and does not change another author's mathematical or manuscript choices.

Each collaborator maintains shared registration and derived navigation at their responsible scope.
Every authored mathematical document retains exactly one human author, including a joint Task.
Initial intake preparation follows the [common adaptation rule](records.md#receiving-and-adapting-selected-content); later corrections to another human's document belong in the correcting human's own suitable material with exact references.
This applies to administrative wording, paths and layout within an authored body as well as substantive mathematics.
Only the same established human may directly revise the body under actual authority, fixed-version and evidence requirements.
For an external representation, an explicitly adopted local_human correspondence in the existing external-person record can establish that relationship; names, a write argument or changing the checkout binding alone cannot.
Do not take over another human's Task/E.
Shared administration needs no per-author approval, additional review or maintenance receipt.
Existing activity-specific roles and publication boundaries retain their scope.

Classify an actual maintenance or integration conflict by its content into two kinds:

- Resolve administrative inconsistencies directly using the [core principles](../readme.md#core-principles-and-interpretation) and applicable topic rules.
  Act when they determine the choice; seek a human ruling only for a remaining decisive gap in intent, authority or facts, identifying the concrete competing content and missing choice.
- For a substantive mathematical conflict, identify the competing statements/evidence and affected materials, then obtain human approval for the scoped mathematical recheck before performing it.
  Preserve the competing evidence rather than silently selecting, combining or rewriting one side as a resolution.
  Reuse explicit approval already given for that same recheck scope without requesting it again.
  Approval for rechecking alone neither transfers authorship nor authorizes substantive editing of another author's material.

Reading enough to locate a difference does not establish a new mathematical verdict.
This conflict procedure adds no approval to routine maintenance, ordinary authorized research in each author's own materials or an already authorized review.
Same-human repairs in acquired material preserve original mathematics and actual acquisition provenance; keep the actual input version separate from a receiving revision.
Distinct research repositories reuse material through intake; another author in this shared repository does not by itself create an intake operation.
That reuse covers permitted authored mathematics and bibliography, not either repository's private local literature documents or holding accounts.

## Identifier and repository identity

Local fixed material paths use `Author_Kind_F0001_v1.md`; rolling S/D omit `_vN`.
Imported C/T/R/L/J use receiving external identities such as `author3_repo2_C_F0001_v1.md`, with chosen local classification, line, serial and version and exact original per-unit source facts.
External T is restricted to a necessary joint contract, with no E; own personal import uses ordinary local identities.
J native files share their numbered group identity.
U uses its separate `SourceKey/Author[_repoN]_U001_v1.md` source-key/unit placement contract without requiring an external-author number.
The human key identifies authorship, not a paper byline, ownership permission or an automatic right to alter an acquired original.

Each author/origin/kind/line has an independent numeric sequence: F0001 through F9999, F10000 and onward.
The chosen research line letter remains unchanged; a Task-derived address inherits only its letter.
C/T/R/L/U/J identities and continuing S identities are not recycled.
D is a working address, stable during its current use and reusable after retirement; a reused D inherits none of the earlier draft's content, scope, review or authority.
A materially different statement/question gets its appropriate new family; a substantive new proof within an unchanged Claim gets a material revision.
Source-unit numbers retain the existing sequence within their citation key, separate from research-line allocation.

repository/config.json stores this repository's actual key, separate project display name and abbreviation, necessary shared settings and the compact `material_next` map of next unissued material-family numbers.
Machine-local interpreters, OS versions, virtual-environment state and their mirrors do not belong in shared configuration; necessary nonsensitive choices use the [runtime home](organization.md#machine-local-runtime), with Git configuration and private resources at their existing responsible homes.
Determine project remote addresses from native Git configuration and the actual selected target under the current instruction and authority, without a project URL mirror in config.json.
It contains no global identity or local self-repository number.
repository/people.json registers local humans by unique readable names such as Yin, Alice and Alice2, with actual Git/GitHub mappings and no shared active-user setting.
Canonical external author numbers are reserved and cannot register or bind a local operator.

repository/repositories.json and repository/intake-people.json are the sole local homes for external repoN and authorN records.
Numbers begin at 1, increase without reuse and have no padding or underscores.
Maintain the selected repository's authors and author's source_repositories together under the existing short lock.
Names, addresses, foreign numbers and Git revisions alone do not prove identity or establish correspondence.
The agent prepares actual adopted source facts and explicit receiving correspondence, asking for a human ruling only for a real unresolved contradiction or collision.
See the [local external format](../material-format.md#local-external-identities-and-prepared-correspondence).

Acquired C/T/R/L/J retain the original source author name, path, line, family/version, selected anchor and fixed revision in provenance, while local filenames describe the prepared receiving content independently.
Repeated acquisition and later versions reuse the established receiving family.
Onward transfer translates selected original facts through explicit receiving correspondence; foreign repoN/authorN tokens never implicitly identify receiving records.
The immediate sender remains transport, separately from the original source.
Do not reacquire this repository's own returning originals or create a self entry to do so.
A distinct external contribution can use an existing local input through prepared exact correspondence without importing that input again.

U retains its original source path, author and input physical version in provenance; the receiving canonical work key, unit position and prepared physical version identify its local content separately.
The receiving key/number defines one position across authors and external prefixes.
Prepare precise declaration/reference edits, and validate affected final positions with unmoved siblings and all same-batch destinations.
Preserve an established original repoN/family's receiving number across versions; a newly occupied position fails without automatic renumbering.
Keep exact original/local paths, anchors, acquired scope, source/transport distinctions and availability at their existing provenance home.
An exact fixed source locator uses receiving repoN, revision, path and anchor under the [intake rules](intake.md).
Displayed names are informative facts, not automatic identity keys.

Readers accept canonical paths and actual anchors, with the selected Git view's own canonical registration tables.
A native J config.json is not a repository registration entrance.
Case-insensitive path collisions and conflicting selected original bindings fail without choosing the first match.
An explicit J refresh replaces only the same original repository and source J family/path, established from the occupied entrance and necessary native provenance.
Historical acquired J scopes remain recorded facts; selected current scope and actual current references have their own [intake checks](intake.md#homes-and-independent-reuse).

## Allocation and concurrency

Each actual human author allocates within the relevant kind/line sequence.
For C/T/R/L/J and continuing S, `repository/config.json` keeps one `material_next` entry per actual author/origin/kind/research-line namespace, with positive integer next unissued numbers only.
Local registered authors and receiving external authorN/repoN namespaces stay distinct; an original source serial or immediate sender does not replace the actual receiving namespace.
U uses the same compact map with its separate citation-key/unit namespace across authors and origin prefixes, under the [allocation format](../material-format.md#material-family-allocation-state).
D is outside this permanent counter because its retired working address can be reused.
Retiring a material, replacing it through another author or line, or leaving its namespace empty does not decrease the bound or make an issued fixed identity available again.
No per-deletion entry, issue date, retirement log, reserved-file stub, hash or migration registry is required.

Before the first relevant allocation or retirement, initialize the affected entry from an agent-confirmed upper bound on previously issued family numbers.
Surviving filenames supply only a lower bound; if the actual used-number upper bound is unresolved, resolve that concrete initialization question rather than resetting the counter or reconstructing Git history automatically.
Under the existing short mutation lock, re-read the stored bound and current occupation, issue a new family and advance the bound without decreasing it after deletion or failure.
The destination remains exclusively created and an occupation conflict fails clearly; unused gaps are acceptable.
Direct agent authoring maintains this same current state instead of bypassing it.
Installing a new explicitly chosen receiving family or U position also advances its actual namespace bound; a fresh number below that initialized bound is not available even if no file occupies it.
An established imported family keeps its existing receiving correspondence across physical versions, and a next physical revision allocates no new family number.
Clean bootstrap starts with an empty map and inherits none of another repository's counters.

Revisions and append/select operations protect the actual same-material read, predecessor/current-main check, modification and publication under the short lock.
Candidate appends preserve fresh history even when the selected decision is unchanged; stale selecting operations fail without silently retrying another predecessor.
Coordinate direct edits to the same material.
A duplicate L family at another home is an error, not a second allocation sequence.

Family-number issuance, coupled identity registration and intake/U allocation use the OS lock at `repository/.lock`, as do selected helpers for navigation or bibliography publication.
Ordinary bounded navigation, bibliography prose and explanatory edits coordinate their actual write scope and preserve unrelated and concurrent content without universally entering a helper's lock and publication protocol.
Wait at most 30 seconds by default; `--maintenance-wait SECONDS` configures the bounded wait and zero fails immediately.
Waiting is cancellable, uses monotonic time and emits one concise notice when contended.
Persistent lock-file existence is normal.
Re-read shared state after acquiring the lock; do not hold it across network retrieval, agent work, broad tests or long computation.

<a id="submission-checks"></a>
## Git delivery

Research proceeds in parallel; Git delivery within one human's local worktree proceeds serially.
Before research writing or delivery, a Git-managed project has its human-chosen registered name and the actual operator binding; native Git supplies no such authorization by itself.
One responsible agent coordinates each intended batch, index and commit.
Preserve another agent's staged work; identify actual paths rather than a research-line glob.
Keep submitted files stable, inspect the exact index, and confirm the completed commit matches the intended deliverable.
Navigation in a commit must resolve within that same deliverable.
If relevant files or index change, repeat the affected delivery inspection.
Ordinary coordination does not establish a new lock, permanent role or research-wide pause.

Plain commit/push requests perform Git delivery.
Inspect intended scope, local actor, effective author/committer, actual outgoing commit identities, branch relationship and the intended tree.
Use native Git status, diffs, the index and commit information as useful aids rather than a compulsory command sequence or framework delivery gate.
Resolve concrete omissions, sensitive files or identity conflicts at their affected scope.
A draft or unfinished result may be committed with its truthful status.
Do not automatically run framework regressions, full material scans, recursive proof review or PDF-store hashing.
Reuse applicable construction/research verification; repeat it only for relevant changes, repaired failures or uncovered uses.

When push is authorized, choose relevant checks for the actual target and account/channel under the [connection responsibilities](#git-and-github-connection-checks), verify the target remote tip and branch relationship, push the authorized local tip and verify the remote result.
Connectivity alone authorizes no mutation.
Within an authorized remote-delivery sequence, a pending batch is its already committed, unpublished work for the selected repository, branch, destination and delivery scope.
Publish that batch before constructing the next delivery batch; a concrete blocker permits only the smallest committed repair and necessary references first.
Other unpushed commits do not create that sequence; a local-only commit needs neither push authority nor a network check merely because earlier commits remain unpublished.
A worktree-only fix does not repair committed HEAD.
Preserve concurrent work and each contribution's authorship.
Resolve divergence and inspect the affected delivery again if the local or remote tip changes.
Commit/push requests do not authorize history rewriting or force-push; any rewrite requires explicit human authority.
A supplied login is not authentication, and an email or remote URL does not establish the logged-in person.

Let Git perform file merging, then inspect the actual affected result and resolve conflicts under the [maintenance rule](#collaboration-maintenance-and-conflicts).
Git's lack of a text conflict establishes neither mathematical agreement, source applicability nor permission to edit another human's body.
Inspect earlier versions only when the actual question needs them; no ordinary commit or merge requires every parent to contain a material, a BASE selector, preimage mapping or framework pass token.

### Shared research Git authority and integration

When a human actually authorizes establishing, advancing or continuing [joint Task collaboration](tasks.md#shared-git-research), routine fetch, pull/merge, commit and push within that assigned collaboration scope are permitted by default.
Apply explicit human restrictions such as local-only work, commit without push, postponed synchronization or limited publication content; an absent separate push grant does not block the default.
Use the current assignment and existing participation facts without asking for separate mode adoption, first-delivery approval or recurring permission, or requiring a permission sentence, new T/E decision or authorization record.
Determine the actual repository, collaboration branch and publishable scope from the current Task, existing agreements and native Git remote/tracking facts, reusing sufficient information directly rather than creating a URL/branch mirror, authorization table, flag or receipt.
Clarify only a genuinely missing destination or branch needed for execution, rather than asking again whether routine joint-research delivery is allowed; actual account capabilities and platform restrictions still apply.
A joint file, active label, clone, registered identity, configured remote or successful connection alone selects no research or delivery.
Apply the default to the currently assigned human-authorized collaboration, without scanning every joint Task or treating Git permissions as permission to begin or resume research.
Handle target changes within that scope from actual facts and existing arrangements; publication beyond it, unrelated remote operations, PR creation, history rewriting, force-push and branch-protection changes are outside these default permissions.

Choose native Git retrieval, fast-forward or ordinary merge from the actual branch relationship and explicit integration target, without prescribing one command sequence, helper or whole-library check.
Integration concerns branches and commits, rather than pulling only one Task's files; select the relevant changed content for inspection afterwards.
Protect uncommitted work, other sessions' staged contents and each contributor's authorship without requiring the entire worktree to be clean or defaulting to whole-tree add, stash, discard, overwrite or rebase.
Coordinate integration, index and commits serially in this working copy, choosing any necessary native saving or temporary arrangement for the actual state without another permanent role, lock or parallel-copy management system.
After Git merges files, inspect affected mathematics, fixed versions, exact inputs, references and review applicability under the existing [conflict rule](#collaboration-maintenance-and-conflicts); a clean text merge certifies neither mathematical agreement nor authority to edit another human's body.
Resolve administrative conflicts within existing authority, preserve competing mathematical evidence, and reuse any applicable scoped recheck approval rather than requesting it again.
Read changed applicable rules and contracts under the [current-rule duty](workflow.md#proportionate-execution); synchronization alone establishes no adoption or research resumption.

Before a push, inspect the whole outgoing commit chain and its actual destination under [serial delivery](#submission-checks), rather than treating the currently staged paths as the whole publication scope.
Resolve an unclear or unauthorized outgoing scope before publishing it, without automatically creating another branch or rewriting history to bypass that issue.
Obtain the fresh remote facts needed for delivery; if the remote advances or rejects the push, retrieve, normally integrate, inspect affected changes and retry within the existing authority and effective limits, without force-push or unlimited retries.
Use the project's actual collaboration branches and contribution requirements; protection or a PR requirement does not itself authorize another remote action or a new publication workflow.
Verify the actual remote result and report a connection, integration or delivery failure with its concrete unconfirmed update, saved commit or unfinished push scope, using existing materials or an ordinary response rather than a queue or retry ledger.
Continue only authorized local work independent of the missing remote facts, deferring the parts that depend on them; an explicit instruction requiring successful synchronization and effective execution stops or allowance limits take precedence.
Keep the existing pending-batch ordering within an authorized delivery sequence; unrelated unpublished commits do not block all local research.

### Explicit material checks

Use useful operation-local material, field, source and reference readers for the explicitly chosen question and actual working files or Git view.
These tools report their stated structural facts, without an aggregate submission verdict or automatic contribution/receiving-history reconstruction.
Address discovery validates the requested kind; creation validates its actual author/origin, kind and line sequence, and mutation validates the selected family and its versions/direct inputs.
Selected Strategy checks include actual ancestors, and an explicitly requested current-E check includes its selected Task decision.
Candidate enumeration does not validate unrelated namespaces or silently drop malformed candidates that could occupy the selected namespace.
Explicit full discovery or navigation regeneration retains its declared complete scope.
The agent judges actual receiving versus local revision, chosen originals, contributors and author permissions from the real materials and instruction under the [agent/tool responsibility](workflow.md#agent-and-tool-responsibilities).
Authored body changes, including layout maintenance, retain the same-human and separately authored correction requirements in the actual editing and receiving work.
Keep fixed-version, source-preservation and actual-review duties at their responsible interfaces, reusing necessary existing evidence rather than replaying them as a commit audit.
An unstaged repair cannot cure a defect in another selected view.
Necessary intake identities and acquired-record facts use that same selected view as their materials, including explicit local-revision inputs and onward provenance under the [intake rule](intake.md#homes-and-independent-reuse).
Their recorded local paths are relative to the record's repository/view; current checkout aliases, links or availability supply no extra condition on fixed Git evidence.

Registration operations and agent-prepared external-table maintenance preserve affected rows, allocation constraints and necessary table-local counterparts, including both association entrances.
Before removing a registration or changing adopted source/author correspondence, the agent identifies necessary actual consumers and prepares their coherent repair from the provenance and current use.
Ordinary searches may locate candidates, but neither candidate discovery nor a table-check PASS establishes complete consumer coverage.
A registration change alone does not select unchanged material headers, source links, intake records or native configurations for checking.
Choose any needed reference check explicitly at its actual path/field scope, using the selected view's shared material-header, source-locator and JSON readers.
These selected checks report the owning path, field and inconsistent number without full material/proof or intake-object validation, historical J availability reconstruction, private-source inspection, background-origin traversal or automatic identity repair.

Apply the [common maintenance boundary](records.md#substantive-material-retention): valid J/E/intake maintenance, coherent moves and authorized reproducible-output cleanup add no generic changed-file reminder.
Concrete identity, reference, native-format, explicit-decision and review-binding errors remain observable; structural success supplies no mathematical review.
Choose ordinary public-reference and path checks for needed registry prose or source links, without treating them as a holding, edition, availability or private-byte verdict.
An outgoing-link check does not discover unchanged incoming consumers or certify their coverage.
The agent identifies necessary incoming consumers through scoped searches and reading, then selects their actual files and target locators for checking in the chosen view.
Use the shared link and locator readers on that explicit scope, requiring exactly one occurrence for each selected Markdown anchor, including Strategy parents and navigation targets.
Registry outgoing checks may stay within changed blocks; an explicit incoming check uses the selected consumer's complete text and designated targets.
The agent chooses any needed [explicit source check](literature.md#selected-source-checks) in the actual requested view; selected source operations retain their own declaration and byte constraints.
The agent selects actual bibliography references in mixed text; a token search is neither an active-citation verdict nor a completeness certificate.
There is no aggregate research checker, automatic Git hook, publication certificate or verification registry.
Work-specific checking responsibilities belong to the [workflow](workflow.md).
