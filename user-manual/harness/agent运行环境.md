# Agent 运行环境

[English](agent-harness.md) · [中文](agent运行环境.md) · [Français](<Environnement d’exécution d’agents.md>) · [Deutsch](Agenten-Laufzeitumgebung.md) · [日本語](エージェント実行環境.md) · [Español](<Entorno de ejecución de agentes.md>)

## 什么是 agent 运行环境

Agent 运行环境（agent harness）是一种软件，你可以通过它向大语言模型布置任务，让模型使用文件和其他工具开展工作。
模型是发动机，运行环境则是底盘、变速箱和方向盘。
同一模型在不同运行环境中的表现可能有很大差异，因为运行环境负责管理工具、上下文、权限和执行循环。

典型的运行环境提供以下功能：

- **Agent 执行循环**：观察任务、制订计划、调用工具、读取结果、调整计划，并在完成后停止。
- **工具**：文件读写、终端命令、搜索、浏览器访问、Git，以及 MCP 或插件集成。
- **上下文管理**：对话裁剪、记忆、代码库检索和子 agent。
- **权限与安全**：操作确认、沙箱、只读或可写范围，以及网络控制。
- **可观测性与评估**：日志、执行追踪、费用统计、基准测试和回归测试。

下表概括了截至 2026 年 11 月 16 日核对的主要模型系列及接入方式。
模型的可用性取决于应用版本、套餐、地区、服务商凭据和组织设置；当前列表请参见链接中的官方模型指南。
支持某个模型不一定包含其服务使用权限：有些运行环境需要你提供 API 密钥、服务商订阅或本地模型服务器。

## 提供独立应用的运行环境

通过官方下载页面选择适合操作系统的安装程序，然后按照入门指南开始使用。

| 应用 | 主要模型及接入方式 | 官方下载 | 入门指南 |
| --- | --- | --- | --- |
| Claude 桌面应用中的 Claude Code | Claude Fable、Claude Haiku、Claude Opus 和 Claude Sonnet（[模型列表](https://code.claude.com/docs/en/model-config)）。 | [下载](https://claude.com/download) | [首次会话](https://code.claude.com/docs/en/desktop-quickstart) |
| DeepSeek Harness (DSH) | DeepSeek；配置其他服务商后还可使用 Claude、GLM、GPT 和 Kimi（[模型服务商](https://deepseek-harness.github.io/deepseek-harness/en/guide/providers)）。 | [下载](https://deepseek.com/en/harness/) | [工作区与首个任务](https://deepseek-harness.github.io/deepseek-harness/en/guide/quickstart) |
| Factory Droid | Claude、Gemini、GPT 和 Grok，以及 DeepSeek、GLM、Kimi 等开放权重模型（[模型列表](https://docs.factory.com/models)）。 | [下载](https://factory.com/product/desktop) | [首次会话](https://docs.factory.com/factory-app/quickstart) |
| Goose | 自行配置的 Claude、Gemini 和 GPT；可通过 Ollama 等服务商使用本地模型（[模型服务商](https://goose-docs.ai/docs/getting-started/providers/)）。 | [下载](https://goose-docs.ai/docs/getting-started/installation/) | [快速入门](https://goose-docs.ai/docs/quickstart/) |
| ChatGPT 桌面应用中的 OpenAI Codex | OpenAI GPT-6 Astra、GPT-6 Luna、GPT-6.1 Sol 和 GPT-6.1 Terra（[模型列表](https://learn.chatgpt.com/docs/models?surface=app)）。 | [下载](https://chatgpt.com/download/) | [快速入门](https://learn.chatgpt.com/docs/quickstart) |
| OpenCode | 通过配置的服务商或 OpenCode 托管模型目录使用 Claude、Gemini、GPT 及开放权重模型（[模型服务商](https://opencode.ai/docs/providers/)）。 | [下载](https://opencode.ai/desktop) | [连接并开始](https://opencode.ai/docs/) |

- 在 Claude 应用中打开 Code 标签页。
- 在 ChatGPT 应用菜单中选择 Codex。

## 浏览器中的云端运行环境

| 应用 | 主要模型及接入方式 | 访问设置 | 入门指南 |
| --- | --- | --- | --- |
| [Open Math OS](https://www.openmathmodel.org/) | DeepSeek、GLM、Kimi 等开放权重模型，由 SAIR Foundation 及其合作伙伴托管。 | [申请使用](https://apply.openmathmodel.org/) | [功能与流程](https://www.openmathmodel.org/) |

Open Math OS 是一个数学研究工作区，为每个项目提供云端机器、共享文件和对话，并通过 Ultramath 支持多个 agent 并行工作。
预装工具包括 Python、Lean 和 Mathlib、SageMath 以及 LaTeX。
使用 SAIR 账号登录并填写研究或团队申请，获批后即可开始使用。

## <a id="notion-ide"></a>支持 agent 运行环境的 IDE

IDE（集成开发环境）是一种应用，可以在同一工作区中编辑文件、运行程序和管理项目。
下列链接介绍编辑器的安装方式，以及如何开始使用其中的 agent 功能。
对于需要 agent 扩展的编辑器，请按照相应集成的链接指南操作。

| IDE | 主要模型及接入方式 | 官方下载 | 入门指南 |
| --- | --- | --- | --- |
| Cursor | Composer 和 Grok；符合条件的套餐还提供 Claude、Gemini 和 GPT（[模型列表](https://cursor.com/docs/models-and-pricing)）。 | [下载](https://cursor.com/download) | [首个任务](https://cursor.com/docs/get-started/quickstart) |
| Devin Desktop（原 Windsurf） | Cognition 的 SWE 系列模型，包括 SWE-2 和 SWE-2 Flash，以及 Claude、Gemini 和 GPT（[模型列表](https://docs.devin.ai/desktop/models)）。 | [下载](https://devin.ai/download) | [入门指南](https://docs.devin.ai/desktop/getting-started) |
| Eclipse Theia | 自行配置的 Claude、Gemini 和 GPT；可通过 Ollama 使用本地模型（[模型服务商](https://theia-ide.org/docs/user_ai/)）。 | [下载](https://theia-ide.org/) | [使用 AI 功能](https://theia-ide.org/docs/user_ai/) |
| Google Antigravity | Claude Opus、Claude Sonnet 和 Gemini；可选项取决于套餐（[模型列表](https://antigravity.google/docs/models)）。 | [下载](https://antigravity.google/download) | [首次会话](https://antigravity.google/docs/getting-started) |
| JetBrains IDEs | 通过 JetBrains AI 或配置的服务商使用 Claude、Gemini 和 GPT，也可连接受支持的本地模型（[模型列表](https://www.jetbrains.com/help/ai-assistant/supported-llms.html)）。 | [下载](https://www.jetbrains.com/ides/) | [在 AI Chat 中使用 agent](https://www.jetbrains.com/help/ai-assistant/ai-chat.html) |
| Kiro | Claude 和 GPT，以及 GLM、Kimi、MiniMax 等开放权重模型；Auto 可为你选择模型（[模型列表](https://kiro.dev/docs/models/available-models/)）。 | [下载](https://kiro.dev/downloads/) | [首个项目](https://kiro.dev/docs/getting-started/first-project/) |
| Positron | 通过配置的服务商使用 Claude、DeepSeek、Gemini 和 GPT；可通过 LM Studio 或 Ollama 使用本地模型（[模型服务商](https://positron.posit.co/assistant-providers.html)）。 | [下载](https://positron.posit.co/download.html) | [AI 设置与首次使用](https://positron.posit.co/assistant-getting-started.html) |
| TRAE | Gemini 和 GPT；地区性模型目录还包含 DeepSeek、GLM、Grok、Kimi、MiniMax 或 Seed，并支持自定义服务商（[模型列表](https://docs.trae.ai/ide/models?_lang=en)）。 | [下载](https://www.trae.ai/download) | [入门指南](https://docs.trae.ai/ide/get-started-with-trae-desktop?_lang=en) |
| VS Code | 通过 Copilot 或配置的服务商使用 Claude、Gemini、GPT 等模型；接入方式还取决于所选的 agent 运行环境（[模型与运行环境](https://code.visualstudio.com/features/models)）。 | [下载](https://code.visualstudio.com/download) | [Agent 快速入门](https://code.visualstudio.com/docs/agents/quickstart) |
| VSCodium | 按照此处链接设置 Cline 后，可使用 Claude、DeepSeek、Gemini 和 GPT，也可配置本地模型（[模型服务商](https://docs.cline.bot/provider-config/openrouter)）。 | [下载](https://github.com/VSCodium/vscodium/releases) | [设置 Cline](https://docs.cline.bot/getting-started/installing-cline) · [使用 Cline 执行首个任务](https://docs.cline.bot/usage/ide) |
| Zed | 托管的 Claude、Gemini 和 GPT（[模型列表](https://zed.dev/docs/account/zed-hosted-models)）；也可配置其他服务商和本地模型（[模型服务商](https://zed.dev/docs/ai/llm-providers)）。 | [下载](https://zed.dev/download) | [AI 快速入门](https://zed.dev/docs/ai/quick-start) |

## 开始使用 ACME

1. 按照官方指南安装应用或 IDE，或登录云端运行环境；按需安装 agent 扩展。
2. 按工具要求登录或配置模型服务商，然后选择模型。
3. 在应用或 IDE 中打开 ACME 项目文件夹，或将项目文件上传到云端工作区。
4. 继续按照[用户手册中的设置步骤](../用户手册.md#setup)和[设置指令示例](../user-instructions/用户指令.md#setup)操作。
