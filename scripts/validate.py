#!/usr/bin/env python3
"""Validate the layout of this skills repository.

Checks, without third-party dependencies:

- every directory under skills/ has a SKILL.md
- each SKILL.md starts with YAML frontmatter containing name and description
- name matches the directory name
- description is long enough to be useful
- the English and Chinese READMEs link to each other
- the plugin marketplace manifest parses and points at existing skills
"""

from __future__ import annotations

import json
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
    zh = ROOT / "README.md"
    en = ROOT / "README.en.md"
    if not zh.is_file():
        errors.append("README.md is missing")
    if not en.is_file():
        errors.append("README.en.md is missing")
    if zh.is_file() and en.is_file():
        if "README.en.md" not in zh.read_text(encoding="utf-8"):
            errors.append("README.md does not link to README.en.md")
        if "README.md" not in en.read_text(encoding="utf-8"):
            errors.append("README.en.md does not link back to README.md")


def check_marketplace(errors: list[str]) -> int:
    path = ROOT / ".claude-plugin" / "marketplace.json"
    if not path.is_file():
        errors.append(".claude-plugin/marketplace.json is missing")
        return 0
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"marketplace.json is not valid JSON: {exc}")
        return 0

    plugins = data.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        errors.append("marketplace.json has no plugins")
        return 0

    total = 0
    for plugin in plugins:
        for skill in plugin.get("skills", []):
            total += 1
            target = (ROOT / skill).resolve()
            if not target.is_dir():
                errors.append(f"marketplace.json points at a missing skill: {skill}")
            elif not (target / "SKILL.md").is_file():
                errors.append(f"marketplace.json skill has no SKILL.md: {skill}")
    return total


def main() -> int:
    errors: list[str] = []
    skill_count = check_skills(errors)
    check_readmes(errors)
    marketplace_count = check_marketplace(errors)

    if errors:
        print("validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"ok: {skill_count} skills, {marketplace_count} marketplace entries")
    return 0


if __name__ == "__main__":
    sys.exit(main())
