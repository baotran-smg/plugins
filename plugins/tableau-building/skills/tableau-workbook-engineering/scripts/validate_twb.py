#!/usr/bin/env python3
import argparse
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree as ET


def names(root: ET.Element, section: str, tag: str) -> list[str]:
    container = root.find(section)
    if container is None:
        return []
    return [element.get("name", "") for element in container.findall(tag)]


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate key Tableau TWB XML invariants")
    parser.add_argument("workbook", type=Path)
    parser.add_argument("--legacy-compatible", action="store_true")
    args = parser.parse_args()

    root = ET.parse(args.workbook).getroot()
    errors: list[str] = []

    manifest = root.find("document-format-change-manifest")
    features = {element.tag for element in manifest} if manifest is not None else set()
    simple_ids = list(root.iter("simple-id"))
    persistent_ids = "WindowsPersistSimpleIdentifiers" in features

    if persistent_ids != bool(simple_ids):
        errors.append(
            "WindowsPersistSimpleIdentifiers and simple-id elements must be present or absent together"
        )
    if args.legacy_compatible and (persistent_ids or simple_ids):
        errors.append("legacy-compatible workbooks must omit persistent simple identifiers")

    for section, tag in (
        ("datasources", "datasource"),
        ("worksheets", "worksheet"),
        ("dashboards", "dashboard"),
    ):
        values = names(root, section, tag)
        duplicates = sorted(name for name, count in Counter(values).items() if name and count > 1)
        if duplicates:
            errors.append(f"duplicate {section}: {', '.join(duplicates)}")

    worksheet_names = set(names(root, "worksheets", "worksheet"))
    dashboard_names = set(names(root, "dashboards", "dashboard"))
    non_sheet_zone_types = {
        "layout-basic", "text", "filter", "title", "paramctrl", "empty", "image", "web"
    }
    for dashboard in root.findall("./dashboards/dashboard"):
        for zone in dashboard.findall(".//zone"):
            zone_name = zone.get("name")
            zone_type = zone.get("type-v2")
            if (
                zone_name
                and zone_name not in worksheet_names
                and zone_name not in dashboard_names
                and zone_type not in non_sheet_zone_types
            ):
                errors.append(
                    f"dashboard {dashboard.get('name')} references missing sheet {zone_name}"
                )

    # Datasource sorts cannot resolve worksheet-scoped field instances.
    for datasource in root.findall("./datasources/datasource"):
        instances = {node.get("name") for node in datasource.findall("column-instance")}
        for sort in datasource.findall("./default-sorts/*"):
            column = sort.get("column", "")
            # Encoded instances, e.g. [none:product:nk], require a declaration
            # in this datasource. Base-field sort syntax is left unchanged.
            if column.startswith("[") and ":" in column and column not in instances:
                errors.append(
                    f"datasource {datasource.get('name')} default sort references "
                    f"undefined datasource-level column-instance {column}; "
                    "worksheet declarations do not establish datasource scope"
                )

    datasource_boundaries = {
        "layout", "style", "semantic-values", "date-options", "default-date-format",
        "default-sorts", "field-sort-info", "datasource-dependencies", "filter", "object-graph",
    }
    for datasource in root.findall("./datasources/datasource"):
        boundary_seen = False
        for child in datasource:
            if child.tag in datasource_boundaries:
                boundary_seen = True
            elif child.tag in ("column", "column-instance") and boundary_seen:
                errors.append(
                    f"datasource {datasource.get('name')} has {child.tag} after layout/semantic metadata"
                )
                break

    view_boundaries = {
        "computed-sort", "manual-sort", "natural-sort", "alphabetic-sort",
        "perspectives", "shelf-sorts", "slices", "aggregation",
    }
    for worksheet in root.findall("./worksheets/worksheet"):
        view = worksheet.find("./table/view")
        if view is None:
            continue
        boundary_seen = False
        for child in view:
            if child.tag in view_boundaries:
                boundary_seen = True
            elif child.tag == "filter" and boundary_seen:
                errors.append(
                    f"worksheet {worksheet.get('name')} has filter after sort/slices/aggregation"
                )
                break

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(
        f"OK: {args.workbook} | datasources={len(names(root, 'datasources', 'datasource'))} "
        f"worksheets={len(worksheet_names)} dashboards={len(dashboard_names)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
