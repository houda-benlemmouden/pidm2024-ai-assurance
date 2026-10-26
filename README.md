# PIDM2024 Public Safety: AI Governance and Assurance Assessment

An independent, document-based assessment of AI-enabled capabilities described in the technical specification for **PIDM2024 Module #32 – Public Safety**.

The portfolio demonstrates a structured approach to requirements traceability, system understanding, AI risk assessment, assurance planning, and evidence-based recommendations in a public-sector technology context.

## Assessment scope

The assessment examines AI-related capabilities described in the procurement specification, including incident detection, predictive analytics, incident correlation, automated protocols, video analytics, drone-related capabilities, and integration with other systems.

The work follows a traceable assessment process:

1. Establish a source baseline and identify documented requirements.
2. Describe the proposed system context and AI-related functions.
3. Identify evidence gaps and assess potential risks.
4. Define proposed assurance tests and recommendations.
5. Document conclusions, limitations, and outstanding evidence needs.

## Start here

**[Read the final assessment report](docs/reporting/final-assessment-report.md)** for the overall conclusions, principal risks, assurance priorities, recommendations, and limitations.

Supporting documents:

- [Source baseline and requirements](docs/source-baseline/index.md)
- [Source requirements register](docs/source-baseline/source-requirements-register.md)
- [Evidence gaps](docs/source-baseline/evidence-gaps.md)
- [AI function inventory](docs/system-understanding/ai-function-inventory.md)
- [Operational context](docs/system-understanding/operational-context.md)
- [System context](docs/system-understanding/system-context.md)
- [Risk assessment overview](docs/risk-assessment/risk-assessment-overview.md)
- [Risk-rating method](docs/risk-assessment/risk-rating-method.md)
- [Assurance strategy](docs/assurance-testing/assurance-strategy.md)
- [Evidence method](docs/methodology/evidence-method.md)
- [Work plan](docs/methodology/work-plan.md)

## Registers and validation

The repository includes structured registers to support traceability and review:

| Register | Purpose |
|---|---|
| [Source register](registers/source-register.csv) | Records the assessment's source references |
| [Risk register](registers/risk-register.csv) | Records identified risks and their supporting evidence |
| [Assurance test register](registers/assurance-test-register.csv) | Defines proposed tests linked to risks |
| [Recommendations register](registers/recommendations-register.csv) | Records proposed actions linked to identified risks |

Python validation scripts check the structure and defined integrity rules of the risk, assurance-test, and recommendations registers. Passing these checks does not establish that the underlying system is safe, compliant, implemented, or operational.

## Evidence and limitations

This is an independent desk-based assessment of documentary evidence. It is not an audit of a deployed system, a certification, a conformity assessment, or a statement that the described capabilities have been implemented or tested.

The technical specification establishes requirements and describes intended capabilities. It does not, on its own, demonstrate implementation, operational performance, control effectiveness, or legal compliance. Where evidence is unavailable, the assessment identifies the limitation rather than treating an assumption as a verified fact.

Risk ratings and assurance activities should therefore be interpreted in light of the documented evidence gaps. Assurance tests and recommendations are proposals, not completed tests or confirmed remediation.

## Source

The primary source is the technical specification for PIDM2024 Module #32 – Public Safety, signed 19 November 2025, with 255 pages. Page references in the assessment refer to the printed folio numbers where stated.

[Official document verification](https://valida.malaga.eu/verifirma/code/PJV6a8q4jb1UziaPQhuhhw%3D%3D)

## Independence

This portfolio was prepared independently for professional demonstration and learning purposes. It is not commissioned by, affiliated with, or endorsed by Ayuntamiento de Málaga, the procurement authority, or any supplier. The analysis should not be interpreted as a finding of misconduct or as a conclusion about the performance of any deployed system.
