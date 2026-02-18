# skill-base {{VERSION}}

## Summary

Public release of `skill-base` as a cross-agent, open-source skill library.

## Highlights

- 30 skills across 10 domains
- Machine-readable catalog in `skills/catalog.yaml`
- Validation automation and README sync checks
- OSS governance and contribution docs

## Domain Coverage

- engineering: 3
- data: 3
- growth: 3
- legal: 3
- onchain: 3
- product: 3
- security: 3
- ops: 3
- finance: 3
- design: 3

## Included Artifacts

- `README.md` with full per-skill skim table
- `SKILL_SPEC.md`
- `skills/` catalog and domain folders
- `scripts/validate_skills.py`
- `scripts/sync_readme_catalog.py`

## Validation Checklist

- [ ] CI validation workflow passed on release commit
- [ ] `python3 scripts/validate_skills.py` passed locally
- [ ] `python3 scripts/sync_readme_catalog.py --check` passed locally

## Upgrade Notes

No breaking API changes. Consumers can continue copying individual skill files directly.
