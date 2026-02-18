#!/usr/bin/env python3
"""Sync README skill catalog table from skills/catalog.yaml."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

START_MARKER = "<!-- SKILL_CATALOG_START -->"
END_MARKER = "<!-- SKILL_CATALOG_END -->"


def load_catalog(path: Path) -> dict[str, Any]:
    raw = path.read_text(encoding="utf-8")
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(
            "skills/catalog.yaml must be valid JSON-formatted YAML for this script"
        ) from exc
    if not isinstance(data, dict):
        raise ValueError("Catalog root must be an object")
    if not isinstance(data.get("skills"), list):
        raise ValueError("Catalog must contain a 'skills' list")
    return data


def build_table(skills: list[dict[str, Any]]) -> str:
    sorted_skills = sorted(skills, key=lambda s: (s["domain"], s["title"]))
    lines = [
        "| Domain | Skill Type | Skill | Summary | Path |",
        "|---|---|---|---|---|",
    ]
    for skill in sorted_skills:
        domain = skill["domain"]
        skill_type = skill["skill_type"]
        title = skill["title"]
        summary = skill["summary"]
        path = skill["path"]
        lines.append(
            f"| {domain} | {skill_type} | [{title}]({path}) | {summary} | `{path}` |"
        )
    return "\n".join(lines)


def sync_readme(readme_path: Path, table: str, check: bool) -> int:
    readme = readme_path.read_text(encoding="utf-8")
    start = readme.find(START_MARKER)
    end = readme.find(END_MARKER)

    if start == -1 or end == -1 or end < start:
        raise ValueError(
            f"README must contain ordered markers: {START_MARKER} and {END_MARKER}"
        )

    start_content = start + len(START_MARKER)
    before = readme[:start_content]
    after = readme[end:]
    updated = f"{before}\n\n{table}\n\n{after}"

    if check:
        if readme != updated:
            print("README catalog is out of sync. Run scripts/sync_readme_catalog.py")
            return 1
        print("README catalog is up to date.")
        return 0

    if readme != updated:
        readme_path.write_text(updated, encoding="utf-8")
        print("README catalog updated.")
    else:
        print("README catalog already up to date.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync README skill catalog table")
    parser.add_argument(
        "--repo-root",
        default=Path(__file__).resolve().parents[1],
        type=Path,
        help="Repository root path",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check mode: exit non-zero if README is out of date",
    )
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    catalog = load_catalog(repo_root / "skills" / "catalog.yaml")
    table = build_table(catalog["skills"])

    return sync_readme(repo_root / "README.md", table, args.check)


if __name__ == "__main__":
    sys.exit(main())
