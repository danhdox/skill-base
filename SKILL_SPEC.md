# Skill Specification

This document defines the required format for all skills in the skill-base repository. Following this specification ensures skills are consistent, discoverable, and composable.

## Required Sections

Every skill MUST include the following sections in order:

### 1. Purpose

**Required**: Yes  
**Format**: Prose description

A clear, concise statement of what the skill does and when it should be used. This should answer:

- What problem does this skill solve?
- What expertise does it encode?
- What value does it provide to the invoker?

**Example**:
```markdown
## Purpose

This skill provides a structured framework for calculating Total Addressable Market (TAM), Serviceable Addressable Market (SAM), and Serviceable Obtainable Market (SOM) for a given business opportunity. It encodes best practices from growth strategy consulting and helps teams make data-driven decisions about market opportunities.
```

### 2. Inputs

**Required**: Yes  
**Format**: Structured list with types and descriptions

Define all required and optional parameters the skill accepts. Each input should specify:

- **Name**: Parameter identifier
- **Type**: Data type (string, number, boolean, object, array, etc.)
- **Required**: Whether the parameter is mandatory
- **Description**: What the parameter represents
- **Default**: Default value if optional
- **Constraints**: Valid ranges, formats, or values

**Example**:
```markdown
## Inputs

| Name | Type | Required | Description | Constraints |
|------|------|----------|-------------|-------------|
| `target_market` | string | Yes | Description of the target market or industry | Non-empty string |
| `geography` | string | Yes | Geographic region (e.g., "North America", "Global") | Valid region name |
| `product_type` | string | No | Type of product or service | Default: "Software" |
| `year` | number | No | Target year for market size | 2020-2030, Default: current year |
```

### 3. Output Format

**Required**: Yes  
**Format**: Schema definition with examples

Define the structure of the skill's output. Use JSON schema, TypeScript interfaces, or clear examples. Outputs should be:

- **Structured**: Follow a consistent, parseable format
- **Complete**: Include all relevant data points
- **Documented**: Explain each field's meaning and units

**Example**:
```markdown
## Output Format

```json
{
  "market_analysis": {
    "tam": {
      "value": 450000000000,
      "unit": "USD",
      "confidence": "medium",
      "methodology": "Top-down industry analysis"
    },
    "sam": {
      "value": 45000000000,
      "unit": "USD",
      "confidence": "medium",
      "methodology": "Geographic and segment filtering"
    },
    "som": {
      "value": 450000000,
      "unit": "USD",
      "confidence": "high",
      "methodology": "Bottoms-up sales capacity model"
    }
  },
  "assumptions": [
    "Global SaaS market growing at 18% CAGR",
    "Target segment represents 10% of total market"
  ],
  "data_sources": [
    "Gartner Market Analysis 2024",
    "Company sales data"
  ],
  "timestamp": "2024-03-15T10:30:00Z"
}
```
```

### 4. Constraints

**Required**: Yes  
**Format**: Bulleted list

Document limitations, edge cases, and conditions where the skill should NOT be used. This helps prevent misuse and sets appropriate expectations. Include:

- **Input limitations**: What kinds of inputs are not supported
- **Scope boundaries**: What the skill explicitly does not cover
- **Quality conditions**: When output quality may be degraded
- **Dependencies**: External data or services required

**Example**:
```markdown
## Constraints

- **Data Requirements**: Requires access to reliable market research data; cannot generate accurate estimates for emerging markets with limited data
- **Time Horizon**: Most accurate for 1-3 year projections; less reliable for 5+ year forecasts
- **Market Maturity**: Best suited for established markets; may underestimate potential in rapidly evolving or nascent categories
- **Geographic Coverage**: Optimized for North America and Western Europe; other regions may require additional validation
- **Not a Substitute**: This skill provides a framework and initial estimates but should not replace comprehensive market research for critical business decisions
```

### 5. Invocation

**Required**: Yes  
**Format**: Concrete examples with expected outputs

Provide 2-3 complete examples showing how to invoke the skill and what to expect. Examples should:

- Cover common use cases
- Show different parameter combinations
- Include both successful and edge-case scenarios
- Display realistic output samples

**Example**:
```markdown
## Invocation

### Example 1: B2B SaaS Market Sizing

**Input**:
```json
{
  "target_market": "B2B SaaS - Project Management Tools",
  "geography": "North America",
  "product_type": "Software",
  "year": 2025
}
```

**Output**:
```json
{
  "market_analysis": {
    "tam": {
      "value": 8500000000,
      "unit": "USD",
      "confidence": "high"
    },
    "sam": {
      "value": 3400000000,
      "unit": "USD",
      "confidence": "high"
    },
    "som": {
      "value": 85000000,
      "unit": "USD",
      "confidence": "medium"
    }
  }
}
```

### Example 2: Global Healthcare Market

**Input**:
```json
{
  "target_market": "Digital Health Platforms",
  "geography": "Global",
  "year": 2024
}
```

**Output**:
```json
{
  "market_analysis": {
    "tam": {
      "value": 175000000000,
      "unit": "USD",
      "confidence": "medium"
    }
  },
  "warnings": [
    "Global market estimates have higher uncertainty",
    "Regional breakdowns recommended for accuracy"
  ]
}
```
```

## Optional Sections

Skills MAY include these additional sections:

### Metadata

Information about the skill itself:

```markdown
## Metadata

- **Version**: 1.2.0
- **Author**: Growth Strategy Team
- **Last Updated**: 2024-03-15
- **Status**: Stable
- **Tags**: market-research, strategy, growth
```

### Dependencies

External services, data sources, or other skills required:

```markdown
## Dependencies

- Market research database access (Gartner, Forrester, or equivalent)
- skills/data/statistical-validation (optional, for confidence intervals)
```

### Implementation Notes

Technical guidance for those implementing or extending the skill:

```markdown
## Implementation Notes

This skill uses a hybrid approach combining top-down market research with bottoms-up analysis. The confidence scores are calculated based on data recency and source reliability.
```

## Formatting Guidelines

1. **Use Markdown**: All skills must be written in clean, standard Markdown
2. **Be Consistent**: Follow the section order and naming exactly
3. **Be Specific**: Avoid vague descriptions; include concrete examples
4. **Be Concise**: Each section should be focused and scannable
5. **Use Code Blocks**: Format JSON, code, and structured data properly
6. **Link Related Skills**: Reference other skills when relevant

## Validation Checklist

Before submitting a skill, verify:

- [ ] All five required sections are present and complete
- [ ] Purpose clearly explains the skill's value
- [ ] All inputs are documented with types and constraints
- [ ] Output format includes a complete schema or example
- [ ] Constraints document limitations and edge cases
- [ ] At least 2 invocation examples are provided
- [ ] Markdown formatting is clean and renders correctly
- [ ] Examples use realistic data and scenarios

## Skill Naming Conventions

- Use lowercase with hyphens: `market-sizing.md`, not `MarketSizing.md`
- Be descriptive but concise: `code-review-checklist.md`, not `review.md`
- Avoid generic names: `sql-query-optimization.md`, not `optimization.md`
- Place in appropriate domain folder: `skills/growth/`, `skills/engineering/`, etc.

## Version Evolution

As skills evolve:

1. Update the version number in Metadata
2. Document breaking changes in the skill
3. Maintain backward compatibility when possible
4. Archive deprecated skills in a `deprecated/` folder

## Questions?

For questions about the specification or help creating a skill, please open an issue in the repository.
