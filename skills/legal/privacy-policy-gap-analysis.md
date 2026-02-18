# Privacy Policy Gap Analysis

## Purpose

This skill reviews privacy policy language against product data practices and regulatory expectations to identify disclosure gaps and remediation priorities.

## Inputs

| Name | Type | Required | Description | Constraints |
|------|------|----------|-------------|-------------|
| `policy_text` | string | Yes | Current privacy policy content | Non-empty string |
| `data_processing_activities` | array | Yes | How personal data is collected/used/shared | At least 1 activity |
| `jurisdictions` | array | Yes | Applicable legal regions | At least 1 jurisdiction |
| `subprocessor_list` | array | No | Vendors/subprocessors handling personal data | Optional |
| `retention_practices` | string | No | Current retention and deletion practices | Optional but recommended |
| `data_subject_request_flow` | string | No | Process for DSAR handling | Optional |

## Output Format

```json
{
  "privacy_gap_analysis": {
    "overall_risk": "medium",
    "coverage_matrix": [
      {
        "topic": "data collection",
        "status": "covered"
      },
      {
        "topic": "cross-border transfers",
        "status": "gap"
      },
      {
        "topic": "retention periods",
        "status": "partial"
      }
    ],
    "gaps": [
      {
        "severity": "high",
        "topic": "third-party disclosures",
        "issue": "Policy does not enumerate subprocessor categories",
        "recommended_update": "Add subprocessor categories and purpose-specific disclosures"
      }
    ],
    "priority_order": [
      "high",
      "medium",
      "low"
    ]
  },
  "legal_review_required": true
}
```

## Constraints

- **Not Legal Advice**: This skill supports legal drafting but does not replace counsel review.
- **Policy-to-Practice Alignment**: Recommendations depend on accurate operational data flow mapping.
- **Jurisdiction Sensitivity**: Requirements differ materially by region and must be explicitly scoped.
- **Change Management**: Policy updates should coordinate with product and support operations.
- **Version Traceability**: Changes should preserve clear revision history and effective dates.

## Invocation

### Example 1: SaaS Privacy Policy Annual Review

**Input**:
```json
{
  "policy_text": "Current policy dated 2025-01-10",
  "data_processing_activities": [
    "account creation",
    "usage analytics",
    "support logs"
  ],
  "jurisdictions": [
    "US",
    "EU"
  ],
  "subprocessor_list": [
    "cloud hosting",
    "email delivery provider"
  ],
  "retention_practices": "Account data retained while subscription is active",
  "data_subject_request_flow": "Support ticket + manual legal review"
}
```

**Output**:
```json
{
  "privacy_gap_analysis": {
    "overall_risk": "medium",
    "gaps": [
      {
        "severity": "medium",
        "topic": "retention",
        "issue": "Retention periods are not specific by data category",
        "recommended_update": "Add category-based retention schedule"
      }
    ]
  },
  "legal_review_required": true
}
```

### Example 2: New AI Feature Data Disclosure

**Input**:
```json
{
  "policy_text": "Policy includes generic analytics language",
  "data_processing_activities": [
    "prompt submission",
    "model output storage",
    "quality review"
  ],
  "jurisdictions": [
    "US",
    "UK"
  ],
  "subprocessor_list": [
    "model hosting provider"
  ],
  "retention_practices": "30-day transient logs",
  "data_subject_request_flow": "Self-service privacy portal"
}
```

**Output**:
```json
{
  "privacy_gap_analysis": {
    "overall_risk": "high",
    "gaps": [
      {
        "severity": "high",
        "topic": "AI data use",
        "issue": "Policy does not explain model training/retention choices",
        "recommended_update": "Add explicit AI processing disclosure and user controls"
      }
    ]
  },
  "legal_review_required": true
}
```
