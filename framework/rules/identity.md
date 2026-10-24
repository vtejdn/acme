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
Local reading, edits, checks, commits and clean exports require no network preflight.
The [daily metadata read](../versioning.md#official-version-check) retains its bounded public HTTPS endpoint, cache and separately authorized upgrade boundary.

## Stable keys and local attribution

repository/people.json registers permanent human IDs, display names, actual registering humans, accepted Git name/email pairs and associated GitHub logins.
New human/repository registrations contain no administrative registration timestamp; retained obsolete values are removed from maintained metadata rather than converted or kept as compatibility facts.
Human/repository keys use letters, digits and internal hyphens; underscores separate identifier fields.
Registration checks keys and GitHub logins without regard to case, rejects duplicate Git signature assignments, and retains canonical spelling.
Display-name changes do not rename records.
Correct mappings through traceable framework maintenance; never reassign a human key to somebody else.

Each Git working copy binds research.actor and its worktree scope in Git's config.worktree, located with git rev-parse --git-path config.worktree.
Sessions in the same checkout read the same binding; linked worktrees bind independently.
identity-bind enables extensions.worktreeConfig and confirms only the selected checkout.
It removes the legacy shared actor after installing that explicit binding.
A new clone, a newly added worktree or a deliberately changed operator needs identity-bind.
Unbound, unknown and automatically copied bindings refuse research writes.
Ordinary folder use requires no Git installation or initialization; determine its operator from the currently explicitly identified human and existing human registration.
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
The effective Git signature must identify the actual contributor through the registered name/email mapping.
The identity-add example is not authorization to register a collaborator.
Supply their actual Git/GitHub mappings through the options when available.
Establish a source creator's correspondence before intake; matching display names alone are insufficient.

New local materials identify their actual registered human author.
Apply the [collaboration and maintenance boundary](#collaboration-maintenance-and-conflicts) to cross-author work.
Original imported authorship and exact source binding remain provenance through the receiving repository's registered external identities.
Registration, acquisition and execution record their actual operator; reviews retain their actual checking relationship, and unknown historical attribution remains unknown.

<a id="collaboration-maintenance-and-conflicts"></a>
## Direct collaboration, maintenance and conflicts

Registered human collaborators work directly in the shared research repository and its existing checkout.
Additional parallel research copies are not recommended; this framework defines no coordination or management workflow for them.
The checkout's actual operator binding remains shared by its chats and does not change another author's mathematical or manuscript choices.

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

repository/config.json stores this repository's actual name, URL when known, necessary runtime settings and the compact `material_next` map of next unissued material-family numbers.
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

Family-number issuance, identity registration, shared navigation publication, explicit bibliography updates and intake/U allocation use the OS lock at `repository/.lock`.
Wait at most 30 seconds by default; `--maintenance-wait SECONDS` configures the bounded wait and zero fails immediately.
Waiting is cancellable, uses monotonic time and emits one concise notice when contended.
Persistent lock-file existence is normal.
Re-read shared state after acquiring the lock; do not hold it across network retrieval, agent work, broad tests or long computation.

## Submission checks

Research proceeds in parallel; Git delivery in a shared worktree proceeds serially.
One responsible agent coordinates each intended batch, index and commit.
Preserve another agent's staged work; identify actual paths rather than a research-line glob.
Keep submitted files stable, inspect the exact index, and confirm the completed commit matches the intended deliverable.
Navigation in a commit must resolve within that same deliverable.
If relevant files or index change, repeat the affected delivery inspection.
Ordinary coordination does not establish a new lock, permanent role or research-wide pause.

Plain commit/push requests perform Git delivery.
Inspect intended scope, local actor, effective author/committer, actual outgoing commit identities, branch relationship and the intended tree.
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

### Explicit material checks

`python scripts/check-research-submission.py` explicitly checks INDEX against its parent(s).
`--working-tree` selects preparation bytes only; `--commits BASE` checks the final BASE-to-HEAD net change rather than replaying intermediate contents.
`--push --github-account VERIFIED_LOGIN` adds an outgoing identity context to that explicit check; it performs no network push and does not authenticate the supplied login.
An unstaged fix cannot repair a checked index or commit.

These optional checks expose the requested view's bytes/differences, explicit identity/field/reference errors and declared review-binding consistency at the affected scope.
Address discovery validates the requested kind; creation validates its actual author/origin, kind and line sequence, and mutation validates the selected family and its versions/direct inputs.
Selected Strategy checks include actual ancestors, and an explicitly requested current-E check includes its selected Task decision.
Candidate enumeration does not validate unrelated namespaces or silently drop malformed candidates that could occupy the selected namespace.
Explicit full discovery or navigation regeneration retains its declared complete scope.
An initial index checks its staged items, and a merge's actual differences are available against its parents.
They do not infer same mathematics, relocations, review transfer or source identity.
The agent judges fixed-version and actual-review obligations from content under the [agent/tool responsibility](workflow.md#agent-and-tool-responsibilities).
An unstaged repair cannot cure a defect in another selected view.

Changes to the canonical external repository or author table check affected rows, allocation constraints and necessary table-local counterparts, including both association entrances, in the selected postimage.
Before removing a registration or changing adopted source/author correspondence, the agent identifies necessary actual consumers and prepares their coherent repair from the provenance and current use.
Ordinary searches may locate candidates, but neither candidate discovery nor a table-check PASS establishes complete consumer coverage.
A registration change alone does not select unchanged material headers, source links, intake records or native configurations for checking.
Choose any needed reference check explicitly at its actual path/field scope, using the selected view's shared material-header, source-locator and JSON readers.
These selected checks report the owning path, field and inconsistent number without full material/proof or intake-object validation, historical J availability reconstruction, private-source inspection, background-origin traversal or automatic identity repair.

Apply the [common maintenance boundary](records.md#substantive-material-retention): valid J/E/intake maintenance, coherent moves and authorized reproducible-output cleanup add no generic changed-file reminder.
Concrete identity, reference, native-format, explicit-decision and review-binding errors remain observable; structural success supplies no mathematical review.
Generic submission checks registry prose and source links at their ordinary public-reference/path scope, without a holding, edition, availability or private-byte verdict.
Generic submission checks changed files' outgoing links; it does not discover unchanged incoming consumers or certify their coverage.
The agent identifies necessary incoming consumers through scoped searches and reading, then selects their actual files and target locators for checking in the chosen view.
Use the shared link and locator readers on that explicit scope, requiring exactly one occurrence for each selected Markdown anchor, including Strategy parents and navigation targets.
Registry outgoing checks may stay within changed blocks; an explicit incoming check uses the selected consumer's complete text and designated targets.
The agent chooses any needed [explicit source check](literature.md#selected-source-checks) in the actual requested view; selected source operations retain their own declaration and byte constraints.
The agent selects actual bibliography references in mixed text; a token search is neither an active-citation verdict nor a completeness certificate.
There is no aggregate research checker, automatic Git hook, publication certificate or verification registry.
Work-specific checking responsibilities belong to the [workflow](workflow.md).
