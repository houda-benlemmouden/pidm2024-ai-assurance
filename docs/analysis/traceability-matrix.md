# Requirements Traceability Matrix

This matrix links each identified risk to the source requirements, evidence gaps, proposed assurance tests, and recommendations recorded in the assessment registers.

## Generated matrix

[Download the traceability matrix (CSV)](../generated/traceability-matrix.csv)

The table below is generated from the assessment registers by `scripts/generate_traceability_matrix.py`.

<!-- MATRIX-TABLE-START -->
| Risk ID | Risk | Source requirements | Evidence gaps | Assurance tests | Recommendations | Reference status |
| --- | --- | --- | --- | --- | --- | --- |
| RSK-001 | Incident detection errors may delay or misdirect response | SRC-008; SRC-009; SRC-023; SRC-024 | EG-001; EG-002; EG-003; EG-007 | AST-001 | REC-001 | References present |
| RSK-002 | Unverified authorisation and override arrangements for automated protocols | SRC-008; SRC-009; SRC-011; SRC-023 | EG-001; EG-003; EG-004; EG-005 | AST-002 | REC-001 | References present |
| RSK-003 | Unreliable predictive analytics may misdirect public-safety planning or response | SRC-007; SRC-011; SRC-024 | EG-002; EG-003; EG-005; EG-007 | AST-003 | REC-002 | References present |
| RSK-004 | Incorrect event correlation may combine, duplicate or misclassify incident information | SRC-004; SRC-006; SRC-012; SRC-023 | EG-002; EG-003; EG-004; EG-007 | AST-004 | REC-002 | References present |
| RSK-005 | Public-safety information reused for CRM personalisation without adequately evidenced safeguards | SRC-005; SRC-010; SRC-012 | EG-006 | AST-005 | REC-003 | References present |
| RSK-006 | Video and drone data may be captured or retained without sufficiently evidenced access and lifecycle controls | SRC-014; SRC-015; SRC-016; SRC-017; SRC-022 | EG-006; EG-007 | AST-006 | REC-003 | References present |
| RSK-007 | Security or integration weaknesses may compromise system integrity or availability | SRC-004; SRC-013; SRC-021; SRC-023 | EG-004; EG-005; EG-007 | AST-007 | REC-004 | References present |
| RSK-008 | Backup, recording or recovery failures may interrupt public-safety operations or remove needed evidence | SRC-015; SRC-019; SRC-020; SRC-021 | EG-007 | AST-008 | REC-004 | References present |
| RSK-009 | AI performance degradation may go undetected during operation | SRC-007; SRC-009; SRC-011; SRC-023; SRC-024 | EG-002; EG-003; EG-005; EG-007 | AST-009 | REC-002 | References present |
| RSK-010 | AI-related incidents and material changes may not be consistently investigated or controlled | SRC-021; SRC-023; SRC-024 | EG-004; EG-005; EG-007 | AST-010 | REC-005 | References present |
| RSK-011 | External data-source quality or provenance may distort analysis if sources are used by Public Safety | SRC-007; SRC-012; SRC-025 | EG-002; EG-003; EG-008 | AST-011 | REC-006 | References present |
<!-- MATRIX-TABLE-END -->

## How to interpret the matrix

The identifiers show relationships recorded in the assessment registers. They support navigation and review across the assessment artefacts.

A recorded relationship does not establish that the underlying evidence is sufficient, that a control has been implemented or verified, or that a proposed assurance test has been executed.

## Validation

The generation script checks for references to known risks, source requirements, and evidence gaps. Passing these checks establishes identifier consistency under the implemented rules, not the substantive correctness of every relationship.