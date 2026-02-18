# Unit Economics Analysis

## Purpose

This skill analyzes unit economics to quantify contribution margin, payback dynamics, and growth sustainability by customer segment.

## Inputs

| Name | Type | Required | Description | Constraints |
|------|------|----------|-------------|-------------|
| `product_line` | string | Yes | Product or segment under analysis | Non-empty string |
| `average_revenue_per_unit` | number | Yes | Revenue per account/user/order | Must be >= 0 |
| `variable_cost_components` | object | Yes | Variable costs tied to each unit | Include key cost categories |
| `acquisition_cost` | number | Yes | Customer acquisition cost | Must be >= 0 |
| `retention_profile` | object | No | Retention/churn assumptions | Optional but recommended |
| `support_and_servicing_cost` | number | No | Support cost allocation per unit | Must be >= 0 |

## Output Format

```json
{
  "unit_economics": {
    "contribution_margin": 0.63,
    "gross_margin": 0.78,
    "cac_payback_months": 11.2,
    "ltv_to_cac": 3.4,
    "sensitivity": [
      {
        "driver": "churn +2pp",
        "ltv_to_cac": 2.7
      },
      {
        "driver": "hosting cost +15%",
        "contribution_margin": 0.58
      }
    ],
    "recommendations": [
      "Improve onboarding activation to reduce early churn"
    ]
  },
  "decision_support": "viable_with_margin_improvements"
}
```

## Constraints

- **Allocation Discipline**: Cost allocations must be consistent across segments.
- **Cohort Sensitivity**: LTV assumptions should reflect cohort-level retention differences.
- **Growth Stage Effects**: Early-stage CAC volatility can distort conclusions.
- **Time Horizon**: Short observation windows can understate true payback risk.
- **Scenario Testing**: Recommendations should account for plausible downside conditions.

## Invocation

### Example 1: Mid-Market SaaS Segment

**Input**:
```json
{
  "product_line": "Mid-market SaaS",
  "average_revenue_per_unit": 420,
  "variable_cost_components": {
    "hosting": 58,
    "payment_fees": 9,
    "support": 34
  },
  "acquisition_cost": 3100,
  "retention_profile": {
    "monthly_logo_churn": 0.018
  },
  "support_and_servicing_cost": 34
}
```

**Output**:
```json
{
  "unit_economics": {
    "cac_payback_months": 9.6,
    "ltv_to_cac": 4.1
  },
  "decision_support": "healthy"
}
```

### Example 2: Self-Serve SMB Segment

**Input**:
```json
{
  "product_line": "SMB self-serve",
  "average_revenue_per_unit": 48,
  "variable_cost_components": {
    "hosting": 8,
    "payment_fees": 2.4,
    "support": 6.5
  },
  "acquisition_cost": 170,
  "retention_profile": {
    "monthly_logo_churn": 0.062
  },
  "support_and_servicing_cost": 6.5
}
```

**Output**:
```json
{
  "unit_economics": {
    "cac_payback_months": 7.4,
    "ltv_to_cac": 2.2,
    "recommendations": [
      "Improve early retention before scaling paid acquisition"
    ]
  },
  "decision_support": "borderline"
}
```
