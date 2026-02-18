#!/usr/bin/env python3
"""Validate skill files, catalog integrity, and core docs links."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

REQUIRED_SECTIONS = [
    "Purpose",
    "Inputs",
    "Output Format",
    "Constraints",
    "Invocation",
]
REQUIRED_CATALOG_FIELDS = {
    "id",
    "domain",
    "skill_type",
    "title",
    "path",
    "summary",
    "status",
    "agent_compatibility",
}
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def load_catalog(path: Path) -> dict[str, Any]:
    raw = path.read_text(encoding="utf-8")
    try:
        data = json.loads(raw)
        if isinstance(data, dict):
            return data
    except json.JSONDecodeError:
        pass

    try:
        import yaml  # type: ignore
    except Exception as exc:  # pragma: no cover
        raise ValueError(
            "catalog is not valid JSON and PyYAML is unavailable for YAML parsing"
        ) from exc

    loaded = yaml.safe_load(raw)
    if not isinstance(loaded, dict):
        raise ValueError("catalog root must be an object")
    return loaded


def parse_sections(markdown: str) -> list[str]:
    sections: list[str] = []
    for line in markdown.splitlines():
        match = re.match(r"^##\s+(.+?)\s*$", line)
        if match:
            sections.append(match.group(1))
    return sections


def validate_skill_file(path: Path, errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or not lines[0].startswith("# "):
        errors.append(f"{path}: missing top-level title")

    sections = parse_sections(text)
    indices: list[int] = []
    for section in REQUIRED_SECTIONS:
        if section not in sections:
            errors.append(f"{path}: missing required section '## {section}'")
            continue
        indices.append(sections.index(section))
    if len(indices) == len(REQUIRED_SECTIONS) and indices != sorted(indices):
        errors.append(
            f"{path}: required sections are not in spec order ({', '.join(REQUIRED_SECTIONS)})"
        )

    example_count = len(re.findall(r"^###\s+Example", text, flags=re.MULTILINE))
    if example_count < 2:
        errors.append(f"{path}: expected at least 2 invocation examples, found {example_count}")


def validate_catalog(repo_root: Path, catalog_path: Path, errors: list[str]) -> None:
    data = load_catalog(catalog_path)
    skills = data.get("skills")
    if not isinstance(skills, list):
        errors.append(f"{catalog_path}: top-level 'skills' must be a list")
        return

    ids_seen: set[str] = set()
    paths_seen: set[str] = set()

    for idx, item in enumerate(skills):
        prefix = f"{catalog_path}: skills[{idx}]"
        if not isinstance(item, dict):
            errors.append(f"{prefix} must be an object")
            continue

        missing = REQUIRED_CATALOG_FIELDS - set(item.keys())
        if missing:
            errors.append(f"{prefix} missing fields: {', '.join(sorted(missing))}")
            continue

        skill_id = item["id"]
        domain = item["domain"]
        rel_path = item["path"]
        compatibility = item["agent_compatibility"]

        if not isinstance(skill_id, str) or "/" not in skill_id:
            errors.append(f"{prefix}.id must be '<domain>/<slug>'")
        elif skill_id in ids_seen:
            errors.append(f"{prefix}.id is duplicated: {skill_id}")
        else:
            ids_seen.add(skill_id)

        if not isinstance(domain, str) or not domain:
            errors.append(f"{prefix}.domain must be a non-empty string")

        if not isinstance(rel_path, str) or not rel_path:
            errors.append(f"{prefix}.path must be a non-empty string")
            continue

        if rel_path in paths_seen:
            errors.append(f"{prefix}.path is duplicated: {rel_path}")
        else:
            paths_seen.add(rel_path)

        full_path = repo_root / rel_path
        if not full_path.exists():
            errors.append(f"{prefix}.path does not exist: {rel_path}")
            continue

        expected_domain = full_path.parent.name
        expected_slug = full_path.stem
        expected_id = f"{expected_domain}/{expected_slug}"
        if skill_id != expected_id:
            errors.append(f"{prefix}.id '{skill_id}' does not match path '{expected_id}'")
        if domain != expected_domain:
            errors.append(
                f"{prefix}.domain '{domain}' does not match path domain '{expected_domain}'"
            )

        if not isinstance(compatibility, list) or not compatibility:
            errors.append(f"{prefix}.agent_compatibility must be a non-empty list")

    skill_paths = {
        p.relative_to(repo_root).as_posix()
        for p in sorted((repo_root / "skills").glob("*/*.md"))
    }
    missing_paths = sorted(skill_paths - paths_seen)
    extra_paths = sorted(paths_seen - skill_paths)
    for rel in missing_paths:
        errors.append(f"{catalog_path}: missing skill entry for {rel}")
    for rel in extra_paths:
        errors.append(f"{catalog_path}: catalog includes non-skill path {rel}")


def validate_markdown_links(doc_path: Path, repo_root: Path, errors: list[str]) -> None:
    if not doc_path.exists():
        errors.append(f"{doc_path}: required doc not found")
        return

    text = doc_path.read_text(encoding="utf-8")
    for target in LINK_RE.findall(text):
        target = target.strip()
        if not target or target.startswith("#"):
            continue
        if target.startswith(("http://", "https://", "mailto:")):
            continue

        clean_target = target.split("#", 1)[0]
        resolved = (doc_path.parent / clean_target).resolve()
        try:
            resolved.relative_to(repo_root.resolve())
        except ValueError:
            errors.append(f"{doc_path}: link escapes repository: {target}")
            continue

        if not resolved.exists():
            rel_doc = doc_path.relative_to(repo_root).as_posix()
            errors.append(f"{rel_doc}: broken relative link '{target}'")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate skill library consistency")
    parser.add_argument(
        "--repo-root",
        default=Path(__file__).resolve().parents[1],
        type=Path,
        help="Repository root path",
    )
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    errors: list[str] = []

    skill_files = sorted((repo_root / "skills").glob("*/*.md"))
    if not skill_files:
        errors.append("No skill markdown files found in skills/*/*.md")
    for path in skill_files:
        validate_skill_file(path, errors)

    validate_catalog(repo_root, repo_root / "skills" / "catalog.yaml", errors)

    for doc in ["README.md", "SKILL_SPEC.md", "CONTRIBUTING.md"]:
        validate_markdown_links(repo_root / doc, repo_root, errors)

    if errors:
        print("Validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1

    print(
        f"Validation passed: {len(skill_files)} skills, catalog integrity OK, and core links resolved."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
