# Human Identity and Numbering

## Stable keys and local attribution

repository/people.json registers permanent human IDs, display names, timezone-bearing minute timestamps, accepted Git name/email pairs and associated GitHub logins.
Human/repository keys use letters, digits and internal hyphens; underscores separate identifier fields.
Registration checks keys and GitHub logins without regard to case, rejects duplicate Git signature assignments, and retains canonical spelling.
Display-name changes do not rename records.
Correct mappings through traceable framework maintenance; never reassign a human key to somebody else.

Each working copy binds research.actor and its worktree scope in Git's config.worktree, located with git rev-parse --git-path config.worktree.
Sessions in the same checkout read the same binding; linked worktrees bind independently.
identity-bind enables extensions.worktreeConfig and confirms only the selected checkout.
It removes the legacy shared actor after installing that explicit binding.
A new clone, a newly added worktree or a deliberately changed operator needs identity-bind.
Unbound, unknown and automatically copied bindings refuse research writes.
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

Each collaborator's agents may directly maintain administrative locations in shared files and another author's materials, including paths, links to the same object/version, derived navigation and purely administrative prose or layout.
Preserve the mathematical object/version, hypotheses and quantifiers, definition/convention, argument, adopted inputs, source identity and review meaning.
A short link, field or sentence change that alters any of these substantive facts is not administrative maintenance.
Substantive mathematics remains in the responsible author's separate materials and authorized work; another collaborator records their actual contribution at their own responsible home with exact references.
Do not take over another human's Task/E.
Routine administration needs no per-author approval, additional review or maintenance receipt, and adds no runtime author-equality gate.
Existing activity-specific roles and publication boundaries retain their scope.

Classify an actual maintenance or integration conflict by its content into two kinds:

- Resolve administrative inconsistencies directly under the applicable framework rule.
  If that rule is unclear, report the concrete competing administrative content and the missing rule choice for a human ruling.
- For a substantive mathematical conflict, identify the competing statements/evidence and affected materials, then obtain human approval for the scoped mathematical recheck before performing it.
  Preserve the competing evidence rather than silently selecting, combining or rewriting one side as a resolution.
  Reuse explicit approval already given for that same recheck scope without requesting it again.
  Approval for rechecking alone neither transfers authorship nor authorizes substantive editing of another author's material.

Reading enough to locate a difference does not establish a new mathematical verdict.
This conflict procedure adds no approval to routine maintenance, ordinary authorized research in each author's own materials or an already authorized review.
Administrative repairs in acquired material preserve original mathematics and actual acquisition provenance; do not replace captured original locators with receiving addresses or turn local feedback into a source amendment.
Distinct research repositories reuse material through intake; another author in this shared repository does not by itself create an intake operation.
That reuse covers permitted authored mathematics and bibliography, not either repository's private local literature documents or holding accounts.

## Identifier and repository identity

Local fixed material paths use `Author_Kind_F0001_v1.md`; rolling S/D omit `_vN`.
Imported C/R/L/J use receiving external identities such as `author3_repo2_C_F0001_v1.md`, with an explicitly chosen receiving family serial and exact original source binding.
J native files share their numbered group identity.
U uses its separate `SourceKey/Author[_repoN]_U001_v1.md` source-key/unit placement contract without requiring an external-author number.
The human key identifies authorship, not a paper byline, ownership permission or an automatic right to alter an acquired original.

Each author/origin/kind/line has an independent numeric sequence: F0001 through F9999, F10000 and onward.
The chosen research line letter remains unchanged; a Task-derived address inherits only its letter.
C/T/R/L/U/J identities and continuing S identities are not recycled.
D is a working address, stable during its current use and reusable after retirement; a reused D inherits none of the earlier draft's content, scope, review or authority.
A materially different statement/question gets its appropriate new family; a substantive new proof within an unchanged Claim gets a material revision.
Source-unit numbers retain the existing sequence within their citation key, separate from research-line allocation.

repository/config.json stores this repository's actual name, URL when known, timezone and necessary runtime settings.
It contains no global identity or local self-repository number.
repository/people.json registers local humans by unique readable names such as Yin, Alice and Alice2, with actual Git/GitHub mappings and no shared active-user setting.
Canonical external author numbers are reserved and cannot register or bind a local operator.

repository/repositories.json and repository/intake-people.json are the sole local homes for external repoN and authorN records.
Numbers begin at 1, increase without reuse and have no padding or underscores.
Maintain the selected repository's authors and author's source_repositories together under the existing short lock.
Names, addresses, foreign numbers and Git revisions alone do not prove identity or establish correspondence.
The agent prepares actual adopted source facts and explicit receiving correspondence, asking for a human ruling only for a real unresolved contradiction or collision.
See the [local external format](../material-format.md#local-external-identities-and-prepared-correspondence).

Acquired C/R/L/J retain the original source author name, path, line, family/version and fixed revision in provenance, while local filenames use receiving authorN/repoN and the explicitly selected receiving serial.
Repeated acquisition and later versions reuse the established receiving family.
Onward transfer translates selected original facts through explicit receiving correspondence; foreign repoN/authorN tokens never implicitly identify receiving records.
The immediate sender remains transport, separately from the original source.
Do not reacquire this repository's own returning originals or create a self entry to do so.
A distinct external contribution can use an existing local input through prepared exact correspondence without importing that input again.

U retains its original source path, author and physical version while the receiving canonical work key and unit position may differ.
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
Independent material creation does not take the shared-maintenance lock: it exclusively creates the next destination and returns a clear retry instruction on a collision.
Revisions and append/select operations protect the actual same-material read, predecessor/current-main check, modification and publication under the short lock.
Candidate appends preserve fresh history even when the selected decision is unchanged; stale selecting operations fail without silently retrying another predecessor.
Coordinate direct edits to the same material.
A duplicate L family at another home is an error, not a second allocation sequence.

Identity registration, shared navigation publication, explicit bibliography updates and intake/U allocation use the OS lock at `repository/.lock`.
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

When push is authorized, use the repository's connectivity preflight and actual account, verify the target remote tip and branch relationship, push the authorized local tip and verify the remote result.
Connectivity alone authorizes no mutation.
Publish an existing pending committed batch before constructing the next batch; a concrete blocker permits only the smallest committed repair and necessary references first.
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
Changed outgoing links and incoming links to affected public targets are separate scopes in the selected view.
Read each discovered incoming consumer in full even when it has other changes, checking only its actual links to affected targets.
Registry outgoing checks may stay within changed blocks, while unchanged unrelated broken links remain outside the incoming scope.
The agent chooses any needed [explicit source check](literature.md#selected-source-checks) in the actual requested view; selected source operations retain their own declaration and byte constraints.
The agent selects actual bibliography references in mixed text; a token search is neither an active-citation verdict nor a completeness certificate.
There is no aggregate research checker, automatic Git hook, publication certificate or verification registry.
Work-specific checking responsibilities belong to the [workflow](workflow.md).
