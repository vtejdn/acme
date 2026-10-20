# Human Request Examples

[User manual](../../user-manual.md)

Use ordinary language to describe your objective, the object to work on and any scope or stopping condition.
These examples suggest useful requests; they are not fixed syntax, a complete command language or mandatory wording.
An example confers no authority until your actual instruction selects work within its applicable boundaries.
The manual explains setup and how to read results; [script documentation](../../scripts/readme.md) supplies exact optional interfaces when needed.

## Start or continue research

| Example request | When useful | Information to provide | Expected result |
| --- | --- | --- | --- |
| “Investigate whether every object satisfying H has property P.” | Start a substantive mathematical question. | Domain, hypotheses, quantifiers, desired proof/counterexample, useful weaker results and execution limits. | A precise authorized question and research progress with actual evidence and gaps. |
| “Continue Task F0001.” | Resume work on an existing objective. | The intended Task or material, changed priorities/limits and any actual resumption authority. | Work within current authority and stop conditions, or the concrete boundary preventing it. |
| “Discuss these possible approaches before choosing one.” | Compare ideas without starting autonomous research. | The question, alternatives and the decision you need. | A scoped comparison and open issues, without silently activating a Task. |

Name the actual question or existing work; you need not choose internal material operations or a sequence of tools.
The result should preserve your actual objective and existing execution boundaries.

## Close a round or stop work

| Example request | When useful | Information to provide | Expected result |
| --- | --- | --- | --- |
| “Close this round and organize the results.” | Finish the current research batch. | The round or materials and any specific deliverable. | Checked results, retained useful failures, remaining obligations and a continuation point. |
| “Complete the Task against its original criteria.” | Assess whether the objective has been met. | The intended Task and any actual requested review scope. | Completion only if its original contract and evidence suffice; otherwise the exact unresolved criterion. |
| “Finish the current work, then pause.” | Stop after the active batch is made usable. | Which work should finish and any retained checkpoint needed. | That closeout and a usable handoff, followed by the requested pause. |
| “Stop execution now.” | End further advancement at the current boundary. | The intended run or object if context is ambiguous. | Preserved available findings and actual stop facts; no mathematical completion inferred. |

Round closeout, execution stopping and Task completion have different outcomes.
Specify which outcome you intend when the distinction affects the work.

## Review work or request a check

| Example request | When useful | Information to provide | Expected result |
| --- | --- | --- | --- |
| “Review this proof and report concrete gaps.” | Assess mathematical correctness. | The exact argument, hypotheses and intended review depth; say whether edits are authorized. | Findings with checked scope, decisive reasoning and remaining limits. |
| “Review the whole manuscript, including citations and build diagnostics.” | Inspect a complete document. | The active document, intended mathematical/citation/layout scope and any source restrictions. | Distinct mathematical, citation and build findings covering the requested scope. |
| “Check the staged view” / “Check changes from BASE.” | Inspect a specific Git view. | INDEX, WORKTREE or the actual comparison base and selected scope. | Findings for those bytes; unstaged fixes do not repair another view. |

A mathematical review, structural check and source-byte inventory answer different questions.
State the intended depth and scope explicitly, especially for a broad audit.

## Find, register or read literature

Original literature stays in local storage and is excluded from cross-repository intake.
Request independent source acquisition when you need the original text.

| Example request | When useful | Information to provide | Expected result |
| --- | --- | --- | --- |
| “Find existing results relevant to this question.” | Reuse knowledge before substantial proof work. | The question, hypotheses, known sources and any access constraints. | Relevant existing evidence, exact applicability and unresolved source checks. |
| “Register this paper and prepare its contents if supplied.” | Retain an actual source for present or future use. | The actual work/edition, provided file or authorized address and any known access limitations. | Bibliographic/artifact facts, actual availability and applicable contents preparation, distinct from proof review. |
| “Read this theorem's statement and hypotheses; do not audit its proof.” | Obtain a precise bounded source inspection. | Exact source/edition/passages and intended use. | The inspected statement, assumptions, applicability and honest depth limits. |
| “Audit this source's proof, including its Lean code.” | Request the additional code/formalization scope. | Exact source, proof and code revision, intended trust/axiom checks and available tools. | Actual proof/code findings and the checks performed; associated Lean is otherwise excluded by default. |

Acquisition, contents, source inspection and proof review remain separate outcomes.

## Write or revise a manuscript

| Example request | When useful | Information to provide | Expected result |
| --- | --- | --- | --- |
| “Prepare this manuscript from these established results.” | Present selected mathematics. | The actual document, author, audience, scope and sources to use. | A manuscript with actual citation/source support and applicable build checks. |
| “Revise this statement without changing its hypotheses or quantifiers.” | Make a precise wording change. | The active source, intended logical meaning and any required notation. | The requested text change and verification of its actual scope. |
| “Use source A as a style model; source B may be reused except Section 4.” | Give scoped writing/reuse choices. | The manuscript or author-wide scope, exact sources and exceptions. | Choices applied at that scope, with truthful attribution and mathematical fit. |

A style reference does not itself authorize text reuse, and changing the operator does not change the responsible author's choices.
The manual's [writing explanation](../../user-manual.md#use-literature-computations-and-manuscripts) helps distinguish these choices.

## Compute, maintain or reuse work

| Example request | When useful | Information to provide | Expected result |
| --- | --- | --- | --- |
| “Reproduce this computation with these parameters.” | Check a stated calculation. | The actual program, inputs, parameter range and result to reproduce. | The actual run, arithmetic mode, result and limits, including failure if it occurs. |
| “Repair these links and navigation while preserving the mathematics.” | Perform routine shared maintenance. | The affected objects and intended same-object targets. | Direct administrative repair, including in another author's material, with meaning and provenance preserved. |
| “Compare these conflicting statements before deciding a repair.” | Locate an actual integration conflict. | Both statements/evidence and affected materials; specify any already authorized mathematical recheck. | A concrete distinction between administrative inconsistency and a substantive mathematical conflict requiring scoped recheck approval. |
| “Reuse this finding from repository B.” | Acquire mathematics from a distinct research repository. | Exact source revision, useful finding and intended local use. | Chosen scope, explicit local source/author correspondence, receiving placement and actual available/unavailable inputs; no automatic adoption. |

Administrative conflicts follow framework rules; an unclear rule is reported for human ruling.
A mathematical recheck approval alone does not authorize substantive editing of another author's material.
The manual explains [collaboration](../../user-manual.md#collaborate-and-acquire-external-work) and [computational limits](../../user-manual.md#use-literature-computations-and-manuscripts).

## Commit and push

| Example request | When useful | Information to provide | Expected result |
| --- | --- | --- | --- |
| “Commit these changes.” | Save a truthful local checkpoint. | The intended paths or full requested worktree scope and any message preference. | A local commit, actual delivered scope and remaining working state. |
| “Push the current commits.” | Deliver an authorized local tip. | The intended branch/remote when context is ambiguous. | A verified remote result or concrete delivery blocker. |
| “Commit and push after the requested corrections are complete.” | Make delivery depend on specific work. | The corrections, intended scope and actual delivery condition. | That condition checked first, followed by the authorized delivery when satisfied. |

Draft or unfinished mathematics can be committed with its true status.
Plain commit/push performs delivery without starting framework regressions, a whole-library audit, recursive proof review or source-store hashing.
Expect the actual delivered scope, attribution and local or remote result to be stated clearly.
