# Market Sizing

## Purpose

This skill provides a structured framework for calculating Total Addressable Market (TAM), Serviceable Addressable Market (SAM), and Serviceable Obtainable Market (SOM) for a given business opportunity. It encodes best practices from growth strategy consulting and helps teams make data-driven decisions about market opportunities. The skill combines top-down industry analysis with bottoms-up validation to produce realistic market estimates with confidence assessments.

## Inputs

| Name | Type | Required | Description | Constraints |
|------|------|----------|-------------|-------------|
| `target_market` | string | Yes | Description of the target market or industry segment | Non-empty string, max 200 chars |
| `geography` | string | Yes | Geographic region for analysis | Valid values: "North America", "Europe", "Asia Pacific", "Latin America", "Global" |
| `product_type` | string | No | Type of product or service offering | Default: "Software" |
| `year` | number | No | Target year for market size estimation | Range: 2020-2030, Default: current year |
| `customer_segment` | string | No | Specific customer segment (e.g., "Enterprise", "SMB") | Default: "All segments" |

## Output Format

```json
{
  "market_analysis": {
    "tam": {
      "value": 450000000000,
      "unit": "USD",
      "confidence": "medium",
      "methodology": "Top-down industry analysis using market research reports",
      "growth_rate": 18.5
    },
    "sam": {
      "value": 45000000000,
      "unit": "USD",
      "confidence": "medium",
      "methodology": "Geographic and segment filtering applied to TAM",
      "market_share_potential": 10.0
    },
    "som": {
      "value": 450000000,
      "unit": "USD",
      "confidence": "high",
      "methodology": "Bottoms-up sales capacity and conversion model",
      "achievable_percentage": 1.0
    }
  },
  "assumptions": [
    "Global SaaS market growing at 18.5% CAGR through 2025",
    "Target segment represents 10% of total addressable market",
    "Sales team can realistically capture 1% of SAM in year one"
  ],
  "data_sources": [
    "Gartner Market Analysis 2024",
    "IDC Forecast Report",
    "Company historical sales data"
  ],
  "risks": [
    "Market estimates sensitive to economic conditions",
    "Competition may impact achievable market share"
  ],
  "timestamp": "2024-03-15T10:30:00Z",
  "version": "1.0.0"
}
```

## Constraints

- **Data Requirements**: Requires access to reliable market research data (Gartner, Forrester, IDC, or equivalent); cannot generate accurate estimates for emerging markets with limited published data
- **Time Horizon**: Most accurate for 1-3 year projections; reliability decreases significantly for 5+ year forecasts due to market uncertainty
- **Market Maturity**: Best suited for established markets with historical data; may underestimate potential in rapidly evolving or nascent categories
- **Geographic Coverage**: Optimized for North America and Western Europe where data is most comprehensive; other regions may require additional validation and local expertise
- **Segment Specificity**: More accurate for broad market categories; highly specific niche markets may require custom research
- **Not a Substitute**: This skill provides a framework and initial estimates but should not replace comprehensive market research for critical business decisions or fundraising
- **Update Frequency**: Market data becomes stale quickly; estimates should be refreshed quarterly for fast-moving markets

## Invocation

### Example 1: B2B SaaS Project Management Tools

**Input**:
```json
{
  "target_market": "B2B SaaS - Project Management Tools",
  "geography": "North America",
  "product_type": "Software",
  "year": 2025,
  "customer_segment": "Enterprise"
}
```

**Output**:
```json
{
  "market_analysis": {
    "tam": {
      "value": 8500000000,
      "unit": "USD",
      "confidence": "high",
      "methodology": "Top-down analysis of project management software market",
      "growth_rate": 12.3
    },
    "sam": {
      "value": 3400000000,
      "unit": "USD",
      "confidence": "high",
      "methodology": "Filtered to North America enterprise segment",
      "market_share_potential": 40.0
    },
    "som": {
      "value": 85000000,
      "unit": "USD",
      "confidence": "medium",
      "methodology": "Based on sales team capacity and conversion rates",
      "achievable_percentage": 2.5
    }
  },
  "assumptions": [
    "Project management software market growing at 12.3% annually",
    "Enterprise segment in North America represents 40% of global market",
    "Realistic capture of 2.5% of SAM based on competitive landscape"
  ],
  "data_sources": [
    "Gartner Magic Quadrant for Project Management 2024",
    "Company competitive analysis"
  ],
  "risks": [
    "Established competitors (Asana, Monday.com) have strong market position",
    "Economic downturn could reduce enterprise software spending"
  ],
  "timestamp": "2024-03-15T14:22:00Z",
  "version": "1.0.0"
}
```

### Example 2: Global Digital Health Platforms

**Input**:
```json
{
  "target_market": "Digital Health Platforms - Telemedicine",
  "geography": "Global",
  "product_type": "Platform",
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
      "confidence": "medium",
      "methodology": "Global telemedicine market size from healthcare research",
      "growth_rate": 24.8
    },
    "sam": {
      "value": 52500000000,
      "unit": "USD",
      "confidence": "medium",
      "methodology": "Filtered to digital-first platform segment",
      "market_share_potential": 30.0
    },
    "som": {
      "value": 262500000,
      "unit": "USD",
      "confidence": "low",
      "methodology": "Conservative estimate due to regulatory complexity",
      "achievable_percentage": 0.5
    }
  },
  "assumptions": [
    "Telemedicine adoption accelerated by 5 years due to pandemic",
    "Digital platforms represent 30% of total telemedicine market",
    "Regulatory barriers limit addressable market in some regions"
  ],
  "data_sources": [
    "WHO Digital Health Report 2024",
    "McKinsey Healthcare Analysis"
  ],
  "risks": [
    "Regulatory requirements vary significantly by country",
    "Reimbursement policies still evolving in many markets"
  ],
  "warnings": [
    "Global market estimates have higher uncertainty due to regional variations",
    "Healthcare regulations create significant market entry barriers"
  ],
  "timestamp": "2024-03-15T14:30:00Z",
  "version": "1.0.0"
}
```

### Example 3: Emerging Market Edge Case

**Input**:
```json
{
  "target_market": "AI-Powered Quantum Computing Services",
  "geography": "Global",
  "year": 2026
}
```

**Output**:
```json
{
  "market_analysis": {
    "tam": {
      "value": 5000000000,
      "unit": "USD",
      "confidence": "low",
      "methodology": "Analyst projections with high uncertainty",
      "growth_rate": 45.0
    },
    "sam": {
      "value": null,
      "unit": "USD",
      "confidence": "insufficient_data",
      "methodology": "Unable to determine serviceable market"
    },
    "som": {
      "value": null,
      "unit": "USD",
      "confidence": "insufficient_data",
      "methodology": "Market too nascent for obtainable market estimate"
    }
  },
  "assumptions": [
    "Quantum computing market projections based on limited historical data"
  ],
  "data_sources": [
    "Various analyst projections with wide variance"
  ],
  "warnings": [
    "Market is highly nascent with limited reliable data",
    "Estimates should be treated as directional only",
    "Recommend comprehensive custom market research"
  ],
  "timestamp": "2024-03-15T14:45:00Z",
  "version": "1.0.0"
}
```

## Metadata

- **Version**: 1.0.0
- **Domain**: Growth
- **Author**: Growth Strategy Team
- **Last Updated**: 2024-03-15
- **Status**: Stable
- **Tags**: market-research, strategy, growth, tam, sam, som
- **Estimated Runtime**: 30-60 seconds
