#!/usr/bin/env python3
"""Validate the project risk register against its schema, scoring rules and traceability IDs.

Run from the repository root:
    python scripts/validate_risk_register.py

This checks assessment artefacts only. It does not validate the real system or prove
that controls are implemented or effective.
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RISK_CSV = ROOT / "registers" / "risk-register.csv"
REQUIREMENTS_MD = ROOT / "docs" / "source-baseline" / "source-requirements-register.md"
GAPS_MD = ROOT / "docs" / "source-baseline" / "evidence-gaps.md"

EXPECTED_HEADERS = [
    "risk_id", "title", "category", "risk_scenario", "cause_or_condition",
    "potential_consequence", "affected_stakeholders", "source_requirement_ids",
    "evidence_gap_ids", "inherent_impact_score", "inherent_impact_rationale",
    "inherent_likelihood_score", "inherent_likelihood_rationale",
    "likelihood_context_and_timeframe", "inherent_score", "inherent_rating",
    "evidence_confidence", "documented_controls", "control_status",
    "control_evidence_and_limitations", "residual_impact_score",
    "residual_likelihood_score", "residual_score", "residual_rating",
    "residual_assessment_status", "additional_evidence_required", "proposed_response",
]

RATING_BANDS = (
    (1, 4, "Low"),
    (5, 9, "Moderate"),
    (10, 16, "High"),
    (17, 25, "Critical"),
)
CONFIDENCE_VALUES = {"high", "moderate", "low"}
SCORE_FIELDS = {
    "inherent_impact_score", "inherent_likelihood_score",
    "residual_impact_score", "residual_likelihood_score",
}


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def rating_for(score: int) -> str:
    for lower, upper, label in RATING_BANDS:
        if lower <= score <= upper:
            return label
    raise ValueError(f"Risk score outside expected 1–25 range: {score}")


def load_ids(path: Path, prefix: str) -> set[str]:
    if not path.exists():
        raise FileNotFoundError(path)
    text = path.read_text(encoding="utf-8")
    return set(re.findall(rf"\b{re.escape(prefix)}-\d{{3}}\b", text))


def parse_score(value: str, field: str, row_num: int, errors: list[str]) -> int | None:
    value = (value or "").strip()
    if not value:
        return None
    try:
        score = int(value)
    except ValueError:
        fail(f"Row {row_num}: {field} must be an integer from 1 to 5 or blank; got {value!r}.", errors)
        return None
    if score < 1 or score > 5:
        fail(f"Row {row_num}: {field} must be between 1 and 5; got {score}.", errors)
        return None
    return score


def check_reference_cell(value: str, prefix: str, known_ids: set[str], field: str,
                         row_num: int, errors: list[str]) -> None:
    if not (value or "").strip():
        return
    found = set(re.findall(rf"\b{re.escape(prefix)}-\d{{3}}\b", value))
    if not found:
        fail(f"Row {row_num}: {field} contains text but no {prefix}-NNN reference was found.", errors)
        return
    unknown = sorted(found - known_ids)
    for ref in unknown:
        fail(f"Row {row_num}: {field} references unknown ID {ref}.", errors)


def validate() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    required_paths = (RISK_CSV, REQUIREMENTS_MD, GAPS_MD)
    missing = [p for p in required_paths if not p.exists()]
    if missing:
        for path in missing:
            errors.append(f"Required file not found: {path.relative_to(ROOT) if path.is_relative_to(ROOT) else path}")
        print_report(errors, warnings, 0)
        return 1

    try:
        known_src = load_ids(REQUIREMENTS_MD, "SRC")
        known_eg = load_ids(GAPS_MD, "EG")
    except (OSError, UnicodeError) as exc:
        print(f"ERROR: Could not read reference registers: {exc}")
        return 1

    try:
        with RISK_CSV.open("r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            headers = reader.fieldnames or []
            if not headers:
                fail("Risk register is empty or has no header row.", errors)
                print_report(errors, warnings, 0)
                return 1
            if len(headers) != len(set(headers)):
                fail("Header row contains duplicate column names.", errors)
            missing_headers = [h for h in EXPECTED_HEADERS if h not in headers]
            extra_headers = [h for h in headers if h not in EXPECTED_HEADERS]
            if missing_headers:
                fail("Missing expected columns: " + ", ".join(missing_headers), errors)
            if extra_headers:
                warnings.append("Additional columns found (review whether intentional): " + ", ".join(extra_headers))

            rows = []
            for row_num, row in enumerate(reader, start=2):
                # Ignore completely blank rows, but not partially completed records.
                if not any((v or "").strip() for v in row.values()):
                    continue
                rows.append((row_num, row))
    except (OSError, csv.Error, UnicodeError) as exc:
        print(f"ERROR: Could not read risk register: {exc}")
        return 1

    if not rows:
        warnings.append("No risk records found yet; schema and scoring rules were checked, but record-level checks await populated rows.")

    seen_ids: set[str] = set()
    for row_num, row in rows:
        risk_id = (row.get("risk_id") or "").strip()
        if not risk_id:
            fail(f"Row {row_num}: risk_id is required.", errors)
        elif risk_id in seen_ids:
            fail(f"Row {row_num}: duplicate risk_id {risk_id}.", errors)
        seen_ids.add(risk_id)

        for field in ("title", "category", "risk_scenario", "cause_or_condition",
                      "potential_consequence", "affected_stakeholders"):
            if not (row.get(field) or "").strip():
                fail(f"Row {row_num}: {field} is required for a populated risk record.", errors)

        check_reference_cell(row.get("source_requirement_ids", ""), "SRC", known_src,
                             "source_requirement_ids", row_num, errors)
        check_reference_cell(row.get("evidence_gap_ids", ""), "EG", known_eg,
                             "evidence_gap_ids", row_num, errors)

        confidence = (row.get("evidence_confidence") or "").strip().lower()
        if confidence and confidence not in CONFIDENCE_VALUES:
            fail(f"Row {row_num}: evidence_confidence must be High, Moderate or Low; got {row.get('evidence_confidence')!r}.", errors)

        inherent_impact = parse_score(row.get("inherent_impact_score", ""), "inherent_impact_score", row_num, errors)
        inherent_likelihood = parse_score(row.get("inherent_likelihood_score", ""), "inherent_likelihood_score", row_num, errors)
        inherent_score_text = (row.get("inherent_score") or "").strip()
        inherent_rating = (row.get("inherent_rating") or "").strip()
        if inherent_impact is not None and inherent_likelihood is not None:
            expected_score = inherent_impact * inherent_likelihood
            if inherent_score_text:
                try:
                    if int(inherent_score_text) != expected_score:
                        fail(f"Row {row_num}: inherent_score should be {expected_score} ({inherent_impact} × {inherent_likelihood}).", errors)
                except ValueError:
                    fail(f"Row {row_num}: inherent_score must be an integer or blank.", errors)
            else:
                warnings.append(f"Row {row_num}: inherent_score is blank although both dimensions are scored; expected {expected_score}.")
            expected_rating = rating_for(expected_score)
            if inherent_rating and inherent_rating.casefold() != expected_rating.casefold():
                fail(f"Row {row_num}: inherent_rating should be {expected_rating} for score {expected_score}.", errors)
            elif not inherent_rating:
                warnings.append(f"Row {row_num}: inherent_rating is blank although both dimensions are scored; expected {expected_rating}.")
        elif inherent_score_text or inherent_rating:
            fail(f"Row {row_num}: do not calculate inherent_score/rating unless both impact and likelihood are scored.", errors)

        residual_impact = parse_score(row.get("residual_impact_score", ""), "residual_impact_score", row_num, errors)
        residual_likelihood = parse_score(row.get("residual_likelihood_score", ""), "residual_likelihood_score", row_num, errors)
        residual_score_text = (row.get("residual_score") or "").strip()
        residual_rating = (row.get("residual_rating") or "").strip()
        if residual_impact is not None and residual_likelihood is not None:
            expected_score = residual_impact * residual_likelihood
            if residual_score_text:
                try:
                    if int(residual_score_text) != expected_score:
                        fail(f"Row {row_num}: residual_score should be {expected_score} ({residual_impact} × {residual_likelihood}).", errors)
                except ValueError:
                    fail(f"Row {row_num}: residual_score must be an integer or blank.", errors)
            else:
                warnings.append(f"Row {row_num}: residual_score is blank although both dimensions are scored; expected {expected_score}.")
            expected_rating = rating_for(expected_score)
            if residual_rating and residual_rating.casefold() != expected_rating.casefold():
                fail(f"Row {row_num}: residual_rating should be {expected_rating} for score {expected_score}.", errors)
            elif not residual_rating:
                warnings.append(f"Row {row_num}: residual_rating is blank although both dimensions are scored; expected {expected_rating}.")
            status = (row.get("residual_assessment_status") or "").strip().lower()
            if "not assessable" in status or "unassessed" in status or "not assessed" in status:
                fail(f"Row {row_num}: residual fields are scored but residual_assessment_status says not assessed.", errors)
        elif residual_score_text or residual_rating:
            fail(f"Row {row_num}: do not calculate residual_score/rating unless both residual dimensions are scored.", errors)

    print_report(errors, warnings, len(rows))
    return 1 if errors else 0


def print_report(errors: list[str], warnings: list[str], row_count: int) -> None:
    print("Risk register validation")
    print("========================")
    print(f"Populated risk records checked: {row_count}")
    print("Scoring bands: 1–4 Low; 5–9 Moderate; 10–16 High; 17–25 Critical")
    if warnings:
        print(f"\nWarnings ({len(warnings)}):")
        for warning in warnings:
            print(f"  WARNING: {warning}")
    if errors:
        print(f"\nErrors ({len(errors)}):")
        for error in errors:
            print(f"  ERROR: {error}")
        print("\nValidation FAILED. Correct the errors before relying on the register.")
    else:
        print("\nNo validation errors found.")
        if warnings:
            print("Review the warnings; they may be expected while records are still being drafted.")
        else:
            print("Validation PASSED.")


if __name__ == "__main__":
    sys.exit(validate())
