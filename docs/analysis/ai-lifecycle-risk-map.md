# AI Lifecycle Risk Map

## Purpose

This analysis considers how the identified risks relate to relevant stages of the AI-enabled system lifecycle, from data sourcing and system integration through validation, operational use, monitoring, and change management.

It is intended to support a lifecycle-oriented review of governance and assurance needs, rather than to assert that every stage or control has been implemented.

## Lifecycle view

| Lifecycle stage | Assessment focus | Related risks | Basis and qualification |
|---|---|---|---|
| Data sourcing, collection and provenance | Input suitability, provenance, freshness and data collection | RSK-003, RSK-004, RSK-006, RSK-011 | SRC-007, SRC-012, SRC-014, SRC-015, SRC-017, SRC-025. RSK-011 is conditional because the connection of Annex I sources to Module #32 is unverified. |
| Data use, purpose and access governance | Permitted purposes, access boundaries, retention and data reuse | RSK-005, RSK-006 | SRC-010, SRC-012, SRC-014, SRC-015, SRC-016, SRC-017, SRC-022; EG-006 and EG-007. RSK-005 primarily concerns CRM reuse safeguards, not input-data quality. |
| System integration, security and availability | Interfaces, access controls, system integrity, security monitoring and availability | RSK-004, RSK-007, RSK-011 | SRC-004, SRC-013, SRC-021, SRC-023, SRC-025. RSK-004 has an integration-related aspect; RSK-011 remains conditional on the external-data connection being established. |
| Model and function validation | Detection performance, prediction validity, correlation accuracy and acceptance criteria | RSK-001, RSK-003, RSK-004 | SRC-006, SRC-007, SRC-009, SRC-023, SRC-024. Validation results and function-specific thresholds remain unverified. |
| Operational use and human oversight | Authorisation, review, escalation, override and safe use of outputs | RSK-001, RSK-002 | SRC-008, SRC-009, SRC-011, SRC-023; EG-001, EG-003, EG-004 and EG-005. Operational oversight arrangements have not been demonstrated by the reviewed evidence. |
| Monitoring, maintenance and revalidation | Detection of performance degradation, monitoring, maintenance and retraining | RSK-003, RSK-009, RSK-010 | SRC-007, SRC-011, SRC-021, SRC-023, SRC-024; EG-002, EG-003 and EG-005. RSK-010 relates here specifically to material changes and maintenance governance. |
| Recording, retention, resilience and recovery | Recording availability, preservation of evidence, backup and restoration | RSK-006, RSK-008 | SRC-015, SRC-019, SRC-020, SRC-021, SRC-022; EG-007. Requirements are documented, but implementation and successful recovery are unverified. |
| Incident and change governance | Reporting, triage, investigation, accountability, approval and follow-up | RSK-002, RSK-007, RSK-010 | SRC-008, SRC-021, SRC-023, SRC-024; EG-004, EG-005 and EG-007. RSK-010 is the primary association; RSK-002 relates to escalation, and RSK-007 to security-event logging and investigation. |

The associations above are an initial analytical grouping based on the existing risk titles and scenarios. They should be checked against the full risk rationales, source requirements, and proposed assurance tests before being treated as a final control mapping.

## How to interpret this view

A risk may span several lifecycle stages. The table does not assign a risk to only one stage, nor does it establish that a lifecycle control is present or effective.

Some associations are conditional. For example, RSK-011 concerns external data-source quality or provenance if those sources are used by Public Safety; the connection remains unverified in the current documentary assessment.

## Next analytical step

The next stage is to validate each lifecycle association against the source requirements and risk rationales, then link relevant stages to expected controls, evidence gaps, and proposed assurance tests.

## Limitations

This is a proposed analytical view derived from the assessment registers. It is not evidence that the system follows a particular development lifecycle, that all lifecycle stages are in scope, or that the described controls have been implemented or tested.