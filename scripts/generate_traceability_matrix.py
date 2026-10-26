"""Generate a risk-centred traceability matrix from the assessment registers."""

from pathlib import Path

import pandas as pd
import re


ROOT = Path(__file__).resolve().parents[1]
REGISTERS = ROOT / "registers"
OUTPUT = ROOT / "docs" / "generated" / "traceability-matrix.csv"

SOURCE_REQUIREMENTS_DOC = (
    ROOT / "docs" / "source-baseline" / "source-requirements-register.md"
)
EVIDENCE_GAPS_DOC = (
    ROOT / "docs" / "source-baseline" / "evidence-gaps.md"
)

PAGE = ROOT / "docs" / "generated" / "index.md"
START_MARKER = "<!-- MATRIX-TABLE-START -->"
END_MARKER = "<!-- MATRIX-TABLE-END -->"

def extract_ids(path: Path, pattern: str) -> set[str]:
    """Extract defined identifiers from a Markdown register."""
    if not path.exists():
        raise FileNotFoundError(f"Markdown register not found: {path}")

    text = path.read_text(encoding="utf-8")
    return set(re.findall(pattern, text))


def load_register(filename: str, required_columns: set[str]) -> pd.DataFrame:
    """Load a CSV register and verify its required columns."""
    path = REGISTERS / filename

    if not path.exists():
        raise FileNotFoundError(f"Register not found: {path}")

    frame = pd.read_csv(path, dtype=str, keep_default_na=False)
    missing = required_columns - set(frame.columns)

    if missing:
        raise ValueError(
            f"{filename} is missing required columns: {sorted(missing)}"
        )

    return frame


def split_ids(value: str) -> list[str]:
    """Split semicolon-separated identifiers without inventing links."""
    if not value or not value.strip():
        return []

    return sorted({
        item.strip()
        for item in value.split(";")
        if item.strip()
    })


def index_records(
    frame: pd.DataFrame,
    id_column: str,
    title_column: str,
) -> dict[str, str]:
    """Map each register ID to its title and reject duplicate IDs."""
    if frame[id_column].duplicated().any():
        duplicates = frame.loc[
            frame[id_column].duplicated(keep=False), id_column
        ].tolist()
        raise ValueError(f"Duplicate IDs in {id_column}: {duplicates}")

    return dict(zip(frame[id_column], frame[title_column]))

def update_matrix_page(matrix: pd.DataFrame) -> None:
    """Insert the generated traceability table into the documentation page."""
    if not PAGE.exists():
        raise FileNotFoundError(f"Matrix page not found: {PAGE}")

    page = PAGE.read_text(encoding="utf-8")

    if page.count(START_MARKER) != 1 or page.count(END_MARKER) != 1:
        raise ValueError(
            "The matrix page must contain exactly one start marker "
            "and one end marker."
        )

    start = page.index(START_MARKER) + len(START_MARKER)
    end = page.index(END_MARKER)

    if end < start:
        raise ValueError("Matrix markers are in the wrong order.")

    columns = [
        ("risk_id", "Risk ID"),
        ("risk_title", "Risk"),
        ("source_requirement_ids", "Source requirements"),
        ("evidence_gap_ids", "Evidence gaps"),
        ("assurance_test_ids", "Assurance tests"),
        ("recommendation_ids", "Recommendations"),
        ("traceability_status", "Reference status"),
    ]

    def cell(value: object) -> str:
        """Format a value safely for a Markdown table cell."""
        return (
            str(value)
            .replace("|", r"\|")
            .replace("\r", " ")
            .replace("\n", " ")
            .strip()
            or "—"
        )

    lines = [
        "| " + " | ".join(label for _, label in columns) + " |",
        "| " + " | ".join("---" for _ in columns) + " |",
    ]

    for _, row in matrix.iterrows():
        lines.append(
            "| "
            + " | ".join(cell(row[column]) for column, _ in columns)
            + " |"
        )

    table = "\n" + "\n".join(lines) + "\n"
    updated = page[:start] + table + page[end:]

    PAGE.write_text(updated, encoding="utf-8")
    print(f"Visible matrix written to: {PAGE.relative_to(ROOT)}")


def main() -> None:
    risks = load_register(
        "risk-register.csv",
        {"risk_id", "title", "source_requirement_ids", "evidence_gap_ids"},
    )
    tests = load_register(
        "assurance-test-register.csv",
        {"test_id", "title", "related_risk_ids"},
    )
    recommendations = load_register(
        "recommendations-register.csv",
        {"recommendation_id", "title", "related_risk_ids"},
    )

    risk_titles = index_records(risks, "risk_id", "title")
    test_titles = index_records(tests, "test_id", "title")
    recommendation_titles = index_records(
        recommendations, "recommendation_id", "title"
    )

        # Load IDs documented in the source-requirements and evidence-gap files.
    valid_source_ids = extract_ids(
        SOURCE_REQUIREMENTS_DOC, r"\bSRC-\d{3}\b"
    )
    valid_gap_ids = extract_ids(
        EVIDENCE_GAPS_DOC, r"\bEG-\d{3}\b"
    )

    # Validate the references recorded in all three assessment registers.
    for register_name, frame, id_column in [
        ("risk register", risks, "risk_id"),
        ("assurance-test register", tests, "test_id"),
        ("recommendations register", recommendations, "recommendation_id"),
    ]:
        for _, record in frame.iterrows():
            record_id = record[id_column]

            for field, valid_ids, label in [
                ("source_requirement_ids", valid_source_ids, "source"),
                ("evidence_gap_ids", valid_gap_ids, "evidence gap"),
            ]:
                if field not in frame.columns:
                    continue

                unknown = set(split_ids(record[field])) - valid_ids

                if unknown:
                    raise ValueError(
                        f"{register_name}: {record_id} references "
                        f"unknown {label} IDs: {sorted(unknown)}"
                    )

    print(f"Source requirement IDs found: {len(valid_source_ids)}")
    print(f"Evidence gap IDs found: {len(valid_gap_ids)}")

    # Confirm that linked tests and recommendations refer to known risks.
    for _, record in tests.iterrows():
        unknown = set(split_ids(record["related_risk_ids"])) - set(risk_titles)
        if unknown:
            raise ValueError(
                f"{record['test_id']} references unknown risks: {sorted(unknown)}"
            )

    for _, record in recommendations.iterrows():
        unknown = (
            set(split_ids(record["related_risk_ids"])) - set(risk_titles)
        )
        if unknown:
            raise ValueError(
                f"{record['recommendation_id']} references unknown risks: "
                f"{sorted(unknown)}"
            )

    rows = []

    for _, risk in risks.iterrows():
        risk_id = risk["risk_id"]

        linked_tests = tests[
            tests["related_risk_ids"].apply(
                lambda value: risk_id in split_ids(value)
            )
        ]
        linked_recommendations = recommendations[
            recommendations["related_risk_ids"].apply(
                lambda value: risk_id in split_ids(value)
            )
        ]

        source_ids = split_ids(risk["source_requirement_ids"])
        gap_ids = split_ids(risk["evidence_gap_ids"])
        test_ids = sorted(linked_tests["test_id"].tolist())
        recommendation_ids = sorted(
            linked_recommendations["recommendation_id"].tolist()
        )

        coverage_notes = []
        if not source_ids:
            coverage_notes.append("No source requirement IDs recorded")
        if not gap_ids:
            coverage_notes.append("No evidence gap IDs recorded")
        if not test_ids:
            coverage_notes.append("No linked assurance test found")
        if not recommendation_ids:
            coverage_notes.append("No linked recommendation found")

        rows.append({
            "risk_id": risk_id,
            "risk_title": risk["title"],
            "source_requirement_ids": "; ".join(source_ids),
            "evidence_gap_ids": "; ".join(gap_ids),
            "assurance_test_ids": "; ".join(test_ids),
            "assurance_test_titles": " | ".join(
                test_titles[item] for item in test_ids
            ),
            "recommendation_ids": "; ".join(recommendation_ids),
            "recommendation_titles": " | ".join(
                recommendation_titles[item]
                for item in recommendation_ids
            ),
            "traceability_status": (
                "References present"
                if not coverage_notes
                else "Review needed: " + "; ".join(coverage_notes)
            ),
        })

    matrix = pd.DataFrame(rows)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    matrix.to_csv(OUTPUT, index=False, encoding="utf-8-sig")
    update_matrix_page(matrix)

    print(f"Risks processed: {len(matrix)}")
    print(f"Matrix written to: {OUTPUT.relative_to(ROOT)}")
    print("\nTraceability status:")
    print(matrix["traceability_status"].value_counts().to_string())


if __name__ == "__main__":
    main()