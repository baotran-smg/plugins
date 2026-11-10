---
name: tableau-dashboard-design
description: Design or restyle Tableau overview matrices and metric-trend dashboards using the user's established typography, colors, spacing, filters, and navigation patterns. Use for Tableau dashboard UI consistency across projects, not for SQL-only work or connection-only troubleshooting.
---

# Tableau dashboard design

Reuse the user's approved visual language without copying a project's data model or turning a past mockup into permission to redesign everything.

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

## Start with scope and evidence

- Read the latest user-saved workbook immediately before editing. Use the newest user-approved screenshot or workbook as the design reference, not an older generated mockup.
- Separate implementation requests from requests to propose, explain, or diagnose. A proposal does not authorize editing the dashboard.
- Determine whether the change affects an overview, trend dashboards, or both. Keep unrelated sections unchanged.
- For a new dashboard in this style, read [references/design-system.md](references/design-system.md) and inspect [assets/approved-trend-reference.png](assets/approved-trend-reference.png). The screenshot illustrates style, not reusable values or authoritative metric definitions. New user references override it.
- For filters, references, navigation, or publishing, also read [references/tableau-behavior.md](references/tableau-behavior.md).

## Approved visual language

Use these defaults unless the project's reference or user says otherwise:

| Role | Default |
|---|---|
| Page | Light blue-gray `#F3F6FA` |
| Cards | White `#FFFFFF`, subtle `#D9E3EA` border |
| Main text | Navy `#173047` |
| Supporting text | Muted blue-gray `#708493` |
| Warning | Pale amber `#FFF6E5`, amber text `#A76B18` |
| Positive / watch / risk | Teal `#46A5A5`, amber `#E6A322`, red `#C4495A` |
| Unavailable / undefined | Gray `#9AA7B1` |

Specify native Tableau font families explicitly: Tableau, Tableau Semibold, Tableau Bold. Use hierarchy rather than enlarging everything. Trend titles are about 30pt, metric headings 16pt, categories 10pt, supporting text 10–11pt, and point labels 12pt. Dense overview cells use smaller sizes; see the design reference.

Status color belongs to the metric value and status strip, not its title or threshold text. Preserve the project's threshold direction, availability rules, and numeric units. Do not infer that a downward trend is automatically bad.

## Layout decisions

- Before implementing a layout change, generate and show an image of the expected layout for user review, unless the user explicitly skips the preview. Follow the buildability requirements below.
- Trend: compact header, native time control, Back navigation, concise warning, consistent chart cards. Shorten repeated chart titles into a category eyebrow plus the metric label.
- Replace redundant subtitles with a useful explanation, for example: “Track monthly trends against configured thresholds; gaps indicate unavailable data.” Do not imply thresholds exist for every metric.
- A short gray empty state can replace a genuinely unavailable trend. Do not remove a real historical series merely because its latest month is null. Keep a clear maintenance path when a static empty-state card must later become a chart.
- Overview: preserve working product-row alignment, row height, status-strip height, and the product-name column. Restyling a header does not authorize rebuilding the metric matrix.
- Use short borderless `Trends →` navigation captions that fit the narrow column. Keep targets intact.
- Choose a single approved dashboard as the first pilot for a new design. Extend it after user review, translating metric labels, units, thresholds, availability, and layouts per product rather than copying AI Studio's content.

## Buildable layout preview

The preview must represent a dashboard that can actually be built in the target Tableau version, not an aspirational graphic-design mockup.

- Ground the image in the current workbook's native components: horizontal/vertical containers, worksheets, text and blank objects, native filter cards, Navigation objects, padding, borders, shading, and reference lines. Map each proposed visual section to its Tableau component and layout arrangement in a brief accompanying note.
- Use realistic dashboard dimensions, container widths, plot heights, font sizes, and text wrapping. Show native-looking controls and charts; preserve room for long labels and filter titles. Prefer tiled layouts; use floating objects only where their placement and resizing behavior are deliberate.
- Exclude effects or interactions without a verified Tableau implementation path, such as unsupported shadows, rounded-card styling, custom dropdowns, or automatic product routing. If a feature requires an extra worksheet or calculation, identify that dependency rather than presenting it as existing.
- Prefer a screenshot of a native Tableau prototype when available. Otherwise render or generate a clearly labeled illustrative image constrained to the native component plan. An image is a design preview, not proof that the workbook loads or publishes correctly.
- Let the user review the preview before implementation unless they explicitly authorize proceeding without that review. Carry the approved geometry and component plan into the workbook; if a native limitation forces a material deviation, explain it and revise the preview rather than silently substituting a different layout.

## Implementation safeguards

For TWB modifications, use the available `tableau-workbook-engineering` skill as well. Preserve its schema-ordering, source-selection, and connection safeguards. Reuse patterns actually saved by the same Tableau Desktop version; a generated image is not an XML template.

- Keep authentication, datasource identity, calculations, and field filters unchanged during a styling-only task. Display-format changes must be explicit and tested; do not interpret every `0` format as a count or round an SEQ score accidentally.
- Do not clone a calculated field per chart when its formula, availability behavior, and format are identical. Share percent, decimal, and count fields where genuinely equivalent. Preserve differing logic rather than silently merging it.
- Never invent KPI values, deltas, unavailable-month points, or native XML to imitate a mockup. A latest-value summary must derive the latest non-null value correctly for its stated scope and handle the time filter; a maximum value is not necessarily the latest value.
- A one-off verification waiver applies only to the requested run, not to future projects. Follow current project verification requirements. Keep structural validation, Desktop loading, and published-browser verification distinct.

## Check before delivery

Inspect available text height after padding, filter worksheet anchors, repeated calculations, both reference-line identities, and native zone ordering. Structural checks do not prove visual correctness or replace opening the workbook.

For actual delivery, compare against a snapshot of the latest source. Check that only the requested scopes changed; all chart fields, units, month selections, navigation targets, and datasource connections remain correct. Before replacing the source, guard against concurrent user edits. Preserve a recoverable before-copy and honor the requested output path.

On published dashboards, inspect header/subtitle, all footnotes, longest metric labels, month controls, both thresholds, row/strip alignment, and navigation. Do not claim published verification without observing it. State what was changed and what remains unverified or blocked.
