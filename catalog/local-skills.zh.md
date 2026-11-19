# 本地 Skills 目录

这份索引收录本机已安装的 355 个 skill，按来源分组。它只是索引，不是分发：每个 skill 仍留在自己的仓库里、遵循各自的许可证。

| 分类 | 数量 |
| --- | --- |
| Other / local | 128 |
| gstack suite | 48 |
| Design / UI skills | 30 |
| Lark / Feishu skill suite | 28 |
| Superpowers workflow suite | 26 |
| Browser / web skills | 20 |
| Engineering guides | 18 |
| Feishu / Miaoda workflow | 16 |
| Diagram skills | 11 |
| ASu skills (Hisn00w/ASu-skills) | 9 |
| ByteDance internal tooling | 8 |
| GSAP official skills | 8 |
| MiniMax skill suite | 5 |

## ASu skills (Hisn00w/ASu-skills)

| Skill | 作用 |
| --- | --- |
| `contributor` | GitHub 开源贡献辅助技能：围绕目标岗位和技术栈发现合适的开源项目与真实问题，评估维护状态、贡献规则和重复风险，准备最小可验证改动，经用户逐项确认后 fork、push、提交 PR，并跟踪 CI、review 和合并状态；当用户输入“/contributor”、想寻找项目、做 first contribution、提交 PR 或把 PR 写进简历时使用。 |
| `evidence-recap` | 把 AI 编程对话和项目交付材料复盘为可核验的九段证据链，区分问题、决策、个人动作、交付阶段、效果证据与责任边界。当用户运行 /evidence-recap、$evidence-recap，或明确要求复盘 AI 编程过程、交付记录、落地状态和证据缺口时使用；仅需简历改写、源码导学或模拟面试时不使用。 |
| `great-resume` | 中文求职经历提升技能：根据目标岗位把真实经历重组为岗位定位、简历要点、项目亮点和 HR 开场白；当用户输入“/great-resume”“我要酥化”或“简历提升”、要求包装或改写经历、项目，或写 HR 自我介绍时使用。若用户明确要求“阿酥同款”、复刻简历模板或生成对应 HTML/PDF，则交给 /make-resume。 |
| `interview` | 中文简历与目标岗位驱动的面试预测、模拟追问和复练技能：提取需要验证的经历 Claim，按面试轮次建立问题与评分契约，通过一次一问、证据反馈和弱项复练检查真实掌握程度；当用户输入“/interview”、要求面试预测、模拟面试、简历追问、压力面、场景设计题或检查面试掌握程度时使用。 |
| `job-apply` | 中文求职申请自动填写技能：使用浏览器读取用户确认的简历资料，逐项填写招聘网站申请表并核对结果；当用户输入“/job-apply”、要求自动填简历或填写求职申请时使用。 |
| `job-match` | 中文岗位匹配分析技能：对照目标 JD 与用户已确认的简历、经历或主张—证据账本，区分已匹配、证据不足和真实缺口，生成可解释的投递建议与后续 skill 交接；当用户输入“/job-match”、要求分析岗位适配度、JD 匹配、简历差距或判断是否值得投递时使用。需要改写简历时交给 /great-resume，需要模拟面试时交给 /interview。 |
| `make-resume` | 中文可编辑简历制作技能：默认基于 ASu 单栏高密度技术简历模板，根据用户经历制作或复刻可编辑 HTML/PDF；用户也可以指定仓库内其他模板、本地 HTML 或参考截图。用户输入“/make-resume”“我要阿酥同款简历”或要求制作、修改、复刻简历文件时使用；用户要求 LaTeX、`.tex` 或 Overleaf 版本时，在默认 HTML 交付之外附 |
| `offer` | 中文秋招求职进度管理技能：记录和更新投递、筛选、测评、面试、Offer、拒信及招聘邮件状态，生成可搜索的进度表；也可以比较多个 Offer 的薪资结构、成长空间、团队、稳定性和个人成本，输出加权决策建议与谈判要点；当用户输入“/offer”、要求管理秋招进度、比较或选择 Offer、分析薪资结构、谈薪时使用。 |
| `project-guide` | 中文项目导学、源码课程与项目面经技能：基于本地项目仓库、项目描述或技术材料，按需生成源码课程与理解题，或生成 导学-{简称}.md、面经-{简称}.md 及交接摘要；当用户输入“/project-guide”、要求项目导学、源码课程、按调用链展开课程、课程练习、项目复盘、项目面经或 STAR 题库时使用。 |

## Browser / web skills

| Skill | 作用 |
| --- | --- |
| `agent-browser` | Browser automation CLI for AI agents. Use when the user needs to interact with websites, verify dev server output, test web apps, navigate pages, fill forms, click buttons, take sc |
| `agent-browser` | Browser automation CLI for AI agents. Use when the user needs to interact with websites, including navigating pages, filling forms, clicking buttons, taking screenshots, extracting |
| `anysearch` | Real-time search engine supporting web search, vertical domain search, parallel batch search, and URL content extraction. |
| `browse` | Fast headless browser for QA testing and site dogfooding. (gstack) |
| `browse` | Fast headless browser for QA testing and site dogfooding. (gstack) |
| `browser-harness` | Direct browser control via CDP. Use when the user wants to automate, scrape, test, or interact with web pages. Connects to the user's already-running Chrome. |
| `clone-website` | Reverse-engineer and clone one or more websites in one shot — extracts assets, CSS, and content section-by-section and proactively dispatches parallel builder agents in worktrees a |
| `connect-chrome` | Launch GStack Browser — AI-controlled Chromium with the sidebar extension baked in. |
| `connect-chrome` | Launch GStack Browser — AI-controlled Chromium with the sidebar extension baked in. |
| `crawl` | Crawl any website and save pages as local markdown files. Use when you need to download documentation, knowledge bases, or web content for offline access or analysis. No code requi |
| `crawl` | Crawl any website and save pages as local markdown files. Use when you need to download documentation, knowledge bases, or web content for offline access or analysis. No code requi |
| `crawl4ai-skill` | Web crawling and scraping tool with LLM-optimized output. 网页爬虫爬取工具 \| Web crawler, web scraper, spider. DuckDuckGo search, site crawling, dynamic page scraping. 智能搜索爬取 \| Free, no  |
| `ego-browser` | When you need a browser, read this Skill by default. Use it to open and operate websites, fill forms, click buttons, take screenshots, extract page data, sign in, and perform other |
| `opencli-browser` | Use when an agent needs to drive a real Chrome window via opencli — inspect a page, fill forms, click through logged-in flows, or extract data ad-hoc. Covers the selector-first tar |
| `opencli-usage` | Use at the start of any OpenCLI session — this is the top-level map of what `opencli` can do, how to discover adapters, what flags and output formats are universal, and which speci |
| `playwright-cli` | Automate browser interactions, test web pages and work with Playwright tests. |
| `scrape` | Pull data from a web page. (gstack) |
| `scrape` | Pull data from a web page. (gstack) |
| `search` | Search the web using Tavily's LLM-optimized search API. Returns relevant results with content snippets, scores, and metadata. Use when you need to find web content on any topic wit |
| `search` | Search the web using Tavily's LLM-optimized search API. Returns relevant results with content snippets, scores, and metadata. Use when you need to find web content on any topic wit |

## ByteDance internal tooling

| Skill | 作用 |
| --- | --- |
| `byteval` | 用于查询和操作 Byteval 平台资源，以及自然语言新建、排查或更新 Byteval Workflow。触发场景包括：用户提到 byteval 并希望查询、创建、更新、运行或调试项目、应用、评测集、评测指标、评估器、工作流或任务；基于评测标准创建评估器或 evaluator skill；基于人工标注数据进行 LLM-as-Judge Prompt 调优；排 |
| `byteval-skill-evalkit` | 面向用户 Skill 的端到端评测编排套件（EvalKit）。当用户想对一个目标 Skill 做完整质量评测——静态检查、CLI 运行能力探针、生成评测标准与评测集、用 traex 推理跑 case、grader 打分、分析根因、产出 HTML 报告——时使用本 skill。它支持本地快速调试和 Byteval 云端正式运行两类模式；本地模式把八个能力编排成 |
| `evalbot-cli` | evalbotcli 是 EvalBot 评测平台的官方命令行工具，提供数据集、任务、评测指标和实验分析等核心能力。 EvalBot CLI 原子操作指南，仅在 evalbot-one-step 已完成路由后使用。 负责安装、认证、Libra 分析和明确的单次 CLI 操作；不得从用户原始评测请求直接触发。 用户明确要求维护本 Skill 自身代码或文档时可 |
| `labelgpt-cli` | LabelGPT CLI 助手：安装和更新 labelgpt-cli，处理认证、配置、Space、命令发现与 schema 查询，并将业务/系统 Plugin、Agent、Agent Harness Managed Agent、Dataset、PE、文档知识库、Model 与 ByteCloud Metrics 的创建、查询、编辑、调试、运行、导入导出、发布 |
| `labelgpt-cli` | LabelGPT CLI 助手：安装和更新 labelgpt-cli，处理认证、配置、Space、命令发现与 schema 查询，并将业务/系统 Plugin、Agent、Agent Harness Managed Agent、Dataset、PE、文档知识库、Model 与 ByteCloud Metrics 的创建、查询、编辑、调试、运行、导入导出、发布 |
| `meegle` | 飞书项目（Meego/Meegle）操作工具。支持查询和管理工作项、节点流转、视图查询、个人待办、排期统计等功能。 Use when user needs to work with Feishu/Lark Meego project management — including querying work items, creating/updating w |
| `meego-complete-operations` | Use when handling Meego/Meegle biweekly project creation, workflow filling, staffing schedules, historical AE migration, or legacy Meego-versus-Bitable reconciliation. |
| `meego-migration-operations` | 在 AE 数据填写从多维表迁移至 Meego 时，创建和维护 Meego 项目/需求、填写作业与交付数据、安排占编人力，并执行双平台数据核验。用户提及 Meego 迁移、需求/项目建项、POC 填写、人效、抽检或占编核对时使用。 |

## Design / UI skills

| Skill | 作用 |
| --- | --- |
| `adapt` | Adapt designs to work across different screen sizes, devices, contexts, or platforms. Implements breakpoints, fluid layouts, and touch targets. Use when the user mentions responsiv |
| `animate` | Review a feature and enhance it with purposeful animations, micro-interactions, and motion effects that improve usability and delight. Use when the user mentions adding animation,  |
| `audit` | Run technical quality checks across accessibility, performance, theming, responsive design, and anti-patterns. Generates a scored report with P0-P3 severity ratings and actionable  |
| `bolder` | Amplify safe or boring designs to make them more visually interesting and stimulating. Increases impact while maintaining usability. Use when the user says the design looks bland,  |
| `clarify` | Improve unclear UX copy, error messages, microcopy, labels, and instructions to make interfaces easier to understand. Use when the user mentions confusing text, unclear labels, bad |
| `colorize` | Add strategic color to features that are too monochromatic or lack visual interest, making interfaces more engaging and expressive. Use when the user mentions the design looking gr |
| `critique` | Evaluate design from a UX perspective, assessing visual hierarchy, information architecture, emotional resonance, cognitive load, and overall quality with quantitative scoring, per |
| `delight` | Add moments of joy, personality, and unexpected touches that make interfaces memorable and enjoyable to use. Elevates functional to delightful. Use when the user asks to add polish |
| `design-consultation` | Design consultation: understands your product, researches the landscape, proposes a complete design system (aesthetic, typography, color, layout, spacing, motion), and generates fo |
| `design-consultation` | Design consultation: understands your product, researches the landscape, proposes a complete design system (aesthetic, typography, color, layout, spacing, motion), and generates fo |
| `design-html` | Design finalization: generates production-quality Pretext-native HTML/CSS. (gstack) |
| `design-html` | Design finalization: generates production-quality Pretext-native HTML/CSS. (gstack) |
| `design-review` | Designer's eye QA: finds visual inconsistency, spacing issues, hierarchy problems, AI slop patterns, and slow interactions — then fixes them. (gstack) |
| `design-review` | Designer's eye QA: finds visual inconsistency, spacing issues, hierarchy problems, AI slop patterns, and slow interactions — then fixes them. (gstack) |
| `design-shotgun` | Design shotgun: generate multiple AI design variants, open a comparison board, collect structured feedback, and iterate. (gstack) |
| `design-shotgun` | Design shotgun: generate multiple AI design variants, open a comparison board, collect structured feedback, and iterate. (gstack) |
| `distill` | Strip designs to their essence by removing unnecessary complexity. Great design is simple, powerful, and clean. Use when the user asks to simplify, declutter, reduce noise, remove  |
| `hallmark` | Design skill for websites and new pages that look designed, not generated. Use when the user asks to build or design something new, or names Hallmark. Never use it on an existing d |
| `impeccable` | Use when the user wants to design, redesign, shape, critique, audit, polish, clarify, distill, harden, optimize, adapt, animate, colorize, extract, or otherwise improve a frontend  |
| `impeccable` | Use when the user wants to design, redesign, shape, critique, audit, polish, clarify, distill, harden, optimize, adapt, animate, colorize, extract, or otherwise improve a frontend  |
| `impeccable` | Use when the user wants to design, redesign, shape, critique, audit, polish, clarify, distill, harden, optimize, adapt, animate, colorize, extract, or otherwise improve a frontend  |
| `layout` | Improve layout, spacing, and visual rhythm. Fixes monotonous grids, inconsistent spacing, and weak visual hierarchy. Use when the user mentions layout feeling off, spacing issues,  |
| `optimize` | Diagnoses and fixes UI performance across loading speed, rendering, animations, images, and bundle size. Use when the user mentions slow, laggy, janky, performance, bundle size, lo |
| `overdrive` | Pushes interfaces past conventional limits with technically ambitious implementations — shaders, spring physics, scroll-driven reveals, 60fps animations. Use when the user wants to |
| `polish` | Performs a final quality pass fixing alignment, spacing, consistency, and micro-detail issues before shipping. Use when the user mentions polish, finishing touches, pre-launch revi |
| `quieter` | Tones down visually aggressive or overstimulating designs, reducing intensity while preserving quality. Use when the user mentions too bold, too loud, overwhelming, aggressive, gar |
| `shape` | Plan the UX and UI for a feature before writing code. Runs a structured discovery interview, then produces a design brief that guides implementation. Use during the planning phase  |
| `typeset` | Improves typography by fixing font choices, hierarchy, sizing, weight, and readability so text feels intentional. Use when the user mentions fonts, type, readability, text hierarch |
| `web-design-guidelines` | Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility", "audit design", "review UX", or "check my site against best practic |
| `web-design-guidelines` | Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility", "audit design", "review UX", or "check my site against best practic |

## Diagram skills

| Skill | 作用 |
| --- | --- |
| `archify` | Create validated architecture, workflow, sequence, data-flow, lifecycle/state, ERD, class, tree, timeline, and waterfall diagrams as explorable standalone HTML with dark/light them |
| `archify` | Create polished, validated architecture, workflow, sequence, data-flow, and lifecycle/state diagrams as explorable standalone HTML with inline SVG, dark/light themes, optional trac |
| `architecture-diagram-creator` | Create comprehensive HTML architecture diagrams showing data flows, business objectives, features, technical architecture, and deployment. Use when users request system architectur |
| `architecture-diagrams` | Create system architecture diagrams using Mermaid, PlantUML, C4 model, flowcharts, and sequence diagrams. Use when documenting architecture, system design, data flows, or technical |
| `diagram` | Turn an English description (or mermaid source) into a diagram triplet: the source, an editable .excalidraw file you can open (gstack) |
| `draw-io-diagram-generator` | Use when creating, editing, or generating draw.io diagram files (.drawio, .drawio.svg, .drawio.png). Covers mxGraph XML authoring, shape libraries, style strings, flowcharts, syste |
| `drawio-flowchart` | Creates flowcharts, swim lane diagrams, and business process diagrams using Draw.io (diagrams.net). Covers standard flowchart shapes (process, decision, start/end), connectors, aut |
| `eraser-diagrams` | Generates architecture diagrams from code, infrastructure, or descriptions. Use when user asks to visualize, diagram, or document system architecture. |
| `excalidraw-diagram-generator` | Generate Excalidraw diagrams from natural language descriptions. Use when asked to "create a diagram", "make a flowchart", "visualize a process", "draw a system architecture", "cre |
| `flowchart-creator` | Create HTML flowcharts and process diagrams with decision trees, color-coded stages, arrows, and swimlanes. Use when users request flowcharts, process diagrams, workflow visualizat |
| `mermaid-diagrams` | Comprehensive guide for creating software diagrams using Mermaid syntax. Use when users need to create, visualize, or document software through diagrams including class diagrams (d |

## Engineering guides

| Skill | 作用 |
| --- | --- |
| `android-native-dev` | Android native application development and UI design guide. Covers Material Design 3, Kotlin/Compose development, project configuration, accessibility, and build troubleshooting. R |
| `backend-development` | Guidelines for backend development in C++ and Elixir/Phoenix, covering modern language features, best practices, and production-ready patterns. |
| `coding-standards` | Baseline cross-project coding conventions for naming, readability, immutability, and code-quality review. Use detailed frontend or backend skills for framework-specific patterns. |
| `coding-standards` | Baseline cross-project coding conventions for naming, readability, immutability, and code-quality review. Use detailed frontend or backend skills for framework-specific patterns. |
| `flutter-dev` | Flutter cross-platform development guide covering widget patterns, Riverpod/Bloc state management, GoRouter navigation, performance optimization, and platform-specific implementati |
| `frontend-code-review` | Trigger when the user requests a review of frontend files (e.g., `.tsx`, `.ts`, `.js`). Support both pending-change reviews and focused file reviews while applying the checklist ru |
| `frontend-design` | Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters, or applicat |
| `frontend-dev` | Full-stack frontend development combining premium UI design, cinematic animations, AI-generated media assets, persuasive copywriting, and visual art. Builds complete, visually stri |
| `frontend-patterns` | Frontend development patterns for React, Next.js, state management, performance optimization, and UI best practices. |
| `fullstack-dev` | Full-stack backend architecture and frontend-backend integration guide. TRIGGER when: building a full-stack app, creating REST API with frontend, scaffolding backend service, build |
| `ios-application-dev` | iOS application development guide covering UIKit, SnapKit, and SwiftUI. Includes touch targets, safe areas, navigation patterns, Dynamic Type, Dark Mode, accessibility, collection  |
| `ios-clean` | Remove the DebugBridge SPM package and all #if DEBUG wiring from an iOS app. (gstack) |
| `ios-design-review` | Visual design audit for iOS apps on real hardware. (gstack) |
| `ios-fix` | Autonomous iOS bug fixer. (gstack) |
| `ios-qa` | Live-device iOS QA for SwiftUI apps. (gstack) |
| `ios-sync` | Regenerate the iOS debug bridge against the latest upstream gstack templates. (gstack) |
| `nodejs-backend-patterns` | Build production-ready Node.js backend services with Express/Fastify, implementing middleware patterns, error handling, authentication, database integration, and API design best pr |
| `react-native-dev` | React Native and Expo development guide covering components, styling, animations, navigation, state management, forms, networking, performance optimization, testing, native capabil |

## Feishu / Miaoda workflow

| Skill | 作用 |
| --- | --- |
| `feishu-aidp-eval-sync` | Use when handling the AIDP Feishu evaluation workflow in this workspace: syncing Bitable evaluation fields to Feishu Sheets by `ID`, filling missing audio parameters from `sample`  |
| `feishu-biaoge` | Use when working with Feishu sheets or bitable in this workspace, including access checks, reading and updating records/cells, downloading attachments, uploading local files, and b |
| `feishu-fixed-table-ops` | Use when reading or writing Feishu bitable or sheets with the fixed internal app credentials in this workspace. Covers tenant token retrieval, bitable record read/write, sheet read |
| `feishu-fixed-table-ops` | Use when reading or writing Feishu bitable or sheets with the fixed internal app credentials in this workspace. Covers tenant token retrieval, bitable record read/write, sheet read |
| `feishu-upload` | 上传音频文件到飞书多维表附件。先拿 token 读表，匹配本地文件，再把 WAV 上传到飞书 Drive，最后用 file_token 回写到多维表记录。需提供 app_id、app_secret、app_token、table_id。 |
| `feishu-upload` | 上传音频文件到飞书多维表附件。先拿 token 读表，匹配本地文件，再把 WAV 上传到飞书 Drive，最后用 file_token 回写到多维表记录。需提供 app_id、app_secret、app_token、table_id。 |
| `feishu_upload_skill` | Use when uploading local audio files to Feishu Bitable attachments, especially for the mono/stereo and left-channel fields in this workspace. |
| `feishu_upload_skill` | Use when uploading local audio files to Feishu Bitable attachments, especially for the mono/stereo and left-channel fields in this workspace. |
| `miaoda-agent-collab` | 妙搭（Spark/Miaoda）本地与云端 Agent 协同：判断哪些任务直接用本地 CLI、哪些需要云端调查/独立审查/限定实现；用 lark-cli apps session/chat 派发自包含任务包并回收证据；说明本地未提交、已提交、已推送与 sprint/default 集成代码如何安全进入云端及真实 dev 验证。适用于平台事实或运行时缺口、跨源 |
| `miaoda-agent-collaboration` | Coordinate local coding agents with a Miaoda cloud Agent across repository discovery, environment-specific diagnosis, branch convergence, implementation, Git pushes, L0-L3 testing  |
| `miaoda-doc-parse` | Use when user needs to parse, extract, or read content from documents (PDF, Word, Excel, PPT, etc.) Converts documents to Markdown via IDP (Intelligent Document Parsing). 触发词：文档解析, |
| `miaoda-image-understanding` | Use when user needs to understand, analyze, or describe image content. Supports image URL and local file path input. 触发词：图片理解, 图片分析, 图片描述, 识别图片, 看图, 图片识别, image understanding, desc |
| `miaoda-speech-to-text` | Use when user needs to convert audio or voice recordings to text. Supports multiple languages. 触发词：语音转文字, 音频转文字, 语音识别, speech to text, STT, 转录, 听写, 会议记录转文字, 录音转文字, transcribe, 音频识别 |
| `miaoda-text-gen-image` | Use when user needs to generate images from text descriptions. Supports various aspect ratios and AI watermark. 触发词：生成图片, 画图, 图片生成, text to image, 文字生成图片, AI 画图, 生成配图, 生成封面, 生成插图,  |
| `miaoda-web-fetch` | Use when user needs to crawl or fetch a specific URL to extract/summarize its content. Provides web-crawl command for fetching known URLs. 触发词：网页抓取, 抓取网页, 提取网页内容, web crawl, 爬取, fe |
| `miaoda-web-search` | Use when user needs to search the web for information by keywords. Provides search-summary command for web search with AI-generated summaries. 触发词：搜索, 网页搜索, 搜一下, 查一下, web search, 搜 |

## GSAP official skills

| Skill | 作用 |
| --- | --- |
| `gsap-core` | Official GSAP skill for the core API — gsap.to(), from(), fromTo(), easing, duration, stagger, defaults, gsap.matchMedia() (responsive, prefers-reduced-motion). Use when the user a |
| `gsap-frameworks` | Official GSAP skill for Vue, Svelte, and other non-React frameworks — lifecycle, scoping selectors, cleanup on unmount. Use when the user wants animation in Vue, Nuxt, Svelte, Svel |
| `gsap-performance` | Official GSAP skill for performance — prefer transforms, avoid layout thrashing, will-change, batching. Use when optimizing GSAP animations, reducing jank, or when the user asks ab |
| `gsap-plugins` | Official GSAP skill for GSAP plugins — registration, ScrollToPlugin, ScrollSmoother, Flip, Draggable, Inertia, Observer, SplitText, ScrambleText, SVG and physics plugins, CustomEas |
| `gsap-react` | Official GSAP skill for React — useGSAP hook, refs, gsap.context(), cleanup. Use when the user wants animation in React or Next.js, or asks about GSAP with React, useGSAP, or clean |
| `gsap-scrolltrigger` | Official GSAP skill for ScrollTrigger — scroll-linked animations, pinning, scrub, triggers. Use when building or recommending scroll-based animation, parallax, pinned sections, or  |
| `gsap-timeline` | Official GSAP skill for timelines — gsap.timeline(), position parameter, nesting, playback. Use when sequencing animations, choreographing keyframes, or when the user asks about an |
| `gsap-utils` | Official GSAP skill for gsap.utils — clamp, mapRange, normalize, interpolate, random, snap, toArray, wrap, pipe. Use when the user asks about gsap.utils, clamp, mapRange, random, s |

## Lark / Feishu skill suite

| Skill | 作用 |
| --- | --- |
| `lark-approval` | 飞书审批：查询和处理审批待办/已办/实例，搜索可发起审批定义、查看定义详情并发起原生审批实例。当用户要处理审批任务、查看审批实例、搜索或发起审批时使用。审批待办不是飞书任务；非审批类待办走 lark-task。不负责创建审批定义；三方审批定义不走原生提单。 |
| `lark-apps` | 妙搭（Spark/Miaoda）应用开发与托管：应用创建、本地全栈开发、云端生成迭代、创意设计（UI mockup / 可交互原型 / 线框图 / 落地页 / 仪表盘 / 幻灯片 deck / 视觉探索）、AI相关能力和飞书平台能力或者其他外部能力集成、日志/Trace/监控指标/PV/UV 查询、环境变量管理、应用协作者与协作权限设置、应用角色与成员管理、 |
| `lark-attendance` | 飞书考勤打卡：查询自己的考勤打卡记录 |
| `lark-base` | 飞书多维表格（Base）操作：建表、字段、记录、视图、统计、公式/lookup、表单、仪表盘、应用模式（BaseApp/AppMode 页面与组件）、Workspace 目录、workflow、角色权限、模板中心（多维表格模板分类/列表/搜索）；遇到 Base/多维表格/bitable、BaseApp/AppMode、/base/ 或 /app/ 链接时使用 |
| `lark-calendar` | 飞书日历：管理日历日程和会议室。查看/搜索日程、创建/更新日程、管理参会人、查询忙闲和推荐时段、预定会议室。当用户需要查看日程安排、创建/修改会议、查询/预定会议室时使用。不负责：查询过去的视频会议记录（走 lark-meeting）、待办任务（走 lark-task）。 |
| `lark-contact` | 飞书 / Lark 通讯录:按姓名 / 邮箱解析成 open_id,或按 open_id 反查姓名 / 部门 / 邮箱 / 联系方式 / 个人状态 / 签名,以及按关键词搜索当前用户可见的机器人 / 智能体(agent)。当用户提到一个名字要下一步发消息 / 排日程,或拿到 open_id 想查具体信息时使用。不负责部门树遍历、按部门列员工、组织架构图,这类 |
| `lark-doc` | 飞书云文档（Docx / Wiki）内容操作：读取、创建、编辑文档，插入或下载图片附件，以及操作思维笔记。用户提供文档 URL/token（包括 doubao.com 的 /docx/、/wiki/）时使用；按 URL 路径/token 而非域名路由；`/page/<token>` 是妙搭应用，非飞书云文档。文档内嵌资源按读取参考中的统一规则分流。独立评论操 |
| `lark-drive` | 飞书云空间（云盘/云存储）：管理 Drive 文件和文件夹，包含上传/下载、创建文件夹、复制/移动/删除、查看元数据、查询权限设置、评论/权限/订阅、标题、版本、飞书文档密级标签（secure labels）和本地文件导入。用户需要整理云盘目录、处理云空间资源 URL/token、判断链接类型/真实 token/标题，或导入 Word/Markdown/Ex |
| `lark-event` | Lark/Feishu real-time event listening / subscribing / consuming: stream events as NDJSON via `lark-cli event consume <EventKey>` (covers IM messages/reactions/chat changes, Approva |
| `lark-im` | 飞书即时通讯：收发消息和管理群聊。发送和回复消息、搜索聊天记录、管理群聊成员、上传下载图片和文件、管理表情回复、发送应用内/短信/电话加急、发送和处理交互卡片（Interactive Card）、监听卡片按钮回调（card.action.trigger）。当用户需要发消息、查看或搜索聊天记录、下载聊天中的文件、查看群成员、搜索群、创建群聊或话题群、管理标记数 |
| `lark-mail` | 飞书邮箱：Use when user mentions 起草邮件、写邮件、草稿、发送/回复/转发邮件、查阅邮件、看邮件、搜索邮件、邮件文件夹、邮件标签、邮件联系人、监听新邮件、邮件收信规则等；use for mail/email intent only. Do not use for docs/sheets/calendar/auth setup/pure  |
| `lark-markdown` | 飞书 Markdown：查看、创建、上传、编辑和比较飞书中的原生 Markdown 文件。当用户要操作飞书 Markdown 文件，或比较其远端版本及本地草稿时使用。纯本地 Markdown 文件操作不触发本 skill。不负责将 Markdown 导入为飞书在线文档，也不负责文件搜索、权限、评论、移动、删除等云空间管理操作。 |
| `lark-meeting` | 飞书视频会议：查询会议记录与会议产物(纪要/逐字稿/妙记)、妙记搜索/上传/下载/编辑、机器人参与会议；查询进行中的会议、实时会议内容(发言/聊天/共享文档)问答(会上/会里)、发送会中聊天/表情；基于 meeting_id、meeting_no、event_id、note_id、minute_token、vc-node-id 或妙记 URL 查询相关信息。 |
| `lark-minutes` | 仅当用户或上游配置显式指定 lark-minutes 时使用，相关请求统一交由 lark-meeting 技能处理。 |
| `lark-note` | 仅当用户或上游配置显式指定 lark-note 时使用，相关请求统一交由 lark-meeting 技能处理。 |
| `lark-okr` | 飞书 OKR：管理目标与关键结果。查看和编辑 OKR 周期、目标、关键结果、对齐关系、量化指标和进展记录。当用户需要查看或创建 OKR、管理目标和关键结果、查看对齐关系时使用。不负责：待办任务管理（lark-task）、日程/会议安排（lark-calendar）、绩效评估 |
| `lark-openapi-explorer` | 飞书/Lark 原生 OpenAPI 探索：从官方文档库中挖掘未经 CLI 封装的原生 OpenAPI 接口。当用户的需求无法被现有 lark-* skill 或 lark-cli 已注册命令满足，需要查找并调用原生飞书 OpenAPI 时使用。 |
| `lark-shared` | Use for lark-cli setup/auth tasks: auth login/status/logout, user vs bot identity, business-domain permissions (--domain, including all/docs/drive), missing scopes, revoking author |
| `lark-sheets` | 飞书电子表格：创建和操作电子表格。支持工作表与行列结构（增删/合并/尺寸/隐藏/冻结/分组）、单元格读写（值/公式/样式/批注/单元格图片）、区域复制移动排序填充、查找替换、批量更新，图表、透视表、条件格式、筛选器与筛选视图、下拉列表、迷你图、浮动图片等对象的创建与维护，以及公式校验、历史版本回滚、本地 Excel/CSV 与飞书表格的导入导出。当用户需要创 |
| `lark-skill-maker` | 创建 lark-cli 的自定义 Skill。当用户需要把飞书 API 操作封装成可复用的 Skill（包装原子 API 或编排多步流程）时使用。 |
| `lark-slides` | 飞书幻灯片：创建和编辑幻灯片。创建演示文稿、读取幻灯片内容、管理幻灯片页面（创建、删除、读取、局部替换）。当用户需要创建或编辑幻灯片、读取或修改单个页面时使用。当用户给出 doubao.com 的 /slides/ URL/token 时，也应直接使用本 skill，不要因为域名不是飞书而回退到 WebFetch；路由依据是 URL 路径模式和 token， |
| `lark-task` | 飞书任务：管理任务、清单和任务智能体。创建待办任务、查看和更新任务状态、拆分子任务、组织任务清单、分配协作成员、上传任务附件、注册或注销任务智能体、更新任务智能体的主页数据、写入智能体任务记录。当用户需要创建待办事项、查看任务列表、跟踪任务进度、管理项目清单或给他人分配任务、为任务上传附件文件、注册注销任务智能体、更新智能体主页数据、写入任务记录时使用。 |
| `lark-vc` | 仅当用户或上游配置显式指定 lark-vc 时使用，相关请求统一交由 lark-meeting 技能处理。 |
| `lark-vc-agent` | 仅当用户或上游配置显式指定 lark-vc-agent 时使用，相关请求统一交由 lark-meeting 技能处理。 |
| `lark-whiteboard` | 飞书画板：查询和编辑飞书云文档中的画板。支持导出画板为预览图片、导出原始节点结构、使用多种格式更新画板内容。 当用户需要查看画板内容、导出画板图片、编辑画板时使用此 skill。不负责：飞书云文档内容编辑（lark-doc）、文档内嵌电子表格/Base（lark-sheets / lark-base）。 |
| `lark-wiki` | 飞书知识库：管理知识空间、空间成员和文档节点。创建和查询知识空间、查看和管理空间成员、管理节点层级结构、在知识库中组织文档和快捷方式。当用户需要在知识库中查找或创建文档、浏览知识空间结构、查看或管理空间成员、移动或复制节点时使用。当用户给出 doubao.com 的 /wiki/ URL/token 时，也应直接使用本 skill，不要因为域名不是飞书而回退 |
| `lark-workflow-meeting-summary` | 会议纪要整理工作流：汇总指定时间范围内的会议纪要并生成结构化报告。当用户需要整理会议纪要、生成会议周报、回顾一段时间内的会议内容时使用。 |
| `lark-workflow-standup-report` | 日程待办摘要：编排 calendar +agenda 和 task +get-my-tasks，生成指定日期的日程与未完成任务摘要。适用于了解今天/明天/本周的安排。 |

## MiniMax skill suite

| Skill | 作用 |
| --- | --- |
| `minimax-docx` | Professional DOCX document creation, editing, and formatting using OpenXML SDK (.NET). Three pipelines: (A) create new documents from scratch, (B) fill/edit content in existing doc |
| `minimax-docx` | Professional DOCX document creation, editing, and formatting using OpenXML SDK (.NET). Three pipelines: (A) create new documents from scratch, (B) fill/edit content in existing doc |
| `minimax-multimodal-toolkit` | MiniMax multimodal model skill — use MiniMax Multi-Modal models for speech, music, video, and image. Create voice, music, video, and images with MiniMax AI: TTS (text-to-speech, vo |
| `minimax-pdf` | Use this skill when visual quality and design identity matter for a PDF. CREATE (generate from scratch): "make a PDF", "generate a report", "write a proposal", "create a resume", " |
| `minimax-xlsx` | Open, create, read, analyze, edit, or validate Excel/spreadsheet files (.xlsx, .xlsm, .csv, .tsv). Use when the user asks to create, build, modify, analyze, read, validate, or form |

## Other / local

| Skill | 作用 |
| --- | --- |
| `_gstack-command` | Router for the gstack skill suite. (gstack) |
| `agent-autoloop` | 配置 Agent 自动化中台：加规则、接新的事件插件、接新的 Agent、接新的通道（飞书、QQ、钉钉、企微……）、写处理手册、部署到服务器、多台电脑。用户说“有事的时候让 Agent 自己处理”“每天几点让 Agent 做某事”“接一下 GitHub / 告警 / 某个系统”“换一个模型”“在飞书里批”“加一台电脑”时用。 |
| `aimi生图` | 使用 AIME 平台的 GPT Image 2 模型生成图片。通过 ego-browser 自动化浏览器操作，打开工作空间、确认 GPT Image 2 生图模型、输入提示词并等待生成完成，最后下载图片。支持单张生成和批量并行生成。适用于需要在字节内部 AIME 平台使用 GPT Image 2 进行 AI 生图的场景。触发词：aimi生图、AIME生图、G |
| `anatomy` | Build crafted, highly detailed, interactive isometric SVG figures that explain a technical idea as a real physical object (a test rig, a dial gauge, a cabinet of drawers, a plotter |
| `autoplan` | Auto-review pipeline — reads the full CEO, design, eng, and DX review skills from disk and runs them sequentially with auto-decisions using 6 decision principles. (gstack) |
| `autoplan` | Auto-review pipeline — reads the full CEO, design, eng, and DX review skills from disk and runs them sequentially with auto-decisions using 6 decision principles. (gstack) |
| `benchmark` | Performance regression detection using the browse daemon. (gstack) |
| `benchmark` | Performance regression detection using the browse daemon. (gstack) |
| `benchmark-models` | Cross-model benchmark for gstack skills. (gstack) |
| `benchmark-models` | Cross-model benchmark for gstack skills. (gstack) |
| `canary` | Post-deploy canary monitoring. (gstack) |
| `canary` | Post-deploy canary monitoring. (gstack) |
| `careful` | Safety guardrails for destructive commands. (gstack) |
| `careful` | Safety guardrails for destructive commands. (gstack) |
| `chorus-audio-pipeline` | Use when a task involves downloading `合轨音频` from a Feishu Bitable view, applying adaptive chorus balancing to stereo audio by lightly boosting the user channel and lightly attenuat |
| `claude-to-deerflow` | Interact with DeerFlow AI agent platform via its HTTP API. Use this skill when the user wants to send messages or questions to DeerFlow for research/analysis, start a DeerFlow conv |
| `codex` | OpenAI Codex CLI wrapper — three modes. (gstack) |
| `codex` | OpenAI Codex CLI wrapper — three modes. (gstack) |
| `context-restore` | Restore working context saved earlier by /context-save. (gstack) |
| `context-restore` | Restore working context saved earlier by /context-save. (gstack) |
| `context-save` | Save working context. (gstack) |
| `context-save` | Save working context. (gstack) |
| `cso` | Chief Security Officer mode. (gstack) |
| `cso` | Chief Security Officer mode. (gstack) |
| `devex-review` | Live developer experience audit. (gstack) |
| `devex-review` | Live developer experience audit. (gstack) |
| `diagnosing-superpowers` | Use when a superpowers session went wrong and your human partner wants to know why — repeated work, ignored plans, stumbles, poor results, a skill that didn't fire, "it took too lo |
| `document-generate` | Generate missing documentation from scratch for a feature, module, or entire project. (gstack) |
| `document-release` | Post-ship documentation update. (gstack) |
| `document-release` | Post-ship documentation update. (gstack) |
| `document-style-guide` | 中文技术文档写作规范，支持撰写、润色、审校中文技术文档，检查标题层级、文本表达、段落、数值、标点和文档体系。适用于编写或修改 README、软件手册、开发指南、API 说明、教程，统一中文技术文档风格，或按中文技术写作规范检查文档；不用于单纯代码逻辑评审、文学创作或一般闲聊。 |
| `documentation-and-adrs` | Records decisions and documentation. Use when making architectural decisions, changing public APIs, shipping features, or when you need to record context that future engineers and  |
| `doubao-group-classifier` | 群聊话题整理与反馈分类助手。用于整理飞书/微信群聊记录，识别用户反馈话题并分类输出为飞书文档格式。 |
| `find-animation-opportunities` | Search a codebase or UI for places that don't animate but should, and reject everything that shouldn't. Read-only; it proposes motion with exact values, it does not implement it. U |
| `find-skills` | Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can...", or express interest in extending c |
| `freeze` | Restrict file edits to a specific directory for the session. (gstack) |
| `freeze` | Restrict file edits to a specific directory for the session. (gstack) |
| `gif-sticker-maker` | Convert photos (people, pets, objects, logos) into 4 animated GIF stickers with captions. Use when: user wants to create cartoon stickers, GIF expressions, emoji packs, animated av |
| `guard` | Full safety mode: destructive command warnings + directory-scoped edits. (gstack) |
| `guard` | Full safety mode: destructive command warnings + directory-scoped edits. (gstack) |
| `haohao-shuohua` | 好好说话：给任何 AI 产出的中文去 AI 味、去翻译腔，让表达像真人说的——定位是「AI 文本清洗与表达优化」，写作只是其中一大场景。模型回答、开发迭代里的答复、总结、汇报、周报日报、邮件、群消息、评论答疑、翻译改写、起草文档等一切要交付给人看的中文都过一遍。触发：去 AI 味、改中文、说人话、润色、改稿、这段像 AI、好好说话、加中文味，以及写文档/写周 |
| `health` | Code quality dashboard. (gstack) |
| `health` | Code quality dashboard. (gstack) |
| `humanizer-zh` | 去除文本中的 AI 生成痕迹。适用于编辑或审阅文本，使其听起来更自然、更像人类书写。 基于维基百科的"AI 写作特征"综合指南。检测并修复以下模式：夸大的象征意义、 宣传性语言、以 -ing 结尾的肤浅分析、模糊的归因、破折号过度使用、三段式法则、 AI 词汇、否定式排比、过多的连接性短语。 |
| `humanizer-zh` | 去除文本中的 AI 生成痕迹。适用于编辑或审阅文本，使其听起来更自然、更像人类书写。 基于维基百科的"AI 写作特征"综合指南。检测并修复以下模式：夸大的象征意义、 宣传性语言、以 -ing 结尾的肤浅分析、模糊的归因、破折号过度使用、三段式法则、 AI 词汇、否定式排比、过多的连接性短语。 |
| `investigate` | Systematic debugging with root cause investigation. (gstack) |
| `investigate` | Systematic debugging with root cause investigation. (gstack) |
| `land-and-deploy` | Land and deploy workflow. (gstack) |
| `land-and-deploy` | Land and deploy workflow. (gstack) |
| `landing-report` | Read-only queue dashboard for workspace-aware ship. (gstack) |
| `landing-report` | Read-only queue dashboard for workspace-aware ship. (gstack) |
| `leader` | 把一句话的想法拆成 AI agent 能独立跑完的目标任务书。用户说「帮我给 agent 写个目标」「帮我详细拆一下这个目标」「写个任务书/brief 给 agent」「写个 goal 提示词」「让 agent 自己跑这个项目」「把活分给几个 agent 并行」时使用。先进代码库实测、必要时联网调研，再一次性提问（≤5 个），产出一份 ≤4000 字符、直接 |
| `learn` | Manage project learnings. |
| `learn` | Manage project learnings. |
| `make-pdf` | Turn any markdown file into a publication-quality PDF. (gstack) |
| `make-pdf` | Turn any markdown file into a publication-quality PDF. (gstack) |
| `migrate-to-codex` | Migrate supported instruction files, skills, agents, and MCP config into Codex project and global files. |
| `modlens` | Plug-in vision for text-only models. Hard rule: when a file path or URL with an image extension (.png, .jpg, .jpeg, .webp, .gif, .heic, .heif) appears anywhere in the conversation  |
| `office-hours` | YC Office Hours — two modes. (gstack) |
| `office-hours` | YC Office Hours — two modes. (gstack) |
| `open-gstack-browser` | Launch GStack Browser — AI-controlled Chromium with the sidebar extension baked in. |
| `open-gstack-browser` | Launch GStack Browser — AI-controlled Chromium with the sidebar extension baked in. |
| `openchatcut` | Connect an MCP-capable coding agent to OpenChatCut and edit local video projects. Use when the user asks to install, connect, or set up OpenChatCut; inspect or edit an OpenChatCut  |
| `pair-agent` | Pair a remote AI agent with your browser. (gstack) |
| `pair-agent` | Pair a remote AI agent with your browser. (gstack) |
| `performance-optimizer` | Optimize application performance and scalability. Use when investigating slow applications, scaling bottlenecks, or improving response times. Use for profiling, caching, database o |
| `plan-ceo-review` | CEO/founder-mode plan review. (gstack) |
| `plan-ceo-review` | CEO/founder-mode plan review. (gstack) |
| `plan-design-review` | Designer's eye plan review — interactive, like CEO and Eng review. (gstack) |
| `plan-design-review` | Designer's eye plan review — interactive, like CEO and Eng review. (gstack) |
| `plan-devex-review` | Interactive developer experience plan review. (gstack) |
| `plan-devex-review` | Interactive developer experience plan review. (gstack) |
| `plan-eng-review` | Eng manager-mode plan review. (gstack) |
| `plan-eng-review` | Eng manager-mode plan review. (gstack) |
| `plan-tune` | Self-tuning question sensitivity + developer psychographic for gstack (v1: observational). (gstack) |
| `plan-tune` | Self-tuning question sensitivity + developer psychographic for gstack (v1: observational). (gstack) |
| `pptx-generator` | Generate, edit, and read PowerPoint presentations. Create from scratch with PptxGenJS (cover, TOC, content, section divider, summary slides), edit existing PPTX via XML workflows,  |
| `pr-review` | Review pull requests for the MiniMax Skills repository. Use when reviewing PRs, validating new skill submissions, or checking existing skills for compliance. Run the validation scr |
| `pua` | 让你的 AI 不敢摆烂。用大厂 PUA 话术穷尽一切方案。触发条件：(1) 任务失败 2+ 次或反复微调同一思路; (2) 即将说'我无法解决'、建议用户手动操作、未验证就归因环境; (3) 被动等待——不搜索、不读源码、只等指示; (4) 用户不满：'try harder'、'stop giving up'、'换个方法'、'为什么还不行'、'你再试试'、' |
| `pua` | 让你的 AI 不敢摆烂。用大厂 PUA 话术穷尽一切方案。触发条件：(1) 任务失败 2+ 次或反复微调同一思路; (2) 即将说'我无法解决'、建议用户手动操作、未验证就归因环境; (3) 被动等待——不搜索、不读源码、只等指示; (4) 用户不满：'try harder'、'stop giving up'、'换个方法'、'为什么还不行'、'你再试试'、' |
| `qa` | Systematically QA test a web application and fix bugs found. (gstack) |
| `qa` | Systematically QA test a web application and fix bugs found. (gstack) |
| `qa-only` | Report-only QA testing. (gstack) |
| `qa-only` | Report-only QA testing. (gstack) |
| `react-best-practices` | React and Next.js performance optimization guidelines from Vercel Engineering. This skill should be used when writing, reviewing, or refactoring React/Next.js code to ensure optima |
| `react-hook-best-practices` | 在编写 React Hooks 时遇到闭包陷阱、冗余 Effect、派生状态管理等问题时使用。涵盖 React 19 的 use()、useActionState、useOptimistic 等新特性，以及依赖数组管理、事件处理 vs Effect 等现代模式。React Hooks best practices for stale closures, re |
| `remembering-conversations` | Use when user asks 'how should I...' or 'what's the best approach...' after exploring code, OR when you've tried to solve something and are stuck, OR for unfamiliar workflows, OR w |
| `remembering-conversations` | You MUST invoke this skill before saying "I don't know," guessing, or treating any topic as new, no matter how trivial the question seems. It supplements other memory systems, whic |
| `retro` | Weekly engineering retrospective. (gstack) |
| `retro` | Weekly engineering retrospective. (gstack) |
| `reverse-engineer-anything` | Reverse engineer native, managed, Electron/JavaScript, packaged, firmware, and browser targets with REA. Use shipped-artifact or requested runtime evidence to explain features, com |
| `review` | Pre-landing PR review. (gstack) |
| `review` | Pre-landing PR review. (gstack) |
| `review-animations` | Reviews animation and motion code against a high craft bar derived from Emil Kowalski's design engineering philosophy. Default to flagging; approval is earned. |
| `reviewing-security-architecture` | This skill should be used when the user asks to "review the security architecture", "check authentication patterns", "evaluate trust boundaries", "review encryption implementation" |
| `secure-code-review` | Expert-level security code review that finds real vulnerabilities across any language or framework. Identifies OWASP Top 10, CWE-mapped issues, injection flaws, auth bypasses, secr |
| `self-improving-agent` | A universal self-improving agent that learns from ALL skill experiences. Uses multi-memory architecture (semantic + episodic + working) to continuously evolve the codebase. Auto-tr |
| `setup-browser-cookies` | Import cookies from your real Chromium browser into the headless browse session. (gstack) |
| `setup-browser-cookies` | Import cookies from your real Chromium browser into the headless browse session. (gstack) |
| `setup-deploy` | Configure deployment settings for /land-and-deploy. |
| `setup-deploy` | Configure deployment settings for /land-and-deploy. |
| `setup-gbrain` | Set up gbrain for this coding agent: install the CLI, initialize a local PGLite or Supabase brain, register MCP, capture per-remote trust policy. (gstack) |
| `setup-gbrain` | Set up gbrain for this coding agent: install the CLI, initialize a local PGLite or Supabase brain, register MCP, capture per-remote trust policy. (gstack) |
| `shader-dev` | Comprehensive GLSL shader techniques for creating stunning visual effects — ray marching, SDF modeling, fluid simulation, particle systems, procedural generation, lighting, post-pr |
| `ship` | Ship workflow: detect + merge base branch, run tests, review diff, bump VERSION, update CHANGELOG, commit, push, create PR. (gstack) |
| `ship` | Ship workflow: detect + merge base branch, run tests, review diff, bump VERSION, update CHANGELOG, commit, push, create PR. (gstack) |
| `skill-creator` | Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run e |
| `skill-finder` | Find existing agent skills from public directories before inventing or rewriting one. Use when the user asks for a suitable skill, similar skills, installable skills for a task, sk |
| `skillify` | Codify the most recent successful /scrape flow into a permanent browser-skill on disk. (gstack) |
| `skillify` | Codify the most recent successful /scrape flow into a permanent browser-skill on disk. (gstack) |
| `spec` | Turn vague intent into a precise, executable spec in five phases. (gstack) |
| `speechtools` | 该技能通过 Speech Tools 上传本地文件到 TOS、将 URL 转换为外链、执行 Whisper 批量语音识别，并查询历史任务或恢复结果。适用于文件上传、外链转换、Whisper 音频转写、相关任务查询与恢复，或明确提到 speechtools CLI 的请求，无需点名 Speech Tools。 |
| `spreadsheet-to-bitable-attachments` | Use when downloading attachments from Feishu spreadsheet columns and uploading them as bitable attachment fields, matching records by trial ID. Covers field type auto-creation, par |
| `spreadsheet-to-bitable-attachments` | Use when downloading attachments from Feishu spreadsheet columns and uploading them as bitable attachment fields, matching records by trial ID. Covers field type auto-creation, par |
| `storage-analyzer` | macOS / Windows 只读存储分析助手（自动识别系统）。扫描整机磁盘占用，找出 占空间大户，把每一项分成 🟢可自动清理 / 🟡需人工判断 / 🔴谨慎清理 三级并给出 可执行处置方案，生成排版精美、可折叠、命令可一键复制的交互式 HTML 报告，并可 起本地服务在网页上一键删除（移废纸篓/直接删）。扫描全程只读。务必在以下场景 使用：用户说"存储分析 |
| `supabase-postgres-best-practices` | Postgres performance optimization and best practices from Supabase. Use this skill when writing, reviewing, or optimizing Postgres queries, schema designs, or database configuratio |
| `sync-gbrain` | Keep gbrain current with this repo's code and refresh agent search guidance in CLAUDE.md. Wraps the gstack-gbrain-sync orchestrator with state (gstack) |
| `sync-gbrain` | Keep gbrain current with this repo's code and refresh agent search guidance in CLAUDE.md. Wraps the gstack-gbrain-sync orchestrator with state (gstack) |
| `token-efficiency` | Token optimization best practices for cost-effective Claude Code usage. Automatically applies efficient file reading, command execution, and output handling strategies. Includes mo |
| `token-efficiency` | Token optimization best practices for cost-effective Claude Code usage. Automatically applies efficient file reading, command execution, and output handling strategies. Includes mo |
| `typesafe-ai` | Build AI-powered software with TypeSafe: small units of AI intelligence you can use like programming primitives. Its System One models, including Jev, turn natural language and app |
| `ui-ux-pro-max` | UI/UX design intelligence for web and mobile. Includes 50+ styles, 161 color palettes, 57 font pairings, 161 product types, 99 UX guidelines, and 25 chart types across 10 stacks (R |
| `ui-ux-pro-max` | UI/UX design intelligence for web and mobile. Includes 50+ styles, 161 color palettes, 57 font pairings, 161 product types, 99 UX guidelines, and 25 chart types across 10 stacks (R |
| `unfreeze` | Clear the freeze boundary set by /freeze, allowing edits to all directories again. (gstack) |
| `unfreeze` | Clear the freeze boundary set by /freeze, allowing edits to all directories again. (gstack) |
| `vision-analysis` | Analyze, describe, and extract information from images using the MiniMax vision MCP tool. Use when: user shares an image file path or URL (any message containing .jpg, .jpeg, .png, |
| `writing-skills` | Use when creating new skills, editing existing skills, or verifying skills work before deployment |
| `writing-skills` | Use when creating new skills, editing existing skills, or verifying skills work before deployment |

## Superpowers workflow suite

| Skill | 作用 |
| --- | --- |
| `brainstorming` | You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior. Explores user intent, requirements and design befo |
| `brainstorming` | You MUST use this before any creative work - creating features, building components, adding functionality, modifying behavior, or planning anything new, in software or out of it (a |
| `dispatching-parallel-agents` | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies |
| `dispatching-parallel-agents` | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies |
| `executing-plans` | Use when you have a written implementation plan to execute in a separate session with review checkpoints |
| `executing-plans` | Use when executing an implementation plan in the current session as the implementer yourself — your human partner chose inline execution, or no subagent tool is available |
| `finishing-a-development-branch` | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work - guides completion of development work by presenting structured options for m |
| `finishing-a-development-branch` | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work |
| `receiving-code-review` | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and verificati |
| `receiving-code-review` | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and verificati |
| `requesting-code-review` | Use when completing tasks, implementing major features, or before merging to verify work meets requirements |
| `requesting-code-review` | Use when completing tasks, implementing major features, or before merging to verify work meets requirements |
| `subagent-driven-development` | Use when executing implementation plans with independent tasks in the current session |
| `subagent-driven-development` | Use when executing implementation plans with independent tasks in the current session |
| `systematic-debugging` | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes |
| `systematic-debugging` | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes |
| `test-driven-development` | Use when implementing any feature or bugfix, before writing implementation code |
| `test-driven-development` | Use when implementing any feature or bugfix, before writing implementation code |
| `using-git-worktrees` | Use when starting feature work that needs isolation from current workspace or before executing implementation plans - creates isolated git worktrees with smart directory selection  |
| `using-git-worktrees` | Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures an isolated workspace exists via native tools or git w |
| `using-superpowers` | Use when starting any conversation - establishes how to find and use skills, requiring Skill tool invocation before ANY response including clarifying questions |
| `using-superpowers` | Use when starting any conversation - establishes how to find and use skills, requiring skill invocation before ANY response including clarifying questions |
| `verification-before-completion` | Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before making any succ |
| `verification-before-completion` | Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before making any succ |
| `writing-plans` | Use when you have a spec or requirements for a multi-step task, before touching code |
| `writing-plans` | Use when you have a spec or requirements for a multi-step task, before touching code |

## gstack suite

| Skill | 作用 |
| --- | --- |
| `gstack` | Fast headless browser for QA testing and site dogfooding. Navigate pages, interact with elements, verify state, diff before/after, take annotated screenshots, test responsive layou |
| `gstack` | Router for the gstack skill suite. (gstack) |
| `gstack-autoplan` | Auto-review pipeline — reads the full CEO, design, eng, and DX review skills from disk and runs them sequentially with auto-decisions using 6 decision principles. Surfaces taste de |
| `gstack-benchmark` | Performance regression detection using the browse daemon. Establishes baselines for page load times, Core Web Vitals, and resource sizes. Compares before/after on every PR. Tracks  |
| `gstack-benchmark-models` | Cross-model benchmark for gstack skills. Runs the same prompt through Claude, GPT (via Codex CLI), and Gemini side-by-side — compares latency, tokens, cost, and optionally quality  |
| `gstack-browse` | Fast headless browser for QA testing and site dogfooding. Navigate any URL, interact with elements, verify page state, diff before/after actions, take annotated screenshots, check  |
| `gstack-canary` | Post-deploy canary monitoring. Watches the live app for console errors, performance regressions, and page failures using the browse daemon. Takes periodic screenshots, compares aga |
| `gstack-careful` | Safety guardrails for destructive commands. Warns before rm -rf, DROP TABLE, force-push, git reset --hard, kubectl delete, and similar destructive operations. User can override eac |
| `gstack-claude` | Claude Code CLI wrapper for non-Claude hosts - three modes. Review: independent diff review via claude -p. Challenge: adversarial failure-mode review. Consult: ask Claude about the |
| `gstack-context-restore` | Restore working context saved earlier by /context-save. Loads the most recent saved state (across all branches by default) so you can pick up where you left off — even across Condu |
| `gstack-context-save` | Save working context. Captures git state, decisions made, and remaining work so any future session can pick up without losing a beat. Use when asked to "save progress", "save state |
| `gstack-cso` | Chief Security Officer mode. Infrastructure-first security audit: secrets archaeology, dependency supply chain, CI/CD pipeline security, LLM/AI security, skill supply chain scannin |
| `gstack-design-consultation` | Design consultation: understands your product, researches the landscape, proposes a complete design system (aesthetic, typography, color, layout, spacing, motion), and generates fo |
| `gstack-design-html` | Design finalization: generates production-quality Pretext-native HTML/CSS. Works with approved mockups from /design-shotgun, CEO plans from /plan-ceo-review, design review context  |
| `gstack-design-review` | Designer's eye QA: finds visual inconsistency, spacing issues, hierarchy problems, AI slop patterns, and slow interactions — then fixes them. Iteratively fixes issues in source cod |
| `gstack-design-shotgun` | Design shotgun: generate multiple AI design variants, open a comparison board, collect structured feedback, and iterate. Standalone design exploration you can run anytime. Use when |
| `gstack-devex-review` | Live developer experience audit. Uses the browse tool to actually TEST the developer experience: navigates docs, tries the getting started flow, times TTHW, screenshots error messa |
| `gstack-document-release` | Post-ship documentation update. Reads all project docs, cross-references the diff, updates README/ARCHITECTURE/CONTRIBUTING/CLAUDE.md to match what shipped, polishes CHANGELOG voic |
| `gstack-freeze` | Restrict file edits to a specific directory for the session. Blocks Edit and Write outside the allowed path. Use when debugging to prevent accidentally "fixing" unrelated code, or  |
| `gstack-guard` | Full safety mode: destructive command warnings + directory-scoped edits. Combines /careful (warns before rm -rf, DROP TABLE, force-push, etc.) with /freeze (blocks edits outside a  |
| `gstack-health` | Code quality dashboard. Wraps existing project tools (type checker, linter, test runner, dead code detector, shell linter), computes a weighted composite 0-10 score, and tracks tre |
| `gstack-investigate` | Systematic debugging with root cause investigation. Four phases: investigate, analyze, hypothesize, implement. Iron Law: no fixes without root cause. Use when asked to "debug this" |
| `gstack-land-and-deploy` | Land and deploy workflow. Merges the PR, waits for CI and deploy, verifies production health via canary checks. Takes over after /ship creates the PR. Use when: "merge", "land", "d |
| `gstack-landing-report` | Read-only queue dashboard for workspace-aware ship. Shows which VERSION slots are currently claimed by open PRs, which sibling Conductor workspaces have WIP work likely to ship soo |
| `gstack-learn` | Manage project learnings. Review, search, prune, and export what gstack has learned across sessions. Use when asked to "what have we learned", "show learnings", "prune stale learni |
| `gstack-make-pdf` | Turn any markdown file into a publication-quality PDF. Proper 1in margins, intelligent page breaks, page numbers, cover pages, running headers, curly quotes and em dashes, clickabl |
| `gstack-office-hours` | YC Office Hours — two modes. Startup mode: six forcing questions that expose demand reality, status quo, desperate specificity, narrowest wedge, observation, and future-fit. Builde |
| `gstack-open-gstack-browser` | Launch GStack Browser — AI-controlled Chromium with the sidebar extension baked in. Opens a visible browser window where you can watch every action in real time. The sidebar shows  |
| `gstack-pair-agent` | Pair a remote AI agent with your browser. One command generates a setup key and prints instructions the other agent can follow to connect. Works with OpenClaw, Hermes, Codex, Curso |
| `gstack-plan-ceo-review` | CEO/founder-mode plan review. Rethink the problem, find the 10-star product, challenge premises, expand scope when it creates a better product. Four modes: SCOPE EXPANSION (dream b |
| `gstack-plan-design-review` | Designer's eye plan review — interactive, like CEO and Eng review. Rates each design dimension 0-10, explains what would make it a 10, then fixes the plan to get there. Works in pl |
| `gstack-plan-devex-review` | Interactive developer experience plan review. Explores developer personas, benchmarks against competitors, designs magical moments, and traces friction points before scoring. Three |
| `gstack-plan-eng-review` | Eng manager-mode plan review. Lock in the execution plan — architecture, data flow, diagrams, edge cases, test coverage, performance. Walks through issues interactively with opinio |
| `gstack-plan-tune` | Self-tuning question sensitivity + developer psychographic for gstack (v1: observational). Review which AskUserQuestion prompts fire across gstack skills, set per-question preferen |
| `gstack-qa` | Systematically QA test a web application and fix bugs found. Runs QA testing, then iteratively fixes bugs in source code, committing each fix atomically and re-verifying. Use when  |
| `gstack-qa-only` | Report-only QA testing. Systematically tests a web application and produces a structured report with health score, screenshots, and repro steps — but never fixes anything. Use when |
| `gstack-retro` | Weekly engineering retrospective. Analyzes commit history, work patterns, and code quality metrics with persistent history and trend tracking. Team-aware: breaks down per-person co |
| `gstack-review` | Pre-landing PR review. Analyzes diff against the base branch for SQL safety, LLM trust boundary violations, conditional side effects, and other structural issues. Use when asked to |
| `gstack-scrape` | Pull data from a web page. First call on a new intent prototypes the flow via $B primitives and returns JSON. Subsequent calls on a matching intent route to a codified browser-skil |
| `gstack-setup-browser-cookies` | Import cookies from your real Chromium browser into the headless browse session. Opens an interactive picker UI where you select which cookie domains to import. Use before QA testi |
| `gstack-setup-deploy` | Configure deployment settings for /land-and-deploy. Detects your deploy platform (Fly.io, Render, Vercel, Netlify, Heroku, GitHub Actions, custom), production URL, health check end |
| `gstack-setup-gbrain` | Set up gbrain for this coding agent: install the CLI, initialize a local PGLite or Supabase brain, register MCP, capture per-remote trust policy. One command from zero to "gbrain i |
| `gstack-ship` | Ship workflow: detect + merge base branch, run tests, review diff, bump VERSION, update CHANGELOG, commit, push, create PR. Use when asked to "ship", "deploy", "push to main", "cre |
| `gstack-skillify` | Codify the most recent successful /scrape flow into a permanent browser-skill on disk. Future /scrape calls with the same intent run the codified script in ~200ms instead of re-dri |
| `gstack-sync-gbrain` | Keep gbrain current with this repo's code and refresh agent search guidance in CLAUDE.md. Wraps the gstack-gbrain-sync orchestrator with state probing, native code-surface registra |
| `gstack-unfreeze` | Clear the freeze boundary set by /freeze, allowing edits to all directories again. Use when you want to widen edit scope without ending the session. Use when asked to "unfreeze", " |
| `gstack-upgrade` | Upgrade gstack to the latest version. |
| `gstack-upgrade` | Upgrade gstack to the latest version. |
