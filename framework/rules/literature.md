# Literature Rules

All fixed L reading notes and mathematical supplements belong in mathematics/ledger/, using the single author/line L sequence.
The optional writer `material.py create --kind L --line W --file -` uses the actual line.
Source audit directories contain U and navigation that may link L; no alternate L home or --source-key placement exists.
A U remains a precise source-local audited input, with its edition, passages and actual inspection scope.
Apply the [agent/tool responsibility](workflow.md#agent-and-tool-responsibilities) when choosing a work, edition, holding or source association.

Literature intake and source audits exclude associated Lean code unless its audit is explicitly requested; follow the [default audit scope](literature-audits.md#default-audit-scope) when a source includes formalization artifacts.

<a id="source-preparation"></a>
## Common source preparation

Research, source audit and writing use the same sequence: search existing mathematical/source evidence; register any missing work and exact artifact/edition; inspect the needed passages; process definitions, terminology and symbols through [def registration](definitions.md); then reuse the source within its actual limits.
Canonical references.bib owns bibliographic identity and keys; the registry owns artifact/version, availability, acquisition and coverage links; intake owns actual cross-repository operation provenance.
Prepare searchable contents when the source supplies them, and state unavailable editions or indispensable passages specifically.
Keep complete definitions in adequate U/C/L content, source findings and presentation observations in adequate source-reading accounts, and writing choices at their applicable profile or manuscript home.
Reuse adequate inspected evidence without inventing equivalence, expanding coverage or requiring a full-paper proof audit for stylistic or bibliographic use.
Follow [progressive reading](#progressive-reading) and the [source-audit rules](literature-audits.md) at the depth needed for the actual use.

<a id="bibliography-content"></a>
## Bibliographic content

Canonical and manuscript-subset BibTeX contain actual authors, title, publication/edition identity, venue/publisher, dates, pages/article numbers, identifiers and legitimate public source URLs.
A concise `note` may explain publication, language, version/edition uncertainty or a meaningful bibliographic exception.
It is not an acquisition log, source/proof-review verdict, Task progress account, local path/configuration, byte-fingerprint register or execution report.

Keep source acquisition and artifact facts in the literature registry, actual cross-repository operation provenance in intake, and inspected mathematics/applicability/limits in U or the responsible source record.
Remove duplicate workflow prose; transfer a genuinely unique needed fact to its proper existing home before removing it.
Read the content rather than classifying notes by English keywords.
Preserve stable keys, true publication fields, actual uncertainty and necessary `alpha-year` identity exceptions.
Registration/intake and typesetting subsets follow this same boundary; copying metadata does not authorize copying process prose.
No new download or proof audit is implied.

<a id="local-pdf-storage"></a>
## Local Source Storage

Source PDFs and original HTML use the Git-ignored logical path mathematics/literature/pdf/.
PDFs keep their flat filenames; HTML pages and explicitly retained related files use a directory named by the established work key.
The entrance is an ordinary directory or one top-level directory junction; symbolic links and nested linked paths are unsupported.
All PDF, original HTML and resource files in this store are local only, excluded from Git/GitHub and unavailable for acquisition by another repository.
Keep links relative to that entrance; another checkout or storage target does not change source identity.
Necessary persistent physical targets belong only in the responsible human's ignored `profiles/<human>/secrets.md`, under the [private-setup rule](organization.md#machine-local-locators).
Concrete source access and file/group maintenance resolve the actual mount; public records keep logical relative locators.

The mount supplies source access, not repository-owned output space.
General repository scans, copies, cleanup, publication snapshots and generated navigation must not descend into it.
Never clean a workspace by recursively deleting or moving through a junction.
Before a source acquisition or explicit file/group maintenance operation writes there, resolve and verify the physical destination, its scope and the applicable existing authorization.
That permission does not extend to sibling directories in the external store.
Current storage checks are read-only and do not reconnect a broken junction, download missing sources or alter source bytes.

An explicit `python scripts/check-literature-storage.py` invocation requests whole-store registered-artifact inventory: actual target, format/decoding facts, recorded limitations, known SHA-256 fingerprints and Git exclusion.
The agent selects any needed [source-check scope](#selected-source-checks), preserving unrelated accounts outside that selection.
Local registration, explicit source reading and public U display use the actual selected declarations and necessary direct relationships.
An unrelated malformed account is not a prerequisite for a selected operation; an explicitly requested whole-store inventory still checks its complete scope.
Competing declarations or several possible primary artifacts require the agent to inspect the concrete candidates and supply chosen facts or a local account edit, rather than accepting the first or last link.
Generic public links into the logical source root, groups or named files check normalization, repository containment and protected paths without resolving the mount or checking source existence, format or native anchors.
They do not audit holding, edition or source bytes.
The sole artifact registration source is mathematics/literature/registry.md; rule examples and other Markdown files do not register artifacts.
Each primary artifact has an explicit account; selected additional pages/resources carry their own locators and fingerprints where known.
Its one `Artifact:` declaration names one exact local Markdown target; its single known fingerprint uses `SHA-256` followed by the inline-code hash on that same line.
Ordinary comparison/dependency/contents links, unlabelled links, retained-artifact prose, a sole Resource and the first hash elsewhere declare no primary artifact or fingerprint.
`Resource:` and a holding's source-artifact field are explicit relationships, independent of the related artifact's own primary account and facts.
Related resources without an Artifact account remain relationships, with actual local availability reported separately and no implied acquisition.
Register an additional edition explicitly.
Ambiguous declarations need correction; a hash alone does not establish source identity, and an unavailable expected artifact need not have one.
Current source fingerprints belong here, not in duplicate U/readme inventories.
Retain necessary version-specific mathematical findings and actual review scope without keeping superseded source-byte inventories or implying that current bytes were an earlier review's input.

PDF reading uses flat filenames directly below the declared entrance, such as `mathematics/literature/pdf/<key>.pdf` or an existing version-suffixed filename.
PDF filenames start with an ASCII letter or digit and otherwise use letters, digits, underscores, hyphens, periods and the literal ASCII plus sign.
Grouped PDFs, unsupported filenames and malformed declarations are errors; the registry must not silently omit them.
Original HTML and explicitly registered related files are the contained group exception described below.
Nested junctions/file links, path escapes, cross-work substitution and attempts to publish this ignored source storage as Claim/Task/J material are rejected.
Publication checks both the input path and its resolved target, including excluded directories.
Whole-repository traversal skips the entire mount before descent.
An unavailable registered source page/PDF/resource is a nonblocking availability notice, separate from an invalid format/path or an actually missing required mathematical input.
No acknowledgment, bypass flag or read-triggered download is needed.
Never-obtained local artifacts have no fingerprint or fictional acquisition; retain an actually established local baseline if that file later becomes unavailable.
Availability says nothing about mathematical verification.

<a id="selected-source-checks"></a>
### Agent-selected source checks

The agent reads the actual change and responsible materials, chooses any needed source keys or artifacts and reuses adequate still-applicable judgments.
An edit, commit or push does not by itself require a new source check; no scope file, acknowledgment or mandatory command sequence is added.
Generic submission checks ordinary public references, logical path containment and private-source tracking boundaries; it does not reconstruct holdings, validate source accounts or inspect private source bytes, fingerprints, formats or native HTML anchors.
For an explicitly chosen relationship check, reuse the shared reader with the selected holding keys or artifact names from the complete registry and bibliography of the actual requested WORKTREE, INDEX or commit postimage.
A holding selection includes that key's unchanged genuine holdings and their directly referenced Artifact accounts, retaining real competition while excluding unrelated malformed accounts.
Text diff fragments and an unstaged repair cannot replace the selected view's necessary declarations.
The reader checks explicit fields, contiguous tables, registered references and numerical page/range constraints; the agent judges identity, edition, completeness and mathematical suitability.
Public U display enriches the structural material with its local holding facts through the same reader; an ordinary material check performs no such enrichment.
Use the existing [selected-view interfaces](../../scripts/readme.md#explicit-selected-source-reading) when mechanical help is useful.
Acquisition, registration and explicitly requested byte or whole-store checks retain their actual physical-file scope; ignored source bytes are not contents of an INDEX or Git commit.

<a id="artifact-source-association"></a>
### Artifact source association and availability

The agent establishes the needed work, edition and association from the actual bibliography, source and inspection facts.
Tools fetch only supplied addresses and report requested/final addresses and bytes; they do not interpret URLs, canonical editions, filenames or U prose to choose identity or a fallback.
For an unestablished response, inspect the returned object before registering the local file under the chosen work/edition.
Reuse adequate existing judgments within their actual scope without a confirmation field or repeated approval.

Byte input is the file explicitly supplied to the operation.
An existing work key chooses bibliography, not a local artifact; neither a missing input, matching suffix nor target fingerprint selects local bytes.
To reuse an actual local file, pass it through the existing PDF, HTML or resource file argument with its actual source facts and limitations.
With no supplied bytes, a free destination records truthful unavailability without a fresh fingerprint; a selected existing absent artifact retains its already recorded local baseline.
An occupied destination reports an address conflict and preserves its existing bytes/account instead of substituting that file or rewriting its provenance.
Pure bibliographic updates do not create an artifact acquisition.

Each primary artifact's existing registry account owns its current selected addresses, actually obtained addresses, necessary edition facts and known limitations.
`Selected source URL:`, `Source URL:`, `Source version:`, `Source association:` and `Current access limitation:` state these literal facts; complete URL values, including parentheses/query text and multiple declared addresses, remain unchanged through local readback and maintenance.
Old `Retrieved` or `Source:` prose declares no current address/edition and is not promoted into these fields.
An undeclared fact is unknown, independently of file availability and known byte fingerprints; reading neither invents a missing-file notice nor rewrites the old account.
The agent handles any actually needed historical fact at its responsible home.
Ordinary comparisons and dependency links select no source.
Local readers and storage display preserve recorded limitations rather than deriving a source verdict.

For a change to an existing account through local registration, read its actual Artifact declaration, current facts and comparison, contents or holding context, then prepare the necessary expected-text edits or expected original text with prepared final text.
Explicit source facts are literal inputs; the agent decides which are current or superseded and retains necessary unrelated content in the prepared result.
The writer requires this preparation when existing prose changes, rather than selecting a first link, merging accounts, stripping prefix-matching prose or appending a fallback account.
An unchanged byte/fact operation may preserve the account as a no-op, and an explicitly chosen free account may render its minimal supplied facts.
Competing accounts require judgment from their actual candidate contents.
Before publication, the prepared selected account must be unique and its fingerprint and current facts must agree with the supplied inputs; local registration, selected catalog and local holding display observe those same persisted facts.
Check the exact expected old text before strict evaluation of the prepared result, so an explicit resolution can repair old ambiguity without selecting an old first/last candidate or borrowing a comparison fingerprint.
Use the [public local-registration inputs](../../scripts/readme.md#local-source-retrieval-and-registration) with the existing short lock, stale-input checks and rollback boundary.

Compute a new registered fingerprint only from actual locally obtained document/resource bytes, after the agent establishes the source association.
The sole registry's local baseline serves accidental-damage checking; comparison with different supplied bytes must preserve existing source bytes and baseline on failure.
Supplied or foreign hashes establish no local baseline, and authored-material intake obtains no literature fingerprint or sender-local integrity baseline.
If an old hash's local provenance is unknown, retain that uncertainty rather than inferring historical local possession.
Hashing an error page or unestablished response is at most a transient byte fact about that response, not the intended publication's registered fingerprint.
Local source registration preserves the responsible account's actual limitations; an original U retains its own authored inspection scope.
Neither a matching hash nor successful copying resolves identity, edition suitability or completeness.
Source availability is reported independently of those judgments.
Changing the local key/path for the same retained bytes preserves its actual baseline and consumers.

Retain selected addresses, edition facts and an actually established prior local baseline for unavailable outcomes, so an authorized later operation can explicitly retry the same address.
Never-obtained local artifacts have no fingerprint; no caller-supplied hash or prepared registry update may establish one without actual obtained bytes.
Update current availability at the actual returned artifact address and resolve a limitation only after the relevant fact or agent judgment is established; successful copying alone does not clear it.
Preserve necessary contents/holding links.
There is no automatic retry, conflict classifier, parallel source register or retry-history archive.

Local registration reports the obtained or unavailable result for each explicitly chosen PDF, original HTML page or resource.
An unavailable local source retains its declared locator, limitations and any previously established actual-local-byte baseline, independently of mathematical-material intake.
An unknown historical hash remains uncertain provenance and does not establish local possession or a local integrity baseline.
The agent determines the resulting limit on intended mathematical use at the actual consumer.
This differs from the authored-material copy's promised C/R/U/L bodies or indispensable J files, which must exist before that operation can claim to copy them.
Unsafe paths, invalid supplied formats, mismatching expected bytes and publication conflicts remain errors; no file suffix or resource-importance classifier decides necessity.

<a id="actual-source-holdings"></a>
### Actual holdings and complete contributions

An independently readable complete contribution inside a retained proceedings satisfies that paper's local holding.
Preserve its bibliographic key and U; do not require a redundant standalone PDF, invent a container work or infer coverage from a filename, title match or hash.
The sole registry explicitly associates the selected work/edition with the actual registered container and contribution range.
The artifact may already be registered under the contribution key; a container with its own bibliographic identity keeps that key.
Readers and source checks follow this association at their selected account scope.
Holding relationships belong to this repository's own local source account; U intake copies no source bytes, availability facts or holding relationship.

The agent establishes the actual work, edition, artifact and inspected extent or partial-source limitation, then prepares the declaration and necessary surrounding prose directly in mathematics/literature/registry.md.
Routine changes may use ordinary file editing; useful batches or shared publication may use the existing [exact text maintenance](../../scripts/readme.md#scoped-checks-and-bibliography-maintenance), preserving unrelated metadata and access/inspection qualifications.
No dedicated holding writer, JSON preparation file or confirmation receipt is required.
An unchanged holding needs no update or no-op invocation; ordinary reading preserves its complete account.
Metadata-only maintenance requires no source download, whole-store inventory or mathematical review.

Use one contiguous `Field | Value` table, with its delimiter and rows uninterrupted, in the work's registry account with `holding`, `source-key`, `source-artifact` (a link to the registered file) and `source-edition`.
Literal examples, orphan rows and disconnected fragments supply no holding or edition declaration.
`holding` is `selected source`, `complete contribution` or `partial source`, as established by actual source inspection.
A complete contribution also supplies `artifact-edition` equal to the selected edition, `contribution`, `printed-pages`, one-based inclusive `pdf-pages` and `artifact-pdf-pages`.
The preparing agent checks the complete contribution; the parser checks the association, not its mathematics.
A partial holding gives its actual `source-limitation`, including known gaps or unverified coverage.
A different edition, incomplete contribution or unavailable container retains its accurate limitation; it does not create a fictional standalone-file notice.
No second coverage registry is added.

<a id="original-html-sources"></a>
### Original HTML source groups

Retain selected HTML as original bytes and encoding under `pdf/<SourceKey>/`, with selected additional pages and needed resources beside it or in contained resource subdirectories.
The registry identifies each actual page/resource, known URL/revision/snapshot, current fingerprint, coverage and genuine resource limitations.
A directory alone proves no holding.
Preserve native source anchors, embedded TeX/MathML and formula-alt text; cite actual headings, labels and anchors rather than PDF pages.
An agent may read disposable decoded/extracted text.
No PDF conversion, durable Markdown reader, website crawl, script/style stripping or mathematical-content filtering is part of acquisition.
Substantive extraction belongs to an actually requested ordinary source audit.

Resolve each explicit file within its canonical work group and the declared mount; nested links and cross-group substitution remain errors.
Internal HTML URLs are source references, not authority to read arbitrary local paths or fetch resources.
The agent selects needed contained resources for ordinary local acquisition and inspection; no resource is transported through intake.
A bare HTML file with missing formula images is not a complete offline visual mirror.
Tools report byte length, decoding, titles/anchors and resource references without running source scripts or using login/error keywords as a source verdict.
The agent judges an empty shell, error/login page, dynamic body and actual completeness; obtain necessary resources or retain the resulting gap.

Use the [source-unit and verification format](literature-audits.md) when extracting reusable inputs.
A key such as `Miy22` identifies the work; a unit such as `Miy22-U001` identifies a specific audited input and is not another bibliographic entry.
Bibliographic checks, statement checks, and proof reviews are separate activities; the presence of a PDF or completed index row does not establish theorem-level verification.

<a id="writing-reference-collections"></a>
## Writing Reference Collections

Two dedicated collections support the [manuscript writing rules](writing.md):

- [Style models](writing.md#style-selection) are author-designated presentation exemplars.
  A style-only role supplies no prose-reuse instruction; follow the actual author's applicable policy or manuscript choices.
- [Community references](writing.md#use-and-reuse) guide terminology, notation and exposition.
  That role alone does not supply permission to copy or closely adapt prose, or select a fallback model for every author.

For [direct text reuse](writing.md#default-reuse-permission), an author's own/coauthored works listed in `profiles/<author>/writing/readme.md` supply default reuse of useful prose when writing for that author; no fresh manuscript designation or extra reuse flag is needed.
Any author, including one without a profile, may also designate further sources in the target manuscript's existing `writing.md` or `conventions.md`.
For example, the profile can list "My coauthored literature: source A"; a manuscript can specify "Reuse source B except Section 4; source C is style-only."
Use canonical keys/links and apply actual work/passage exceptions and subfield/manuscript overrides through the four writing layers.
No coauthor identity gate or repeated passage approval is added.

Keep concrete roles and choices at those existing policy homes.
The manuscript's `citation.md` separately records actual external citation applications and links to source evidence; it neither selects a writing role nor grants text-reuse permission.
The canonical references.bib owns structured bibliographic identity; the registry owns acquisition, artifact versions, availability, access classifications and scope links.
Being a writing exemplar does not establish mathematical verification or require a full source audit.

A newly retained writing-reference PDF belongs in `mathematics/literature/pdf/`, using the existing canonical filename and explicit version suffixes.
Record its actual location in the sole registry.
Explicit roles and reuse limits belong in the responsible author profile or manuscript choice; source-specific observations belong in adequate U or compact source-reading accounts, with complete definitions registered through def.
A work may serve several scoped roles with one artifact; reuse permission derives from its user designation and limits, never from relocation or note membership.

These are input-literature collections.
The existing rules for unpublished and restricted material still govern external disclosure, and the manuscript build-output policy is unchanged.
The current framework creates collection entrances, not an automatic selection of papers or permission to treat all literature as reusable prose.

## Literature Acquisition

The common acquisition norm applies directly within the actual authorized scope; it needs no project adoption record.

Choose the existing work key or explicitly new work and exact bibliographic field updates, and inspect prepared bytes outside the short shared-maintenance lock.
Search candidates and identifier/title differences are evidence for the agent, not automatic same-work decisions or field fusion.
Under the lock, reread those explicit inputs, allocate an unoccupied key only for the chosen new work and exclusively publish at the actual destination with truthful registry facts.
A stale choice reports observed changes for fresh judgment; no heuristic reconciles it.
Keep retrieval and judgment outside the lock.
Do not reserve keys, publish provisional artifacts, add a retry queue or rewrite existing consumers during routine registration.

For U intake, explicitly choose the bibliography target and authored source unit; the private document store is outside that operation.
For ordinary local source acquisition, retain an actual contribution/container relation rather than inventing a same-key standalone PDF; tools do not infer holdings from filenames, sole HTML files or arbitrary U links.
Distinct chosen artifacts keep separate destinations and availability/provenance facts.
A missing edition neither borrows another edition's status nor blocks an available chosen artifact.
Use the actual returned destination, preserve recorded partial-source limitations and reuse adequate unchanged bytes without download history.
Copying does not retrieve an unavailable artifact; an authorized retry is a separate explicit fetch and registration action.

Download and retain is the single acquisition norm: reuse an adequate existing local copy or obtain the selected artifact, validate it and register its logical relative path/version and acquisition details.
Online-only registration is not an equal mode; it survives only as an explicit exception registration for failed acquisition, recording the source URL, identified edition/version, access date and exact locator, an explicit no-local-artifact declaration and the failure record.
Record a failed download as an access limitation, never completed local acquisition.
An expected local locator may be recorded as unavailable; never claim retained bytes or invent a fingerprint.

The norm and every exception registration use the sole literature registry and the same source-applicability checks; acquisition does not certify mathematics.
Online-only entries registered before this norm remain valid historical registrations; reacquiring their artifacts is ordinary acquisition maintenance under the norm.
A scope change applies prospectively and does not authorize bulk retrospective acquisition.

Apply the [ACME material boundary](intake.md#scope-and-routing) before acquisition.
Other mathematical sources use this literature-input flow regardless of hosting platform.
A known ACME output retains its origin when published, mirrored or renamed.
Classify the selected material, not every file in its container.

Agents may autonomously download relevant literature publicly available at no charge within an authorized research goal, source study, or other exploration.
Routine downloads within that scope do not require repeated approval.
Use the root [autonomous literature-search policy](literature-search.md#autonomous-literature-search) for search triggers, expansion, and stopping conditions.

Before downloading, identify a concrete expected use: a proof input, candidate route, counterexample, or comparison relevant to the authorized work.
Check mathematics/literature/registry.md and existing files by bibliographic identity, DOI or arXiv identifier where available, and the required version.
Reuse an existing adequate artifact.
A different URL, filename, or byte encoding does not by itself identify a new work or justify retaining a duplicate.

Attempt a bounded public-source download with a timeout and finite retries as part of the actual operation, after reusing an adequate local copy.
A failure completes known bibliographic information and the actual acquisition/access account with the failure, known exact locator/edition, access date and unavailable artifact.
Acquisition-only failure creates no U and claims no source inspection; a never-obtained local artifact has no fingerprint, while an established local baseline survives later absence.
Link adequate existing U evidence without erasing its historical checked scope or treating the current access failure as a new inspection.
Retain new or revised U/C/L only for necessary substantive inspection content at its actual depth under the [common content decision](records.md#substantive-material-retention) and fixed-version rules.
A receiving inspection contribution uses its author's own evidence home rather than revising an acquired original.
Genuine online/partial-source inspection may coexist with a failed download; title-page or bibliographic identity checking alone is no theorem/definition/proof audit.
Failure does not block unrelated authorized work or create a queue, background retry or repeated attempts at each check.
Validate the retrieved artifact before recording successful retention: confirm its intended format, readable content, expected title, authors and version.
A file extension or successful HTTP response is insufficient; an error/login page, dynamic empty shell or HTML response saved with a PDF extension is not the selected mathematical source.
Preserve the actual retrieval URL and acquisition date, and compute the SHA-256 of each retained file.
Keep successful current provenance concise rather than retaining redundant retry/copy chronology.
For Git-hosted sources, include a known fixed commit or release locator when available; do not invent one or require repository cloning to retain a paper.
Mirror URLs do not create new bibliographic works.

Keep acquisition and version metadata in mathematics/literature/registry.md, either in its table or a per-work subsection.
Record the source URL or supplied-file provenance, identified version and intended use.
A retained artifact records acquisition date, actual local file and its storage fingerprint; an exception-registered source instead records access date, exact locator, an explicit no-local-artifact declaration and the acquisition-failure record.
Fingerprints only suggest possible accidental corruption and do not decide source identity or review validity.
Link an existing goal, route, or source unit when applicable.
For material supplied by the user for later use, record `User-supplied for future research; no goal assigned` instead of inventing a goal or audit unit.
State unknown provenance explicitly for pre-existing material; an audit date or a later discovered publisher URL must not be substituted for the original download date or source.

A citation key identifies a bibliographic work; explicit artifact locators identify retained versions, for example `<key>--arxiv-v2.pdf`.
A same-work revision, including mathematical changes or an established journal version, retains the key without new-key approval.
Adding a side version does not switch the primary PDF.
Before switching the primary, preserve older artifacts needed by existing evidence at explicit version locators and maintain truthful links from their reviews and uses.
Compare the statements, hypotheses and proof interfaces actually used before adopting a revised result.
Acquisition does not extend earlier review coverage or require an audit of unrelated parts of the work.

Discovery, validated download, statement checking, and proof review are separate activities.
A full source audit is not required merely to retain a relevant paper.
Record verification only to the depth actually performed, and use the source-audit records for mathematical checks when the paper is subsequently used.

<a id="searchable-contents"></a>
## Searchable tables of contents

After acquiring, receiving or reusing a selected book, monograph or other long-form source with a table of contents, prepare a searchable transcription of that artifact's actual contents.
This is ordinary source preparation, including user-supplied future material without a Task and independent local acquisition when original text is needed after U reuse.
Check first for an adequate transcription of the same edition.
A real contents list triggers the obligation; no page-count threshold or BibTeX-type classifier is needed.
A command that saves a PDF completes acquisition only, and cannot itself certify that the agent has prepared its contents.

Save UTF-8 Markdown in `mathematics/literature/contents/`.
For PDF, keep the exact registered filename stem: `pdf/SourceKey--edition.pdf` corresponds to `contents/SourceKey--edition.md`.
For original HTML, mirror the complete registered artifact path below `pdf/` into `contents/` and append `.md` to its native filename, retaining the HTML extension.
Thus `pdf/WorkA/source.html` uses `contents/WorkA/source.html.md`, `pdf/WorkB/source.html` uses `contents/WorkB/source.html.md`, and `pdf/WorkA/edition-2/toc.htm` uses `contents/WorkA/edition-2/toc.htm.md`.
Do not flatten nested paths, drop native extensions or infer source identity from a generic basename; the registered original-artifact names and facts already distinguish editions, volumes and snapshots.
Confirm title/author and actual language, edition, volume or revision against the source and registry.
Each file states that identity and coverage and links the exact native source or verified primary contents excerpt and the corresponding registry artifact account.
For PDF, identify the one-based PDF pages containing the contents separately from the source's printed destination labels.
For HTML, use actual part/chapter/section labels, native anchors and exact registered page paths, retaining any real printed page labels and omitting inapplicable PDF page fields.
Reuse an unambiguous registry anchor or add one at the existing account.
Do not duplicate bibliographic or acquisition logs.

The preparing agent chooses the registered page carrying the list as an HTML transcription's naming reference.
If one supplied list spans several pages, retain one adequate transcription with exact links to every actually used page and native location and state its actual coverage.
Different artifact accounts may share an adequate same-edition transcription only after the agent compares their actual lists and coverage and maintains their explicit links.
Preserve native source bytes and actual unavailable-resource limits; no site traversal or mandatory transcription per resource file is required.

Transcribe the complete supplied part/chapter/section hierarchy, numbers, titles, mathematical notation, appendices, unnumbered entries and printed page labels, including Roman numerals and all continuation pages.
Preserve the original language.
A detailed list may subsume a redundant overview.
Compare extracted/OCR text with the actual pages and correct order, columns, wrapped titles, numbering, symbols and pagination.
Inspect images for scans or damaged text layers.
Do not reconstruct a missing contents list from body headings, guess page offsets or make unverified body-page links.
Temporary extraction and images follow the [temporary-storage rule](organization.md#temporary-storage).

The preparing agent publishes the transcription and its direct consumers together: the exact work/artifact account in `registry.md` links `Contents: [Table of contents — actual edition](contents/SourceKey--edition.md)`; the transcription links back to that account and its exact source.
The literature entrance links the generic `contents/readme.md` usage guide alongside bibliography/registry.
That guide is not another book list.
Key/path changes and retirement update the affected filename, PDF association and actual links together.
Different editions/volumes keep separate associations; same-edition encodings may share an adequate transcription only after comparing their actual lists and page associations.
Never redirect one edition's contents link to another to clear a broken link.
No contents navigation belongs in BibTeX notes, and no reverse link from every mathematical material is required.

Known work: use its registry artifact account, follow the edition's contents link, then inspect the source passage.
Unknown work/topic: search retained titles under `mathematics/literature/contents/`, for example `rg -n -i --glob '*.md' -- "Hankel|Toeplitz|Hardy" mathematics/literature/contents`, confirm the matching file's edition/coverage, and inspect its source.
Search the original language and useful equivalent terms.
Follow the existing order of reviewed mathematical inputs, relevant local sources, then external search when insufficient; a complete contents scan is not a Task-startup requirement.
A hit is a locator, not theorem evidence.
No hit or absent/incomplete contents establishes no result absence; continue with relevant source indexes/full text and [progressive reading](#progressive-reading).

Partial artifacts and primary contents excerpts retain their true scope: a preview may supply a complete book contents list while holding only some body chapters.
State both boundaries.
A missing full PDF permits a verified same-edition publisher/author excerpt with its exact locator, never another edition's list.
Unreadable entries, missing pages or unavailable editions remain specific limitations in the existing registry and handoff; do not publish an empty placeholder as a completed transcription or invent a download.
A source actually without a supplied contents list needs no file.
Acquisition may succeed while transcription remains incomplete; report both truthfully, without a queue, automatic retry or extra approval.

Contents are source navigation, not a U inspection, review or mathematical argument.
Create no U/L/R merely for a contents list, mathematical digest, reading receipt or per-page register.
Citations continue to identify actual source statements/versions/passages.
Clean installations receive this rule and the generic usage entrance with an otherwise empty contents collection; named transcriptions and source artifacts are excluded.

<a id=progressive-reading></a>

## Progressive Reading and Audit Triggers

These rules cover monographs, papers, and unpublished manuscripts.
Adding a source does not assign a full audit.
During ordinary local source acquisition/registration, register identity, actual file/version, source type, publication status, access classification, known provenance and the fingerprint computed from actual locally obtained bytes.
An exception-registered source carries access date, exact locator, no-current-local-artifact declaration and failure record; only a previously established local fingerprint survives absence, and a never-obtained artifact has none.
Keep source type, publication status, and access as separate fields under the classifications below.
Inspect the title page and, as useful, the abstract, contents, index, or preface; label subject tags as provisional.
User-supplied sources may be registered for future research without an active goal, using the acquisition purpose stated above.
Do not invent a research objective or claim that unread chapters have been reviewed.

For each research task, follow this sequence.
The root [reuse-before-proof rule](knowledge-reuse.md#reuse-before-proof) also triggers it before substantial work on a nontrivial intermediate claim: inspect existing knowledge, then relevant unaudited local sources, and then external primary sources when local evidence remains insufficient.
Stop advancing when enough evidence is available; do not wait until a proof attempt stalls or repeat an adequate unchanged search.

1. State the question and identify the definition, result, method, or decision that needs evidence.
   Check the registry and relevant existing audit units, including their version and unchecked dependencies.
2. If reviewed material is insufficient, search unaudited local sources: use the [searchable contents route](#searchable-contents) and source indexes, then relevant terminology, equivalent formulations, theorem names, and citation leads.
   Trigger this step for a missing input, unclear convention, new mathematical lead, suspected conflict, or changed source version.
   Do not wait for a whole-source audit.
3. Read a promising passage with enough surrounding material to resolve notation and hypotheses.
   Record the exact source version, chapter/section, theorem or equation number, and printed/PDF page mapping where available.
   A search hit or extracted snippet is only a locator, not a verified result.
   If extraction is unreliable, inspect the relevant rendered pages; failed text search is not evidence of absence.
4. Before using a result in a proof, formalization, or substantive research conclusion, verify its exact source statement, version, locator, hypotheses, and local applicability.
   An ordinary established external theorem may be accepted without re-auditing its proof when no unresolved objection affects its use; document that acceptance and the actual inspection depth under the [accepted external-input rule](literature-audits.md#accepted-external-inputs).
   Trigger detailed proof review for a suspected error, a critical nonstandard input, incompatible conventions or a local extension requiring new reasoning, a version discrepancy, or an explicit task.
   Candidate routes may cite unaudited leads if clearly marked as conditional.
   Acceptance is not proof-assistant verification.
5. Expand to the definitions, lemmas, and dependency interfaces required by the current result.
   Distinguish accepted external inputs from unresolved evidence, applicability, or local deductions.
   An accepted foundational theorem does not become an unresolved condition merely because its proof was not reread; genuinely unresolved inputs and adaptations keep the affected conclusions conditional.
   Do not recursively audit every bibliography entry.
   Extend to an entire chapter or book only when the needed dependency structure or explicit task warrants it, recording the reason.
6. Stop when evidence is sufficient for the current decision, or record the exact unresolved gap and next useful action when access or repeated unproductive searches prevent progress.
   Reopen for new evidence, changed assumptions, or a new version; do not repeat unchanged searches by default.

The [registry](../../mathematics/literature/registry.md) owns source-acquisition and artifact facts and links to coverage records.
Concrete cross-repository acquisition operations and their obtained or unavailable provenance belong in `intake/<initiator>/` under the [intake rule](intake.md#scope-and-routing).
Source-specific reading/search notes and theorem-level audit coverage belong in `mathematics/audits/literature/`; use a compact section of an existing source record until a reusable unit warrants its own record.
Do not create one file or unit for every search hit.
Follow the [coverage states and template](literature-audits.md#coverage-states).
Existing full-source audits retain their documented scope; this policy neither downgrades them nor extends them to related sources.

<a id=unpublished-material></a>

## Unpublished and Restricted Material

Record three separate fields: source type (for example, paper, monograph, or lecture notes), publication status (`published`, `preprint`, `draft`, or `unknown`), and access classification (`public`, `restricted`, or `unknown`).
Apply them to the exact retained version.
A preprint whose public release has been verified follows the public-literature rules even if it has not appeared in a journal.
Private revisions, annotations, and accompanying communications do not inherit that public classification.

Private unpublished drafts default to local research use; existing explicit authorization governs any permitted disclosure.
Without authorization covering the action, do not upload restricted files or extracts to external services, publish or push them to a remote repository, or include private author information, nonpublic claims, or quotations in online searches.
This also applies to revealing audit notes and derived search queries.
Generic public mathematical terminology may be searched when it does not disclose private content.
If access classification is unknown, establish it before external disclosure.
General permission for public literature searches does not authorize disclosure of private material.
Material subject to copyright or distribution restrictions, especially original literature PDFs, stays outside Git tracking, uploads and outgoing material transfers.
The local source store's original PDF, HTML and resource files remain excluded even when publicly reachable; public availability alone selects no redistribution.
Relocating originals into J, attachments, another directory or large copied passages does not make them transferable agent-authored material.
The agent judges actual content and permitted disclosure, including revealing audit prose; scripts enforce known excluded paths and explicit publication boundaries without a copyright classifier.

## 1. Citation Keys and Filenames

Use readable, simplified alpha-style ASCII addresses, omitting diacritics from the key.
Exact reproduction of standard BibTeX alpha labels or typography is not required, and consistent existing keys need no rename solely for style conformance.
Preserve the complete ordered author list and actual name/diacritic forms in references.bib.
Identify surname components and source order correctly: ordinary single surnames use their three-character abbreviation; two through four authors contribute their surname initials; five or more contribute the first three names plus literal + before the year.
Retain the supported short/compound surnames, particles and editor/organization fallbacks.
Do not shorten author fields with and others to manufacture a key.
Use an established Latin transliteration only for the portable label and diagnose collisions.

Work identity uses stable source identifiers and actual bibliographic authorship, not the shortened key.
Compare supported BibTeX personal-name forms by their components and author order, interpreting equivalent TeX/Unicode name characters without rewriting the original fields or evaluating arbitrary TeX.
For example, `Dra\v{z}en` and `Dražen` identify the same spelling; an accent-free key is not evidence that two different full names identify the same author.
No initials expansion, fuzzy person matching or person registry is implied.

At initial registration, use formal publication year when known, otherwise first public release, otherwise the known private draft year with its basis.
A genuinely unknown identity/year needs an explicitly grounded provisional address; do not invent authorship or a publication date.
Later publication metadata does not recalculate an established address.

Primary PDFs use mathematics/literature/pdf/<key>.pdf; additional versions use <key>--<version>.pdf.
Original HTML pages/resources use the established `<key>/` group with explicit edition/page locators.
Source U directories, local explicit anchors, citations and writing choices use the same stable key.
Native HTML anchors and original source text are opaque source content, preserved during local key/directory maintenance.
Plus is a literal key character, not a form-encoded space; quote it as %2B in URLs and escape it in regular expressions.
It does not expand the human/repository name syntax.

## 2. Collisions, Versions, and Key Stability

Compare the full collection case-insensitively.
An unused base receives no suffix.
Once occupied, assign only the new distinct works b, c and onward; never rename the first registered work to add a.
Keep existing addresses stable, retain the established suffix progression beyond z and do not fill earlier holes, reorder the group or regenerate keys from a manuscript subset.
Identify same-work acquisitions or editions before resolving a shortened-key collision; reuse their established key and keep exact inspected editions distinct in the artifact registry and U.

<a id="coordinated-key-renaming"></a>
### Coordinated Key and Source-Unit Renaming

For an adopted naming migration, the agent identifies the actual work correspondence and affected consumers, then supplies complete chosen keys, exact designated text edits or expected original text with prepared final text, and complete source/destination file pairs.
Tools change those explicit paths/fields without global text replacement, same-work inference or source-store discovery.
Choosing a file does not select every matching citation, anchor or key token inside it.
Designated edits check their expected original text; parsed entry keys and the defined single-key `crossref`/`xref` values use exact complete-key lookup.
Key lists, mixed fields, file/URL values and other selected bibliography text require explicit supplied values or designated edits; no shared key prefix selects another work or path.
Use the supplied target key's exact spelling in bibliography keys, structured references and selected key-derived paths; an old token's lowercase spelling does not change the chosen target.
Choose any lowercase local anchor separately in the designated edit, while case-insensitive destination-conflict checks remain in force.
Mixed notes, quotations, literal examples, mathematical notation and original-source locators remain unchanged unless explicitly selected for a corresponding edit.
Preserve source bytes, original HTML anchors/filenames/relative resources, mathematical content, review facts and source headers.
Inspect only each chosen group for containment before moving it, never the entire external mount.
Retire old active addresses after actual consumers are repaired; no alias or permanent correspondence registry is needed.
The agent judges actual citation completeness and updates responsible writing records; optional structural checks do not classify arbitrary TeX or Markdown matches as active citations or refuse literal old spellings.
A missing chosen artifact keeps its new actual-format address and availability fact.
Prepare any selected intake operation's exact local path, actual anchor and necessary file/artifact correspondences with the same material edits, following the [operation contract](intake.md#one-operation-record).

The sole structured bibliography is mathematics/literature/references.bib.
Record known complete names, title, type, year, venue, volume/issue, pages/article number, publisher/edition, DOI/arXiv and actual source/version locators there.
Unknown or unverified metadata is explicit, not invented.
registry.md records acquisition/access, artifact versions and byte identity, availability/exceptions and useful links by key; it does not maintain another manual author/title/publication table.
Manuscript .bib files are synchronized subsets, retaining explicitly cited alternate-edition titles/years where the registered version supports them.
Do not overwrite a U's inspected edition with a different canonical primary edition.

## 3. Citations Elsewhere in the Repository

- Use the complete citation key in prose, for example `[Miy22]`.
  Do not use only an author and year, a bare numeric reference such as `[1]`, or wording such as "the paper above" as the sole identifier.
- In Markdown, link the first occurrence of each work in each document to its registered source artifact, or to its registered online URL for an exception-registered source.
  Resolve destinations relative to the current document; a root-level document uses a path such as `mathematics/literature/pdf/Src26.pdf`.
  Link destinations containing spaces may be enclosed in `<...>`.
- A review directly inside `mathematics/audits/literature/` uses the relative source path `../../literature/pdf/Src26.pdf`; a unit one directory deeper uses `../../../literature/pdf/Src26.pdf`.
  These are formatting examples, not registered artifacts.
- When citing a specific result, include a locator, such as `[Miy22, Theorem 3.1]` or `[Miy22, Section 2.3]`.
  These examples illustrate formatting only; verify actual numbering against the source.
- Page references default to the paper's printed page numbers.
  Explicitly write `PDF p. 5` when using the PDF viewer's page sequence.
  When citing a version other than the primary version, identify the version, include the locator, and link to that version's file.
- Do not treat numbers in a paper's bibliography as this repository's citation keys.
  Register a referenced work separately when citing it directly.
  If relying only on the current paper's account, explicitly identify the secondary citation, for example "reference [11] in [Miy22], cited via [Miy22]."
- Use the same keys in LaTeX and BibTeX, for example `\cite{Miy22}` and `@article{Miy22, ...}`.
  Code comments, computation records, and audit notes must also use these keys, adding result numbers where needed.

## 5. Checklist for Adding or Updating Literature

1. Identify the expected use and linked authorized research record when applicable.
   For user-supplied future material, record `User-supplied for future research; no goal assigned` without creating a goal or unit.
   Check existing entries and files by bibliographic identity, stable identifier, and version before downloading; reuse an adequate existing source.
2. Verify the authors, title, known year, stable identifier, and version against the retrieved or supplied artifact.
   Record source type, publication status, and access classification separately for that version.
   Check that the file contains the intended source rather than an error or login response; apply the restricted-material rules before external disclosure.
   For an exception-registered source, verify the same identity fields against the identified online page at the registered locator instead, including that it is the intended source rather than an error or login response.
3. Assign keys under the identity and changed-source rules above.
   Validate the actual locally obtained artifact and compute/record its storage fingerprint for accidental-damage checking.
   A never-obtained artifact has no fingerprint; a previously obtained file that later becomes unavailable retains its established local baseline and actual access limitations.
4. Complete the known bibliographic fields and appropriate entry type in canonical references.bib, then record acquisition and artifact facts in registry.md: actual source URL or supplied provenance, identified edition/version, purpose and relevant record link.
   A retained artifact records acquisition date, actual path and storage details; an exception-registered source records access date, exact locator, an explicit no-local-artifact declaration and the failure record.
   Keep source inspection and proof-review scope in U or the responsible audit material, linked from the registry.
   Record access failures accurately.
   Keep unknown metadata explicit and preserve evidence needed for earlier audits.
5. Use the same key in notes, prose, scripts, and bibliographies.
   Verify the version and locator when citing a specific result; compare relevant statements and hypotheses before transferring an audit or changing its locators.
   Do not label an acquisition as a statement check or proof review.
6. Prepare or reuse [searchable contents](#searchable-contents) when the selected source supplies a contents list, including user-supplied future material.
   Link its exact artifact account and source; state any unfinished transcription separately from acquisition.
7. Check that relative links resolve to the intended files.
   When changing keys or replacing versions, maintain affected contents filenames/edition links alongside stale citations, broken links, and theorem numbers or page references that no longer match.

## Registry Fields

Use the canonical citation key to link each registry entry to references.bib.
Complete authors, title, known year, publication venue/type, volume/issue, pages/article number, publisher/edition and DOI/arXiv identifiers belong in that BibTeX entry, not a second registry table.
The registry owns supplied provenance or actual acquisition URL, dates, exact retained/online edition, artifact path and byte identity where available, access classification, availability and failure/exception facts.
Distinguish the canonical publication from an inspected preprint; U or the responsible source audit owns the inspected passages, conclusions and proof-review limits.
Historical verification observations may retain their actual locators and scope without becoming another current bibliography.
An intake purpose of `User-supplied for future research; no goal assigned` is valid without a goal, route, or unit link.
Mark unverified details as "To be verified" instead of inferring them from filenames.


### Preparatory local PDFs

An unregistered PDF may remain in the local literature store as preparatory material.
Its presence produces an informational reminder, not a failure or a prerequisite to further work.
Registration, bibliographic verification and actual source inspection remain separate substantive actions when needed.
Do not invent metadata, allocate a key, delete the file or request acknowledgement just to clear the reminder.
Missing required evidence and invalid registered artifacts retain their actual error diagnostics.
Clean framework exports exclude personal literature; no pending-file inventory or exception list is maintained.
