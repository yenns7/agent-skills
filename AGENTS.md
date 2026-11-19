# Repository notes for agents

This repository publishes four original skills and an index of locally installed skills.

## Rules

- Only skills under `skills/` are distributed by this repository. They are MIT licensed and written from scratch here.
- Never copy third-party skill content into this repository. The catalog records names, descriptions and categories only.
- Keep `README.md` and `README.zh.md` structurally identical: same headings, same order, same links.
- Every skill directory must contain `SKILL.md` with `name` and `description` in the frontmatter, and `name` must match the directory name.
- Run `python scripts/validate.py` before committing.

## Catalog

The three files under `catalog/` are generated from the local skills directories. Regenerate all three together so the counts stay consistent.
