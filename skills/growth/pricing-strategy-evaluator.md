# Pricing Strategy Evaluator

## Purpose

This skill evaluates pricing and packaging options against willingness-to-pay signals, competitive context, and revenue objectives.

## Inputs

| Name | Type | Required | Description | Constraints |
|------|------|----------|-------------|-------------|
| `product_name` | string | Yes | Offering being priced | Non-empty string |
| `pricing_models` | array | Yes | Candidate pricing models | At least 2 models |
| `customer_segments` | array | Yes | Segments and buying motions | At least 1 segment |
| `competitor_benchmarks` | array | No | Comparable competitor plans and price points | Optional |
| `cost_structure` | object | No | Key cost drivers | Include variable cost assumptions when possible |
| `revenue_targets` | object | No | ARR/retention targets | Optional |
| `pricing_constraints` | array | No | Business or legal limits | Optional |

## Output Format

```json
{
  "pricing_evaluation": {
    "recommended_model": "hybrid_subscription_plus_usage",
    "rationale": [
      "Aligns revenue with customer value realization",
      "Protects gross margin at higher usage tiers"
    ],
    "packaging_recommendations": [
      {
        "tier": "starter",
        "positioning": "self-serve",
        "guardrail": "feature limits"
      },
      {
        "tier": "enterprise",
        "positioning": "security and governance",
        "guardrail": "annual commitment"
      }
    ],
    "sensitivity_analysis": {
      "price_increase_10pct_retention_delta": -0.02,
      "discount_ceiling_recommendation": 0.15
    },
    "experiments": [
      "decoy-tier test",
      "annual prepay discount test"
    ]
  },
  "decision_confidence": "medium"
}
```

## Constraints

- **Signal Quality**: Recommendations are weaker without recent customer willingness-to-pay data.
- **Cost Visibility**: Missing unit cost data can hide margin risk.
- **Segment Differences**: SMB and enterprise pricing logic should not be conflated.
- **Legal Boundaries**: Regional pricing practices must comply with local requirements.
- **Experimentation Need**: Significant pricing changes should be validated with controlled tests.

## Invocation

### Example 1: Transition From Flat Seat Pricing

**Input**:
```json
{
  "product_name": "Workflow Cloud",
  "pricing_models": [
    "flat_per_seat",
    "usage_based",
    "hybrid"
  ],
  "customer_segments": [
    "SMB",
    "mid-market"
  ],
  "competitor_benchmarks": [
    "Competitor A: $39/seat",
    "Competitor B: usage tiered"
  ],
  "cost_structure": {
    "hosting_per_active_org": 12.5,
    "support_per_org": 7.2
  },
  "revenue_targets": {
    "net_new_arr": 3000000,
    "gross_margin_target": 0.78
  },
  "pricing_constraints": [
    "No invoice shock for existing annual contracts"
  ]
}
```

**Output**:
```json
{
  "pricing_evaluation": {
    "recommended_model": "hybrid",
    "experiments": [
      "grandfathered-seat migration cohort"
    ]
  },
  "decision_confidence": "medium"
}
```

### Example 2: New Enterprise Tier Design

**Input**:
```json
{
  "product_name": "Workflow Cloud",
  "pricing_models": [
    "tiered_subscription",
    "contracted_usage"
  ],
  "customer_segments": [
    "enterprise"
  ],
  "competitor_benchmarks": [
    "Competitor C enterprise starts at $60k ARR"
  ],
  "cost_structure": {
    "implementation_hours": 120,
    "support_sla_cost": 9000
  },
  "revenue_targets": {
    "enterprise_arr": 8500000
  },
  "pricing_constraints": [
    "Must include procurement-friendly fixed fee option"
  ]
}
```

**Output**:
```json
{
  "pricing_evaluation": {
    "recommended_model": "tiered_subscription",
    "packaging_recommendations": [
      {
        "tier": "enterprise-plus",
        "positioning": "compliance and dedicated support"
      }
    ]
  },
  "decision_confidence": "high"
}
```
