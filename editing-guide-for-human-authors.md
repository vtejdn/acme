# Editing Guide for Human Authors

Declared: 2026-09-14T16:37+08:00.

This guide identifies files that should be preserved or maintained through the research workflow, and working sources suitable for direct human editing.
See [About](about.md) for the human and agent roles in the research framework.
"Protected" means unsuitable for ad hoc manual rewriting; it does not remove the author's authority to decide a correction.
The same requirements to preserve history apply to agents.
This document declares editing boundaries and adds no filesystem restrictions, hooks, or approval mechanism.

Apply the [agent/tool responsibility](framework/rules/workflow.md#agent-and-tool-responsibilities) to content retention, version changes, source identity and actual review scope.
Optional writers and focused checks handle explicit fields, locators and byte operations; no parser or PASS certifies unchanged mathematical meaning.
For the general introduction and ordinary use, see the [user manual](user-manual.md).
The [collaboration boundary](framework/rules/identity.md#collaboration-maintenance-and-conflicts) permits routine administrative repairs across authors while preserving substantive mathematics and captured provenance.

## Protected files and records

Paths below are relative to the repository root.
A directory pattern applies to its files whenever they exist; it does not imply that cross-repository intake has already occurred.

| Files or data | What to preserve and how to change it |
| --- | --- |
| Fixed C/T/R/L/U materials | Preserve the actual statements, arguments, decisions, original author/UID, inspection facts and useful failed history. Substantive changes create the appropriate next mathematical version; unchanged-mathematics decisions append at the responsible C/T home. |
| Original received materials | Keep original author, repository UID, captured source path/revision and acquired scope. Routine administrative locations and same-object links may be repaired with original mathematics and provenance preserved. Write substantive local judgments and feedback in your own responsible material; matching author keys grant no substantive edit right. |
| `intake/<initiator>/*.json` | Preserve actual original/transport provenance, recorder, selected scope and acquired/unavailable outcomes. Truthfully correct necessary facts; no receipt, current-use register or generic edit reminder is required. |
| `execution/Author_E_SERIAL.md` | Keep necessary actual authority, observations, stops, Task adoption and authorized resumption at the one stable E. Direct editing or the optional execution writer supplies facts; tools cannot authenticate instructions or evaluate custom-policy prose. |
| mathematics/claims/index.md, tasks/index.md and strategies/index.md | Derive needed navigation from authored decisions/routes and explicit acquisition provenance. Correct the responsible decision/route first, never status or priority solely in the index. |
| Historical review facts | Preserve what was actually checked, by whom, at which scope/date and with what result. Remove persistent mathematical digest values and byte-binding requirements; preserve literature-PDF and intake source fingerprints in their responsible provenance. |
| repository/.lock | Let tools manage the existing short publication lock; never delete it to bypass a running operation. Retired object, transaction, record/version and catalog stores are not authoring interfaces. |
| mathematics/literature/pdf and its declared external source mount | Preserve original PDF/HTML/resource bytes and record actual chosen associations/limits. Do not include the mount in broad cleanup; explicit source changes follow the literature rules. A new digest or file presence does not identify a work/edition. |

See the [research record rules](framework/rules/records.md), [review rules](framework/rules/proof-audits.md), [execution rules](framework/rules/execution.md), and [PDF storage boundary](framework/rules/literature.md#local-pdf-storage).

## Working sources suitable for direct human editing

| Location | Suitable human edits | Boundary to retain |
| --- | --- | --- |
| `mathematics/manuscripts/**/main.tex` and included `*.tex` files | Rewrite exposition, notation, definitions, proofs, introductions, abstracts and document organization. | Follow the adopted writing conventions. Changed hypotheses, conclusions or substantive proof arguments must also be reconciled with the responsible Claim and review records. A TeX edit alone does not update their mathematical status. |
| Manuscript `*.bib` files and editable figure sources | Correct typesetting entries, captions, diagrams and presentation. | Keep citation keys and bibliographic fields consistent with the canonical [references.bib](mathematics/literature/references.bib). Original-artifact and source-version facts continue to use their responsible [literature registry](mathematics/literature/registry.md) accounts. Edit figure sources rather than generated output. |
| Manuscript project/document notes and editorial selections | Record writing plans, intended scope, terminology choices and editorial comments. | Preserve recorded user decisions, provenance mappings and the scope of previous manuscript reviews; describe later decisions as later decisions. |
| Working D/S text, definition sources and newly prepared fixed material | Develop arguments, questions, definitions, examples, counterexamples and research routes. | Keep identifiers stable during their applicable use, preserve anchors and historical alternatives, and retire a D only after its necessary content and consumers move to responsible fixed homes. Fixed support files require the version/review workflow below; an index or a retained historical proof is not a free-form draft. |
| J programs, necessary original inputs and authored text in `mathematics/computations/programs/` | Develop calculations and reproduction instructions; correct or condense inspection prose in its existing responsible material. | Check changed calculations before claiming results. Retain useful inspection facts and actual author/origin identity, and repair references. Meaning-preserving edits follow the [common maintenance boundary](framework/rules/records.md#substantive-material-retention), with no generic change reminder, acknowledgment or new mathematical version. Substantive changes retain their actual reproduction/review duties; separately fixed evidence and acquired originals keep their preservation boundaries. |
| Regenerable J output in the ignored `mathematics/computation/outputs/`, including needed troubleshooting logs and useful continuation checkpoints | Regenerate, overwrite, relocate or remove them with coherent consumers. | Keep the program, necessary inputs, decisive parameters and usable reproduction command. Preserve inputs, witnesses or certificates with an actual mathematical role; no output archive or per-run report is required. |
| Own local derivations from received material | Record an actual new argument, limitation, method case or successor with precise source formulation. | Preserve the original acquisition/provenance and received bytes; local feedback is complete without rewriting the source or waiting for its author. Another source update uses its own authorized acquisition scope. |
| `about.md`, `ai-disclosure-for-human-authors.md`, and this guide | Improve the human-facing description and author guidance. | Keep statements about responsibility and implemented protections accurate; prose edits alone do not implement a new mechanism. |

The [manuscript and writing rules](framework/rules/writing.md), [definition rules](framework/rules/definitions.md), and [computation rules](framework/rules/computations.md) provide the relevant details.

## Files for deliberate framework maintenance

These files are editable when maintaining the framework, rather than as ordinary manuscript or research prose:

| Files | Maintenance boundary |
| --- | --- |
| `scripts/`, `.gitattributes`, and `.gitignore` | Preserve validation, exact-byte storage and external-directory boundaries. Check the affected behavior after changing it. |
| `repository/config.json`, `repository/people.json`, `framework/`, `profiles/`, and directory entry files | Keep repository identity, rules and recorded user decisions consistent. Preserve actual mathematical, review and execution decisions. Current personal/manuscript choices state only the current rule and applicable scope, without adoption timelines or administrative logs. |
| `.git/`, including `.git/config`, and any `.codex/` or `.agents/` configuration | Use the appropriate Git or application workflow for maintenance. Normal authorized Git configuration, commits, pushes and tags are supported; internal object databases, references and permission records are not research documents to rewrite manually. |

## When a human edit changes registered material

A newly prepared working text can be editable while its older fixed mathematical versions remain preserved.
Inspect the actual selected C/T decision, fixed input/review locators, material identity and acquired-source header.
These determine the responsible scope; there is no current-record manifest or separate hash registry defining mathematical authority.

First inspect the actual diff under [Navigation and Artifact Maintenance](framework/rules/proof-audits.md#navigation-maintenance).
Meaning-preserving wording, spelling, layout and links to the same input are maintained in place.
Retain material and C/T versions, mathematical selections and review assessments.
Do not publish, request a new review or create a formal correspondence artifact solely for changed bytes.
Shared harmless edits cause no automatic publication cascade.

A changed sign, quantifier, hypothesis, conclusion, substantive proof or actual theorem input follows the fixed material-version workflow.
The agent reconciles affected arguments and review scope, adopts actual material decisions, and checks direct consumers; derive navigation when needed.
S and D remain rolling material; D addresses are stable during use and reusable only after retirement and consumer repair: update their owned fields and retain meaningful dated history without minting fixed versions or hashes.
A genuinely different route can receive its appropriate successor with preserved lineage.
Received originals keep their captured mathematics and provenance; routine administrative repair follows the collaboration boundary, while author-key equality grants no substantive edit right.
Judge mathematical meaning rather than diff size.
Ordinary local development within the assignment needs no repeated owner permission.

Task objectives, scope and lifecycle in `mathematics/tasks/*.md` remain research contracts.
Record an actual new decision through the existing Task workflow instead of silently changing a completed contract, its authorization or its history.

Generated PDFs and build files under `mathematics/manuscripts/`, `.generated/` output, caches and disposable operational files in `.tmp/` are not primary authoring sources.
Ordinary mathematics uses D/J and its other responsible materials directly; `.tmp/` is limited by the [temporary-storage rule](framework/rules/organization.md#temporary-storage).
Git ignores these local files and the literature PDF store; the repository tag does not back them up.
See [.gitignore](.gitignore) for the exclusions.
These editing declarations rely on the documented workflow and validation; they do not claim that the operating system or GitHub prevents every direct edit.
