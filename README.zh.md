# Agent Skills

4 个 Agent Skill，每一个都是被验证过的方法总结，而不是提示词合集。它们来自真实做过并验证过的工作，不是泛泛的建议。

[English](README.md) · 中文

## Skills

| Skill | 作用 |
| --- | --- |
| [`oss-contribution`](skills/oss-contribution/SKILL.md) | 在写代码之前先过闸门：仓库是否接受外部 PR、issue 是否仍然成立、改动能否被验证。 |
| [`dify-plugin-fix`](skills/dify-plugin-fix/SKILL.md) | 用两轮静态检查在 Dify 官方插件仓库里定位真实缺陷，再按该仓库的规则验证并提交。 |
| [`bilingual-docs`](skills/bilingual-docs/SKILL.md) | 让中英文档保持一致：文件命名、语言切换器、哪些要翻译、哪些必须逐字相同。 |
| [`repo-audit`](skills/repo-audit/SKILL.md) | 只读的 GitHub 审计，产出的是一份分三档的清理方案，而不是主观感受。 |

每个 skill 是一个目录，里面有 `SKILL.md`；部分还会带 `references/` 或 `scripts/`。

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
├── scripts/validate.py
└── .github/workflows/validate.yml
```

## 校验

```bash
python scripts/validate.py
```

同样的检查会在每次推送和 PR 时于 CI 中运行：每个 skill 的 frontmatter 是否合法、skill 名称是否与目录一致、描述是否足够具体、两份 README 是否互相链接。

## 参与贡献

欢迎提 issue 或 PR，详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可证

MIT，见 [LICENSE](LICENSE)。
