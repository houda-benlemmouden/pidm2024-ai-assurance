# Operational Context and Function Relationships

## 1. Purpose

This document describes the intended operational context of the Public Safety module specified in the PIDM2024 technical procurement specification.

It connects the AI-enabled functions identified in the AI Function Inventory to their documented inputs, outputs, operational relationships, and outstanding assurance questions.

The document is based on the reviewed procurement specification. It does not establish that the described components, integrations, or workflows have been implemented or are operating as specified.

## 2. Evidence and Interpretation

The following distinctions apply throughout this document:

- **Specified:** Explicitly described in the reviewed procurement specification.
- **Interpretation:** An analytical explanation of how documented capabilities or relationships may fit together.
- **Unverified:** A technical, operational, or organisational detail that requires further evidence.

A documented relationship between components does not, by itself, establish the exact data flow, triggering mechanism, authorisation process, or operational responsibility.

## 3. Operational Context

The Public Safety module is intended to support the management of urban incidents and emergencies affecting tourism.

The specification describes a technical environment involving video surveillance, IoT sensors, municipal systems, GIS information, incident-management functions, event correlation, predictive analytics, and automated alerts or protocols.

The documented environment includes integrations or relationships involving IDIS, GESPOL, GIS, the tourist portal and application, the perception-analysis module, the CRM/fidelity module, and the route planner.

The exact implementation and operational configuration of these relationships remain unverified.

## 4. Relationship Between AI-Enabled Functions

### 4.1 Automatic Incident Detection

**Documented capability:** The specification describes automatic incident detection using AI-enabled video analysis, IoT devices, and events from municipal systems.

**Operational significance:** Detection outputs may contribute to incident awareness and subsequent incident-management or alerting activities.

**Requires verification:** Incident categories, detection methods, thresholds, error handling, and whether human confirmation is required before action.

### 4.2 Embedded Camera Analytics

**Documented capability:** The camera requirements describe analytics including object classification and tracking, people and vehicle detection, intrusion detection, abandoned-object detection, line crossing, loitering, and tamper detection.

**Operational significance:** Camera-generated events may provide information relevant to surveillance and incident management.

**Requires verification:** Which functions are enabled, how camera analytics connect to the Public Safety module, and how camera-generated events relate to the module's automatic incident-detection function.

### 4.3 Multi-Source Event Correlation

**Documented capability:** The specification describes correlating information from sources including sensors, cameras, social media, GESPOL, and other municipal systems.

**Operational significance:** Correlated information may support a broader operational understanding of events than an individual source provides.

**Requires verification:** The correlation logic, treatment of conflicting or duplicate information, source provenance, and the relationship between correlation results and incident classification or escalation.

### 4.4 Predictive Analytics

**Documented capability:** The specification describes predictive analysis involving historical incident records, meteorological information, urban and tourism GIS layers, and real-time video-surveillance information.

**Operational significance:** Predictive outputs are intended to support public-safety planning or operations.

**Requires verification:** The specific outcomes predicted, the inputs used by individual models, the interpretation of predictions, and whether predictions influence operational priorities or actions.

### 4.5 Drone-Based Analytics

**Documented capability:** The drone requirements describe aerial video, telemetry, and AI-based capabilities such as object classification and counting, tracking, low-visibility imaging, and fire-area assessment.

**Operational significance:** These capabilities may contribute aerial information to situational awareness and operational assessment.

**Requires verification:** The operational uses of individual analytics, their integration with GIS and video management, and the procedures governing the use and review of their outputs.

## 5. Downstream Operational Consequences

The specification describes automated activation of multi-area protocols for priority incidents and alerts distributed through multiple channels.

These capabilities are relevant to the assessment because detection, correlation, or prediction errors could potentially affect subsequent operational responses.

However, the reviewed passages do not establish that every protocol activation or alert is directly triggered by an AI model.

The following details therefore require verification:

- The conditions that trigger an alert or protocol.
- The relationship between AI-generated information and operational decisions.
- The roles authorised to confirm, reject, escalate, or close an incident.
- The availability of human review before consequential actions.
- The handling of incorrect, incomplete, delayed, or conflicting information.
- The recording of decisions, overrides, and subsequent corrections.

These are assurance questions, not findings that the corresponding controls are absent.

## 6. Cross-Module Relationships

The specification describes relationships between Public Safety and other PIDM2024 components, including:

- Tourist portal and application: submission of incident-related information.
- Perception-analysis module: comparison of safety indicators with perception-survey information.
- CRM/fidelity module: incorporation of safety-related interactions into a unified profile for personalisation and campaigns.
- Route planner: use of information such as safe zones, risk zones, police presence, active alerts, and temporary restrictions in suggested itineraries.

These relationships may raise questions about purpose limitation, data minimisation, access control, information accuracy, retention, and the separation of public-safety purposes from personalisation or marketing purposes.

The specification's description of a relationship does not establish which data fields are transferred, whether transfers occur in live operation, or what safeguards are implemented.

The assessment remains limited to the Public Safety module and the implications of its documented interfaces. It does not assess the other modules as independent systems.

## 7. Initial Assurance Questions

The operational relationships described above suggest several areas for further evidence collection:

1. **Function boundaries:** How are camera analytics, automatic incident detection, event correlation, predictive analytics, and drone analytics separated or connected?
2. **Data lineage:** Can information be traced from its originating source through processing to the resulting event, alert, or operational decision?
3. **Error handling:** How are false detections, incorrect correlations, and unreliable predictions identified and managed?
4. **Human oversight:** Who reviews or authorises consequential operational actions, and under what conditions?
5. **Escalation:** What rules govern incident prioritisation, protocol activation, and multichannel alerts?
6. **Cross-module data use:** What information is shared with other modules, for what purposes, and under which access and retention controls?
7. **Performance and change:** How are accuracy, operational performance, model changes, and degradation assessed over time?

These questions should be linked to the source requirements and evidence gaps before being converted into detailed risks or assurance tests.

## 8. Traceability to Existing Registers

The operational relationships and assurance questions described in this document should be interpreted alongside the existing source-requirements and evidence-gaps registers.

| Operational area | Source requirements | Related evidence gaps |
|---|---|---|
| Automatic incident detection | SRC-003, SRC-009, SRC-012 | EG-001, EG-002, EG-003, EG-007 |
| Embedded camera analytics | SRC-014, SRC-015, SRC-022 | EG-002, EG-003, EG-006, EG-007 |
| Multi-source event correlation | SRC-006, SRC-012 | EG-001, EG-002, EG-004, EG-007 |
| Predictive analytics | SRC-007, SRC-024 | EG-002, EG-003, EG-005 |
| Automated protocols and alerts | SRC-008, SRC-011 | EG-001, EG-003, EG-004, EG-005 |
| Drone-based analytics | SRC-017 | EG-001, EG-002, EG-006, EG-007 |
| Cross-module data relationships | SRC-005, SRC-010, SRC-012, SRC-025 | EG-006, EG-008 |
| Integration, logging and operational evidence | SRC-004, SRC-013, SRC-021, SRC-023 | EG-004, EG-005, EG-007 |

These mappings identify relevant existing records; they do not establish that a requirement has been fulfilled, that a control is effective, or that a risk has been confirmed.

The mappings should be reviewed against the source passages and updated if subsequent analysis identifies a more specific relationship.

## 9. Limitations and Status

This document describes the intended context and relationships indicated by the reviewed procurement specification. It does not confirm deployed architecture, actual data flows, operational procedures, model performance, control effectiveness, or legal compliance.

**Status:** Initial analytical context based on the documentary source baseline. Relationships and assumptions require cross-checking against the source requirements register and evidence-gaps register.
