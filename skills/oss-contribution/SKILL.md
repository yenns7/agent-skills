---
name: oss-contribution
description: Land a real, verifiable open-source pull request instead of a drive-by typo fix. Use when the user wants to contribute to open source, build a contribution record, prepare first-contribution PRs, or asks why a repository rejected their PR.
---

# OSS contribution

A contribution is only worth submitting when the problem is real, the repository accepts outside pull requests, and the change can be verified locally. Work through the gates in order and stop at the first one that fails.

## 1. Check whether pull requests are welcome at all

Read these before reading any issue:

- `CONTRIBUTING.md`, `.github/CONTRIBUTING.md`, `AGENTS.md`, `AI_POLICY.md`
- the last 20 merged pull requests, to see what maintainers actually accept
- whether required checks include a CLA, DCO or a maintainer approval gate

Many large repositories now restrict outside pull requests, either explicitly ("we accept issues, not pull requests") or by auto-closing them. Record the verdict as one of:

| Verdict | Meaning |
| --- | --- |
| `eligible` | outside pull requests are accepted |
| `blocked` | accepted, but only after an issue is claimed or a maintainer approves |
| `ineligible` | pull requests are not accepted; do not spend time on a diff |

## 2. Find a problem that is still real

Label filters (`good first issue`, `help wanted`) are a starting point, not a source of truth. For every candidate, verify all of the following:

1. The issue is still open and unassigned.
2. No pull request already links to it. Check the issue timeline and the open pull request list; keyword search alone misses duplicates.
3. Nobody claimed it in the comments, even informally ("I'm working on it").
4. The described behaviour still exists in the current default branch. Read the code, not just the issue. Stale issues are common — a fix may already have shipped.
5. The change is verifiable without paid credentials, proprietary services or a GPU.

Drop a candidate at the first failed check. Write down which check failed so the same candidate is not re-investigated later.

## 3. Prefer defects that prove themselves

Highest merge odds, roughly in order:

1. A crash with a deterministic reproduction (`NameError`, `KeyError`, `IndexError`) that a linter or a small test already exposes.
2. A logic defect where the code cannot do what its own comment or docstring says.
3. Dead code that can never run — provided you can prove the path is unreachable.
4. A missing input validation that produces a confusing error.
5. Documentation that contradicts the shipped behaviour.

Avoid: typo-only changes, formatting sweeps, mass dependency bumps, and "add tests" pull requests with no failing case behind them.

## 4. Build the smallest honest diff

- Branch from the current upstream default branch, never from another feature branch.
- Change one thing. If the diff needs a second unrelated fix, split it.
- Match the surrounding style instead of reformatting the file.
- Add a regression test where the project has a test suite, and make it fail before the fix.
- Do not silence a linter to make a check pass.

## 5. Verify with evidence

Record the exact commands and their output:

- the failing test before the change, if one exists
- the full test suite after the change
- the project's lint and format commands
- a note on what was **not** verified, and why

Never describe a local run as continuous-integration success. `pending`, `queued` and `action_required` are not passes.

## 6. Write the pull request

- Title: follow the repository's convention (`fix(scope): ...`, `docs: ...`).
- Body: what changed, why, how it was verified, and the linked issue.
- State the limitation plainly when a live end-to-end test was not possible.
- If a required check needs maintainer approval for first-time contributors, say so instead of waiting silently.

## 7. Track it

Watch the checks, the review comments and the merge state. When a reviewer asks for a change, continue on the same branch. Record the final state accurately: submitted, in review, merged, or closed.

## What to report back

- repository, pull request link and current state
- the defect, the root cause and the fix in one paragraph each
- verification commands and results
- what remains unverified
- the reusable lesson, if any
