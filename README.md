# Agent Skills

Four agent skills, each one a written-down method rather than a prompt collection. They come from work that was actually done and verified, not from general advice.

English · [中文](README.zh.md)

## Skills

| Skill | What it does |
| --- | --- |
| [`oss-contribution`](skills/oss-contribution/SKILL.md) | Gates a contribution before any code is written: is the repository open to outside pull requests, is the issue still real, can the change be verified. |
| [`dify-plugin-fix`](skills/dify-plugin-fix/SKILL.md) | Finds real defects in Dify's official plugin repository with two lint passes, then verifies and submits them under that repository's rules. |
| [`bilingual-docs`](skills/bilingual-docs/SKILL.md) | Keeps Chinese and English documentation in step: file naming, the language switcher, what to translate and what to leave byte-identical. |
| [`repo-audit`](skills/repo-audit/SKILL.md) | A read-only GitHub audit that ends in a three-tier cleanup plan instead of an opinion. |

Each skill is a directory with a `SKILL.md`. Some carry `references/` or `scripts/` next to it.

## Install

Copy a skill directory into the skills folder your agent reads, for example:

```bash
cp -r skills/oss-contribution ~/.codex/skills/
```

The exact location depends on the agent: `~/.codex/skills`, `~/.claude/skills`, `~/.agents/skills` and `~/.trae/skills` are all in common use. Most agents pick up a new skill on the next session.

## Layout

```
.
├── skills/
│   ├── oss-contribution/SKILL.md
│   ├── dify-plugin-fix/SKILL.md
│   ├── bilingual-docs/SKILL.md
│   └── repo-audit/SKILL.md
├── scripts/validate.py
└── .github/workflows/validate.yml
```

## Validate

```bash
python scripts/validate.py
```

The same check runs in CI on every push and pull request. It verifies that each skill has valid frontmatter, that the skill name matches its directory, that the description is long enough to be useful, and that the two READMEs link to each other.

## Contributing

Issues and pull requests are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT. See [LICENSE](LICENSE).
