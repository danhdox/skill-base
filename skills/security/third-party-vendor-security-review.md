# Third-Party Vendor Security Review

## Purpose

This skill evaluates third-party vendors for security, privacy, and operational risk before procurement or renewal.

## Inputs

| Name | Type | Required | Description | Constraints |
|------|------|----------|-------------|-------------|
| `vendor_name` | string | Yes | Vendor being reviewed | Non-empty string |
| `service_description` | string | Yes | What the vendor provides | Non-empty string |
| `data_access_level` | string | Yes | Sensitivity of data vendor can access | Valid values: "none", "metadata", "customer-content", "regulated-data" |
| `security_artifacts` | array | Yes | SOC2/ISO reports, pen test summaries, etc. | At least 1 artifact |
| `integration_surface` | array | No | APIs, webhooks, network connectivity | Optional |
| `contractual_controls` | array | No | Security/privacy contract clauses | Optional |

## Output Format

```json
{
  "vendor_security_review": {
    "overall_risk_rating": "medium",
    "control_assessment": [
      {
        "control": "access_management",
        "status": "adequate"
      },
      {
        "control": "incident_notification",
        "status": "gap"
      }
    ],
    "top_risks": [
      {
        "severity": "high",
        "risk": "No contractual breach-notification SLA",
        "mitigation": "Add 72-hour notification requirement"
      }
    ],
    "approval_recommendation": "conditional_approval",
    "required_conditions": [
      "Execute DPA addendum",
      "Enable SSO provisioning"
    ]
  },
  "review_expiry": "12 months"
}
```

## Constraints

- **Document Quality**: Outdated attestations should reduce confidence in conclusions.
- **Scope Fit**: Vendor controls must be assessed in context of intended integration scope.
- **Shared Responsibility**: Some controls remain customer responsibilities and must be called out.
- **Contract Dependency**: Technical controls and contractual commitments must align.
- **Reassessment Trigger**: Material product or control changes require re-review.

## Invocation

### Example 1: Analytics SaaS Procurement

**Input**:
```json
{
  "vendor_name": "MetricsCloud",
  "service_description": "Product analytics and event warehousing",
  "data_access_level": "metadata",
  "security_artifacts": [
    "SOC2 Type II 2025",
    "Pen test attestation"
  ],
  "integration_surface": [
    "event ingestion API",
    "warehouse sync"
  ],
  "contractual_controls": [
    "DPA required",
    "subprocessor notification clause"
  ]
}
```

**Output**:
```json
{
  "vendor_security_review": {
    "overall_risk_rating": "low",
    "approval_recommendation": "approved"
  },
  "review_expiry": "12 months"
}
```

### Example 2: Support Tool Renewal

**Input**:
```json
{
  "vendor_name": "SupportDesk Pro",
  "service_description": "Ticketing platform with customer attachment storage",
  "data_access_level": "customer-content",
  "security_artifacts": [
    "SOC2 Type II 2024"
  ],
  "integration_surface": [
    "SSO",
    "webhook automation",
    "attachment CDN"
  ],
  "contractual_controls": [
    "Breach notification clause missing"
  ]
}
```

**Output**:
```json
{
  "vendor_security_review": {
    "overall_risk_rating": "high",
    "approval_recommendation": "blocked_until_controls_added",
    "required_conditions": [
      "Update contract SLA",
      "Restrict attachment retention"
    ]
  },
  "review_expiry": "6 months"
}
```
