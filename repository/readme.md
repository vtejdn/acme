# Repository identity

`config.json` retains this repository's name and settings; `people.json` registers local humans by readable names.
The operator is bound in Git worktree configuration.
See the [identity rules](../framework/rules/identity.md).
Acquisition metadata belongs in `intake/<initiator>/`, with original mathematics in its typed home.

The external repositories.json and intake-people.json tables register only actually used repoN/authorN and maintain their two-way associations.
No self-repository number is allocated; external numbers are interpreted only in this local database.
An external person's explicitly adopted local_human correspondence can establish that an external author and a registered local operator are the same human; matching names alone cannot.
Own [personal import](../framework/rules/intake.md#personal-import) uses ordinary local identities and creates no external registration or intake operation for that human's own content.

## Official framework version reminders

The repository Boolean framework_update_check controls the [daily official version check](../framework/versioning.md#official-version-check).
It is enabled when absent; explicit false disables it, while any other non-Boolean value is a configuration problem.
New installations initialize it to true independently of the source repository's choice.

The ignored framework-update-check.json stores only the current UTC attempt date, success/unavailable result, verified latest version or null, and last version actually presented or null.
It is disposable local state, separate from repository identity, installed version and upgrade permission.
Clearing it makes the next enabled work start unchecked; an explicit recheck can refresh the current day.
The agent reports unconfirmed queries and continues the current assignment; replacement framework files still require explicit authorization.
