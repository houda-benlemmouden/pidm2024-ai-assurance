"""Generate an evidence-gap coverage matrix and interactive heatmap."""

import re
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go


ROOT = Path(__file__).resolve().parents[1]
RISK_REGISTER = ROOT / "registers" / "risk-register.csv"
GAPS_DOCUMENT = ROOT / "docs" / "source-baseline" / "evidence-gaps.md"
OUTPUT_DIR = ROOT / "docs" / "generated"

MATRIX_CSV = OUTPUT_DIR / "evidence-gap-coverage.csv"
HEATMAP_HTML = OUTPUT_DIR / "evidence-gap-coverage.html"


def split_ids(value: str) -> list[str]:
    """Parse semicolon-separated IDs."""
    if not value or not value.strip():
        return []

    return sorted({
        item.strip()
        for item in value.split(";")
        if item.strip()
    })


def main() -> None:
    if not RISK_REGISTER.exists():
        raise FileNotFoundError(f"Risk register not found: {RISK_REGISTER}")

    if not GAPS_DOCUMENT.exists():
        raise FileNotFoundError(f"Evidence-gap document not found: {GAPS_DOCUMENT}")

    risks = pd.read_csv(
        RISK_REGISTER,
        dtype=str,
        keep_default_na=False,
        encoding="utf-8-sig",
    )

    required = {"risk_id", "title", "evidence_gap_ids"}
    missing = required - set(risks.columns)
    if missing:
        raise ValueError(f"Risk register missing columns: {sorted(missing)}")

    if risks["risk_id"].duplicated().any():
        raise ValueError("Duplicate risk IDs found.")

    gap_text = GAPS_DOCUMENT.read_text(encoding="utf-8")
    gap_ids = sorted(set(re.findall(r"\bEG-\d{3}\b", gap_text)))

    if not gap_ids:
        raise ValueError("No evidence-gap IDs were found in the Markdown document.")

    # Parse the relationships recorded in the risk register.
    risk_gap_map = {}
    for _, risk in risks.iterrows():
        linked_gaps = set(split_ids(risk["evidence_gap_ids"]))
        unknown = linked_gaps - set(gap_ids)

        if unknown:
            raise ValueError(
                f"{risk['risk_id']} references unknown evidence gaps: "
                f"{sorted(unknown)}"
            )

        risk_gap_map[risk["risk_id"]] = linked_gaps

    # Create a matrix: 1 = relationship recorded, 0 = no link recorded.
    matrix_rows = []
    for _, risk in risks.iterrows():
        linked_gaps = risk_gap_map[risk["risk_id"]]
        row = {
            "risk_id": risk["risk_id"],
            "risk_title": risk["title"],
        }
        row.update({gap_id: int(gap_id in linked_gaps) for gap_id in gap_ids})
        matrix_rows.append(row)

    matrix = pd.DataFrame(matrix_rows)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    matrix.to_csv(MATRIX_CSV, index=False, encoding="utf-8-sig")

    z_values = [
        [int(gap_id in risk_gap_map[risk_id]) for gap_id in gap_ids]
        for risk_id in risks["risk_id"]
    ]

    hover_data = [
        [
            [
                risks.loc[index, "title"],
                (
                    "Relationship recorded"
                    if gap_id in risk_gap_map[risk_id]
                    else "No relationship recorded"
                ),
            ]
            for gap_id in gap_ids
        ]
        for index, risk_id in enumerate(risks["risk_id"])
    ]

    chart = go.Figure(
        data=go.Heatmap(
            z=z_values,
            x=gap_ids,
            y=risks["risk_id"].tolist(),
            customdata=hover_data,
            zmin=0,
            zmax=1,
            colorscale=[
                [0.0, "#EEF1F3"],
                [0.499, "#EEF1F3"],
                [0.5, "#0F766E"],
                [1.0, "#0F766E"],
            ],
            xgap=3,
            ygap=3,
            colorbar={
                "title": "Recorded link",
                "tickmode": "array",
                "tickvals": [0, 1],
                "ticktext": ["No", "Yes"],
            },
            hovertemplate=(
                "<b>%{y}</b><br>"
                "%{customdata[0]}<br>"
                "Evidence gap: %{x}<br>"
                "%{customdata[1]}"
                "<extra></extra>"
            ),
        )
    )

    chart.update_layout(
        title={
            "text": "Evidence-gap coverage across identified risks",
            "x": 0,
        },
        template="plotly_white",
        autosize=True,
        height=max(620, len(risks) * 44),
        margin={"l": 100, "r": 45, "t": 90, "b": 80},
        font={"family": "Arial, sans-serif", "size": 12, "color": "#263238"},
        xaxis={
            "title": "Evidence gap",
            "side": "bottom",
            "fixedrange": False,
        },
        yaxis={
            "title": "Risk",
            "autorange": "reversed",
            "fixedrange": False,
        },
    )

    chart.write_html(
        HEATMAP_HTML,
        include_plotlyjs="cdn",
        full_html=True,
        config={"responsive": True, "displaylogo": False},
    )

    total_links = sum(len(gaps) for gaps in risk_gap_map.values())

    print(f"Risks processed: {len(risks)}")
    print(f"Evidence gaps found: {len(gap_ids)}")
    print(f"Recorded risk-gap links: {total_links}")
    print(f"CSV matrix written to: {MATRIX_CSV.relative_to(ROOT)}")
    print(f"Interactive heatmap written to: {HEATMAP_HTML.relative_to(ROOT)}")
    print("Note: unmarked cells mean no relationship is recorded, not that no risk exists.")


if __name__ == "__main__":
    main()