# Design System Audit

## Purpose

This skill audits design system health across component quality, token consistency, documentation coverage, and adoption patterns.

## Inputs

| Name | Type | Required | Description | Constraints |
|------|------|----------|-------------|-------------|
| `component_inventory` | array | Yes | Current component catalog | At least 1 component |
| `design_tokens` | array | Yes | Token sets in use | At least 1 token group |
| `adoption_data` | object | Yes | Usage/adoption metrics | Include at least one product surface |
| `documentation_coverage` | string | No | Current docs quality summary | Optional |
| `accessibility_baseline` | string | No | Known accessibility maturity | Optional |
| `governance_model` | string | No | How changes are proposed/reviewed | Optional |

## Output Format

```json
{
  "design_system_audit": {
    "health_score": 68,
    "coverage_findings": [
      {
        "area": "components",
        "issue": "Table variants duplicated across 3 product teams",
        "severity": "high"
      }
    ],
    "token_consistency": {
      "status": "warning",
      "notes": [
        "Spacing scale diverges in mobile app"
      ]
    },
    "documentation_gaps": [
      "Missing do/don't guidance for complex form patterns"
    ],
    "adoption_recommendations": [
      "Deprecate duplicate table variants over two releases"
    ]
  },
  "audit_status": "improvement_plan_required"
}
```

## Constraints

- **Inventory Accuracy**: Audit quality depends on a current and complete component inventory.
- **Cross-Platform Scope**: Web/mobile/platform-specific variants should be compared explicitly.
- **Governance Coupling**: Adoption issues often stem from weak governance, not missing components only.
- **Migration Reality**: Deprecation recommendations should include migration pathways.
- **Accessibility Integration**: System health scoring should account for accessibility maturity.

## Invocation

### Example 1: Enterprise Web Design System Audit

**Input**:
```json
{
  "component_inventory": [
    "button",
    "table",
    "modal",
    "date-picker",
    "toast"
  ],
  "design_tokens": [
    "color",
    "typography",
    "spacing",
    "radius"
  ],
  "adoption_data": {
    "products_using_system": 5,
    "coverage_pct": 63
  },
  "documentation_coverage": "Core components documented, advanced patterns partial",
  "accessibility_baseline": "mixed WCAG 2.1 AA compliance",
  "governance_model": "weekly design-system working group"
}
```

**Output**:
```json
{
  "design_system_audit": {
    "health_score": 74,
    "adoption_recommendations": [
      "Create migration kit for legacy table component"
    ]
  },
  "audit_status": "on_track"
}
```

### Example 2: Multi-Platform System Consolidation

**Input**:
```json
{
  "component_inventory": [
    "button-web",
    "button-ios",
    "button-android",
    "input-web"
  ],
  "design_tokens": [
    "semantic color",
    "motion"
  ],
  "adoption_data": {
    "platform_variance_incidents": 14,
    "coverage_pct": 41
  },
  "documentation_coverage": "Platform docs fragmented",
  "accessibility_baseline": "unknown",
  "governance_model": "ad hoc"
}
```

**Output**:
```json
{
  "design_system_audit": {
    "health_score": 55,
    "coverage_findings": [
      {
        "area": "platform parity",
        "issue": "Token semantics diverge across native clients"
      }
    ]
  },
  "audit_status": "critical_attention_needed"
}
```
