# API Design Review

## Purpose

This skill performs a pre-implementation design review for APIs to catch consistency, usability, security, and versioning issues before code is shipped. It helps teams avoid expensive interface rewrites and improves long-term developer experience.

## Inputs

| Name | Type | Required | Description | Constraints |
|------|------|----------|-------------|-------------|
| `api_style` | string | Yes | API style under review | Valid values: "REST", "GraphQL", "gRPC", "event-driven" |
| `api_spec` | string | Yes | OpenAPI/GraphQL schema/protobuf summary | Non-empty string or linked spec excerpt |
| `consumer_types` | array | Yes | Primary API consumers | At least 1 item (e.g., web, mobile, partner) |
| `auth_model` | string | No | Authentication/authorization approach | Default: "unspecified" |
| `versioning_strategy` | string | No | Versioning and deprecation policy | Describe timeline and compatibility guarantees |
| `non_functional_requirements` | array | No | Latency, reliability, and throughput goals | Each item should be measurable |

## Output Format

```json
{
  "api_design_review": {
    "overall_status": "needs_changes",
    "design_score": 72,
    "strengths": [
      "Resource naming is consistent",
      "Error envelope is mostly standardized"
    ],
    "findings": [
      {
        "severity": "high",
        "area": "versioning",
        "issue": "Breaking field rename without migration window",
        "recommendation": "Ship additive field first, deprecate old field over two minor versions"
      }
    ],
    "compatibility_notes": [
      "Partner SDK impact requires coordination"
    ],
    "release_readiness": "blocked_on_high_findings"
  },
  "open_questions": [
    "Should rate-limit quotas differ by tenant tier?"
  ],
  "next_steps": [
    "Address high findings",
    "Re-review before implementation freeze"
  ]
}
```

## Constraints

- **Interface Focus**: This skill reviews API contract quality, not implementation code correctness.
- **Spec Quality Dependency**: Missing or stale API specs reduce confidence and must be flagged.
- **Consumer Context Required**: Recommendations may be misleading if consumer types are omitted.
- **Policy Alignment**: Security and data retention requirements should reference organization policy, not guessed defaults.
- **Backward Compatibility**: Breaking changes must include migration guidance to be considered acceptable.

## Invocation

### Example 1: REST API Before Public Beta

**Input**:
```json
{
  "api_style": "REST",
  "api_spec": "OpenAPI v3 spec for Billing and Invoices endpoints",
  "consumer_types": [
    "web",
    "partner"
  ],
  "auth_model": "OAuth2 client credentials",
  "versioning_strategy": "URI versioning with 6-month deprecation window",
  "non_functional_requirements": [
    "p95 < 300ms",
    "99.9% success rate"
  ]
}
```

**Output**:
```json
{
  "api_design_review": {
    "overall_status": "needs_changes",
    "design_score": 78,
    "findings": [
      {
        "severity": "medium",
        "area": "pagination",
        "issue": "Inconsistent cursor format across list endpoints",
        "recommendation": "Adopt a shared cursor schema and examples in docs"
      }
    ],
    "release_readiness": "ready_after_medium_findings"
  },
  "next_steps": [
    "Unify pagination schema",
    "Add partner migration notes"
  ]
}
```

### Example 2: gRPC Internal Platform API

**Input**:
```json
{
  "api_style": "gRPC",
  "api_spec": "protobuf services for authz and entitlements",
  "consumer_types": [
    "backend-services"
  ],
  "auth_model": "mTLS + workload identity",
  "versioning_strategy": "field-level additive evolution",
  "non_functional_requirements": [
    "p99 < 120ms",
    "10k RPS burst"
  ]
}
```

**Output**:
```json
{
  "api_design_review": {
    "overall_status": "approved_with_notes",
    "design_score": 88,
    "findings": [
      {
        "severity": "low",
        "area": "observability",
        "issue": "Missing correlation-id guidance",
        "recommendation": "Add standard metadata key and tracing requirement"
      }
    ],
    "release_readiness": "approved"
  },
  "next_steps": [
    "Document tracing metadata in platform handbook"
  ]
}
```
