---
name: tableau-building
description: Guide Tableau dashboard work from requirements through design, implementation, verification, and handoff. Route each stage to the bundled specialist skill.
---

# Tableau Building

Use the skills needed for the current stage. Reuse agreed decisions. Do not restart the workflow for a small repair or repeat a completed interview.

## Workflow

1. **Plan:** Use `tableau-dashboard-planning` to clarify the brief, write the Tableau spec, and split larger work into dependent tickets. Inspect the supplied references, source definitions, and latest relevant workbook. Ask only about unresolved decisions.
2. **Design:** Use `tableau-dashboard-design` to make a Tableau-buildable preview. Follow the user's approved reference. Get approval before layout implementation unless the user explicitly skips preview review.
3. **Implement:** Use `tableau-workbook-engineering` for each approved slice. Preserve the current workbook, confirmed connection, authentication, and unrelated tabs. Use Tableau Desktop or a version-compatible Desktop-created starter. Do not invent Tableau XML.
4. **Verify:** Run the ticket checks and final integration checks. Open every changed final `.twb` in the installed Tableau Desktop version and confirm it loads. Keep XML checks, Desktop checks, and published-browser checks distinct.
5. **Hand off:** Record the outcome, workbook and SQL locations, metric definitions, checks, open issues, and next action. Turn a validated cross-project pattern into a reusable skill; keep project-specific facts in the handoff.

Use the team's existing project folder. For a new dashboard, agree on a parent location and create one project folder. Add `SQL Query/`, `Design/`, `Config/`, and `Backup/` inside it. Reuse existing folders without renaming them.

## Data and access

Use the user's named source or the latest confirmed workbook connection. Verify grain, date coverage, metric definitions, joins, and missing-value meaning. Do not borrow another project's data model or authentication. If access fails, state the gap and continue with a design spec and SQL.

Treat production BigQuery data as read-only. Write tables or views only in a non-production target authorized for the current project. If no target is authorized, prepare SQL without executing writes. Dry-run every SQL query before execution. If the estimate exceeds 50 GB, stop and report it.

Do not publish, change authentication, or create warehouse objects as part of layout work. Do not package credentials, connection-bearing workbooks, or private data in this plugin.
