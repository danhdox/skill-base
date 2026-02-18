# Financial Model Sanity Check

## Purpose

This skill audits financial models for formula integrity, assumption consistency, and scenario coherence before decisions are made from model outputs.

## Inputs

| Name | Type | Required | Description | Constraints |
|------|------|----------|-------------|-------------|
| `model_scope` | string | Yes | What model and decisions are in scope | Non-empty string |
| `assumptions` | array | Yes | Core model assumptions | At least 3 assumptions |
| `revenue_logic` | string | Yes | How revenue is modeled | Non-empty string |
| `cost_logic` | string | Yes | How costs are modeled | Non-empty string |
| `scenario_definitions` | array | No | Base/upside/downside scenarios | Optional |
| `known_model_risks` | array | No | Known weak spots or unresolved issues | Optional |

## Output Format

```json
{
  "financial_model_sanity_check": {
    "overall_assessment": "requires_revision",
    "formula_integrity": {
      "status": "warning",
      "issues": [
        "Hard-coded value in gross margin calc"
      ]
    },
    "assumption_consistency": {
      "status": "warning",
      "issues": [
        "Churn assumption differs between revenue sheet and cohort sheet"
      ]
    },
    "scenario_coherence": {
      "status": "pass",
      "issues": []
    },
    "priority_fixes": [
      {
        "id": "FM-07",
        "owner": "finance-ops",
        "deadline": "2026-02-24",
        "description": "Remove hard-coded constants"
      }
    ]
  },
  "decision_readiness": "not_ready"
}
```

## Constraints

- **Model Access**: Review quality depends on access to formulas and assumptions, not outputs only.
- **Version Control**: Untracked edits can invalidate findings quickly.
- **Cross-Sheet Drift**: Large models often diverge across linked tabs without strict controls.
- **Scenario Discipline**: Scenario labels must correspond to actual parameter changes.
- **Decision Risk**: High-impact decisions should not proceed with unresolved high-severity model issues.

## Invocation

### Example 1: Annual Budget Model QA

**Input**:
```json
{
  "model_scope": "FY2027 operating plan",
  "assumptions": [
    "Net revenue retention 112%",
    "Hiring plan 38 net adds",
    "Cloud COGS +9%"
  ],
  "revenue_logic": "ARR cohort expansion + new bookings waterfall",
  "cost_logic": "Department budget roll-up with headcount driver",
  "scenario_definitions": [
    "base",
    "stretch",
    "downside"
  ],
  "known_model_risks": [
    "Sales ramp assumptions from old cohort data"
  ]
}
```

**Output**:
```json
{
  "financial_model_sanity_check": {
    "overall_assessment": "conditional",
    "priority_fixes": [
      {
        "id": "FM-10",
        "description": "Refresh sales ramp assumptions from 2026 cohorts"
      }
    ]
  },
  "decision_readiness": "ready_after_fixes"
}
```

### Example 2: Fundraising Scenario Model Review

**Input**:
```json
{
  "model_scope": "18-month fundraising runway model",
  "assumptions": [
    "Raise closes in month 5",
    "Gross margin improves to 78%",
    "Churn steady at 1.9%"
  ],
  "revenue_logic": "Top-down pipeline conversion assumptions",
  "cost_logic": "Function-level spend with staged hiring",
  "scenario_definitions": [
    "on-time raise",
    "delayed raise",
    "no raise"
  ],
  "known_model_risks": [
    "No sensitivity for delayed enterprise launches"
  ]
}
```

**Output**:
```json
{
  "financial_model_sanity_check": {
    "formula_integrity": {
      "status": "pass"
    },
    "assumption_consistency": {
      "status": "warning"
    }
  },
  "decision_readiness": "requires_executive_review"
}
```
