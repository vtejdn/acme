# Searchable tables of contents

This collection holds searchable chapter/section lists transcribed from actual source editions under the [literature rule](../../../framework/rules/literature.md#searchable-contents).
It supplies source navigation, not theorem evidence or a whole-source review.

Use the shared bibliography and edition-specific transcriptions to locate a known work; an actual local source check may consult `mathematics/literature/registry.md` without making it a shared prerequisite.
Each transcription names its work/edition, coverage, actual contents locators and exact source pages, with logical original-source or verified excerpt links rather than a registry-account backlink.
Filenames use the registered PDF's complete stem: `pdf/SourceKey--edition.pdf` corresponds to `contents/SourceKey--edition.md`.
For original HTML, mirror the complete path below `pdf/` and append `.md`: `pdf/WorkA/source.html` uses `contents/WorkA/source.html.md`, while `pdf/WorkB/source.html` uses `contents/WorkB/source.html.md`.
Nested edition paths and native extensions remain intact, as in `contents/WorkA/edition-2/toc.htm.md`.
Choose the registered page carrying the list as its naming reference; one adequate transcription can cover a multi-page list through exact links and stated coverage under the common rule.
Different editions and volumes remain distinguishable.
This generic entrance is not a second book or availability list.

For an unknown work or topic, search the retained titles from the repository root:

```powershell
rg -n -i --glob '*.md' -- "Hankel|Toeplitz|Hardy" mathematics/literature/contents
```

Search the source language and relevant equivalent terms.
Open a matching transcription, confirm its edition and stated coverage, then inspect the actual source passage using its printed labels when that original is needed and available.
Contents-page PDF positions and printed destination labels serve different purposes; no constant offset is assumed.
HTML uses actual chapter/section labels, native anchors and registered page paths, retaining real printed labels where present and omitting PDF page fields.
No hit, an empty collection, missing transcription or unavailable source establishes no result absence.
Continue with source indexes/full text and [progressive reading](../../../framework/rules/literature.md#progressive-reading) when needed.

When preparing a source with an actual contents list, reuse an adequate same-edition transcription or save the complete supplied hierarchy and page labels.
Maintain the transcription's exact source links and necessary shared consumers together, and state missing/unreadable portions honestly; a local account may link to it without a reciprocal private-account link.
A successful source acquisition alone does not complete this agent step.
A clean installation starts with this usage guide and no named source transcriptions.
