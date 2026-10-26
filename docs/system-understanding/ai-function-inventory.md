# AI Function Inventory

## 1. Purpose and Scope

This inventory identifies AI-enabled functions described in the technical specification for PIDM2024 Module #32 (Public Safety) and its associated infrastructure requirements.

It provides a structured view of each function's stated purpose, documented inputs, outputs or operational consequences, and outstanding verification questions.

The inventory is based on the reviewed procurement specification. It does not establish actual deployment, configuration, performance or operational effectiveness.

## 2. Evidence Conventions

- **Specified:** Explicitly described in the reviewed source.
- **Partially specified:** A capability is described, but important technical or operational details remain unclear.
- **Unverified:** Implementation or operational evidence has not been reviewed.

A function's inclusion in this inventory does not mean it is confirmed to be operational.

## 3. AI-Enabled Function Inventory

### AI-FN-001: Automatic Incident Detection

**Source references:** §7.5.2–7.5.3, pp. 82–84.

**Stated purpose:** Detect incidents automatically using AI-enabled video analysis, IoT devices and events from municipal systems.

**Documented inputs:**
- Video feeds and CCTV.
- IoT sensor data.
- Events from municipal systems.

**Documented outputs or consequences:**

- Automatic incident detection is specified as a capability of the Public Safety module.
- The wider module specification describes incident management, GIS visualisation, automated multi-area protocols and multichannel alerts. The precise relationship between individual detection outputs and these downstream functions requires verification.

**Outstanding questions:**
- Which incident types are within scope?
- Which detection methods or models are used for each incident type?
- What are the evaluation datasets, metrics and acceptance thresholds?
- How are false positives and false negatives handled?
- Which detections require human confirmation before operational action?

**Evidence status:** Specified at capability level; implementation and performance unverified.

### AI-FN-002: Multi-Source Event Correlation

**Source references:** §7.5.3, pp. 83–84.

**Stated purpose:** Use AI to correlate events captured from multiple sources, group related incidents, and avoid duplicate incidents.

**Documented inputs:**
- Sensors and cameras.
- Social-media sources.
- GESPOL and other municipal-system information.

**Documented outputs or consequences:**
- Correlated event information for operational use.

**Outstanding questions:**
- What constitutes a correlated event?
- How are duplicate, conflicting, incomplete or delayed reports handled?
- Does correlation use AI/ML, predefined rules, or a combination?
- How is the provenance of each contributing source retained?
- How are incorrect correlations identified and corrected?

**Evidence status:** Specified at capability level; technical design and validation unverified.

### AI-FN-003: Predictive Analytics

**Source references:** §7.5.3, pp. 83–84; §5.9.2, p. 30.

**Stated purpose:** Use historical incidents, seasonality, environmental information, GIS and video-related information to support predictive analysis.

**Documented inputs:**
- Historical incident records.
- Meteorological data from AEMET and municipal sensors.
- Urban and tourism GIS layers.
- Real-time information from the video-surveillance system.

**Processing environment:** The specification states that processing takes place locally on the module server, which has a dedicated GPU and is integrated with IDIS, GESPOL and GIS. It describes local analytics without recurring cloud costs and includes maintenance within the module infrastructure.

**Outstanding clarification:** The exact predictive targets, model architecture and allocation of inputs to individual models are not specified in the reviewed passage.

**Documented outputs or consequences:**

- Predictive analytics intended to anticipate risks and support proactive action, as described in §7.5.2.
- The specific prediction targets, output formats and operational uses are not defined in the reviewed passage.

**Outstanding questions:**
- What specific outcomes are predicted: incident likelihood, location, severity, demand or something else?
- Which inputs are actually used by each predictive model?
- What metrics and acceptable thresholds have been approved by the RMC?
- How are training and evaluation data selected and documented?
- How are prediction uncertainty, model limitations and performance changes communicated to operators?
- What maintenance, retraining and change-control procedures apply?

**Evidence status:** Specified at capability level; model design, evaluation and operational use unverified.

### AI-FN-004: Embedded Camera Analytics

**Source references:** Annex II, §§1.2.1.1–1.2.1.2, pp. 248–249.

**Stated purpose:** Provide video analytics through specified PTZ and fixed cameras.

**Documented capabilities include:**

- **PTZ cameras:** automatic tracking, line-crossing detection, loitering detection, object classification and tamper detection.
- **Fixed cameras:** people and vehicle detection, intrusion detection, abandoned-object detection, occupancy counting, zone occupancy and tamper detection.

These are specified equipment capabilities. The specification does not establish that every feature will be enabled or used operationally.

These are specified equipment capabilities; the document does not establish that every feature will be enabled or used operationally.

**Documented inputs:**
- Camera video streams.

**Documented outputs or consequences:**
- Analytics events or detections that may support surveillance and incident-management workflows.

**Outstanding questions:**
- Which analytics functions are enabled, and at which locations?
- What objects, behaviours and event categories are detected?
- How are performance and error rates assessed under different operating conditions?
- What retention, access and review controls apply to video and analytics outputs?
- How are camera analytics integrated with the Public Safety module and video-management system?

**Evidence status:** Equipment capabilities specified; deployed configuration, enabled functions and performance unverified.

### AI-FN-005: Drone-Based Analytics

**Source references:** Annex II, §1.2.5, pp. 251–253.

**Stated purpose:** Provide aerial video and telemetry with AI-based functions, integrated with GIS and the video-management system.

**Documented capabilities include:**

- **Image enhancement:** improve contrast and sharpness in conditions of extreme fog, and provide full-colour night vision in near-total darkness.
- **Object analytics:** automatically classify and count objects, people and/or animals, with intelligent real-time tracking.
- **Fire-area assessment:** detect and delineate areas affected by fires, calculate wind direction, predict potentially affected areas, and identify safe operational access zones.

The specification requires these capabilities to integrate with the Public Safety module’s video-management system and GIS, with real-time use in emergency environments and visualisation on the CME’s large LED display.

These are specified requirements, not evidence that the capabilities have been delivered, configured, validated or used operationally.

**Documented inputs:**
- Aerial video.
- Drone telemetry.
- GIS and video-management-system information, as relevant to the specified integration.

**Documented outputs or consequences:**
- Aerial imagery, telemetry and analytics intended to support situational awareness and operational assessment.

**Outstanding questions:**
- Which analytics are enabled for each operational use?
- How are outputs validated and communicated to personnel?
- What restrictions govern deployment, data capture, storage and access?
- What procedures apply when visibility, connectivity or analytics performance is inadequate?
- How are operational safety, authorisation and accountability documented?

**Evidence status:** Equipment and capability requirements specified; operational configuration, safeguards and performance unverified.

## 4. Cross-Cutting Observations

The five entries describe different functions and should not be treated as one model or one AI system without further evidence.

In particular:

- Automatic incident detection and embedded camera analytics may be related, but their exact technical relationship is not established by the reviewed passages.
- Multi-source event correlation may combine information from several systems, but the specification does not establish whether the correlation mechanism is AI/ML, rule-based or hybrid.
- Predictive analytics is distinct from detecting an incident that is already occurring.
- Drone analytics introduces a separate aerial data-capture context and associated operational questions.
- General requirements for model evaluation, testing, audit and maintenance exist in the specification. Their application to each function and the results of any activities remain unverified.
- The specification also describes automated activation of multi-area protocols for priority incidents, with multichannel alerts. This is an important downstream operational consequence to consider when assessing detection and correlation errors. The reviewed passages do not establish that every alert or protocol activation is directly triggered by an AI model, nor do they fully specify the authorisation and human-review workflow.
- The specification also describes cross-module relationships: incidents submitted through the tourist portal and app; comparisons between safety indicators and perception surveys; feedback of safety-related interactions into a unified CRM profile for personalisation and campaigns; and the inclusion of safe zones, risk zones, police presence, active alerts and temporary restrictions in suggested tourist itineraries. These are specified relationships, not proof of operational data flows. Their purposes, data fields, access boundaries and safeguards require separate verification.

## 5. Limitations

This inventory is derived from the reviewed technical specification. It does not establish that the listed functions were delivered, enabled, connected, validated or used in live operations.

The outstanding questions are assessment questions, not findings of confirmed deficiencies or non-compliance.

Further conclusions require implementation documentation, system configuration, test results, operational procedures and other appropriate evidence.

## 6. Status

**Status:** Initial inventory based on the documentary source baseline.

The entries require a cross-check against the source requirements register and evidence-gaps register before they are used as the basis for detailed risk assessment.
