# Repository identity

`config.json` retains this repository's optional repository key, separate project display name and abbreviation, and settings; `people.json` registers local humans by readable names, without registrar history.
Without Git, one explicitly registered human can work locally with an absent or null repository name, without uploading local research content.
Git-managed research writing and delivery require the human-chosen registered repository name and an explicit operator binding in Git worktree configuration; unavailable Git does not change that requirement.
An unnamed personal configuration uses repository: null when prepared explicitly; enabling Git preserves materials and permits reading and necessary setup repair before those prerequisites are complete.
An existing named project clone preserves its identity, while a new project from the official blank source selects its own name instead of silently adopting acme.
For an actual new project downloaded or cloned from the official blank source, first set repository, repository_display_name and repository_abbr to the human's actual choices or null, then complete the existing human registration, scoped License notice and necessary checkout binding.
A Git clone with an unchosen repository key remains preparation for research writing, even if the inherited key is syntactically valid; an explicitly chosen acme key remains permitted.
Source inspection, backups, framework maintenance, existing shared-project clones and upgrades retain their actual identities and are not reset by this fresh-project sequence.
Actual repository-key registration or a human-chosen update preserves the independently chosen display settings, human/material identities and historical source facts.
repository_display_name and repository_abbr hold nonempty single-line human choices, including spaces or Unicode, or null when unknown; they are separate from the repository key and each human's display_name.
When both are known, the agent maintains the root readme.md heading as `# <repository_abbr>: <repository_display_name>` by ordinary bounded editing with faithful Markdown escaping, preserving the remaining contents and the ACME framework name.
Missing choices retain null and the existing heading without blocking independent authorized work; a new project does not adopt the official source's display choices, while a shared-project clone preserves its own.
Report missing title choices as incomplete display setup rather than treating the template heading as a human choice.
Project remote targets come from native Git configuration and the actual selected operation, without a repository_url mirror in config.json.
For a selected GitHub project remote with a different name, the agent may suggest a non-blocking local-name update under the [name rule](../framework/rules/identity.md#repository-names-and-use-environments); a source or upstream name alone supplies no project rename.
See the [identity rules](../framework/rules/identity.md).
Acquisition metadata belongs in `intake/<initiator>/`, with original mathematics in its typed home.

The human id is the author-selected path key; that person's display_name is the independently chosen License name, distinct from project display settings and the Git signature.
Registration stores actual Git/account mappings, and identity-bind confirms the current checkout operator; neither configures the effective Git commit name or email.
When a commit is needed, check that signature against the contributor's mapping and limit necessary settings to the selected checkout.
Inspect actual configuration, human registration, full upstream LICENSE and any missing project contribution notice, README and necessary binding; report completed and missing setup without a new receipt or status field.

The external repositories.json and intake-people.json tables register only actually used repoN/authorN and maintain their two-way associations.
No self-repository number is allocated; external numbers are interpreted only in this local database.
An external person's explicitly adopted local_human correspondence can establish that an external author and a registered local operator are the same human; matching names alone cannot.
Own [personal import](../framework/rules/intake.md#personal-import) uses ordinary local identities and creates no external registration or intake operation for that human's own content.

## Official framework version reminders

The repository Boolean framework_update_check controls the [daily official version check](../framework/versioning.md#official-version-check).
It is enabled when absent; explicit false disables it, while any other non-Boolean value is a configuration problem.
The official blank starting configuration sets it to true; cloning an existing shared repository preserves that repository's actual choice.

The ignored framework-update-check.json stores only the current UTC attempt date, success/unavailable result, verified latest version or null, and last version actually presented or null.
It is disposable local state, separate from repository identity, installed version and upgrade permission.
Clearing it makes the next enabled work start unchecked; an explicit recheck can refresh the current day.
The agent reports unconfirmed queries and continues the current assignment; replacement framework files still require explicit authorization.
