# Agent Harness

[English](agent-harness.md) · [中文](agent运行环境.md) · [Français](<Environnement d’exécution d’agents.md>) · [Deutsch](Agenten-Laufzeitumgebung.md) · [日本語](エージェント実行環境.md) · [Español](<Entorno de ejecución de agentes.md>)

## What an agent harness is

An agent harness is software that lets you give a large language model a task and allows it to work with files and other tools.
The model is the engine; the harness is the chassis, gearbox and steering wheel.
The same model can behave very differently under different harnesses because the harness controls tools, context, permissions and the execution loop.

A typical harness provides:

- **An agent loop**: observe the task, plan, call tools, read results, revise the plan, and stop when done.
- **Tools**: file reading and editing, terminal commands, search, browser access, Git, and MCP or plugin integrations.
- **Context management**: conversation trimming, memory, codebase retrieval and subagents.
- **Permissions and safety**: approval prompts, sandboxes, read-only or writable scopes, and network controls.
- **Observability and evaluation**: logs, traces, cost tracking, benchmarks and regression tests.

The tables below summarize major model families and access options checked on 16 November 2026.
Model availability depends on the app version, plan, region, provider credentials and organization settings; follow the linked official model guides for the current list.
Support for a model does not necessarily include access to its service: some harnesses require your own API key, provider subscription or local model server.

## Harnesses with a standalone app

Use the official download page to choose an installer for your operating system, then follow the getting-started guide.

| App | Main models and access | Official download | Getting started |
| --- | --- | --- | --- |
| Claude Code in the Claude desktop app | Claude Fable, Claude Haiku, Claude Opus and Claude Sonnet ([Models](https://code.claude.com/docs/en/model-config)). | [Download](https://claude.com/download) | [First session](https://code.claude.com/docs/en/desktop-quickstart) |
| DeepSeek Harness (DSH) | DeepSeek; configured providers also offer Claude, GLM, GPT and Kimi ([Providers](https://deepseek-harness.github.io/deepseek-harness/en/guide/providers)). | [Download](https://deepseek.com/en/harness/) | [Workspace and first task](https://deepseek-harness.github.io/deepseek-harness/en/guide/quickstart) |
| Factory Droid | Claude, Gemini, GPT and Grok, plus open-weight models such as DeepSeek, GLM and Kimi ([Models](https://docs.factory.com/models)). | [Download](https://factory.com/product/desktop) | [First session](https://docs.factory.com/factory-app/quickstart) |
| Goose | User-configured Claude, Gemini and GPT; local models through Ollama and other providers ([Providers](https://goose-docs.ai/docs/getting-started/providers/)). | [Download](https://goose-docs.ai/docs/getting-started/installation/) | [Quickstart](https://goose-docs.ai/docs/quickstart/) |
| OpenAI Codex in the ChatGPT desktop app | OpenAI GPT-6 Astra, GPT-6 Luna, GPT-6.1 Sol and GPT-6.1 Terra ([Models](https://learn.chatgpt.com/docs/models?surface=app)). | [Download](https://chatgpt.com/download/) | [Quickstart](https://learn.chatgpt.com/docs/quickstart) |
| OpenCode | Claude, Gemini, GPT and open-weight models through configured providers or OpenCode's hosted catalog ([Providers](https://opencode.ai/docs/providers/)). | [Download](https://opencode.ai/desktop) | [Connect and start](https://opencode.ai/docs/) |

- In the Claude app, open the Code tab.
- in the ChatGPT app, select Codex from the app menu.

## Cloud harnesses in the browser

| App | Main models and access | Access setup | Getting started |
| --- | --- | --- | --- |
| [Open Math OS](https://www.openmathmodel.org/) | Open-weight models including DeepSeek, GLM and Kimi, hosted by SAIR Foundation and its partners. | [Apply for access](https://apply.openmathmodel.org/) | [Features and workflow](https://www.openmathmodel.org/) |

Open Math OS is a workspace for mathematical research with a cloud machine for each project, shared files and conversations, and parallel agents through Ultramath.
Its preinstalled tools include Python, Lean and Mathlib, SageMath and LaTeX .
Sign in with a SAIR account and complete the research or team application; access begins after approval.

## <a id="notion-ide"></a>IDEs with harness support

An IDE (integrated development environment) is an application that lets you edit files, run programs and manage a project in one workspace.
The links below cover installing the editor and starting with its agent features.
For editors that need an agent extension, follow the linked guide for that integration.

| IDE | Main models and access | Official download | Getting started |
| --- | --- | --- | --- |
| Cursor | Composer and Grok; Claude, Gemini and GPT on eligible plans ([Models](https://cursor.com/docs/models-and-pricing)). | [Download](https://cursor.com/download) | [First task](https://cursor.com/docs/get-started/quickstart) |
| Devin Desktop (formerly Windsurf) | Cognition SWE models, including SWE-2 and SWE-2 Flash, plus Claude, Gemini and GPT ([Models](https://docs.devin.ai/desktop/models)). | [Download](https://devin.ai/download) | [Getting started](https://docs.devin.ai/desktop/getting-started) |
| Eclipse Theia | User-configured Claude, Gemini and GPT; local models through Ollama ([Providers](https://theia-ide.org/docs/user_ai/)). | [Download](https://theia-ide.org/) | [Use AI features](https://theia-ide.org/docs/user_ai/) |
| Google Antigravity | Claude Opus, Claude Sonnet and Gemini; choices depend on the plan ([Models](https://antigravity.google/docs/models)). | [Download](https://antigravity.google/download) | [First session](https://antigravity.google/docs/getting-started) |
| JetBrains IDEs | Claude, Gemini and GPT through JetBrains AI or configured providers; supported local models can also be connected ([Models](https://www.jetbrains.com/help/ai-assistant/supported-llms.html)). | [Download](https://www.jetbrains.com/ides/) | [Use agents in AI Chat](https://www.jetbrains.com/help/ai-assistant/ai-chat.html) |
| Kiro | Claude and GPT, plus open-weight choices such as GLM, Kimi and MiniMax; Auto can select models for you ([Models](https://kiro.dev/docs/models/available-models/)). | [Download](https://kiro.dev/downloads/) | [First project](https://kiro.dev/docs/getting-started/first-project/) |
| Positron | Claude, DeepSeek, Gemini and GPT through configured providers; local models through LM Studio or Ollama ([Providers](https://positron.posit.co/assistant-providers.html)). | [Download](https://positron.posit.co/download.html) | [AI setup and first use](https://positron.posit.co/assistant-getting-started.html) |
| TRAE | Gemini and GPT; regional catalogs also include DeepSeek, GLM, Grok, Kimi, MiniMax or Seed, with custom providers supported ([Models](https://docs.trae.ai/ide/models?_lang=en)). | [Download](https://www.trae.ai/download) | [Getting started](https://docs.trae.ai/ide/get-started-with-trae-desktop?_lang=en) |
| VS Code | Claude, Gemini, GPT and other models through Copilot or configured providers; access also depends on the chosen agent harness ([Models and harnesses](https://code.visualstudio.com/features/models)). | [Download](https://code.visualstudio.com/download) | [Agents quickstart](https://code.visualstudio.com/docs/agents/quickstart) |
| VSCodium | Through the Cline setup linked here: Claude, DeepSeek, Gemini and GPT, with local models also configurable ([Providers](https://docs.cline.bot/provider-config/openrouter)). | [Download](https://github.com/VSCodium/vscodium/releases) | [Set up Cline](https://docs.cline.bot/getting-started/installing-cline) · [First task with Cline](https://docs.cline.bot/usage/ide) |
| Zed | Hosted Claude, Gemini and GPT ([Models](https://zed.dev/docs/account/zed-hosted-models)); additional providers and local models can be configured ([Providers](https://zed.dev/docs/ai/llm-providers)). | [Download](https://zed.dev/download) | [AI quickstart](https://zed.dev/docs/ai/quick-start) |

## Start using ACME

1. Install an app or IDE using its official guide, or sign in to a cloud harness; install an agent extension if needed.
2. Sign in or configure a model provider as required by the tool, then select a model.
3. Open your ACME project folder in the app or IDE, or upload the project files to the cloud workspace.
4. Continue with the [user manual's setup steps](../user-manual.md#setup) and [setup instruction examples](../user-instructions/user-instructions.md#setup).
