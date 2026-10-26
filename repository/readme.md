# Repository identity

`config.json` retains this repository's optional personal name and settings; `people.json` registers local humans by readable names.
Without Git, one explicitly registered human can work locally with an absent or null repository name, without uploading local research content.
Git-managed research writing and delivery require the human-chosen registered repository name and an explicit operator binding in Git worktree configuration; unavailable Git does not change that requirement.
An unnamed personal configuration uses repository: null when prepared explicitly; enabling Git preserves materials and permits reading and necessary setup repair before those prerequisites are complete.
An existing named project clone preserves its identity, while a new project from the official blank source selects its own name instead of silently adopting acme.
Actual name registration or a human-chosen update maintains necessary current displays without renaming human/material identities or historical source facts.
For a selected GitHub project remote with a different name, the agent may suggest a non-blocking local-name update under the [name rule](../framework/rules/identity.md#repository-names-and-use-environments); a source or upstream name alone supplies no project rename.
See the [identity rules](../framework/rules/identity.md).
Acquisition metadata belongs in `intake/<initiator>/`, with original mathematics in its typed home.

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
