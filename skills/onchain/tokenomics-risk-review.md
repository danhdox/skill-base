# Tokenomics Risk Review

## Purpose

This skill provides a structured framework for assessing incentive design, supply mechanics, and governance attack vectors in token systems. It encodes practical decision criteria, standard review checkpoints, and output conventions so teams can execute consistently across different AI agents and operators. The goal is to produce an actionable artifact that can be reused in downstream planning and execution.

## Inputs

| Name | Type | Required | Description | Constraints |
|------|------|----------|-------------|-------------|
| `objective` | string | Yes | What decision or outcome this run should support | Non-empty string, max 250 chars |
| `scope` | string | Yes | System, project, or workflow boundaries for analysis | Non-empty string |
| `context` | string | No | Additional business or technical context | Max 2000 chars |
| `constraints` | array | No | Hard constraints that recommendations must respect | Each item non-empty string |
| `analysis_depth` | string | No | Depth of analysis to perform | Valid values: "quick", "standard", "comprehensive", Default: "standard" |
| `time_horizon` | string | No | Relevant time horizon for recommendations | Valid values: "immediate", "quarter", "year", Default: "quarter" |

## Output Format

```json
{
  "tokenomics_risk_review": {
    "artifact_type": "tokenomics_risk_report",
    "overall_status": "needs_revision",
    "executive_summary": "Concise summary of current state and recommended direction.",
    "confidence": "medium",
    "priority_actions": [
      {
        "id": "A1",
        "title": "Highest-impact action",
        "owner": "team-or-role",
        "timeline": "2 weeks",
        "expected_outcome": "Measurable improvement tied to objective"
      }
    ],
    "risks": [
      {
        "severity": "medium",
        "description": "Primary execution risk",
        "mitigation": "Concrete mitigation step"
      }
    ]
  },
  "assumptions": [
    "Assumption 1",
    "Assumption 2"
  ],
  "input_quality": {
    "completeness": "partial",
    "notes": "List missing context that may affect confidence"
  },
  "next_review_trigger": "Condition or date that should trigger a re-run"
}
```

## Constraints

- **Scope Discipline**: This skill should only evaluate the scope explicitly provided; out-of-scope systems must be flagged, not inferred.
- **Input Dependency**: Output quality depends on the completeness and recency of supplied context. Missing constraints must be called out explicitly.
- **Decision Support**: This skill produces structured recommendations, not final approvals or legal/security sign-off by itself.
- **No Hidden Assumptions**: Any assumption that materially affects recommendations must be listed in the output.
- **Agent Portability**: Recommendations should remain implementation-agnostic enough to be reused across Codex, Claude, and similar agent workflows.

## Invocation

### Example 1: Standard Planning Run

**Input**:
```json
{
  "objective": "Prepare a reliable first-pass plan for upcoming execution",
  "scope": "Core application workflow and supporting operations",
  "context": "Current process has inconsistent outputs between teams",
  "constraints": ["No downtime", "No new paid tooling"],
  "analysis_depth": "standard",
  "time_horizon": "quarter"
}
```

**Output**:
```json
{
  "tokenomics_risk_review": {
    "artifact_type": "tokenomics_risk_report",
    "overall_status": "actionable",
    "executive_summary": "The current state can support delivery after three blocking actions are completed.",
    "confidence": "medium",
    "priority_actions": [
      {
        "id": "A1",
        "title": "Standardize operating checklist",
        "owner": "project-lead",
        "timeline": "1 week",
        "expected_outcome": "Reduced execution variance"
      }
    ],
    "risks": [
      {
        "severity": "medium",
        "description": "Missing baseline metrics",
        "mitigation": "Collect two-week baseline before optimization"
      }
    ]
  },
  "assumptions": [
    "Team capacity remains stable for this quarter"
  ],
  "input_quality": {
    "completeness": "good",
    "notes": "Sufficient context for a standard-depth run"
  },
  "next_review_trigger": "After first implementation milestone"
}
```

### Example 2: High-Risk Escalation Run

**Input**:
```json
{
  "objective": "Identify critical blockers before high-visibility launch",
  "scope": "Customer-facing release workflow",
  "context": "Launch date is fixed and rollback windows are limited",
  "constraints": ["No schedule slip", "Must keep audit trail"],
  "analysis_depth": "comprehensive",
  "time_horizon": "immediate"
}
```

**Output**:
```json
{
  "tokenomics_risk_review": {
    "artifact_type": "tokenomics_risk_report",
    "overall_status": "blocked",
    "executive_summary": "Launch should pause until high-severity control gaps are closed.",
    "confidence": "high",
    "priority_actions": [
      {
        "id": "A1",
        "title": "Close critical control gap",
        "owner": "incident-commander",
        "timeline": "48 hours",
        "expected_outcome": "Risk reduced to acceptable launch threshold"
      }
    ],
    "risks": [
      {
        "severity": "high",
        "description": "Single-point failure in release approvals",
        "mitigation": "Add dual-approval fallback and test during drill"
      }
    ]
  },
  "assumptions": [
    "Operational team is available for rapid remediation"
  ],
  "input_quality": {
    "completeness": "partial",
    "notes": "Some upstream dependency owners not yet identified"
  },
  "next_review_trigger": "Immediately after critical fixes are verified"
}
```
