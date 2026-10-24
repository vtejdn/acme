# Computation Evidence

Routine naming, path, link and layout maintenance follows the [common content and maintenance boundary](records.md#substantive-material-retention), preserving mathematical meaning with coherent edits and Git history.
It requires no new mathematical version, operation entry, standalone maintenance report or duplicate correspondence artifact.
Keep the responsible material and its actual consumers coherent in place; substantive mathematics retains its version and review requirements.

## When to Retain a Computation Record

First apply the [common content decision](records.md#substantive-material-retention) to needed native work and adequate existing J homes, then the [work-obligation rules](workflow.md#work-obligations) and J reproduction duties below.
Useful failed or not-yet-run continuing programs may need retention; routine moves, link-repair scripts and disposable trials do not become J archives.
This adds no per-run fixed version or output-history obligation.
A temporary trial with no consequential finding requires neither a Claim ID nor a standalone computation record.
When an executed computation is retained or cited as evidence, changes a route decision or supports a handoff, preserve the relevant reproducibility information below.
Its context may be an authorized question, Task, route, exploration entry, Claim or source unit.
A script supplied for future execution must remain marked not run until actually executed.

A compact comment block or existing exploration section can supply a small computation's execution information.
Each retained authored computation, including a single program or dataset, has one numbered J directory with a concise README; link existing fixed evidence instead of copying it into another report.
Preserve decisive parameters, outcomes and limitations when they matter; do not invent a theorem, analytic reduction or review merely to fill the template.

Retain programs, necessary inputs, decisive parameters, usable commands and mathematical checks.
Runtime and library details matter when a concrete method, representation or known behavior affects the calculation or its reproduction.
Generated output may be regenerated, overwritten or removed only when its actual consumers remain coherent.
Retain necessary witnesses, certificates, non-reconstructible data and earlier results still used as inputs.
Keep the exact finite scope, precision or error control, actual outcome and coverage, useful failures and any real checking relationship in the existing responsible material.
Unknown generation or inspection facts remain unknown.
Execution dates, elapsed time, machine identity, invocation counts and empty stderr have no generic retention duty.
Fixed R review facts and E authority/stop facts retain their separate responsibilities.
Retain logs locally only while needed for troubleshooting and checkpoints only while useful for continuation.
After necessary content is retained and consumers repaired, clear redundant diagnostics and obsolete continuation state.
Do not create a raw-log archive, execution chronology, per-run report, fingerprint gate or substitute receipt.
Keep live resource limits, failure handling, atomic publication and useful resume interfaces.
Publish complete output only after its claimed calculation succeeds; failed or incomplete calculations remain truthful.

Keep useful inspection facts in the existing J README or authored J text; an ordinary `## Inspection summary` heading may help organize them.
No field table, dedicated fact file or report per run is required.
A long report may be condensed or relocated with useful facts and mathematics retained and actual references repaired.
Correct historical errors explicitly while preserving the actual scope and results.

Valid J documentation maintenance, coherent moves and authorized cleanup of reproducible output add no generic change reminder in any selected Git view.
The responsible agent inspects relevant changes and retains needed programs, inputs, witnesses, actual inspection facts and limits under the common rule and [agent/tool responsibility](workflow.md#agent-and-tool-responsibilities).
Concrete identity, reference, native-format, explicit-decision and review-binding errors remain checked, with actual source unavailability and recorded limitations at their scope.
J/E/intake edits do not trigger generic reminders.
A quiet structural check supplies no proof review or assertion that a result is unchanged.
Generated JSON, Markdown and other reproducible output may be regenerated or removed with coherent consumers; this permission does not authorize overwriting fixed mathematics, review evidence or acquired originals.

When reproduction is needed, the agent may delete only the generated outputs it will replace and rerun using the same responsible J program and output homes.
Existing safe overwrite commands remain usable; deletion is optional.
Document replaceable outputs, required inputs and command order.
Preserve programs, original inputs, parameters, non-reconstructible witnesses and earlier results still read by the chosen check.
A failed rerun remains failed or incomplete: do not advertise an absent replacement, report an old success as a new pass or change tolerances/scope to force agreement.
Ordinary reading, link/layout maintenance and hash removal do not require reproduction.
No per-run directory, archive or cleanup approval is required.

<a id="computation-output-location"></a>
## Work and Output Location

Develop a program that will be continued or reused directly in its responsible writable J group.
Exploration, unsuccessful trials and independent checks can share that group with their actual scope; a J directory does not certify a result.
Reuse the same group for one coherent calculation rather than allocating an identity per run.
Short disposable arithmetic may remain interactive or in an existing working draft; it needs no file, Claim or new J merely to avoid temporary storage.
Continuing mathematical arguments belong in D, with useful findings and failures retained in their responsible mathematical materials.

Programs, verification programs, required original inputs and the concise README use `mathematics/computations/programs/<J>/`.
Generated results, certificates and verification data use `mathematics/computation/outputs/<J>/`.
The plural program path and singular output path are intentional.
Use the exact existing J directory identity, including the receiving authorN/repoN and established receiving serial of an acquired group.
Both homes belong to that one J; output separation creates no new identity or per-run directory.
The shared output root is local to the checkout and ignored by Git through `/mathematics/computation/outputs/`.
Generic discovery, ordinary staging and clean framework export exclude it.
Explicit reads, declared verification inputs and selected intake attachments may access actual files there under the usual path-safety rules.

Resolve default paths from the actual repository and J location, independently of the caller's working directory.
The containing J is the directory directly under `mathematics/computations/programs/`, including any acquired repository component; a nested `programs/` or `checks/` directory is not the J identity.
Self-group input defaults, output defaults and newly recorded locators follow that actual containing J after acquisition or onward transfer.
Create the required output directory on use.
A shared helper receives the calling J's output location explicitly.
Genuine cross-J dependencies use an explicitly specified retained file or native input parameter, without deriving a qualified name, searching alternatives or falling back to another local group.
If the required file or supported binding is absent, report that execution limit.
Maintain source programs and their callers; intake preserves native bytes unless an explicitly selected `file_preparations` input supplies permissible adaptation under the responsible author's boundary.
Preserve actual per-file originals and verify relevant behavior or mathematical-method changes.
Keep meaningful child names for distinct mathematical scopes and distinguish author output from independent verification output.
The documented generation command must work without root `tmp/` or `.tmp/` and without prior generated output, except declared input dependencies.
An explicitly identified verification-only command requires its actual retained inputs.
When one J consumes another's generated data, name that dependency and read the producing J's output home.
The README links actual output files and explains input requirements, command order, observed scope and limitations.

Keep an explicit output option when useful, using the responsible J output home in ordinary examples.
A small control must not replace evidence for a different claimed range.
Repeated runs at the same scope may overwrite the same replaceable output.
Preserve acquired-original attachments when an actual consumer still needs them, and distinguish receiver-generated results from those originals.
Use the [explicit attachment boundary](intake.md#computation-output-attachments) for transfer and onward provenance.
Ignoring output provides neither a backup nor delivery to another checkout.
A clone can lack it; report the actual missing scope without a substitute, automatic calculation or claim of completed acquisition.

Retained diagnostic logs, useful checkpoints and atomic-write intermediates use the same J output home and remain distinguishable from complete results.
A file called progress or checkpoint may contain necessary mathematical evidence or input; read its actual role and consumers before cleanup.
Preserve necessary content and repair consumers before removing a container.
A checkpoint does not establish completion, resume a stopped Task or authorize a larger computation.
Deliberate corruption controls use an isolated copy under the [temporary-storage rule](organization.md#temporary-storage).

Ordinary mathematical exploration has no scratch-directory stage before J/D/L.
The root `.tmp/` is for disposable operational isolation, not a normal calculation target or the only home of a proof, witness, required input, useful failure or continuation record.

## Files and Reproducibility

- Use `mathematics/computations/programs/Author_J_W0001/` for a local program home, with the author's chosen research line and an independent J counter.
  Imported groups use the receiving external identities and explicitly chosen receiving serial in both program and output homes, for example `author3_repo2_J_W0007/`.
  Preserve the exact original author, repository, research line, family/serial, physical version where applicable, path and revision in existing provenance/correspondence, separately from the chosen receiving identity.
  Repeated acquisition and later versions reuse the established receiving family; original and immediate transport identities remain distinct.
  Every group has one entrance `readme.md`, with the minimal author/source header and the [template](../templates/computation.md) sections: Question and scope, Files, Reproduction, Results and limits.
  These examples are inert.
- Group one coherent calculation with its actual programs, inputs, outputs and checks across the two declared homes.
  Use names reflecting actual roles, such as `main.py`, `verify.py`, `helpers.py`, `inputs/` and an authored `record.md` on the program side, with generated `data.json`, `verification.json` or certificate children on the output side.
  Parameter-labelled child data may distinguish mathematical scopes.
  Share helpers through explicit imports/links and supply the caller's output location when a helper writes results.
  Preserve native structured data and meaningful failed or partial results.
  A surviving dataset needs no invented program or separate identity for each child.
- Inspect authored TXT prose/output before converting it to Markdown or its actual structured format.
  Original literature PDFs stay in their literature store and manuscript PDFs in their manuscript project; J links those sources rather than retaining PDF copies.
- Retained inspection summaries preserve the actual conclusion and checking scope; whole computation reports need not be byte-locked.
  A `versions/vN/` directory alone does not make every native child immutable.
  Programs, required inputs and coherent consumers must remain available, while reproducible outputs may be regenerated or cleaned up.
  A README links separately fixed mathematics or C/L material without replacing its proof, assessment or review.
- Give a usable command and working directory, required inputs and parameters, relevant random seeds, precision and tolerance.
  State a runtime or dependency version when it affects the method or reproduction.
  Use repository-relative durable locators under the [locator rule](organization.md#machine-local-locators); resolve actual OS paths at runtime.
  Distinguish normalized historical commands, literal original invocations and proposed reproduction commands.
- Preserve or reproduce the mathematical result with necessary inputs and checks; a saved output is not its own correctness oracle.
  State the actual outcome, completed finite coverage and failed checks.
  A zero exit code alone does not establish the mathematical property.
- State the exact finite question, tested range or observation and why it informs the investigation.
  If the computation is claimed to establish part of an argument, supply or link the analytic reduction and its assumptions.
  Where that reduction remains unknown, label the result as exploratory and state what it does not establish.
- Before refactoring a supporting script or extracting shared helpers, preserve a meaningful baseline for the claimed calculation and check that representation, normalization, and certified scope remain compatible.
  Record changes that affect earlier results.
- For a relocation, inspect imports, dynamic loaders, sibling/parent path assumptions, input/output defaults, working directories and direct callers together.
  Rewrite active references coherently while preserving truthful descriptions of historical execution.
  Use bounded checks of affected interfaces and recorded mathematical outputs; moving a certificate does not require rerunning every historical computation.
- Verification scripts compare the mathematical payload, including scope-relevant inputs, range, tolerance and normalization.
  Remove persistent input/program/output fingerprints, saved digest baselines, digest warnings and digest acceptance gates, including historical values and their writers/readers.
  Preserve exact mathematical checks; incidental time/path metadata or raw bytes are not the mathematical target.
  Literature-file fingerprints computed from actual local bytes retain their separate accidental-damage checking role in the source registry; intake carries no literature baseline.

## Evidence and Limits

State whether each result uses exact arithmetic, symbolic manipulation, floating-point approximation, or heuristic exploration.
When a script combines these modes, distinguish their outputs and conclusions.
For symbolic calculations, record domain assumptions and the verification needed for the resulting identities.

Exact arithmetic certifies only the finite identity, inequality, or bounded parameter region actually checked, subject to the recorded mathematical reduction.
It does not establish all-order positivity, untested parameters, convergence, or an exchange of limits and integrals.
Floating-point scans, truncated expansions, and random trials are observations unless a separate rigorous argument supplies the required error control and coverage.

Use checks relevant to the mathematical property: known identities, small exact cases, an independent calculation, or justified error bounds.
Preserve counterexamples and discrepancies with their parameter settings.
Reviews of computations supporting a project argument belong in [proof audits](../../mathematics/audits/reviews); the [Claim index](../../mathematics/claims/index.md) links the applicable review evidence.
Consequential outcomes belong in the responsible Task, Claim or route; the stable mathematics entrance carries no progress narrative.

<a id="counterexample-validation"></a>
## From Numerical Anomalies to Verified Counterexamples

Use this procedure when pursuing a numerical candidate as a counterexample.
A retained candidate may stay in an existing exploration record or script comment under the retention rules above; the procedure creates no registration or certification requirement for routine trials.

1. Preserve the candidate's parameters, construction, precision and relevant output.
   Describe it as a numerical anomaly or candidate counterexample while the decisive verification is outstanding.
2. Check the original hypotheses and specify the exact instance being tested.
   If parameters are rounded, reconstructed or replaced by exact values, recheck admissibility and the claimed violation for those values.
   A defect in a stronger intermediate conjecture does not by itself refute the original target.
3. Certify the violated conclusion using exact arithmetic, validated interval enclosures or a proved error bound.
   Cover relevant errors in input representation, object construction, truncation and numerical evaluation.
   Higher precision, repeated runs and different algorithms can guide diagnosis but do not alone supply a certificate.
4. Explain why the verified instance contradicts the original assertion at its stated scope.
   One admissible finite witness can refute a universal assertion that includes it; a finite approximation to an infinite-dimensional or limiting assertion needs a justified connection.
   Preserve the witness, certificate and verification method, and apply the existing [proof-review](proof-audits.md) and [Claim assessment](claims.md#separate-assessment-fields) rules before recording the target as refuted.
   If verification is incomplete, retain the missing obligation and next useful check.

For illustration, suppose the assertion is that a finite Hermitian matrix \(A(\theta)\) is positive semidefinite for every admissible \(\theta\).
A computed minimum eigenvalue \(\widehat\lambda\approx-10^{-14}\) is a candidate anomaly when its error is uncontrolled.
Its small magnitude alone proves neither negativity nor a rounding artifact.
A rigorous bound for the actual matrix at a verified admissible parameter can establish negativity when
\[
|\lambda_{\min}(A(\theta))-\widehat\lambda|\leq\varepsilon,
\qquad \widehat\lambda+\varepsilon<0.
\]
An enclosure containing zero leaves this sign check inconclusive; it does not establish positivity.

A simpler certificate may be an explicitly specified nonzero vector \(v\) with \(v^*A(\theta)v<0\), established exactly or by a validated strictly negative upper bound.
For example, components with exact rational real and imaginary parts chosen near a numerical direction can be tested against the actual matrix; the vector need not be an exact eigenvector.
This certifies failure of positive semidefiniteness without computing the full spectrum.

## Record Template

Use the inert [README template](../templates/computation.md), replacing placeholders with actual evidence and omitting example files that do not exist.
Record unavailable reproduction details explicitly.
A template is neither authorization nor a completed record.

## Computation index

mathematics/computations/index.md manually links retained J groups or registered supporting scripts, with a short finite/exploratory scope drawn from the responsible entrance.
Link an associated C/U or other mathematical record only when it exists.
The agent changing the group updates its entry; results and limits stay in J or the responsible material, and exploratory J requires no invented C/U.

Check newly produced or changed mathematical output at its actual input and parameter scope.
Reuse prior checks for unchanged applicable results; ordinary Git delivery does not request a historical rerun or full regression.
A failed or partial calculation remains failed or partial in its responsible record.
