# User Story Mapping

## Purpose

This skill maps user journeys into activities, tasks, and release slices so product teams can ship coherent increments of value.

## Inputs

| Name | Type | Required | Description | Constraints |
|------|------|----------|-------------|-------------|
| `personas` | array | Yes | Primary user personas | At least 1 persona |
| `journey_goal` | string | Yes | Outcome users are trying to achieve | Non-empty string |
| `current_pain_points` | array | Yes | Known friction points | At least 1 item |
| `business_outcomes` | array | Yes | Business goals tied to journey | At least 1 item |
| `release_constraints` | array | No | Timeline, compliance, or capacity constraints | Optional |
| `integration_dependencies` | array | No | External system dependencies | Optional |

## Output Format

```json
{
  "user_story_map": {
    "backbone_activities": [
      "Discover",
      "Configure",
      "Execute",
      "Review"
    ],
    "story_slices": [
      {
        "release": "R1",
        "stories": [
          "As admin, I can invite teammates",
          "As user, I can complete setup checklist"
        ]
      },
      {
        "release": "R2",
        "stories": [
          "As admin, I can enforce policy templates"
        ]
      }
    ],
    "risk_stories": [
      "Cross-team handoff edge case for invite acceptance"
    ],
    "acceptance_focus": [
      "time_to_first_value",
      "task_completion_rate"
    ]
  },
  "alignment_notes": [
    "Design and support reviewed R1 stories"
  ]
}
```

## Constraints

- **Journey Integrity**: Stories should preserve end-to-end user flow, not isolated tasks only.
- **Slice Completeness**: Each release slice should deliver usable customer value.
- **Dependency Transparency**: Cross-team dependencies must be explicit in story slices.
- **Persona Specificity**: Mixed persona assumptions should be separated when behavior differs.
- **Validation Hook**: Stories should link to measurable outcomes or usability checks.

## Invocation

### Example 1: Team Onboarding Journey

**Input**:
```json
{
  "personas": [
    "workspace_admin",
    "new_member"
  ],
  "journey_goal": "Get a new team productive within first week",
  "current_pain_points": [
    "Invite links expire unpredictably",
    "Permissions are hard to understand"
  ],
  "business_outcomes": [
    "Increase week-1 activation",
    "Reduce onboarding support tickets"
  ],
  "release_constraints": [
    "Must ship by end of Q2"
  ],
  "integration_dependencies": [
    "Email service",
    "identity provider"
  ]
}
```

**Output**:
```json
{
  "user_story_map": {
    "story_slices": [
      {
        "release": "R1",
        "stories": [
          "Invite + accept flow",
          "Role visibility during onboarding"
        ]
      }
    ]
  },
  "alignment_notes": [
    "Support team validated top pain points"
  ]
}
```

### Example 2: Incident Acknowledgement Journey

**Input**:
```json
{
  "personas": [
    "oncall_engineer",
    "incident_commander"
  ],
  "journey_goal": "Acknowledge and coordinate incidents quickly",
  "current_pain_points": [
    "Alert noise",
    "Unclear ownership handoff"
  ],
  "business_outcomes": [
    "Reduce MTTA",
    "Improve escalation accuracy"
  ],
  "release_constraints": [
    "Must integrate with existing pager tooling"
  ],
  "integration_dependencies": [
    "Pager system",
    "chat ops bot"
  ]
}
```

**Output**:
```json
{
  "user_story_map": {
    "risk_stories": [
      "Pager webhook failure path"
    ],
    "acceptance_focus": [
      "mtta",
      "handoff_success_rate"
    ]
  },
  "alignment_notes": [
    "Ops lead requested game-day validation before launch"
  ]
}
```
