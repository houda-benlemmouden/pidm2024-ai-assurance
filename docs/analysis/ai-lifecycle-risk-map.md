# AI Lifecycle Risk Map

## Purpose

This analysis considers how the identified risks relate to relevant stages of the AI-enabled system lifecycle, from data sourcing and system integration through validation, operational use, monitoring, and change management.

It is intended to support a lifecycle-oriented review of governance and assurance needs, rather than to assert that every stage or control has been implemented.

## Lifecycle view

| Lifecycle stage | Assessment focus | Related risks |
|---|---|---|
| Data sourcing and quality | Data provenance, suitability, freshness, and quality controls | RSK-003, RSK-004, RSK-005, RSK-006, RSK-011 |
| System integration and security | Interfaces, access controls, system integrity, and availability | RSK-005, RSK-007, RSK-010, RSK-011 |
| Model and function validation | Performance thresholds, representative evaluation, and error analysis | RSK-001, RSK-003, RSK-004 |
| Operational use and human oversight | Detection errors, automated protocols, authorisation, override, and fallback | RSK-001, RSK-002 |
| Monitoring and maintenance | Performance degradation, logging, monitoring, and revalidation triggers | RSK-003, RSK-009, RSK-010 |
| Recording, recovery, and continuity | Recording availability, backup, restoration, and preservation of evidence | RSK-006, RSK-008 |
| Incident and change governance | Investigation, accountability, change control, and escalation | RSK-007, RSK-009, RSK-010 |

The associations above are an initial analytical grouping based on the existing risk titles and scenarios. They should be checked against the full risk rationales, source requirements, and proposed assurance tests before being treated as a final control mapping.

## How to interpret this view

A risk may span several lifecycle stages. The table does not assign a risk to only one stage, nor does it establish that a lifecycle control is present or effective.

Some associations are conditional. For example, RSK-011 concerns external data-source quality or provenance if those sources are used by Public Safety; the connection remains unverified in the current documentary assessment.

## Next analytical step

The next stage is to validate each lifecycle association against the source requirements and risk rationales, then link relevant stages to expected controls, evidence gaps, and proposed assurance tests.

## Limitations

This is a proposed analytical view derived from the assessment registers. It is not evidence that the system follows a particular development lifecycle, that all lifecycle stages are in scope, or that the described controls have been implemented or tested.