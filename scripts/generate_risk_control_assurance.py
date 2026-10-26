"""Generate a risk-centred control and assurance mapping."""

from pathlib import Path
import re

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
REGISTERS = ROOT / "registers"
OUTPUT_DIR = ROOT / "docs" / "generated"
OUTPUT_CSV = OUTPUT_DIR / "risk-control-assurance.csv"

PAGE = ROOT / "docs" / "analysis" / "risk-controls-assurance.md"
START_MARKER = "<!-- CONTROL-MAPPING-START -->"
END_MARKER = "<!-- CONTROL-MAPPING-END -->"

SOURCE_DOC = ROOT / "docs" / "source-baseline" / "source-requirements-register.md"
GAPS_DOC = ROOT / "docs" / "source-baseline" / "evidence-gaps.md"


def load_register(filename: str, required: set[str]) -> pd.DataFrame:
    """Load a register and check its required columns."""
    path = REGISTERS / filename
    if not path.exists():
        raise FileNotFoundError(f"Register not found: {path}")

    frame = pd.read_csv(
        path, dtype=str, keep_default_na=False, encoding="utf-8-sig"
    )

    missing = required - set(frame.columns)
    if missing:
        raise ValueError(f"{filename} is missing columns: {sorted(missing)}")

    return frame


def split_ids(value: str) -> list[str]:
    """Parse semicolon-separated identifiers."""
    if not value or not value.strip():
        return []

    return sorted({item.strip() for item in value.split(";") if item.strip()})


def clean(value: object) -> str:
    """Normalise text for readable output."""
    return re.sub(r"\s+", " ", str(value or "")).strip()


def extract_ids(path: Path, pattern: str) -> set[str]:
    """Extract identifiers documented in a Markdown register."""
    if not path.exists():
        raise FileNotFoundError(f"Document not found: {path}")

    return set(re.findall(pattern, path.read_text(encoding="utf-8")))


def validate_references(
    frame: pd.DataFrame,
    id_column: str,
    valid_risks: set[str],
    valid_sources: set[str],
    valid_gaps: set[str],
    register_name: str,
) -> None:
    """Fail if a register contains risk, source, or gap IDs that are unknown."""
    for _, record in frame.iterrows():
        record_id = record[id_column]

        checks = [
            ("related_risk_ids", valid_risks, "risk"),
            ("source_requirement_ids", valid_sources, "source requirement"),
            ("evidence_gap_ids", valid_gaps, "evidence gap"),
        ]

        for field, valid_ids, label in checks:
            if field not in frame.columns:
                continue

            unknown = set(split_ids(record[field])) - valid_ids
            if unknown:
                raise ValueError(
                    f"{register_name} {record_id} references unknown "
                    f"{label} IDs: {sorted(unknown)}"
                )


def format_list(values: list[str]) -> str:
    """Format a list for the generated Markdown page."""
    return ", ".join(values) if values else "None recorded"


def update_page(sections: str) -> None:
    """Replace the content between the page's generated-content markers."""
    if not PAGE.exists():
        raise FileNotFoundError(f"Assurance page not found: {PAGE}")

    page = PAGE.read_text(encoding="utf-8")

    if page.count(START_MARKER) != 1 or page.count(END_MARKER) != 1:
        raise ValueError(
            "The assurance page must contain exactly one start marker "
            "and one end marker."
        )

    start = page.index(START_MARKER) + len(START_MARKER)
    end = page.index(END_MARKER)

    if end < start:
        raise ValueError("Control-mapping markers are in the wrong order.")

    updated = page[:start] + "\n\n" + sections.strip() + "\n\n" + page[end:]
    PAGE.write_text(updated, encoding="utf-8")
    print(f"Website mapping updated: {PAGE.relative_to(ROOT)}")


def main() -> None:
    risks = load_register(
        "risk-register.csv",
        {
            "risk_id", "title", "risk_scenario",
            "source_requirement_ids", "evidence_gap_ids",
            "evidence_confidence", "assessment_priority",
            "control_status", "control_evidence_and_limitations",
            "additional_evidence_required",
        },
    )
    tests = load_register(
        "assurance-test-register.csv",
        {
            "test_id", "title", "related_risk_ids",
            "source_requirement_ids", "evidence_gap_ids",
            "objective", "proposed_procedure", "required_evidence",
            "pass_criteria", "execution_status",
        },
    )
    recommendations = load_register(
        "recommendations-register.csv",
        {
            "recommendation_id", "title", "related_risk_ids",
            "source_requirement_ids", "evidence_gap_ids",
            "recommendation", "acceptance_criteria", "status",
        },
    )

    for frame, id_column, filename in [
        (risks, "risk_id", "risk-register.csv"),
        (tests, "test_id", "assurance-test-register.csv"),
        (recommendations, "recommendation_id", "recommendations-register.csv"),
    ]:
        if frame[id_column].duplicated().any():
            raise ValueError(f"Duplicate IDs found in {filename}.")

    valid_risks = set(risks["risk_id"])
    valid_sources = extract_ids(SOURCE_DOC, r"\bSRC-\d{3}\b")
    valid_gaps = extract_ids(GAPS_DOC, r"\bEG-\d{3}\b")

    validate_references(
        risks, "risk_id", valid_risks, valid_sources, valid_gaps, "Risk register"
    )
    validate_references(
        tests, "test_id", valid_risks, valid_sources, valid_gaps,
        "Assurance-test register",
    )
    validate_references(
        recommendations, "recommendation_id", valid_risks,
        valid_sources, valid_gaps, "Recommendations register",
    )

    valid_test_ids = set(tests["test_id"])
    valid_rec_ids = set(recommendations["recommendation_id"])

    rows = []
    sections = []

    for _, risk in risks.iterrows():
        risk_id = risk["risk_id"]
        source_ids = split_ids(risk["source_requirement_ids"])
        gap_ids = split_ids(risk["evidence_gap_ids"])

        linked_tests = tests[
            tests["related_risk_ids"].apply(
                lambda value: risk_id in split_ids(value)
            )
        ]
        linked_recs = recommendations[
            recommendations["related_risk_ids"].apply(
                lambda value: risk_id in split_ids(value)
            )
        ]

        test_ids = sorted(linked_tests["test_id"].tolist())
        rec_ids = sorted(linked_recs["recommendation_id"].tolist())

        # Build the structured record used for download and further analysis.
        rows.append({
            "risk_id": risk_id,
            "risk_title": risk["title"],
            "risk_scenario": risk["risk_scenario"],
            "source_requirement_ids": "; ".join(source_ids),
            "evidence_gap_ids": "; ".join(gap_ids),
            "evidence_confidence": risk["evidence_confidence"],
            "assessment_priority": risk["assessment_priority"],
            "control_status": risk["control_status"],
            "control_evidence_and_limitations":
                risk["control_evidence_and_limitations"],
            "additional_evidence_required":
                risk["additional_evidence_required"],
            "assurance_test_ids": "; ".join(test_ids),
            "assurance_test_titles": " | ".join(
                clean(test["title"]) for _, test in linked_tests.iterrows()
            ),
            "assurance_test_statuses": "; ".join(
                clean(test["execution_status"])
                for _, test in linked_tests.iterrows()
            ),
            "assurance_test_objectives": " || ".join(
                clean(test["objective"]) for _, test in linked_tests.iterrows()
            ),
            "assurance_test_procedures": " || ".join(
                clean(test["proposed_procedure"])
                for _, test in linked_tests.iterrows()
            ),
            "required_assurance_evidence": " || ".join(
                clean(test["required_evidence"])
                for _, test in linked_tests.iterrows()
            ),
            "recommendation_ids": "; ".join(rec_ids),
            "recommendation_titles": " | ".join(
                clean(rec["title"]) for _, rec in linked_recs.iterrows()
            ),
            "recommendation_statuses": "; ".join(
                clean(rec["status"]) for _, rec in linked_recs.iterrows()
            ),
            "recommendations": " || ".join(
                clean(rec["recommendation"])
                for _, rec in linked_recs.iterrows()
            ),
            "recommendation_acceptance_criteria": " || ".join(
                clean(rec["acceptance_criteria"])
                for _, rec in linked_recs.iterrows()
            ),
        })

        # Build a readable section for the documentation website.
        section = [
            f"### {risk_id} — {clean(risk['title'])}",
            "",
            f"**Assessment priority:** {clean(risk['assessment_priority'])}<br>",
            f"**Evidence confidence:** {clean(risk['evidence_confidence'])}",
            "",
            f"**Risk scenario:** {clean(risk['risk_scenario'])}",
            "",
            f"**Source requirements:** {format_list(source_ids)}<br>",
            f"**Evidence gaps:** {format_list(gap_ids)}",
            "",
            f"**Control position:** {clean(risk['control_status'])}",
            "",
            f"**Evidence reviewed and limitations:** "
            f"{clean(risk['control_evidence_and_limitations'])}",
            "",
            f"**Further evidence required:** "
            f"{clean(risk['additional_evidence_required'])}",
            "",
            "**Linked assurance tests:**",
        ]

        if linked_tests.empty:
            section.append("- No linked assurance test recorded.")
        else:
            for _, test in linked_tests.iterrows():
                section.extend([
                    f"- **{test['test_id']} — {clean(test['title'])}** "
                    f"(Execution status: {clean(test['execution_status'])}).",
                    f"  - Objective: {clean(test['objective'])}",
                    f"  - Proposed procedure: {clean(test['proposed_procedure'])}",
                    f"  - Required evidence: {clean(test['required_evidence'])}",
                    f"  - Pass criteria: {clean(test['pass_criteria'])}",
                ])

        section.extend(["", "**Linked recommendations:**"])

        if linked_recs.empty:
            section.append("- No linked recommendation recorded.")
        else:
            for _, rec in linked_recs.iterrows():
                section.extend([
                    f"- **{rec['recommendation_id']} — {clean(rec['title'])}** "
                    f"(Status: {clean(rec['status'])}).",
                    f"  - Proposed action: {clean(rec['recommendation'])}",
                    f"  - Acceptance criteria: {clean(rec['acceptance_criteria'])}",
                ])

        section.append("")
        sections.append("\n".join(section))

    matrix = pd.DataFrame(rows)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    matrix.to_csv(OUTPUT_CSV, index=False, encoding="utf-8-sig")
    update_page("\n\n".join(sections))

    print(f"Risks mapped: {len(matrix)}")
    print(f"Source requirement IDs recognised: {len(valid_sources)}")
    print(f"Evidence-gap IDs recognised: {len(valid_gaps)}")
    print(f"Assurance tests linked: {len(valid_test_ids)}")
    print(f"Recommendations linked: {len(valid_rec_ids)}")
    print(f"CSV written to: {OUTPUT_CSV.relative_to(ROOT)}")
    print("Validation passed: no unknown risk, source, or evidence-gap IDs found.")
    print(
        "Scope note: this is a risk-centred mapping, not a complete inventory "
        "of individually identified controls."
    )


if __name__ == "__main__":
    main()