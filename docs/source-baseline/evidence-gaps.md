# Evidence Gaps and Verification Questions

## 1. Purpose

This document consolidates questions that remain unresolved after reviewing the technical specification for PIDM2024 Module #32 (Public Safety).

The purpose is to distinguish requirements stated in the specification from evidence needed to determine how those requirements have been implemented and whether the relevant controls operate effectively.

This is an independent, desk-based assessment of public documentation. No access to the live system, implementation records, test results or operational procedures is assumed.

## 2. Evidence Status

The following classifications apply:

- **Specified:** The technical specification states a requirement or capability.
- **Unverified:** The specification does not establish whether the requirement has been implemented or operates effectively.
- **Evidence required:** The records, documentation or test results needed to resolve the question.

An unverified item is not, by itself, evidence of non-compliance or system failure.

## 3. AI Governance and Assurance

### EG-001: Human oversight

**Source references:** §7.5.2–7.5.3, pp. 82–84; Annex II, pp. 247–253.

**Specified:** The module includes a control-room interface, incident alerts, automatic incident detection, event correlation and predictive analytics.

**Unresolved questions:**
- Which AI-generated detections, alerts or predictions require human review?
- Who is authorised to confirm, reject, override or escalate an AI-generated output?
- What procedures apply when an output is incorrect, ambiguous or unavailable?
- Are operator responsibilities and escalation routes documented?

**Evidence required:** Operating procedures, role and responsibility matrices, escalation procedures, operator guidance and relevant system workflow documentation.

### EG-002: Model validation and acceptance criteria

**Source references:** §5.3, pp. 14–15; §5.9.2, p. 30; §7.5.3, pp. 83–84.

**Specified:** The specification requires testing and, for predictive or AI/ML models, identification of evaluation metrics and acceptable thresholds, subject to RMC approval.

**Unresolved questions:**
- Which evaluation metrics and thresholds have been defined for each AI-enabled function?
- How are detection errors and incorrect predictions evaluated?
- What datasets, test scenarios and acceptance criteria are used?
- How are the suitability and limitations of the evaluation methods documented?

**Evidence required:** Model evaluation plans, test datasets and their documentation, metric definitions, approved thresholds, test results and acceptance records.

### EG-003: Ongoing performance monitoring

**Source references:** §5.9.2, p. 30; §7.5.5, pp. 84–85.

**Specified:** The specification includes model maintenance and retraining considerations, alongside operational KPIs for incidents, response times, alerts and seasonal risk trends.

**Unresolved questions:**
- How is the ongoing performance of each AI-enabled function monitored?
- Are false positives, false negatives or other error indicators tracked?
- How are changes in data patterns or model performance identified?
- What conditions trigger investigation, corrective action or retraining?

**Evidence required:** Monitoring plans, operational dashboards, model-performance reports, alert thresholds, retraining procedures and change records.

### EG-004: AI-related incident management

**Source references:** §7.5.3, pp. 83–84; §7.5.5–7.5.7, pp. 84–85; general logging provisions, p. 26.

**Specified:** The module includes incident detection, alerts, operational dashboards and event histories. General provisions require logging and monitoring of user activity, exceptions and security events.

**Unresolved questions:**
- How are AI-related failures, incorrect detections or unavailable services reported?
- How are AI-related operational incidents investigated and documented?
- How are incidents linked to the relevant output, model version, input data and system configuration?
- What procedures govern corrective action and the return to normal operation?

**Evidence required:** Incident-management procedures, incident records, investigation templates, logging specifications, escalation rules and corrective-action records.

### EG-005: Accountability and change control

**Source references:** §5.3, pp. 14–15; §5.9.1–5.9.2, pp. 29–30; §7.5, pp. 82–86.

**Specified:** The specification provides for testing, technical audits, RMC approval of model evaluation metrics and thresholds, and model maintenance and retraining.

**Unresolved questions:**
- Who is accountable for each AI-enabled function throughout its lifecycle?
- Who approves model, configuration, data-source or threshold changes?
- How are changes assessed, tested, documented and authorised before release?
- Who accepts residual risks and authorises operational use?

**Evidence required:** Governance and responsibility matrices, approval records, change-management procedures, release records, audit findings and risk-acceptance documentation.

## 4. Privacy and Data Governance

### EG-006: Data use, access and retention

**Source references:** §7.5.4, p. 84; §7.5.6–7.5.7, p. 85; general security provisions, pp. 24–26 and 40; Annex II, pp. 249–251.

**Specified:** The module uses or may receive information from CCTV, sensors, social networks, citizen reporting channels and municipal systems. The specification describes feeding safety-related incidents and interactions into a unified CRM profile for personalisation and campaigns. It also includes access-control, logging, backup and video-storage requirements.

**Unresolved questions:**
- Which data fields are collected, generated, combined or shared by each function?
- What purposes and access permissions apply to each data category?
- What retention and deletion rules apply to incident records, video, logs, backups and CRM information?
- What safeguards govern the use of safety-related information for personalisation or campaigns?
- What documented assessment establishes the applicable data-protection requirements and lawful basis for each processing activity?

**Evidence required:** Data-flow diagrams, data inventories, access-control matrices, retention schedules, deletion procedures, data-protection assessments where applicable, and documentation of purposes and lawful bases.

## 5. Implementation and Operational Evidence

### EG-007: Verification of implementation and commissioning

**Source references:** §5.3, pp. 14–15; §5.9.1, pp. 29–30; Annex II, pp. 247–254.

**Specified:** The specification includes infrastructure, integration, testing, technical audit, training, installation and commissioning requirements.

**Unresolved questions:**
- Which specified components and AI-enabled functions were actually delivered and configured?
- Were the required functional, integration, performance, security and interoperability tests executed?
- Were critical or high-severity audit findings resolved before the relevant acceptance milestones?
- Were the required training, installation, connectivity and compatibility records completed?

**Evidence required:** As-built architecture, configuration records, test plans and results, audit reports, issue and remediation logs, training records, commissioning certificates and acceptance documentation.

### EG-008: External data sources and indicator integration

**Source references:** Annex I, pp. 241–246; §7.5.6–7.5.7, p. 85; §7.5.3, pp. 83–84.

**Specified:** Annex I lists multiple data sources and indicator frameworks for PIDM, including INE, Proyecto D3HUB, the SEGITTUR Tourism Intelligence System, SmartData–Turismo Andaluz and INSTO. The listed indicators include tourist-related crime, mobile-position tourism analysis, visitor activity, employment, economic performance and environmental indicators. The Public Safety module separately identifies sources such as CCTV, sensors, citizen reporting channels and municipal systems.

**Unresolved questions:**
- Which Annex I sources and indicators are connected to Module #32?
- Are the listed indicators used directly in public-safety operations, used only for destination-level reporting, or not connected to this module?
- What are the provenance, update frequency, aggregation level, quality controls and ownership of each relevant dataset?
- Does any integration involve personal or location data, and what access, purpose and retention restrictions apply?
- How are indicator definitions, calculation methods and changes documented?

**Evidence required:** Module-specific data-flow diagrams, interface and API specifications, data dictionaries, indicator definitions, data-sharing arrangements, integration test results and applicable data-protection documentation.

**Status:** Open. The annex identifies sources and indicators but does not establish their actual connection to the Public Safety module.


## 6. Interpretation and Limitations

The technical specification describes intended capabilities and contractual requirements. It does not, on its own, establish that those capabilities were delivered, that controls were implemented, or that the system operates effectively.

The questions in this register identify evidence needed for further assessment. They must not be presented as confirmed control failures, legal violations or proof of non-compliance.

A lack of evidence in the documents reviewed means that a conclusion cannot yet be reached; it does not establish that the relevant evidence or control does not exist.

## 7. Review Status

**Status:** Open. Evidence collection and verification remain outstanding.

The source baseline should not be considered frozen until the relevant source sections and cross-references have been reviewed, the requirements register has been checked for completeness, and the outstanding evidence questions have been documented.
