# Instruction Examples

[User manual](../user-manual.md)

Use natural language to describe your goal.
The examples below are grouped into [setup](#setup), [research](#research-instructions) and [administration](#administration-instructions) instructions.
Adapt the wording to your actual question, files and scope.

## <a id="setup"></a>Setup instructions

Use these examples to prepare your workspace, register your author identity and configure local resources.
See the manual's [setup](../user-manual.md#setup) section for the sequence of installation and registration steps.

| Example instruction | Expected agent actions |
| --- | --- |
| Download [ACME](https://github.com/vtejdn/acme) to `D:\acme`. | Check that the destination is suitable for installation, download the ACME framework files, preserve existing content, and report the version and any remaining setup steps. |
| Install [Git](../git-repository.md#notion-git). | Check whether Git is already installed, install it if needed, and report the available version and any remaining setup steps. |
| Register Ali as my author key; use Alice for the full name. | Use the supplied `Ali` as your author key and `Alice` as your `LICENSE` attribution name, after checking the key and existing registrations. Register you, add the attribution while preserving existing identities and notices, and associate this working copy with `Ali` if it uses Git. |
| Tell me how to connect to [GitHub](../git-repository.md#notion-github). | Explain how to sign in, authenticate and connect to a remote repository, identifying any steps you need to complete yourself. |
| I have signed in to GitHub. Test the connection. | Check the authenticated account and perform read-only connectivity tests for GitHub and the target repository. Report the result or the specific error. |
| [Clone](../user-manual.md#notion-clone) [ACME](https://github.com/vtejdn/acme) to `D:\acme`. | Check that Git, access permissions and the destination are ready, clone the ACME repository including its version history, and report the branch, version and remaining initialization steps. |
| Use `repository name` as the repository name | Validate the chosen name, asking you to choose another if it is invalid rather than changing it automatically. Record the accepted name in the framework and update the current repository name display and affected references, preserving author keys, material identities and historical source facts. |
| Set up Git and connect it to my repository <https://github.com/alice/acme>. | Initialize Git only if needed, complete any missing repository name or author registration using your choices, and associate the working copy with your author key. Check or configure the commit identity to match your registration, connect the specified remote and test access through the relevant account or authentication channel. Preserve existing commits, unrelated settings and Task limits, and report the configured destination and any remaining setup steps. |
| Clone my collaborator's repository <https://github.com/alice/acme> and register me as Bob. | Clone the shared repository, register you as Bob, and associate the new Git working copy with Bob. Preserve existing authors and research materials, and report the Git commit identity settings. |

## Research instructions

Use these examples to work with literature and explore mathematical questions.

### Find, register or audit literature

| Example instruction | Expected agent actions |
| --- | --- |
| Inspect the local source abc26, register it and audit it. | Identify the work, edition and local original for abc26, and complete its bibliographic and file registration. If the original has a table of contents, prepare a searchable copy of it. Audit its mathematical content and record the scope checked, conclusions and unresolved issues. |
| Audit Theorem 1.7 in abc26. | Locate Theorem 1.7 in the original, check its full statement, hypotheses, proof and the applicability of necessary dependencies, and record the findings, unchecked parts and specific gaps. |
| Search for *On the construction of S* and try to register and audit it. | Identify the work and edition, check existing records and try to obtain the original. Record the bibliographic details and what was actually obtained. If the original has a table of contents, prepare a searchable copy. Audit the available content and identify anything unavailable. |
| How is this definition used in the related literature? | Consult existing definition records and relevant original sources, compare objects, hypotheses, notation and uses, give precise citations, and distinguish source definitions from local reformulations or generalizations. |

### <a id="start-or-continue-research"></a>Start or continue a [Task](../user-manual.md#material-task)

| Example instruction | Expected agent actions |
| --- | --- |
| Set up a Task in line W for Conjecture 1.3 in abc26. | Check the original statement, hypotheses and scope of Conjecture 1.3, and first look for an existing Task on the same question. If a new Task is needed, use [line W](../user-manual.md#notion-research-line-letter) and state its source, exact question and completion criteria. |
| Set up a Task in line F with the goal 'if P, then Q'. | Specify the objects, hypotheses and quantifiers in P and Q, create a Task in line F with 'P implies Q' as its full objective, and state the completion criteria. |
| Create a new Task to generalize Proposition P from finite dimensions to infinite dimensions. | Check the original proposition, specify the new objects, hypotheses and intended conclusion, create the Task, and retain the original proposition as a special case that the generalization must cover. |
| Set up a Task to find a general formula in setting P that includes formula (1) in abc26. | Check the original formula's hypotheses and notation, specify setting P and the scope of the general formula, and create a Task whose completion criteria include a correct derivation and an explanation of how it covers the original formula. |
| Start working on Task F0001 until 5% of the weekly allowance remains, then organize the results and pause. | Check the Task's current state and execution conditions, and confirm that the relevant weekly usage can be read before proceeding. Monitor the remaining allowance and stop advancement at the 5% threshold, organize results, open questions and a continuation point, then pause. |
| Continue working on Task F0001. | Read the current objective, strategies, existing results and stopping conditions, then resume within the current authorization and limits that still apply. If a stopping condition remains in force, explain the specific reason preventing continuation. |

### Shared goals

| Example instruction | Expected agent actions |
| --- | --- |
| First inspect collaborators' routes, then choose a useful approach for my Task F0001. | Read the relevant routes, reusable results and informative failures, then choose or adapt your own Strategy within F0001's participation scope and existing execution conditions. Different routes can reduce repeated work; deliberate independent verification, replication and cross-checking remain appropriate. |
| Establish a joint Task for this question and link it to Task F0001. | Check the shared question, hypotheses, scope and completion criteria, and establish or reuse an appropriate joint Task; link your F0001 to the version of the common contract actually adopted, specify your participation scope and individual completion criteria, and preserve existing execution conditions. Establishing the link alone does not start research. |


### Content imports

| Example instruction | Expected agent actions |
| --- | --- |
| Import Task F0001 from my repository `〈repository URL〉`. | Verify the source repository and your author identity, import F0001 and its necessary mathematical dependencies, and reuse adequate existing local materials; obtain required inputs from other authors through intake, and retain the joint contract link or prepare a complete standalone contract as appropriate. Preserve effective stopping conditions and allowances; import alone does not start research. |
| Import my writing settings and manuscript F0001 from my repository `〈repository URL〉`. | Import the selected personal writing settings that still apply, along with the source files, figures, bibliography and necessary mathematical support for manuscript F0001; preserve authorship and the scope of the settings, reuse existing local materials, repair references, perform necessary build checks, and report missing inputs and remaining issues. |
| Receive materials related to Alice's Task A0001 from `〈repository URL〉`. | Verify the source repository and Alice's author identity, select the results, arguments, computations and reviews related to A0001 that are needed for this request, and reuse adequate existing materials; preserve original authorship, exact sources, complete necessary mathematics and actual review limitations, and report unavailable necessary inputs. Conduct subsequent research under your own Task and authorization. |

### Other common instructions

| Example instruction | Expected agent actions |
| --- | --- |
| Consider constructing an S using theory A; add this [strategy](../user-manual.md#material-strategy) to Task F0001. | Check the applicability of theory A and record the candidate construction as a research strategy for F0001. State its hypotheses, intended role, steps still to be verified and next action, and compare it with existing strategies to avoid duplication. |
| Incorporate the discussion above into F0001's strategies. | Identify the approach discussed, update an existing strategy or create one as needed, retain its basis, open questions and next step, and associate it with F0001. |
| Organize and record the discussion above according to the framework rules. | Preserve reusable statements and arguments, exploratory findings and other necessary evidence in the appropriate materials, with their hypotheses, sources and unresolved parts. Reuse existing records and repair references. |
| Report on current progress with F0001. | Check the Task's current state, distinguish proved results, candidate arguments, computational observations and open questions, link the relevant materials, and explain what remains to achieve the original objective. |
| Organize the results so far, then pause. | Finish checking and organizing the current round's work. Preserve useful results, failed attempts, remaining questions and a usable continuation point; record the pause and conditions that still apply, then stop further advancement. |

## Administration instructions

Use these examples for Git operations, environment settings and routine maintenance.

### Commit and push

| Example instruction | Expected agent actions |
| --- | --- |
| [Commit](../user-manual.md#notion-commit) and [push](../user-manual.md#notion-push). | Determine the intended delivery scope and preserve unrelated staged work. Check the contributor identity, branch and destination remote; confirm connectivity, create the commit and push it, then report the scope committed and the remote result. |
| Commit and push the changes in the manuscript directory for F0001. | Locate the manuscript project for F0001, commit only the changes in the specified directory that belong in Git, and preserve other work. Confirm the identity, destination and connection before pushing, and report the actual scope. |
| Commit all workspace changes. | Check all workspace changes and their authorship, create a local commit of the content that belongs in Git, preserve files excluded by ignore rules, and report the commit scope and any remaining changes. |
| Commit and push without any checks. | Skip content review, formatting checks, tests and extra scans. Perform only the scope, identity, destination and connectivity checks needed for Git delivery, then commit, push and report the result. |

### Pull and merge

| Example instruction | Expected agent actions |
| --- | --- |
| [Pull](../user-manual.md#notion-pull) the latest remote changes and [merge](../user-manual.md#notion-merge) them into the [local branch](../user-manual.md#notion-git-branch). | Check the current branch and its corresponding remote, preserve local work, fetch and merge remote updates, and report the result. For conflicts affecting mathematical meaning, explain the specific differences and suggest how to proceed. |

### Environment settings

| Example instruction | Expected agent actions |
| --- | --- |
| Create a directory junction from [mathematics/literature/pdf](../../mathematics/literature/pdf) to `D:\MyLiterature`. | Check the project path and target directory, preserve existing sources, set up the directory junction to the specified folder, and confirm that source files are excluded from Git. |
| Set the default [context length](../user-manual.md#notion-context-length) for this project's `<harness name>` to 512k. | Identify the [harness](../agent-harness.md) configuration for this project, confirm that the model and runtime support the requested length, and update this project's default. Explain how the change takes effect and whether it has been verified in use; report the actual limit if the requested setting is unsupported. |
| Set my default Task stopping condition: pause when 5% of the weekly allowance remains. | Record this as your personal default execution preference, to apply when no more specific setting takes precedence. Preserve effective conditions on existing Tasks, and explain how the relevant weekly usage can be read. |

### Routine maintenance

| Example instruction | Expected agent actions |
| --- | --- |
| Defer the framework upgrade and continue the current work. | Keep the installed version and continue the authorized assignment; the reminder grants no upgrade permission. |
| Disable automatic framework version checks for this repository. | Disable this repository's daily metadata check while preserving the current framework and research work. |
| Enable automatic framework version checks for this repository. | Enable the repository's daily check; any later upgrade still requires your explicit request. |
| Recheck the official framework version now. | Make one fresh bounded version check, report the installed and verified available versions or an unavailable result, and preserve any previous reminder. |
| Upgrade this repository to the official framework version you just identified. | Identify the selected version, affected local framework files and actual material migration, preserve existing research and effective Task conditions, and perform the explicitly authorized upgrade. |
| Inspect the files in `.tmp` and delete those that can be safely removed. | Check what the files are for and whether they are in use. First preserve any necessary content not yet saved in the research materials, then delete files confirmed to be disposable and unused by other active sessions. |

## Writing manuscripts

| Example instruction | Expected agent actions |
| --- | --- |

## Lean formalization

| Example instruction | Expected agent actions |
| --- | --- |
