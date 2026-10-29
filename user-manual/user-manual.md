# User Manual

[Instruction examples](user-instructions/user-instructions.md) · [Example disclosure of AI assistance](ai-disclosure-example.md)

## ACME: Autonomous and Collaborative Mathematical Exploration

ACME is a lightweight framework for autonomous and collaborative mathematical research.
It combines Markdown rules for [AI agents](#notion-agent) with auxiliary scripts to support sustained exploration and preserve research that can be inspected, reused and continued.
It serves two main purposes: enabling autonomous AI agents to conduct mathematical research under the guidance of human mathematicians, and supporting collaboration among human authors.

### Human mathematicians

Human mathematicians are responsible for:

1. Defining research questions, their authorized scope and completion criteria to initiate [Tasks](#material-task).
2. Guiding the development of [Strategies](#material-strategy) together with [agents](#notion-agent).
3. Contributing ideas, clarifying mathematical intent, setting scientific priorities, challenging arguments, refining questions and redirecting investigations.
4. Understanding the research outputs and exploring the frontiers of mathematical knowledge.
5. Taking responsibility for the mathematical results.

### Agents powered by [LLMs](#notion-llm)

Within the authorized scope, autonomous [agents](#notion-agent) are responsible for:

1. Studying literature and verifying the results needed for the investigation.
2. Developing and evaluating research [Strategies](#material-strategy), identifying gaps, and making routine methodological decisions autonomously within the assignment.
3. Exploring open-ended questions and clarifying the scope and limits of emerging results.
4. Seeking proofs and counterexamples for specific questions, and running reproducible computations to obtain observations, evidence and insights.
5. Preserving assumptions, arguments, evidence, dependencies, useful failed approaches, unresolved questions and substantive research history in the appropriate research materials, including [Claims](#material-claim) and [Ledgers](#material-ledger).
6. Arranging independent [Reviews](#material-review) when required, and recording their scope, findings and limitations.
7. Preparing and reviewing manuscripts according to general mathematical writing standards and the responsible author's preferences.

### Collaboration

Mathematicians can [collaborate](#joint-task) through a shared [Git repository](git-repository.md#notion-git-repository), sharing research materials and reusing one another's results.
The repository can be hosted on a platform such as [GitHub](git-repository.md#notion-github), allowing collaborators to work on their own devices and synchronize changes.
See the [Git repository collaboration diagram](git-repo.png).

Different mathematicians or teams can also collaborate across repositories by receiving selected materials through [Intake](#notion-intake); see the [cross-repository collaboration diagram](collaboration.jpg).

### Workflow

Research begins with a human-defined [Task](#material-task) specifying completion criteria.
[Agents](#notion-agent) first consult and reuse relevant local research materials and literature, then search the web for additional sources when needed.
They check the applicability of results, develop [Strategies](#material-strategy), and iterate through proof attempts, computations and counterexample searches.
Each attempt informs the next: useful findings, failures and unresolved questions are retained in the appropriate research materials, including [Claims](#material-claim) and [Ledgers](#material-ledger).
Strategies adapt within the authorized objective.
Candidate results undergo mathematical [Review](#material-review), and Task completion is judged against the original criteria.

See [workflow](workflow.jpg).

## <a id="setup"></a>Setup

For a new research project, follow Steps I–III below. If you are joining an existing collaboration, [set up your workspace](#setup-workplace) and then follow the [collaboration setup steps](#setup-collaboration).

### Step I. Choose capable [LLMs](#notion-llm)

Compare LLM performance on research-level mathematical tasks.
Use [FrontierMath Tier 4](https://epoch.ai/frontiermath/tiers-1-4?tier=Tier+4+%28v2%29&view=graph&tab=leaderboard), [MathArena](https://matharena.ai/models), [Riemann-bench](https://surgehq.ai/benchmarks/riemann-bench) and other relevant evaluations as reference points.
Choose models for mathematical research and administrative tasks, taking into account whether they are open source, their accessibility and their cost.

### <a id="setup-workplace"></a>Step II. Set up your workspace

For individual research on a single device, use a suitable [agent harness](agent-harness.md) with access to a capable [LLM](#notion-llm).

1. Install an agent harness, either as a standalone application or within an [IDE](agent-harness.md#notion-ide), and sign in if required or desired.
2. Choose a folder on your device to store the framework and future research materials.
3. Select the model and provider in the settings or model picker.

Without [Git](git-repository.md#notion-git), the default is personal research on your local device.
To synchronize work across devices or collaborate through a shared [Git repository](git-repository.md#notion-git-repository), you may choose a hosting platform such as [GitHub](git-repository.md#notion-github).
Uploading research records and making a repository public are separate choices.

4. (Optional) Install Git on your device, or ask an [agent](#notion-agent) in your chosen harness to do it for you.
5. (Optional) Create or sign in to a repository hosting account, then connect to an existing repository or create a new one.

- See also [Setup instructions](user-instructions/user-instructions.md#setup).

### Step III. Install and initialize the framework

If you are joining an existing research repository that already contains ACME, follow the steps in the next section instead.

1. Ask an [agent](#notion-agent) to download the [ACME framework](https://github.com/vtejdn/acme) into your project folder, or [clone](#notion-clone) its repository if you are using [Git](git-repository.md#notion-git).
2. Choose a unique author key, such as `Alice` or `Ali`, and independently choose the name to appear in the `LICENSE` attribution.
   Ask an agent to register you as an author and add that attribution.
   In a Git workspace, ask the agent to associate this working copy with your author key so that new records use the correct authorship.
3. (When using Git) Configure the name and email associated with your [commits](#notion-commit), or ask an agent to do so.
4. (When using Git) Choose or confirm a short name for your research [repository](git-repository.md#notion-git-repository) and ask an agent to ensure it is recorded correctly in the framework.
5. (Optional) When appropriate, we strongly recommend sharing your research records through a public repository.

- See also [Setup instructions](user-instructions/user-instructions.md#setup).

### <a id="setup-collaboration"></a>Join an existing [Git repository](git-repository.md#notion-git-repository) as a collaborator

1. Sign in to the repository hosting platform and accept your coauthor's invitation.
2. Ask an [agent](#notion-agent) to help configure access to the shared repository.
3. Give the repository address to an agent and ask it to [clone](#notion-clone) the repository into a new local folder.
   Open that folder in your agent harness.
4. If you are not yet registered in the research repository, choose an author key distinct from those of your collaborators and independently choose the name to appear in the `LICENSE` attribution,
   then ask an agent to register you and add that attribution.
   Ask the agent to associate this working copy with your author key in ACME.
5. Configure the name and email used for your [Git](git-repository.md#notion-git) [commits](#notion-commit), or ask an agent to do so.

- See also [Setup instructions](user-instructions/user-instructions.md#setup).

## Getting started

### Start a [Task](#material-task)

1. (Optional) Provide relevant literature or ask an [agent](#notion-agent) to find it.
   Ask the agent to store source files in [the local literature directory](../mathematics/literature/pdf) and audit the specified portions of relevant articles at the requested depth.
2. Establish a Task through discussion with agents, specifying the questions, constraints and completion criteria.
   You may choose a [research-line letter](#notion-research-line-letter) to organize the Task and its related materials.
3. For sustained autonomous work, specify or adopt execution limits and stopping conditions.
4. Approve necessary tool actions when prompted, and respond to questions raised by agents.
5. Think through and understand the mathematical materials produced by agents (no agent can do this for you).
   Discuss the mathematics with agents to deepen and accelerate your understanding.
   Ask for relevant references and question the sources of arguments and ideas Socratically, especially when an argument relies on model knowledge without explicit source support.
6. (Optional, when using [Git](git-repository.md#notion-git)) [Commit](#notion-commit) changes you want to keep; use undo for local edits or revert commits when appropriate.

- See also [research instruction examples](user-instructions/user-instructions.md#research-instructions).

### <a id="joint-task"></a>Start a joint [Task](#material-task)

Collaborators in the same repository can establish a joint Task for a common mathematical goal, specifying the shared question, hypotheses, scope and completion criteria; each participant advances their research through their own Task.

1. Ask an [agent](#notion-agent) to establish a joint Task; if a collaborator has already established a suitable one, proceed directly to the next step.
2. Ask the agent to establish or reuse your individual Task, link it to the joint Task that you and your collaborators agreed to adopt, and specify your scope of participation and personal completion criteria.
   An individual Task can cover all or part of the common question; its completion criteria can match those of the joint Task or be determined by your scope of participation.
   Participants can also divide work on the same question: one person may attempt a proof while another looks for a counterexample.
   We recommend choosing different research [Strategies](#material-strategy) in consultation with your collaborators to reduce repeated mathematical work and make more effective use of AI computational resources.
   For independent verification, replication or cross-checking, collaborators may also deliberately adopt the same research approach.
3. During joint research, the [main research agent](#notion-main-research-agent) synchronizes collaborators' updates before each round through operations such as [pulls](#notion-pull) and [merges](#notion-merge), and [commits](#notion-commit) and [pushes](#notion-push) shareable research progress at appropriate times.
   The agent handles administrative conflicts within its authority; for substantive mathematical disagreements, it explains the issue and conducts a recheck under existing authorization or after obtaining the necessary authorization.
   You can also explicitly request synchronization operations such as pushes, pulls and merges.

### Cautions

- [Agents](#notion-agent) will try to download publicly available literature to [the local literature directory](../mathematics/literature/pdf).
  This directory is ignored by [Git](git-repository.md#notion-git) by default.
  If you put your own private material there, make sure this directory is ignored by Git and is not uploaded to a public repository.
- If collaborators would otherwise use the same author key, agree on distinct keys, such as `Wang1` and `Wang2`.
- Use different [research-line letters](#notion-research-line-letter) for [Tasks](#material-task) that will be advanced concurrently by separate main research agents.
  Choose the letters during Task setup to separate material numbering and reduce write conflicts.
  Ask the agents to coordinate changes to shared files, including indexes, the bibliography and repository identity records.
  Additional parallel research worktrees are not recommended; the framework defines no management workflow for them.
- ACME guides agents through written rules and supporting tools.
  If an agent departs from your instructions or the framework rules, ask it to explain the discrepancy and correct the affected work.
- The rules of the framework may contain ambiguities, inconsistencies or gaps.
  You can ask an agent to revise the rules in the framework if you consider it appropriate.
  You're also welcome to report it to the [author](https://github.com/vtejdn) of the ACME framework.

### Useful habits

- Ask an [agent](#notion-agent) whenever you have questions about the framework.
- If you keep literature in a local directory synchronized by a cloud service, ask an agent to connect [the local literature directory](../mathematics/literature/pdf) to it through a directory junction.
  Grant the agent the permissions needed to read and manage files in that directory.
- When agents automate related tasks involving credentials, store secrets appropriately and exclude them from [Git](git-repository.md#notion-git).

### Write a manuscript

Under construction.

### Lean formalization

Under construction.

## Useful information

### Framework version

The current framework version is 0.6.0.

When automatic checks are enabled and network access is permitted,
the [agent](#notion-agent) checks the [official ACME framework](https://github.com/vtejdn/acme) for a newer version at the start of work, at most once per UTC day.
If one is available, it tells you the installed and available versions and asks whether to arrange an upgrade; your current work can continue while you decide.
A reminder does not install or upgrade anything, and you may defer it.
You can ask to disable or enable this repository's automatic checks, recheck now, or upgrade explicitly.

### Instruction examples

The [instruction examples](user-instructions/user-instructions.md) illustrate common instructions and explain what results to expect.

### Top-level directories and files

The tables below describe the main files and directories in the repository root.
Some directories are created only when needed.

| Path | Purpose |
| --- | --- |
| `.tmp/` | Holds temporary inputs and byproducts created by [agents](#notion-agent) and removed after use. |
| `execution/` | Records the current execution state, limits and stopping conditions for individual research [Tasks](#material-task). |
| [`framework/`](../framework/readme.md) | Contains framework rules, material templates, format specifications and version guidance. |
| `intake/` | Records which materials were received from other [repositories](git-repository.md#notion-git-repository), their sources and the scope of each acquisition. |
| [`mathematics/`](../mathematics/readme.md) | Holds research materials, literature records, computations, manuscripts and presentations. |
| `profiles/` | Holds personal research policies, execution preferences and mathematical writing choices. |
| [`repository/`](../repository/readme.md) | Stores repository settings, author registrations and mappings to external repositories and authors. |
| [`scripts/`](../scripts/readme.md) | Provides optional command-line tools for setup, material management, navigation and checks. |
| [`user-manual/`](./) | Contains user guides, setup explanations and instruction examples. |
| `.gitattributes` | Configures [Git](git-repository.md#notion-git) handling of text and binary files, including line endings. |
| `.gitignore` | Specifies untracked files and directories that Git should ignore. |
| `AGENTS.md` | Provides entry instructions that direct agents to the applicable framework rules and materials. |
| `LICENSE` | Contains the repository’s license terms and notices. |
| `readme.md` | Introduces the repository and links to the user manual, framework rules and research materials. |

Depending on your tools and setup, you may also see the following directories.

| Path | Purpose |
| --- | --- |
| `.agents/` | Holds repository-local agent skills. |
| `.claude/` | Holds local Claude Code settings for this workspace. |
| `.codex/` | Holds local Codex configuration for this workspace. |
| `.git/` | Holds Git history, references, configuration and other version-control metadata. |
| `.venv/` | Holds the local Python virtual environment and its installed dependencies. |
| `.vscode/` | Holds VS Code workspace configuration and extension recommendations. |

### Categories of research materials

| Abbreviation | Material | Location | Purpose |
| --- | --- | --- | --- |
| T | [Task](#material-task) | [`mathematics/tasks/`](../mathematics/tasks/index.md) | Defines a research question, its authorized scope and completion criteria, and records lifecycle decisions. |
| S | [Strategy](#material-strategy) | [`mathematics/strategies/`](../mathematics/strategies/index.md) | Develops and evaluates a research route, organizes priorities, and identifies obstacles and next steps. |
| C | [Claim](#material-claim) | [`mathematics/claims/`](../mathematics/claims/index.md) | States precise mathematical claims, preserves their arguments and dependencies, and records their mathematical and review assessments. |
| R | [Review](#material-review) | [`mathematics/audits/reviews/`](../mathematics/audits/reviews/readme.md) | Records mathematical reviews of specified project arguments, including the inputs checked, findings, review arrangement and limitations. |
| D | Draft | [`mathematics/drafts/`](../mathematics/drafts/readme.md) | Provides a working space for developing mathematical arguments, calculations and alternatives that are still being explored. |
| L | [Ledger](#material-ledger) | [`mathematics/ledger/`](../mathematics/ledger/readme.md) | Preserves useful exploration, comparisons, syntheses and failed approaches, together with the reasons and outcomes of substantive mathematical changes. |
| J | Computation | [`mathematics/computations/programs/`](../mathematics/computations/readme.md) | Organizes programs and required inputs for reproducible computations, and records run status, results and limitations. |
| U | Literature audit unit | [`mathematics/audits/literature/`](../mathematics/audits/literature/readme.md) | Makes inspected literature reusable by recording the source edition and passages, mathematical content, applicability and inspection limits. |
| — | Manuscript | [`mathematics/manuscripts/`](../mathematics/manuscripts/index.md) | Develops papers and related mathematical documents, with their exposition, citations, writing choices and build records. |
| — | Presentation | [`mathematics/presentations/`](../mathematics/presentations/readme.md) | Develops talks and slides for a specified audience, with presentation sources, writing choices, build information and review records. |

- Each computation has a numbered J directory containing its programs, required inputs and `readme.md`.
  Generated outputs are stored separately under the local, [Git](git-repository.md#notion-git)-ignored path `mathematics/computations/outputs/<J>/`.
- Literature audit units are grouped by citation key under `mathematics/audits/literature/`.
- The [definition index](../mathematics/definitions/index.md) organizes definitions, terminology and symbols by concept, with links to their complete formulations in the responsible C, L or U materials.
- The canonical [bibliography](../mathematics/literature/references.bib) records publication identity and citation keys.
  Source acquisition, artifact versions and availability are recorded separately in the [literature registry](../mathematics/literature/registry.md).

### Basic notions

| Term | Meaning |
| --- | --- |
| <a id="notion-llm"></a>LLM (large language model) | An AI model trained on large amounts of text to process and generate language, including mathematical explanations and computer code. |
| <a id="notion-agent"></a>Agent | An AI system powered by an [LLM](#notion-llm) that can plan and carry out tasks, use tools and adjust its actions based on results. It works through an [agent harness](agent-harness.md) within the scope and limits authorized by the human user. It has not yet evolved into an [Agent](https://en.wikipedia.org/wiki/Agent_%28The_Matrix%29). |
| <a id="notion-context"></a>Context | The information available to an LLM during a model call, including instructions, conversation history, supplied materials and tool results. The current context may contain only a selection or summary of the full [session](#notion-session) history. |
| <a id="notion-context-length"></a>Context length | The maximum combined length of input and output an LLM can handle at once, usually measured in tokens (small units of text). This includes instructions, conversation history, supplied material and the generated response. |
| <a id="notion-session"></a>Session | A continuing interaction with an [agent](#notion-agent), managed by an [agent harness](agent-harness.md). It may contain multiple conversation turns, each typically beginning with a user message and including the agent's responses and tool operations. The harness maintains the conversation history and prepares the [context](#notion-context) for each model call; to stay within the model's [context length](#notion-context-length), it may select or summarize earlier history. |
| Material identifier | A structured reference identifying a material and, where applicable, its version. For example, `Alice_C_F0007_v1.md` identifies a [Claim](#material-claim) by author, kind, research line, serial number and version. |
| <a id="notion-research-line-letter"></a>Research-line letter | A letter, such as `F` in `Alice_C_F0007_v1.md`, used to organize numbered research materials. Task-derived materials inherit the Task's letter but receive their own serial numbers. The default is `A` when no line is specified. |
| Author key | A stable registered key for a human author, such as `Alice`, used in material identifiers and authorship records. |
| Material family | The retained versions of the same material, such as `Alice_C_F0007_v1.md` and `Alice_C_F0007_v2.md`. |
| Material version | A particular retained revision of a material, such as the `v1` or `v2` version of a Claim. |
| <a id="notion-main-research-agent"></a>Main research agent | The agent leading work on a [Task](#material-task), coordinating any other subagents involved and keeping the research records consistent. |
| Task round | A period of work on a Task, ending with a record of progress, unresolved issues and where to continue. |
| <a id="notion-git-branch"></a>Git branch | A named line of development in a [Git repository](git-repository.md#notion-git-repository), allowing changes to be developed separately from other lines of work. |
| <a id="notion-clone"></a>Clone | Copying an existing Git repository to a new local folder, including its files and version history. |
| <a id="notion-commit"></a>Commit | A saved version in local [Git](git-repository.md#notion-git) history, recording selected changes with a message describing them. |
| <a id="notion-push"></a>Push | Sending local commits to a remote Git repository so that the recorded work is available there. |
| <a id="notion-pull"></a>Pull | Retrieving changes from a remote Git repository and incorporating them into your local work. |
| <a id="notion-merge"></a>Merge | Combining changes from another [branch](#notion-git-branch) into your current Git branch, resolving conflicting edits when necessary. |
| <a id="notion-intake"></a>Intake | Bringing selected research materials from another public ACME repository into your own, with their authorship, origin and review limitations preserved. |
| Citation key | A short identifier for a work in the bibliography, used to cite it consistently in research records and manuscripts. |

### <a id="material-task"></a>Task

A Task organizes research around a precise mathematical objective, its authorized scope and agreed completion criteria.

| Task status | Meaning for the reader |
| --- | --- |
| `proposed` | A research question has been put forward but has not yet become an active research objective. |
| `active` | The investigation is authorized and remains ongoing. |
| `paused` | The investigation is deliberately on hold, with an intention and a stated basis for resuming it. |
| `blocked` | A specific missing input or unmet prerequisite prevents the next necessary step. The record explains what is needed for progress to resume. |
| `completed` | The agreed completion criteria have been met, with supporting mathematical evidence and the required review. |
| `retired` | The investigation has been discontinued. Its reasons, useful findings and unfinished parts remain recorded. |

- A Task may remain active while no [agent](#notion-agent) is currently working on it.
- A Task brings together the research materials supporting your investigation.
  Related manuscripts, progress reports and other documents you request can be collected in a project such as `mathematics/manuscripts/Alice_T_A0007/`.
- You may ask to reactivate a completed Task for further work on the relevant research objective.
  Explain what you would like to investigate next and any changes to scope or limits.
  A materially different research objective should be established as a new Task.

### <a id="material-strategy"></a>Strategy

A Strategy describes a concrete route towards a research objective, including its mechanism, remaining obstacles and next useful steps.

| Strategy status | Meaning for the reader |
| --- | --- |
| `proposed` | A possible approach has been identified but has not yet been selected for current investigation. |
| `active` | The route is currently selected for research towards the Task's objective. |
| `paused` | The route is temporarily set aside because of priorities, sequencing or available resources. No mathematical failure is implied. |
| `blocked` | A specific unmet prerequisite prevents the next planned step. The record identifies the obstacle and what would allow the route to continue. |
| `completed` | The route has delivered its stated result or contribution, with the required supporting evidence. Other work may still be needed to complete the Task. |
| `refuted` | Checked mathematical evidence rules out the recorded mechanism or an auxiliary assertion it requires, under the stated hypotheses. |
| `superseded` | The route has been replaced by identified successor Strategies or incorporated into another route. Its history and useful findings remain available. |

- A [Task](#material-task) may have several Strategies, either as alternatives or as parts of a combined approach.
  Completing, pausing or ruling out one Strategy does not by itself determine the status of the whole Task.
- You can suggest approaches, ask the [agent](#notion-agent) to compare alternatives, or specify priorities.
  State explicitly if a priority or order must remain fixed; otherwise the agent may adapt its choice of routes within the agreed scope.
- Within the authorized scope, autonomous agents may add, revise, reprioritize, split, merge, pause or restart Strategies as findings and resources change.
- A failed route can still be informative.
  It may reveal an obstruction, rule out an approach or identify where an additional hypothesis would be needed.

### <a id="material-claim"></a>Claim

A Claim records an important, precise mathematical statement and what is currently known about its validity.

| Mathematical status | Meaning for the reader |
| --- | --- |
| `open` | The exact statement remains unresolved. Partial results, reductions or a candidate argument may exist, but the conditions for `proved` or `refuted` have not yet been met. |
| `proved` | A complete proof establishes the exact statement under its stated hypotheses. All necessary supporting results are established and applicable, and a recorded mathematical [review](#material-review) found no remaining gap. |
| `refuted` | A checked counterexample or argument disproves the exact statement within its stated scope. All necessary supporting results are established and applicable, and a recorded mathematical review found no remaining gap. |

### <a id="material-review"></a>Review

A Review records an [agent](#notion-agent)'s examination of a mathematical statement or argument, including the exact inputs and scope, findings and unresolved limits.

| Review relationship | Meaning for the reader |
| --- | --- |
| `self-reviewed` | The proof has been checked by an agent involved in developing it or familiar with the mathematical discussion that produced it. |
| `independently reviewed` | A separate agent checked the proof without participating in its development or receiving the development discussion as its own [context](#notion-context). |
| `unknown` | The relationship of an older or source review is genuinely unestablished; this does not imply an error or an independent inspection. |

- These labels describe the review agents' relationship to the proof, not whether the proof is correct.
  A missing relationship declaration differs from `unknown`; no selected review means that the Claim selects no review evidence.
- Another agent still performs self-review if it inherits proof-development discussions, mathematical summaries, author explanations or earlier review conclusions.
  A different [session](#notion-session) or model alone does not establish independence.
- The [main research agent](#notion-main-research-agent) arranges independent reviews at key proof points and, after [Task](#material-task) completion, of the full logical chain.
  You can also request a review of a particular result or proof step.

### <a id="material-ledger"></a>Ledger

A Ledger preserves useful mathematical exploration, including comparisons, failed approaches and reasons for changes in direction.
An entry may explain what was investigated, under which assumptions, what was tried, what the reasoning or evidence showed and what remains unresolved.

A Ledger can preserve partial arguments and useful insights even when an investigation has not produced a standalone [Claim](#material-claim).
For example, failed or inconclusive attempts can reveal obstructions, distinguish approaches or help avoid repeated work.

- You can ask an [agent](#notion-agent) to compare [Strategies](#material-strategy), explain a failed attempt, synthesize findings from several sources or preserve a useful line of reasoning for later work.
- You can also ask an agent to record anything that you consider mathematically substantial and worth recording.
