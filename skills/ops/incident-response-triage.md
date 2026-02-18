# Incident Response Triage

## Purpose

This skill classifies incoming incidents quickly, aligns severity to impact, and produces a coordinated response packet for on-call teams.

## Inputs

| Name | Type | Required | Description | Constraints |
|------|------|----------|-------------|-------------|
| `incident_signal` | string | Yes | Initial alert or report | Non-empty string |
| `impacted_services` | array | Yes | Services/systems impacted | At least 1 service |
| `customer_impact` | string | Yes | Observed user impact | Describe scope and severity |
| `error_budget_state` | string | No | Current SLO/error budget context | Optional |
| `known_dependencies` | array | No | Upstream/downstream dependencies | Optional |
| `oncall_roster` | array | No | Available responders by function | Optional |

## Output Format

```json
{
  "incident_triage": {
    "severity": "SEV-2",
    "classification_rationale": [
      "User-facing impact confirmed",
      "Partial service outage in one region"
    ],
    "initial_actions": [
      "Assign incident commander",
      "Start mitigation timeline",
      "Post customer status update"
    ],
    "responder_assignments": [
      {
        "role": "incident_commander",
        "owner": "oncall-sre"
      },
      {
        "role": "communications",
        "owner": "support-lead"
      }
    ],
    "next_checkpoints": [
      "15-minute technical update",
      "30-minute customer update"
    ]
  },
  "triage_status": "active"
}
```

## Constraints

- **Signal Uncertainty**: Initial severity can change as more evidence arrives.
- **Consistency**: Severity decisions should follow a documented rubric.
- **Comms Discipline**: External updates must align with verified facts.
- **Ownership Clarity**: Incident command and communications ownership must be explicit.
- **Escalation Path**: Escalate when blast radius exceeds current responder authority.

## Invocation

### Example 1: Elevated API Error Rate

**Input**:
```json
{
  "incident_signal": "Alert: 5xx rate above 7% for api-gateway",
  "impacted_services": [
    "api-gateway",
    "payments-api"
  ],
  "customer_impact": "Checkout intermittently failing for US users",
  "error_budget_state": "80% budget burned this week",
  "known_dependencies": [
    "database-primary",
    "feature-flag-service"
  ],
  "oncall_roster": [
    "sre-oncall",
    "payments-oncall",
    "support-manager"
  ]
}
```

**Output**:
```json
{
  "incident_triage": {
    "severity": "SEV-1",
    "initial_actions": [
      "Trigger SEV-1 bridge",
      "Rollback latest deploy"
    ]
  },
  "triage_status": "active"
}
```

### Example 2: Background Job Delay

**Input**:
```json
{
  "incident_signal": "Queue lag warning on nightly reporting jobs",
  "impacted_services": [
    "reporting-worker"
  ],
  "customer_impact": "Reports delayed by up to 45 minutes; no data loss",
  "error_budget_state": "within budget",
  "known_dependencies": [
    "warehouse read replica"
  ],
  "oncall_roster": [
    "data-platform-oncall"
  ]
}
```

**Output**:
```json
{
  "incident_triage": {
    "severity": "SEV-3",
    "classification_rationale": [
      "Degraded internal function",
      "No immediate customer outage"
    ]
  },
  "triage_status": "monitoring"
}
```
