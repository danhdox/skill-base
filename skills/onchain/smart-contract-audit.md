# Smart Contract Security Audit

## Purpose

This skill provides a systematic framework for auditing smart contract security on blockchain platforms. It encodes expertise from blockchain security researchers and auditors to help teams identify vulnerabilities, unsafe patterns, and potential exploits before deployment. The skill produces a comprehensive security assessment with severity ratings, specific vulnerability descriptions, remediation guidance, and gas optimization recommendations, reducing the risk of costly exploits and loss of funds.

## Inputs

| Name | Type | Required | Description | Constraints |
|------|------|----------|-------------|-------------|
| `contract_code` | string | Yes | Source code of the smart contract | Max 25000 chars; Solidity or Vyper |
| `blockchain_platform` | string | Yes | Target blockchain platform | Valid values: "Ethereum", "Polygon", "BSC", "Arbitrum", "Optimism", "Avalanche", "Other_EVM" |
| `contract_type` | string | Yes | Primary contract function | Valid values: "token", "defi", "nft", "dao", "bridge", "marketplace", "staking", "other" |
| `compiler_version` | string | No | Solidity or Vyper compiler version | Format: "0.8.20" or similar |
| `audit_depth` | string | No | Depth of security analysis | Valid values: "quick", "standard", "comprehensive", Default: "standard" |
| `include_gas_analysis` | boolean | No | Include gas optimization recommendations | Default: true |

## Output Format

```json
{
  "audit_summary": {
    "contract_name": "TokenVault",
    "contract_type": "defi",
    "platform": "Ethereum",
    "compiler_version": "0.8.20",
    "overall_risk_level": "high",
    "critical_issues": 2,
    "high_issues": 3,
    "medium_issues": 5,
    "low_issues": 8,
    "informational": 12,
    "audit_recommendation": "do_not_deploy"
  },
  "critical_vulnerabilities": [
    {
      "id": "CRIT-001",
      "category": "Reentrancy",
      "title": "Reentrancy vulnerability in withdraw function",
      "severity": "critical",
      "cwe_id": "CWE-841",
      "location": {
        "function": "withdraw",
        "line_numbers": [45, 52]
      },
      "description": "The withdraw function updates user balance after external call, allowing reentrancy attacks via fallback function.",
      "code_snippet": "function withdraw(uint amount) external {\n    require(balances[msg.sender] >= amount);\n    (bool success, ) = msg.sender.call{value: amount}(\"\");\n    require(success);\n    balances[msg.sender] -= amount;\n}",
      "exploit_scenario": "Attacker can recursively call withdraw() before balance is updated, draining contract funds.",
      "potential_impact": "Complete loss of all funds in contract (~$500K+ based on typical TVL)",
      "remediation": {
        "recommendation": "Apply checks-effects-interactions pattern: update balance before external call",
        "fixed_code": "function withdraw(uint amount) external {\n    require(balances[msg.sender] >= amount);\n    balances[msg.sender] -= amount;\n    (bool success, ) = msg.sender.call{value: amount}(\"\");\n    require(success);\n}",
        "additional_measures": [
          "Add ReentrancyGuard modifier from OpenZeppelin",
          "Consider using pull payment pattern instead"
        ]
      },
      "references": [
        "https://consensys.github.io/smart-contract-best-practices/attacks/reentrancy/",
        "SWC-107: Reentrancy"
      ]
    },
    {
      "id": "CRIT-002",
      "category": "Access Control",
      "title": "Missing access control on critical admin function",
      "severity": "critical",
      "cwe_id": "CWE-284",
      "location": {
        "function": "setTreasuryAddress",
        "line_numbers": [78]
      },
      "description": "Function to change treasury address has no access control, allowing anyone to redirect funds.",
      "code_snippet": "function setTreasuryAddress(address _treasury) external {\n    treasury = _treasury;\n}",
      "exploit_scenario": "Attacker calls setTreasuryAddress with their own address, then triggers fund transfers to steal treasury.",
      "potential_impact": "Complete loss of treasury funds and protocol revenue",
      "remediation": {
        "recommendation": "Add onlyOwner or role-based access control",
        "fixed_code": "function setTreasuryAddress(address _treasury) external onlyOwner {\n    require(_treasury != address(0), \"Invalid address\");\n    treasury = _treasury;\n    emit TreasuryAddressUpdated(_treasury);\n}",
        "additional_measures": [
          "Implement timelock for critical parameter changes",
          "Add multi-sig requirement for admin functions",
          "Emit events for all admin actions"
        ]
      },
      "references": [
        "SWC-105: Unprotected Ether Withdrawal"
      ]
    }
  ],
  "high_vulnerabilities": [
    {
      "id": "HIGH-001",
      "category": "Integer Overflow",
      "title": "Potential integer overflow in reward calculation",
      "severity": "high",
      "location": {
        "function": "calculateReward",
        "line_numbers": [102, 104]
      },
      "description": "Multiplication before division can cause overflow for large values",
      "remediation": {
        "recommendation": "Use SafeMath or rely on Solidity 0.8+ overflow checks",
        "note": "Solidity 0.8+ has built-in overflow protection, but verify edge cases"
      }
    }
  ],
  "medium_vulnerabilities": [
    {
      "id": "MED-001",
      "category": "Gas Optimization",
      "title": "Unbounded loop in user iteration",
      "severity": "medium",
      "location": {
        "function": "distributeRewards",
        "line_numbers": [120, 125]
      },
      "description": "Loop over all users array can exceed gas limit as user count grows",
      "remediation": {
        "recommendation": "Implement pagination or pull payment pattern",
        "fixed_approach": "Allow users to claim rewards individually rather than push distribution"
      }
    }
  ],
  "low_vulnerabilities": [
    {
      "id": "LOW-001",
      "category": "Best Practices",
      "title": "Missing zero address check",
      "severity": "low",
      "location": {
        "function": "constructor",
        "line_numbers": [25]
      },
      "remediation": {
        "recommendation": "Add require(_token != address(0)) checks for address parameters"
      }
    }
  ],
  "informational_findings": [
    {
      "id": "INFO-001",
      "category": "Code Quality",
      "title": "Magic numbers should be constants",
      "location": {
        "line_numbers": [67, 89]
      },
      "recommendation": "Define constants for repeated numeric values (e.g., BASIS_POINTS = 10000)"
    },
    {
      "id": "INFO-002",
      "category": "Documentation",
      "title": "Missing NatSpec documentation",
      "recommendation": "Add NatSpec comments (@notice, @param, @return) for all public functions"
    }
  ],
  "gas_optimization": {
    "estimated_savings": "~15-20%",
    "recommendations": [
      {
        "id": "GAS-001",
        "title": "Use uint256 instead of smaller uints",
        "location": "State variables",
        "current_gas": 23000,
        "optimized_gas": 20000,
        "savings": 3000,
        "explanation": "uint8 requires additional gas for conversions; uint256 is native word size"
      },
      {
        "id": "GAS-002",
        "title": "Cache array length in loops",
        "location": "Line 120",
        "savings": "~200 gas per iteration",
        "fixed_code": "uint256 length = users.length;\nfor (uint256 i = 0; i < length; i++) {"
      },
      {
        "id": "GAS-003",
        "title": "Use calldata instead of memory for read-only function parameters",
        "location": "Function parameters",
        "savings": "~1000 gas per call"
      }
    ]
  },
  "best_practices_compliance": {
    "checks_effects_interactions": {
      "compliant": false,
      "violations": 2,
      "details": "withdraw() and claimRewards() violate pattern"
    },
    "access_control": {
      "compliant": false,
      "violations": 1,
      "details": "Missing access control on admin functions"
    },
    "event_emission": {
      "compliant": "partial",
      "missing_events": ["State changes in setTreasuryAddress", "Parameter updates"]
    },
    "input_validation": {
      "compliant": "partial",
      "missing_checks": ["Zero address validation", "Amount boundaries"]
    }
  },
  "dependencies_analysis": {
    "imported_contracts": [
      {
        "name": "OpenZeppelin/SafeMath.sol",
        "version": "4.9.0",
        "status": "up_to_date",
        "known_vulnerabilities": 0
      },
      {
        "name": "OpenZeppelin/Ownable.sol",
        "version": "4.9.0",
        "status": "up_to_date",
        "known_vulnerabilities": 0
      }
    ],
    "recommendation": "Dependencies are current; no known vulnerabilities"
  },
  "deployment_checklist": [
    {
      "item": "Fix all critical vulnerabilities",
      "status": "required",
      "completed": false
    },
    {
      "item": "Address high-severity issues",
      "status": "required",
      "completed": false
    },
    {
      "item": "Review and test all remediations",
      "status": "required",
      "completed": false
    },
    {
      "item": "Conduct full test coverage",
      "status": "required",
      "completed": false
    },
    {
      "item": "External security audit",
      "status": "recommended",
      "completed": false
    },
    {
      "item": "Bug bounty program",
      "status": "recommended",
      "completed": false
    }
  ],
  "recommendations": {
    "immediate_actions": [
      "DO NOT DEPLOY: Fix CRIT-001 reentrancy vulnerability immediately",
      "DO NOT DEPLOY: Add access control to setTreasuryAddress function",
      "Implement ReentrancyGuard on all external functions handling value transfers"
    ],
    "before_deployment": [
      "Address all high-severity findings",
      "Add comprehensive test coverage (>95%) including edge cases",
      "Conduct formal external audit by reputable firm",
      "Set up monitoring and emergency pause mechanism"
    ],
    "post_deployment": [
      "Implement bug bounty program",
      "Monitor contract for unusual activity",
      "Prepare emergency response plan",
      "Plan regular security reviews for upgrades"
    ]
  },
  "estimated_audit_cost": {
    "internal_remediation": "40-60 hours developer time",
    "external_audit": "$15,000 - $35,000 USD",
    "bug_bounty_budget": "$10,000 - $50,000 USD recommended"
  },
  "summary": "This smart contract contains CRITICAL security vulnerabilities that make it unsafe for deployment. The reentrancy vulnerability in the withdraw function and missing access control on the treasury address function could result in complete loss of funds. These issues must be resolved before any deployment consideration. Additionally, several high and medium severity issues should be addressed to improve overall security posture. Recommend comprehensive remediation, full test coverage, and external audit before mainnet deployment.",
  "timestamp": "2024-03-15T10:30:00Z",
  "version": "1.0.0"
}
```

## Constraints

- **Contract Size**: Optimized for contracts up to 1000 lines; larger systems should be audited in modules
- **Language Support**: Solidity and Vyper only; other smart contract languages not supported
- **EVM Focus**: Designed for EVM-compatible chains; non-EVM chains (Solana, Cardano) require different analysis
- **Static Analysis Limitations**: Cannot detect all business logic flaws or economic exploits; focuses on common security patterns
- **Automated Analysis**: Combines pattern matching and heuristics but may miss novel attack vectors
- **Not a Replacement**: Does not replace comprehensive manual audit by security experts, especially for high-value contracts
- **Testing Scope**: Identifies issues but doesn't execute exploit code or perform dynamic analysis
- **Update Frequency**: Vulnerability patterns updated regularly, but novel attacks may not be detected immediately
- **No Formal Verification**: Does not provide mathematical proofs of correctness; use formal verification tools for critical contracts

## Invocation

### Example 1: DeFi Staking Contract (Comprehensive Audit)

**Input**:
```json
{
  "contract_code": "[Full Solidity code for staking contract - ~400 lines]",
  "blockchain_platform": "Ethereum",
  "contract_type": "staking",
  "compiler_version": "0.8.20",
  "audit_depth": "comprehensive",
  "include_gas_analysis": true
}
```

**Output**: [See detailed output format above - comprehensive analysis with 2 critical, 3 high, 5 medium, 8 low issues]

### Example 2: Simple ERC-20 Token (Quick Audit)

**Input**:
```json
{
  "contract_code": "[Standard ERC-20 implementation - ~150 lines]",
  "blockchain_platform": "Ethereum",
  "contract_type": "token",
  "compiler_version": "0.8.19",
  "audit_depth": "quick"
}
```

**Output**:
```json
{
  "audit_summary": {
    "contract_name": "MyToken",
    "contract_type": "token",
    "platform": "Ethereum",
    "compiler_version": "0.8.19",
    "overall_risk_level": "low",
    "critical_issues": 0,
    "high_issues": 0,
    "medium_issues": 1,
    "low_issues": 2,
    "informational": 4,
    "audit_recommendation": "safe_with_minor_improvements"
  },
  "critical_vulnerabilities": [],
  "high_vulnerabilities": [],
  "medium_vulnerabilities": [
    {
      "id": "MED-001",
      "category": "Centralization Risk",
      "title": "Owner can mint unlimited tokens",
      "severity": "medium",
      "location": {
        "function": "mint",
        "line_numbers": [65]
      },
      "description": "No supply cap on minting function",
      "remediation": {
        "recommendation": "Consider adding max supply cap or removing mint after initial distribution",
        "note": "Acceptable for governance tokens, but document clearly"
      }
    }
  ],
  "low_vulnerabilities": [
    {
      "id": "LOW-001",
      "category": "Best Practices",
      "title": "Missing event emission in critical functions",
      "severity": "low",
      "location": {
        "function": "mint",
        "line_numbers": [65]
      },
      "remediation": {
        "recommendation": "Emit Minted event for tracking"
      }
    }
  ],
  "informational_findings": [
    {
      "id": "INFO-001",
      "category": "Code Quality",
      "title": "Consider using OpenZeppelin's ERC20 implementation",
      "recommendation": "Leverage battle-tested libraries instead of custom implementation"
    }
  ],
  "best_practices_compliance": {
    "checks_effects_interactions": {
      "compliant": true
    },
    "access_control": {
      "compliant": true,
      "details": "Proper use of Ownable pattern"
    },
    "event_emission": {
      "compliant": "partial",
      "missing_events": ["Mint events"]
    }
  },
  "recommendations": {
    "immediate_actions": [],
    "before_deployment": [
      "Add maximum supply cap or document unlimited minting rationale",
      "Add comprehensive event emission",
      "Consider third-party audit if high value"
    ],
    "post_deployment": [
      "Monitor for unusual minting activity",
      "Consider transitioning to governance-based minting"
    ]
  },
  "summary": "Standard ERC-20 token implementation with good security practices. Main concern is unlimited minting capability, which may be acceptable depending on tokenomics design. No critical issues found. Safe for deployment with documented centralization risks.",
  "timestamp": "2024-03-15T16:20:00Z",
  "version": "1.0.0"
}
```

### Example 3: NFT Marketplace Contract

**Input**:
```json
{
  "contract_code": "[NFT marketplace contract code - ~600 lines]",
  "blockchain_platform": "Polygon",
  "contract_type": "marketplace",
  "compiler_version": "0.8.17",
  "audit_depth": "standard",
  "include_gas_analysis": true
}
```

**Output**:
```json
{
  "audit_summary": {
    "contract_name": "NFTMarketplace",
    "contract_type": "marketplace",
    "platform": "Polygon",
    "overall_risk_level": "medium",
    "critical_issues": 0,
    "high_issues": 1,
    "medium_issues": 3,
    "low_issues": 5,
    "audit_recommendation": "deploy_after_fixes"
  },
  "high_vulnerabilities": [
    {
      "id": "HIGH-001",
      "category": "Price Manipulation",
      "title": "Front-running vulnerability in listing price",
      "severity": "high",
      "location": {
        "function": "updateListing",
        "line_numbers": [145]
      },
      "description": "Seller can update listing price after buyer initiates purchase transaction",
      "exploit_scenario": "Seller sees purchase transaction in mempool, front-runs with price increase",
      "remediation": {
        "recommendation": "Require explicit price parameter in purchase function to lock price",
        "fixed_approach": "function buyNFT(uint256 listingId, uint256 maxPrice) - revert if listing.price > maxPrice"
      }
    }
  ],
  "gas_optimization": {
    "estimated_savings": "~25%",
    "recommendations": [
      {
        "id": "GAS-001",
        "title": "Batch listing updates",
        "savings": "~8000 gas per batch operation"
      },
      {
        "id": "GAS-002",
        "title": "Use mapping instead of array for active listings",
        "savings": "~15000 gas for large collections"
      }
    ]
  },
  "recommendations": {
    "immediate_actions": [
      "Fix front-running vulnerability in updateListing"
    ],
    "before_deployment": [
      "Implement slippage protection on purchases",
      "Add comprehensive tests for edge cases",
      "Consider royalty enforcement mechanism"
    ]
  },
  "summary": "NFT marketplace with one high-severity front-running issue that should be addressed before deployment. Several medium priority improvements related to user experience and gas optimization. Overall architecture is sound.",
  "timestamp": "2024-03-15T16:35:00Z",
  "version": "1.0.0"
}
```

## Metadata

- **Version**: 1.0.0
- **Domain**: Onchain
- **Author**: Blockchain Security Team
- **Last Updated**: 2024-03-15
- **Status**: Stable
- **Tags**: smart-contracts, security, blockchain, audit, ethereum, solidity
- **Estimated Runtime**: 45-180 seconds (depending on contract size and audit depth)
- **Important Notice**: This skill provides automated security analysis but does not replace professional security audits. Always engage qualified auditors for production contracts, especially those handling significant value.
- **Dependencies**: Solidity parser, static analysis tools, vulnerability pattern database
