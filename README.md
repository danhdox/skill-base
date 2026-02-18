# skill-base

A curated registry of high-leverage, agent-callable skills. Structured playbooks that encode judgment, not just prompts. Designed for LLM workflows, slash-command invocation, and composable expertise across growth, engineering, data, legal, and onchain domains.

## What is a Skill?

A **skill** is a structured, reusable package of expertise that agents (human or AI) can invoke to perform specific tasks. Unlike simple prompts or scripts, skills encode:

- **Judgment**: Domain-specific decision-making criteria and best practices
- **Structured Outputs**: Consistent, parseable formats that can be composed into workflows
- **Context Awareness**: Clear boundaries on when to use (and when not to use) the skill

### Key Characteristics

1. **Encoded Judgment**: Skills capture expert decision-making patterns, not just procedural steps
2. **Structured Outputs**: Results follow defined schemas for downstream consumption
3. **Composable**: Skills can be chained together to build complex workflows
4. **Self-Documenting**: Each skill includes its purpose, inputs, constraints, and usage examples

### Invocation Examples

Skills in this repository are designed to be invoked in multiple ways:

**Direct Agent Call**:
```
@agent invoke skill:growth/market-sizing --target-market "B2B SaaS" --geography "North America"
```

**CLI/Slash Command**:
```
/skill growth/market-sizing --target-market="B2B SaaS"
```

**Programmatic**:
```python
from skill_base import invoke_skill

result = invoke_skill(
    "growth/market-sizing",
    params={"target_market": "B2B SaaS", "geography": "North America"}
)
```

**Natural Language**:
```
"Run the market sizing skill for the B2B SaaS market in North America"
```

## Repository Structure

```
skill-base/
├── skills/           # Core skill library organized by domain
│   ├── growth/       # Growth and GTM skills
│   ├── engineering/  # Software development and architecture
│   ├── data/         # Data analysis and modeling
│   ├── legal/        # Legal review and compliance
│   └── onchain/      # Blockchain and web3 operations
├── external/         # Links to external skill registries
└── SKILL_SPEC.md     # Specification for creating new skills
```

## Getting Started

### Using Skills

1. Browse the `skills/` directory to find relevant skills for your domain
2. Read the skill's documentation to understand its purpose and inputs
3. Invoke the skill using your preferred method (agent, CLI, or programmatic)
4. Process the structured output in your workflow

### Contributing Skills

1. Review the [SKILL_SPEC.md](SKILL_SPEC.md) specification
2. Create your skill following the required format
3. Place it in the appropriate domain folder under `skills/`
4. Include comprehensive examples and edge case handling
5. Submit a pull request with your skill and tests

## Example Skills

This repository includes example skills demonstrating the specification:

- **growth/market-sizing.md** - TAM/SAM/SOM calculation framework
- **engineering/code-review-checklist.md** - Structured code review process
- **data/exploratory-analysis.md** - Data profiling and initial analysis
- **legal/contract-risk-assessment.md** - Contract review framework
- **onchain/smart-contract-audit.md** - Blockchain smart contract security review

## Philosophy

Skills represent **encoded expertise** rather than simple automation. They:

- Capture decision-making patterns from experienced practitioners
- Provide guardrails and constraints to prevent common mistakes
- Generate outputs that can feed into other skills or systems
- Evolve based on real-world usage and feedback

## License

This repository is open-source and available under the MIT License. Contributions are welcome!
