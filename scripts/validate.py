#!/usr/bin/env python3
"""Validate the layout of this skills repository.

Checks, without third-party dependencies:

- every directory under skills/ has a SKILL.md
- each SKILL.md starts with YAML frontmatter containing name and description
- name matches the directory name
- description is long enough to be useful
- the English and Chinese READMEs link to each other
- catalog/local-skills.json parses and its count matches its entries
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
MIN_DESCRIPTION = 40


def parse_frontmatter(text: str) -> dict[str, str] | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    block = text[4:end]
    data: dict[str, str] = {}
    for line in block.splitlines():
        if ":" not in line or line.startswith(" "):
            continue
        key, _, value = line.partition(":")
        data[key.strip()] = value.strip().strip('"')
    return data


def check_skills(errors: list[str]) -> int:
    if not SKILLS.is_dir():
        errors.append("skills/ directory is missing")
        return 0

    count = 0
    for directory in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        count += 1
        skill = directory / "SKILL.md"
        if not skill.is_file():
            errors.append(f"{directory.name}: SKILL.md is missing")
            continue

        frontmatter = parse_frontmatter(skill.read_text(encoding="utf-8"))
        if frontmatter is None:
            errors.append(f"{directory.name}: SKILL.md has no frontmatter")
            continue

        name = frontmatter.get("name", "")
        description = frontmatter.get("description", "")

        if not name:
            errors.append(f"{directory.name}: frontmatter has no name")
        elif name != directory.name:
            errors.append(f"{directory.name}: name is '{name}' but the directory is '{directory.name}'")

        if not description:
            errors.append(f"{directory.name}: frontmatter has no description")
        elif len(description) < MIN_DESCRIPTION:
            errors.append(
                f"{directory.name}: description is {len(description)} characters, "
                f"needs at least {MIN_DESCRIPTION}"
            )

    return count


def check_readmes(errors: list[str]) -> None:
    en = ROOT / "README.md"
    zh = ROOT / "README.zh.md"
    if not en.is_file():
        errors.append("README.md is missing")
    if not zh.is_file():
        errors.append("README.zh.md is missing")
    if en.is_file() and zh.is_file():
        if "README.zh.md" not in en.read_text(encoding="utf-8"):
            errors.append("README.md does not link to README.zh.md")
        if "README.md" not in zh.read_text(encoding="utf-8"):
            errors.append("README.zh.md does not link back to README.md")


def check_catalog(errors: list[str]) -> int:
    path = ROOT / "catalog" / "local-skills.json"
    if not path.is_file():
        errors.append("catalog/local-skills.json is missing")
        return 0
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"catalog/local-skills.json is not valid JSON: {exc}")
        return 0

    skills = data.get("skills")
    if not isinstance(skills, list):
        errors.append("catalog/local-skills.json has no skills array")
        return 0
    if data.get("count") != len(skills):
        errors.append(
            f"catalog count is {data.get('count')} but the array holds {len(skills)} entries"
        )
    for entry in skills:
        for field in ("name", "description", "category"):
            if not entry.get(field):
                errors.append(f"catalog entry {entry.get('name', '<unnamed>')} has no {field}")
    return len(skills)


def main() -> int:
    errors: list[str] = []
    skill_count = check_skills(errors)
    check_readmes(errors)
    catalog_count = check_catalog(errors)

    if errors:
        print("validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"ok: {skill_count} skills, {catalog_count} catalog entries")
    return 0


if __name__ == "__main__":
    sys.exit(main())
