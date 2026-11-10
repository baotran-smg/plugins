---
name: tableau-building
description: Plan, build, or review a Tableau dashboard from a short brief. Clarifies decision needs, validates the data source and metric definitions, applies the bundled Tableau design and workbook skills, and verifies the result.
---

# Tableau Building

Turn a user's dashboard request into a useful, accurate, and reviewable Tableau deliverable. Work in the user's project context and use the bundled `tableau-dashboard-design` and `tableau-workbook-engineering` skills for their specialist guidance.

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

## Workflow

### 1. Grill and agree on the dashboard requirements

Translate the brief into the audience, decision or action, required metrics, reporting period, useful filters, and expected deliverable. Ask only questions whose answers could materially change the metrics, source, or dashboard design. Summarize assumptions and unresolved decisions before proceeding when ambiguity affects correctness. A request for a proposal or explanation is not authorization to edit a workbook.

### 2. Identify and validate the data source

Use the source named by the user or connected in the latest user-approved workbook. Confirm its owner and access method, grain, date coverage, refresh status, field meanings, units, joins, and whether missing values mean unknown, unavailable, or zero. Prefer curated `dw_pl` sources to raw Pub/Sub when applicable. Validate surprising dashboard numbers against source data. Do not borrow another project's datasource, metric definitions, workbook, or authentication settings as a shortcut.

For BigQuery work:

- Treat production tables and views as read-only. Create or modify tables and views only in `smg-data-automotive-dev.dev_baotran`, unless the user names a different non-production destination.
- Dry-run every SQL query before execution. If estimated bytes processed exceed 50 GB, stop and report the estimate without executing.
- Do not label missing or unavailable source data as zero.

If the source cannot be accessed or its meaning cannot be confirmed, continue with a clearly labeled data mapping or SQL proposal and state what evidence is missing. Do not imply that a data connection or query was validated when it was not.

### 3. Agree on the design

Inspect the user's latest workbook and any provided reference artifact before designing. Follow that reference for the requested scope; do not substitute an unrelated workbook. Define the worksheet and dashboard purpose, visual hierarchy, filters, navigation, metric units, thresholds, and unavailable-data states. Use the bundled `tableau-dashboard-design` skill for layout work. Show a preview built from realistic Tableau-native components and obtain review before implementing it, unless the user explicitly authorizes proceeding without review.

### 4. Build the workbook

Prefer Tableau Desktop. For direct workbook edits, follow the bundled `tableau-workbook-engineering` skill. Preserve the confirmed datasource, connection, authentication, calculations, filters, and existing user changes outside the requested scope. Never hand-author a new `.twb` from scratch without a compatible Tableau Desktop-created starter workbook. Never add XML elements or attributes from assumptions; use patterns verified from the same Tableau Desktop version. Preserve the target workbook root order and each element's allowed child/attribute schema; in the 2026.3.0 schema, `<dashboards>` precedes `<windows>`, `<table>` cannot contain a direct `<title>`, and `<dashboard>` cannot use an unverified `enable-sort-zone-taborder` attribute. Place titles in a verified dashboard text zone. Do not change OAuth, service-account authentication, publishing, extracts, refresh schedules, or warehouse objects as an incidental part of layout work.

If Tableau Desktop or an authenticated connection is unavailable, keep that access limitation separate from the design work. Deliver a design specification and SQL rather than an unverified workbook.

### 5. Verify and hand off

Validate the workbook structure and the numbers against the approved source. Check metric labels, units, filters, date ranges, null handling, joins, navigation, and the affected layout. For every `.twb` change, open the final workbook in the installed Tableau Desktop version and confirm it loads and renders. XML parsing or custom validation alone is not proof of successful delivery. Report exactly which checks were completed and which remain unverified.

Do not claim the dashboard is complete until the required Desktop check succeeds. Do not publish or send the result to others unless the user asks for that action.

## Reusable package boundary

Keep this plugin generic to the workflow. Do not package client credentials, connection-bearing workbooks, private metric data, or project-specific SQL results. Obtain a user's source, definitions, and authorization separately for each dashboard task.
