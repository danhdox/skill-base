# Runbook Creation

## Purpose

This skill converts operational response knowledge into clear runbooks with prerequisites, diagnostics, remediation steps, and escalation criteria.

## Inputs

| Name | Type | Required | Description | Constraints |
|------|------|----------|-------------|-------------|
| `service_name` | string | Yes | Service/system covered by the runbook | Non-empty string |
| `trigger_conditions` | array | Yes | Conditions that should trigger runbook use | At least 1 trigger |
| `prerequisites` | array | Yes | Access/tools required | At least 1 prerequisite |
| `diagnostic_signals` | array | Yes | Logs/metrics/traces to inspect | At least 1 signal |
| `remediation_options` | array | Yes | Potential mitigation actions | At least 1 option |
| `escalation_policy` | string | No | When and to whom to escalate | Optional |

## Output Format

```json
{
  "runbook": {
    "title": "Service Incident Response Runbook",
    "entry_criteria": [
      "Alert threshold crossed",
      "Customer report confirms impact"
    ],
    "diagnostic_steps": [
      "Check dashboard X",
      "Validate dependency Y",
      "Review deploy history"
    ],
    "remediation_playbooks": [
      {
        "scenario": "dependency_timeout",
        "steps": [
          "Fail over",
          "reduce traffic",
          "notify stakeholders"
        ]
      }
    ],
    "rollback_criteria": [
      "Error rate remains >2% after mitigation"
    ],
    "escalation_triggers": [
      "No improvement after 20 minutes"
    ]
  },
  "maintenance_plan": "Review quarterly and after incidents"
}
```

## Constraints

- **Operator Clarity**: Runbooks must be executable by on-call responders under stress.
- **Step Verifiability**: Each action should include observable success/failure indicators.
- **Environment Accuracy**: Commands/procedures must match current infrastructure.
- **Escalation Safety**: High-risk actions should include approval/escalation checkpoints.
- **Revision Cadence**: Runbooks should be updated after incidents and architecture changes.

## Invocation

### Example 1: API Gateway Latency Runbook

**Input**:
```json
{
  "service_name": "api-gateway",
  "trigger_conditions": [
    "p95 latency > 600ms for 10 min",
    "error rate > 2%"
  ],
  "prerequisites": [
    "prod dashboard access",
    "kubectl access",
    "pager role"
  ],
  "diagnostic_signals": [
    "gateway latency dashboard",
    "upstream timeout logs"
  ],
  "remediation_options": [
    "rollback latest release",
    "shift traffic to healthy region"
  ],
  "escalation_policy": "Escalate to platform lead if unresolved after 20 minutes"
}
```

**Output**:
```json
{
  "runbook": {
    "entry_criteria": [
      "SEV-2 latency threshold crossed"
    ],
    "escalation_triggers": [
      "Mitigation fails twice"
    ]
  },
  "maintenance_plan": "Drill monthly"
}
```

### Example 2: Batch Processing Failure Runbook

**Input**:
```json
{
  "service_name": "billing-batch-worker",
  "trigger_conditions": [
    "Job failure count > 3",
    "queue lag > 30 min"
  ],
  "prerequisites": [
    "job scheduler access",
    "warehouse query permissions"
  ],
  "diagnostic_signals": [
    "job logs",
    "queue backlog metrics"
  ],
  "remediation_options": [
    "retry failed partition",
    "backfill from checkpoint"
  ],
  "escalation_policy": "Escalate to finance ops if invoice SLA risk exceeds 4 hours"
}
```

**Output**:
```json
{
  "runbook": {
    "remediation_playbooks": [
      {
        "scenario": "partition_corruption",
        "steps": [
          "stop consumer",
          "rebuild partition",
          "resume with monitor"
        ]
      }
    ]
  },
  "maintenance_plan": "Update after each month-end incident"
}
```
