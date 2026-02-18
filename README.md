# skill-base

Open-source skills for AI agents.

`skill-base` is a reusable library of structured skills that work across Codex, Claude, and other agent runtimes. Skills are grouped by domain, written in a consistent format, and designed so teams can copy them directly into their own projects.

## Why This Repository

- Build reliable agent workflows with reusable, reviewable skill files.
- Keep skill outputs predictable with a shared contract.
- Help teams quickly skim, copy, and compose domain-specific skills.

## Quick Start

### Option 1: Copy one skill

```bash
cp skills/engineering/code-review-checklist.md /path/to/your-project/skills/
```

### Option 2: Copy a full domain

```bash
cp -R skills/security /path/to/your-project/skills/
```

### Option 3: Clone and curate

```bash
git clone https://github.com/danhdox/skill-base.git
```

## Use With Any Agent

You can invoke these skills with:

- Codex-style workflows
- Claude-style workflows
- Internal agent frameworks and prompt runners
- Manual human-in-the-loop review flows

## Repository Layout

```text
skill-base/
├── skills/
│   ├── catalog.yaml
│   ├── engineering/
│   ├── data/
│   ├── growth/
│   ├── legal/
│   ├── onchain/
│   ├── product/
│   ├── security/
│   ├── ops/
│   ├── finance/
│   └── design/
├── scripts/
│   ├── validate_skills.py
│   └── sync_readme_catalog.py
├── SKILL_SPEC.md
└── .github/workflows/validate.yml
```

## Skill Contract

All skills follow the required specification in [`SKILL_SPEC.md`](SKILL_SPEC.md).

## Full Skill Catalog

The table below is generated from [`skills/catalog.yaml`](skills/catalog.yaml).

<!-- SKILL_CATALOG_START -->

| Domain | Skill Type | Skill | Summary | Path |
|---|---|---|---|---|
| data | audit | [Data Quality Audit](skills/data/data-quality-audit.md) | Audits data assets for completeness, validity, and operational trustworthiness. | `skills/data/data-quality-audit.md` |
| data | planning | [Experiment Design and Power Analysis](skills/data/experiment-design-power-analysis.md) | Designs experiments with measurable outcomes and statistically valid sample sizing. | `skills/data/experiment-design-power-analysis.md` |
| data | analysis | [Exploratory Data Analysis](skills/data/exploratory-analysis.md) | Profiles datasets to surface distributions, quality issues, and early hypotheses. | `skills/data/exploratory-analysis.md` |
| design | audit | [Accessibility Audit (WCAG)](skills/design/accessibility-audit-wcag.md) | Reviews interfaces against WCAG criteria with prioritized remediation steps. | `skills/design/accessibility-audit-wcag.md` |
| design | audit | [Design System Audit](skills/design/design-system-audit.md) | Audits design system consistency, coverage, and adoption quality. | `skills/design/design-system-audit.md` |
| design | evaluation | [UX Heuristic Evaluation](skills/design/ux-heuristic-evaluation.md) | Evaluates product UX against established usability heuristics. | `skills/design/ux-heuristic-evaluation.md` |
| engineering | review | [API Design Review](skills/engineering/api-design-review.md) | Evaluates API design for consistency, usability, and long-term maintainability. | `skills/engineering/api-design-review.md` |
| engineering | checklist | [Code Review Checklist](skills/engineering/code-review-checklist.md) | Structured checklist for reviewing code quality, correctness, and delivery risk. | `skills/engineering/code-review-checklist.md` |
| engineering | analysis | [Incident Postmortem Analysis](skills/engineering/incident-postmortem-analysis.md) | Turns incident timelines into root causes, lessons, and prevention actions. | `skills/engineering/incident-postmortem-analysis.md` |
| finance | forecasting | [Cash Flow Forecast Scenarios](skills/finance/cash-flow-forecast-scenarios.md) | Builds scenario-based cash flow forecasts for planning and risk control. | `skills/finance/cash-flow-forecast-scenarios.md` |
| finance | validation | [Financial Model Sanity Check](skills/finance/financial-model-sanity-check.md) | Validates financial model assumptions, formulas, and internal consistency. | `skills/finance/financial-model-sanity-check.md` |
| finance | analysis | [Unit Economics Analysis](skills/finance/unit-economics-analysis.md) | Calculates unit economics to identify margin drivers and growth constraints. | `skills/finance/unit-economics-analysis.md` |
| growth | planning | [Go-to-Market Plan](skills/growth/go-to-market-plan.md) | Builds launch strategy, channel sequencing, and execution milestones. | `skills/growth/go-to-market-plan.md` |
| growth | analysis | [Market Sizing](skills/growth/market-sizing.md) | Estimates TAM, SAM, and SOM with explicit assumptions and confidence ranges. | `skills/growth/market-sizing.md` |
| growth | evaluation | [Pricing Strategy Evaluator](skills/growth/pricing-strategy-evaluator.md) | Assesses pricing approaches against value capture and growth objectives. | `skills/growth/pricing-strategy-evaluator.md` |
| legal | assessment | [Contract Risk Assessment](skills/legal/contract-risk-assessment.md) | Identifies legal risk in contracts and recommends negotiation priorities. | `skills/legal/contract-risk-assessment.md` |
| legal | compliance | [Open Source License Compliance Check](skills/legal/open-source-license-compliance-check.md) | Checks OSS dependency licenses for obligations, conflicts, and remediation. | `skills/legal/open-source-license-compliance-check.md` |
| legal | analysis | [Privacy Policy Gap Analysis](skills/legal/privacy-policy-gap-analysis.md) | Finds policy coverage gaps versus privacy obligations and operations. | `skills/legal/privacy-policy-gap-analysis.md` |
| onchain | review | [Protocol Governance Design Review](skills/onchain/protocol-governance-design-review.md) | Evaluates protocol governance mechanics for resilience and capture resistance. | `skills/onchain/protocol-governance-design-review.md` |
| onchain | audit | [Smart Contract Security Audit](skills/onchain/smart-contract-audit.md) | Reviews smart contract logic for vulnerabilities and deployment risk. | `skills/onchain/smart-contract-audit.md` |
| onchain | review | [Tokenomics Risk Review](skills/onchain/tokenomics-risk-review.md) | Analyzes token incentive design, supply dynamics, and governance risks. | `skills/onchain/tokenomics-risk-review.md` |
| ops | triage | [Incident Response Triage](skills/ops/incident-response-triage.md) | Classifies incidents quickly and triggers coordinated response workflows. | `skills/ops/incident-response-triage.md` |
| ops | documentation | [Runbook Creation](skills/ops/runbook-creation.md) | Transforms operational procedures into executable runbooks. | `skills/ops/runbook-creation.md` |
| ops | planning | [SLO Planning](skills/ops/slo-planning.md) | Defines SLOs, SLIs, and error budgets aligned to user impact. | `skills/ops/slo-planning.md` |
| product | prioritization | [Feature Prioritization (RICE)](skills/product/feature-prioritization-rice.md) | Ranks feature candidates using RICE with transparent scoring assumptions. | `skills/product/feature-prioritization-rice.md` |
| product | planning | [Product Requirements Brief](skills/product/product-requirements-brief.md) | Converts product intent into a clear, testable requirements brief. | `skills/product/product-requirements-brief.md` |
| product | planning | [User Story Mapping](skills/product/user-story-mapping.md) | Maps user journeys into release slices and implementation-ready stories. | `skills/product/user-story-mapping.md` |
| security | review | [Authentication Flow Review](skills/security/authentication-flow-review.md) | Assesses auth and session flows for security, UX, and reliability gaps. | `skills/security/authentication-flow-review.md` |
| security | assessment | [Third-Party Vendor Security Review](skills/security/third-party-vendor-security-review.md) | Evaluates third-party vendors for security posture and integration risk. | `skills/security/third-party-vendor-security-review.md` |
| security | modeling | [Threat Modeling (STRIDE)](skills/security/threat-modeling-stride.md) | Identifies and prioritizes system threats using STRIDE methodology. | `skills/security/threat-modeling-stride.md` |

<!-- SKILL_CATALOG_END -->

## Validation

Run local checks before publishing or opening a PR:

```bash
python3 scripts/validate_skills.py
python3 scripts/sync_readme_catalog.py --check
```

## Contributing and Governance

- Contribution guide: [`CONTRIBUTING.md`](CONTRIBUTING.md)
- Code of conduct: [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md)
- Security policy: [`SECURITY.md`](SECURITY.md)
- Changelog: [`CHANGELOG.md`](CHANGELOG.md)

## License

MIT. See [`LICENSE`](LICENSE).
