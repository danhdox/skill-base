# Go-to-Market Plan

## Purpose

This skill produces a launch-ready GTM plan covering audience targeting, channel strategy, messaging, timeline, and success metrics.

## Inputs

| Name | Type | Required | Description | Constraints |
|------|------|----------|-------------|-------------|
| `product_name` | string | Yes | Product or feature being launched | Non-empty string |
| `target_segments` | array | Yes | Customer segments to target | At least 1 segment |
| `value_proposition` | string | Yes | Core promise to customers | Non-empty string |
| `launch_window` | string | Yes | Planned launch timeframe | Non-empty string |
| `channels` | array | No | Distribution and acquisition channels | Optional but recommended |
| `budget_usd` | number | No | Campaign and launch budget | Must be >= 0 |
| `regional_constraints` | array | No | Compliance or operational limits by region | Optional |

## Output Format

```json
{
  "gtm_plan": {
    "positioning": {
      "primary_message": "Fastest path from setup to measurable value",
      "proof_points": [
        "2-day onboarding",
        "SOC2 and SSO ready"
      ]
    },
    "channel_plan": [
      {
        "channel": "product-led",
        "objective": "activation",
        "owner": "growth-pm"
      },
      {
        "channel": "partner",
        "objective": "pipeline",
        "owner": "alliances"
      }
    ],
    "launch_milestones": [
      {
        "name": "beta",
        "date": "2026-04-01"
      },
      {
        "name": "general-availability",
        "date": "2026-05-15"
      }
    ],
    "success_metrics": [
      "trial_to_paid",
      "CAC_payback_months",
      "activation_rate"
    ],
    "risk_register": [
      "Message confusion between SMB and enterprise segments"
    ]
  },
  "execution_status": "draft_ready_for_review"
}
```

## Constraints

- **Segment Clarity**: Plans without explicit target segments should be marked incomplete.
- **Channel Capacity**: Channel recommendations must respect team execution bandwidth.
- **Positioning Consistency**: Messaging should align with actual product capabilities at launch.
- **Metric Ownership**: Every core KPI should have a named owner.
- **Regional Readiness**: Geo expansion assumptions require legal and operational confirmation.

## Invocation

### Example 1: New Analytics Module Launch

**Input**:
```json
{
  "product_name": "Insights Hub",
  "target_segments": [
    "mid-market SaaS",
    "enterprise operations"
  ],
  "value_proposition": "Reduce reporting cycle from days to minutes",
  "launch_window": "Q2 2026",
  "channels": [
    "in-product upsell",
    "lifecycle email",
    "sales enablement"
  ],
  "budget_usd": 120000,
  "regional_constraints": [
    "EU data residency messaging required"
  ]
}
```

**Output**:
```json
{
  "gtm_plan": {
    "success_metrics": [
      "attach_rate",
      "pipeline_influenced",
      "activation_rate"
    ],
    "execution_owner": "growth-director"
  },
  "execution_status": "approved_for_execution"
}
```

### Example 2: Vertical-Specific Packaging Release

**Input**:
```json
{
  "product_name": "Compliance Add-on",
  "target_segments": [
    "healthcare",
    "finserv"
  ],
  "value_proposition": "Audit-ready workflows with minimal setup",
  "launch_window": "August 2026",
  "channels": [
    "partner webinars",
    "ABM campaigns"
  ],
  "budget_usd": 85000,
  "regional_constraints": [
    "HIPAA claims review",
    "state-level disclosures"
  ]
}
```

**Output**:
```json
{
  "gtm_plan": {
    "risk_register": [
      "Partner training lead time may delay pipeline activation"
    ],
    "success_metrics": [
      "SQL_volume",
      "win_rate",
      "sales_cycle_days"
    ]
  },
  "execution_status": "needs_dependency_alignment"
}
```
