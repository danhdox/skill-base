# Cash Flow Forecast Scenarios

## Purpose

This skill produces base, upside, and downside cash-flow scenarios to support runway planning and risk-aware operating decisions.

## Inputs

| Name | Type | Required | Description | Constraints |
|------|------|----------|-------------|-------------|
| `opening_cash` | number | Yes | Starting cash balance | Must be >= 0 |
| `monthly_revenue_projection` | array | Yes | Projected monthly inflows | At least 3 months |
| `monthly_expense_projection` | array | Yes | Projected monthly outflows | At least 3 months |
| `financing_events` | array | No | Expected financing or debt events | Optional |
| `scenario_assumptions` | object | Yes | Assumptions for base/best/worst cases | Must include at least base and downside |
| `forecast_horizon_months` | number | No | Forecast duration | Range: 3-36, Default: 12 |

## Output Format

```json
{
  "cash_flow_forecast": {
    "base_case": {
      "runway_months": 14,
      "min_cash_balance": 1200000
    },
    "upside_case": {
      "runway_months": 19,
      "min_cash_balance": 2150000
    },
    "downside_case": {
      "runway_months": 9,
      "min_cash_balance": 280000
    },
    "key_drivers": [
      "new ARR conversion",
      "hiring pace",
      "infrastructure spend"
    ],
    "recommended_controls": [
      "Trigger hiring freeze if downside runway < 8 months"
    ]
  },
  "board_packet_ready": true
}
```

## Constraints

- **Projection Uncertainty**: Forecasts are sensitive to pipeline and expense assumptions.
- **Event Timing**: Financing delays can materially shift runway outcomes.
- **Granularity Limits**: Monthly models may hide intra-month liquidity crunches.
- **Scenario Discipline**: Downside scenarios should be plausible, not extreme fantasies.
- **Decision Triggers**: Forecasts are most useful when tied to explicit control actions.

## Invocation

### Example 1: Annual Operating Plan Forecast

**Input**:
```json
{
  "opening_cash": 6400000,
  "monthly_revenue_projection": [
    620000,
    650000,
    690000,
    730000
  ],
  "monthly_expense_projection": [
    980000,
    1020000,
    1050000,
    1080000
  ],
  "financing_events": [
    {
      "month": 8,
      "amount": 4000000,
      "type": "equity"
    }
  ],
  "scenario_assumptions": {
    "base": "pipeline conversion at historical average",
    "upside": "enterprise deal closes one quarter early",
    "downside": "hiring costs exceed plan by 12%"
  },
  "forecast_horizon_months": 12
}
```

**Output**:
```json
{
  "cash_flow_forecast": {
    "base_case": {
      "runway_months": 13
    },
    "downside_case": {
      "runway_months": 8
    }
  },
  "board_packet_ready": true
}
```

### Example 2: Cost Containment Scenario

**Input**:
```json
{
  "opening_cash": 2200000,
  "monthly_revenue_projection": [
    210000,
    225000,
    240000,
    255000
  ],
  "monthly_expense_projection": [
    390000,
    395000,
    405000,
    420000
  ],
  "financing_events": [],
  "scenario_assumptions": {
    "base": "planned spend profile",
    "upside": "vendor renegotiation reduces COGS",
    "downside": "renewal churn increases by 5%"
  },
  "forecast_horizon_months": 9
}
```

**Output**:
```json
{
  "cash_flow_forecast": {
    "recommended_controls": [
      "Reduce discretionary spend by 10% in month 2"
    ],
    "downside_case": {
      "runway_months": 5
    }
  },
  "board_packet_ready": false
}
```
