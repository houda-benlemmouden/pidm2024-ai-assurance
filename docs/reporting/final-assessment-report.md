# PIDM2024 Public Safety Module
## Independent AI Governance and Assurance Assessment

**Assessment type:** Independent, desk-based documentary assessment  
**System in scope:** PIDM2024 Module #32, Public Safety  
**Primary source:** *Pliego de Prescripciones Técnicas Particulares – Servicios*, EXPTE. SERV. – 125/25  
**Source date:** 19 November 2025  
**Status:** Initial assessment based on the reviewed procurement specification

## 1. Executive Summary

This assessment examines the AI-enabled capabilities, operational relationships, data handling requirements and governance considerations documented for PIDM2024 Module #32 (Public Safety) in the technical procurement specification issued by the Ayuntamiento de Málaga.

The specification describes a module intended to support the real-time management of urban incidents and emergencies affecting tourism. Its documented capabilities include automatic incident detection, multi-source event correlation, predictive analytics, embedded camera analytics, drone-based analytics, incident-management functions and automated multi-area protocols with multichannel alerts.

The documentary review identifies assurance questions concerning AI performance, human oversight, automated operational actions, data quality, cross-module data use, surveillance data handling, cybersecurity, service resilience, monitoring, incident management and external data dependencies.

The assessment records eleven plausible risk scenarios and six proposed recommendations. It also defines eleven proposed assurance tests designed to identify the evidence needed to evaluate the relevant requirements and controls.

**The available procurement documentation does not establish whether the specified system has been implemented or whether its controls operate effectively.** The assessment therefore does not claim that a control has failed, that harm has occurred, or that the deployed system is unsafe or compliant.

Likelihood and numeric inherent risk scores remain unassessed because the reviewed material does not provide a sufficient basis for reliable likelihood estimates. Residual risk also remains unassessed because implementation and control-effectiveness evidence has not been established. Assessment priorities are used separately to identify areas requiring further evidence collection.

The principal outcome is an evidence-based assurance agenda: establish the implemented configuration and operating model, obtain function-specific performance and control evidence, verify data flows and governance arrangements, and perform appropriately authorised assurance activities before reaching conclusions about operational effectiveness.

## 2. Purpose and Scope

### 2.1 Purpose

The purpose of this assessment is to translate the requirements and relationships documented in the procurement specification into a traceable analysis of potential AI governance and operational risks, associated evidence needs, proposed assurance activities and practical recommendations.

The assessment aims to distinguish source-backed statements from analytical inferences, unknowns and matters requiring verification.

### 2.2 Scope

The assessment covers:

- The documented purpose and intended capabilities of Public Safety Module #32.
- Automatic incident detection, event correlation, predictive analytics, camera analytics and drone analytics.
- Specified information sources, integrations, outputs, protocols, alerts and operational dependencies.
- Human oversight, authorisation, escalation, accountability and change-control questions.
- Data protection, privacy, access, retention, cybersecurity, data quality, model performance and operational resilience where relevant to the documented system.
- Evidence gaps, proposed assurance tests and prioritised recommendations.

Related PIDM2024 components are considered only where a documented relationship or dependency affects the assessment of Public Safety.

### 2.3 Out of scope

The assessment does not establish:

- The actual deployed or as-built system architecture.
- The implementation or operation of every specified capability or integration.
- Actual model accuracy, error rates, prediction quality or operational performance.
- The implementation or effectiveness of organisational and technical controls.
- Definitive legal or regulatory compliance conclusions based solely on procurement documentation.

No live-system testing, penetration testing, operational validation or stakeholder interviews are claimed in this report.

## 3. Method and Evidence Basis

### 3.1 Primary source

The primary source is the technical procurement specification for PIDM2024, EXPTE. SERV. – 125/25, dated 19 November 2025.

The reviewed passages include the Public Safety module specification in §7.5, printed pages 82–86; relevant technical requirements in the infrastructure annex, printed pages 248–253; and applicable cross-cutting requirements concerning logging, backups, testing and model lifecycle management.

The source is recorded in `registers/source-register.csv`. The source-requirements register records individual requirements and characteristics with their relevant section and printed-page references.

Official verification copy:

https://valida.malaga.eu/verifirma/code/PJV6a8q4jb1UziaPQhuhhw%3D%3D

### 3.2 Evidence classification

The assessment distinguishes:

- **Documented fact:** A statement supported by an identified source passage.
- **Analytical inference:** A reasoned interpretation of documented facts.
- **Unknown:** A matter that cannot be established from the reviewed evidence.
- **Verification required:** A matter requiring additional documentation, stakeholder confirmation, inspection or testing.

A requirement is not proof of implementation. The absence of implementation evidence in the reviewed material is not proof that the corresponding control or capability is absent in practice.

### 3.3 Traceability

The principal working records are:

- `registers/source-register.csv`
- `docs/source-baseline/source-requirements-register.md`
- `docs/source-baseline/evidence-gaps.md`
- `docs/system-understanding/ai-function-inventory.md`
- `docs/system-understanding/operational-context.md`
- `docs/system-understanding/system-context.md`
- `docs/risk-assessment/risk-rating-method.md`
- `registers/risk-register.csv`
- `registers/assurance-test-register.csv`
- `registers/recommendations-register.csv`

The risk and assurance-test registers connect the proposed assessment activities to source requirements and evidence gaps. The recommendations register links proposed actions to the relevant risks.

## 4. System Understanding

### 4.1 Intended purpose and operational context

The specification describes Public Safety Module #32 as intended to manage urban incidents and emergencies affecting tourism in real time. Stated objectives include reducing response times, improving coordination between municipal services, and supporting proactive action through analytics, visualisation and automation.

The documented context includes information from CCTV and video-surveillance systems, IoT and environmental sensors, municipal systems such as GESPOL, social-media sources, historical incident records, meteorological information, GIS layers and incident reports submitted through tourist-facing channels. The specification also describes drone video and telemetry capabilities.

These sources are documented at different points in the specification. Their inclusion does not establish that every source feeds every function or that every described integration operates in practice.

### 4.2 AI-enabled functions

The reviewed passages describe five distinct function groups:

1. **Automatic incident detection:** Detection using AI video analytics, IoT sensors and events from existing municipal systems.
2. **Multi-source event correlation:** Correlation of information from sources including sensors, cameras, social networks and GESPOL, with the stated aim of grouping related incidents and avoiding duplicates.
3. **Predictive analytics:** Analysis involving historical incidents, seasonality, environmental information, GIS and video-surveillance information.
4. **Embedded camera analytics:** Specified camera capabilities include object classification and tracking, people and vehicle detection, intrusion and abandoned-object detection, occupancy-related analytics and tamper detection.
5. **Drone-based analytics:** Specified capabilities include image enhancement in low visibility, full-colour night vision, object classification and counting, tracking, and fire-area assessment.

The specification does not establish that every feature is enabled or used operationally, that the five functions form a single AI model or pipeline, or that their outputs have been validated for their intended uses.

### 4.3 Operational relationships and dependencies

The specification describes relationships with GESPOL, IDIS video-management infrastructure, the tourist portal and application, perception-analysis functionality, the CRM/fidelity module and the route planner.

It also describes automated activation of multi-area protocols for priority incidents and multichannel alerts.

These relationships create important assurance questions about data lineage, decision authority, error handling, escalation, access boundaries and the consequences of incorrect or delayed information. They do not, by themselves, establish the precise end-to-end workflow or confirm that AI outputs directly trigger every protocol or alert.

The broader PIDM24 architecture in §6.3, printed page 41, provides platform-level context but does not establish which platform components are connected to Public Safety Module #32.

## 5. Initial Risk Assessment

### 5.1 Overview

The risk register contains eleven scenarios covering AI performance, operational oversight, data governance, cybersecurity, resilience, accountability and external data dependencies.

| Risk ID | Risk area | Assessment priority |
|---|---|---|
| RSK-001 | Incident detection errors | High |
| RSK-002 | Authorisation and override of automated protocols | High |
| RSK-003 | Predictive analytics reliability | High |
| RSK-004 | Multi-source event correlation errors | High |
| RSK-005 | CRM personalisation and reuse of public-safety information | High |
| RSK-006 | Video and drone data lifecycle controls | High |
| RSK-007 | Connected-system security and integration | High |
| RSK-008 | Backup, recording and recovery | High |
| RSK-009 | Ongoing AI performance monitoring and degradation | High |
| RSK-010 | AI-related incident management and change control | Moderate |
| RSK-011 | External data-source quality and provenance, if integrated | Moderate |

These priorities concern the urgency of further assessment and evidence collection. They are not claims that the events are likely, that controls have failed, or that the system has caused harm.

### 5.2 Main risk themes

**AI performance and operational safety.** Errors in incident detection or event correlation, unreliable predictive outputs, or undetected performance degradation could affect the information available to public-safety operators. The specification describes these capabilities but does not establish function-specific performance results, operational error rates or effective ongoing monitoring.

**Human oversight and automated actions.** Automated protocols and multichannel alerts create a need to understand trigger conditions, decision authority, human review, override, escalation and fallback arrangements. The reviewed material does not fully establish the deployed authorisation workflow.

**Privacy and data governance.** The documented relationship between safety-related interactions, CRM profiles and personalisation or campaigns raises questions about purpose, field-level transfers, access, retention and safeguards. Camera and drone capabilities also require evidence about deployment, enabled analytics, data handling and lifecycle controls. These observations do not constitute findings of unlawful processing.

**Security and resilience.** The specification requires protected interfaces, logging, security testing, backup, recording and recovery capabilities. The reviewed material does not establish the implemented configuration, successful test results or operational effectiveness of those controls.

**Accountability and external dependencies.** The effectiveness of AI-related incident handling, material-change governance and corrective-action tracking requires further evidence. Annex I lists external indicators for integration into PIDM, but the reviewed passages do not establish which of those sources connect to Public Safety Module #32. RSK-011 therefore remains conditional.

### 5.3 Rating limitations

The rating method assesses potential impact separately from likelihood. Potential-impact scores in the register are analytical judgements about plausible consequences.

Likelihood remains unassessed for all eleven risks because the reviewed documentation does not provide sufficient operational exposure, incident history, configuration or performance data to support reliable estimates. Consequently, numeric inherent risk scores and ratings remain unassigned.

Residual risk is also unassessed because the implementation and effectiveness of relevant controls have not been established.

These are limitations of the evidence available, not findings that the system lacks safeguards. Ratings should be revisited if suitable implementation, performance, operational or control evidence becomes available.

## 6. Proposed Assurance Strategy

The assurance-test register contains eleven proposed tests linked to the risks, source requirements and evidence gaps.

The tests address:

- Detection performance and acceptance criteria.
- Human review, authorisation, override and escalation.
- Predictive-model validation and uncertainty handling.
- Event-correlation logic, provenance and error handling.
- Cross-module purposes, data fields and access safeguards.
- Video and drone data capture, access, export and retention.
- Connected-system security and integration.
- Backup, recording and recovery readiness.
- Ongoing AI performance monitoring.
- AI-related incident investigation and material-change control.
- External data-source integration and quality, where a connection is established.

The detailed procedures, evidence requirements, pass criteria, exception criteria and prerequisites are maintained in `registers/assurance-test-register.csv`. The overall sequence and method are described in `docs/assurance-testing/assurance-strategy.md`.

All tests remain **Proposed**. They must not be reported as executed unless the activity is actually performed, authorised where necessary, and supported by recorded evidence.

The proposed assurance work should begin with document and configuration evidence, establish prerequisites for technical testing, and distinguish satisfactory evidence from exceptions and cases where no defensible conclusion can be reached.

Passing a portfolio validation script checks the structure and consistency of assessment artefacts. It does not validate the actual Public Safety system or demonstrate control effectiveness.

## 7. Prioritised Recommendations

Six recommendations are recorded in `registers/recommendations-register.csv`.

### REC-001: Establish validated detection and accountable human oversight

Define incident-detection categories and approved thresholds, evaluate false-positive and false-negative performance, clarify how outputs relate to operational protocols, and establish documented authorisation, review, override, escalation and fallback arrangements.

### REC-002: Validate predictive and event-correlation functions

Document the purpose and permitted use of each function, establish appropriate evaluation criteria, preserve data provenance, examine error scenarios, and implement evidence-based monitoring and revalidation arrangements.

### REC-003: Define purpose, access and retention controls

Map relevant data flows and fields, assess CRM personalisation and campaign uses, document purposes and recipients, and establish evidence for applicable access, export, retention and deletion safeguards covering incident, video and drone data.

### REC-004: Verify connected-system security and service recovery

Review interface security, access permissions, integration and security testing, audit logging, backup coverage, recovery objectives, restoration procedures and the handling of material findings.

### REC-005: Establish AI incident and material-change governance

Assign responsibilities for reporting, investigating and escalating AI-related incidents and unexpected outputs. Define change-impact assessment, approval, validation, rollback or fallback planning, post-incident review and corrective-action tracking.

### REC-006: Establish external data dependencies

Obtain authoritative interface evidence to determine whether Annex I indicators feed Public Safety. If a connection is confirmed, document source ownership, provenance, freshness, suitability, transformations, quality checks and monitoring.

The owner roles and actions in the recommendations register are proposals for planning. They do not establish the Ayuntamiento's actual governance structure or imply that a particular organisational role has accepted responsibility.

Acceptance should be based on evidence that the relevant action has been completed and its intended outcome demonstrated, not solely on the publication of a policy or procedure.

## 8. Limitations and Unresolved Questions

The assessment is based on the reviewed procurement specification and the source baseline recorded in the repository. It does not establish the deployed architecture, actual data flows, model performance, operational procedures, control effectiveness or legal compliance.

Material unresolved questions include:

- Which specified functions and features have been implemented, enabled and connected.
- What performance metrics and thresholds apply to each AI-enabled function, and what validation results exist.
- How human review, authorisation, escalation, override and fallback operate in practice.
- What data fields and processing purposes govern cross-module transfers and potential CRM reuse.
- How video, drone and incident data access, retention, deletion and export are configured.
- Whether integration, security, audit logging, backup and restoration controls operate effectively.
- What procedures govern AI-related incidents, material changes, model maintenance and corrective action.
- Whether external data sources listed in Annex I are connected to Public Safety Module #32.

The absence of evidence from the reviewed passages does not prove that a capability or safeguard is absent in practice. Additional evidence may change the assessment and its priorities.

## 9. Conclusion

The procurement specification describes an ambitious Public Safety module combining surveillance and sensing infrastructure, AI-enabled analysis, incident-management capabilities, integrations and automated operational protocols.

Those requirements provide a basis for an independent documentary risk assessment and a structured assurance plan. They do not, by themselves, establish whether the intended system has been delivered, whether its controls are effective, or whether the system performs safely in operation.

The defensible conclusion at this stage is therefore that **material assurance questions remain open and require evidence before operational effectiveness or residual risk can be determined**.

The next stage is to obtain legitimately available implementation and governance evidence, perform only appropriately authorised assurance activities, record the results, update the risk assessments where justified, and link any final recommendations to demonstrated findings or explicitly stated uncertainties.

**Assessment status:** Initial documentary assessment. Further evidence and assurance activities are required before conclusions can be made about the implementation, performance or effectiveness of the deployed system.

## 10. Portfolio Independence Statement

This report is an independent portfolio exercise based on the cited procurement documentation. It was not commissioned by, delivered to or endorsed by the Ayuntamiento de Málaga, the platform supplier or any procurement participant. It does not claim access to internal systems or confidential operational evidence.