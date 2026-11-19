---
name: bilingual-docs
description: Keep a project's documentation available in both Chinese and English without letting the two versions drift. Use when a README or docs set needs a Chinese and an English version, when one language is stale, or when a repository mixes languages inconsistently.
---

# Bilingual docs

Two language versions only work if each one is clearly labelled and they are checked against each other. A translated README that silently falls behind is worse than no translation, because readers trust it.

## File layout

Pick one convention per repository and use it everywhere:

| Pattern | When to use |
| --- | --- |
| `README.md` + `README.zh.md` | English is the default language |
| `README.md` + `README.en.md` | Chinese is the default language |
| `README.md` + `README.zh-CN.md` | a regional variant is needed |

Documentation pages follow the same rule: `guide.md` + `guide.zh.md`, never a bare `guide-zh.md` mixed with `guide.en.md`.

## The language switcher

Every version opens with the same one-line switcher, directly under the title:

```markdown
English · [中文](README.zh.md)
```

```markdown
[English](README.en.md) · 中文
```

The current language is plain text, the other one is a link. Keep the order identical in both files so the switcher does not jump around.

## Writing the second version

- Translate the structure, not just the sentences: the same headings, in the same order, with the same badges and tables.
- Keep code blocks, commands, file paths, environment variable names and URLs identical. Translate only the prose around them.
- Translate product names only if an official Chinese name exists; otherwise keep the original.
- Do not add sections that exist in one version only. If a section is genuinely language-specific, mark it as such in both files.
- If the source version changes, update both before merging. A one-sided edit is a defect.

## Checklist before committing

1. Both files start with the same title and a language switcher.
2. Heading counts match, in the same order.
3. Every link in both files resolves — check relative links, not just URLs.
4. Commands are byte-identical across versions.
5. The default file is the one most readers expect, and `README.zh.md`/`README.en.md` is linked from it.
6. If the repository has a validator or CI, it passes.

## What to report back

- which files were added or changed
- whether the two versions are structurally identical
- anything that could not be translated faithfully, and how it was handled
