# Experiment Design and Power Analysis

## Purpose

This skill designs controlled experiments and calculates sample size/power so teams can make statistically reliable product and growth decisions.

## Inputs

| Name | Type | Required | Description | Constraints |
|------|------|----------|-------------|-------------|
| `hypothesis` | string | Yes | Experiment hypothesis | Non-empty string |
| `primary_metric` | string | Yes | Primary success metric | Non-empty string |
| `baseline_value` | number | Yes | Current baseline metric value | Must be >= 0 |
| `minimum_detectable_effect` | number | Yes | Smallest meaningful lift/drop to detect | Express as decimal (e.g., 0.03 for 3%) |
| `alpha` | number | No | Type I error rate | Default: 0.05 |
| `power` | number | No | Desired statistical power | Default: 0.8 |
| `expected_daily_traffic` | number | No | Eligible daily sample volume | Must be > 0 |

## Output Format

```json
{
  "experiment_design": {
    "recommended_test_type": "A/B",
    "sample_size_per_variant": 18450,
    "estimated_runtime_days": 14,
    "randomization_unit": "user_id",
    "guardrail_metrics": [
      "error_rate",
      "latency_p95"
    ],
    "analysis_plan": "Two-sided z-test with CUPED adjustment"
  },
  "power_analysis": {
    "assumptions": [
      "independent samples",
      "stable traffic mix"
    ],
    "sensitivity_table": [
      {
        "mde": 0.02,
        "sample_size_per_variant": 41000
      },
      {
        "mde": 0.03,
        "sample_size_per_variant": 18450
      }
    ],
    "confidence": "high"
  }
}
```

## Constraints

- **Metric Integrity**: Metric definitions must be stable for the full experiment window.
- **Interference Risk**: Network effects or spillover can invalidate independence assumptions.
- **Traffic Reality**: Runtime estimates depend on accurate eligible traffic forecasts.
- **Sequential Peeking**: Repeated significance checks inflate false-positive risk unless corrected.
- **Operational Guardrails**: Safety metrics must be monitored continuously during the run.

## Invocation

### Example 1: Checkout Conversion Uplift Test

**Input**:
```json
{
  "hypothesis": "Reducing checkout steps increases completed purchases",
  "primary_metric": "checkout_conversion_rate",
  "baseline_value": 0.214,
  "minimum_detectable_effect": 0.025,
  "alpha": 0.05,
  "power": 0.8,
  "expected_daily_traffic": 5200
}
```

**Output**:
```json
{
  "experiment_design": {
    "recommended_test_type": "A/B",
    "sample_size_per_variant": 22500,
    "estimated_runtime_days": 9,
    "randomization_unit": "session_id"
  },
  "power_analysis": {
    "confidence": "high"
  }
}
```

### Example 2: Email Subject Line CTR Test

**Input**:
```json
{
  "hypothesis": "Personalized subject lines improve open rate",
  "primary_metric": "email_open_rate",
  "baseline_value": 0.34,
  "minimum_detectable_effect": 0.015,
  "alpha": 0.05,
  "power": 0.9,
  "expected_daily_traffic": 18000
}
```

**Output**:
```json
{
  "experiment_design": {
    "recommended_test_type": "A/B/n",
    "sample_size_per_variant": 30500,
    "estimated_runtime_days": 6,
    "randomization_unit": "recipient_id"
  },
  "power_analysis": {
    "confidence": "medium"
  }
}
```
