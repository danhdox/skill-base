# Contract Risk Assessment

## Purpose

This skill provides a systematic framework for reviewing and assessing legal risks in contracts. It encodes expertise from commercial lawyers to help teams identify potential liabilities, unfavorable terms, and compliance issues before signing agreements. The skill produces a structured risk assessment with severity ratings, specific clause concerns, and actionable recommendations, enabling informed decision-making while reducing legal review costs for standard contracts.

## Inputs

| Name | Type | Required | Description | Constraints |
|------|------|----------|-------------|-------------|
| `contract_type` | string | Yes | Type of contract being reviewed | Valid values: "NDA", "MSA", "SaaS_Agreement", "Employment", "Vendor_Agreement", "Partnership", "License", "Other" |
| `contract_text` | string | Yes | Full text of the contract or key sections | Max 50000 chars (approx 10000 words) |
| `party_role` | string | Yes | Your organization's role in the contract | Valid values: "vendor", "customer", "employer", "employee", "licensor", "licensee" |
| `jurisdiction` | string | No | Governing law jurisdiction | Valid values: "US", "UK", "EU", "California", "New_York", "Other", Default: "US" |
| `contract_value` | number | No | Total contract value in USD | Range: 0-100000000, used for risk prioritization |
| `review_depth` | string | No | Level of review detail | Valid values: "standard", "thorough", "expedited", Default: "standard" |

## Output Format

```json
{
  "risk_assessment": {
    "overall_risk_level": "medium",
    "overall_score": 65,
    "recommended_action": "negotiate_key_terms",
    "contract_type": "SaaS_Agreement",
    "party_role": "customer"
  },
  "critical_issues": [
    {
      "category": "Liability",
      "issue": "Liability cap set at contract value with no exceptions",
      "severity": "high",
      "clause_reference": "Section 12.3",
      "risk_description": "Customer liability limited only by contract value, not reasonable for SaaS context",
      "potential_impact": "Unlimited liability for certain categories (IP infringement, data breaches)",
      "recommendation": "Negotiate for liability cap of 12 months fees with carve-outs only for gross negligence"
    },
    {
      "category": "Data Protection",
      "issue": "Vendor retains rights to customer data for AI training",
      "severity": "high",
      "clause_reference": "Section 8.5",
      "risk_description": "Broad data usage rights could compromise confidential information",
      "potential_impact": "Proprietary data may be used to train competitor models",
      "recommendation": "Require explicit opt-in for any data usage beyond service delivery"
    }
  ],
  "important_concerns": [
    {
      "category": "Termination",
      "issue": "Automatic renewal with 90-day notice period",
      "severity": "medium",
      "clause_reference": "Section 4.2",
      "risk_description": "Long notice period may lock in unfavorable terms",
      "recommendation": "Negotiate for 30-day notice or annual review checkpoint"
    },
    {
      "category": "Indemnification",
      "issue": "One-sided indemnification favoring vendor",
      "severity": "medium",
      "clause_reference": "Section 11.1",
      "risk_description": "Customer must indemnify vendor but not vice versa",
      "recommendation": "Request mutual indemnification obligations"
    }
  ],
  "standard_concerns": [
    {
      "category": "Payment Terms",
      "issue": "Payment due net-15 days",
      "severity": "low",
      "clause_reference": "Section 5.3",
      "recommendation": "Request net-30 payment terms for better cash flow"
    }
  ],
  "positive_terms": [
    {
      "category": "Service Levels",
      "description": "Clear SLA with 99.9% uptime guarantee and service credits",
      "clause_reference": "Schedule A"
    },
    {
      "category": "Security",
      "description": "SOC 2 Type II compliance with annual audits",
      "clause_reference": "Section 9.2"
    }
  ],
  "missing_provisions": [
    {
      "provision": "Data Processing Agreement (DPA)",
      "importance": "critical",
      "reason": "Required for GDPR/CCPA compliance when processing personal data",
      "recommendation": "Request separate DPA or add data processing terms"
    },
    {
      "provision": "Disaster Recovery and Business Continuity",
      "importance": "important",
      "reason": "No clear commitments on RTO/RPO for service restoration",
      "recommendation": "Define disaster recovery expectations"
    }
  ],
  "compliance_analysis": {
    "gdpr_compliant": false,
    "ccpa_compliant": false,
    "issues": [
      "Missing data subject rights provisions",
      "No clear data retention and deletion policies",
      "Subprocessor list not provided"
    ]
  },
  "clause_analysis": [
    {
      "clause_name": "Limitation of Liability",
      "location": "Section 12",
      "standard_vs_actual": "Significantly favors vendor compared to industry standard",
      "negotiation_priority": "high"
    },
    {
      "clause_name": "Intellectual Property",
      "location": "Section 10",
      "standard_vs_actual": "Standard IP ownership terms",
      "negotiation_priority": "low"
    }
  ],
  "recommendations": {
    "must_address": [
      "Negotiate liability cap to 12 months of fees",
      "Remove vendor's right to use customer data for AI training",
      "Add Data Processing Agreement for GDPR/CCPA compliance"
    ],
    "should_address": [
      "Request mutual indemnification obligations",
      "Reduce automatic renewal notice period to 30 days",
      "Add disaster recovery commitments"
    ],
    "nice_to_have": [
      "Extend payment terms to net-30",
      "Add most-favored-nation pricing clause"
    ]
  },
  "summary": "This SaaS agreement contains several concerning provisions that significantly favor the vendor. Critical issues include overly broad liability terms and problematic data usage rights. The contract also lacks necessary data protection provisions required for GDPR/CCPA compliance. Recommend negotiating critical and important items before signing. Estimated negotiation leverage: medium (competitive market with alternatives).",
  "estimated_legal_review_cost": {
    "value": 2500,
    "currency": "USD",
    "note": "Full attorney review for this complexity and value"
  },
  "timestamp": "2024-03-15T10:30:00Z",
  "version": "1.0.0"
}
```

## Constraints

- **Contract Length**: Optimized for contracts up to 50 pages; longer contracts should be reviewed in sections or require extended processing time
- **Language Support**: English language contracts only; translations may lose legal nuance
- **Jurisdiction Expertise**: Most comprehensive for US/UK/EU law; other jurisdictions receive general risk analysis only
- **Contract Types**: Covers common commercial contracts; specialized agreements (M&A, real estate, IP licensing) require domain-specific legal expertise
- **Not Legal Advice**: This skill provides risk identification and guidance but does not constitute legal advice; consult qualified attorney for binding opinions
- **Context Limitations**: Cannot assess business context, negotiation leverage, or strategic considerations without additional information
- **Standard Library**: Risk assessment based on market-standard terms; may not capture industry-specific customs or practices
- **Update Frequency**: Legal standards evolve; recommendations reflect best practices as of skill version date

## Invocation

### Example 1: SaaS Customer Agreement Review

**Input**:
```json
{
  "contract_type": "SaaS_Agreement",
  "contract_text": "[Full contract text of 15-page SaaS agreement]",
  "party_role": "customer",
  "jurisdiction": "California",
  "contract_value": 120000,
  "review_depth": "thorough"
}
```

**Output**:
```json
{
  "risk_assessment": {
    "overall_risk_level": "medium-high",
    "overall_score": 58,
    "recommended_action": "negotiate_key_terms",
    "contract_type": "SaaS_Agreement",
    "party_role": "customer"
  },
  "critical_issues": [
    {
      "category": "Liability",
      "issue": "Unlimited liability for data breaches",
      "severity": "high",
      "clause_reference": "Section 12.3(c)",
      "risk_description": "Liability cap ($120K) has broad carve-outs including all data security incidents",
      "potential_impact": "Could face multi-million dollar liability for vendor's security failure",
      "recommendation": "Limit liability carve-outs to gross negligence and willful misconduct only"
    },
    {
      "category": "Data Ownership",
      "issue": "Vendor claims joint ownership of customer-generated data insights",
      "severity": "high",
      "clause_reference": "Section 8.7",
      "risk_description": "Aggregated data insights could include proprietary business information",
      "potential_impact": "Competitive intelligence may be shared with other customers",
      "recommendation": "Ensure customer retains exclusive ownership of all data and derived insights"
    }
  ],
  "important_concerns": [
    {
      "category": "Audit Rights",
      "issue": "Limited audit rights - only once per year with 60-day notice",
      "severity": "medium",
      "clause_reference": "Section 9.6",
      "risk_description": "Insufficient for compliance with security and financial regulations",
      "recommendation": "Request quarterly audit rights with 30-day notice plus incident-triggered audits"
    },
    {
      "category": "Vendor Lock-in",
      "issue": "No data portability provisions",
      "severity": "medium",
      "clause_reference": "Missing from Agreement",
      "risk_description": "Difficult to migrate to competitor if needed",
      "recommendation": "Add data export requirements in standard format with 90-day transition assistance"
    }
  ],
  "standard_concerns": [
    {
      "category": "Pricing",
      "issue": "Annual price increase up to 10% without caps",
      "severity": "low",
      "clause_reference": "Section 5.2",
      "recommendation": "Cap annual increases at CPI or 5%, whichever is lower"
    }
  ],
  "positive_terms": [
    {
      "category": "Service Levels",
      "description": "Strong SLA with 99.9% uptime, 1-hour critical issue response, meaningful service credits",
      "clause_reference": "Exhibit B - Service Level Agreement"
    },
    {
      "category": "Security Standards",
      "description": "SOC 2 Type II compliance, annual penetration testing, encryption at rest and in transit",
      "clause_reference": "Section 9.1-9.4"
    }
  ],
  "missing_provisions": [
    {
      "provision": "Data Processing Agreement (DPA)",
      "importance": "critical",
      "reason": "Required for CCPA compliance when processing California resident data",
      "recommendation": "Must add comprehensive DPA as separate exhibit"
    },
    {
      "provision": "Right to Delete Data",
      "importance": "critical",
      "reason": "CCPA requires ability to request data deletion within 45 days",
      "recommendation": "Add data deletion commitment with specific timeline"
    },
    {
      "provision": "Source Code Escrow",
      "importance": "important",
      "reason": "Business continuity if vendor goes bankrupt or is acquired",
      "recommendation": "Establish source code escrow for mission-critical systems"
    }
  ],
  "compliance_analysis": {
    "gdpr_compliant": "N/A",
    "ccpa_compliant": false,
    "issues": [
      "No Data Processing Agreement",
      "Missing consumer data rights (deletion, portability, opt-out)",
      "Unclear data retention policies",
      "No subprocessor disclosure mechanism"
    ],
    "required_actions": [
      "Add CCPA-compliant DPA",
      "Define data subject rights fulfillment process",
      "Disclose all subprocessors with opt-out mechanism"
    ]
  },
  "clause_analysis": [
    {
      "clause_name": "Limitation of Liability",
      "location": "Section 12",
      "standard_vs_actual": "Heavily favors vendor - carve-outs eliminate most protection",
      "negotiation_priority": "critical"
    },
    {
      "clause_name": "Termination for Convenience",
      "location": "Section 13.2",
      "standard_vs_actual": "Standard 30-day termination with prorated refund",
      "negotiation_priority": "low"
    }
  ],
  "recommendations": {
    "must_address": [
      "Limit liability carve-outs to gross negligence/willful misconduct",
      "Remove vendor ownership claims on customer data insights",
      "Add comprehensive CCPA-compliant Data Processing Agreement",
      "Include data portability and deletion provisions"
    ],
    "should_address": [
      "Expand audit rights to quarterly with incident triggers",
      "Add source code escrow provisions",
      "Cap annual price increases",
      "Add 90-day transition assistance period"
    ],
    "nice_to_have": [
      "Most-favored-nation pricing",
      "Extended payment terms to net-45",
      "Dedicated customer success manager commitment"
    ]
  },
  "summary": "This SaaS agreement presents medium-high risk due to overly broad liability carve-outs, concerning data ownership provisions, and missing CCPA compliance requirements. Given the $120K annual value and California jurisdiction, addressing data protection and liability issues is critical before signing. Vendor appears to be using a one-sided template; significant negotiation is warranted and likely achievable in competitive SaaS market.",
  "negotiation_strategy": {
    "leverage_assessment": "medium",
    "rationale": "Competitive market with alternatives; $120K contract is significant but not enterprise-scale",
    "likely_vendor_flexibility": [
      "Data ownership terms - high flexibility",
      "Liability caps - medium flexibility (standard ask)",
      "CCPA compliance - high flexibility (legal requirement)",
      "Audit rights - medium flexibility"
    ]
  },
  "estimated_legal_review_cost": {
    "value": 3500,
    "currency": "USD",
    "note": "Attorney review and negotiation support for contract of this complexity and value"
  },
  "timestamp": "2024-03-15T15:30:00Z",
  "version": "1.0.0"
}
```

### Example 2: Simple NDA Review (Expedited)

**Input**:
```json
{
  "contract_type": "NDA",
  "contract_text": "[Full text of 3-page mutual NDA]",
  "party_role": "vendor",
  "review_depth": "expedited"
}
```

**Output**:
```json
{
  "risk_assessment": {
    "overall_risk_level": "low",
    "overall_score": 85,
    "recommended_action": "safe_to_sign",
    "contract_type": "NDA",
    "party_role": "vendor"
  },
  "critical_issues": [],
  "important_concerns": [],
  "standard_concerns": [
    {
      "category": "Term",
      "issue": "5-year confidentiality period",
      "severity": "low",
      "clause_reference": "Section 3",
      "recommendation": "Industry standard is 3 years; consider negotiating down if not critical"
    }
  ],
  "positive_terms": [
    {
      "category": "Mutual Obligations",
      "description": "Balanced mutual NDA with symmetric obligations",
      "clause_reference": "Throughout"
    },
    {
      "category": "Exceptions",
      "description": "Standard carve-outs for public information, independent development, required disclosures",
      "clause_reference": "Section 2"
    }
  ],
  "missing_provisions": [],
  "recommendations": {
    "must_address": [],
    "should_address": [],
    "nice_to_have": [
      "Consider reducing confidentiality period to 3 years"
    ]
  },
  "summary": "Standard mutual NDA with balanced terms and appropriate exceptions. No significant red flags. Safe to sign with minimal risk. The 5-year term is slightly longer than typical but not problematic for most business contexts.",
  "estimated_legal_review_cost": {
    "value": 500,
    "currency": "USD",
    "note": "Brief attorney review for standard NDA"
  },
  "timestamp": "2024-03-15T15:45:00Z",
  "version": "1.0.0"
}
```

## Metadata

- **Version**: 1.0.0
- **Domain**: Legal
- **Author**: Legal Operations Team
- **Last Updated**: 2024-03-15
- **Status**: Stable
- **Tags**: legal, contracts, risk-assessment, compliance
- **Estimated Runtime**: 20-90 seconds (depending on contract length and review depth)
- **Important Notice**: This skill provides risk analysis and guidance but does not constitute legal advice. Always consult with a qualified attorney for legal decisions.
