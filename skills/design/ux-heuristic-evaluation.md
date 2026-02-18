# UX Heuristic Evaluation

## Purpose

This skill evaluates product UX against established usability heuristics and generates prioritized improvements with rationale.

## Inputs

| Name | Type | Required | Description | Constraints |
|------|------|----------|-------------|-------------|
| `product_area` | string | Yes | Feature or flow being evaluated | Non-empty string |
| `target_personas` | array | Yes | Primary users for this area | At least 1 persona |
| `critical_tasks` | array | Yes | Top tasks users must complete | At least 1 task |
| `platform` | string | Yes | Platform under review | Valid values: "web", "ios", "android", "desktop" |
| `heuristic_set` | array | No | Heuristics to apply | Default: Nielsen 10 heuristics |
| `known_constraints` | array | No | Design/engineering constraints | Optional |

## Output Format

```json
{
  "ux_heuristic_evaluation": {
    "overall_usability_score": 76,
    "heuristic_findings": [
      {
        "heuristic": "Visibility of system status",
        "severity": "medium",
        "issue": "Long-running import has no progress feedback",
        "recommendation": "Add progress state with stage-level updates"
      }
    ],
    "quick_wins": [
      "Clarify destructive action confirmation copy"
    ],
    "strategic_improvements": [
      "Simplify first-run navigation hierarchy"
    ],
    "evaluation_confidence": "high"
  },
  "next_research_needed": [
    "Task-based usability test with new users"
  ]
}
```

## Constraints

- **Heuristic Method Limits**: Heuristic evaluation does not replace user testing.
- **Persona Fit**: Findings should be tied to intended personas and their goals.
- **Task Scope**: Evaluation should focus on high-value user tasks first.
- **Severity Calibration**: Severity ratings should combine usability impact and frequency.
- **Constraint Awareness**: Recommendations should acknowledge real implementation constraints.

## Invocation

### Example 1: Dashboard Setup Flow

**Input**:
```json
{
  "product_area": "Initial dashboard setup wizard",
  "target_personas": [
    "new_admin",
    "analyst"
  ],
  "critical_tasks": [
    "Connect data source",
    "Create first dashboard"
  ],
  "platform": "web",
  "heuristic_set": [
    "Nielsen"
  ],
  "known_constraints": [
    "No major IA changes this quarter"
  ]
}
```

**Output**:
```json
{
  "ux_heuristic_evaluation": {
    "overall_usability_score": 71,
    "quick_wins": [
      "Improve step titles and completion confirmation"
    ]
  },
  "next_research_needed": [
    "Wizard abandonment study"
  ]
}
```

### Example 2: Mobile Approval Workflow

**Input**:
```json
{
  "product_area": "Mobile request approval screen",
  "target_personas": [
    "approver_manager"
  ],
  "critical_tasks": [
    "Review request",
    "Approve/reject with reason"
  ],
  "platform": "ios",
  "heuristic_set": [
    "Nielsen",
    "mobile accessibility heuristics"
  ],
  "known_constraints": [
    "Cannot increase number of screens in flow"
  ]
}
```

**Output**:
```json
{
  "ux_heuristic_evaluation": {
    "overall_usability_score": 82,
    "strategic_improvements": [
      "Improve context visibility before irreversible actions"
    ]
  },
  "next_research_needed": [
    "Field test under low-connectivity conditions"
  ]
}
```
