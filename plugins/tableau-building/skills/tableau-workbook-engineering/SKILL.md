---
name: tableau-workbook-engineering
description: Create, edit, consolidate, or repair Tableau TWB workbooks and datasource connections while preserving Tableau XML compatibility and current user changes.
---

# Tableau Workbook Engineering

Use this skill for direct `.twb` generation or XML edits.

## Master Tableau project setup

Apply these rules to every new Tableau dashboard project and when continuing an existing one.

- Use `/Users/baotran/Documents/Working Projects/Tableau Dashboards` as the dashboard project parent. For a fresh project, create one clearly named child folder; for existing work, reuse its child folder. Do not create a second project folder for each request. Honor an explicitly different user destination.
- Create and use these dedicated subfolders in the project folder: `SQL Query/` for SQL files; `Design/` for requirements, specifications, reference copies, previews and design exports; `Config/` for configuration, build scripts and validation reports; `Backup/` for previous dashboard versions. Do not store credentials in configuration files. Keep user-supplied reference originals in place unless asked to move them.
- Keep the latest verified `.twb` or `.twbx` for each deliverable directly in the project folder. Update script destinations and relative links to match this structure.
- Before any workbook edit or replacement, preserve a timestamped copy of the latest user-saved workbook in `Backup/` (for example, `<name>_YYYY-MM-DD_HH-mm-ss.twbx`); avoid overwriting an existing backup. Keep the current workbook in place while preparing and verifying its replacement. Preserve packaged dependencies needed to restore it.
- After the replacement passes the required Tableau Desktop checks, place it at the canonical main-folder path and move superseded dashboard versions and backup copies into `Backup/`. Recheck for concurrent user edits before replacement. If validation fails, retain the last verified workbook in the main folder and clearly identify the unfinished candidate. Do not delete backup history or archive an ambiguous workbook without establishing which version is current.

## Always grill the requirements

Before building a fresh dashboard or implementing a changed requirement, critically examine the brief and available project evidence. Probe the audience and decision, success criteria, metric formulas and denominators, reporting grain and dates, data sources and access, filters and comparisons, edge cases and missing values, reference layout, deliverables, and acceptance checks. Challenge contradictions and unsupported assumptions instead of silently inventing requirements.

Ask focused follow-up questions for unresolved decisions that materially affect correctness or design, using small rounds and continuing useful independent work while waiting. Reuse confirmed answers rather than asking again. Record the agreed requirements, assumptions, and open questions in `Design/` before implementation; resolve blocking questions before dependent work. For a small repair, grill only the affected scope. This requirements review does not replace the required design preview and user review unless the user explicitly skips it.

## Source selection

- For edits, locate and read the user's latest workbook immediately before changing it. Do not use a previously generated or backup copy as the source unless explicitly requested.
- For a new workbook, prefer a minimal known-good workbook exported by the user's Tableau Desktop version.
- Never modify the stakeholder workbook when the request calls for an isolated POC.

## XML compatibility

- Treat document-format manifest flags and their dependent elements as a pair.
- `WindowsPersistSimpleIdentifiers` and every `simple-id` must be handled together.
- For broad compatibility in a newly generated workbook, remove both the manifest flag and all `simple-id` elements. A workbook that declares the feature but omits IDs can fail with a missing-element error; an incompatible Tableau schema can reject IDs even when they are declared.
- Preserve element ordering from a known-good workbook. Tableau validates more than ordinary XML well-formedness.
- Treat the complete root and each nested element content model as part of the schema contract. For example, the 2026.3.0 workbook schema requires `<dashboards>` before `<windows>`; a worksheet `<table>` rejects a direct child `<title>`; and its `<dashboard>` element rejects the unverified `enable-sort-zone-taborder` attribute. Do not infer XML tags or attributes from another Tableau build.
- Put dashboard titles in a verified dashboard text zone. Before writing, compare the target-build workbook's root ordering, worksheet table children, and dashboard attributes with a workbook authored by that same Desktop build.
- Do not invent shelf or mark elements such as `angle`; copy the exact representation from a workbook created by the target Tableau version.
- Every dashboard worksheet zone must reference a worksheet that has a complete visual representation.
- Keep worksheet, dashboard, datasource, named-connection, and relation identifiers unique.
- Preserve datasource child ordering: `connection`, `aliases`, columns/calculations, then layout/style/semantic metadata and `object-graph`.
- Preserve worksheet view ordering: datasources and dependencies first, all filters before sort/perspective/shelf metadata, then slices and aggregation.
- Validate sort references in their own scope. A datasource-level `default-sorts` entry cannot resolve a column-instance declared only inside a worksheet's `datasource-dependencies`. In a 2026.3 workbook, adding `natural-sort column="[none:product:nk]"` at datasource level without a matching datasource-level instance caused the warning "Field ... is undefined, ignoring sort specification."
- For a sort-warning repair, remove the invalid added sort when the existing natural ordering is sufficient. If explicit sorting is required, use a same-version Desktop-authored pattern with its complete field/instance declarations. Copying only a sort element's shape does not establish that its field reference is valid. Recheck fixed navigation buttons against actual row order after loading.

## Tooltip composition and calculation validation

- For display-only tooltips, prefer native text with separately inserted field tokens and line breaks rather than creating a concatenation calculation solely to format text. Tableau's standard workflow inserts dimensions with `ATTR`; verify each tooltip field resolves in the worksheet and is available through Tooltip or an appropriate Marks encoding. When using Detail, preserve the intended mark grain; an aggregated text attribute avoids adding a new discrete grouping dimension. See [Tableau Marks and tooltips](https://help.tableau.com/current/pro/desktop/en-us/viewparts_marks_markproperties.htm).
- In XML work, reuse the current version's saved tooltip, attribute-instance and Marks encoding patterns, including complete worksheet dependencies. A field appearing in formatted tooltip text alone does not prove that its calculation or reference is valid. Update dependent worksheets when removing or replacing a calculated field; search the whole workbook for stale tokens.
- A 2026.3 Inventory tooltip concatenation produced an aggregation/source-context error in Desktop despite passing XML checks. Its exact evaluation-context cause was not established; do not treat `CHAR` or text concatenation as generally invalid. Removing the unnecessary calculation and composing the tooltip from its original attributes avoids that failed dependency. A structural validator cannot compile Tableau formulas; retain the Desktop check unless the user explicitly defers it.

## Verification

1. Parse the final file as XML.
2. Run `scripts/validate_twb.py --legacy-compatible <workbook>` for a newly generated broad-compatibility workbook.
3. Confirm there are no duplicate datasource, worksheet, or dashboard names.
4. Confirm all dashboard worksheet zones resolve to existing worksheets.
5. Confirm datasource columns and worksheet filters satisfy Tableau's schema-sensitive ordering.
6. Search for stale datasource and table names after replacement.
7. For every `.twb` change, open the final file in the installed Tableau Desktop version and confirm that it loads and renders before calling it complete. If Desktop automation is unavailable, deliver a design specification and SQL rather than an unverified workbook.

XML parsing proves only well-formedness. It does not replace opening the workbook in Tableau.
