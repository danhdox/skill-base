# SLO Planning

## Purpose

This skill defines practical SLOs and error budgets tied to user journeys and operational response capacity.

## Inputs

| Name | Type | Required | Description | Constraints |
|------|------|----------|-------------|-------------|
| `service_name` | string | Yes | Service or product surface | Non-empty string |
| `critical_user_journeys` | array | Yes | Journeys to protect | At least 1 journey |
| `historical_performance` | object | Yes | Recent latency/availability data | Include at least one month of data when possible |
| `business_tolerance` | string | Yes | Acceptable failure impact | Non-empty string |
| `oncall_capacity` | string | No | Responder capacity and coverage | Optional |
| `release_cadence` | string | No | Deployment frequency | Optional |

## Output Format

```json
{
  "slo_plan": {
    "slis": [
      {
        "name": "request_success_rate",
        "definition": "2xx/3xx responses over total valid requests"
      },
      {
        "name": "p95_latency",
        "definition": "95th percentile request latency"
      }
    ],
    "slos": [
      {
        "name": "availability",
        "target": "99.9% per 30 days"
      },
      {
        "name": "latency",
        "target": "p95 < 300ms"
      }
    ],
    "error_budget_policy": {
      "burn_alerts": [
        "2% in 1h",
        "10% in 6h"
      ],
      "actions": [
        "Freeze risky deploys",
        "Escalate to incident review"
      ]
    },
    "review_cadence": "monthly"
  },
  "adoption_readiness": "ready"
}
```

## Constraints

- **Journey Alignment**: SLOs should map to user-critical journeys, not only system internals.
- **Data Quality**: SLI definitions require reliable telemetry and denominator rules.
- **Operability**: Alert thresholds should be actionable for on-call responders.
- **Budget Policy**: Error budget policies must define concrete operational actions.
- **Recalibration**: SLO targets should be reviewed when product usage or reliability profile shifts.

## Invocation

### Example 1: API Platform SLO Set

**Input**:
```json
{
  "service_name": "public-api",
  "critical_user_journeys": [
    "create resource",
    "list resources",
    "webhook delivery"
  ],
  "historical_performance": {
    "availability_30d": 99.82,
    "p95_latency_ms": 340
  },
  "business_tolerance": "Partial degradation acceptable, sustained failures are not",
  "oncall_capacity": "24/7 SRE primary + product engineer secondary",
  "release_cadence": "daily"
}
```

**Output**:
```json
{
  "slo_plan": {
    "slos": [
      {
        "name": "availability",
        "target": "99.9%"
      },
      {
        "name": "latency",
        "target": "p95 < 300ms"
      }
    ]
  },
  "adoption_readiness": "ready_after_dashboard_cleanup"
}
```

### Example 2: Internal Reporting Service

**Input**:
```json
{
  "service_name": "reporting-jobs",
  "critical_user_journeys": [
    "daily report generation",
    "monthly finance export"
  ],
  "historical_performance": {
    "success_rate": 98.7,
    "median_runtime_minutes": 14
  },
  "business_tolerance": "Daily reports can be delayed up to 30 minutes",
  "oncall_capacity": "business-hours only",
  "release_cadence": "weekly"
}
```

**Output**:
```json
{
  "slo_plan": {
    "slos": [
      {
        "name": "job_success_rate",
        "target": "99.2%"
      }
    ],
    "error_budget_policy": {
      "actions": [
        "Defer non-critical releases after high burn"
      ]
    }
  },
  "adoption_readiness": "needs_alerting_coverage"
}
```
