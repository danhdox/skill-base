# Accessibility Audit (WCAG)

## Purpose

This skill evaluates interfaces against WCAG criteria and prioritizes remediation based on user impact and compliance risk.

## Inputs

| Name | Type | Required | Description | Constraints |
|------|------|----------|-------------|-------------|
| `target_surfaces` | array | Yes | Screens/pages/components to audit | At least 1 surface |
| `platforms` | array | Yes | Platforms included in the audit | At least 1 platform |
| `wcag_level` | string | Yes | Target WCAG conformance level | Valid values: "A", "AA", "AAA" |
| `assistive_tech_scope` | array | No | Screen readers/input methods in scope | Optional |
| `localization_scope` | array | No | Locales covered | Optional |
| `remediation_window` | string | No | Target timeline for fixes | Optional |

## Output Format

```json
{
  "accessibility_audit_wcag": {
    "conformance_summary": {
      "wcag_level": "AA",
      "pass_rate": 0.84,
      "critical_failures": 3
    },
    "findings": [
      {
        "severity": "critical",
        "criterion": "1.3.1 Info and Relationships",
        "issue": "Form labels not programmatically associated",
        "affected_surfaces": [
          "signup_form"
        ],
        "recommended_fix": "Use explicit label-for bindings and aria-describedby"
      }
    ],
    "remediation_plan": [
      {
        "priority": "P0",
        "owner": "frontend-platform",
        "target_date": "2026-03-01"
      }
    ],
    "retest_strategy": "Automated + manual assistive tech verification"
  },
  "compliance_risk": "high_until_p0_closed"
}
```

## Constraints

- **Tooling Limits**: Automated scanners cannot detect all accessibility issues.
- **Manual Verification**: Keyboard and screen-reader checks are required for confidence.
- **Locale Differences**: Localization can introduce unique accessibility regressions.
- **Priority Focus**: Critical user flows should be audited first when scope is large.
- **Sustained Compliance**: Accessibility requires ongoing regression checks, not one-time audits.

## Invocation

### Example 1: Signup and Billing Flow Audit

**Input**:
```json
{
  "target_surfaces": [
    "signup",
    "plan-selection",
    "billing-details"
  ],
  "platforms": [
    "web"
  ],
  "wcag_level": "AA",
  "assistive_tech_scope": [
    "NVDA",
    "VoiceOver"
  ],
  "localization_scope": [
    "en-US"
  ],
  "remediation_window": "6 weeks"
}
```

**Output**:
```json
{
  "accessibility_audit_wcag": {
    "conformance_summary": {
      "pass_rate": 0.88,
      "critical_failures": 1
    },
    "compliance_phase": "pre-release"
  },
  "compliance_risk": "medium"
}
```

### Example 2: Mobile Navigation Audit

**Input**:
```json
{
  "target_surfaces": [
    "home",
    "settings",
    "notifications"
  ],
  "platforms": [
    "ios",
    "android"
  ],
  "wcag_level": "AA",
  "assistive_tech_scope": [
    "VoiceOver",
    "TalkBack"
  ],
  "localization_scope": [
    "en-US",
    "es-ES"
  ],
  "remediation_window": "8 weeks"
}
```

**Output**:
```json
{
  "accessibility_audit_wcag": {
    "findings": [
      {
        "severity": "high",
        "criterion": "2.4.7 Focus Visible",
        "issue": "Focus indicator insufficient contrast on dark backgrounds"
      }
    ]
  },
  "compliance_risk": "high"
}
```
