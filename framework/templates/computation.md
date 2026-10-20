# Computation

Apply the [common content decision](../rules/records.md#substantive-material-retention) before retaining content, reusing an adequate responsible home.
Then follow actual registration, reproduction, source and review duties.
A template does not justify a process-only record.

## Computation Directory README

Use one `readme.md` at `mathematics/computations/programs/<J>/`, with actual programs, verification programs and required original inputs.
Generated results, certificates and verification data belong at the Git-ignored `mathematics/computation/outputs/<J>/`.
Both homes share the same J identity; imported groups use receiving `authorN_repoN_J_Fxxxx` identities and explicitly chosen receiving serials.
Preserve the original research line and physical version where applicable, and original author, repository, source family/serial, path and revision in existing provenance/correspondence.
Repeated acquisition and later versions reuse the established receiving family, distinguishing original identity from immediate transport.
See the [computation rules](../rules/computations.md#computation-output-location).
The inert example below uses `Author_J_W0001`; replace it and its file rows with the actual retained group and files.
Do not invent programs, data or a run to fill the template.
Use the minimal author/source header from the [material format](../material-format.md).

```markdown
---
author: Author
---
# Mathematical computation title

Context: precise links to the responsible Task, Claim, exploration or source audit.

## Question and scope
Question, tested range, assumptions and arithmetic mode.

## Files
| File | Role |
| --- | --- |
| [main.py](main.py) | Actual program role. |
| [input.json](inputs/input.json) | Required original input and scope. |
| [Result](../../../computation/outputs/Author_J_W0001/result.json) | Generated result; state actual local availability. |

## Reproduction
Working directory, command, required inputs and dependency order.
Default output: mathematics/computation/outputs/Author_J_W0001/.
State precision, tolerance, seed and software dependencies when relevant to reproduction.
Identify verification-only commands and their required existing evidence.

## Results and limits
Observed outcome and finite coverage, or not run / incomplete / unknown generator.
Links to responsible mathematics, meaningful failures and actual reviews.
What is established and what remains outside the computation.
```

Retain necessary mathematics and reproduction information in the existing J entrance, authored account or responsible mathematical material.
An optional inspection summary preserves actual checked scope, checking relationship, outcome and limits when they matter.
Unknown details remain unknown; a suggested command is not a new run.
Retain runtime/version details only when they affect the method or reproduction.
There is no generic execution-date duty, raw-log archive, invocation history or report per run.
Logs remain only while useful for troubleshooting; checkpoints only while useful for continuation.
Read actual content and consumers before clearing them: a diagnostic container may hold necessary mathematical data.
Preserve that content and repair consumers first.

Resolve output defaults from the actual repository/J location, create the output home on use and name distinct mathematical scopes clearly.
For a nested entry, identify the containing J directly under `mathematics/computations/programs/`; self inputs, outputs and future locators must follow its actual qualified name.
Shared helpers receive the calling J's output location explicitly.
Document explicit parameters for genuine cross-J dependencies and the actual retained files chosen for them, with no same-name fallback or inferred qualified counterpart.
Use the actual acquired program path when adapting a source command; intake copies native code without rewriting it.
Keep author output, independent verification and smaller controls distinguishable.
Ordinary commands do not rely on root `.tmp/` or undeclared previous output.
Keep live limits, error handling, atomic publication and useful continuation interfaces.
Publish complete output only after the claimed calculation succeeds.

Required witnesses, non-reconstructible data and earlier results used as inputs remain preserved locally.
The ignore rule is neither backup nor delivery; a clone can lack output.
Use [explicit output attachments](../rules/intake.md#computation-output-attachments) when an actual transfer needs them.
A tracked program revision does not attribute an ignored file to its Git tree or establish its generator.
Distinguish acquired-original attachments from receiver-generated results, without changing prior acquisition facts.
No ordinary read, link repair or Git delivery implicitly runs the computation.

Apply the [common maintenance boundary](../rules/records.md#substantive-material-retention) to output cleanup and concise account maintenance.
Preserve fixed mathematics, actual review scope and acquired originals.
Full proofs belong in their responsible mathematical materials; the README supplies no separate Claim assessment or review.
For candidate counterexamples, retain decisive evidence and outstanding checks under [counterexample validation](../rules/computations.md#counterexample-validation).
