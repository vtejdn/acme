# ACME Framework Versions

The name is Autonomous and Collaborative Mathematical Exploration (ACME), with fixed framework_id: acme and framework_name: Autonomous and Collaborative Mathematical Exploration in the export manifest.
Repository names and research IDs remain independent.

The sole current framework release identifier is `framework_version` in the [export manifest](export-manifest.json).
Use three nonnegative decimal integers, `MAJOR.MINOR.PATCH`, without leading zeros, a date prefix or a leading `v`.

## Scope and Compatibility

The version covers portable rules, templates, tools and the export contract as one framework.
Compatibility alone does not justify retaining non-substantive content, including administrative and authorization history; apply the [core principles](readme.md#core-principles-and-interpretation) and [content-retention rule](rules/records.md#substantive-material-retention).

During development before 1.0.0, MAJOR remains zero; incompatible changes increment MINOR and other framework changes increment PATCH.

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
Current cross-repository intake requires both installations to support the material-owned format and its exact original-source/acquisition boundaries.

<a id="official-version-check"></a>
## Official version check and upgrade choice

The common [version module](../scripts/acme/framework/version.py) owns the official repository address, published ref and manifest URL.
The official source is the clean exported ACME framework; only its published main-branch export manifest supplies public release-version metadata.
Neither GitHub Releases, a research repository's origin nor development materials are required.
Validate the exact framework_id acme and the existing three-integer release format, then compare integer tuples with the installed manifest's framework_version.
Equal or older public versions cause no reminder or downgrade.
The [current-rule reading duty](rules/workflow.md#proportionate-execution) applies independently of whether the public-version query runs or succeeds; an available official version does not replace the installed governing text.

At the [start of a work round](agent-actions.md#start-a-work-round), read the repository's framework_update_check setting and current local daily cache.
The absent setting defaults to true; only Boolean false disables the check, and an invalid configured value is reported without interpreting it as permission.
An explicit offline instruction also prevents the request.
Use one bounded metadata request on a new UTC day; a same-day success, unavailable result or interrupted attempt is reused without an automatic retry.
An explicit human recheck may retry that day.
Subagents reuse the responsible main agent's daily result.
The bounded public HTTPS read needs no GitHub CLI authentication, Git remote or optional local skill; the agent applies actual network permissions and the [connection responsibilities](rules/identity.md#git-and-github-connection-checks).

The ignored repository/framework-update-check.json is a replaceable four-field cache:
last_attempt_on is the UTC date bucket, result is success or unavailable, latest_version is the version verified by that attempt or null, and notified_version is the last version actually presented to the human or null.
It is neither identity nor an installed-version authority, acquisition record, approval or research history.
A missing or malformed cache is unchecked.
Begin the attempt by safely recording today's unavailable placeholder, release the short write lock before the network request, then publish its actual result while preserving an intervening notification.
The latest started fresh request owns publication through one disposable opaque claim under root .tmp, prepared with the placeholder under the same short lock.
Same-day reuse makes no request and takes no ownership.
A later fresh request supersedes an earlier one even when the later result is unavailable and its four cache fields equal the earlier placeholder.
Publication checks the current owner and UTC-day cache under that lock; an older caller returns superseded with cache_saved false and preserves the later result and notification.
Only the matching owner releases its claim on completion; a later eligible attempt may replace an abandoned claim.
The claim coordinates processes and is cleaned under the creator-owned temporary-storage rule, without adding cache fields or retaining request history.
An interrupted attempt remains unavailable; a cache-write failure is reported without pretending the fact was saved.
No background process or scheduler is installed.

When a verified public version is newer and has not already been presented, give the human the installed and available versions and the official repository link, and ask whether to arrange an upgrade while continuing the current assignment.
Only after actually presenting that reminder record its notified_version; a query's reminder_due result does not itself establish notification.
Refreshes and failures preserve the actual notification fact.
An unanswered reminder, deferral or successful query grants no upgrade permission.

An explicitly authorized upgrade separately identifies its selected official version, affected local framework/configuration and actual material-migration scope.
Apply the [current-rule reading duty](rules/workflow.md#proportionate-execution) before affected work resumes, preserving actual assignment authority and Task/E stopped conditions.
Clean export initializes a blank repository and is not an overlay or upgrade of an existing research project.
Metadata-query failure leaves the public version unconfirmed and does not block unrelated authorized work.
