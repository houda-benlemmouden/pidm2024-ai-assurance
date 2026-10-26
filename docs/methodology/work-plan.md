# Portfolio Work Plan

## 1. Purpose

This work plan defines the phases, deliverables, dependencies and completion criteria for an independent, desk-based AI governance and assurance assessment of the Public Safety module specified in the Málaga Intelligent Destination Platform (PIDM 2024) technical procurement document.

The project will examine the requirements documented in the source, identify governance and assurance questions arising from those requirements, and develop evidence-based risk analysis and recommendations.

The portfolio is an independent analytical exercise. It is not commissioned by, delivered to or endorsed by the Ayuntamiento de Málaga or any procurement participant.

## 2. Objectives

The assessment aims to:

1. Establish a traceable baseline of the documented system requirements.
2. Describe the system's intended capabilities, data sources, integrations, outputs and operational context.
3. Identify relevant AI governance, privacy, security, operational and accountability risks.
4. Distinguish documented requirements from inferences, unknowns and matters requiring verification.
5. Define proportionate assurance questions and proposed tests.
6. Develop prioritised recommendations and communicate the findings in a clear final report.

The assessment will not claim to verify the operation or effectiveness of a deployed system without supporting evidence.

## 3. Scope

### 3.1 In scope

- The Public Safety module described in the PIDM 2024 technical specification.
- Documented AI-enabled capabilities, including video analytics, event correlation and predictive analytics.
- Specified data sources, integrations, incident workflows, alerts, dashboards and outputs.
- Governance responsibilities, human oversight, accountability and escalation questions.
- Data protection, information security, data quality, model performance, operational resilience and third-party dependency risks, where relevant to the documented system.
- Evidence gaps and assurance activities needed to validate assumptions.
- Practical recommendations linked to identified risks or evidence gaps.

### 3.2 Out of scope

- Claims about the actual deployed system that cannot be supported by evidence.
- Live-system access, penetration testing, model testing or operational validation unless separately authorised and actually performed.
- Definitive legal-compliance conclusions based solely on the technical specification.
- Claims that a control is absent merely because it is not explicitly described in the passages reviewed.
- Evaluation of unrelated PIDM modules except where an explicitly documented interface or dependency affects Public Safety.

## 4. Work phases and deliverables

### Phase 1: Project and source preparation

**Activities**
- Establish the repository, folder structure and version-control workflow.
- Record the primary source and its provenance.
- Define the evidence classification and traceability method.

**Deliverables**
- `README.md`
- `registers/source-register.csv`
- `docs/methodology/evidence-method.md`
- `docs/methodology/work-plan.md`

**Completion criteria**
- Project boundaries and independent status are explicit.
- The primary source is identifiable and traceable.
- Evidence categories and limitations are documented.

### Phase 2: Source validation and requirements baseline

**Activities**
- Check each requirement against the relevant source passage.
- Record exact section and page references.
- Separate explicit requirements from interpretation.
- Record ambiguous wording and unresolved questions.
- Correct the requirements register where necessary.

**Deliverables**
- `docs/source-baseline/source-requirements-register.md`
- Updated source register, where needed.

**Completion criteria**
- Each material requirement has a traceable reference.
- Interpretations are not presented as direct source statements.
- Unverified claims and evidence gaps are clearly labelled.

### Phase 3: System understanding

**Activities**
- Map the intended system context, inputs, processing capabilities, integrations, outputs and stakeholders.
- Describe key information flows and operational dependencies.
- Identify points where decisions, alerts or actions may affect people.
- Record uncertainties that cannot be resolved from the source.

**Deliverables**
- System overview and context diagram.
- Data-flow and integration descriptions.
- Stakeholder and responsibility map.
- Initial assumptions and unknowns register, if required.

**Completion criteria**
- Each documented component and connection is traceable to evidence.
- Inferred relationships are labelled as inferences.
- Unknown implementation details remain explicit.

### Phase 4: AI governance and risk assessment

**Activities**
- Identify risks associated with the documented capabilities and information flows.
- Assess plausible impacts, affected stakeholders, causes and existing evidence.
- Distinguish inherent risks from documented controls and unverified control assumptions.
- Prioritise risks using a defined, consistently applied rating method.
- Identify the evidence required to validate each material risk.

**Deliverables**
- `docs/risk-assessment/` analysis.
- `registers/risk-register.csv`.
- Risk-rating methodology and rationale.

**Completion criteria**
- Each risk has a clear scenario, rationale and evidence reference.
- Ratings follow documented criteria.
- Proposed controls are not described as existing controls without evidence.
- Priorities reflect both potential impact and uncertainty where appropriate.

### Phase 5: Assurance strategy and proposed tests

**Activities**
- Translate material risks and evidence gaps into assurance questions.
- Define proposed document reviews, interviews, inspections or tests.
- Specify expected evidence, pass criteria and limitations for each proposed test.
- Distinguish tests designed on paper from tests actually executed.

**Deliverables**
- `docs/assurance-testing/` assessment approach.
- `registers/assurance-test-register.csv`.

**Completion criteria**
- Each proposed test links to one or more risks or requirements.
- Evidence requirements and pass criteria are defined.
- No test is represented as completed unless it was actually performed and documented.

### Phase 6: Recommendations and final reporting

**Activities**
- Prioritise recommendations by risk, urgency, feasibility and dependency.
- Identify the rationale and intended outcome for each recommendation.
- Summarise material findings, limitations and further verification needs.
- Review the report for accuracy, traceability and clear communication.

**Deliverables**
- Executive summary and final assessment report.
- Prioritised recommendations and proposed roadmap.
- Supporting registers and diagrams.
- Published portfolio documentation.

**Completion criteria**
- Material findings link to evidence or are clearly labelled as hypotheses.
- Recommendations address identified issues.
- Limitations and unresolved questions are visible.
- The portfolio does not imply endorsement, deployment access or testing that did not occur.

## 5. Evidence and quality controls

The following controls apply throughout the project:

- **Traceability:** Material requirements, risks and recommendations reference their supporting sources.
- **Classification:** Facts, inferences, unknowns and verification requirements are distinguished.
- **Consistency:** Risk ratings and evidence categories use documented criteria.
- **Reproducibility:** Relevant working documents and registers are version-controlled.
- **Scope discipline:** Conclusions remain within the limits of the evidence.
- **Review:** Each deliverable is checked against its completion criteria before proceeding.

## 6. Dependencies and assumptions

The project depends on access to the primary technical specification and any additional sources that can legitimately be obtained.

Where the specification does not establish implementation details, operating practices, control effectiveness or actual performance, those matters will remain unverified unless further evidence becomes available.

The assessment assumes no access to internal municipal systems, confidential supplier materials, production data or stakeholder interviews unless such access is explicitly obtained and documented.

## 7. Project tracking

Progress will be tracked through the deliverables and completion criteria defined in this plan. Changes to scope, assumptions or methodology will be recorded in the repository where material.

The work plan may be updated as the evidence develops. Changes must not be used to disguise unresolved gaps or retrospectively present proposed activities as completed work.

## 8. Definition of completion

The portfolio will be considered complete when:

- The source baseline has been checked against the cited passages.
- The intended system and key information flows are documented.
- The risk register is populated and consistently prioritised.
- Proposed assurance activities have defined evidence and pass criteria.
- Recommendations are linked to the assessment findings.
- The final report states its methodology, scope, limitations and unresolved questions.
- The published materials are internally consistent and traceable to the available evidence.