# Design system and approval history

## What to reuse

This visual language was developed for a B2B product-health overview and monthly trends. It is a starting point for other Tableau projects, not a requirement to use HEART categories or the original metrics.

The approved trend screenshot in `../assets/approved-trend-reference.png` is an actual user-reviewed view. Reuse hierarchy, spacing, and colors, not the numbers, survey names, products, date range, or datasource.

## Trend typography and components

| Element | Typeface and approximate size | Treatment |
|---|---|---|
| Breadcrumb | Tableau Semibold 10pt | Muted, short, uppercase |
| Product/dashboard heading | Tableau Bold 30pt | Navy; allow real space for the longest name |
| Explanation | Tableau 11pt | Muted; one useful sentence, not another heading |
| Category eyebrow | Tableau Semibold 10pt | Muted, uppercase |
| Metric name | Tableau Semibold 16pt | Navy; allow two lines when needed |
| Plotted value label | Tableau Semibold 12pt | Dark, readable without dominating the plot |
| Supporting note / legend | Tableau 10–11pt | Muted |
| Pending-state heading | Tableau Semibold about 16pt | Gray; missing is not zero |

The original large-value concept used 30–34pt KPI numbers and month-over-month deltas. Those summaries were NOT fully implemented or user-verified. Do not treat them as a finished native template. A future implementation needs a compatible native KPI pattern and calculations that respect the intended reporting period, distinguish percentage-point from relative changes, and label older last-available months clearly.

Use a flat light page with white cards and quiet borders. The generated mockup's gradient, exact font appearance, and shadows are not requirements or proof of native Tableau support. Avoid visual decoration that is hard to publish reliably.

Use consistent card gutters of roughly 16–20px as a starting point, with about 10–14px internal text padding; adapt to the verified workbook geometry. Keep equal plot heights and aligned headings. Favor light horizontal gridlines, restrained axes, small visible point markers, and sparse value labels. The approved native trend uses a blue series (approximately `#4E79A7`); teal/red threshold lines are visually quieter than the series. Do not confuse a series color with the metric's current status color.

The common desktop pattern is two equal-width cards per row for four metrics, with a shorter full-width pending-state card only when the remaining metric has no data. If the fifth metric has real history, retain a full-width chart and enlarge the page rather than replacing it with text or shrinking other plots. Other metric counts may require a different grid.

## Overview: approved and reverted choices

Approved header treatment:

- Navy main title, Tableau Bold about 28pt.
- A compact breadcrumb and a descriptive subtitle.
- Pale amber POC warning rather than alarming red text across a large area.
- A compact status legend rather than a tall explanatory banner.
- Reporting-month filter in an intentionally aligned, compact white panel, preferably aligned with the main heading rather than the page's extreme top edge.
- Short `Trends →` links with no surrounding button border.

Important correction: a generated overview mockup showed larger values, entirely white cards, narrower strips, new gutters, and simplified N/A cells. The implemented matrix did not match well; the user explicitly reverted that PRODUCT-METRIC SECTION to the prior version while retaining the new header. Do NOT reapply the rejected matrix redesign automatically.

For an existing overview, preserve its working matrix unless the user separately approves changes. The retained B2B matrix used approximately 10pt product names, 9pt metric labels, 14pt values, 8pt thresholds, and existing row spacing/strip widths. These are a legacy baseline, not mandatory sizes for a new project. A larger 11/10/17/9pt matrix is a proposal requiring real rendering checks, not the current approved default.

Treat N/A presentation as a user choice. Do not automatically suppress its strip, blank its value/threshold, center it, or change its row height during a typography task. Proposed N/A simplifications were among the matrix changes later reverted.

## Cloud-safe spacing

Font sizes are points; dashboard geometry is pixels. Text needs more height than its nominal font size. Allow line-height, top/bottom padding, wrapping, and browser differences.

A concrete regression to avoid: a 23px footnote object with 8px top and bottom padding leaves only 7px for its text. The successful adjustment reduced padding to 2px, leaving about 19px, sufficient for a short 10pt note. It is the available content area, not “2px everywhere,” that matters.

The three-line trend header originally had about 91px height and was clipped after publishing. The accepted fix used about 110px and reduced padding; 24px was added to the page and downstream content shifted by that amount, preserving plot heights. Adapt this to actual content instead of hard-coding every dashboard to those dimensions.

Keep metric/header sizes small enough for the card's real text area. Do not shrink fonts to hide a geometry problem or add blank space around every product to solve one clipped subtitle.

## Data semantics are not design tokens

- Do not reuse this project's professional-seller, listing, or survey definitions in another domain.
- Use each metric's configured percentage, count, or decimal format. A stored 0.853 may display as 85.3%; a count must not inherit percentage formatting.
- Preserve configured number precision. Do not round a decimal SEQ metric merely because another metric is an integer count.
- Teal/amber/red mapping depends on configured business rules, including whether higher or lower is better. Some projects treat missing thresholds as on-track; that is a business convention, not a universal design rule.
- Null data is not zero. Do not draw a zero-value marker, connect a line through a missing month, or assert “no history” when only the latest month is absent.
