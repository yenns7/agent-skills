<div align="center">

[中文](./README.md) · **English**

# 🧰 Agent Skills

#### Four skills distilled from work I actually did and verified

[![License](https://img.shields.io/badge/License-MIT-3B82F6?style=for-the-badge)](./LICENSE)
[![Skills](https://img.shields.io/badge/Skills-4-10B981?style=for-the-badge)](#-skills)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-8B5CF6?style=for-the-badge)](https://agentskills.io)

![Claude Code](https://img.shields.io/badge/Claude_Code-Skill-D97706?style=flat-square&logo=anthropic&logoColor=white)
![Codex](https://img.shields.io/badge/Codex-Skill-10B981?style=flat-square&logo=openai&logoColor=white)
![40+ Agents](https://img.shields.io/badge/40%2B_Agents-Compatible-3B82F6?style=flat-square)

</div>

These four skills are not prompts written from imagination. They came out of the last few weeks of real work: nine pull requests to Dify's official plugin repository, a run-in with a project that quietly stopped accepting outside pull requests, several repositories that needed Chinese and English versions, and a read-only audit of a GitHub account. Every rule traces back to a specific failure or a specific verification.

Each skill is a structured instruction set an agent can load directly. They follow the [Agent Skills](https://agentskills.io) open standard and work with Claude Code, Codex, Cursor and other agents that support it.

---

## 📋 Index

| Name | One-liner | Details |
|---|---|---|
| 🧭 [**oss-contribution**](#-oss-contribution) | Before writing any code, check whether the repository accepts outside pull requests and whether the issue is still real | [SKILL.md](./skills/oss-contribution/SKILL.md) |
| 🩺 [**dify-plugin-fix**](#-dify-plugin-fix) | Two lint passes find real crashes in Dify's official plugin repository, then submit them under that repository's rules | [SKILL.md](./skills/dify-plugin-fix/SKILL.md) |
| 🌏 [**bilingual-docs**](#-bilingual-docs) | Two language versions that check each other, so a translation never silently falls behind | [SKILL.md](./skills/bilingual-docs/SKILL.md) |
| 🔍 [**repo-audit**](#-repo-audit) | A read-only scan of an account or repository that ends in a three-tier cleanup plan, not in changes | [SKILL.md](./skills/repo-audit/SKILL.md) |

---

## 📦 Install

In any agent that supports Agent Skills, just say:

```
Install this skill: https://github.com/yenns7/agent-skills/tree/main/skills/<skill-name>
```

Replace `<skill-name>` with the one you want, for example `oss-contribution` or `dify-plugin-fix`. The agent clones it into the right directory.

To install by hand, copy the whole directory into the skills folder your agent reads:

| Tool | Available everywhere | Only inside one project |
|---|---|---|
| Claude Code | `~/.claude/skills/<skill-name>/` | `.claude/skills/<skill-name>/` |
| Codex, Gemini CLI, GitHub Copilot, etc. | `~/.agents/skills/<skill-name>/` | `.agents/skills/<skill-name>/` |

Keep the whole skill directory. Copying only `SKILL.md` still explains the method, but the supporting scripts and references are lost.

---

## ✨ Skills

<a id="-skills"></a>

<table>
<tr><td>

### 🧭 oss-contribution

> *"A repository that says 'contributions welcome' is not the same as a repository that will take your pull request."*

**It solves one thing: decide whether a contribution is worth doing before you spend time on it.**

The expensive part of contributing is rarely the code. It is discovering, after the fact, that the project paused outside pull requests, that the issue was already claimed, or that upstream fixed the bug months ago. This skill turns those checks into an ordered set of gates; the first one that fails ends the investigation.

**Four gates**

| # | Gate | Evidence |
|---|---|---|
| 1 | Does the project accept outside pull requests | `CONTRIBUTING`, `AGENTS.md`, the last 20 merged pull requests, whether a CLA is required |
| 2 | Is the problem still real | issue open and unassigned, no linked pull request, **and the bug still present in the current code** |
| 3 | Can the change be verified | no paid credentials, proprietary service or GPU required |
| 4 | Is it worth submitting | crash > logic defect > dead code > missing validation > docs; skip typos and formatting |

Gate 2 is where most time is lost: the issue is still open, but the code was already fixed. That is why the skill reads the code, not just the issue.

**Why evidence matters**

It keeps "I ran it locally" and "continuous integration passed" strictly separate. `pending`, `queued` and `action_required` are not passes; only a green page is. After submitting, the state is recorded accurately: submitted, in review, merged or closed.

**Triggers**

```
I want to contribute a PR to this project
Find me some good first contributions
Why did this repository reject my PR
```

→ [SKILL.md](./skills/oss-contribution/SKILL.md)

</td></tr>
</table>

<table>
<tr><td>

### 🩺 dify-plugin-fix

> *"Dify's plugin repository does not run a linter in CI, so real crashes just sit there."*

**It solves one thing: find defects in the Dify plugin ecosystem that can be proven, verified and merged.**

`langgenius/dify-official-plugins` holds one directory per plugin, and maintainers merge small fixes continuously. But its CI only checks packaging and version numbers, never undefined names — which is why `F821` crashes survive there for months.

**Two passes are enough**

```bash
ruff check models tools --select F821,F823 --output-format concise   # undefined names
ruff check models tools --select F811 --output-format concise        # shadowed definitions
```

For every hit, confirm three things: the name really is undefined in that scope, the path is reachable in normal use, and no outer handler turns the failure into something harmless. A hit inside a test fixture or an `except` clause that never runs is not a user-facing bug.

**The two most valuable classes**

- **Shadowed methods** — Python keeps the last definition in a class body, so the earlier one never runs. Removing it is behaviour-neutral and provable.
- **Dead code after `return`** — usually a merge accident, often carrying a nested import that shadows a module-level one.

**Rules for this repository**

- Open an issue first, with the crash, the file and line, and the lint output
- Bump `version:` in `manifest.yaml`, or CI rejects the version as already published
- `## Release Notes` in the pull request body must not be empty — it is published to the marketplace
- One plugin per pull request

**Triggers**

```
Look for something fixable in the Dify plugin repository
This Dify plugin throws NameError, help me locate it
```

→ [SKILL.md](./skills/dify-plugin-fix/SKILL.md)

</td></tr>
</table>

<table>
<tr><td>

### 🌏 bilingual-docs

> *"A translation that quietly falls behind is worse than no translation, because readers trust it."*

**It solves one thing: keep the Chinese and English versions structurally identical, mutually linked, and unable to drift apart.**

**Pick one naming convention**

| Convention | When |
|---|---|
| `README.md` + `README.zh.md` | English is the default language |
| `README.md` + `README.en.md` | Chinese is the default language |

One per repository. Never mix them.

**The switcher**

The first line under the title in both files is the same, with the current language as plain text and the other as a link:

```markdown
English · [中文](README.zh.md)
```

**What to translate, what to keep byte-identical**

Translate the structure, not just the sentences: the same headings, the same order, the same badges and tables. Code blocks, commands, paths, environment variable names and URLs stay exactly as they are. When the source changes, both files change in the same commit; a one-sided edit is a defect.

**Checklist before committing**

1. Both files start with the same title and a language switcher
2. Heading count and order match
3. Every relative link resolves
4. Commands are byte-identical
5. The default file links to the other language

**Triggers**

```
Add an English version of this README
This project's docs are inconsistent between Chinese and English
Check whether the bilingual docs are aligned
```

→ [SKILL.md](./skills/bilingual-docs/SKILL.md)

</td></tr>
</table>

<table>
<tr><td>

### 🔍 repo-audit

> *"Audit means look, do not touch. You get the plan; you decide what to delete."*

**It solves one thing: turn "my profile feels cluttered" into an evidence-backed, prioritised list.**

**What it collects**

For every repository: visibility, fork status, last push, description, topics, licence, star count, and whether the default branch has **any commits of its own**. A fork's `pushedAt` is the upstream's last commit, not your activity — a detail that is misread constantly.

**What counts as a problem**

| Signal | Why it matters | Suggested action |
|---|---|---|
| Fork with no commits ahead of upstream | Dilutes the profile; it shows someone else's work | Delete, unless a pull request branch is still open |
| No description | Shows up blank in listings and search | Add one sentence |
| A real project with no topics | Hurts discoverability | Add 5–8 accurate topics |
| Public code with no licence | Nobody can legally reuse it | Add the licence the project already implies |
| Untouched for more than 12 months | Reads as abandoned | Archive, or explain why it stays |
| Several near-duplicate repositories | Readers cannot tell which is real | Keep one |

**Three tiers of output**

Do now (reversible, pure upside) / confirm first (irreversible or a judgement call) / leave alone. Deletion, archiving and making a repository public all need your explicit go-ahead; the skill only produces the list.

**Triggers**

```
Is my GitHub profile a mess
Which repositories should I pin
Which forks can I delete
```

→ [SKILL.md](./skills/repo-audit/SKILL.md)

</td></tr>
</table>

---

## ✅ Validate

```bash
python scripts/validate.py
```

The same check runs in CI on every push and pull request: frontmatter is valid, the skill name matches its directory, the description is specific enough, and the two READMEs link to each other.

## 🌟 About

These skills come from my own workflow, with the mistakes written into the rules. If you build AI products or automation, I hope they save you some time. A ⭐ is enough if they help; questions and suggestions are welcome in Issues.

---

<div align="center">

[MIT License](./LICENSE) · Use, modify and redistribute freely

Made by [@yenns7](https://github.com/yenns7)

</div>
