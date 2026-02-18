# Incident Postmortem Analysis

## Purpose

This skill converts incident evidence into a structured postmortem with root-cause analysis, corrective actions, and prevention metrics. It is designed for blameless analysis and repeatable reliability improvements.

## Inputs

| Name | Type | Required | Description | Constraints |
|------|------|----------|-------------|-------------|
| `incident_id` | string | Yes | Unique identifier for the incident | Non-empty string |
| `incident_timeline` | array | Yes | Chronological event timeline | At least 3 timestamped events |
| `customer_impact` | string | Yes | User-facing impact summary | Describe scope and duration |
| `systems_involved` | array | Yes | Services/components involved | At least 1 service |
| `detection_and_response` | object | No | How incident was detected and handled | Include alert source and response times when known |
| `known_contributing_factors` | array | No | Initial hypotheses or contributing conditions | Optional, can be empty |

## Output Format

```json
{
  "postmortem_analysis": {
    "severity": "SEV-2",
    "root_causes": [
      {
        "category": "change-management",
        "description": "Unreviewed config toggle bypassed safeguard"
      }
    ],
    "contributing_factors": [
      "Alert threshold too permissive",
      "Runbook lacked rollback decision tree"
    ],
    "corrective_actions": [
      {
        "id": "PM-12",
        "owner": "platform-team",
        "priority": "high",
        "due_date": "2026-03-15"
      }
    ],
    "prevention_metrics": [
      "MTTD",
      "MTTR",
      "repeat-incident rate"
    ],
    "postmortem_status": "action_items_open"
  },
  "executive_summary": "Primary root cause identified with high confidence; prevention work is in progress."
}
```

## Constraints

- **Blameless Standard**: Focus on system conditions and decisions, not individual blame.
- **Evidence Requirement**: Root causes must be traceable to timeline evidence.
- **Actionability**: Corrective actions must be owner-assigned and time-bound.
- **Scope Boundaries**: Include only incident-relevant systems unless dependencies are proven.
- **Learning Loop**: Close the postmortem only when follow-up actions are tracked to completion.

## Invocation

### Example 1: Payments API Latency Incident

**Input**:
```json
{
  "incident_id": "INC-2026-014",
  "incident_timeline": [
    "09:12 UTC: deploy started",
    "09:19 UTC: latency alerts fired",
    "09:28 UTC: rollback completed"
  ],
  "customer_impact": "Checkout failures rose to 8% for 16 minutes in NA region",
  "systems_involved": [
    "payments-api",
    "redis-cache",
    "feature-flag-service"
  ],
  "detection_and_response": {
    "detection": "synthetic monitor",
    "first_response_minutes": 4
  },
  "known_contributing_factors": [
    "Cache key cardinality spike"
  ]
}
```

**Output**:
```json
{
  "postmortem_analysis": {
    "severity": "SEV-2",
    "root_causes": [
      {
        "category": "capacity-planning",
        "description": "New query path caused hot-key amplification in cache"
      }
    ],
    "corrective_actions": [
      {
        "id": "PM-14",
        "owner": "payments-team",
        "priority": "high",
        "due_date": "2026-03-05"
      }
    ],
    "postmortem_status": "action_items_open"
  },
  "executive_summary": "Incident is understood and immediate mitigations are in place."
}
```

### Example 2: Identity Provider Degradation

**Input**:
```json
{
  "incident_id": "INC-2026-021",
  "incident_timeline": [
    "14:01 UTC: login error rate increased",
    "14:07 UTC: external IdP status page reported degradation",
    "14:31 UTC: failover policy enabled"
  ],
  "customer_impact": "SSO login unavailable for enterprise tenants for 30 minutes",
  "systems_involved": [
    "auth-gateway",
    "idp-adapter"
  ],
  "detection_and_response": {
    "detection": "error-rate SLO burn alert",
    "first_response_minutes": 3
  },
  "known_contributing_factors": [
    "No tested failover runbook for SSO-only tenants"
  ]
}
```

**Output**:
```json
{
  "postmortem_analysis": {
    "severity": "SEV-1",
    "root_causes": [
      {
        "category": "resilience",
        "description": "Failover path existed but was not operationally exercised"
      }
    ],
    "corrective_actions": [
      {
        "id": "PM-19",
        "owner": "identity-team",
        "priority": "critical",
        "due_date": "2026-02-28"
      }
    ],
    "postmortem_status": "pending_leadership_review"
  },
  "executive_summary": "Critical reliability gap identified; resiliency program escalated."
}
```
