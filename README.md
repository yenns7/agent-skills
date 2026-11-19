# Agent Skills

A working collection of agent skills — four written from scratch here, plus an index of the 355 skills installed on the author's machine.

English · [中文](README.zh.md)

## Why this exists

Agent skills are easy to accumulate and hard to keep track of. After a few months of installing bundles, the local skills directory becomes a pile of names with no map: what came from where, what is still used, what duplicates what.

This repository does two things:

1. **Publishes original skills** that are small, self-contained and written against real workflows.
2. **Indexes the local collection** so the whole set can be reasoned about — without copying anyone else's work.

## Skills in this repository

| Skill | What it does |
| --- | --- |
| [`oss-contribution`](skills/oss-contribution/SKILL.md) | Gates a contribution before any code is written: is the repository open to outside pull requests, is the issue still real, can the change be verified. |
| [`dify-plugin-fix`](skills/dify-plugin-fix/SKILL.md) | Finds real defects in Dify's official plugin repository with two lint passes, then verifies and submits them under that repository's rules. |
| [`bilingual-docs`](skills/bilingual-docs/SKILL.md) | Keeps Chinese and English documentation in step: file naming, the language switcher, what to translate and what to leave byte-identical. |
| [`repo-audit`](skills/repo-audit/SKILL.md) | A read-only GitHub audit that ends in a three-tier cleanup plan instead of an opinion. |

Each skill is a directory with a `SKILL.md`. Some carry `references/` or `scripts/` next to it.

## Catalog

The catalog is an index, not a redistribution. Every third-party skill stays in its own repository and keeps its own licence.

- [`catalog/local-skills.json`](catalog/local-skills.json) — machine-readable: name, description, category, source path
- [`catalog/local-skills.md`](catalog/local-skills.md) — grouped tables
- [`catalog/local-skills.zh.md`](catalog/local-skills.zh.md) — the same index in Chinese

Current breakdown:

| Category | Skills |
| --- | --- |
| Other / local | 128 |
| gstack suite | 48 |
| Design / UI skills | 30 |
| Lark / Feishu skill suite | 28 |
| Superpowers workflow suite | 26 |
| Browser / web skills | 20 |
| Engineering guides | 18 |
| Feishu / Miaoda workflow | 16 |
| Diagram skills | 11 |
| ASu skills (Hisn00w/ASu-skills) | 9 |
| ByteDance internal tooling | 8 |
| GSAP official skills | 8 |
| MiniMax skill suite | 5 |

To refresh the index after installing or removing skills, regenerate the three catalog files from the local skills directories.

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
├── catalog/
│   ├── local-skills.json
│   ├── local-skills.md
│   └── local-skills.zh.md
├── scripts/validate.py
└── .github/workflows/validate.yml
```

## Validate

```bash
python scripts/validate.py
```

The same check runs in CI on every push and pull request. It verifies that each skill has valid frontmatter, that the skill name matches its directory, that the two READMEs link to each other, and that the catalog parses and its count is consistent.

## Contributing

Issues and pull requests are welcome for the four skills in `skills/`. See [CONTRIBUTING.md](CONTRIBUTING.md). The catalog is a personal index; please do not add third-party skill content to it.

## License

MIT. See [LICENSE](LICENSE).
