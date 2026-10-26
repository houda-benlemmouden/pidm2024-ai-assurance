#!/usr/bin/env python3
"""Validate the recommendations register for the PIDM2024 Public Safety portfolio.

Run from any working directory:
    python scripts/validate_recommendations_register.py

The script validates the portfolio artefacts only. It does not assess the real
Public Safety system or substantiate the recommendations themselves.
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path
from typing import Iterable

EXPECTED_HEADERS = [
    "recommendation_id",
    "title",
    "related_risk_ids",
    "source_requirement_ids",
    "evidence_gap_ids",
    "recommendation",
    "rationale",
    "proposed_owner_role",
    "priority",
    "dependencies",
    "acceptance_criteria",
    "status",
    "limitations",
]

ALLOWED_PRIORITIES = {"High", "Moderate", "Low"}
ALLOWED_STATUSES = {"Proposed", "In progress", "Complete", "Deferred"}
ID_PATTERNS = {
    "risk": re.compile(r"\bRSK-\d{3}\b"),
    "source requirement": re.compile(r"\bSRC-\d{3}\b"),
    "evidence gap": re.compile(r"\bEG-\d{3}\b"),
}


def extract_ids(text: str, pattern: re.Pattern[str]) -> set[str]:
    return set(pattern.findall(text))


def split_ids(value: str | None) -> list[str]:
    if not value or not value.strip():
        return []
    return [part.strip() for part in value.split(";") if part.strip()]


def report_issue(message: str, errors: list[str]) -> None:
    errors.append(message)


def load_csv(path: Path, errors: list[str]) -> tuple[list[str], list[tuple[int, dict[str, str]]]]:
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle, restkey="__extra_fields__")
            headers = reader.fieldnames or []
            if not headers:
                report_issue(f"{path}: CSV is empty or has no header row.", errors)
                return [], []

            rows: list[tuple[int, dict[str, str]]] = []
            for row_num, raw_row in enumerate(reader, start=2):
                extra = raw_row.pop("__extra_fields__", None)
                values = [raw_row.get(header) for header in headers]
                # Ignore completely blank lines.
                if not any((value or "").strip() for value in values) and not extra:
                    continue
                if extra is not None:
                    report_issue(
                        f"{path}: row {row_num} has {len(headers) + len(extra)} fields; "
                        f"header has {len(headers)}.",
                        errors,
                    )
                missing = [header for header in headers if raw_row.get(header) is None]
                if missing:
                    report_issue(
                        f"{path}: row {row_num} has too few fields; missing trailing "
                        f"field(s): {', '.join(missing)}.",
                        errors,
                    )
                row = {header: (raw_row.get(header) or "").strip() for header in headers}
                rows.append((row_num, row))
            return headers, rows
    except OSError as exc:
        report_issue(f"Unable to read {path}: {exc}", errors)
        return [], []
    except csv.Error as exc:
        report_issue(f"Unable to parse {path}: {exc}", errors)
        return [], []


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    recommendation_path = root / "registers" / "recommendations-register.csv"
    risk_path = root / "registers" / "risk-register.csv"
    source_path = root / "docs" / "source-baseline" / "source-requirements-register.md"
    gaps_path = root / "docs" / "source-baseline" / "evidence-gaps.md"

    errors: list[str] = []
    warnings: list[str] = []

    for required_path in (recommendation_path, risk_path, source_path, gaps_path):
        if not required_path.is_file():
            report_issue(f"Required file not found: {required_path.relative_to(root)}", errors)

    if errors:
        print("Recommendations register validation")
        print("===================================")
        print("\nErrors:")
        for error in errors:
            print(f"  ERROR: {error}")
        print("\nValidation FAILED.")
        return 1

    headers, rows = load_csv(recommendation_path, errors)
    if headers:
        if len(headers) != len(set(headers)):
            report_issue("Recommendations CSV contains duplicate column names.", errors)
        if headers != EXPECTED_HEADERS:
            missing = [name for name in EXPECTED_HEADERS if name not in headers]
            extra = [name for name in headers if name not in EXPECTED_HEADERS]
            if missing:
                report_issue("Missing expected column(s): " + ", ".join(missing), errors)
            if extra:
                report_issue("Unexpected column(s): " + ", ".join(extra), errors)
            if not missing and not extra:
                report_issue("Columns are present but not in the expected order.", errors)

    risk_headers, risk_rows = load_csv(risk_path, errors)
    if "risk_id" not in risk_headers:
        report_issue("Risk register has no 'risk_id' column.", errors)
    elif risk_rows:
        known_risks = {row.get("risk_id", "") for _, row in risk_rows if row.get("risk_id", "")}
    else:
        known_risks = set()
        warnings.append("No risk records found; risk references cannot be validated against populated records.")

    try:
        source_text = source_path.read_text(encoding="utf-8-sig")
        gap_text = gaps_path.read_text(encoding="utf-8-sig")
    except OSError as exc:
        report_issue(f"Unable to read source/evidence-gap register: {exc}", errors)
        source_text, gap_text = "", ""

    known_sources = extract_ids(source_text, ID_PATTERNS["source requirement"])
    known_gaps = extract_ids(gap_text, ID_PATTERNS["evidence gap"])
    if not known_sources:
        warnings.append("No source-requirement IDs were detected in the source-requirements register.")
    if not known_gaps:
        warnings.append("No evidence-gap IDs were detected in the evidence-gaps register.")

    seen_ids: set[str] = set()
    for row_num, row in rows:
        rec_id = row.get("recommendation_id", "")
        prefix = f"Row {row_num}"
        if not rec_id:
            report_issue(f"{prefix}: recommendation_id is blank.", errors)
        elif rec_id in seen_ids:
            report_issue(f"{prefix}: duplicate recommendation_id '{rec_id}'.", errors)
        else:
            seen_ids.add(rec_id)
        if rec_id and not re.fullmatch(r"REC-\d{3}", rec_id):
            report_issue(f"{prefix}: recommendation_id '{rec_id}' must follow REC-NNN format.", errors)

        # These fields must be populated for a usable recommendation record.
        for field in ("title", "related_risk_ids", "source_requirement_ids", "evidence_gap_ids",
                      "recommendation", "rationale", "proposed_owner_role", "priority",
                      "acceptance_criteria", "status", "limitations"):
            if not row.get(field, "").strip():
                report_issue(f"{prefix}: required field '{field}' is blank.", errors)

        priority = row.get("priority", "")
        if priority and priority not in ALLOWED_PRIORITIES:
            report_issue(f"{prefix}: priority must be one of {sorted(ALLOWED_PRIORITIES)}; got '{priority}'.", errors)
        status = row.get("status", "")
        if status and status not in ALLOWED_STATUSES:
            report_issue(f"{prefix}: status must be one of {sorted(ALLOWED_STATUSES)}; got '{status}'.", errors)

        for field, kind, known in (
            ("related_risk_ids", "risk", known_risks),
            ("source_requirement_ids", "source requirement", known_sources),
            ("evidence_gap_ids", "evidence gap", known_gaps),
        ):
            values = split_ids(row.get(field))
            if not values:
                report_issue(f"{prefix}: '{field}' must contain at least one ID.", errors)
                continue
            for value in values:
                if not ID_PATTERNS[kind].fullmatch(value):
                    report_issue(f"{prefix}: malformed {kind} ID '{value}' in '{field}'.", errors)
                elif known and value not in known:
                    report_issue(f"{prefix}: {kind} ID '{value}' in '{field}' was not found in its register.", errors)

        if status == "Complete":
            warnings.append(
                f"{rec_id}: status is Complete; ensure supporting completion evidence is retained."
            )

    print("Recommendations register validation")
    print("===================================")
    print(f"Populated recommendation records checked: {len(rows)}")
    print(f"Expected columns: {len(EXPECTED_HEADERS)}")
    print(f"Known risk IDs: {len(known_risks)}; source-requirement IDs: {len(known_sources)}; evidence-gap IDs: {len(known_gaps)}")

    if warnings:
        print(f"\nWarnings ({len(warnings)}):")
        for warning in warnings:
            print(f"  WARNING: {warning}")

    if errors:
        print(f"\nErrors ({len(errors)}):")
        for error in errors:
            print(f"  ERROR: {error}")
        print("\nValidation FAILED. Correct the errors before relying on the register.")
        return 1

    if not rows:
        print("\nWARNING: No recommendation records found yet; schema checks completed only.")
        print("\nNo validation errors found.")
        return 0

    print("\nNo validation errors found.")
    print("Validation PASSED.")
    print("Note: validation checks structure and references; it does not validate the substance of recommendations.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
