---
name: dify-plugin-fix
description: Find, reproduce and fix real defects in Dify's official plugin repository (langgenius/dify-official-plugins). Use when working on a Dify model provider, tool, datasource or agent strategy plugin, or when a Dify plugin PR needs a verifiable bug fix.
---

# Dify plugin fix

The official plugin repository holds one directory per plugin under `models/`, `tools/`, `datasources/`, `triggers/` and `extensions/`. It merges small, well-scoped plugin fixes continuously, and its continuous integration does **not** run a linter over plugin code — which means real defects survive there and are cheap to find.

## Where the defects hide

Run these checks against a fresh clone. They are fast, need no credentials, and every hit is a genuine defect rather than a style preference.

```bash
# undefined names: the most common source of hard crashes
ruff check models tools --select F821,F823 --output-format concise

# definitions that silently override an earlier one
ruff check models tools --select F811 --output-format concise
```

For each hit, open the file and confirm three things before touching anything:

1. The name really is undefined in that scope (not a `TYPE_CHECKING` import or a string annotation).
2. The code path is reachable in normal use.
3. The surrounding handler does not already turn the failure into something harmless.

A hit inside a test fixture or an `except` clause that is never evaluated is not a user-facing bug — say so instead of "fixing" it.

## Two classes worth knowing

**Shadowed definitions.** Python keeps the last definition of a method in a class body. A second `def validate_credentials` silently discards the first, so logic that looks active never runs. Removing the shadowed copy is behaviour-neutral and provable.

**Dead code after a return.** A duplicated block after `return` often carries a nested import that shadows a module-level one. Deleting it cannot change behaviour, but confirm the block is truly unreachable first.

## Verification recipe

```bash
cd models/<plugin>          # or tools/<plugin>
python -m pytest -q         # the plugin's own suite
ruff check .                # must be clean on the files you touched
```

If a test fails, check whether it fails on the untouched default branch before blaming your change. Report pre-existing failures explicitly in the pull request.

When a plugin has no tests, add one only if the defect is behavioural and a test can pin it. For a one-line import fix, the lint output plus the code path is enough evidence.

## Pull request rules for this repository

- Link an issue. Open one first if none exists; describe the crash, the file and line, and the lint output.
- Bump `version:` in the plugin's `manifest.yaml`; the CI rejects a version that already exists in the marketplace.
- Keep the `## Release Notes` section in the pull request body non-empty — it is published on the marketplace page.
- Do not change `author:`; it must stay `langgenius`.
- Never commit `.venv` directories inside a plugin path.

## Scope discipline

One plugin per pull request. Two unrelated fixes in one diff are harder to review and slower to merge. If the same defect class appears in several plugins, submit them separately and link them to each other.
