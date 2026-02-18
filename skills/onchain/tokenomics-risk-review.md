# Tokenomics Risk Review

## Purpose

This skill evaluates token incentive systems for sustainability, attack resistance, and governance alignment before launch or major parameter updates.

## Inputs

| Name | Type | Required | Description | Constraints |
|------|------|----------|-------------|-------------|
| `token_supply_model` | string | Yes | Fixed, inflationary, or dynamic supply model | Non-empty string |
| `emission_schedule` | string | Yes | How and when tokens are emitted | Include vesting/unlock assumptions |
| `utility_definition` | array | Yes | Primary token utilities | At least 1 utility |
| `holder_distribution` | object | Yes | Initial and projected ownership distribution | Include team, investors, community |
| `staking_and_rewards` | string | No | Staking mechanics and reward source | Optional |
| `governance_rights` | string | No | Voting/governance privileges tied to token | Optional |

## Output Format

```json
{
  "tokenomics_risk_review": {
    "overall_risk_level": "high",
    "risk_dimensions": {
      "inflation_pressure": "high",
      "concentration_risk": "medium",
      "incentive_misalignment": "high",
      "governance_capture": "medium"
    },
    "critical_findings": [
      {
        "issue": "Large unlock cliff near month 12",
        "impact": "Sell pressure may destabilize protocol usage incentives",
        "recommendation": "Smooth unlock curve and increase utility sinks"
      }
    ],
    "stress_scenarios": [
      "50% TVL decline",
      "token price drawdown >60%"
    ],
    "go_live_recommendation": "delay_until_high_findings_closed"
  },
  "confidence": "medium"
}
```

## Constraints

- **Market Sensitivity**: Token behavior depends on external market conditions not controlled by the protocol.
- **Simulation Limits**: Simplified models may underrepresent adversarial behavior.
- **Governance Dynamics**: Holder coordination assumptions can be wrong in volatile markets.
- **Data Freshness**: Outdated wallet/distribution data weakens concentration analysis.
- **Regulatory Overlay**: Token design decisions may have legal implications requiring counsel.

## Invocation

### Example 1: New DeFi Governance Token

**Input**:
```json
{
  "token_supply_model": "inflationary with capped tail emissions",
  "emission_schedule": "High bootstrap emissions for first 18 months",
  "utility_definition": [
    "governance voting",
    "fee rebates",
    "staking rewards"
  ],
  "holder_distribution": {
    "team": 0.2,
    "investors": 0.25,
    "community": 0.55
  },
  "staking_and_rewards": "Rewards sourced from emissions + protocol fees",
  "governance_rights": "Token-weighted quorum voting"
}
```

**Output**:
```json
{
  "tokenomics_risk_review": {
    "overall_risk_level": "medium",
    "critical_findings": [
      {
        "issue": "Investor unlock overlaps incentive drop",
        "recommendation": "Introduce staggered unlock and fee-share ramp"
      }
    ]
  },
  "confidence": "medium"
}
```

### Example 2: Parameter Update for Existing Token

**Input**:
```json
{
  "token_supply_model": "fixed supply",
  "emission_schedule": "No new emissions; rewards from treasury",
  "utility_definition": [
    "staking",
    "protocol fee discounts"
  ],
  "holder_distribution": {
    "top_10_wallets": 0.41,
    "active_delegates": 27
  },
  "staking_and_rewards": "Treasury-funded APR 8%",
  "governance_rights": "Delegated voting with proposal threshold"
}
```

**Output**:
```json
{
  "tokenomics_risk_review": {
    "overall_risk_level": "high",
    "critical_findings": [
      {
        "issue": "Treasury-funded APR unsustainable under low fee regime",
        "recommendation": "Tie rewards to protocol revenue floor"
      }
    ]
  },
  "confidence": "high"
}
```
