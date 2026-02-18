# Contributing to skill-base

Thanks for contributing skills for agent workflows.

## Before You Start

1. Read [`SKILL_SPEC.md`](SKILL_SPEC.md).
2. Check the existing catalog in [`skills/catalog.yaml`](skills/catalog.yaml) to avoid duplicates.
3. Open an issue for large additions or domain-level changes.

## Adding or Updating a Skill

1. Place skill files under `skills/<domain>/<skill-name>.md`.
2. Follow the required section order from `SKILL_SPEC.md`:
   - `## Purpose`
   - `## Inputs`
   - `## Output Format`
   - `## Constraints`
   - `## Invocation`
3. Include at least two realistic examples under `## Invocation`.
4. Add or update the matching entry in `skills/catalog.yaml`.

## Local Validation

Run these commands before opening a pull request:

```bash
python3 scripts/validate_skills.py
python3 scripts/sync_readme_catalog.py
python3 scripts/sync_readme_catalog.py --check
```

## Pull Request Checklist

- [ ] Skill content follows `SKILL_SPEC.md`.
- [ ] `skills/catalog.yaml` includes every changed/added skill.
- [ ] `README.md` catalog is synchronized.
- [ ] Validation script passes locally.
- [ ] Scope is focused and unrelated files are not modified.

## Contribution Standards

- Keep changes minimal and reversible.
- Use clear, descriptive commit messages.
- Preserve existing style and formatting conventions.
- Add source attribution when external frameworks or standards influenced a skill.

## Need Help?

Open a discussion or issue with:
- the skill/domain you are proposing,
- the user workflow it supports,
- expected output shape.
