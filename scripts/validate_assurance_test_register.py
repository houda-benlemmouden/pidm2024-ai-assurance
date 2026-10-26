#!/usr/bin/env python3
"""Validate the proposed assurance-test register for the PIDM2024 portfolio.

Run from any working directory with:
    python scripts/validate_assurance_test_register.py

This checks the portfolio artefacts only. It does not test the real Public Safety system.
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

EXPECTED_HEADERS = [
    "test_id",
    "title",
    "test_type",
    "related_risk_ids",
    "source_requirement_ids",
    "evidence_gap_ids",
    "assurance_question",
    "objective",
    "proposed_procedure",
    "required_evidence",
    "pass_criteria",
    "exception_criteria",
    "prerequisites",
    "test_priority",
    "execution_status",
    "execution_date",
    "results_summary",
    "limitations",
]

REQUIRED_FIELDS = [
    h for h in EXPECTED_HEADERS if h not in {"execution_date", "results_summary"}
]
ALLOWED_STATUSES = {"Proposed", "In progress", "Executed", "Blocked", "Cancelled"}
ID_PATTERN = re.compile(r"^AST-\d{3}$")
REF_PATTERNS = {
    "related_risk_ids": re.compile(r"^RSK-\d{3}$"),
    "source_requirement_ids": re.compile(r"^SRC-\d{3}$"),
    "evidence_gap_ids": re.compile(r"^EG-\d{3}$"),
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def split_refs(value: str | None) -> list[str]:
    if value is None:
        return []
    return [part.strip() for part in value.split(";") if part.strip()]


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def load_existing_ids(path: Path, column: str, errors: list[str]) -> set[str]:
    if not path.exists():
        fail(f"Required reference file not found: {path}", errors)
        return set()
    try:
        with path.open("r", newline="", encoding="utf-8-sig") as handle:
            reader = csv.DictReader(handle)
            if not reader.fieldnames or column not in reader.fieldnames:
                fail(f"Reference file {path} has no '{column}' column.", errors)
                return set()
            return {
                (row.get(column) or "").strip()
                for row in reader
                if (row.get(column) or "").strip()
            }
    except (OSError, csv.Error) as exc:
        fail(f"Could not read reference file {path}: {exc}", errors)
        return set()


def ids_from_markdown(path: Path, pattern: re.Pattern[str], errors: list[str]) -> set[str]:
    if not path.exists():
        fail(f"Required reference file not found: {path}", errors)
        return set()
    try:
        return set(pattern.findall(read_text(path)))
    except OSError as exc:
        fail(f"Could not read reference file {path}: {exc}", errors)
        return set()


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    test_csv = repo_root / "registers" / "assurance-test-register.csv"
    risk_csv = repo_root / "registers" / "risk-register.csv"
    requirements_md = repo_root / "docs" / "source-baseline" / "source-requirements-register.md"
    gaps_md = repo_root / "docs" / "source-baseline" / "evidence-gaps.md"

    errors: list[str] = []
    warnings: list[str] = []

    if not test_csv.exists():
        print(f"ERROR: Assurance-test register not found: {test_csv}")
        return 1

    risk_ids = load_existing_ids(risk_csv, "risk_id", errors)
    source_ids = ids_from_markdown(requirements_md, re.compile(r"\bSRC-\d{3}\b"), errors)
    gap_ids = ids_from_markdown(gaps_md, re.compile(r"\bEG-\d{3}\b"), errors)

    try:
        with test_csv.open("r", newline="", encoding="utf-8-sig") as handle:
            reader = csv.DictReader(handle, restkey="__extra_fields__")
            headers = reader.fieldnames
            if not headers:
                fail("The assurance-test register is empty or has no header row.", errors)
                headers = []
            else:
                if headers != EXPECTED_HEADERS:
                    missing = [h for h in EXPECTED_HEADERS if h not in headers]
                    extra = [h for h in headers if h not in EXPECTED_HEADERS]
                    if missing:
                        fail("Missing header(s): " + ", ".join(missing), errors)
                    if extra:
                        fail("Unexpected header(s): " + ", ".join(extra), errors)
                    if not missing and not extra:
                        fail("Header columns are present but not in the expected order.", errors)

            rows: list[tuple[int, dict[str, str | None]]] = []
            for row_num, row in enumerate(reader, start=2):
                extra_fields = row.pop("__extra_fields__", None)
                if not any((row.get(h) or "").strip() for h in EXPECTED_HEADERS) and not extra_fields:
                    continue

                missing_fields = [h for h in EXPECTED_HEADERS if row.get(h) is None]
                if extra_fields is not None:
                    fail(
                        f"Row {row_num}: row has {len(EXPECTED_HEADERS) + len(extra_fields)} "
                        f"fields but the header has {len(EXPECTED_HEADERS)}.", errors
                    )
                if missing_fields:
                    fail(
                        f"Row {row_num}: row has too few fields; missing trailing field(s): "
                        + ", ".join(missing_fields), errors
                    )
                rows.append((row_num, row))
    except (OSError, csv.Error) as exc:
        print(f"ERROR: Could not read {test_csv}: {exc}")
        return 1

    seen_test_ids: set[str] = set()
    for row_num, row in rows:
        test_id = (row.get("test_id") or "").strip()
        if not ID_PATTERN.fullmatch(test_id):
            fail(f"Row {row_num}: invalid test_id {test_id!r}; expected AST-###.", errors)
        elif test_id in seen_test_ids:
            fail(f"Row {row_num}: duplicate test_id {test_id}.", errors)
        seen_test_ids.add(test_id)

        for field in REQUIRED_FIELDS:
            if not (row.get(field) or "").strip():
                fail(f"Row {row_num}: required field '{field}' is blank.", errors)

        status = (row.get("execution_status") or "").strip()
        if status and status not in ALLOWED_STATUSES:
            fail(
                f"Row {row_num}: execution_status must be one of "
                + ", ".join(sorted(ALLOWED_STATUSES)) + f"; got {status!r}.", errors
            )
        execution_date = (row.get("execution_date") or "").strip()
        results_summary = (row.get("results_summary") or "").strip()
        if status == "Proposed" and (execution_date or results_summary):
            fail(f"Row {row_num}: Proposed tests must not have execution_date or results_summary.", errors)
        if status == "Executed" and (not execution_date or not results_summary):
            fail(f"Row {row_num}: Executed tests require execution_date and results_summary.", errors)
        if execution_date and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", execution_date):
            fail(f"Row {row_num}: execution_date must use YYYY-MM-DD format.", errors)

        priority = (row.get("test_priority") or "").strip()
        if priority not in {"Critical", "High", "Moderate", "Low"}:
            fail(f"Row {row_num}: test_priority must be Critical, High, Moderate or Low; got {priority!r}.", errors)

        for field, pattern in REF_PATTERNS.items():
            refs = split_refs(row.get(field))
            if not refs:
                fail(f"Row {row_num}: '{field}' must contain at least one semicolon-separated reference.", errors)
                continue
            if len(refs) != len(set(refs)):
                fail(f"Row {row_num}: duplicate reference in '{field}'.", errors)
            valid_ids = {
                "related_risk_ids": risk_ids,
                "source_requirement_ids": source_ids,
                "evidence_gap_ids": gap_ids,
            }[field]
            for ref in refs:
                if not pattern.fullmatch(ref):
                    fail(f"Row {row_num}: malformed reference {ref!r} in '{field}'.", errors)
                elif valid_ids and ref not in valid_ids:
                    fail(f"Row {row_num}: {ref} in '{field}' was not found in its reference register.", errors)

        if (row.get("execution_status") or "").strip() == "Proposed":
            procedure = (row.get("proposed_procedure") or "").lower()
            if any(term in procedure for term in ("if authorised", "if authorised access", "if access is authorised")):
                if not (row.get("limitations") or "").strip():
                    warnings.append(f"Row {row_num}: technical work is conditional on authorisation; ensure limitations are recorded.")

    print("Assurance-test register validation")
    print("==================================")
    print(f"Populated test records checked: {len(rows)}")
    print("Expected fields per record: 18")
    print(f"Reference IDs loaded: {len(risk_ids)} risks, {len(source_ids)} source requirements, {len(gap_ids)} evidence gaps")

    if not rows:
        warnings.append("No assurance-test records found; schema and reference files were checked, but record-level validation awaits populated rows.")

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

    print("\nNo validation errors found.")
    print("Validation PASSED.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
