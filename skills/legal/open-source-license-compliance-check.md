# Open Source License Compliance Check

## Purpose

This skill audits dependency licenses to identify obligations, incompatibilities, and release risks for commercial software distribution.

## Inputs

| Name | Type | Required | Description | Constraints |
|------|------|----------|-------------|-------------|
| `dependency_manifest` | array | Yes | Dependencies and detected licenses | At least 1 dependency |
| `distribution_model` | string | Yes | How the software is distributed | Valid values: "SaaS", "on-prem", "mobile", "embedded", "library" |
| `commercial_use` | boolean | Yes | Whether software is used commercially | Boolean |
| `modification_of_dependencies` | boolean | No | Whether OSS dependencies are modified | Default: false |
| `copyleft_tolerance` | string | No | Organization's accepted copyleft level | Valid values: "none", "weak", "strong", Default: "weak" |
| `attribution_process` | string | No | Current method for attribution notices | Optional |

## Output Format

```json
{
  "license_compliance_check": {
    "overall_status": "review_required",
    "high_risk_dependencies": [
      {
        "package": "example-lib",
        "license": "GPL-3.0",
        "risk": "Potential copyleft conflict with proprietary distribution",
        "recommended_action": "Replace dependency or isolate via service boundary"
      }
    ],
    "obligations": [
      "Include NOTICE file",
      "Provide license texts in distribution"
    ],
    "policy_violations": [
      "Unapproved strong copyleft package detected"
    ],
    "remediation_plan": [
      "Run dependency replacement spike",
      "Automate license scan in CI"
    ]
  },
  "counsel_escalation": true
}
```

## Constraints

- **Counsel Confirmation**: Final legal interpretation should be validated by legal counsel.
- **Metadata Accuracy**: License scan inaccuracies can produce false positives/negatives.
- **Distribution Context**: Obligations vary by deployment/distribution model.
- **Transitive Risk**: Transitive dependencies can introduce hidden license obligations.
- **Change Tracking**: Compliance should be re-run when dependency graph changes.

## Invocation

### Example 1: SaaS Dependency Audit

**Input**:
```json
{
  "dependency_manifest": [
    {
      "package": "framework-x",
      "license": "MIT"
    },
    {
      "package": "image-tool",
      "license": "LGPL-2.1"
    }
  ],
  "distribution_model": "SaaS",
  "commercial_use": true,
  "modification_of_dependencies": false,
  "copyleft_tolerance": "weak",
  "attribution_process": "Auto-generated acknowledgements page"
}
```

**Output**:
```json
{
  "license_compliance_check": {
    "overall_status": "pass_with_obligations",
    "obligations": [
      "Retain LGPL notices for image-tool"
    ],
    "policy_violations": []
  },
  "counsel_escalation": false
}
```

### Example 2: On-Prem Enterprise Distribution

**Input**:
```json
{
  "dependency_manifest": [
    {
      "package": "core-engine",
      "license": "Apache-2.0"
    },
    {
      "package": "legacy-parser",
      "license": "GPL-3.0"
    }
  ],
  "distribution_model": "on-prem",
  "commercial_use": true,
  "modification_of_dependencies": true,
  "copyleft_tolerance": "none",
  "attribution_process": "manual"
}
```

**Output**:
```json
{
  "license_compliance_check": {
    "overall_status": "blocked",
    "policy_violations": [
      "GPL-3.0 package violates policy for on-prem proprietary release"
    ],
    "remediation_plan": [
      "Replace legacy-parser before release cut"
    ]
  },
  "counsel_escalation": true
}
```
