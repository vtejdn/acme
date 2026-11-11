# ACME Framework Versions

The name is Autonomous and Collaborative Mathematical Exploration (ACME).
Repository names and research IDs remain independent.

The sole current framework release identifier is `framework_version` in [framework/version.json](version.json), whose only field is framework_version.
Use three nonnegative decimal integers, `MAJOR.MINOR.PATCH`, without leading zeros, a date prefix or a leading `v`.

## Scope and Compatibility

The version covers common rules, templates, tools and installation guidance as one framework.
Compatibility alone does not justify retaining non-substantive content, including administrative and authorization history; apply the [core principles](readme.md#core-principles-and-interpretation) and [content-retention rule](rules/records.md#substantive-material-retention).

Assess compatibility for repositories that already have ACME installed and are taking the relevant upgrade.
An upgrade is compatible when ordinary synchronization and bounded merges of local edits let those repositories continue using their existing materials and project setup without substantive maintenance.
An upgrade is incompatible when continued use requires substantive work such as migrating stored material, restructuring project configuration or adapting an existing integration to a removed supported interface.
A change confined to first-installation eligibility leaves installed repositories compatible.

During development before 1.0.0, MAJOR remains zero.
Increment MINOR for an incompatible upgrade and PATCH for other framework changes.

Historical compatibility obligations begin with formal releases starting at 1.0.0.
Development releases in the 0.x series do not promise continued support for their obsolete formats, readers or workflows.
Remove compatibility promises and adapters with no actual supported object.
A test can construct an older input without creating a support obligation.
A future formal release does not retroactively turn 0.x formats into supported protocols.

For formal releases from 1.0.0 onward, assess effects on actual supported releases and consumers and state the applicable compatibility or migration boundary.
This does not require keeping every old parser forever or certifying old mathematics under new rules.
Actual authorship, source assertions, mathematical decisions and recorded review scope remain truthful at every development stage.
Adopting this rule does not issue a release or advance the installed version.

Research content, manuscript revisions, local project choices and personal preferences do not by themselves increment the framework version.
Claim/Task `vN` labels and managed material `name_vN.md` versions keep their own meanings and compatibility checks.
A framework release neither proves a Claim nor certifies a manuscript.

Strategies remain rolling under their stable S identity.
Substantial progress or a local repair within the same mechanism does not require a successor; a genuinely distinct route records its actual lineage.
Fixed mathematical evidence and historical review scope remain separate.

A released identifier must not be reassigned to a different release.
A version number is not an exact byte identity or a review verdict.
Cross-repository intake follows the receiving installation's current rules for the actual selected fixed-source content under the [common adaptation rule](rules/records.md#receiving-and-adapting-selected-content).
Different sender versions, absent installation metadata or lack of current-format support alone do not forbid adequate receiving-side preparation or require changing the sender.
The receiving agent checks the selected mathematics and claimed state for its intended use, original authorship and sufficient fixed-source facts, and prepares a conforming local result with the existing evidence and provenance duties intact.

## Official version tags and upgrade notes

Each commit published to the official ACME repository has its own stable version tag, named exactly by that commit's three-integer framework_version without a leading v.
Preserve released identifiers and tag targets; different published contents require a new released version rather than reusing or retargeting one.
The tag identifies the official source commit, while the installed version metadata remains the sole local version authority.
The official repository and published branch retain the [existing metadata source](#official-version-check), and actual publication follows the [connection and authority rules](rules/identity.md#git-and-github-connection-checks).
This contract grants no commit, tagging or remote-publication authority by itself.

### Contents of an upgrade note

Each new official version ships `framework/upgrade/<target-version>.md` for the existing installations that can take that upgrade.
Identify the target version, actual preceding published version, its fixed official source and any restriction on which installations can take the upgrade at the start of the note.
A draft identifies its working baseline and any pending scope until the target and shipped changes are verified at closeout.
The body covers two subjects.

1. **What changed.** Summarize the behavior, interface or file location that changed and identify the affected shipped paths, grouped by feature or by common handling.
   For a removed or moved path, field or call that requires local action, give its exact former name and any replacement.
   Use the predecessor and candidate Git differences to verify coverage of additions, modifications, removals and moves, including supplied human-document changes at their actual language and path scope.
   Link to the responsible installed rule or interface when the reader needs its full contract.
2. **Additional actions for this version.** State what an existing installation must do beyond the [ordinary upgrade procedure](#upgrading-an-installed-framework).
   For each action give the local condition that triggers it, what to change and preserve, any necessary order and the check that establishes completion of that particular adaptation.
   Include steps that must precede replacement, removal of an exclusion or advancement of the installed version when their order matters.
   When the usual synchronization and local merges suffice, say so explicitly.
   A duty first triggered during subsequent research belongs in the change summary.

Ongoing research and operating instructions belong in the responsible rules and tool documentation, and design rationale, construction tests and acceptance cases belong in development materials.
Keep the notes for offered upgrade paths together, with references usable from the distributed framework. [Upgrade notes](upgrade/)
When an editorial cleanup of retained notes is in scope for a later distribution, preserve each original version transition, its source facts, compatibility limits and all still-needed migration actions and dependencies.
Clarify later general handling in the selected target's common rules or a later note, keeping each earlier note about its own release.

## Upgrading an installed framework

The [upgrade action](agent-actions.md#upgrade-installed-framework) is separate from daily metadata checking and [first installation of selected framework files](agent-actions.md#install-the-framework).
One explicit upgrade assignment covers ordinary retrieval, agent-selected adaptation and necessary checks; ask only for a decisive conflict, missing fact or operation outside that authority.

1. Identify the installed version and selected official target, obtain its source in a creator-owned child of root `.tmp/`, and fix the exact target commit.
   Verify the selected official source and agreement among target tag, version metadata and target-version note before preparing installation; a later moving branch tip does not change the selected source.
   Without Git, use available public tag/commit evidence and an archive or selected fixed-source files through ordinary authorized reads and copying, without Git initialization or a required local clone.
   For Git retrieval, acquire only the history and tags useful for that comparison; a shallow checkout does not establish availability of older contents.
   Unavailable necessary source or migration facts remain explicit limitations, without marking the target installed.
2. Read the applicable notes between installed and target versions, combine their affected paths and inspect the local files and necessary direct consumers.
   The upgrade includes synchronizing the selected official target's user manuals, human request guides and instruction examples in all actually affected existing languages, including body changes rather than only version literals and links.
   Where there is no local adaptation, use the target's actual content without rewriting unchanged parts, inventing missing translations or executing installed examples.
   When using earlier notes, apply the selected target's common contract to ordinary human-document handling and carry forward the concrete adaptations required by each original transition.
   Use final target files directly, ordering intermediate adaptations only when their actual dependencies require it, without serial complete installations of skipped versions.
   Retrieve older tagged sources when needed to understand local changes or incomplete guidance, without assuming that installed local contents still equal the old official source.
   Resolve or report an unavailable necessary baseline or migration fact as a concrete gap, without assuming no adaptation or defaulting to a whole-library comparison.
3. Before writes, preserve unrelated work and a recoverable baseline of affected contents using ordinary recovery copies when Git is absent, or native Git and necessary temporary preservation when applicable, without requiring a clean worktree, automatic stash or preliminary commit.
   Select replacements and bounded merges from the actual affected files and their local responsibilities; a common file path alone does not authorize overwriting its locally maintained content.
   Read actual local document content and necessary entrances, preserving local additions, purposes and choices while merging applicable official changes.
   Protect committed adaptations, including files in a clean worktree, alongside staged and uncommitted edits; tracked status or comparison with local HEAD does not establish equality with earlier official contents.
   Use earlier official contents, the selected target and actual local text as needed through native Git or ordinary comparison, without deciding replacement from filenames, directory placement, version numbers or timestamps.
   An unavailable earlier baseline alone does not prevent adequate judgment from available facts; if a concrete missing fact or decisive intent conflict prevents a necessary merge, preserve that content, report the gap and finish independent authorized work without claiming a complete upgrade.
   Local adaptation does not freeze the whole file or require keeping obsolete framework usage; make necessary bounded command, path, rule-reference and explanation updates within upgrade authority while preserving the local purpose and choices.
   Preserve the actual named or unnamed configuration, human identities, allocation bounds, profiles, bibliography, source holdings, mathematics, manuscripts and effective Task/E conditions, without initializing empty state over them.
   Inspect mixed README, AGENTS, ignore and License contents before merging; retire a framework file only after judging its local role and necessary consumers, preserving authorship, original-source facts and actual decisions/review scope under existing rules.
   Read each affected publication page and its necessary entrances to determine whether it remains an example, presents local results or contains mixed content; filename, directory and upstream distribution role do not determine replacement.
   Preserve user-authored results, attribution, publication links and chosen page entrances, even when the page remains at `user-manual/publication-example.md`.
   Apply only necessary bounded framework adaptations within existing authority, retaining local content and entrance intent rather than restoring upstream example prose or resetting a publication entrance to an example.
   Unchanged examples retain their actual purpose and authorized maintenance scope; this does not freeze the entire `user-manual/` directory.
   Direct overwrites used when copying framework files into the blank official source do not govern ordinary research-repository upgrades.
   Synchronizing and merging already published official document bodies is ordinary upgrade maintenance and needs no additional routine body-editing approval.
   Framework-development limits on designing, authoring, translating or auditing those bodies do not restrict this installation work to mechanical edits.
   Independent human-document authoring, substantial rewriting beyond necessary synchronization and adaptation, and new translations follow their actual separate assignment.
4. Complete adaptation and checks at the affected scope before marking the target installed version or reporting success, and verify the final version metadata, files and required migrations agree.
   On failure restore this operation's affected changes while preserving foreign work; incomplete restoration requires a truthful state and remaining-limit report rather than a completed-upgrade claim.
   Preserve any still-needed recovery content before cleanup or handoff; a handoff cannot depend on recovery files held only in `.tmp/`.
   Reread newly applicable rules before affected work continues, preserving current assignment, stopped conditions and allowances; upgrading selects or resumes no research.
5. With an applicable project remote, deliver the verified upgrade and necessary adaptations through the [common Git delivery default](rules/identity.md#submission-checks) and [delivery action](agent-actions.md#commit-or-push-requested-work), then confirm the actual remote result.
   This applies both to an upgrade before starting the original task and to a separately assigned upgrade in a single-author or collaborative repository.
   Reuse existing identity, serial index, outgoing-scope, integration and delivery checks, limiting the batch to this upgrade and its necessary adaptations while preserving unrelated work and staged contents.
   Honor explicit local-only, offline, no-push or postponed-synchronization instructions.
   Without Git or an applicable project remote, complete the authorized local upgrade without creating either for delivery.
   On a connection, permission or integration failure, report local installation, any saved commit and unfinished push distinctly under the existing failure rules, continuing independently supported authorized work without claiming remote success.
   Upgrade delivery neither resumes research nor supplies unrelated publication authority.

After applicable delivery, report actual from/to versions, target commit, necessary adaptations, checks, actual Git delivery result and remaining limitations to the human author, then clean owned temporary work after its use and necessary diagnostics.

Apply the existing connection, [content-retention](rules/records.md#substantive-material-retention), review, [current-rule reading](rules/workflow.md#proportionate-execution) and [temporary-cleanup](rules/organization.md#temporary-storage) duties at their actual scope.
Ordinary agent reading, retrieval and prepared file operations suffice; this procedure requires no dedicated skill, mandatory installer, automatic semantic merger or generic migration engine.
An authorized personal-folder upgrade works without a Git executable, never initializes Git and updates the installed version only after required adaptation and checks succeed.

<a id="official-version-check"></a>
## Official version check and upgrade choice

The common [version module](../scripts/acme/framework/version.py) owns the official repository address, published ref and version-metadata URL.
The official source is the ACME starting repository; its published main-branch framework/version.json supplies public release-version metadata.
Neither GitHub Releases, a research repository's origin nor development materials are required.
Validate the one-field metadata and existing three-integer release format, then compare integer tuples with the installed framework_version.
The official repository and fixed selected revision establish the retrieval source; version metadata supplies no authorship, source applicability or review verdict.
The retired metadata address has no automatic fallback; an older checker may report unavailable until explicitly upgraded.
Equal or older public versions cause no reminder or downgrade.
The [current-rule reading duty](rules/workflow.md#proportionate-execution) applies independently of whether the public-version query runs or succeeds; an available official version does not replace the installed governing text.

At the [start of a work round](agent-actions.md#start-a-work-round), read the repository's framework_update_check setting and current local daily cache.
The absent setting defaults to true; only Boolean false disables the check, and an invalid configured value is reported without interpreting it as permission.
An explicit offline instruction also prevents the request.
Use one bounded metadata request on a new UTC day; a same-day success, unavailable result or interrupted attempt is reused without an automatic retry.
An explicit human recheck or the permission-granted recheck below may retry that day.
Subagents reuse the responsible main agent's daily result.
The bounded public HTTPS read needs no GitHub CLI authentication, Git remote or optional local skill; the agent applies actual network permissions and the [connection responsibilities](rules/identity.md#git-and-github-connection-checks).

If execution permissions deny an enabled, non-offline official metadata read, request the minimum network permission needed for that read through the host's normal permission mechanism.
After permission is granted, explicitly recheck once, using the existing `--force` if today's cached `unavailable` result would suppress that request.
If permission is not granted or the recheck fails, report the actual limitation and continue independent authorized work without inferring that no update exists.
Other same-day calls retain the reuse rule, and offline or disabled settings continue to prevent a request.
The agent handles permissions; reuse the checker's existing bounded request, cache and concurrency mechanism without script self-elevation or new cache fields.

The ignored repository/framework-update-check.json is a replaceable four-field cache:
last_attempt_on is the UTC date bucket, result is success or unavailable, latest_version is the version verified by that attempt or null, and notified_version is the last version actually presented to the human or null.
It is neither identity nor an installed-version authority, acquisition record, approval or research history.
A missing or malformed cache is unchecked.
Begin the attempt by safely recording today's unavailable placeholder, release the short write lock before the network request, then publish its actual result while preserving an intervening notification.
The latest started fresh request owns publication through one disposable opaque claim under root .tmp, prepared with the placeholder under the same short lock.
Same-day reuse makes no request and takes no ownership.
Before claiming, reread the cache under that first lock and preserve a valid later UTC-day bucket, even for a forced call with an older captured clock.
The production clock is refreshed inside the claim lock; a preclaim refusal returns superseded with attempted false and cache_saved false without a request, placeholder or owner write or another owner's cleanup.
A later fresh request supersedes an earlier one even when the later result is unavailable and its four cache fields equal the earlier placeholder.
Publication checks the current owner and UTC-day cache under that lock; an older caller returns superseded with cache_saved false and preserves the later result and notification.
An already claimed caller reports attempted true when superseded at publication.
Only the matching owner releases its claim on completion; a later eligible attempt may replace an abandoned claim.
The claim coordinates processes and is cleaned under the creator-owned temporary-storage rule, without adding cache fields or retaining request history.
An interrupted attempt remains unavailable; a cache-write failure is reported without pretending the fact was saved.
No background process or scheduler is installed.

When a verified public version is newer and has not already been presented, give the human the installed and available versions and the official repository link, and ask whether to arrange an upgrade while continuing the current assignment.
Only after actually presenting that reminder record its notified_version; a query's reminder_due result does not itself establish notification.
The agent establishes the actual presentation and its order relative to known facts, rather than inferring order from command arrival, numeric version magnitude or query completion.
The optional notification helper requires an explicit expected_notified_version taken from a valid observed cache or its captured query result; an actually observed null differs from omitted input or an invalid cache.
Under the existing short lock, reread the valid cache and compare only notified_version with that premise, preserving independent changes to the attempt date, result and latest verified version.
If the premise is stale, return superseded with cache_saved false and the current notified_version without writing; missing valid cache or malformed input is refused.
Do not automatically retry a stale write, take a numeric maximum or repeat a reminder merely to obtain a saved marker.
Field equality alone establishes no presentation order; the agent preserves the known current fact and reports any unsaved or uncertain fact while continuing authorized work.
A genuinely later presentation of a lower version may be recorded with the explicit current premise, subject to the existing requirement that the presented version be newer than installed.
Adequate ordinary bounded cache maintenance remains available under the same actual-fact and concurrency responsibilities, without a compulsory helper sequence or another approval.
Retain the four fields without notification timestamps, counters, ownership claims, history, receipts or services; the query's existing ownership and UTC-day protections remain separate and unchanged.
Refreshes and failures preserve the actual notification fact.
An unanswered reminder, deferral or successful query grants no upgrade permission.

An explicitly authorized upgrade follows the [installed-framework procedure](#upgrading-an-installed-framework) for its selected official version, affected local framework/configuration and actual material-migration scope.
Apply the [current-rule reading duty](rules/workflow.md#proportionate-execution) before affected work resumes, preserving actual assignment authority and Task/E stopped conditions.
First framework installation and upgrading an existing research project retain their separate setup and preservation responsibilities under the installation and upgrade actions.
Metadata-query failure leaves the public version unconfirmed and does not block unrelated authorized work.
