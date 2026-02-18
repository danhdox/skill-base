# Protocol Governance Design Review

## Purpose

This skill reviews onchain governance architecture to identify capture risks, operational bottlenecks, and emergency control gaps.

## Inputs

| Name | Type | Required | Description | Constraints |
|------|------|----------|-------------|-------------|
| `governance_model` | string | Yes | Core governance model | Examples: token voting, council, hybrid |
| `proposal_lifecycle` | array | Yes | Proposal stages from draft to execution | At least 3 stages |
| `voting_mechanics` | object | Yes | Quorum, thresholds, and voting periods | Include current parameter values |
| `power_distribution` | object | Yes | Voting power concentration indicators | Include top-holder or delegate concentration |
| `emergency_controls` | string | No | Pause/guardian controls | Optional |
| `operational_capacity` | string | No | Team/community ability to process governance workload | Optional |

## Output Format

```json
{
  "governance_design_review": {
    "health_score": 74,
    "attack_vectors": [
      {
        "severity": "high",
        "vector": "low-turnout proposal capture",
        "mitigation": "raise quorum and extend notice windows"
      }
    ],
    "operational_gaps": [
      "No clear incident override procedure",
      "Voter education is inconsistent"
    ],
    "parameter_recommendations": [
      "Increase proposal delay from 24h to 48h"
    ],
    "readiness": "needs_hardening"
  },
  "follow_up_actions": [
    "Run governance game day",
    "Publish delegate accountability rubric"
  ]
}
```

## Constraints

- **Participation Uncertainty**: Governance assumptions may fail when voter turnout shifts.
- **Operational Reality**: Protocol ops capacity must match governance cadence.
- **Emergency Tradeoffs**: Faster emergency controls can increase centralization risk.
- **Parameter Coupling**: Quorum/threshold/timelock settings should be evaluated together.
- **Execution Risk**: Governance decisions are only as reliable as execution safeguards.

## Invocation

### Example 1: DAO Governance v2 Review

**Input**:
```json
{
  "governance_model": "token voting + elected security council",
  "proposal_lifecycle": [
    "forum discussion",
    "snapshot temperature check",
    "onchain vote",
    "timelock execution"
  ],
  "voting_mechanics": {
    "quorum": "8%",
    "pass_threshold": "55%",
    "voting_period_days": 5
  },
  "power_distribution": {
    "top_20_holders": "46%",
    "active_delegates": 32
  },
  "emergency_controls": "3/5 security council pause",
  "operational_capacity": "core team supports 6 major proposals per quarter"
}
```

**Output**:
```json
{
  "governance_design_review": {
    "health_score": 79,
    "parameter_recommendations": [
      "Introduce proposer bond for spam mitigation"
    ]
  },
  "follow_up_actions": [
    "Pilot delegate scorecards"
  ]
}
```

### Example 2: Early-Stage Protocol Governance Setup

**Input**:
```json
{
  "governance_model": "founder multisig transitioning to token governance",
  "proposal_lifecycle": [
    "multisig proposal",
    "community comment",
    "execution"
  ],
  "voting_mechanics": {
    "quorum": "n/a",
    "pass_threshold": "3/5 signers",
    "voting_period_days": 0
  },
  "power_distribution": {
    "multisig_members": 5
  },
  "emergency_controls": "same multisig can pause core contracts",
  "operational_capacity": "limited governance ops"
}
```

**Output**:
```json
{
  "governance_design_review": {
    "health_score": 52,
    "attack_vectors": [
      {
        "severity": "high",
        "vector": "key compromise risk in concentrated signer set"
      }
    ],
    "readiness": "not_ready_for_decentralized_governance_claims"
  },
  "follow_up_actions": [
    "Publish decentralization roadmap with milestone gates"
  ]
}
```
