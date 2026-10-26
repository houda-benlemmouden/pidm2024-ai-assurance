# Source and Requirements Register

**Project:** PIDM2024 Module #32, Public Safety  
**Source:** Official PIDM2024 technical specification, signed 19 November 2025  
**Source section:** 7.5, printed pages 82–85 of 255  
**Status:** Baseline draft v0.1  
**Assessment type:** Independent, desk-based assessment of public procurement documentation

## 1. Purpose

This register records source-backed requirements and system characteristics before risk conclusions are made. It distinguishes what the specification states from what remains unknown and what would need to be verified through implementation evidence.

## 2. Source and requirements register

| ID | Source location | Requirement or documented characteristic | Evidence type | Assurance relevance | Limitation / open question | Status |
|---|---|---|---|---|---|---|
| SRC-001 | §7.5.1, p. 82 | The module is intended to manage urban incidents and emergencies affecting the tourism environment in real time. | Stated purpose | Scope and intended use | Actual operational scope and deployment are unverified. | Source verified |
| SRC-002 | §7.5.2, p. 82 | Objectives include reducing response times and improving coordination between municipal services. | Stated objective | Performance and operational safety | Actual outcomes are not established here. | Source verified |
| SRC-003 | §7.5.2–7.5.3, pp. 82–84 | The specification describes AI, video analytics, GIS and sensors. | Stated capabilities | AI inventory and technical assurance | Specific model types, versions, limitations and validation methods are not established here. | Source verified |
| SRC-004 | §7.5.3, pp. 82–83 | Integration with GESPOL is mandatory and must support bidirectional data flows. | Functional requirement | Interoperability and security | Interface specifications, access controls and integration test results remain unknown. | Source verified |
| SRC-005 | §7.5.3, p. 83 | A multilingual electronic incident-reporting function is described for the tourist app and municipal website, including geolocation and multimedia. | Functional requirement | Privacy, data protection and accessibility | Data minimisation, permissions, retention and handling of uploaded media require further review. | Source verified |
| SRC-006 | §7.5.3, p. 83 | AI is intended to correlate events from sources including sensors, cameras, social networks and GESPOL, grouping related incidents and avoiding duplicates. | AI capability requirement | Accuracy, false positives, false negatives and data quality | Correlation logic, performance thresholds, testing and error handling are not established here. | Source verified |
| SRC-007 | §7.5.3, p. 83 | Predictive analytics are described using historical incidents, seasonal patterns, environmental conditions, GIS layers and video surveillance information. | AI capability requirement | Predictive validity and operational safety | Prediction targets, evaluation methods, uncertainty handling and limits on use remain unknown. | Source verified |
| SRC-008 | §7.5.3, pp. 83–84 | Automated multi-area protocols and multichannel alerts are described, including SMS, push notifications, email and intelligent sirens. | Automation requirement | Human oversight and safe escalation | Authorisation, approval gates, override, failure handling and escalation responsibilities require verification. | Source verified |
| SRC-009 | §7.5.3, p. 84 | Automatic incident detection is described using AI video analytics, IoT sensors and events from existing municipal systems. | AI capability requirement | Detection performance and safety | Detection categories, operating conditions, error rates and acceptance criteria remain unknown. | Source verified |
| SRC-010 | §7.5.4, p. 84 | Safety-related information may feed into a unified CRM user profile for service personalisation and campaign design. | Cross-module relationship | Privacy, purpose limitation and access governance | Data fields, legal basis, access boundaries, retention and restrictions on reuse require review. | Source verified |
| SRC-011 | §7.5.5, pp. 84–85 | KPIs include response times, incident counts by zone and severity, resolution within a six-hour target, alerts and multi-entity activations. | Monitoring requirement | Performance monitoring and assurance | KPI definitions, calculation rules, data quality and reporting responsibilities require verification. | Source verified |
| SRC-012 | §7.5.6–7.5.7, p. 85 | Sources include CCTV, environmental sensors, weather data, social networks, citizen channels, municipal systems and GIS. Outputs include geolocated incidents, alerts, KPIs and event histories. | Data inventory | Data governance and lifecycle management | Ownership, provenance, quality controls, access and retention are not fully established by this inventory. | Source verified |
| SRC-013 | §7.5.8, pp. 85–86 | The specification names interoperability standards, secure documented REST APIs and compatibility with the SEGITTUR Central Node. | Technical requirement | Integration assurance and cybersecurity | Compliance evidence, API security testing and conformance results remain unknown. | Source verified |

## 3. Evidence interpretation rules

1. A requirement in a specification is not proof that the capability has been implemented.
2. A missing statement in a reviewed section is not proof that a control does not exist elsewhere.
3. A potential risk is not automatically a legal violation.
4. Each risk conclusion must link to the relevant source evidence and clearly state any inference.
5. Proposed assurance tests must be labelled as proposed unless execution evidence exists.

## 4. Next verification steps

- Review the infrastructure annex and record camera, storage and server requirements separately.
- Review general security, privacy, logging, backup and training provisions.
- Search the full document for AI-specific oversight, validation, monitoring, incident management and accountability requirements.
- Record unresolved questions and the evidence needed to answer them.
- Freeze the baseline only after relevant sections and cross-references have been reviewed.

## 5. Independence statement

This is an independent portfolio assessment based on documentary evidence. It is not commissioned by, delivered to or endorsed by the Ayuntamiento de Málaga or any procurement participant. No claim is made that the described system has been deployed or that its controls have been tested in operation.