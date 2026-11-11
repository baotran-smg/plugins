---
name: tableau-dashboard-planning
description: Clarify Tableau dashboard requirements, write an agreed spec, and split larger dashboards into reviewable, dependency-aware tickets. Use before design or implementation, not for direct workbook editing.
---

# Tableau dashboard planning

Use this skill to define dashboard work before design or implementation. Reuse decisions already recorded. Keep the spec and tickets in the project's `Design/` folder, or the user's chosen location. For a new project, use the agreed parent folder and create one project folder with `SQL Query/`, `Design/`, `Config/`, and `Backup/`. Reuse existing folders without renaming them. A request for a spec or tickets does not authorize workbook edits, BigQuery writes, publication, or issue-tracker creation.

## Clarify the requirement

Inspect the brief, supplied references, and relevant workbook or SQL. Do not use an unrelated workbook as a design or authentication reference. Ask only about unresolved decisions: audience, tabs, charts, metrics, grain, dates, sources, filters, missing values, and acceptance checks. Record answers once. For a small repair, clarify only the affected scope. If the user invokes `/grill-me`, use its interview workflow; otherwise ask proportionate questions.

## Write a Tableau-buildable spec

State the problem, user decisions, scope, tabs, charts, interactions, metric and data contracts, visual reference, acceptance checks, exclusions, and open decisions. Mark confirmed requirements, assumptions, and proposals. For each chart, specify measure, dimensions, grain, date logic, filters, null behavior, and expected form. Describe shared components once. Identify a Tableau Desktop build path or compatible starter workbook for new dashboards. Pass the spec to `tableau-dashboard-design` for preview and approval.

## Split into reviewable tickets

After the spec is agreed, create tickets when the user wants them. Use a tab or coherent chart group as a usable slice, including data, calculations, filters, formatting, and checks. Give shared data or navigation its own prerequisite ticket when several slices need it. Add a final integration ticket for cross-tab behavior, performance, visual consistency, and Desktop verification. Do not split every chart mechanically. Each ticket states its output, dependencies, acceptance checks, and evidence. Update affected tickets if the design preview changes the agreed scope.

If an issue tracker is specified and accessible, use its existing schema and avoid duplicates. Otherwise keep the tickets in `Design/` for review.
