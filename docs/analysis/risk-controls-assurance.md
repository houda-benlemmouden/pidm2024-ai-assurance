# Risk, Controls & Assurance

## Purpose

This analysis will connect each identified risk to the controls intended to prevent, detect, or mitigate it, the evidence available to assess those controls, and the assurance activities proposed to verify their operation.

The objective is to distinguish documented requirements from demonstrated implementation and verified effectiveness.

## Current position

The assessment already includes:

- A risk register with 11 identified risks and documented evidence limitations.
- An assurance-test register with 11 proposed tests linked to risks.
- A recommendations register with six proposed recommendations.
- Evidence-gap records describing information that has not been established by the reviewed documentation.

These artefacts provide the basis for the analysis. They do not establish that the relevant controls have been implemented or tested.

## Control-assurance mapping

The next stage of this analysis will structure the following relationships:

The following mapping is generated from the risk, assurance-test, and recommendations registers. It distinguishes documented control requirements from unverified implementation and proposed assurance activities.

<!-- CONTROL-MAPPING-START -->

### RSK-001 — Incident detection errors may delay or misdirect response

**Assessment priority:** High<br>
**Evidence confidence:** Moderate

**Risk scenario:** If automatic incident detection misses a real incident or generates an incorrect detection, incident information may be delayed, misclassified or acted on inappropriately, potentially affecting response.

**Source requirements:** SRC-008, SRC-009, SRC-023, SRC-024<br>
**Evidence gaps:** EG-001, EG-002, EG-003, EG-007

**Control position:** Specified at requirement level; implementation and effectiveness unverified

**Evidence reviewed and limitations:** No implementation or configuration evidence, function-specific acceptance thresholds, evaluation results, false-positive/false-negative rates or operational review evidence are available in the reviewed material.

**Further evidence required:** Obtain implementation/configuration and test evidence; define detection categories and acceptance thresholds; evaluate false positives and false negatives across relevant conditions; verify human review, escalation, override and ongoing monitoring.

**Linked assurance tests:**
- **AST-001 — Incident detection performance and acceptance criteria** (Execution status: Proposed).
  - Objective: Establish whether detection performance, false positives and false negatives can be evaluated against defined acceptance thresholds.
  - Proposed procedure: Review the defined detection categories, model or analytics configuration, test plan, dataset selection and ground-truth method. If authorised access and a suitable test environment become available, test representative cases across relevant conditions and report results by detection category and condition.
  - Required evidence: Approved detection requirements and thresholds; model/configuration documentation; test plan and test cases; representative labelled data or controlled scenarios; results by category and operating condition; finding-remediation records.
  - Pass criteria: Detection categories and acceptance thresholds are defined before testing; the test method and data are appropriate to intended use; results are reproducible and reported against each threshold; critical and high-severity test findings are resolved before the relevant validation milestone.

**Linked recommendations:**
- **REC-001 — Establish validated detection and accountable human oversight** (Status: Proposed).
  - Proposed action: Define incident-detection categories, operating conditions and approved acceptance thresholds; validate false-positive and false-negative performance; document which outputs may influence protocols or alerts; establish clear authorisation, human review, override, escalation and fallback procedures for consequential actions.
  - Acceptance criteria: Detection performance is evaluated against approved thresholds; roles and decision points are documented; required review and override mechanisms are evidenced; relevant failure scenarios are tested and findings have documented dispositions.


### RSK-002 — Unverified authorisation and override arrangements for automated protocols

**Assessment priority:** High<br>
**Evidence confidence:** Moderate

**Risk scenario:** If the deployed workflow does not provide effective authorisation, review, override and escalation arrangements for automated protocols and multichannel alerts, an inappropriate activation or failure to intervene could lead to a disproportionate, delayed or misdirected operational response.

**Source requirements:** SRC-008, SRC-009, SRC-011, SRC-023<br>
**Evidence gaps:** EG-001, EG-003, EG-004, EG-005

**Control position:** Human authorisation, review, override, failure handling and escalation arrangements are unverified; control effectiveness cannot be assessed.

**Evidence reviewed and limitations:** No implementation or operational evidence has been reviewed for the relevant authorisation, review, override and escalation arrangements; general test-plan requirements do not establish that these controls were implemented or tested.

**Further evidence required:** Obtain workflow and role documentation; identify which events or outputs can trigger each protocol and channel; verify approval gates, human review, override/cancellation, fallback handling, escalation responsibilities and logs; review test and incident records.

**Linked assurance tests:**
- **AST-002 — Authorisation, human review and override of automated protocols** (Execution status: Proposed).
  - Objective: Establish whether the intended operational workflow provides clear authority, human review where required, escalation, override and fallback arrangements.
  - Proposed procedure: Review workflow diagrams, operating procedures, role assignments and relevant permissions. Walk through scenarios involving a false detection, conflicting information, an urgent priority incident, a communications failure and an attempted cancellation or override. If access is authorised, inspect supporting configuration, logs and test evidence.
  - Required evidence: Protocol trigger rules; role and responsibility matrix; approval and escalation procedures; override/cancellation and fallback instructions; access configuration; operator training evidence; relevant audit logs and test results.
  - Pass criteria: Trigger conditions and responsible roles are clear; required approvals and human review points are documented; operators can exercise the specified override or cancellation powers; degraded/failure scenarios have defined handling; and the workflow can be evidenced through appropriate test records or logs.

**Linked recommendations:**
- **REC-001 — Establish validated detection and accountable human oversight** (Status: Proposed).
  - Proposed action: Define incident-detection categories, operating conditions and approved acceptance thresholds; validate false-positive and false-negative performance; document which outputs may influence protocols or alerts; establish clear authorisation, human review, override, escalation and fallback procedures for consequential actions.
  - Acceptance criteria: Detection performance is evaluated against approved thresholds; roles and decision points are documented; required review and override mechanisms are evidenced; relevant failure scenarios are tested and findings have documented dispositions.


### RSK-003 — Unreliable predictive analytics may misdirect public-safety planning or response

**Assessment priority:** High<br>
**Evidence confidence:** Moderate

**Risk scenario:** If predictive outputs are inaccurate, poorly calibrated or misunderstood, public-safety resources or attention may be directed toward the wrong locations, periods or incidents.

**Source requirements:** SRC-007, SRC-011, SRC-024<br>
**Evidence gaps:** EG-002, EG-003, EG-005, EG-007

**Control position:** Evaluation and monitoring controls are specified at a general or requirement level; implementation and effectiveness for the predictive function are unverified.

**Evidence reviewed and limitations:** No function-specific validation report, approved performance thresholds, calibration results, uncertainty presentation, data-suitability analysis or monitoring/retraining records have been reviewed.

**Further evidence required:** Obtain the model purpose and target definitions; approved evaluation metrics and thresholds; representative validation results; input/data-quality and drift analyses; operator guidance; monitoring, maintenance and change-control records.

**Linked assurance tests:**
- **AST-003 — Predictive-model purpose, validation and uncertainty handling** (Execution status: Proposed).
  - Objective: Determine whether the predictive function is adequately specified and validated for its intended public-safety use, and whether limitations and uncertainty are communicated appropriately.
  - Proposed procedure: First identify the specific prediction target and intended decision use. Review the model development/evaluation documentation, data selection, approved metrics and thresholds, assumptions affecting continued validity, and maintenance/retraining plans. If authorised model access and suitable data become available, assess performance on appropriate evaluation data, including temporal or geographic variation where relevant, and compare results with the approved criteria.
  - Required evidence: Model purpose and target definitions; CRISP-DM documentation where applicable; data description and provenance; evaluation methodology and results; RMC approval of proposed metrics and thresholds; calibration or uncertainty documentation where relevant; monitoring and maintenance/retraining records.
  - Pass criteria: Prediction targets and intended use are explicit; metrics and acceptable thresholds are approved by the RMC as required by the specification; evaluation data and methods are appropriate to the use; results are assessed against thresholds; limitations and uncertainty are documented; and required remediation or revalidation is evidenced.

**Linked recommendations:**
- **REC-002 — Validate predictive and event-correlation functions and monitor their reliability** (Status: Proposed).
  - Proposed action: Define the purpose and permitted operational use of each predictive and correlation function; document input data, event definitions and provenance; approve suitable evaluation metrics and thresholds; test representative conditions and error scenarios; establish ongoing performance monitoring, uncertainty communication, maintenance and revalidation triggers.
  - Acceptance criteria: Each function has documented purposes and evaluation criteria; validation results are compared with approved thresholds; correlation errors and source provenance are assessed; limitations and uncertainty are documented; monitoring and corrective-action responsibilities are assigned and evidenced.


### RSK-004 — Incorrect event correlation may combine, duplicate or misclassify incident information

**Assessment priority:** High<br>
**Evidence confidence:** Moderate

**Risk scenario:** If the event-correlation function incorrectly links unrelated reports, fails to link reports about the same event, or handles conflicting and delayed source data poorly, operators may receive a misleading incident picture.

**Source requirements:** SRC-004, SRC-006, SRC-012, SRC-023<br>
**Evidence gaps:** EG-002, EG-003, EG-004, EG-007

**Control position:** Capability and general test requirements are specified; the correlation mechanism, implementation and effectiveness are unverified.

**Evidence reviewed and limitations:** No design description, event-matching rules, conflict/duplicate handling procedures, source-provenance evidence, representative test results or operational correction records have been reviewed.

**Further evidence required:** Obtain the correlation design and event definitions; document sources and lineage; review handling of duplicate, conflicting, incomplete and delayed events; inspect representative test cases/results and correction/escalation procedures.

**Linked assurance tests:**
- **AST-004 — Event-correlation logic, provenance and error handling** (Execution status: Proposed).
  - Objective: Determine whether the event-correlation behaviour is specified, testable and supported by evidence appropriate to its intended operational use.
  - Proposed procedure: Review event definitions, correlation rules/model documentation, source mappings, data-quality assumptions, and test plans/results. If authorised test access is available, run controlled scenarios representing same-event reports, unrelated reports, duplicates, conflicting attributes, incomplete records and delayed inputs; compare outcomes with pre-defined expected results.
  - Required evidence: Event definitions and matching criteria; source/interface mappings; data dictionary and lineage; approved test cases and expected results; labelled or controlled test inputs; correlation outputs and error logs; remediation records.
  - Pass criteria: Expected behaviour is defined for each scenario; source provenance is retained; false links and missed links are measured against pre-defined criteria; conflicting, incomplete and delayed data have documented handling; results and exceptions are reproducible and traceable.

**Linked recommendations:**
- **REC-002 — Validate predictive and event-correlation functions and monitor their reliability** (Status: Proposed).
  - Proposed action: Define the purpose and permitted operational use of each predictive and correlation function; document input data, event definitions and provenance; approve suitable evaluation metrics and thresholds; test representative conditions and error scenarios; establish ongoing performance monitoring, uncertainty communication, maintenance and revalidation triggers.
  - Acceptance criteria: Each function has documented purposes and evaluation criteria; validation results are compared with approved thresholds; correlation errors and source provenance are assessed; limitations and uncertainty are documented; monitoring and corrective-action responsibilities are assigned and evidenced.


### RSK-005 — Public-safety information reused for CRM personalisation without adequately evidenced safeguards

**Assessment priority:** High<br>
**Evidence confidence:** Moderate

**Risk scenario:** If incident-related information or interactions are incorporated into unified CRM profiles and used for personalisation or awareness/loyalty campaigns without clearly defined purposes, data boundaries and safeguards, information collected in a public-safety context may be reused in ways affected people do not expect or that are not appropriately limited.

**Source requirements:** SRC-005, SRC-010, SRC-012<br>
**Evidence gaps:** EG-006

**Control position:** Purpose limitation, data minimisation, access boundaries, retention, transparency and any separation between public-safety and campaign uses are unverified in the reviewed material.

**Evidence reviewed and limitations:** No data-flow specification, field-level mapping, purpose/legal-basis assessment, transparency material, access matrix, retention schedule or evidence of controls over campaign reuse has been reviewed.

**Further evidence required:** Obtain the cross-module data-flow and field mappings; document purposes, roles, lawful basis and transparency arrangements; inspect access controls, retention/deletion rules, minimisation and separation of public-safety data from campaign use; confirm approval and audit trails for any reuse.

**Linked assurance tests:**
- **AST-005 — Cross-module purposes, data fields and access safeguards** (Execution status: Proposed).
  - Objective: Establish whether the documented design limits cross-module processing to defined purposes and whether data transfers and safeguards can be traced.
  - Proposed procedure: Obtain and compare the Public Safety-to-CRM data-flow diagram, field mapping, purpose descriptions and relevant privacy/governance documentation. Trace each specified field to its purpose, recipient, access roles, retention/deletion rule and any campaign/personalisation use. If permitted, inspect configured interfaces, access rules and relevant records to compare actual configuration with approved documentation.
  - Required evidence: Cross-module data-flow/interface specification; field-level mapping and data dictionary; purpose and role descriptions; applicable privacy assessment and transparency materials; access matrix; retention/deletion schedule; campaign-use rules; configuration or audit evidence where available.
  - Pass criteria: Each transferred field and purpose is documented; access and retention rules are assigned; reuse for personalisation/campaigns is explicitly addressed and justified; safeguards and restrictions are reflected in design/configuration evidence; unresolved legal or governance questions are escalated rather than assumed away.

**Linked recommendations:**
- **REC-003 — Define purpose, access and retention controls for safety-related and surveillance data** (Status: Proposed).
  - Proposed action: Map relevant data flows and fields; document the purposes and recipients of information transferred between Public Safety and the CRM/fidelity module; assess any proposed personalisation or campaign reuse; define and evidence role-based access, export restrictions, retention and deletion rules for relevant video, drone and incident data; document procedures for drone deployment and associated data handling.
  - Acceptance criteria: Relevant data flows, purposes, recipients and fields are documented; access and retention rules are defined for the applicable data categories; any CRM reuse is explicitly assessed and justified; implementation evidence supports the stated controls; unresolved questions are recorded for decision.


### RSK-006 — Video and drone data may be captured or retained without sufficiently evidenced access and lifecycle controls

**Assessment priority:** High<br>
**Evidence confidence:** Moderate

**Risk scenario:** If camera or drone footage and associated telemetry are captured, accessed, exported, retained or reused without suitable purpose, access, retention and review controls, individuals may be monitored or their information exposed beyond the intended operational need.

**Source requirements:** SRC-014, SRC-015, SRC-016, SRC-017, SRC-022<br>
**Evidence gaps:** EG-006, EG-007

**Control position:** Equipment, storage and certain security requirements are specified; actual access permissions, retention settings, deletion controls, drone operating procedures and safeguard effectiveness are unverified.

**Evidence reviewed and limitations:** No as-built camera/drone configuration, access matrix, retention/deletion evidence, export/access logs, operating procedures, data-protection assessment or commissioning evidence has been reviewed.

**Further evidence required:** Obtain deployment locations and enabled analytics; confirm purpose and necessity for capture; inspect access and export permissions, logging, retention/deletion configuration and monitoring; establish drone deployment/authorisation procedures and how footage and telemetry are handled; review commissioning evidence.

**Linked assurance tests:**
- **AST-006 — Video and drone data capture, access, export and retention controls** (Execution status: Proposed).
  - Objective: Determine whether video and drone data handling can be traced to documented purposes, permissions, retention settings and operating procedures.
  - Proposed procedure: Review camera/drone deployment and configuration records, enabled analytics, access permissions, export procedures and retention rules. Verify how the specified minimum 30-day local video storage requirement for critical channels is configured without assuming that this is the appropriate retention period for every data category. For drone operations, review deployment authorisation and footage/telemetry handling. If authorised, sample configuration and logs and test retention/deletion or access controls in a controlled environment.
  - Required evidence: Camera and drone inventory/configuration; deployment locations and enabled analytics; purpose and operating procedures; access matrix; export and access logs; retention schedule by data category; deletion/rotation evidence; commissioning records; drone deployment and telemetry handling procedures.
  - Pass criteria: Data capture and enabled analytics are linked to documented purposes; access and export permissions are role-based and evidenced; retention rules distinguish relevant data categories and the critical-channel minimum; deletion/rotation and logging operate as specified; drone deployment and telemetry handling responsibilities are documented.

**Linked recommendations:**
- **REC-003 — Define purpose, access and retention controls for safety-related and surveillance data** (Status: Proposed).
  - Proposed action: Map relevant data flows and fields; document the purposes and recipients of information transferred between Public Safety and the CRM/fidelity module; assess any proposed personalisation or campaign reuse; define and evidence role-based access, export restrictions, retention and deletion rules for relevant video, drone and incident data; document procedures for drone deployment and associated data handling.
  - Acceptance criteria: Relevant data flows, purposes, recipients and fields are documented; access and retention rules are defined for the applicable data categories; any CRM reuse is explicitly assessed and justified; implementation evidence supports the stated controls; unresolved questions are recorded for decision.


### RSK-007 — Security or integration weaknesses may compromise system integrity or availability

**Assessment priority:** High<br>
**Evidence confidence:** Moderate

**Risk scenario:** If interfaces between Public Safety and connected municipal systems are incorrectly configured, insufficiently protected or inadequately monitored, unauthorised activity or integration failures could affect the confidentiality, integrity or availability of information used in public-safety operations.

**Source requirements:** SRC-004, SRC-013, SRC-021, SRC-023<br>
**Evidence gaps:** EG-004, EG-005, EG-007

**Control position:** Security, integration and logging controls are specified at requirement level; implementation and effectiveness are unverified.

**Evidence reviewed and limitations:** No interface specifications, deployed access-control configuration, integration test results, security assessment, log-monitoring evidence or remediation records have been reviewed.

**Further evidence required:** Obtain interface and network documentation; review authentication, authorisation, data validation and error handling; inspect security and integration test results; verify logging coverage, protection against log tampering, alerting and remediation processes.

**Linked assurance tests:**
- **AST-007 — Security controls and connected-system integration** (Execution status: Proposed).
  - Objective: Assess whether the documented interface, access-control, logging and integration requirements are supported by implementation and test evidence.
  - Proposed procedure: Review interface specifications, authentication and authorisation arrangements, API security requirements, integration test results, centralised logging configuration and relevant audit/monitoring procedures. If authorised testing is available, execute approved negative and failure-path tests in a controlled environment and verify logging and alert behaviour.
  - Required evidence: Interface and network documentation; access-control configuration; API security requirements; integration and security test cases/results; logging configuration and sample events; monitoring and remediation records.
  - Pass criteria: Interface permissions and security requirements are documented; integration tests cover expected and failure scenarios; relevant actions and security events are logged and traceable; material findings are resolved or formally handled before the relevant acceptance milestone.

**Linked recommendations:**
- **REC-004 — Verify connected-system security and service recovery readiness** (Status: Proposed).
  - Proposed action: Review deployed interface security, access permissions, integration failure handling, audit logging and security monitoring. Separately verify recording redundancy, backup coverage, recovery objectives, restoration procedures and test results. Require material security, integration or recovery findings to have documented remediation or an approved disposition.
  - Acceptance criteria: Interface and logging controls are evidenced against applicable requirements; integration and security tests have documented results; backup and recovery coverage is defined; restoration tests demonstrate results against approved objectives; material findings are tracked to resolution or formal disposition.


### RSK-008 — Backup, recording or recovery failures may interrupt public-safety operations or remove needed evidence

**Assessment priority:** High<br>
**Evidence confidence:** Moderate

**Risk scenario:** If recording, backup or recovery arrangements fail or cannot restore usable information when needed, operators may lose access to video evidence, incident records or supporting information during an outage or emergency.

**Source requirements:** SRC-015, SRC-019, SRC-020, SRC-021<br>
**Evidence gaps:** EG-007

**Control position:** Resilience and recovery controls are specified; implementation, recovery performance and effectiveness are unverified.

**Evidence reviewed and limitations:** No as-built resilience design, backup configuration, retention mapping, restoration-test results, recovery objectives or evidence of recovery exercises have been reviewed.

**Further evidence required:** Obtain architecture and dependency documentation; inspect backup schedules and coverage, storage protection, retention requirements, restoration procedures, test results, recovery objectives and fault-handling records; verify how failures are detected and escalated.

**Linked assurance tests:**
- **AST-008 — Backup, recording and service-recovery readiness** (Execution status: Proposed).
  - Objective: Establish whether the specified resilience, backup, recording and restoration requirements are implemented and tested.
  - Proposed procedure: Review the resilience design, backup scope and schedules, recording redundancy, retention requirements, restoration procedures, recovery objectives and test results. If authorised, observe or execute a controlled restoration test and compare the recovered data and elapsed recovery time with pre-approved criteria.
  - Required evidence: As-built resilience design; backup configuration and logs; recording redundancy evidence; data-category retention mapping; documented recovery objectives; restoration test plan/results; failure and escalation records.
  - Pass criteria: Backup and recording coverage is defined; restoration procedures and recovery objectives are approved; test results demonstrate recovery of required data within the approved criteria; failures and exceptions are recorded and addressed.

**Linked recommendations:**
- **REC-004 — Verify connected-system security and service recovery readiness** (Status: Proposed).
  - Proposed action: Review deployed interface security, access permissions, integration failure handling, audit logging and security monitoring. Separately verify recording redundancy, backup coverage, recovery objectives, restoration procedures and test results. Require material security, integration or recovery findings to have documented remediation or an approved disposition.
  - Acceptance criteria: Interface and logging controls are evidenced against applicable requirements; integration and security tests have documented results; backup and recovery coverage is defined; restoration tests demonstrate results against approved objectives; material findings are tracked to resolution or formal disposition.


### RSK-009 — AI performance degradation may go undetected during operation

**Assessment priority:** High<br>
**Evidence confidence:** Moderate

**Risk scenario:** If the performance of detection, correlation or predictive functions degrades over time and that degradation is not identified promptly, operators may continue relying on outputs whose quality no longer meets operational needs.

**Source requirements:** SRC-007, SRC-009, SRC-011, SRC-023, SRC-024<br>
**Evidence gaps:** EG-002, EG-003, EG-005, EG-007

**Control position:** Monitoring and model-lifecycle requirements are specified at general level; implementation and effectiveness for each function are unverified.

**Evidence reviewed and limitations:** No approved function-specific thresholds, baseline evaluations, monitoring dashboards/alerts, drift analyses, maintenance records or evidence of review and corrective action have been reviewed.

**Further evidence required:** Obtain approved model-specific metrics and thresholds; baseline and ongoing evaluation results; monitoring frequency and alert rules; data/operational drift analyses; responsible review roles; maintenance, retraining and corrective-action records.

**Linked assurance tests:**
- **AST-009 — Ongoing AI performance monitoring and degradation detection** (Execution status: Proposed).
  - Objective: Determine whether deterioration in detection, correlation or predictive performance can be identified and addressed during operation.
  - Proposed procedure: Identify each function's approved performance measures and thresholds. Review baseline and ongoing evaluation results, monitoring frequency, input/data drift indicators, alert and review responsibilities, maintenance/retraining records, and examples of corrective action. If authorised operational evidence is available, trace a sample of monitoring alerts through review and disposition.
  - Required evidence: Model-specific metrics and thresholds; approval records; baseline and ongoing evaluation reports; monitoring dashboards or logs; drift assessments; review records; maintenance/retraining and corrective-action evidence.
  - Pass criteria: Relevant metrics and thresholds are defined and appropriately approved; monitoring evidence covers the intended functions and relevant conditions; exceptions trigger documented review; and required corrective action or revalidation can be traced to closure.

**Linked recommendations:**
- **REC-002 — Validate predictive and event-correlation functions and monitor their reliability** (Status: Proposed).
  - Proposed action: Define the purpose and permitted operational use of each predictive and correlation function; document input data, event definitions and provenance; approve suitable evaluation metrics and thresholds; test representative conditions and error scenarios; establish ongoing performance monitoring, uncertainty communication, maintenance and revalidation triggers.
  - Acceptance criteria: Each function has documented purposes and evaluation criteria; validation results are compared with approved thresholds; correlation errors and source provenance are assessed; limitations and uncertainty are documented; monitoring and corrective-action responsibilities are assigned and evidenced.


### RSK-010 — AI-related incidents and material changes may not be consistently investigated or controlled

**Assessment priority:** Moderate<br>
**Evidence confidence:** Moderate

**Risk scenario:** If an AI-related failure, unexpected output or material change occurs without a sufficiently documented and implemented process for reporting, triage, investigation, approval, rollback and follow-up, the issue may remain unresolved or recur without clear accountability.

**Source requirements:** SRC-021, SRC-023, SRC-024<br>
**Evidence gaps:** EG-004, EG-005, EG-007

**Control position:** Logging, testing and model-lifecycle requirements are specified; function-specific incident management, change accountability and effectiveness remain unverified.

**Evidence reviewed and limitations:** No incident taxonomy or reporting workflow, triage/escalation procedure, accountable owner map, change approval record, impact assessment, rollback procedure or post-incident review evidence has been reviewed.

**Further evidence required:** Obtain incident management and change-control procedures; confirm accountable roles, severity criteria, escalation and notification routes; inspect incident records, model/configuration changes, approval and validation evidence, rollback plans and post-incident reviews.

**Linked assurance tests:**
- **AST-010 — AI-related incident investigation and material-change control** (Execution status: Proposed).
  - Objective: Determine whether incidents and changes affecting AI-enabled functions have defined ownership, escalation, impact assessment, verification and closure procedures.
  - Proposed procedure: Review incident and change-management procedures, role assignments, severity criteria, approval and rollback rules, and post-incident review requirements. If records are available and access is authorised, trace a sample of relevant incidents or changes from identification through assessment, approval, testing, implementation, monitoring and closure.
  - Required evidence: Incident taxonomy and workflow; accountable role map; incident and change records; impact assessments; approval history; test evidence; rollback/fallback procedures; post-incident reviews; corrective-action tracking.
  - Pass criteria: Responsibilities and escalation routes are defined; material changes receive documented impact assessment and appropriate approval/testing; incidents are investigated and corrective actions tracked; relevant decisions and outcomes are auditable.

**Linked recommendations:**
- **REC-005 — Establish accountable AI incident and material-change governance** (Status: Proposed).
  - Proposed action: Define and assign responsibilities for reporting, classifying, escalating and investigating AI-related incidents and unexpected outputs. Establish a proportionate change process covering impact assessment, approval, validation, rollback or fallback planning, post-incident review and corrective-action tracking. Ensure relevant decisions and outcomes are traceable through appropriate records.
  - Acceptance criteria: Accountable roles and escalation routes are documented; incident and change procedures define required assessments and approvals; material changes have traceable validation and rollback/fallback considerations; corrective actions are tracked and closure is evidenced.


### RSK-011 — External data-source quality or provenance may distort analysis if sources are used by Public Safety

**Assessment priority:** Moderate<br>
**Evidence confidence:** Low

**Risk scenario:** If external tourism, mobility, crime or other indicators are incorporated into Public Safety analysis without adequate provenance, freshness, suitability and quality checks, the resulting analysis or prioritisation may be misleading.

**Source requirements:** SRC-007, SRC-012, SRC-025<br>
**Evidence gaps:** EG-002, EG-003, EG-008

**Control position:** Connection of the listed external sources to Module #32 is unverified; data provenance, freshness, suitability and quality controls for any such integration are also unverified.

**Evidence reviewed and limitations:** No interface mapping, source lineage, data dictionary, freshness/quality thresholds, validation results, ownership information or monitoring evidence has been reviewed for a connection between Annex I sources and Public Safety.

**Further evidence required:** Obtain Module #32 interface mappings and source lineage; establish whether Annex I sources are used; if so, identify source owners, fields, refresh frequency, quality/freshness checks, transformations, validation rules and monitoring.

**Linked assurance tests:**
- **AST-011 — External indicator integration, provenance and data-quality validation** (Execution status: Proposed).
  - Objective: Establish whether an integration exists before assessing its data-quality controls or influence on Public Safety outputs.
  - Proposed procedure: First obtain authoritative interface mappings and determine whether Annex I sources are connected to Module #32. If no connection is evidenced, record the dependency as unverified and do not infer that the risk pathway is active. If a connection is confirmed, trace selected data fields from source to use, inspect source ownership and refresh frequency, review validation and transformation rules, and assess monitoring and error handling.
  - Required evidence: Module #32 interface mappings; data lineage and data dictionary; source owner and provenance records; data refresh/freshness rules; transformations and validation logic; data-quality monitoring results; documented use of indicators in analysis or prediction.
  - Pass criteria: The existence or absence of the interface is evidenced; any connected source has documented ownership, provenance, fields, transformations, freshness and suitability criteria; quality exceptions are monitored and handled; and the influence of data on relevant outputs is traceable.

**Linked recommendations:**
- **REC-006 — Establish whether Annex I indicators feed Public Safety and validate any confirmed dependency** (Status: Proposed).
  - Proposed action: Obtain authoritative interface mappings to determine whether any Annex I external source or indicator is connected to Module #32. If a connection is confirmed, document the purpose, source owner, fields, provenance, refresh frequency, transformations, data-quality checks and monitoring. If no connection can be evidenced, retain the dependency as unresolved and do not assume that the listed sources feed Public Safety.
  - Acceptance criteria: The presence or absence of the interface is supported by authoritative evidence; any confirmed source has documented lineage, ownership, purpose, freshness and quality criteria; monitoring and exception handling are evidenced where applicable.

<!-- CONTROL-MAPPING-END -->

## Verification principles

A requirement does not prove implementation. A description of a control does not prove that it operates as intended. A proposed assurance test does not constitute a test result.

Where evidence is unavailable, the mapping will record that limitation instead of assigning an unsupported effectiveness rating.

## Status

The structured risk, assurance-test, and recommendations registers exist. A consolidated control-by-control assurance mapping has not yet been completed.

The next analytical step is to derive that mapping from the existing registers and source requirements, preserving the distinction between specified controls, available evidence, and proposed verification activities.