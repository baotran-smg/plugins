---
name: tableau-dashboard-design
description: Design or restyle Tableau overview matrices and metric-trend dashboards using the user's established typography, colors, spacing, filters, and navigation patterns. Use for Tableau dashboard UI consistency across projects, not for SQL-only work or connection-only troubleshooting.
---

# Tableau dashboard design

Reuse the user's approved visual language without copying a project's data model or turning a past mockup into permission to redesign everything.

For a multi-tab dashboard, read the agreed spec and tickets from `tableau-dashboard-planning`. Reuse their decisions. Ask only about new design gaps. A design request does not authorize tracker or workbook changes.

## Design input

Use the agreed project folder. For a new project, use `SQL Query/`, `Design/`, `Config/`, and `Backup/` inside it. Reuse existing folders without renaming them. Keep the spec, references, and preview in `Design/`. Preserve original references in place.

Read the agreed requirements. For a small design repair without a full spec, clarify only the affected scope. Resolve design conflicts before making a preview. Do not repeat a completed planning interview.

## Start with scope and evidence

- Inspect the latest user-saved workbook when one exists. Use the newest user-approved screenshot or workbook as the design reference.
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

- Show a buildable layout preview before implementation, unless the user explicitly skips it.
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
- Get approval for the preview before implementation. Carry its geometry and component plan into the workbook. If a native limit forces a material change, revise the preview and review it again.

## Design handoff

Pass the approved preview and any changed acceptance checks to `tableau-workbook-engineering`. A generated image is not an XML template.

- State any required display formats and calculations in the approved design. Do not infer that every `0` format is a count or round a decimal score accidentally.
- Do not invent KPI values, deltas, unavailable-month points, or native XML to imitate a mockup. A latest-value summary needs the latest non-null value for its stated scope and time filter; a maximum is not the latest value.
- Leave connection preservation, calculation reuse, XML checks, backups, and Desktop verification to `tableau-workbook-engineering`.

## Check before delivery

For a design preview, check text height after padding, long labels, controls, thresholds, row alignment, and navigation. State what the preview proves and what still needs Desktop or published verification. When a published view is in scope, inspect those elements in the browser before claiming visual verification.
