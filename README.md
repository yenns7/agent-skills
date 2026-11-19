<div align="center">

**中文** · [English](./README.en.md)

# 🧰 Agent Skills

#### 把自己真实做过、验证过的方法，写成 Agent 能直接加载的 4 个 Skill

[![License](https://img.shields.io/badge/License-MIT-3B82F6?style=for-the-badge)](./LICENSE)
[![Skills](https://img.shields.io/badge/Skills-4-10B981?style=for-the-badge)](#-skills)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-8B5CF6?style=for-the-badge)](https://agentskills.io)

![Claude Code](https://img.shields.io/badge/Claude_Code-Skill-D97706?style=flat-square&logo=anthropic&logoColor=white)
![Codex](https://img.shields.io/badge/Codex-Skill-10B981?style=flat-square&logo=openai&logoColor=white)
![40+ Agents](https://img.shields.io/badge/40%2B_Agents-Compatible-3B82F6?style=flat-square)

</div>

这 4 个 Skill 不是凭空写的提示词，是最近几周真实干活时沉淀下来的：给 Dify 官方插件仓库提了 9 个 PR、踩过「仓库其实不收外部 PR」的坑、给几个项目补中英双语、还做过一次 GitHub 账号的只读审计。每一条规则背后都有一次具体的失败或验证。

每个 Skill 都是 Agent 能直接加载的结构化指令集，遵循 [Agent Skills](https://agentskills.io) 开放标准。Claude Code、Codex、Cursor 等支持该标准的 Agent 都能装。

---

## 📋 目录

| 名字 | 一句话 | 详情 |
|---|---|---|
| 🧭 [**oss-contribution（开源贡献闸门）**](#-oss-contribution开源贡献闸门) | 动手写代码之前，先判断这个仓库到底收不收外部 PR、这个 issue 还成不成立 | [SKILL.md](./skills/oss-contribution/SKILL.md) |
| 🩺 [**dify-plugin-fix（Dify 插件修缺陷）**](#-dify-plugin-fixdify-插件修缺陷) | 用两轮静态检查在 Dify 官方插件仓库里捞出真实崩溃点，再按它的规则提交 | [SKILL.md](./skills/dify-plugin-fix/SKILL.md) |
| 🌏 [**bilingual-docs（中英双语文档）**](#-bilingual-docs中英双语文档) | 两个语言版本互相校验，不让翻译悄悄落后于原文 | [SKILL.md](./skills/bilingual-docs/SKILL.md) |
| 🔍 [**repo-audit（GitHub 只读审计）**](#-repo-auditgithub-只读审计) | 只读扫描账号或仓库，产出分三档的清理方案，而不是替你动手 | [SKILL.md](./skills/repo-audit/SKILL.md) |

---

## 📦 安装方式

在 Claude Code、Codex 等支持 Agent Skills 的工具里，直接说：

```
帮我安装这个 skill：https://github.com/yenns7/agent-skills/tree/main/skills/<skill-name>
```

把 `<skill-name>` 换成想装的那个，比如 `oss-contribution`、`dify-plugin-fix`。Agent 会自己 clone 到对应目录。

手动安装就把整个目录放进 Agent 读取的 skills 目录：

| 工具 | 所有项目可用 | 只在某个项目里用 |
|---|---|---|
| Claude Code | `~/.claude/skills/<skill-name>/` | `.claude/skills/<skill-name>/` |
| Codex、Gemini CLI、GitHub Copilot 等 | `~/.agents/skills/<skill-name>/` | `.agents/skills/<skill-name>/` |

安装时保留整个 Skill 目录。只复制 `SKILL.md` 也能读懂方法，但配套的脚本和参考文件就没了。

---

## ✨ Skills

<a id="-skills"></a>

<table>
<tr><td>

### 🧭 oss-contribution（开源贡献闸门）

> *"仓库写着「欢迎贡献」，不代表它收你的 PR。"*

**它只解决一件事：在花时间写代码之前，先判断这次贡献值不值得做。**

贡献的开销大头从来不是写那几行代码，而是写完之后发现仓库暂停了外部 PR、issue 已经被别人认领、或者这个 bug 上游早就修好了。这个 Skill 把这些检查做成固定顺序的闸门，任何一关不过就停下。

**四道闸门**

| # | 闸门 | 判断依据 |
|---|---|---|
| 1 | 仓库收不收外部 PR | `CONTRIBUTING`、`AGENTS.md`、最近 20 个已合并 PR、有没有 CLA |
| 2 | 问题还成不成立 | issue 是否开放、是否被认领、有没有关联 PR、**当前代码里这个 bug 还在不在** |
| 3 | 改动能不能验证 | 不需要付费凭证、专有服务或 GPU |
| 4 | 值不值得提交 | 崩溃 > 逻辑缺陷 > 死代码 > 缺校验 > 文档，跳过 typo 和格式化 |

第 2 关最容易翻车：issue 还开着，代码其实已经修好了。所以它要求读代码，而不是只读 issue。

**为什么强调「证据」**

它把「本地跑过」和「CI 通过」严格分开。`pending`、`queued`、`action_required` 都不算通过，只有页面显示 success 才算。提交后要如实记录：已提交、评审中、已合并，还是已关闭。

**怎么触发**

```
我想给这个开源项目提个 PR
帮我找几个适合我的 first contribution
这个仓库为什么不收我的 PR
```

→ [SKILL.md](./skills/oss-contribution/SKILL.md)

</td></tr>
</table>

<table>
<tr><td>

### 🩺 dify-plugin-fix（Dify 插件修缺陷）

> *"Dify 官方插件仓库的 CI 不跑 lint，所以真实的崩溃点一直躺在那里。"*

**它只解决一件事：在 Dify 插件生态里找到能证明、能验证、能被合并的缺陷。**

`langgenius/dify-official-plugins` 里每个插件一个目录，维护者合并小修复很勤。但它的 CI 只检查打包和版本号，不检查未定义变量，所以 `F821` 这类必然崩溃的写法能长期存在。

**两轮检查就够**

```bash
ruff check models tools --select F821,F823 --output-format concise   # 未定义变量
ruff check models tools --select F811 --output-format concise        # 重复定义
```

命中的每一条都要再确认三件事：作用域里真的没定义、代码路径可达、外层没有把异常吞掉。测试夹具里、永远不会执行的 `except` 里命中，不算用户可见的 bug。

**两类最值得修**

- **被覆盖的方法**：Python 里同名方法后者覆盖前者，前一份逻辑永远不执行。删掉是行为中性的，可证明。
- **`return` 之后的死代码**：常见于合并事故，里面还藏着一个嵌套 import。

**这个仓库的提交规矩**

- 先开 issue，写清崩溃现象、文件行号和 lint 输出
- `manifest.yaml` 必须升版本号，否则 CI 报「版本已存在」
- PR 正文的 `## Release Notes` 不能空，它会直接发布到插件市场
- 一个插件一个 PR

**怎么触发**

```
帮我看看 Dify 插件仓库里有什么能修的
这个 Dify 插件报 NameError，帮我定位
```

→ [SKILL.md](./skills/dify-plugin-fix/SKILL.md)

</td></tr>
</table>

<table>
<tr><td>

### 🌏 bilingual-docs（中英双语文档）

> *"一个悄悄落后于原文的翻译，比没有翻译更糟——因为读者会信它。"*

**它只解决一件事：让中英两个版本结构一致、互相互链、不会各自漂移。**

**命名先统一**

| 约定 | 适用 |
|---|---|
| `README.md` + `README.zh.md` | 英文是默认语言 |
| `README.md` + `README.en.md` | 中文是默认语言 |

一个仓库只用一种，别混着来。

**切换器**

两个版本标题下第一行都是同一句，当前语言用纯文本，另一个用链接：

```markdown
English · [中文](README.zh.md)
```

**翻译什么、不翻译什么**

翻译结构而不是句子：同样的标题、同样的顺序、同样的徽章和表格。代码块、命令、路径、环境变量名、URL 一律逐字保留。原文改了，两个版本要一起改，单边修改就是缺陷。

**提交前自查**

1. 两边标题和切换器一致
2. 标题数量、顺序一致
3. 相对链接都能打开
4. 命令逐字相同
5. 默认文件链到了另一个语言

**怎么触发**

```
帮我把这个 README 补一个英文版
这个项目的文档中英文不一致
帮我检查双语文档有没有对齐
```

→ [SKILL.md](./skills/bilingual-docs/SKILL.md)

</td></tr>
</table>

<table>
<tr><td>

### 🔍 repo-audit（GitHub 只读审计）

> *"审计的意思是只看不动。方案给你，删不删你决定。"*

**它只解决一件事：把「主页有点乱」这种感觉，变成一份有证据、分优先级的清单。**

**收什么事实**

每个仓库都要记录：可见性、是否 fork、最后推送时间、描述、topics、许可证、star 数，以及默认分支**有没有自己的提交**。fork 的 `pushedAt` 是上游的时间，不是你的活动——这一点经常被误读。

**什么算问题**

| 信号 | 为什么是问题 | 建议 |
|---|---|---|
| fork 但相对上游没有任何自己的提交 | 稀释主页，展示的是别人的作品 | 删除，除非还挂着 PR 分支 |
| 没有描述 | 列表和搜索里显示空白 | 补一句话 |
| 真实项目没有 topics | 影响发现 | 补 5–8 个准确标签 |
| 公开代码没有许可证 | 别人无法合法复用 | 补上项目本来就隐含的那个 |
| 超过 12 个月没动 | 看起来像废弃 | 归档，或说明为什么保留 |
| 几个高度重复的仓库 | 读者分不清哪个是真的 | 留一个 |

**三档输出**

立刻做（可逆、纯收益）／先确认（不可逆或有取舍）／可以不管。删除、归档、转公开都要你点头，它只给清单。

**怎么触发**

```
帮我看看我的 GitHub 主页乱不乱
我该置顶哪几个仓库
哪些 fork 可以删了
```

→ [SKILL.md](./skills/repo-audit/SKILL.md)

</td></tr>
</table>

---

## ✅ 校验

```bash
python scripts/validate.py
```

每次推送和 PR 都会在 CI 里跑同一套检查：frontmatter 是否合法、skill 名称是否与目录一致、描述是否足够具体、两份 README 是否互相链接。

## 🌟 关于

这些 Skill 都来自我自己真实的工作流，踩过的坑写在规则里。如果你也在做 AI 产品或者自动化，希望能省你一点时间。觉得有用给个 ⭐ 就行，有问题欢迎在 Issues 里说。

---

<div align="center">

[MIT License](./LICENSE) · 自由使用 / 修改 / 再分发

Made by [@yenns7](https://github.com/yenns7)

</div>
