# Agenten-Laufzeitumgebung

[English](agent-harness.md) · [中文](agent运行环境.md) · [Français](<Environnement d’exécution d’agents.md>) · [Deutsch](Agenten-Laufzeitumgebung.md) · [日本語](エージェント実行環境.md) · [Español](<Entorno de ejecución de agentes.md>)

## Was ist eine Agenten-Laufzeitumgebung?

Eine Agenten-Laufzeitumgebung (Agent Harness) ist Software, mit der Sie einem großen Sprachmodell eine Aufgabe geben und es mit Dateien und anderen Werkzeugen arbeiten lassen können.
Das Modell ist der Motor; die Laufzeitumgebung stellt Fahrgestell, Getriebe und Lenkrad bereit.
Dasselbe Modell kann sich in verschiedenen Laufzeitumgebungen sehr unterschiedlich verhalten, da diese Werkzeuge, Kontext, Berechtigungen und die Ausführungsschleife steuern.

Eine typische Laufzeitumgebung bietet:

- **Eine Agentenschleife**: Aufgabe erfassen, planen, Werkzeuge aufrufen, Ergebnisse lesen, den Plan anpassen und nach Abschluss stoppen.
- **Werkzeuge**: Dateien lesen und bearbeiten, Terminalbefehle, Suche, Browserzugriff, Git sowie MCP- oder Plugin-Integrationen.
- **Kontextverwaltung**: Gesprächsverläufe kürzen, Gedächtnis, Suche im Quellcode und Unteragenten.
- **Berechtigungen und Sicherheit**: Bestätigungsabfragen, Sandboxes, schreibgeschützte oder beschreibbare Bereiche und Netzwerkkontrollen.
- **Beobachtbarkeit und Bewertung**: Protokolle, Ausführungsspuren, Kostenübersichten, Benchmarks und Regressionstests.

Die folgenden Tabellen fassen wichtige Modellfamilien und Zugangswege zusammen, die am 16. November 2026 geprüft wurden.
Die Verfügbarkeit hängt von Anwendungsversion, Tarif, Region, Anbieterzugangsdaten und Organisationseinstellungen ab; die aktuelle Liste finden Sie in den verlinkten offiziellen Modellbeschreibungen.
Die Unterstützung eines Modells umfasst nicht unbedingt den Zugang zu seinem Dienst: Manche Laufzeitumgebungen benötigen einen eigenen API-Schlüssel, ein Anbieterabonnement oder einen lokalen Modellserver.

## Laufzeitumgebungen mit eigenständiger Anwendung

Wählen Sie auf der offiziellen Downloadseite ein Installationsprogramm für Ihr Betriebssystem und folgen Sie anschließend der Anleitung für die ersten Schritte.

| Anwendung | Wichtige Modelle und Zugang | Offizieller Download | Erste Schritte |
| --- | --- | --- | --- |
| Claude Code in der Claude-Desktopanwendung | Claude Fable, Claude Haiku, Claude Opus und Claude Sonnet ([Modelle](https://code.claude.com/docs/en/model-config)). | [Herunterladen](https://claude.com/download) | [Erste Sitzung](https://code.claude.com/docs/en/desktop-quickstart) |
| DeepSeek Harness (DSH) | DeepSeek; konfigurierte Anbieter bieten auch Claude, GLM, GPT und Kimi ([Anbieter](https://deepseek-harness.github.io/deepseek-harness/en/guide/providers)). | [Herunterladen](https://deepseek.com/en/harness/) | [Arbeitsbereich und erste Aufgabe](https://deepseek-harness.github.io/deepseek-harness/en/guide/quickstart) |
| Factory Droid | Claude, Gemini, GPT und Grok sowie Modelle mit offenen Gewichten wie DeepSeek, GLM und Kimi ([Modelle](https://docs.factory.com/models)). | [Herunterladen](https://factory.com/product/desktop) | [Erste Sitzung](https://docs.factory.com/factory-app/quickstart) |
| Goose | Selbst konfigurierte Claude-, Gemini- und GPT-Modelle; lokale Modelle über Ollama und andere Anbieter ([Anbieter](https://goose-docs.ai/docs/getting-started/providers/)). | [Herunterladen](https://goose-docs.ai/docs/getting-started/installation/) | [Schnellstart](https://goose-docs.ai/docs/quickstart/) |
| OpenAI Codex in der ChatGPT-Desktopanwendung | OpenAI GPT-6 Astra, GPT-6 Luna, GPT-6.1 Sol und GPT-6.1 Terra ([Modelle](https://learn.chatgpt.com/docs/models?surface=app)). | [Herunterladen](https://chatgpt.com/download/) | [Schnellstart](https://learn.chatgpt.com/docs/quickstart) |
| OpenCode | Claude, Gemini, GPT und Modelle mit offenen Gewichten über konfigurierte Anbieter oder den von OpenCode gehosteten Katalog ([Anbieter](https://opencode.ai/docs/providers/)). | [Herunterladen](https://opencode.ai/desktop) | [Verbinden und starten](https://opencode.ai/docs/) |

- Öffnen Sie in der Claude-Anwendung den Reiter Code.
- Wählen Sie in der ChatGPT-Anwendung Codex im Anwendungsmenü.

## Cloud-Laufzeitumgebungen im Browser

| Anwendung | Wichtige Modelle und Zugang | Zugang einrichten | Erste Schritte |
| --- | --- | --- | --- |
| [Open Math OS](https://www.openmathmodel.org/) | Modelle mit offenen Gewichten, darunter DeepSeek, GLM und Kimi, gehostet von SAIR Foundation und ihren Partnern. | [Zugang beantragen](https://apply.openmathmodel.org/) | [Funktionen und Arbeitsablauf](https://www.openmathmodel.org/) |

Open Math OS ist ein Arbeitsbereich für mathematische Forschung mit einem Cloud-Rechner pro Projekt, gemeinsamen Dateien und Gesprächen sowie parallelen Agenten über Ultramath.
Zu den vorinstallierten Werkzeugen gehören Python, Lean und Mathlib, SageMath und LaTeX.
Melden Sie sich mit einem SAIR-Konto an und füllen Sie den Antrag zu Ihrer Forschung oder Ihrem Team aus; der Zugang beginnt nach der Genehmigung.

## <a id="notion-ide"></a>IDEs mit Unterstützung für Agenten-Laufzeitumgebungen

Eine IDE (integrierte Entwicklungsumgebung) ist eine Anwendung, mit der Sie Dateien bearbeiten, Programme ausführen und ein Projekt in einem Arbeitsbereich verwalten können.
Die folgenden Links führen zur Installation des Editors und zu den ersten Schritten mit seinen Agentenfunktionen.
Benötigt der Editor eine Agentenerweiterung, folgen Sie der verlinkten Anleitung für diese Integration.

| IDE | Wichtige Modelle und Zugang | Offizieller Download | Erste Schritte |
| --- | --- | --- | --- |
| Cursor | Composer und Grok; Claude, Gemini und GPT in entsprechenden Tarifen ([Modelle](https://cursor.com/docs/models-and-pricing)). | [Herunterladen](https://cursor.com/download) | [Erste Aufgabe](https://cursor.com/docs/get-started/quickstart) |
| Devin Desktop (ehemals Windsurf) | SWE-Modelle von Cognition, darunter SWE-2 und SWE-2 Flash, sowie Claude, Gemini und GPT ([Modelle](https://docs.devin.ai/desktop/models)). | [Herunterladen](https://devin.ai/download) | [Erste Schritte](https://docs.devin.ai/desktop/getting-started) |
| Eclipse Theia | Selbst konfigurierte Claude-, Gemini- und GPT-Modelle; lokale Modelle über Ollama ([Anbieter](https://theia-ide.org/docs/user_ai/)). | [Herunterladen](https://theia-ide.org/) | [KI-Funktionen nutzen](https://theia-ide.org/docs/user_ai/) |
| Google Antigravity | Claude Opus, Claude Sonnet und Gemini; die Auswahl hängt vom Tarif ab ([Modelle](https://antigravity.google/docs/models)). | [Herunterladen](https://antigravity.google/download) | [Erste Sitzung](https://antigravity.google/docs/getting-started) |
| JetBrains IDEs | Claude, Gemini und GPT über JetBrains AI oder konfigurierte Anbieter; unterstützte lokale Modelle lassen sich ebenfalls verbinden ([Modelle](https://www.jetbrains.com/help/ai-assistant/supported-llms.html)). | [Herunterladen](https://www.jetbrains.com/ides/) | [Agenten in AI Chat nutzen](https://www.jetbrains.com/help/ai-assistant/ai-chat.html) |
| Kiro | Claude und GPT sowie Modelle mit offenen Gewichten wie GLM, Kimi und MiniMax; Auto kann Modelle für Sie auswählen ([Modelle](https://kiro.dev/docs/models/available-models/)). | [Herunterladen](https://kiro.dev/downloads/) | [Erstes Projekt](https://kiro.dev/docs/getting-started/first-project/) |
| Positron | Claude, DeepSeek, Gemini und GPT über konfigurierte Anbieter; lokale Modelle über LM Studio oder Ollama ([Anbieter](https://positron.posit.co/assistant-providers.html)). | [Herunterladen](https://positron.posit.co/download.html) | [KI einrichten und erstmals nutzen](https://positron.posit.co/assistant-getting-started.html) |
| TRAE | Gemini und GPT; regionale Kataloge enthalten auch DeepSeek, GLM, Grok, Kimi, MiniMax oder Seed, und eigene Anbieter lassen sich konfigurieren ([Modelle](https://docs.trae.ai/ide/models?_lang=en)). | [Herunterladen](https://www.trae.ai/download) | [Erste Schritte](https://docs.trae.ai/ide/get-started-with-trae-desktop?_lang=en) |
| VS Code | Claude, Gemini, GPT und weitere Modelle über Copilot oder konfigurierte Anbieter; der Zugang hängt auch von der gewählten Agenten-Laufzeitumgebung ab ([Modelle und Laufzeitumgebungen](https://code.visualstudio.com/features/models)). | [Herunterladen](https://code.visualstudio.com/download) | [Schnellstart mit Agenten](https://code.visualstudio.com/docs/agents/quickstart) |
| VSCodium | Mit der hier verlinkten Cline-Einrichtung: Claude, DeepSeek, Gemini und GPT; lokale Modelle sind ebenfalls konfigurierbar ([Anbieter](https://docs.cline.bot/provider-config/openrouter)). | [Herunterladen](https://github.com/VSCodium/vscodium/releases) | [Cline einrichten](https://docs.cline.bot/getting-started/installing-cline) · [Erste Aufgabe mit Cline](https://docs.cline.bot/usage/ide) |
| Zed | Gehostete Claude-, Gemini- und GPT-Modelle ([Modelle](https://zed.dev/docs/account/zed-hosted-models)); weitere Anbieter und lokale Modelle lassen sich konfigurieren ([Anbieter](https://zed.dev/docs/ai/llm-providers)). | [Herunterladen](https://zed.dev/download) | [KI-Schnellstart](https://zed.dev/docs/ai/quick-start) |

## ACME verwenden

1. Installieren Sie eine Anwendung oder IDE nach der offiziellen Anleitung oder melden Sie sich bei einer Cloud-Laufzeitumgebung an; installieren Sie bei Bedarf eine Agentenerweiterung.
2. Melden Sie sich an oder konfigurieren Sie einen Modellanbieter gemäß den Anforderungen des Werkzeugs und wählen Sie dann ein Modell.
3. Öffnen Sie Ihren ACME-Projektordner in der Anwendung oder IDE oder laden Sie die Projektdateien in den Cloud-Arbeitsbereich hoch.
4. Folgen Sie anschließend den [Einrichtungsschritten im Benutzerhandbuch](../Benutzerhandbuch.md#setup) und den [Anweisungsbeispielen zur Einrichtung](../user-instructions/Anweisungsbeispiele.md#setup).
