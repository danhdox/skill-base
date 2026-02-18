# Threat Modeling (STRIDE)

## Purpose

This skill identifies security threats across system components using STRIDE and prioritizes mitigations based on likelihood and impact.

## Inputs

| Name | Type | Required | Description | Constraints |
|------|------|----------|-------------|-------------|
| `system_architecture` | string | Yes | Architecture overview and boundaries | Non-empty string |
| `assets` | array | Yes | Critical assets to protect | At least 1 asset |
| `trust_boundaries` | array | Yes | System trust boundaries | At least 1 boundary |
| `data_flows` | array | Yes | Key data flows between components | At least 1 flow |
| `authentication_model` | string | No | AuthN/AuthZ approach | Optional |
| `third_party_integrations` | array | No | External services and dependencies | Optional |

## Output Format

```json
{
  "stride_threat_model": {
    "threats": [
      {
        "stride_category": "Tampering",
        "component": "webhook-ingest",
        "scenario": "Unsigned webhook payload replay",
        "risk": "high",
        "mitigation": "Require HMAC verification + nonce store"
      }
    ],
    "risk_summary": {
      "critical": 1,
      "high": 3,
      "medium": 5,
      "low": 4
    },
    "mitigation_backlog": [
      {
        "id": "TM-03",
        "owner": "security-engineering",
        "target_date": "2026-03-10"
      }
    ],
    "residual_risk": "medium"
  },
  "review_scope": "application and integration layer"
}
```

## Constraints

- **Architecture Fidelity**: Incomplete architecture context reduces model accuracy.
- **Threat Breadth**: STRIDE coverage should include all trust boundaries, not just perimeter components.
- **Risk Calibration**: Severity must reflect both exploitability and business impact.
- **Mitigation Ownership**: Threat findings without owners should be considered unresolved.
- **Periodic Refresh**: Threat model should be refreshed after major architecture changes.

## Invocation

### Example 1: SaaS File Upload Pipeline

**Input**:
```json
{
  "system_architecture": "Web app uploads files to object storage then async scans and indexes",
  "assets": [
    "customer documents",
    "metadata index",
    "tenant keys"
  ],
  "trust_boundaries": [
    "browser -> api",
    "api -> storage",
    "worker -> database"
  ],
  "data_flows": [
    "upload request",
    "scan callback",
    "index write"
  ],
  "authentication_model": "OIDC + tenant RBAC",
  "third_party_integrations": [
    "malware scanning service"
  ]
}
```

**Output**:
```json
{
  "stride_threat_model": {
    "risk_summary": {
      "critical": 0,
      "high": 2,
      "medium": 4,
      "low": 3
    },
    "residual_risk": "low_after_mitigations"
  },
  "review_scope": "upload + processing path"
}
```

### Example 2: Internal Service Mesh Auth Path

**Input**:
```json
{
  "system_architecture": "Microservices communicate over mesh with mTLS and JWT service tokens",
  "assets": [
    "service credentials",
    "billing data"
  ],
  "trust_boundaries": [
    "service namespace boundary",
    "control-plane boundary"
  ],
  "data_flows": [
    "token mint",
    "service-to-service call",
    "audit log"
  ],
  "authentication_model": "SPIFFE identity + OPA policy",
  "third_party_integrations": [
    "central secrets manager"
  ]
}
```

**Output**:
```json
{
  "stride_threat_model": {
    "threats": [
      {
        "stride_category": "Spoofing",
        "component": "token-issuer",
        "scenario": "misconfigured trust domain",
        "risk": "high"
      }
    ],
    "residual_risk": "medium"
  },
  "review_scope": "service identity plane"
}
```
