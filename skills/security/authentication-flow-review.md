# Authentication Flow Review

## Purpose

This skill reviews authentication and session flows for security, reliability, and user-friction risks before release.

## Inputs

| Name | Type | Required | Description | Constraints |
|------|------|----------|-------------|-------------|
| `auth_flows` | array | Yes | Login/signup/recovery/session flows | At least 1 flow |
| `identity_provider` | string | Yes | Primary identity stack | Non-empty string |
| `session_management` | string | Yes | Session/token lifecycle model | Non-empty string |
| `mfa_policy` | string | No | MFA requirements by user tier | Optional |
| `account_recovery` | string | No | Recovery/reset strategy | Optional |
| `threat_assumptions` | array | No | Known threat scenarios | Optional |

## Output Format

```json
{
  "authentication_flow_review": {
    "overall_status": "needs_changes",
    "security_findings": [
      {
        "severity": "high",
        "flow": "password-reset",
        "issue": "Reset token not invalidated on use",
        "recommendation": "Single-use token with immediate revocation"
      }
    ],
    "ux_findings": [
      "MFA enrollment path too easy to skip for admins"
    ],
    "resilience_findings": [
      "IdP outage fallback not documented"
    ],
    "release_gate": "blocked_on_high_security_findings"
  },
  "required_follow_up": [
    "Pen test auth flows",
    "Add recovery abuse-rate limits"
  ]
}
```

## Constraints

- **Flow Completeness**: Login-only reviews are insufficient; include recovery and session revocation paths.
- **Threat Context**: Findings should reflect realistic attacker capabilities for the product tier.
- **Identity Coupling**: IdP limitations may constrain recommended controls.
- **Usability Balance**: Strong controls should be evaluated against account lockout/support impact.
- **Operational Readiness**: Incident runbooks are required for auth provider outages.

## Invocation

### Example 1: Enterprise SSO + Password Fallback

**Input**:
```json
{
  "auth_flows": [
    "SSO login",
    "password login",
    "password reset",
    "session revoke"
  ],
  "identity_provider": "Okta",
  "session_management": "JWT access + rotating refresh token",
  "mfa_policy": "Required for admins and finance roles",
  "account_recovery": "Email link + support escalation",
  "threat_assumptions": [
    "credential stuffing",
    "session theft"
  ]
}
```

**Output**:
```json
{
  "authentication_flow_review": {
    "overall_status": "needs_changes",
    "release_gate": "blocked_on_high_security_findings"
  },
  "required_follow_up": [
    "Add failed-login anomaly detection"
  ]
}
```

### Example 2: Consumer Passwordless Magic Link

**Input**:
```json
{
  "auth_flows": [
    "magic-link login",
    "device remember",
    "account recovery"
  ],
  "identity_provider": "custom auth service",
  "session_management": "opaque server sessions",
  "mfa_policy": "Not required",
  "account_recovery": "support verification workflow",
  "threat_assumptions": [
    "email inbox compromise",
    "link replay"
  ]
}
```

**Output**:
```json
{
  "authentication_flow_review": {
    "overall_status": "approved_with_notes",
    "ux_findings": [
      "Add explicit session activity page for users"
    ],
    "release_gate": "approved_after_low_fixes"
  },
  "required_follow_up": [
    "Implement one-click global logout"
  ]
}
```
