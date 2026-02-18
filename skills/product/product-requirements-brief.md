# Product Requirements Brief

## Purpose

This skill transforms product intent into a concise, execution-ready requirements brief with clear scope, success criteria, and delivery guardrails.

## Inputs

| Name | Type | Required | Description | Constraints |
|------|------|----------|-------------|-------------|
| `problem_statement` | string | Yes | User or business problem to solve | Non-empty string |
| `target_users` | array | Yes | Primary user personas | At least 1 persona |
| `goals` | array | Yes | Desired outcomes | At least 1 measurable goal |
| `non_goals` | array | No | Out-of-scope items | Optional but recommended |
| `success_metrics` | array | Yes | How success is measured | At least 1 metric |
| `constraints` | array | No | Technical/legal/timeline constraints | Optional |

## Output Format

```json
{
  "product_requirements_brief": {
    "scope_summary": "Clear MVP boundary with must-have and defer list",
    "requirements": [
      {
        "id": "REQ-1",
        "statement": "System must support role-based visibility controls",
        "priority": "must"
      }
    ],
    "assumptions": [
      "Existing auth service can support additional claims"
    ],
    "dependencies": [
      "Design system component update",
      "Data pipeline availability"
    ],
    "acceptance_criteria": [
      "Metric baseline and target defined for each goal"
    ],
    "readiness": "draft"
  },
  "handoff_checklist": [
    "Engineering signoff",
    "Design signoff",
    "Analytics instrumentation plan"
  ]
}
```

## Constraints

- **Problem-first**: Requirements should be tied directly to the stated problem.
- **Scope Control**: Non-goals must be explicit to prevent scope creep.
- **Measurable Outcomes**: Goals without measurable metrics should be flagged.
- **Dependency Awareness**: External dependencies must be documented with owners.
- **Implementation Neutrality**: Requirements should avoid over-prescribing technical solutions.

## Invocation

### Example 1: Admin Audit Log Feature

**Input**:
```json
{
  "problem_statement": "Admins cannot trace permission changes reliably",
  "target_users": [
    "workspace_admin",
    "security_analyst"
  ],
  "goals": [
    "Improve compliance readiness",
    "Reduce support escalations"
  ],
  "non_goals": [
    "No custom report builder in MVP"
  ],
  "success_metrics": [
    "audit_log_adoption",
    "time_to_investigate"
  ],
  "constraints": [
    "Must reuse existing event store",
    "SOC2 evidence requirements"
  ]
}
```

**Output**:
```json
{
  "product_requirements_brief": {
    "readiness": "ready_for_estimation",
    "dependencies": [
      "Event schema update",
      "RBAC policy review"
    ]
  },
  "handoff_checklist": [
    "Security review",
    "Support training"
  ]
}
```

### Example 2: Onboarding Checklist Revamp

**Input**:
```json
{
  "problem_statement": "New users drop off before first key action",
  "target_users": [
    "new_trial_user"
  ],
  "goals": [
    "Increase first-week activation by 15%"
  ],
  "non_goals": [
    "No full IA redesign"
  ],
  "success_metrics": [
    "activation_rate_day7",
    "time_to_first_value"
  ],
  "constraints": [
    "Launch within 6 weeks"
  ]
}
```

**Output**:
```json
{
  "product_requirements_brief": {
    "readiness": "draft",
    "assumptions": [
      "Behavioral nudges can be localized in current frontend stack"
    ]
  },
  "handoff_checklist": [
    "Analytics event QA"
  ]
}
```
