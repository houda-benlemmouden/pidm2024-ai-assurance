"""Generate an interactive risk impact profile from the risk register."""

from pathlib import Path

import pandas as pd
import plotly.graph_objects as go


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "registers" / "risk-register.csv"
OUTPUT_DIR = ROOT / "docs" / "generated"
OUTPUT = OUTPUT_DIR / "risk-impact-profile.html"


def main() -> None:
    required_columns = {
        "risk_id",
        "title",
        "inherent_impact_score",
        "assessment_priority",
        "evidence_confidence",
    }

    risks = pd.read_csv(
        INPUT,
        dtype=str,
        keep_default_na=False,
        encoding="utf-8-sig",
    )

    missing = required_columns - set(risks.columns)
    if missing:
        raise ValueError(f"Risk register missing columns: {sorted(missing)}")

    if risks["risk_id"].duplicated().any():
        raise ValueError("Duplicate risk IDs found in the risk register.")

    risks["impact_score"] = pd.to_numeric(
        risks["inherent_impact_score"], errors="coerce"
    )

    if risks["impact_score"].isna().any():
        invalid = risks.loc[
            risks["impact_score"].isna(), "risk_id"
        ].tolist()
        raise ValueError(f"Missing or invalid impact scores: {invalid}")

    if not risks["impact_score"].isin([1, 2, 3, 4, 5]).all():
        raise ValueError("Impact scores must be between 1 and 5.")

    risks["impact_rating"] = risks["impact_score"].map({
        1: "Negligible",
        2: "Minor",
        3: "Moderate",
        4: "Major",
        5: "Severe",
    })

    # Plot high-impact risks first, retaining IDs for traceability.
    risks = risks.sort_values(
        ["impact_score", "risk_id"],
        ascending=[True, False],
    )

    colours = {
        1: "#CBD5E1",
        2: "#94A3B8",
        3: "#64748B",
        4: "#B45309",
        5: "#991B1B",
    }

    bar_colours = [colours[int(score)] for score in risks["impact_score"]]

    hover = [
        (
            f"<b>{row.risk_id}</b><br>"
            f"{row.title}<br>"
            f"Inherent impact: {int(row.impact_score)} "
            f"({row.impact_rating})<br>"
            f"Assessment priority: {row.assessment_priority}<br>"
            f"Evidence confidence: {row.evidence_confidence}<br>"
            "Likelihood: Not assessed<br>"
            "Residual risk: Not assessed"
        )
        for row in risks.itertuples()
    ]

    fig = go.Figure(
        go.Bar(
            x=risks["impact_score"],
            y=risks["risk_id"],
            orientation="h",
            marker_color=bar_colours,
            customdata=hover,
            hovertemplate="%{customdata}<extra></extra>",
            text=[
                f"{int(score)} · {rating}"
                for score, rating in zip(
                    risks["impact_score"], risks["impact_rating"]
                )
            ],
            textposition="outside",
            cliponaxis=False,
        )
    )

    fig.update_layout(
        title={
            "text": "Inherent impact profile of identified risks",
            "x": 0,
        },
        template="plotly_white",
        height=650,
        autosize=True,
        margin={"l": 90, "r": 100, "t": 90, "b": 80},
        font={"family": "Arial, sans-serif", "size": 12, "color": "#263238"},
        xaxis={
            "title": "Inherent impact score",
            "range": [0, 5.8],
            "tickmode": "linear",
            "dtick": 1,
        },
        yaxis={"title": "Risk ID"},
        annotations=[
            {
                "text": (
                    "Impact only. Likelihood and residual risk are not assessed. "
                    "Assessment priority is a separate field."
                ),
                "xref": "paper",
                "yref": "paper",
                "x": 0,
                "y": -0.19,
                "showarrow": False,
                "align": "left",
                "font": {"size": 11, "color": "#52616B"},
            }
        ],
    )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    fig.write_html(
        OUTPUT,
        include_plotlyjs="cdn",
        full_html=True,
        config={"responsive": True, "displaylogo": False},
    )

    print(f"Risks visualised: {len(risks)}")
    print(f"Impact score counts: {risks['impact_score'].value_counts().sort_index().to_dict()}")
    print(f"Interactive profile written to: {OUTPUT.relative_to(ROOT)}")
    print("Likelihood and residual risk were not inferred or imputed.")


if __name__ == "__main__":
    main()