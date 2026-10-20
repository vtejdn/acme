# ACME Framework Versions

The name is Autonomous and Collaborative Mathematical Exploration (ACME), with fixed framework_id: acme and framework_name: Autonomous and Collaborative Mathematical Exploration in the export manifest.
Repository names and research IDs remain independent.

The sole current framework release identifier is `framework_version` in the [export manifest](export-manifest.json).
Use three nonnegative decimal integers, `MAJOR.MINOR.PATCH`, without leading zeros, a date prefix or a leading `v`.

## Scope and Compatibility

The version covers portable rules, templates, tools and the export contract as one framework.

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
