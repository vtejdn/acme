# Agent Harness

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

## Harnesses with a standalone app

This list is limited to the mainstream harnesses that provide a standalone app which can be downloaded, installed and used directly.
Model support varies by plan, region and release, so check the official documentation before committing to a setup.

| Harness | Models and providers | Notes |
| --- | --- | --- |
| Claude Code | Anthropic Claude (Opus, Sonnet, Haiku) through the Anthropic API, Amazon Bedrock or Google Vertex AI | Official support focuses on Claude; community routers can reach other models but are not official |
| DeepSeek Harness (DSH) | DeepSeek series | Other providers depend on its configuration |
| Factory Droid |  Claude, GPT and Gemini models, configured per enterprise | Commercial |
| Goose | Anthropic, OpenAI, Google, Ollama and OpenRouter | Open source |
| OpenAI Codex | OpenAI GPT and Codex models | Open-source models can be added through a custom provider |
| OpenCode | More than 75 providers through Models.dev, including OpenAI, Anthropic, Google, DeepSeek and local models | Open source |

## <a id="notion-ide"></a>IDEs with harness support

An IDE (integrated development environment) is an application that lets you edit files, run programs and manage a project in one workspace.
The following IDEs can host one or more harnesses, either as built-in agents or as installable plugins.
The plugin column lists representative integrations, not a guarantee of compatibility; check the IDE marketplace and the harness documentation.

| IDE | Harness plugins or integrations | Notes |
| --- | --- | --- |
| Cursor | Cline, Roo Code, Kilo Code and other VS Code extensions (compatibility varies) | Built-in Cursor agent is the primary harness; VS Code-based |
| Eclipse Theia | VS Code extension compatibility layer, including Cline or Roo Code where supported | Used as a base for custom IDEs; compatibility varies by distribution |
| Google Antigravity | Built-in Antigravity agent; VS Code extension compatibility where the marketplace allows | Agent-first IDE from Google |
| JetBrains IDEs | GitHub Copilot, Claude Code plugin, Continue, Sourcegraph Cody, Amazon Q Developer, Gemini Code Assist, Junie and AI Assistant | Plugin availability varies by JetBrains product |
| Kiro | Built-in Kiro agent; VS Code extensions through its marketplace | Agentic IDE from AWS built on a VS Code base |
| Positron | VS Code extension compatibility, including GitHub Copilot and Continue where supported | Data-science IDE built on VS Code; some extensions are unsupported |
| Trae | Built-in Trae agent; compatible VS Code extensions | AI IDE from ByteDance |
| VS Code | GitHub Copilot, Cline, Roo Code, Kilo Code, Continue, Sourcegraph Cody, Amazon Q Developer, Gemini Code Assist, Claude Code extension, Codex extension, Gemini CLI integration | Extensions come from the VS Code Marketplace |
| VSCodium / Code-OSS | Cline, Roo Code, Kilo Code, Continue, Codex extension, Gemini CLI integration | Uses Open VSX; Microsoft-only extensions such as GitHub Copilot are unavailable |
| Windsurf | Built-in Cascade agent; compatible VS Code extensions | Extension compatibility depends on its marketplace |
| Zed | Built-in agent panel; external agents through the Agent Client Protocol, including Claude Code and Gemini CLI | Native editor; does not use the VS Code extension ecosystem |

## References

- [Microsoft Agent Framework: Agent Harness](https://learn.microsoft.com/en-us/agent-framework/concepts/harness)
- [Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents](https://arxiv.org/abs/2609.00006)
- [Claude Code platforms and integrations](https://code.claude.com/docs/en/platforms)
- [Codex documentation](https://openai.com/codex/)
- [Gemini CLI and VS Code integration](https://developers.googleblog.com/en/gemini-cli-vs-code-native-diffing-context-aware-workflows/)
- [GitHub Copilot CLI general availability](https://github.blog/changelog/2026-06-23-github-copilot-cli-is-now-generally-available/)
- [Cursor models and pricing](https://cursor.com/docs/models-and-pricing)
- [Cline model providers](https://docs.cline.bot/sdk/model-providers)
- [OpenCode providers](https://opencode.ai/docs/providers/)
- [OpenHands LLM configuration](https://docs.openhands.dev/openhands/usage/llms/llms)
- [Qwen Code IDE integration](https://qwenlm.github.io/qwen-code-docs/en/users/ide-integration/ide-integration/)
- [Factory desktop app](https://factory.com/news/working-with-droid-in-the-desktop-app)
- [Aider (excluded CLI-only)](https://aider.chat/docs/llms/other.html)
- [SWE-agent (excluded CLI-only)](https://pypi.org/project/swe-ai-agent/)
