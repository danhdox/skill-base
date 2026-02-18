# Code Review Checklist

## Purpose

This skill provides a systematic framework for conducting thorough code reviews. It encodes best practices from senior engineers and helps teams maintain code quality, catch bugs early, and share knowledge effectively. The skill generates a structured checklist tailored to the code type, language, and context, ensuring consistent review quality across teams while capturing important security, performance, and maintainability concerns.

## Inputs

| Name | Type | Required | Description | Constraints |
|------|------|----------|-------------|-------------|
| `language` | string | Yes | Programming language of the code under review | Valid values: "JavaScript", "TypeScript", "Python", "Go", "Java", "C#", "Ruby", "Rust", "C++", "Other" |
| `code_type` | string | Yes | Type of code being reviewed | Valid values: "feature", "bugfix", "refactoring", "performance", "security", "test" |
| `files_changed` | number | No | Number of files modified in the change | Range: 1-100, Default: 1 |
| `lines_changed` | number | No | Approximate lines of code changed | Range: 1-5000, Default: 50 |
| `context` | string | No | Additional context about the change | Max 500 chars |
| `security_sensitive` | boolean | No | Whether code handles sensitive data or auth | Default: false |

## Output Format

```json
{
  "checklist": {
    "critical": [
      {
        "category": "Security",
        "item": "Verify input validation and sanitization",
        "rationale": "Prevent injection attacks and XSS vulnerabilities",
        "checked": false
      },
      {
        "category": "Correctness",
        "item": "Verify error handling covers edge cases",
        "rationale": "Prevent runtime failures and data corruption",
        "checked": false
      }
    ],
    "important": [
      {
        "category": "Testing",
        "item": "Check test coverage for new code paths",
        "rationale": "Ensure changes are verified and maintainable",
        "checked": false
      },
      {
        "category": "Performance",
        "item": "Review for N+1 queries or unnecessary loops",
        "rationale": "Prevent performance degradation",
        "checked": false
      }
    ],
    "recommended": [
      {
        "category": "Code Style",
        "item": "Verify consistent naming conventions",
        "rationale": "Maintain codebase readability",
        "checked": false
      },
      {
        "category": "Documentation",
        "item": "Check that complex logic is commented",
        "rationale": "Help future maintainers understand intent",
        "checked": false
      }
    ]
  },
  "language_specific_checks": [
    {
      "category": "TypeScript",
      "item": "Verify proper type annotations and no 'any' abuse",
      "priority": "important"
    }
  ],
  "review_guidance": {
    "estimated_time": "15-20 minutes",
    "focus_areas": ["Security validation", "Error handling", "Test coverage"],
    "suggested_reviewers": ["@security-team"],
    "blockers": []
  },
  "summary": {
    "total_items": 12,
    "critical_items": 2,
    "important_items": 5,
    "recommended_items": 5
  },
  "timestamp": "2024-03-15T10:30:00Z",
  "version": "1.0.0"
}
```

## Constraints

- **Code Size Limits**: Most effective for changes under 500 lines; larger changes should be broken down or require multiple focused reviews
- **Language Coverage**: Comprehensive checks available for mainstream languages; "Other" languages receive generic best-practice guidance only
- **Context Dependency**: Cannot assess domain-specific requirements without additional context; generic checks may miss business logic issues
- **Automation Boundary**: This skill generates a checklist but doesn't perform automated analysis; should be used alongside linters, static analysis, and tests
- **Not a Replacement**: Does not replace human judgment, domain expertise, or architectural review for significant changes
- **Review Scope**: Focuses on code quality and common issues; doesn't cover product requirements validation or UX concerns

## Invocation

### Example 1: Security-Sensitive Authentication Feature

**Input**:
```json
{
  "language": "TypeScript",
  "code_type": "feature",
  "files_changed": 5,
  "lines_changed": 300,
  "context": "New OAuth2 authentication flow with token refresh",
  "security_sensitive": true
}
```

**Output**:
```json
{
  "checklist": {
    "critical": [
      {
        "category": "Security",
        "item": "Verify OAuth2 token storage uses secure, httpOnly cookies or secure storage",
        "rationale": "Prevent token theft via XSS attacks",
        "checked": false
      },
      {
        "category": "Security",
        "item": "Confirm PKCE (Proof Key for Code Exchange) is implemented",
        "rationale": "Protect against authorization code interception",
        "checked": false
      },
      {
        "category": "Security",
        "item": "Check that refresh tokens are rotated on use",
        "rationale": "Limit impact of token compromise",
        "checked": false
      },
      {
        "category": "Security",
        "item": "Verify HTTPS-only enforcement for token endpoints",
        "rationale": "Prevent man-in-the-middle attacks",
        "checked": false
      },
      {
        "category": "Correctness",
        "item": "Validate token expiration is checked before use",
        "rationale": "Prevent unauthorized access with expired tokens",
        "checked": false
      }
    ],
    "important": [
      {
        "category": "Error Handling",
        "item": "Check that auth failures don't leak sensitive information",
        "rationale": "Prevent information disclosure attacks",
        "checked": false
      },
      {
        "category": "Testing",
        "item": "Verify test coverage for token refresh flow",
        "rationale": "Critical path must be thoroughly tested",
        "checked": false
      },
      {
        "category": "Testing",
        "item": "Confirm tests cover token expiration scenarios",
        "rationale": "Edge cases in auth are security-critical",
        "checked": false
      },
      {
        "category": "Logging",
        "item": "Verify auth events are logged (without sensitive data)",
        "rationale": "Enable security monitoring and debugging",
        "checked": false
      }
    ],
    "recommended": [
      {
        "category": "Documentation",
        "item": "Check that OAuth2 flow is documented",
        "rationale": "Help team understand security model",
        "checked": false
      },
      {
        "category": "Code Organization",
        "item": "Verify auth logic is properly separated from business logic",
        "rationale": "Maintain clear security boundaries",
        "checked": false
      }
    ]
  },
  "language_specific_checks": [
    {
      "category": "TypeScript",
      "item": "Verify proper type definitions for token payloads",
      "priority": "important"
    },
    {
      "category": "TypeScript",
      "item": "Check that secrets are not committed or logged",
      "priority": "critical"
    }
  ],
  "review_guidance": {
    "estimated_time": "30-45 minutes",
    "focus_areas": [
      "OAuth2 spec compliance",
      "Token security and storage",
      "Error handling and logging"
    ],
    "suggested_reviewers": ["@security-team", "@auth-experts"],
    "blockers": [
      "Must pass security review before merge"
    ]
  },
  "summary": {
    "total_items": 13,
    "critical_items": 5,
    "important_items": 5,
    "recommended_items": 3
  },
  "timestamp": "2024-03-15T11:15:00Z",
  "version": "1.0.0"
}
```

### Example 2: Simple Bug Fix

**Input**:
```json
{
  "language": "Python",
  "code_type": "bugfix",
  "files_changed": 1,
  "lines_changed": 15,
  "context": "Fix off-by-one error in pagination logic",
  "security_sensitive": false
}
```

**Output**:
```json
{
  "checklist": {
    "critical": [
      {
        "category": "Correctness",
        "item": "Verify the fix addresses the root cause, not just symptoms",
        "rationale": "Prevent recurring bugs",
        "checked": false
      },
      {
        "category": "Testing",
        "item": "Confirm regression test is added for this bug",
        "rationale": "Prevent reintroduction of the same bug",
        "checked": false
      }
    ],
    "important": [
      {
        "category": "Edge Cases",
        "item": "Check boundary conditions (first page, last page, empty results)",
        "rationale": "Off-by-one errors often affect boundaries",
        "checked": false
      },
      {
        "category": "Testing",
        "item": "Verify existing pagination tests still pass",
        "rationale": "Ensure fix doesn't break other scenarios",
        "checked": false
      }
    ],
    "recommended": [
      {
        "category": "Code Style",
        "item": "Check that variable names clearly indicate inclusive/exclusive ranges",
        "rationale": "Prevent future confusion",
        "checked": false
      }
    ]
  },
  "language_specific_checks": [
    {
      "category": "Python",
      "item": "Verify proper use of range() or slice notation",
      "priority": "important"
    }
  ],
  "review_guidance": {
    "estimated_time": "10-15 minutes",
    "focus_areas": ["Boundary conditions", "Test coverage"],
    "suggested_reviewers": [],
    "blockers": []
  },
  "summary": {
    "total_items": 6,
    "critical_items": 2,
    "important_items": 2,
    "recommended_items": 2
  },
  "timestamp": "2024-03-15T11:30:00Z",
  "version": "1.0.0"
}
```

### Example 3: Performance Optimization

**Input**:
```json
{
  "language": "Go",
  "code_type": "performance",
  "files_changed": 3,
  "lines_changed": 120,
  "context": "Optimize database queries using connection pooling and caching"
}
```

**Output**:
```json
{
  "checklist": {
    "critical": [
      {
        "category": "Correctness",
        "item": "Verify optimization doesn't change behavior or break functionality",
        "rationale": "Performance gains are worthless if they introduce bugs",
        "checked": false
      },
      {
        "category": "Performance",
        "item": "Confirm performance improvement with benchmarks",
        "rationale": "Validate the optimization actually helps",
        "checked": false
      }
    ],
    "important": [
      {
        "category": "Caching",
        "item": "Check cache invalidation strategy is correct",
        "rationale": "Stale cache data causes incorrect behavior",
        "checked": false
      },
      {
        "category": "Resource Management",
        "item": "Verify connection pool is properly sized and cleaned up",
        "rationale": "Prevent resource leaks",
        "checked": false
      },
      {
        "category": "Testing",
        "item": "Check that edge cases (cache miss, pool exhaustion) are tested",
        "rationale": "Performance code often has complex edge cases",
        "checked": false
      },
      {
        "category": "Monitoring",
        "item": "Verify metrics are added for cache hit rate and pool usage",
        "rationale": "Enable production monitoring of optimization",
        "checked": false
      }
    ],
    "recommended": [
      {
        "category": "Documentation",
        "item": "Document caching strategy and TTL decisions",
        "rationale": "Help team understand performance characteristics",
        "checked": false
      }
    ]
  },
  "language_specific_checks": [
    {
      "category": "Go",
      "item": "Verify goroutines are properly managed and don't leak",
      "priority": "critical"
    },
    {
      "category": "Go",
      "item": "Check that context cancellation is respected",
      "priority": "important"
    }
  ],
  "review_guidance": {
    "estimated_time": "25-35 minutes",
    "focus_areas": [
      "Benchmark results validation",
      "Cache correctness",
      "Resource management"
    ],
    "suggested_reviewers": ["@performance-team"],
    "blockers": ["Need benchmark results before merge"]
  },
  "summary": {
    "total_items": 9,
    "critical_items": 2,
    "important_items": 4,
    "recommended_items": 3
  },
  "timestamp": "2024-03-15T11:45:00Z",
  "version": "1.0.0"
}
```

## Metadata

- **Version**: 1.0.0
- **Domain**: Engineering
- **Author**: Engineering Excellence Team
- **Last Updated**: 2024-03-15
- **Status**: Stable
- **Tags**: code-review, quality, engineering, best-practices
- **Estimated Runtime**: 5-10 seconds
