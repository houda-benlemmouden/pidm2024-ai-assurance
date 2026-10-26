# Public Safety Risk Assessment Overview

## 1. Purpose and Status

This document summarises the initial risk assessment of PIDM2024 Module #32 (Public Safety), based on the reviewed technical procurement specification and the existing source-requirements and evidence-gaps registers.

The assessment is independent and desk-based. It identifies plausible risk scenarios arising from the capabilities, integrations and operational relationships described in the source. It does not establish that the system has been deployed, that any adverse event has occurred, or that a control has failed.

The detailed risk records are maintained in `registers/risk-register.csv`. The rating approach is defined in `docs/risk-assessment/risk-rating-method.md`.

## 2. Assessment Approach

Each risk record describes a plausible scenario, its cause or condition, potential consequences, affected stakeholders, supporting source requirements and relevant evidence gaps.

Potential impact is assessed separately from likelihood. Numeric inherent risk scores are not calculated when likelihood cannot be assessed reliably from the available evidence.

Assessment priority is recorded separately from the numeric risk rating. It indicates the urgency of further evidence collection or investigation and does not mean that an event is likely or that harm has occurred.

Controls described in the procurement specification are treated as requirements or documented capabilities, not as proof of implementation or effectiveness. Residual risk remains unassessed where available evidence does not support a defensible conclusion about control implementation and effectiveness.

## 3. Risk Coverage

The current register contains eleven risk scenarios across the following areas:

| Risk IDs | Area covered |
|---|---|
| RSK-001 | Errors in automatic incident detection |
| RSK-002 | Authorisation, human review and override of automated protocols |
| RSK-003 | Predictive analytics that may misdirect planning or response |
| RSK-004 | Incorrect multi-source event correlation |
| RSK-005 | Cross-module reuse of safety-related information for CRM personalisation |
| RSK-006 | Video and drone data capture, access, export and retention |
| RSK-007 | Security and integration weaknesses |
| RSK-008 | Backup, recording and recovery failures |
| RSK-009 | AI performance degradation and ongoing monitoring |
| RSK-010 | AI-related incident investigation and change control |
| RSK-011 | External data-source quality and provenance, where integration is established |

The scenarios are related but address different failure mechanisms. In particular, detection errors, incorrect event correlation and performance degradation are not treated as the same risk. Human oversight and authorisation are also distinguished from incident investigation and change accountability.

RSK-011 is explicitly conditional. Annex I lists external indicators for PIDM integration, but the reviewed source does not establish that those sources connect to Public Safety Module #32.

## 4. Initial Rating Profile

The current register assigns potential-impact scores of 3 or 4 to the eleven scenarios. These are analytical judgements about plausible consequences, not observed outcomes or measurements of actual system performance.

The register assigns High assessment priority to RSK-001 through RSK-009, and Moderate assessment priority to RSK-010 and RSK-011. These priorities reflect the current judgement about the need for further evidence collection. They are not numeric risk ratings.

Likelihood remains unassessed for all eleven risks because the reviewed documentation does not establish sufficient operational exposure, incident history, configuration or performance data to support reliable estimates.

Consequently, the numeric inherent risk score and rating remain unassigned. Residual risk is also unassessed because the available evidence does not establish the implementation and effectiveness of relevant controls.

These limitations must remain visible until further evidence supports a more complete assessment.

## 5. Main Evidence Needs

The most important evidence needs identified across the register are:

- **AI performance:** defined intended uses, approved performance metrics and thresholds, representative validation results, and monitoring evidence.
- **Operational oversight:** documented trigger conditions, authorisation roles, human review, override, escalation and fallback procedures.
- **Data governance:** field-level mappings, data lineage, purpose and access boundaries, retention rules, and evidence of safeguards for cross-module reuse.
- **Security and resilience:** deployed interface and access configurations, security and integration test results, audit logging evidence, backup coverage and restoration results.
- **Accountability and change:** incident procedures, assigned responsibilities, change-impact assessments, approval records, rollback arrangements and corrective-action tracking.
- **External dependencies:** authoritative interface evidence establishing whether Annex I indicators feed Module #32, followed by provenance and data-quality evidence if a connection is confirmed.

The absence of these materials from the reviewed documentary baseline does not establish that they are absent from the actual system.

## 6. Relationship to Assurance Testing

The proposed activities addressing these risks are recorded in `registers/assurance-test-register.csv`, with the overall approach described in `docs/assurance-testing/assurance-strategy.md`.

Each proposed test is linked to relevant risk, source-requirement and evidence-gap identifiers. The register defines intended procedures, required evidence, pass criteria and exception criteria.

All tests remain proposed until they are actually performed and their dates, evidence and results are recorded. Passing a portfolio validation script checks the structure and consistency of the assessment artefacts; it does not validate the real system or demonstrate control effectiveness.

## 7. Limitations and Next Steps

This is an initial risk assessment based on procurement documentation. It does not establish actual event likelihood, deployed system behaviour, operational performance, control effectiveness or legal compliance.

The next steps are to obtain and assess additional evidence where legitimately available, execute only authorised assurance activities, update ratings when the evidence supports doing so, and develop recommendations traceable to the findings.

**Status:** Initial documentary risk assessment. Material uncertainty remains, and the conclusions must be updated if additional evidence becomes available.