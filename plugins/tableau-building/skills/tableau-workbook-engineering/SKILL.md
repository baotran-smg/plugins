---
name: tableau-workbook-engineering
description: Create, edit, consolidate, or repair Tableau TWB workbooks and datasource connections while preserving Tableau XML compatibility and current user changes.
---

# Tableau Workbook Engineering

Use this skill for direct `.twb` generation or XML edits.

Implement only the approved slice. Read its spec, ticket, design preview, and acceptance checks. Ask about new blockers, not settled decisions. Use `tableau-dashboard-planning` if the scope is still undefined, and `tableau-dashboard-design` if layout approval is still needed.

## Project and workbook state

Use the agreed project folder. For a new project, create `SQL Query/`, `Design/`, `Config/`, and `Backup/` inside it. Reuse existing folders without renaming them. Keep SQL in `SQL Query/`, design artifacts in `Design/`, scripts and reports in `Config/`, and prior workbooks in `Backup/`. Keep the latest verified workbook in the project folder. Do not store credentials in project files.

Before editing, back up the latest user-saved workbook with a unique timestamp. Keep it in place while preparing the candidate. Preserve packaged dependencies. Recheck for concurrent user edits before replacement. Replace the main workbook only after the required Desktop checks pass. Keep the last verified version if they fail. Do not delete backup history.

For each ticket, change only its approved scope. Keep shared calculations and connections consistent across slices. Run its acceptance checks before starting the next slice. Reserve cross-tab filters, navigation, performance, and overall consistency for the integration ticket.

## Source selection

- For edits, locate and read the user's latest workbook immediately before changing it. Do not use a previously generated or backup copy as the source unless explicitly requested.
- For a new workbook, use a Tableau Desktop-created, version-compatible starter. Do not hand-author a new `.twb` from scratch.
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
2. Run `scripts/validate_twb.py --legacy-compatible <workbook>` when broad compatibility is part of the approved work.
3. Confirm there are no duplicate datasource, worksheet, or dashboard names.
4. Confirm all dashboard worksheet zones resolve to existing worksheets.
5. Confirm datasource columns and worksheet filters satisfy Tableau's schema-sensitive ordering.
6. Search for stale datasource and table names after replacement.
7. For every `.twb` change, open the final file in the installed Tableau Desktop version and confirm that it loads and renders before calling it complete. If Desktop automation is unavailable, deliver a design specification and SQL rather than an unverified workbook.

XML parsing proves only well-formedness. It does not replace opening the workbook in Tableau.

## Handoff

After a verified slice or release, record the outcome, approved scope, workbook and SQL locations, metric and source definitions, checks performed, open issues, and next action. Link to the spec and ticket. Keep project-specific details in the handoff. Extract a reusable skill only after the pattern is validated for reuse. Do not claim Desktop or published verification without observing it.
