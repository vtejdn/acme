# Research Strategies

## Autonomous Strategy Management

Within an authorized research goal, agents may **add, revise, split, merge, reprioritize, pause, and restart strategies autonomously**.
Do not wait for a separate user request or approval for these ordinary methodological decisions.
A `proposed` strategy is a research candidate, not a request awaiting permission; an agent may activate it when there is a justified next step within scope.
Explicit user constraints continue to govern.

Subagents exercise these methodological choices within their delegated scope under the main agent's [research coordination](workflow.md#records-review-and-handoff).
They may request suitable parallel work through ordinary coordination messages; the main agent adjusts assignments, dependencies, resources and overlapping writes without a fixed role hierarchy or one-to-one agent/S/D assignment.
A Preparation subagent may continue the same Draft's research when its assignment includes that work or is extended, without a replacement agent, copied Draft or handoff report.

Initial priorities for strategies and substrategies are a starting allocation.
Once exploration begins, agents may freely adjust them according to actual findings, obstacles, expected effort and available resources, without first exhausting the initially preferred route or seeking separate approval.
An initial ranking alone is not a continuing constraint; an explicit user requirement to keep a priority or sequence fixed remains binding.
A priority adjustment needs no new mathematical result, S identity or version: update the affected rolling S and briefly record the allocation reason under the ordinary rules below.

This authority concerns methods and work allocation.
It does not authorize changing the goal's target, quantifiers, completion criteria, or scope beyond the existing authorization.
Strategy dispositions are independent of goal states: pausing a route does not pause or complete its goal, and restarting a route does not activate an unauthorized goal.
A route change does not promote a conjecture or proof draft to a proved claim.

The [result-organization policy](claims.md#lemma-extraction-and-approval) permits internal extraction and proof/dependency organization within an assigned Task without separate approval or lemma labels.
Route management preserves the original objective, actual mathematical review and main-theorem/objective authorization boundaries.

<a id="writable-route-boundary"></a>
Route revisions and predecessor-disposition changes below apply to local writable materials.
Route body maintenance belongs to the same established human under the [collaboration boundary](identity.md#collaboration-maintenance-and-conflicts); other humans contribute through their own materials and references.
Publish a substantive contribution under its responsible human's own material identity with exact links, and apply the actual conflict procedure when needed.
When deriving a local successor from a public source material, record the precise source revision or identifiable formulation and the obligations actually carried in the local successor.
Do not change the source route's disposition, priority or history.
A public source material is not writable for local feedback solely because its author key matches the operator.
Explicit references make local derivation discoverable in reverse navigation without implying source-owner adoption or supersession, waiting for a response, or requiring remote synchronization.
The source owner may later adopt the contribution through a real revision.

| Operation | Agent action and required record |
| --- | --- |
| Add | Allocate the next unused route ID, link the authorized goal, and state the mechanism, its relation to the goal, inputs and next discriminating step. Set `proposed` or `active` according to the actual work decision. |
| Revise or reprioritize | Keep the ID when the route retains its mathematical identity. Update its scope or next step explicitly, preserve earlier failures, and explain the evidence or allocation reason for the change. A materially different mechanism or target gets a new route ID. |
| Split | Allocate IDs for the distinct successor routes. For local writable predecessors, link predecessor and successors in both directions; keep the original active only if it retains a distinct coordinating role, otherwise mark it `superseded`. For a public source predecessor, link the precise source only from the local successors and preserve its disposition. Record which successors actually carry each unresolved obligation. |
| Merge | Normally create a new route for the combined mechanism and mark local writable predecessors `superseded`. A local writable ID may absorb another local writable route when its mathematical identity remains intact; record the absorption and mark the absorbed route `superseded`. A local combination using a public source route records its source and carried obligations without marking that source absorbed or superseded. Preserve all relevant evidence, failed attempts and unresolved obligations. |
| Pause | Set `paused` when work is intentionally deferred for priority, resource allocation or sequencing. Record the current result, unfinished obligation, reason for pausing and a useful reconsideration condition. State whether the hold includes subroutes. |
| Restart | Return a paused route to `active` when priorities or available resources justify it, recheck its dependencies and record the next action. No new theorem or external evidence is required for this allocation decision. Apply the stricter evidence conditions below to blocked, refuted, completed or superseded routes. |

Use a short dated entry in each affected local writable route's evidence/change section: acting agent, operation, previous and resulting disposition, reason, related route IDs, and outstanding work or next action.
For a local derivation from a public source route, record the source relationship in the local route instead of editing the source.
Link substantive mathematical evidence from the ledger or audits instead of duplicating it.
Do not create a separate approval checklist or require a new audit merely for route administration; mathematical claim changes retain their existing review requirements.

Each route material owns its disposition, priority, Task associations and next step.
Update the actual S material and regenerate the derived route index.
Preserve meaningful predecessor history and cited mathematical locations during split/merge.
Coordinate same-family edits and allocation among concurrent agents.
If every current route is deferred, name the next selection/reassessment step rather than silently changing Task lifecycle.

<a id="strategy-hierarchy"></a>
## Main Strategies and Substrategies

Strategy and Substrategy are roles of the same rolling S material.
The Task owns the exact question and authorization.
A main Strategy explains one coherent mechanism, its major remaining obligations and why its branches are alternatives, jointly needed components, or a mixture.
A Substrategy owns a concrete approach, local uncertainty, next discriminating action and disposition.
Neither the parent nor navigation copies the child's proof or running history.

Use a distinct S when an approach can usefully be selected, compared, assigned, paused or abandoned independently.
A calculation, lemma or local repair within the same mechanism normally remains in that route and its responsible evidence.
Keep the hierarchy shallow unless another level expresses a real research choice.
New notation for an equivalent question is not by itself another mechanism or mathematical progress.

The child declares at most one current `parent` row in its designated `## Route` table.
Its value is one Markdown link to the exact writable local S and an existing stable anchor.
Omit the row for a root; do not use an empty placeholder or root flag.
Self-parenting, duplicate rows, cycles, another material kind and unresolved or ambiguous local identities are invalid.
Examples in literal or excluded regions are not declarations.
Reverse children and Task entrances are derived from the child declarations, not a separate manual registry.

The parent is current organization; a predecessor is historical lineage.
A historical split or matching title, Task, line or serial does not establish a parent.
Reparenting preserves identity and records a concise dated organizational change.
Cross-route and cross-Task reuse uses precise references rather than additional parents.
Each child retains explicit Task associations and the exact scope served, including any additional Task.
Public source Strategies remain at their original repository/revision/path; a local adaptation uses its own S and an explicit source reference.
S is not an acquired material kind.
Needed external S mathematics may be explicitly adapted by intake into an appropriate fixed receiving home, preserving its actual source scope.
An S associates with an ordinary individual Task, never directly with a joint coordination T.
For a shared goal, use the actual relationship joint T to individual T to that individual's S, compare collaborators' usable routes and failures, and choose useful diversity without forbidding replication.

Ordinary child selection is covered by the existing Task authorization.
A parent link cannot activate an unrelated Task, expand its contract or resume a stopped execution run.
Pausing a parent states whether its children are also paused and updates their actual local dispositions when so; a branch continuing for a separate authorized use states that scope.
Completion and refutation never propagate by counting children: completing the parent requires the actual assembly and completion check, and failure of an auxiliary child need not refute the parent or Task.
A completed source route may be reused without reopening it.

Partial navigation shows an omitted parent as an external context link when available and does not turn it into a new root assignment.
A partial reverse child list does not claim completeness.
Public source references remain explicit repository/revision/path locators; malformed local locators remain errors.

## Identifiers and Files

- Choose and author the rolling S under the [agent/tool responsibility](workflow.md#agent-and-tool-responsibilities).
  The optional `material.py create --kind S --line F --file route.md` writer, or `--task PATH` inheriting only an actual Task's letter, allocates an independent author/origin/S/line numeric sequence, growing from F9999 to F10000.
  No global counter or index reservation owns allocation.
  Preserve the original author and never recycle an allocated identity.
- Local routes use `Author_S_F0001.md`; public source Strategies retain their original repository, fixed revision, path and anchor in the reference.
  They are not installed under a recipient filename.
  Title, priority and associated Task changes do not themselves change identity.
- Put exact Task path/anchor and scope in `## Task associations`; `## Route` owns disposition/priority.
  Link Claims and fixed source inputs precisely.
  A common number/line or filename never implies a Task association.
- Keep the route concise and link full proofs, computations and reviews.
  Its own fields govern route navigation; a derived index row cannot change them.

### Rolling-Document Regime

A strategy file is a rolling document, not a versioned material: it never mints a `name_vN.md` version file.
Keep the same S identity while the core mechanism and intended contribution remain the same.
A new estimate, repaired construction, revised auxiliary parameters or substantial progress does not by itself require a successor.
Update the current question, allocation and next step in place while retaining meaningful earlier failures, expectations and consequential decisions in dated history or linked responsible evidence.
Identity and locator maintenance uses verified current identities without changing historical mathematical meaning.

Allocate another S for a materially different mechanism or independently managed branch, not successive improvements of the same route.
At a consequential split or redirection record the date at its available precision, earlier formulation, what is retained or rejected, and obligations actually carried.
A predecessor is not the previous edit of the same S and does not assert that its current rolling body equals the earlier formulation.
Preserve a cited historical location; if the actual formulation is unavailable, state that limitation.
A short history entry and precise evidence links normally suffice.
Use an available Git revision or captured evidence when exact earlier bytes are needed; ordinary maintenance needs no snapshot, hash, receipt or per-edit archive.
Mathematical reliance cites fixed arguments with their actual hypotheses, not a rolling predecessor as proof support.

Ordinary edits require no hash registration or separate maintenance report.
A split or merge preserves meaningful lineage in the routes and maintains affected derived navigation through ordinary bounded edits or optional rendering.

## Choosing and Revising a Route

When selecting or materially redirecting a route, search existing Claims, arguments, source audits, constructions, related strategies and failed attempts by the conclusion and problem features actually needed, under [knowledge reuse](knowledge-reuse.md#reuse-before-proof).
Explain consequential reuse at the consuming route: local objects and parameters, satisfied and missing hypotheses, actual output and remaining gap.
Preserve losses and order of choices when they matter.
A simple application can need only one sentence; no separate application record or reciprocal feedback workflow is required.

When several families repeat the same realization or normalization problem, compare a concrete shared construction with the family-specific obligations before allocating work.
Check the complete objects, boundary cases and unused scope of already retained sources.
Similar matrices, scalars or finite coefficients do not establish a structural realization; one campaign supplies experience, not a universal ordering or success rate.
Before assigning finite verification, identify every unbounded parameter and prove that the proposed bounds close all directions.
A bound at each fixed auxiliary layer may leave an infinite family.

Apply the [work-obligation rules](workflow.md#work-obligations).
An exploratory route may state a current question, a mechanism to test and provisional parameter or hypothesis choices; identify what remains to be determined instead of inventing a complete proposition.
When the route undertakes a proof of a particular assertion, state that assertion, hypotheses and quantifiers precisely.
Distinguish an established necessary, sufficient or equivalent relationship from a partial target or heuristic association, and link the justification for any claimed implication or equivalence.

Identify verified inputs separately from conjectural dependencies and unchecked applicability.
Conditional exploration may proceed using those explicitly marked premises without registering or resolving every tentative subclaim first.
State the current uncertainty or obstruction and the next discriminating step: a calculation, candidate assertion, example, or source check whose outcome can change the route's assessment.
Give explicit conditions for continuing, redirecting, or reopening the route.

A concrete obstruction or promising external mechanism can trigger autonomous literature search under the [repository search policy](literature-search.md#autonomous-literature-search).
Specify the question and how possible findings would affect the route.
Link consequential search evidence from the relevant ledger entry or source audit, and identify any new lead that justifies expansion or reopening.
Repeated searches with no useful new evidence call for reassessment; stopping a search does not refute the route or discharge an unresolved dependency.

At a consequential redirection or stage closeout, compare the dated expectation with the actual result, explain the discrepancy and its effect on the next decision.
A retrospective synthesis carries its actual date and cannot imply it was consulted earlier.
Complete attempts, calculations and proof arguments remain in their responsible materials; a stable mechanism or lessons section can retain concise reusable experience with exact evidence.
Independent substantive synthesis belongs in appropriate ledger material only when worth preserving separately.
For a received source, record the precise source formulation, applicability and necessary evidence in local writable material; no source amendment or response is required.
Routine actions need no retrospective, and failure of a sufficient construction does not by itself refute its Task.

<a id="route-dispositions"></a>
### Dispositions and Restart Conditions

| Disposition | Meaning and condition for changing it |
| --- | --- |
| `proposed` | A candidate mechanism not yet selected for execution. Activate autonomously when it offers an in-scope next step. |
| `active` | Selected for current work, including a coordinating route with active subroutes. It need not have a tool or agent running at every moment. |
| `paused` | Intentional deferral. Resume for a recorded priority, sequencing or resource reason after checking the current context; the underlying mathematics need not have changed. |
| `blocked` | A named unmet prerequisite prevents the planned next step. Resume when that prerequisite changes, a justified alternative bypasses it, or the earlier diagnosis is corrected. If investigating the missing lemma is itself an executable next step, its being unproved alone does not require a blocked disposition. |
| `completed` | The route's stated deliverable is achieved with the required evidence. Reopen the same route if a concrete challenge reveals an unmet completion obligation; broader follow-up work normally gets a new route. Route completion need not complete the goal. |
| `refuted` | Evidence rules out the recorded mechanism or auxiliary assertion under its stated hypotheses. Reconsider only with a concrete change in evidence, assumptions, mechanism or diagnosis. Preserve the failed assertion; it remains refuted unless its refutation is overturned. A materially different replacement gets a successor ID. |
| `superseded` | Work has been reorganized into identified successors or absorbed elsewhere. Keep the historical record and successor links. Restore the same ID only when deliberately reversing that reorganization while reinstating the same route identity; reconcile successor dispositions to avoid duplicate active ownership. |

Record the scope and evidence of a failure in the ledger.
Failure of a sufficient strategy does not refute its goal.
A **goal counterexample** requires a verified example contradicting the original goal under its actual hypotheses, with the relevant claim and proof review linked before the goal's assessment changes.
Do not confuse an allocation decision to pause with evidence that a strategy is blocked or refuted, or treat restarting work as proof that an earlier mathematical objection is resolved.

## Record Template

Use the inert [record template](../templates/mathematics/strategy.md), replacing placeholders with actual evidence.
A template is neither authorization nor a completed record.

When a useful failed attempt changes a route or prevents repetition, fix its scope, evidence and limitations in ledger without waiting for Task completion.
Link that finding from the route evidence/change section and explain its consequence for continuation or reopening.
Keep ongoing unbound arguments in mathematics/drafts/; strategy decisions remain in this rolling record.

## Strategy navigation

The existing renderer derives mathematics/strategies/index.md from S Route declarations and actual source/feedback relationships: route identity/title, parent hierarchy, Task association and route disposition.
S and the exact linked T/evidence own those meanings.
After relevant inputs settle, maintain affected navigation through ordinary bounded edits or optional rendering, including populated generated rows.
Preserve route values, exact links and source facts; changing the index cannot change the responsible S, T or evidence.
