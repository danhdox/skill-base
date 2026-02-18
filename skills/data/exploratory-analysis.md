# Exploratory Data Analysis

## Purpose

This skill provides a systematic framework for conducting initial exploratory data analysis (EDA) on a dataset. It encodes best practices from experienced data scientists to help teams quickly understand data characteristics, identify quality issues, discover patterns, and generate hypotheses. The skill produces a comprehensive data profile with visualizations, statistical summaries, and actionable insights that inform downstream modeling and analysis decisions.

## Inputs

| Name | Type | Required | Description | Constraints |
|------|------|----------|-------------|-------------|
| `dataset_name` | string | Yes | Identifier or name of the dataset | Non-empty string, max 100 chars |
| `data_location` | string | Yes | Path or URL to the dataset | Valid file path, URL, or database connection string |
| `file_format` | string | No | Format of the data file | Valid values: "csv", "json", "parquet", "excel", "sql", Default: "csv" |
| `sample_size` | number | No | Number of rows to analyze (for large datasets) | Range: 100-1000000, Default: 10000 |
| `target_variable` | string | No | Name of the target/outcome variable if known | Column name that exists in dataset |
| `analysis_depth` | string | No | Level of analysis detail | Valid values: "quick", "standard", "comprehensive", Default: "standard" |

## Output Format

```json
{
  "dataset_profile": {
    "name": "customer_transactions",
    "rows": 125000,
    "columns": 15,
    "memory_usage_mb": 45.2,
    "datetime_range": {
      "start": "2023-01-01",
      "end": "2024-03-15"
    }
  },
  "column_analysis": [
    {
      "name": "customer_id",
      "type": "integer",
      "unique_values": 8500,
      "missing_count": 0,
      "missing_percentage": 0.0,
      "summary_stats": {
        "mean": 45892.3,
        "median": 45123,
        "std": 12456.7,
        "min": 1001,
        "max": 99999
      },
      "recommended_actions": []
    },
    {
      "name": "transaction_amount",
      "type": "float",
      "unique_values": 45678,
      "missing_count": 342,
      "missing_percentage": 0.27,
      "summary_stats": {
        "mean": 156.78,
        "median": 89.50,
        "std": 234.56,
        "min": 0.01,
        "max": 9999.99
      },
      "distribution": "right_skewed",
      "outliers_detected": 234,
      "outlier_percentage": 0.19,
      "recommended_actions": [
        "Investigate high-value outliers above $5000",
        "Consider log transformation for modeling"
      ]
    }
  ],
  "data_quality": {
    "overall_score": 82,
    "issues": [
      {
        "severity": "medium",
        "type": "missing_values",
        "description": "3 columns have >1% missing values",
        "affected_columns": ["transaction_amount", "customer_email", "shipping_address"]
      },
      {
        "severity": "low",
        "type": "potential_duplicates",
        "description": "Found 45 potential duplicate rows",
        "recommendation": "Review duplicate detection criteria"
      }
    ],
    "completeness": 97.5,
    "consistency": 89.2,
    "validity": 95.8
  },
  "correlations": {
    "high_correlations": [
      {
        "variable_1": "transaction_amount",
        "variable_2": "customer_lifetime_value",
        "correlation": 0.87,
        "type": "positive"
      }
    ],
    "target_correlations": [
      {
        "variable": "days_since_last_purchase",
        "correlation": -0.62,
        "interpretation": "Strong negative correlation with churn"
      }
    ]
  },
  "insights": [
    "Transaction amounts show strong right skew - median ($89.50) much lower than mean ($156.78)",
    "Customer tenure strongly predicts transaction frequency (correlation: 0.74)",
    "Missing values appear to be systematic - concentrated in specific time periods",
    "Potential data quality issue: 15% of email addresses fail validation"
  ],
  "recommendations": [
    "Impute missing transaction amounts using customer segment median",
    "Create log-transformed features for skewed numeric variables",
    "Investigate cause of missing values in Q2 2023 time period",
    "Add email validation step in data pipeline"
  ],
  "visualizations": [
    {
      "type": "distribution",
      "variables": ["transaction_amount"],
      "path": "/tmp/eda/transaction_amount_dist.png"
    },
    {
      "type": "correlation_matrix",
      "path": "/tmp/eda/correlation_heatmap.png"
    },
    {
      "type": "missing_data_pattern",
      "path": "/tmp/eda/missing_data.png"
    }
  ],
  "timestamp": "2024-03-15T10:30:00Z",
  "version": "1.0.0"
}
```

## Constraints

- **Data Size Limits**: Optimized for datasets up to 10 million rows; larger datasets should be sampled or processed in distributed environment
- **File Format Support**: Handles common tabular formats; unstructured data (images, text, audio) requires specialized analysis skills
- **Computational Resources**: Memory-intensive for wide datasets (>1000 columns); may require sampling or column selection
- **Statistical Assumptions**: Correlation and distribution analysis assumes numeric or ordinal data; categorical analysis is separate
- **Visualization Limits**: Generates up to 20 standard visualizations; custom plots require additional specification
- **Domain Context**: Cannot interpret business meaning of variables without additional context; focuses on statistical properties
- **Not a Substitute**: Provides initial exploration only; does not replace domain expertise, hypothesis testing, or causal analysis
- **Privacy Considerations**: Does not automatically detect or mask PII; user responsible for data privacy compliance

## Invocation

### Example 1: E-commerce Customer Transactions

**Input**:
```json
{
  "dataset_name": "customer_transactions_2024",
  "data_location": "/data/ecommerce/transactions.csv",
  "file_format": "csv",
  "sample_size": 50000,
  "target_variable": "will_churn",
  "analysis_depth": "comprehensive"
}
```

**Output**:
```json
{
  "dataset_profile": {
    "name": "customer_transactions_2024",
    "rows": 50000,
    "columns": 18,
    "memory_usage_mb": 22.5,
    "datetime_range": {
      "start": "2024-01-01",
      "end": "2024-03-15"
    }
  },
  "column_analysis": [
    {
      "name": "customer_id",
      "type": "integer",
      "unique_values": 12456,
      "missing_count": 0,
      "missing_percentage": 0.0,
      "cardinality": "high",
      "recommended_actions": ["Good candidate for grouping/aggregation"]
    },
    {
      "name": "will_churn",
      "type": "boolean",
      "unique_values": 2,
      "missing_count": 0,
      "value_counts": {
        "false": 42300,
        "true": 7700
      },
      "class_imbalance_ratio": 5.49,
      "recommended_actions": [
        "Target variable shows class imbalance (15.4% positive class)",
        "Consider SMOTE or class weights for modeling"
      ]
    },
    {
      "name": "transaction_amount",
      "type": "float",
      "missing_count": 125,
      "missing_percentage": 0.25,
      "summary_stats": {
        "mean": 156.78,
        "median": 89.50,
        "std": 234.56,
        "min": 0.01,
        "max": 9999.99,
        "q25": 45.20,
        "q75": 178.90
      },
      "distribution": "right_skewed",
      "skewness": 3.45,
      "kurtosis": 18.23,
      "outliers_detected": 234,
      "recommended_actions": [
        "Apply log transformation to reduce skewness",
        "Investigate outliers >$5000"
      ]
    }
  ],
  "data_quality": {
    "overall_score": 86,
    "issues": [
      {
        "severity": "high",
        "type": "class_imbalance",
        "description": "Target variable has 5.5:1 class imbalance",
        "recommendation": "Use stratified sampling and appropriate metrics (F1, AUC-ROC)"
      },
      {
        "severity": "medium",
        "type": "missing_values",
        "description": "Transaction_amount has 125 missing values (0.25%)",
        "recommendation": "Missing pattern appears random - safe to impute"
      }
    ],
    "completeness": 98.9,
    "consistency": 92.3,
    "validity": 96.1
  },
  "correlations": {
    "high_correlations": [
      {
        "variable_1": "total_purchases",
        "variable_2": "customer_lifetime_value",
        "correlation": 0.94,
        "type": "positive",
        "note": "Expected strong correlation - consider removing one for multicollinearity"
      }
    ],
    "target_correlations": [
      {
        "variable": "days_since_last_purchase",
        "correlation": 0.68,
        "interpretation": "Strong positive correlation with churn"
      },
      {
        "variable": "customer_satisfaction_score",
        "correlation": -0.52,
        "interpretation": "Moderate negative correlation with churn"
      },
      {
        "variable": "number_of_support_tickets",
        "correlation": 0.41,
        "interpretation": "Moderate positive correlation with churn"
      }
    ]
  },
  "insights": [
    "Churn rate is 15.4% - consistent with industry benchmarks for e-commerce",
    "Days since last purchase is strongest predictor (0.68 correlation)",
    "High multicollinearity between total_purchases and customer_lifetime_value",
    "Transaction amounts are heavily right-skewed - log transformation recommended",
    "Support tickets show interesting pattern - customers with 0 or >5 tickets more likely to churn"
  ],
  "recommendations": [
    "Focus feature engineering on recency metrics (days_since_last_purchase)",
    "Handle class imbalance with SMOTE or class weights",
    "Apply log transformation to transaction_amount",
    "Remove customer_lifetime_value to reduce multicollinearity",
    "Create categorical bins for support_tickets (0, 1-2, 3-5, 5+)",
    "Investigate non-linear relationships with polynomial features"
  ],
  "visualizations": [
    {
      "type": "target_distribution",
      "description": "Churn class distribution",
      "path": "/tmp/eda/churn_distribution.png"
    },
    {
      "type": "correlation_matrix",
      "description": "Feature correlations heatmap",
      "path": "/tmp/eda/correlation_heatmap.png"
    },
    {
      "type": "distribution_grid",
      "description": "Numeric features distributions",
      "path": "/tmp/eda/feature_distributions.png"
    },
    {
      "type": "box_plot",
      "description": "Transaction amount by churn status",
      "path": "/tmp/eda/amount_by_churn.png"
    }
  ],
  "next_steps": [
    "Feature engineering based on insights",
    "Train baseline models with cross-validation",
    "Perform feature importance analysis",
    "Investigate non-linear relationships"
  ],
  "timestamp": "2024-03-15T14:20:00Z",
  "version": "1.0.0"
}
```

### Example 2: Quick Analysis of Small Dataset

**Input**:
```json
{
  "dataset_name": "sales_leads",
  "data_location": "/data/leads.csv",
  "analysis_depth": "quick"
}
```

**Output**:
```json
{
  "dataset_profile": {
    "name": "sales_leads",
    "rows": 1500,
    "columns": 8,
    "memory_usage_mb": 0.5
  },
  "column_analysis": [
    {
      "name": "lead_source",
      "type": "string",
      "unique_values": 6,
      "missing_count": 12,
      "top_values": {
        "Website": 650,
        "Referral": 420,
        "Cold Call": 230
      }
    },
    {
      "name": "lead_score",
      "type": "integer",
      "missing_count": 0,
      "summary_stats": {
        "mean": 67.5,
        "median": 72,
        "min": 10,
        "max": 100
      }
    }
  ],
  "data_quality": {
    "overall_score": 94,
    "issues": [
      {
        "severity": "low",
        "type": "missing_values",
        "description": "12 missing lead_source values (0.8%)"
      }
    ]
  },
  "insights": [
    "Dataset is small and clean - suitable for quick analysis",
    "Lead scores appear normally distributed",
    "Website is dominant lead source (43%)"
  ],
  "recommendations": [
    "Dataset is analysis-ready",
    "Consider collecting more data for robust modeling"
  ],
  "timestamp": "2024-03-15T14:35:00Z",
  "version": "1.0.0"
}
```

## Metadata

- **Version**: 1.0.0
- **Domain**: Data
- **Author**: Data Science Team
- **Last Updated**: 2024-03-15
- **Status**: Stable
- **Tags**: data-analysis, eda, data-profiling, statistics
- **Estimated Runtime**: 30-120 seconds (depending on analysis_depth and dataset size)
- **Dependencies**: pandas, numpy, matplotlib, seaborn (or equivalent data science stack)
