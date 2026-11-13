# Instruction Examples

[User manual](../user-manual.md)

Use your preferred language to describe your goal.
Give your agent clear instructions in your chosen harness, using the examples below as a guide.
The examples below are grouped into [setup](#setup), [research](#research-instructions), [administration](#administration-instructions), [manuscript writing](#writing-instructions) and [Lean formalization](#lean-instructions) instructions.
Adapt the wording to your actual question, files and scope.

## <a id="setup"></a>Setup instructions

Use these examples to prepare your workspace, register your author identity and configure local resources.
See the manual's [setup](../user-manual.md#setup) section for the sequence of installation and registration steps.

| Example instruction | Expected agent actions |
| --- | --- |
| <a id="install-acme"></a> Download and install ACME (https://github.com/vtejdn/acme) in `D:\my-math-repository`. | Check the existing contents of the specified directory and integrate the framework files from the selected official version into the actual project root, preserving existing content and Git history and excluding the official repository's Git metadata. Reuse existing project and author information, complete any necessary setup, verify the framework version and entry points at the root, and report the actual installation location, version and unfinished work. |
| <a id="register"></a>Register Ali as my author key; use Alice for the full name. | Use the supplied `Ali` as your author key and `Alice` as your `LICENSE` attribution name, after checking the key and existing registrations. Register you, add the attribution while preserving existing identities and notices, and associate this working copy with `Ali` if it uses Git. |
| <a id="install-git"></a> Install [Git](../git-repository/git-repository.md#notion-git). | Check whether Git is already installed, install it if needed, and report the available version and any remaining setup steps. |
| <a id="setup-git"></a> Set the Git commit name to `Alice` and email to `alice@email.com` for this repository. | Check the effective Git commit identity for this repository. Configure the supplied name and email at the repository or worktree scope when needed. Verify that they match the registered author's Git identity mapping and report the effective values. |
| Tell me how to connect to [GitHub](../git-repository/git-repository.md#notion-github). | Explain how to sign in, authenticate and connect to a remote repository, identifying any steps you need to complete yourself. |
| <a id="test-github-ssh"></a> Test my SSH connection to GitHub | Test authentication with `ssh -T git@github.com` using the SSH settings intended for Git, substituting the configured host alias if applicable. Verify any new host key's fingerprint against GitHub's published values before accepting it. Treat GitHub's authentication greeting as success even with exit status `1`. Report the account named in the greeting and any mismatch with the expected account, or report the specific failure. [GitHub's SSH test guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection) |
| I have set up the connection to Github. Test the connection. | Identify the intended GitHub repository and use `git ls-remote` over its configured SSH or HTTPS connection to test read access. A successful check can return no refs for an empty repository. Report the target, transport, verified account if available, and read result or specific error. [Git reference for `ls-remote`](https://git-scm.com/docs/git-ls-remote) |
| <a id="setup-repo"></a> Set the repository key to `〈repository key〉`. | Validate the selected repository key, record a valid value and update affected current references; ask you to choose another if it is invalid. The repository key is independent of the project abbreviation, full name and README title; preserve the meaning of author keys, material identities and historical source facts. |
| Set the repository abbreviation and full name to `〈abbreviation〉` and `〈full name〉`. | Record your separately chosen project abbreviation and full name, checking that both are nonempty single-line text. Use them to form the README's main heading as “〈abbreviation〉: 〈full name〉”, keeping the configuration and heading consistent and preserving the remaining prose. Set the repository key separately from these choices. |
| <a id="connect-github"></a>Set up Git and connect it to my repository <https://github.com/alice/acme>. | Initialize Git only if needed, complete any missing repository name or author registration using your choices, and associate the working copy with your author key. Check or configure the commit identity to match your registration, connect the specified remote and test access through the relevant account or authentication channel. Preserve existing commits, unrelated settings and Task limits, and report the configured destination and any remaining setup steps. |
| <a id="clone-repo"></a> [Clone](../user-manual.md#notion-clone) my collaborator's repository <https://github.com/alice/acme> and register me as Bob. | Clone the shared repository and check the author key `Bob`, your actual identity and existing registration. For first registration, ask for your independently chosen `LICENSE` attribution name before registering you and adding any required notice. Reuse an applicable existing identity, associate the new Git working copy with the verified author key, preserve existing authors and research materials, and explain the Git commit identity settings. |

## Research instructions

Use these examples to work with literature and explore mathematical questions.

### Find, register or audit literature

| Example instruction | Expected agent actions |
| --- | --- |
| Inspect the local source abc26, register it and audit it. | Identify the work, edition and local original for abc26, complete the bibliography, and maintain edition and original-source location notes as needed. If the original has a table of contents, prepare a searchable copy. Audit its mathematical content and record the scope checked, conclusions and unresolved issues. |
| Audit Theorem 1.7 in abc26. | Locate Theorem 1.7 in the original, check its full statement, hypotheses, proof and the applicability of necessary dependencies, and record the findings, unchecked parts and specific gaps. |
| Search for *On the construction of S* and try to register and audit it. | Identify the work and edition, consult existing materials and try to obtain the original; complete the bibliography and maintain notes on the obtained edition and source location as needed. If the original has a table of contents, prepare a searchable copy. Audit the obtained content and report acquisition failures, unavailable parts and the actual scope checked. |
| How is this definition used in the related literature? | Consult existing definition records and relevant original sources, compare objects, hypotheses, notation and uses, give precise citations, and distinguish source definitions from local reformulations or generalizations. |

### <a id="start-or-continue-research"></a>[Task](../user-manual.md#material-task)

| Example instruction | Expected agent actions |
| --- | --- |
| Set up a Task in [line W](../user-manual.md#notion-research-line-letter) for Conjecture 1.3 in abc26. | Check the original statement, hypotheses and scope of Conjecture 1.3, and first look for an existing Task on the same question. If a new Task is needed, use line W and state its source, exact question and completion criteria. |
| Set up a Task in line F with the goal 'if P, then Q'. | Specify the objects, hypotheses and quantifiers in P and Q, create a Task in line F with 'P implies Q' as its full objective, and state the completion criteria. |
| Create a new Task to generalize Proposition P from finite dimensions to infinite dimensions. | Check the original proposition, specify the new objects, hypotheses and intended conclusion, create the Task, and retain the original proposition as a special case that the generalization must cover. |
| Set up a Task to find a general formula in setting P that includes formula (1) in abc26. | Check the original formula's hypotheses and notation, specify setting P and the scope of the general formula, and create a Task whose completion criteria include a correct derivation and an explanation of how it covers the original formula. |
| Start working on Task F0001 until 5% of the weekly allowance remains. | Check the Task's current state and effective execution conditions, and confirm that weekly usage for the relevant account can be read; report the limitation and defer advancement if it cannot. Advance when execution conditions are met, monitor the remaining allowance, and stop on the first observation of 5% or less remaining or a monitoring failure. Preserve useful results, open questions and a continuation point, and record effective stopping conditions. |
| Organize the results so far, then pause. | Finish checking and organizing the current round's work. Preserve useful results, failed attempts, remaining questions and a usable continuation point; record the pause and conditions that still apply, then stop further advancement. |
| Report on current progress with F0001. | Check the Task's current state, distinguish proved results, candidate arguments, computational observations and open questions, link the relevant materials, and explain what remains to achieve the original objective. |
| Continue working on Task F0001. | Read the current objective, strategies, existing results and stopping conditions, then resume within the current authorization and limits that still apply. If a stopping condition remains in force, explain the specific reason preventing continuation. |

### [Strategies](../user-manual.md#material-strategy)

| Example instruction | Expected agent actions |
| --- | --- |
| Consider constructing an S using theory A; add this strategy to [Task](../user-manual.md#material-task) F0001. | Check the applicability of theory A and record the candidate construction as a research strategy for F0001. State its hypotheses, intended role, steps still to be verified and next action, and compare it with existing strategies to avoid duplication. |
| Incorporate the discussion above into F0001's strategies. | Identify the approach discussed, update an existing strategy or create one as needed, retain its basis, open questions and next step, and associate it with F0001. |
| Search and analyze approaches for Task G0001, propose strategies and set their priorities autonomously. | Read G0001's objective, constraints, existing strategies and relevant materials, reuse local results first, then search and check literature as needed. Compare candidate routes' applicability, grounds, obstacles and resource needs, propose strategies and set their priorities autonomously, recording the reasons, unresolved steps and next action; preserve the original objective, completion criteria and effective execution limits. |

### [Joint Tasks](../user-manual.md#material-task)

| Example instruction | Expected agent actions |
| --- | --- |
| First inspect collaborator Alice's routes, then choose a useful approach for my Task F0001. | Read the relevant routes, reusable results and informative failures, then choose or adapt your own Strategy within F0001's participation scope and existing execution conditions. Different routes can reduce repeated work; deliberate independent verification, replication and cross-checking remain appropriate. |
| Establish a joint Task for this question and link it to Task F0001. | Check the shared question, hypotheses, scope and completion criteria, and establish or reuse an appropriate joint Task; link your F0001 to the version of the common contract actually adopted, specify your participation scope and individual completion criteria, and preserve existing execution conditions. Establishing the link alone does not start research. |

### [Claims](../user-manual.md#material-claim) and [Ledgers](../user-manual.md#material-ledger)

| Example instruction | Expected agent actions |
| --- | --- |
| Organize and record the discussion above according to the framework rules. | Preserve reusable statements and arguments, exploratory findings and other necessary evidence in the appropriate materials, with their hypotheses, sources and unresolved parts. Reuse existing records and repair references. |

## Administration instructions

Use these examples for [Git](../git-repository/git-repository.md#notion-git) operations, environment settings and routine maintenance.

### [Commit](../user-manual.md#notion-commit) and [push](../user-manual.md#notion-push)

| Example instruction | Expected agent actions |
| --- | --- |
| Commit and push. | Determine the intended delivery scope and preserve unrelated staged work. Check the contributor identity, branch and destination remote; confirm connectivity, create the commit and push it, then report the scope committed and the remote result. |
| Commit and push the changes in the manuscript directory for F0001. | Locate the manuscript project for F0001, commit only the changes in the specified directory that belong in Git, and preserve other work. Confirm the identity, destination and connection before pushing, and report the actual scope. |
| Commit all workspace changes. | Check all workspace changes and their authorship, create a local commit of the content that belongs in Git, preserve files excluded by ignore rules, and report the commit scope and any remaining changes. |
| Commit and push without any checks. | Skip content review, formatting checks, tests and extra scans. Perform only the scope, identity, destination and connectivity checks needed for Git delivery, then commit, push and report the result. |

### [Pull](../user-manual.md#notion-pull) and [merge](../user-manual.md#notion-merge)

| Example instruction | Expected agent actions |
| --- | --- |
| Pull the latest remote changes and merge them into the [local branch](../user-manual.md#notion-git-branch). | Check the current branch and its corresponding remote, preserve local work, fetch and merge remote updates, and report the result. For conflicts affecting mathematical meaning, explain the specific differences and suggest how to proceed. |

### Environment settings

| Example instruction | Expected agent actions |
| --- | --- |
| Create a directory junction from [mathematics/literature/pdf](../../mathematics/literature/pdf) to `D:\MyLiterature`. | Check the project path and target directory, preserve existing sources, set up the directory junction to the specified folder, and confirm that source files are excluded from Git. |
| Set the default [context length](../user-manual.md#notion-context-length) for this project's `<harness name>` to 512k. | Identify the [harness](../agent-harness.md) configuration for this project, confirm that the model and runtime support the requested length, and update this project's default. Explain how the change takes effect and whether it has been verified in use; report the actual limit if the requested setting is unsupported. |
| Set my default Task stopping condition: pause when 5% of the weekly allowance remains. | Record this as your personal default execution preference, to apply when no more specific setting takes precedence. Preserve effective conditions on existing Tasks, and explain how the relevant weekly usage can be read. |

### [Import](../user-manual.md#notion-import) and [Intake](../user-manual.md#notion-intake)

| Example instruction | Expected agent actions |
| --- | --- |
| Import Task F0001 from my repository `〈repository URL〉`. | Verify the source repository and your author identity, import F0001 and its necessary mathematical dependencies, and reuse adequate existing local materials; obtain required inputs from other authors through intake, and retain the joint contract link or prepare a complete standalone contract as appropriate. Preserve effective stopping conditions and allowances; import alone does not start research. |
| Import my writing settings and manuscript F0001 from my repository `〈repository URL〉`. | Import the selected personal writing settings that still apply, along with the source files, figures, bibliography and necessary mathematical support for manuscript F0001; preserve authorship and the scope of the settings, reuse existing local materials, repair references, perform necessary build checks, and report missing inputs and remaining issues. |
| Receive materials related to Alice's Task A0001 from `〈repository URL〉`. | Verify the source repository and Alice's author identity, select the results, arguments, computations and reviews related to A0001 that are needed for this request, and reuse adequate existing materials; preserve original authorship, exact sources, complete necessary mathematics and actual review limitations, and report unavailable necessary inputs. Conduct subsequent research under your own Task and authorization. |

### Routine maintenance

| Example instruction | Expected agent actions |
| --- | --- |
| Enable/disable automatic framework version checks for this repository. | Update this repository's setting according to your choice of enabling or disabling checks, preserve other configuration and report the current setting; when enabled, follow the automatic-check rules for each UTC day. An upgrade still requires actual explicit authorization. |
| Upgrade the framework to the latest version. | Check the installed and latest official versions; if an update is available, fix the target version and commit, adapt affected files according to the upgrade notes and perform necessary checks, preserving local changes, research materials, personal settings and effective execution conditions. Update the installed version after checks pass; in an actual multi-author shared Git repository, commit, push and confirm the remote result under the default authority, honoring explicit local-only, offline or no-push limits. Report the versions before and after, target commit, checks and delivery results, and whether no update was available or any work remains unfinished. |
| Resolve merge conflicts according to the framework rules. | Inspect both sides' changes, authorship and actual authority, and directly resolve administrative conflicts whose resolution is clear, including locator repairs that preserve the object and mathematical meaning. Preserve both sides' evidence for substantive mathematical disagreements, explain the differences and perform a scoped recheck under existing authorization or after obtaining the necessary authorization; retain substantive corrections to another author's content in the correcting author's own materials. Check the merged result and affected references, and report the outcome and unresolved issues. |
| Inspect the files in `.tmp` and delete those that can be safely removed. | Check what the files are for and whether they are in use. First preserve any necessary content not yet saved in the research materials, then delete files confirmed to be disposable and unused by other active sessions. |
| Check whether local mathematical materials conform to the framework rules. | Within the assigned scope, have an agent isolated from the repair and acceptance stages inspect local mathematical materials and necessary inputs and references in read-only batches, checking authorship, versions, assessments, sources, review bindings and other applicable requirements. Record conformity issues in `maintenance` and substantive mathematical issues in `erratum`, and report actual coverage, unchecked scope and unresolved issues. |
| Read maintenance and erratum, and repair issues according to the framework rules. | Read the issues awaiting repair within the assigned scope; have an agent meeting the stage-isolation requirements verify them, repair within the applicable author permissions, self-check and inspect necessary consumers. Arrange independent acceptance for conformity repairs, and apply the actual version, assessment and mathematical-review requirements to mathematical errors. Preserve the original issue, grounds, acceptance requirements and unrepaired or unaccepted items, and report the repair scope and remaining limits. |
| Accept material repairs according to the framework rules. | Have an independent agent that neither participated in inspection or repair of the same scope nor inherited related substantive discussion check submitted repairs and necessary consumers against the original issues and current rules, and report which repairs pass or fail and the scope checked. Clear accepted worklist portions only within actual author-side or receiving-side disposition authority, retaining failed, unaccepted, out-of-scope and concurrently added items; acceptance does not repair materials, and conformity acceptance is not independent mathematical review. |

## <a id="writing-instructions"></a>Writing manuscripts

| Example instruction | Expected agent actions |
| --- | --- |

## <a id="lean-instructions"></a>Lean formalization

| Example instruction | Expected agent actions |
| --- | --- |

