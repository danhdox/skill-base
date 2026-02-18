# Data Quality Audit

## Purpose

This skill audits a dataset for quality dimensions such as completeness, validity, consistency, uniqueness, and timeliness. It helps teams establish data trust before analytics, experimentation, or model training.

## Inputs

| Name | Type | Required | Description | Constraints |
|------|------|----------|-------------|-------------|
| `dataset_name` | string | Yes | Dataset to audit | Non-empty string |
| `data_source` | string | Yes | Source system or pipeline | Non-empty string |
| `critical_columns` | array | Yes | Columns that cannot fail quality checks | At least 1 column |
| `primary_key_columns` | array | No | Columns expected to be unique | Optional, but recommended |
| `freshness_sla_hours` | number | No | Maximum allowed staleness | Range: 1-720, Default: 24 |
| `sampling_strategy` | string | No | How rows are selected for audit | Valid values: "full", "recent-window", "random-sample", Default: "recent-window" |

## Output Format

```json
{
  "data_quality_audit": {
    "overall_score": 81,
    "dimension_scores": {
      "completeness": 84,
      "validity": 79,
      "consistency": 83,
      "uniqueness": 92,
      "timeliness": 68
    },
    "critical_failures": [
      {
        "column": "customer_email",
        "issue": "invalid format ratio 6.2%",
        "severity": "high"
      }
    ],
    "recommended_remediation": [
      "Add upstream email normalization",
      "Backfill missing timestamps for the last 7 days"
    ]
  },
  "audit_confidence": "high",
  "retest_recommendation": "After pipeline fixes are deployed"
}
```

## Constraints

- **Sampling Impact**: Partial sampling may miss rare edge-case anomalies.
- **Business Rule Dependency**: Validity checks must align with documented domain rules.
- **Schema Drift**: Changing schemas can invalidate historical quality comparisons.
- **Critical Column Priority**: Critical failures should block downstream usage until mitigated.
- **Timeliness Context**: Freshness thresholds must match actual business cadence.

## Invocation

### Example 1: Customer 360 Daily Snapshot

**Input**:
```json
{
  "dataset_name": "customer_360_daily",
  "data_source": "warehouse.analytics.customer_360",
  "critical_columns": [
    "customer_id",
    "email",
    "lifecycle_stage"
  ],
  "primary_key_columns": [
    "customer_id"
  ],
  "freshness_sla_hours": 24,
  "sampling_strategy": "recent-window"
}
```

**Output**:
```json
{
  "data_quality_audit": {
    "overall_score": 86,
    "critical_failures": [],
    "recommended_remediation": [
      "Tighten lifecycle_stage enum validation"
    ]
  },
  "audit_confidence": "high",
  "retest_recommendation": "Weekly"
}
```

### Example 2: Event Stream Ingestion Table

**Input**:
```json
{
  "dataset_name": "events_raw",
  "data_source": "kafka -> lakehouse bronze",
  "critical_columns": [
    "event_id",
    "event_timestamp",
    "event_name"
  ],
  "primary_key_columns": [
    "event_id"
  ],
  "freshness_sla_hours": 2,
  "sampling_strategy": "full"
}
```

**Output**:
```json
{
  "data_quality_audit": {
    "overall_score": 69,
    "critical_failures": [
      {
        "column": "event_timestamp",
        "issue": "future timestamps 3.1%",
        "severity": "high"
      }
    ],
    "recommended_remediation": [
      "Reject malformed event_timestamp at ingestion gateway"
    ]
  },
  "audit_confidence": "medium",
  "retest_recommendation": "After ingestion parser patch"
}
```
