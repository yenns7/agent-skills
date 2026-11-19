---
name: repo-audit
description: Read-only audit of a GitHub account or repository that produces an actionable cleanup plan instead of a vague impression. Use when a profile feels cluttered, when deciding what to pin or archive, or before a job search that will point people at the account.
---

# Repository audit

Audit means **read only**. Do not create, delete, archive, rename, pin or edit anything while auditing. The deliverable is a plan with evidence, and the user decides what to execute.

## What to collect

Use the GitHub API through the authenticated CLI:

```bash
gh api user
gh repo list <owner> --limit 200 --json name,description,isFork,isArchived,stargazerCount,pushedAt,repositoryTopics,licenseInfo
gh api repos/<owner>/<repo>/compare/<upstream>:<branch>...<owner>:<branch>
```

For every repository record: visibility, fork status, last push, description, topics, licence, star count, and whether the default branch has any commits of its own.

## What counts as a problem

| Signal | Why it matters | Suggested action |
| --- | --- | --- |
| Fork with no commits ahead of upstream | Dilutes the profile; it is someone else's work | Delete, unless a pull request branch is open |
| Repository without a description | Shows up blank in listings and search | Add one sentence |
| No topics on a real project | Hurts discoverability | Add 5–8 accurate topics |
| Missing licence while the code is public | Blocks reuse and looks unfinished | Add the licence the project already implies |
| Stale for more than 12 months | Reads as abandoned | Archive, or say why it stays |
| Several near-duplicate repositories | Confuses readers about what is real | Keep one, archive the rest |
| Profile without a README, bio or pins | The first screen is empty | Add a short README, bio and up to six pins |

## Ranking the output

Split every recommendation into three tiers:

1. **Do now** — reversible and pure upside: descriptions, topics, licences, a profile README.
2. **Confirm first** — irreversible or judgement-based: deleting forks, archiving, making a private repository public.
3. **Leave alone** — harmless clutter that costs more to clean than to keep.

## Pinning

Only pin work you authored. Pinning a fork advertises someone else's project. Fewer than six strong pins looks better than six mixed ones, and a repository with no description should not be pinned until it has one.

## Rules for the report

- Every claim needs a fact behind it: repository name, date, field value or URL.
- Say when a field could not be read instead of guessing.
- Never present a fork's `pushedAt` as the user's own activity; it is the upstream's last commit.
- State clearly that deletion and archiving are irreversible and require the user's explicit go-ahead.

## Output shape

1. A short overall verdict — is the account cluttered, empty, or inconsistent?
2. A table of the repositories that have problems.
3. The three-tier action list.
4. A pinning recommendation with reasons.
5. An explicit reminder that nothing was changed.
