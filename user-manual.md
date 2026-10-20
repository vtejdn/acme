# User Manual

[Request examples](user-manual/user-instructions/user-instructions.md) · [About](about.md)

## ACME: Autonomous and Collaborative Mathematics Exploration

ACME is a light-weight framework consits of a set of core Markdown files on rules with 辅助 scripts.
The main features are two: supporting autonomous AI agents to carry mathematical research under the guidance of human mathematicians and supporting collaboration between human authors.

### Mathematicains
A human mathematian 负责
1. set the exploration tasks and authorized scope
2. provide guidence for developing strategies together with agent
3. During the exploration, clarify mathematical intent and decide scientific priorities, contribute ideas, challenge arguments, refine questions and redirect the investigation, including decisions about which results to develop and how to present them.


### Agent
Autonomous agents 负责
1. Within authorized scope, study and verify literature
2. develop strategies, routine methodological decisions can proceed autonomously within the assignment.
3. construct proofs and counterexamples, run reproducible computations, call subagent to review arguments independently, identify gaps and retain assumptions, dependencies, useful unsuccessful approaches and unresolved questions.
4. preserves arguments, evidence and unresolved questions, exploration history in the designed places
4. prepare manuscripts.



It 





Research connects question formulation, literature verification, strategy development, proof and computation, review and manuscript preparation, with feedback between these stages.
Linked mathematical statements and supporting evidence let work continue across agents and sessions.
The framework distinguishes conjectures, computational observations, proof drafts and reviewed results, keeping each conclusion's support and limitations visible.
See [About](about.md) and [AI disclosure](ai-disclosure-for-human-authors.md).

This manual introduces the environment, setup and ordinary use.
[Request examples](user-manual/user-instructions/user-instructions.md) help you describe useful work and understand the result to expect.
The [export manifest](framework/export-manifest.json) identifies the installed framework version.

## Recommended working environment

Use an agent environment that can read and edit repository files, run a terminal and inspect Git state under your actual authorization.
A UTF-8 text editor with Markdown support makes statements, links and decisions easy to inspect.
Work directly in the shared research repository and its existing checkout under the [collaboration rule](framework/rules/identity.md#collaboration-maintenance-and-conflicts).
Additional parallel research copies are not recommended; the framework defines no management workflow for them.

Git and Python 3.12 or later are needed for the supplied command interfaces and clean export.
The common runtime uses Python's standard library; an isolated Python environment is a convenience, not an additional framework service.
Run examples from the repository root using the available interpreter.
A particular computation may require libraries documented in its own reproduction instructions.
LaTeX is needed when building a TeX manuscript, and Lean is needed only for work that actually includes Lean code or formalization.
Source retrieval needs access to the selected resources; private setup remains in the responsible human's ignored local configuration under the [private-setup rule](framework/rules/organization.md#machine-local-locators).
No particular operating system, agent product, machine path or hosted service is a framework requirement.

## Installation and first setup

<a id="choose-your-starting-point"></a>
### Join an existing collaboration

Use the existing repository and read its [mathematical entrance](mathematics/readme.md), relevant Task and actual materials.
Register the actual human if needed and explicitly bind the actual current operator before authoring; do not reinitialize a populated research repository.
The shared human registry records identities, while the checkout binding supplies current operator attribution for its chats.
Binding does not change a material's responsible author, another author's policies or the effective Git signature.
Use actual registered Git name/email mappings when delivering work; see [identity](framework/rules/identity.md#stable-keys-and-local-attribution).

### Create an independent blank repository

From a framework source, use the supported [clean exporter](framework/exporting.md):

```powershell
python scripts/export-framework.py ../new-research --repository Demo --dry-run
python scripts/export-framework.py ../new-research --repository Demo
```

Replace the destination and repository key with your actual choice.
Its parent must exist; the destination must be new or an eligible blank target.
Clean export creates a fresh identity and empty research structures and preserves eligible existing Git metadata.
It is not an overlay for a populated repository and copies no research, personal policies, source signatures or execution authorization.
It performs no fetch, commit or push.

Without `--author`, the human registry is empty and the checkout is unbound.
Register the first actual human and then bind explicitly:

```powershell
python scripts/research.py identity-add Alice --display-name "Alice Example"
python scripts/research.py identity-bind Alice
```

Replace the example identity with the responsible human's declared key.
An explicit export `--author Alice` instead registers and binds that one chosen human, with no inherited source signatures or policies.
Configure actual identity mappings and local choices before authoring or submission.
The [script documentation](scripts/readme.md) describes the exact interfaces and side effects.

Ordinary research uses the installed rules.
Research requests, corrections, check failures and preferences do not themselves authorize framework changes, retrieval or version changes.
Separately authorized framework maintenance retains its actual assigned scope.

## Ordinary use

### Give an agent a research assignment

State the mathematical question, domain, hypotheses and quantifiers, desired deliverable and authorized exploration scope.
Explain whether a weaker result would be useful and whether it would resolve your original question.
For sustained autonomous work, specify or adopt execution limits and stopping conditions.
Use the [request examples](user-manual/user-instructions/user-instructions.md#start-or-continue-research) for wording; you need not prescribe internal material operations or a tool sequence.

An actual substantive objective uses a precise Task contract; discussion, literature reading or maintenance alone does not activate one.
A proposed Task, an active mathematical Task and a currently running agent are distinct.
A usage stop does not settle the mathematics, and a new chat or Task revision does not reset allowance or resume a stopped run.
Every local Task family has one current execution boundary, prepared as non-running at setup and retained after completion.
It keeps only its relevant exact Task decision and effective conditions, without a quota diary or session history.
Expect updates about established facts, uncertainty, useful failures and the next discriminating step.
See [Tasks](framework/rules/tasks.md) and [execution](framework/rules/execution.md).

### Follow the mathematical materials

Start from a Task's selected decision and exact contract and follow its actual support, routes and review findings.
For a Claim, inspect the selected statement, argument, dependencies and applicable review rather than inferring a relationship from matching numbers.

| Material | What to read there |
| --- | --- |
| T — Task | Exact question, authorization, completion criteria and lifecycle decisions |
| C — Claim | Precise reusable statement, assessment and selected arguments/evidence |
| S — Strategy | A route, its disposition, priority, Task associations and next step |
| D — Draft | Developing mathematics and unresolved alternatives |
| L — Ledger material | Exploration, synthesis, meaningful failures and eligible scoped self-review or unknown findings |
| R — Review | The mathematical inputs actually reviewed, findings, relationship and limits |
| J — Computation | Native programs, needed data, reproduction context and honest run status |
| U — Source unit | Exact source edition/passages, applicability and actual inspection depth |

Definitions, bibliography and manuscript projects have their own responsible homes.
Not every scratch calculation needs a Claim or a separate review account.
These materials make the actual argument, source and review scope inspectable; indexes help locate them without deciding their status.

### Read status and review evidence

| Mathematical status | Meaning for the reader |
| --- | --- |
| `open` | A precise unresolved statement; an argument need not exist. |
| `proof draft` | An argument is developing, has gaps or awaits required review. |
| `conditional` | The conclusion depends on explicit unresolved inputs or additional conditions. |
| `proved` | A complete argument covers the statement, with resolved dependencies and actual completed internal review. |
| `refuted` | Checked evidence contradicts the exact statement within its stated scope. |

Review status separately records unreviewed, under review, self-reviewed, independently reviewed or changes required.
A complete self-reviewed proof can support progress as `proved`; independent review requires a separately organized reviewer to inspect the relevant reasoning.
Key proof points and the full chain after Task completion require that independent arrangement, with unfinished obligations retained.
Read which inputs, versions and arguments the review covered and what it excluded.
An older or narrower review does not automatically cover a changed proof or contract.
Formal verification, publication and human review are separate facts; see [Claim assessments](framework/rules/claims.md) and [review rules](framework/rules/proof-audits.md).

### Revise and continue work

Describe the intended change and identify the actual result or document.
Say whether the question, hypotheses or conclusion should change, or whether you want clearer wording with the same mathematics.
Expect the response to explain the effect on the result, preserve useful earlier findings and identify remaining limitations.
Strategies can adapt to findings and resources unless you explicitly fixed a priority or order; a route change does not enlarge the objective.

For continuation, name the Task or actual document and any changed scope or limits.
For round closeout, expect retained results, remaining obligations and a usable next step.
Closing a round is distinct from satisfying the Task's original criteria; pausing execution is distinct from mathematical completion.
See [continuation and closeout requests](user-manual/user-instructions/user-instructions.md#close-a-round-or-stop-work).

### Collaborate and acquire external work

Local collaborators retain readable registered names; external sources receive local repository and author numbers with explicit source correspondence.
Equal names or addresses alone do not establish identity, and onward transfer uses the receiving repository's own numbers.
The agent prepares the chosen receiving family placement and original-source facts; a real unresolved identity collision needs your ruling.

Registered collaborators work directly in the shared repository, with actual human attribution and authorized substantive work in each responsible author's materials.
Agents may directly repair routine administrative locations, including same-object links and navigation in another author's material, under the [collaboration boundary](framework/rules/identity.md#collaboration-maintenance-and-conflicts).
Preserve the actual mathematics, inputs, source identity and review meaning; routine maintenance does not transfer authorship or take over another human's Task/E.

Administrative conflicts follow the applicable framework rule; an unclear rule is reported with the concrete competing content for human ruling.
A substantive mathematical conflict needs human approval for its identified scoped recheck before that recheck, with existing explicit approval for the same scope reused.
Approval to recheck alone does not authorize substantive editing of another author's material.
Ordinary authorized research and routine maintenance have no blanket new approval requirement.

Reuse from a distinct research repository preserves the actual original attribution and review limits; another author in this shared repository is direct collaboration.
Name the finding you want to reuse and its intended purpose.
Expect a clear account of the acquired scope, any unavailable inputs and what remains unchecked.
Copying a document does not endorse all its findings or grant its research authority.

### Use literature, computations and manuscripts

Ask for the needed work, edition, passages and inspection depth.
Bibliography identifies the publication, source records describe what was actually inspected, and the result should state its applicability and limitations.
Acquisition, availability, source inspection and source-proof review are separate outcomes.
A successful copy or matching hash does not establish work identity, completeness or a theorem.
For a source with a contents list, use its [searchable contents](mathematics/literature/contents/readme.md) to locate the right chapter or section, then read the actual passage.
A contents hit is a locator, and no hit does not establish absence of a result.
Ask about actual coverage and readability when the source is part of a collection, a partial scan or original HTML.
Source audits exclude associated Lean code unless you explicitly include it.

The local PDF, original HTML and resource store is excluded from Git/GitHub and is not copied between repositories.
Reusing a source unit preserves its recorded reading scope without claiming a local copy of the source; obtain original text independently when needed.

For computations, give the question, inputs, parameters and range you need checked.
Expect the arithmetic mode, actual result and limitations, including failures.
Finite scans and floating-point observations do not prove an unrestricted theorem; exact checks also need a stated scope and mathematical reduction.

For writing, identify the manuscript, responsible author, audience, intended mathematical scope and source or style choices.
Existing author and manuscript choices continue to apply; a different current operator does not change them.
State whether a new preference is for this manuscript or a broader author scope.
For a talk or presentation, retain your explicitly designated document directory and apply the same source, build and review duties without creating a research Task merely for its location.
For direct text reuse, designate your own/coauthored works in your author-wide writing choices, or designate sources and exceptions for a particular manuscript.
A style-only reference grants no text reuse permission; attribution and suitability for the present mathematics remain necessary.
See [text reuse](framework/rules/writing.md#default-reuse-permission).

Expect actual citation support and a clear statement of mathematical review, compilation and any layout checks performed.
A successful build does not prove the mathematics, and a text edit does not itself complete the research objective.
[Writing requests](user-manual/user-instructions/user-instructions.md#write-or-revise-a-manuscript) illustrate how to specify that scope.

### Everyday commands and publication

Use [request examples](user-manual/user-instructions/user-instructions.md) to describe ordinary work and [script documentation](scripts/readme.md) when you need an exact optional command.
Specify the files or commits you want delivered, the intended destination if needed, and any condition that should be satisfied first.
A commit saves selected work with its truthful status, including unfinished work; a push delivers authorized commits and should report the actual remote result.
A check or review answers the question at its requested scope; Git delivery alone is not a mathematical review.
Plain commit/push does not reopen research review, run framework regressions or inventory the source store.
See [delivery requests](user-manual/user-instructions/user-instructions.md#commit-and-push).

## Common questions

**Must every conjecture have a proof?**
An open Claim may state an unresolved question without an argument.

**Must I approve every intermediate Claim?**
Ordinary exploration and result organization within the assignment can proceed; changed objectives and actual authorization boundaries still govern.

**Can I fix status in the index?**
The actual status belongs to the responsible mathematical material and its evidence; changing the index alone does not change that assessment.

**Does a stopped agent mean the Task is blocked or complete?**
Execution state and mathematical lifecycle are separate; preserve the unresolved question and handoff.

**Must I read every rule before asking?**
Start with your objective and this manual; the agent reads its applicable action and topic rules.
