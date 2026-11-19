# Agent Skills

一份可用的 Agent Skills 合集 —— 4 个原创 skill，外加本机已安装的 355 个 skill 的索引。

[English](README.md) · 中文

## 为什么建这个仓库

Skill 很容易越装越多，却很难看清全貌。装过几套合集之后，本地 skills 目录就变成一堆没有地图的名字：哪个来自哪里、哪些还在用、哪些和别的重复。

这个仓库做两件事：

1. **发布原创 skill**：体积小、自成一体、针对真实工作流写成。
2. **索引本地合集**：让整套 skill 可以被整体审视 —— 但不复制别人的作品。

## 仓库内的 skill

| Skill | 作用 |
| --- | --- |
| [`oss-contribution`](skills/oss-contribution/SKILL.md) | 在写代码之前先过闸门：仓库是否接受外部 PR、issue 是否仍然成立、改动能否被验证。 |
| [`dify-plugin-fix`](skills/dify-plugin-fix/SKILL.md) | 用两轮静态检查在 Dify 官方插件仓库里定位真实缺陷，再按该仓库的规则验证并提交。 |
| [`bilingual-docs`](skills/bilingual-docs/SKILL.md) | 让中英文档保持一致：文件命名、语言切换器、哪些要翻译、哪些必须逐字相同。 |
| [`repo-audit`](skills/repo-audit/SKILL.md) | 只读的 GitHub 审计，产出的是一份分三档的清理方案，而不是主观感受。 |

每个 skill 是一个目录，里面有 `SKILL.md`；部分还会带 `references/` 或 `scripts/`。

## 目录索引

索引只是索引，不是分发。所有第三方 skill 仍留在各自的仓库里，遵循各自的许可证。

- [`catalog/local-skills.json`](catalog/local-skills.json) —— 机器可读：名称、描述、分类、来源路径
- [`catalog/local-skills.md`](catalog/local-skills.md) —— 分组表格（英文）
- [`catalog/local-skills.zh.md`](catalog/local-skills.zh.md) —— 同一份索引的中文版

当前分布：

| 分类 | 数量 |
| --- | --- |
| 其他 / 本地 | 128 |
| gstack 套件 | 48 |
| 设计 / UI 类 | 30 |
| Lark / 飞书 skill 套件 | 28 |
| Superpowers 工作流套件 | 26 |
| 浏览器 / 网页类 | 20 |
| 工程规范类 | 18 |
| 飞书 / 妙搭工作流 | 16 |
| 图表类 | 11 |
| ASu skills（Hisn00w/ASu-skills） | 9 |
| 字节内部工具 | 8 |
| GSAP 官方 skills | 8 |
| MiniMax 套件 | 5 |

安装或删除 skill 之后，重新生成本地 skills 目录对应的三个索引文件即可。

## 安装

把 skill 目录复制到你的 agent 读取的 skills 目录，例如：

```bash
cp -r skills/oss-contribution ~/.codex/skills/
```

具体位置取决于 agent：`~/.codex/skills`、`~/.claude/skills`、`~/.agents/skills`、`~/.trae/skills` 都很常见。多数 agent 在下一个会话即可识别。

## 目录结构

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

## 校验

```bash
python scripts/validate.py
```

同样的检查会在每次推送和 PR 时于 CI 中运行：每个 skill 的 frontmatter 是否合法、skill 名称是否与目录一致、两份 README 是否互相链接、索引能否解析且数量一致。

## 参与贡献

欢迎针对 `skills/` 下的 4 个 skill 提 issue 或 PR，详见 [CONTRIBUTING.md](CONTRIBUTING.md)。索引属于个人清单，请不要把第三方 skill 的内容加进来。

## 许可证

MIT，见 [LICENSE](LICENSE)。
