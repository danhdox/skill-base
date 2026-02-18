# Feature Prioritization (RICE)

## Purpose

This skill prioritizes candidate features using a transparent RICE framework so teams can align roadmap decisions with impact and delivery capacity.

## Inputs

| Name | Type | Required | Description | Constraints |
|------|------|----------|-------------|-------------|
| `feature_candidates` | array | Yes | List of features with problem statements | At least 2 items |
| `reach_estimates` | object | Yes | Expected user/business reach per feature | Provide estimate horizon |
| `impact_scores` | object | Yes | Expected impact per feature | Use consistent scoring scale |
| `confidence_scores` | object | Yes | Confidence in assumptions | Range 0-1 or 0-100 |
| `effort_estimates` | object | Yes | Delivery effort estimates | Use shared unit (person-weeks, story points, etc.) |
| `capacity_constraints` | string | No | Current team capacity and constraints | Optional |

## Output Format

```json
{
  "rice_prioritization": {
    "ranked_features": [
      {
        "feature": "Audit log export",
        "rice_score": 412,
        "priority": 1
      },
      {
        "feature": "Bulk role assignment",
        "rice_score": 265,
        "priority": 2
      }
    ],
    "scoring_notes": [
      "Confidence penalty applied to features with unvalidated demand"
    ],
    "cut_line": "Top 3 features fit quarter capacity",
    "tradeoffs": [
      "Higher strategic feature deferred due to high delivery effort"
    ]
  },
  "decision_log": "RICE inputs and assumptions archived for roadmap review"
}
```

## Constraints

- **Comparable Inputs**: RICE scores are only meaningful when inputs use the same scales and horizon.
- **Confidence Honesty**: Low-confidence estimates should materially reduce rank.
- **Capacity Fit**: Prioritization must account for real delivery bandwidth.
- **Strategic Overlay**: RICE informs decisions but does not replace strategic constraints.
- **Review Cadence**: Recompute scores when major assumptions change.

## Invocation

### Example 1: Q3 Platform Roadmap Prioritization

**Input**:
```json
{
  "feature_candidates": [
    "Audit log export",
    "Custom roles",
    "API token rotation UX"
  ],
  "reach_estimates": {
    "Audit log export": 1800,
    "Custom roles": 950,
    "API token rotation UX": 2200
  },
  "impact_scores": {
    "Audit log export": 2.5,
    "Custom roles": 3.0,
    "API token rotation UX": 1.8
  },
  "confidence_scores": {
    "Audit log export": 0.85,
    "Custom roles": 0.6,
    "API token rotation UX": 0.9
  },
  "effort_estimates": {
    "Audit log export": 8,
    "Custom roles": 14,
    "API token rotation UX": 5
  },
  "capacity_constraints": "20 engineer-weeks available"
}
```

**Output**:
```json
{
  "rice_prioritization": {
    "ranked_features": [
      {
        "feature": "API token rotation UX",
        "rice_score": 712,
        "priority": 1
      },
      {
        "feature": "Audit log export",
        "rice_score": 478,
        "priority": 2
      }
    ],
    "cut_line": "Top 2 ship in quarter"
  },
  "decision_log": "Accepted in roadmap review 2026-02-18"
}
```

### Example 2: Expansion Pack Feature Batch

**Input**:
```json
{
  "feature_candidates": [
    "Multi-region failover",
    "Advanced dashboard filters",
    "SCIM group sync"
  ],
  "reach_estimates": {
    "Multi-region failover": 300,
    "Advanced dashboard filters": 1600,
    "SCIM group sync": 700
  },
  "impact_scores": {
    "Multi-region failover": 3.2,
    "Advanced dashboard filters": 1.6,
    "SCIM group sync": 2.4
  },
  "confidence_scores": {
    "Multi-region failover": 0.55,
    "Advanced dashboard filters": 0.8,
    "SCIM group sync": 0.75
  },
  "effort_estimates": {
    "Multi-region failover": 28,
    "Advanced dashboard filters": 10,
    "SCIM group sync": 12
  },
  "capacity_constraints": "One platform squad and one product squad"
}
```

**Output**:
```json
{
  "rice_prioritization": {
    "tradeoffs": [
      "Multi-region failover deferred pending architecture prep work"
    ],
    "cut_line": "Dashboard filters + SCIM sync selected"
  },
  "decision_log": "Requires infra readiness checkpoint"
}
```
