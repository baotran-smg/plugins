# Tableau interaction and delivery lessons

## Controls need a real worksheet anchor

Date filters copied from a template must not remain attached to a worksheet that was replaced by a static text card. In the B2B case, every time control initially referenced Happiness; dashboards without a displayed Happiness chart lost their filter controls after opening/saving.

Attach the control to an actual worksheet displayed in the relevant layout. The anchor can differ by product: an Adoption chart, Engagement chart, or another visible metric. Recheck default and phone layouts. XML existence alone does not prove the control will remain visible.

Apply the selected period to the intended charts, with groups isolated per product/dashboard unless synchronized filtering was requested. Keep a month selector on an overview separate from a trend's multi-month range. Preserve actual date grain; sorting formatted month strings alphabetically is not chronological sorting.

For a dashboard with no available charts, decide with the user whether a period control is useful. Show a clear unavailable state; do not invent a hidden chart or missing native XML to make a control appear. A dedicated visible, native date/coverage worksheet can be designed when a date control is genuinely required despite no metric values.

## Two native threshold lines

- Preserve both the original/native user pattern and correct field bindings. Add a second line; do not edit one line from green to red and mistake that for two lines.
- Use separately identified lines with the distinct draw order shown by the compatible native template. The user-saved working pair used independent reference IDs and draw orders.
- Keep style entries associated with the right line. Remove obsolete duplicates. Do not assume six- and eight-character color values have interchangeable opacity behavior; preserve a known-good native color representation.
- Use configured fields such as green_min/red_max, not hard-coded sample values. Keep null thresholds absent. Do not replace missing thresholds with zero.
- Reference labels need their own unit formatting: percentage for rates, numeric for scores/counts. Default field formatting may not be enough.
- A full-table minimum threshold assumes a constant boundary across the visible months. If historical boundaries vary, use an appropriate per-period representation rather than flattening the history silently.

For TWB ordering and other schema requirements, read the available `tableau-workbook-engineering` skill before editing.

## Status strips, matrices, and navigation

Square marks can couple visible width and height. Narrowing a status-sheet column previously shortened the strip. Preserve the user's confirmed geometry; choose a native, independently sized bar/Gantt pattern only when a compatible template is available and the change is authorized.

Worksheet row shading/banding can override a white pane or cell background. Do not assume a page/background-color change disables banding. Use Tableau's native shading controls/pattern and verify in the published view. Stop and request a small native example if an unsupported style representation is the remaining blocker.

Keep product-label, metric, status-strip, and navigation rows aligned through filtering and viewport changes. Horizontal auto-layout once collapsed Product Labels to about 10px beside container-based metric columns. Use a verified stable sizing/layout pattern and check the product column explicitly after edits.

Prefer native Navigation objects for product-to-trend links when tooltip menu actions do not work in the published dashboard. A menu on a shared Product Labels sheet may show every product's actions rather than route automatically.

Static row-aligned navigation buttons are not data-bound: adding, removing, sorting, or filtering products can misroute them. Either constrain and verify row order, update the mapping with the product list, or choose a verified dynamic navigation design. Do not sell static buttons as automatic routing.

Keep captions short enough to fit (`Trends →`) and remove borders only when requested/approved. Preserve actual target window identities during duplication; the displayed dashboard name is not necessarily the navigation identity.

## Workbook and data-source lifecycle

Keep workbook UI publishing separate from data-source publishing. A Desktop workbook still connected directly to BigQuery can overwrite a Cloud-only extract setup when republished. For a reusable Cloud extract, connect the saved workbook to the separately published data source and preserve that connection for later layout edits.

Do not switch live/extract modes, replace data sources, modify OAuth, publish a source, create refresh schedules, or edit warehouse objects as an incidental styling step. Those are distinct operations requiring scope and verified configuration. A live connection to a published Tableau source can still use the source's server-side extract.

Never package a project's credentials, connection-bearing TWB, warehouse queries, or metric data as a cross-project skill template. Keep the reusable skill visual and behavioral; obtain the new project's actual sources and authorization separately.

## Evidence levels and stopping conditions

1. Structural audit: source parses; identifiers, dependencies, filters, targets, and XML ordering are coherent.
2. Desktop check: final file opens and displays correctly in the installed compatible version.
3. Published check: the relevant browser view actually shows the expected text, controls, lines, and interactions.

These are different claims. Follow current project instructions about required checks. If the user explicitly waives a check for this run, identify the omitted check in the handoff; do not treat it as permanently waived.

If a native pattern is missing, finish independent safe work and state exactly what remains blocked. Do not quietly substitute static KPI numbers, fabricate native elements, or repeatedly publish speculative repairs. Request one compatible native example for the missing feature. When a user reverts a section, restore only that section's relevant formatting from a recoverable reference; preserve current month selections, datasource connection, other dashboards, and unrelated new work.
