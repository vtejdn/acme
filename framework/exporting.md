# Clean ACME Framework Export

Clean export bootstraps a blank research repository from the explicit [manifest](export-manifest.json).
It is offline and performs no fetch, commit or push.
It is not an upgrade or overlay of a research project.

```powershell
python scripts/export-framework.py ../new-research --repository New-Research --repository-name "New Research" --repository-abbreviation "NR"
python scripts/export-framework.py ../new-research --repository New-Research --repository-name "New Research" --repository-abbreviation "NR" --dry-run
```

The `--repository` value is the fresh identity key stored in `repository/config.json`.
The `--repository-name` and `--repository-abbreviation` values are independent reader-facing display values for the exported root README.
Both display values are required, must be nonempty single-line text, and preserve their supplied spelling, spaces and Unicode.
Neither display value is derived from the identity key, validated with the repository-key grammar, or stored as repository configuration.
The exported root README title is rendered as `# {{REPOSITORY_ABBREVIATION}}: {{REPOSITORY_NAME}}` from the maintained template.

The parent must exist.
The destination may be new, an empty directory, or a blank Git checkout (including a linked worktree).
An existing target contains no non-Git content, has an empty index and an empty HEAD tree if HEAD exists, and has no unfinished merge/rebase operation.
An empty-tree commit is allowed.
The exact target checkout is checked; an unrelated empty subdirectory is not its parent repository.

Existing Git metadata, refs, index, remotes and unrelated configuration remain intact.
The exporter never installs staging Git metadata into an existing Git target or initializes it again.
Without `--author`, an existing research binding is a conflict.
With explicit `--author HUMAN`, only the selected human and necessary target binding/worktree configuration are initialized through the ordinary identity tool, with its main-worktree safeguards.
The target's administration scope is used, never staging's scope.

Without `--author`, no source actor or human registry is read.
The output has `people: []` and no actor binding.
Register and then explicitly bind the actual human before authoring:

```powershell
python scripts/research.py identity-add HUMAN --display-name "Human Name"
python scripts/research.py identity-bind HUMAN
```

The first declaration in an empty, unbound registry is self-registration: `registered_by` is that declared key.
It is not authentication and does not bind automatically.
Later registrations require the actual bound registrar.
Explicit `--author HUMAN` deliberately registers and binds only that key.
No source signatures, profiles, personal choices or research/execution authority are inherited.

The exporter captures allowlisted source bytes, checks only its actual portable output files/links, privacy boundaries, manifest facts and installed entrances in owned staging, rechecks target eligibility immediately before installation, and creates files exclusively.
It does not invoke a research-record audit or inspect live mathematics/holdings.
Failure removes only this operation's installed files and restores its binding/configuration changes, preserving foreign files and pre-existing metadata.
Incomplete cleanup is reported.
Dry-run applies the same read-only eligibility checks and reports the target class without staging or writing.
New non-Git outputs receive Git initialization once.

The manifest alone owns the current framework version.
No export receipt, source-commit snapshot or copied-file registry is persisted.
The export contains common framework files and empty research structures, without actual research, source artifacts, intake/execution facts or personal profiles.
The general manual in [English](../user-manual/user-manual.md), [Chinese](../user-manual/用户手册.md), [German](../user-manual/Benutzerhandbuch.md), [French](<../user-manual/Manuel d’utilisation.md>) and [Japanese](../user-manual/ユーザーマニュアル.md) introduces ACME, environment, installation and ordinary use.
The human request suggestions in [English](../user-manual/user-instructions/user-instructions.md), [Chinese](../user-manual/user-instructions/用户指令.md), [German](../user-manual/user-instructions/Anweisungsbeispiele.md), [French](<../user-manual/user-instructions/Exemples de consignes.md>) and [Japanese](../user-manual/user-instructions/指示例.md) explain example requests and expected outcomes.
[AGENTS.md](../AGENTS.md) remains the short bootstrap and cross-activity guidance, and the English [agent action guide](agent-actions.md) owns the function-to-action entrance.
The installed [topic rules](readme.md) govern responsibilities and conditions; the [material format](material-format.md) owns exact declarations/acquisition inputs, and [script documentation](../scripts/readme.md) owns optional interfaces and side effects.
All these guides accompany the export and their navigation resolves within the installed output.
The manual's actual collaboration and workflow diagrams accompany it at their explicit manifest paths.
Official non-English human-facing editions may be maintained in any language alongside their responsible originals, explaining the same framework without a competing rule authority.
Generic entrances, empty collections, common tools, templates and guides remain self-exportable.
The repository identity is fresh; the source's Git history and remotes are never copied.

The [version policy](versioning.md#scope-and-compatibility) governs actual compatibility.
Separately authorized framework maintenance names the recipient, selected framework source and actual scope of retrieval and changes.
Clean export does not implement retrieval or relax collision checks to simulate an upgrade.
