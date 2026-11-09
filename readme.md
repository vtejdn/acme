# ACME: Autonomous and Collaborative Mathematical Exploration

This mathematical research repository uses the framework [ACME](https://github.com/vtejdn/acme), Autonomous and Collaborative Mathematical Exploration.
ACME supports autonomous mathematical exploration carried out by AI agents and collaboration among human mathematicians.

## To human authors

The [user manual](user-manual/user-manual.md) ([用户手册](user-manual/用户手册.md), [Manuel d’utilisation](<user-manual/Manuel d’utilisation.md>), [Benutzerhandbuch](user-manual/Benutzerhandbuch.md), [ユーザーマニュアル](user-manual/ユーザーマニュアル.md) or [Manual de usuario](<user-manual/Manual de usuario.md>)) is all you need.

## To agents

Start with the current human request and the scope it authorizes.
Use the reading guidance in [AGENTS.md](AGENTS.md) and choose the matching action in the [agent action guide](framework/agent-actions.md).
Read the rules that govern the chosen action and the materials needed for it.
Follow the [work-start action](framework/agent-actions.md#start-a-work-round), including the applicable project remote update and daily official version check.
The [current-rule reading duty](framework/rules/workflow.md#proportionate-execution) applies even when the public query is skipped or unavailable.

For a requested first installation, use the [installation action](framework/agent-actions.md#install-the-framework).
Confirm that the local project root and any target project remote are empty apart from Git setup before obtaining the installation files or writing to the target.
If either already contains project work, preserve it, stop the installation, and report it to the human author.
For an authorized upgrade, use the [upgrade action](framework/agent-actions.md#upgrade-installed-framework) at the existing project root, where the first-installation empty-target condition does not apply.
A newer-version reminder leaves upgrade authorization with the human.

## Reference

The [mathematical materials](mathematics/readme.md) and [manuscripts](mathematics/manuscripts/index.md) provide starting points for reading.
Follow indexes to the materials themselves for the actual statements, arguments, status, selected decisions, and review scope.
Distinguish conjectures, computational observations, self-reviewed proofs, and independently reviewed results.

The [framework rules](framework/readme.md) explain how to carry out each activity.
The [material format](framework/material-format.md) defines declarations and inputs for acquiring material.
The [script documentation](scripts/readme.md) describes optional tools and their effects.
The installed framework version is recorded in [framework/version.json](framework/version.json).

Use [personal import](framework/rules/intake.md#personal-import) to transfer your own selected material and [external intake](framework/rules/intake.md#scope-and-routing) to receive other authors' selected mathematical material from a different research repository.
