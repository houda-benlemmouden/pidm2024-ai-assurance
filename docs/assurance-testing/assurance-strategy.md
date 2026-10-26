# Public Safety Assurance Strategy

## 1. Purpose

This document defines the proposed assurance approach for the AI-enabled capabilities and related operational controls specified for PIDM2024 Module #32 (Public Safety).

The strategy translates the identified risks into evidence requests, document reviews, walkthroughs and, where authorised and practicable, controlled technical tests.

This is an independent, desk-based portfolio assessment. The strategy does not establish that the specified system has been deployed, that its controls are effective, or that any proposed test has been executed.

The `registers/assurance-test-register.csv` file is the detailed record of proposed tests, related risks, source requirements, evidence needs, procedures and pass or exception criteria.

## 2. Objectives

The assurance activities are intended to:

- Determine whether requirements and relevant controls are sufficiently specified and traceable.
- Identify the implementation and operational evidence needed to assess material risks.
- Examine whether proposed safeguards address the risk scenarios recorded in the risk register.
- Define conditions for evaluating performance, oversight, data handling, security, resilience and accountability.
- Distinguish satisfactory evidence, exceptions, unresolved questions and matters that cannot be concluded from the available material.
- Support proportionate recommendations linked to identified risks and evidence gaps.

## 3. Scope

The assurance approach covers:

- Automatic incident detection and its performance criteria.
- Human review, authorisation, override and escalation for automated protocols and alerts.
- Predictive analytics and model-validation evidence.
- Multi-source event correlation and data provenance.
- Cross-module data use involving incident reporting and CRM personalisation.
- Video and drone data capture, access, export and retention.
- Connected-system security, integration and audit logging.
- Backup, recording and recovery readiness.
- Ongoing AI performance monitoring and degradation detection.
- AI-related incident management and material-change control.
- External data-source quality and provenance, where a connection to Public Safety is established.

The assessment remains limited to Public Safety and the implications of its documented interfaces. Other PIDM2024 components are not assessed as independent systems.

## 4. Assurance Principles

### 4.1 Evidence before conclusions

Each material conclusion must be supported by identified evidence or explicitly labelled as an inference, an unknown or a matter requiring verification.

A procurement requirement is not proof that the corresponding capability or control has been implemented or operates effectively.

### 4.2 Traceability

Each proposed test must identify its related risk IDs, source-requirement IDs and evidence-gap IDs. Findings and recommendations should be traceable back to the relevant evidence and risk scenarios.

### 4.3 Proportionate testing

Document review and structured walkthroughs should be used where they can answer the assurance question. Technical or operational testing should be proposed only where suitable access, permissions, data and test conditions are available.

No testing of a live system, intrusive inspection or access to personal or operational data should be implied unless it has been explicitly authorised and actually performed.

### 4.4 Uncertainty remains visible

Where required evidence is missing, contradictory or insufficient to support a conclusion, the result should be recorded as unresolved or unable to conclude. Missing evidence must not automatically be treated as proof that a control is absent or ineffective.

### 4.5 Proposed and executed activities remain distinct

All entries in the current assurance-test register are marked `Proposed`. A test may be marked as executed only when the activity has actually been performed and its date, evidence and results have been recorded.

## 5. Assurance Workstreams and Sequence

The proposed activities are grouped into six workstreams. This sequence supports dependency management; it does not mean that any test has already been performed.

### Workstream 1: Detection and operational oversight

**Tests:** AST-001, AST-002

Establish the intended detection categories and performance criteria, then examine how incident information relates to operational decisions, protocol activation, human review, override and escalation.

The key dependency is that meaningful performance testing requires defined intended uses, test scenarios, expected outcomes and acceptance criteria.

### Workstream 2: Predictive analytics and event correlation

**Tests:** AST-003, AST-004

Review prediction targets, evaluation methods, approved metrics, thresholds and uncertainty handling. Separately examine event definitions, correlation rules, source provenance and the handling of duplicate, conflicting, incomplete or delayed information.

The two functions should remain distinct unless evidence establishes their technical relationship.

### Workstream 3: Data use and surveillance lifecycle

**Tests:** AST-005, AST-006

Review cross-module purposes and data fields, particularly the documented relationship between safety-related interactions and CRM personalisation or campaigns. Separately assess video and drone capture, access, export, retention, deletion and operating procedures.

The assessment must not assume that every listed data source is connected to every function, or that the presence of an integration requirement proves live data transfer.

### Workstream 4: Security and operational resilience

**Tests:** AST-007, AST-008

Examine interface protection, access controls, integration testing, audit logging and security-event traceability. Separately review recording redundancy, backup coverage, restoration procedures and evidence of recovery testing.

Any technical test must take place in an authorised environment and follow approved safeguards.

### Workstream 5: Performance monitoring and governance

**Tests:** AST-009, AST-010

Review ongoing performance indicators, thresholds, monitoring, degradation detection, maintenance and retraining. Separately examine AI-related incident reporting, investigation, change approval, impact assessment, rollback and corrective-action tracking.

The existence of general model-lifecycle or logging requirements does not establish that these processes are implemented for each function.

### Workstream 6: External data-source dependencies

**Test:** AST-011

First establish whether any Annex I external data sources or indicators are connected to Public Safety Module #32. If the connection is not evidenced, record it as unresolved and do not infer that the integration is active.

If a connection is confirmed, review provenance, ownership, freshness, suitability, transformations, quality monitoring and how the information affects relevant analysis.

## 6. Evidence Collection

Evidence should be requested according to the relevant test. Depending on the assurance question, it may include:

- Approved requirements, system and interface specifications, architecture diagrams and data-flow mappings.
- Model documentation, intended-use definitions, evaluation metrics, acceptance thresholds and validation results.
- Workflow procedures, role assignments, authorisation rules, training records and override or escalation evidence.
- Data dictionaries, source lineage, access matrices, retention schedules, deletion evidence and relevant privacy documentation.
- Integration and security test results, audit logs, monitoring records and remediation history.
- Backup configurations, recovery objectives, restoration tests, incident records and change approvals.

Where an artefact is unavailable, the register should record the missing evidence, the resulting limitation and the conclusion that can and cannot be supported.

## 7. Interpreting Test Outcomes

Each executed test should produce a documented outcome supported by the evidence reviewed.

### Satisfactory

The required evidence is available and demonstrates that the defined pass criteria are met within the scope and limitations of the test.

### Exception identified

The evidence demonstrates that one or more pass criteria are not met, or an observed result conflicts with a specified requirement or approved criterion. The exception should identify the evidence, impact and any remediation or further investigation required.

### Unable to conclude

The evidence is missing, incomplete, contradictory or otherwise insufficient to determine whether the pass criteria are met. This is an unresolved assurance outcome, not automatic proof of failure.

### Not applicable

The test or part of the test does not apply to the evidenced configuration or scope. The rationale and supporting evidence must be recorded before the item is treated as not applicable.

For every outcome, record the evidence examined, limitations, unresolved questions and any resulting recommendation. A satisfactory document review should not be represented as proof of operational effectiveness when that would require configuration inspection, performance testing or other evidence.

## 8. Prioritisation and Dependencies

Initial assurance priority is recorded in the test register. Activities should be prioritised by the potential consequences of the associated risk, the importance of unresolved evidence, dependencies between tests, and the feasibility of obtaining reliable evidence.

Where performance testing depends on approved thresholds or suitable datasets, those prerequisites should be established first. Where a test depends on a confirmed interface or deployment, that dependency must be resolved before conclusions about the relevant operational pathway are drawn.

Priority labels determine the order of evidence collection. They do not establish event likelihood, actual harm, control failure or residual risk.

## 9. Tool-Assisted Quality Checks

Python validation scripts may be used to check the structure and internal consistency of the assessment artefacts, including:

- Required CSV columns and record field counts.
- Unique risk and test identifiers.
- References to existing risk, source-requirement and evidence-gap IDs.
- Valid rating values and scoring calculations where applicable.
- Consistent test-status values and traceability between registers.

These checks validate the portfolio artefacts. They do not test the actual Public Safety system, verify source truth independently or establish the effectiveness of any operational control.

## 10. Limitations and Status

This strategy defines proposed assurance activities for an independent, desk-based assessment. No live-system testing, operational validation or control-effectiveness assessment should be claimed unless it is actually performed, appropriately authorised and documented.

**Status:** Proposed assurance strategy. The detailed procedures and criteria are maintained in `registers/assurance-test-register.csv`. All tests remain proposed until execution evidence is recorded.