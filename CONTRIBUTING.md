# Contributing

Thanks for taking a look. This repository is small on purpose.

## What is welcome

- Fixes and improvements to the four skills under `skills/`
- Corrections to the validator or the CI workflow
- Documentation fixes in either language

## What is not welcome

- Third-party skill content. The catalog indexes other projects; it does not redistribute them.
- New skills without a real workflow behind them. A skill that restates general advice is not useful.
- Formatting-only pull requests.

## Before opening a pull request

1. Run `python scripts/validate.py` and make sure it passes.
2. If you changed a skill's frontmatter, check that `name` still matches its directory.
3. If you edited one README, make the same structural change in the other language.
4. Keep the change focused; one topic per pull request.
