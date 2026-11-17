# Entorno de ejecución de agentes

[English](agent-harness.md) · [中文](agent运行环境.md) · [Français](<Environnement d’exécution d’agents.md>) · [Deutsch](Agenten-Laufzeitumgebung.md) · [日本語](エージェント実行環境.md) · [Español](<Entorno de ejecución de agentes.md>)

## Qué es un entorno de ejecución de agentes

Un entorno de ejecución de agentes (agent harness) es un programa que permite asignar una tarea a un modelo de lenguaje grande y dejar que trabaje con archivos y otras herramientas.
El modelo es el motor; el entorno de ejecución es el chasis, la caja de cambios y el volante.
Un mismo modelo puede comportarse de forma muy distinta en diferentes entornos, porque estos controlan las herramientas, el contexto, los permisos y el bucle de ejecución.

Un entorno de ejecución suele proporcionar:

- **Un bucle de ejecución del agente**: observar la tarea, planificar, llamar a herramientas, leer los resultados, revisar el plan y detenerse al terminar.
- **Herramientas**: lectura y edición de archivos, comandos de terminal, búsqueda, acceso al navegador, Git e integraciones MCP o complementos.
- **Gestión del contexto**: reducción del historial de conversación, memoria, búsqueda en el código y subagentes.
- **Permisos y seguridad**: solicitudes de aprobación, entornos aislados, ámbitos de solo lectura o con escritura y controles de red.
- **Observabilidad y evaluación**: registros, trazas de ejecución, seguimiento de costes, pruebas comparativas y pruebas de regresión.

Las tablas siguientes resumen las principales familias de modelos y las formas de acceso comprobadas el 16 de noviembre de 2026.
La disponibilidad depende de la versión de la aplicación, el plan, la región, las credenciales del proveedor y la configuración de la organización; consulte los enlaces a las guías oficiales para ver la lista actual.
La compatibilidad con un modelo no incluye necesariamente el acceso a su servicio: algunos entornos requieren su propia clave API, una suscripción al proveedor o un servidor de modelos local.

## Entornos con aplicación independiente

En la página oficial de descarga, elija el instalador correspondiente a su sistema operativo y siga la guía de inicio.

| Aplicación | Modelos principales y acceso | Descarga oficial | Primeros pasos |
| --- | --- | --- | --- |
| Claude Code en la aplicación de escritorio de Claude | Claude Fable, Claude Haiku, Claude Opus y Claude Sonnet ([Modelos](https://code.claude.com/docs/en/model-config)). | [Descargar](https://claude.com/download) | [Primera sesión](https://code.claude.com/docs/en/desktop-quickstart) |
| DeepSeek Harness (DSH) | DeepSeek; los proveedores configurados también ofrecen Claude, GLM, GPT y Kimi ([Proveedores](https://deepseek-harness.github.io/deepseek-harness/en/guide/providers)). | [Descargar](https://deepseek.com/en/harness/) | [Espacio de trabajo y primera tarea](https://deepseek-harness.github.io/deepseek-harness/en/guide/quickstart) |
| Factory Droid | Claude, Gemini, GPT y Grok, además de modelos de pesos abiertos como DeepSeek, GLM y Kimi ([Modelos](https://docs.factory.com/models)). | [Descargar](https://factory.com/product/desktop) | [Primera sesión](https://docs.factory.com/factory-app/quickstart) |
| Goose | Claude, Gemini y GPT configurados por el usuario; modelos locales mediante Ollama y otros proveedores ([Proveedores](https://goose-docs.ai/docs/getting-started/providers/)). | [Descargar](https://goose-docs.ai/docs/getting-started/installation/) | [Inicio rápido](https://goose-docs.ai/docs/quickstart/) |
| OpenAI Codex en la aplicación de escritorio de ChatGPT | OpenAI GPT-6 Astra, GPT-6 Luna, GPT-6.1 Sol y GPT-6.1 Terra ([Modelos](https://learn.chatgpt.com/docs/models?surface=app)). | [Descargar](https://chatgpt.com/download/) | [Inicio rápido](https://learn.chatgpt.com/docs/quickstart) |
| OpenCode | Claude, Gemini, GPT y modelos de pesos abiertos mediante proveedores configurados o el catálogo alojado de OpenCode ([Proveedores](https://opencode.ai/docs/providers/)). | [Descargar](https://opencode.ai/desktop) | [Conectar y empezar](https://opencode.ai/docs/) |

- En la aplicación Claude, abra la pestaña Code.
- En la aplicación ChatGPT, seleccione Codex en el menú de la aplicación.

## Entornos en la nube desde el navegador

| Aplicación | Modelos principales y acceso | Configuración del acceso | Primeros pasos |
| --- | --- | --- | --- |
| [Open Math OS](https://www.openmathmodel.org/) | Modelos de pesos abiertos, incluidos DeepSeek, GLM y Kimi, alojados por SAIR Foundation y sus socios. | [Solicitar acceso](https://apply.openmathmodel.org/) | [Funciones y flujo de trabajo](https://www.openmathmodel.org/) |

Open Math OS es un espacio de trabajo para la investigación matemática con una máquina en la nube por proyecto, archivos y conversaciones compartidos y agentes que trabajan en paralelo mediante Ultramath.
Las herramientas preinstaladas incluyen Python, Lean y Mathlib, SageMath y LaTeX.
Inicie sesión con una cuenta SAIR y complete la solicitud sobre su investigación o su equipo; el acceso comienza tras la aprobación.

## <a id="notion-ide"></a>IDE compatibles con entornos de ejecución de agentes

Un IDE (entorno de desarrollo integrado) es una aplicación que permite editar archivos, ejecutar programas y gestionar un proyecto en un mismo espacio de trabajo.
Los enlaces siguientes explican cómo instalar el editor y empezar a utilizar sus funciones de agente.
Si el editor requiere una extensión de agente, siga la guía enlazada de esa integración.

| IDE | Modelos principales y acceso | Descarga oficial | Primeros pasos |
| --- | --- | --- | --- |
| Cursor | Composer y Grok; Claude, Gemini y GPT con los planes que los incluyen ([Modelos](https://cursor.com/docs/models-and-pricing)). | [Descargar](https://cursor.com/download) | [Primera tarea](https://cursor.com/docs/get-started/quickstart) |
| Devin Desktop (antes Windsurf) | Modelos SWE de Cognition, incluidos SWE-2 y SWE-2 Flash, además de Claude, Gemini y GPT ([Modelos](https://docs.devin.ai/desktop/models)). | [Descargar](https://devin.ai/download) | [Primeros pasos](https://docs.devin.ai/desktop/getting-started) |
| Eclipse Theia | Claude, Gemini y GPT configurados por el usuario; modelos locales mediante Ollama ([Proveedores](https://theia-ide.org/docs/user_ai/)). | [Descargar](https://theia-ide.org/) | [Usar las funciones de IA](https://theia-ide.org/docs/user_ai/) |
| Google Antigravity | Claude Opus, Claude Sonnet y Gemini; las opciones dependen del plan ([Modelos](https://antigravity.google/docs/models)). | [Descargar](https://antigravity.google/download) | [Primera sesión](https://antigravity.google/docs/getting-started) |
| JetBrains IDEs | Claude, Gemini y GPT mediante JetBrains AI o proveedores configurados; también se pueden conectar modelos locales compatibles ([Modelos](https://www.jetbrains.com/help/ai-assistant/supported-llms.html)). | [Descargar](https://www.jetbrains.com/ides/) | [Usar agentes en AI Chat](https://www.jetbrains.com/help/ai-assistant/ai-chat.html) |
| Kiro | Claude y GPT, además de modelos de pesos abiertos como GLM, Kimi y MiniMax; Auto puede elegir los modelos por usted ([Modelos](https://kiro.dev/docs/models/available-models/)). | [Descargar](https://kiro.dev/downloads/) | [Primer proyecto](https://kiro.dev/docs/getting-started/first-project/) |
| Positron | Claude, DeepSeek, Gemini y GPT mediante proveedores configurados; modelos locales mediante LM Studio u Ollama ([Proveedores](https://positron.posit.co/assistant-providers.html)). | [Descargar](https://positron.posit.co/download.html) | [Configuración de IA y primer uso](https://positron.posit.co/assistant-getting-started.html) |
| TRAE | Gemini y GPT; los catálogos regionales también incluyen DeepSeek, GLM, Grok, Kimi, MiniMax o Seed y admiten proveedores personalizados ([Modelos](https://docs.trae.ai/ide/models?_lang=en)). | [Descargar](https://www.trae.ai/download) | [Primeros pasos](https://docs.trae.ai/ide/get-started-with-trae-desktop?_lang=en) |
| VS Code | Claude, Gemini, GPT y otros modelos mediante Copilot o proveedores configurados; el acceso también depende del entorno de ejecución elegido ([Modelos y entornos de ejecución](https://code.visualstudio.com/features/models)). | [Descargar](https://code.visualstudio.com/download) | [Inicio rápido con agentes](https://code.visualstudio.com/docs/agents/quickstart) |
| VSCodium | Con la configuración de Cline enlazada aquí: Claude, DeepSeek, Gemini y GPT, con modelos locales también configurables ([Proveedores](https://docs.cline.bot/provider-config/openrouter)). | [Descargar](https://github.com/VSCodium/vscodium/releases) | [Configurar Cline](https://docs.cline.bot/getting-started/installing-cline) · [Primera tarea con Cline](https://docs.cline.bot/usage/ide) |
| Zed | Claude, Gemini y GPT alojados ([Modelos](https://zed.dev/docs/account/zed-hosted-models)); también se pueden configurar otros proveedores y modelos locales ([Proveedores](https://zed.dev/docs/ai/llm-providers)). | [Descargar](https://zed.dev/download) | [Inicio rápido de IA](https://zed.dev/docs/ai/quick-start) |

## Empezar a utilizar ACME

1. Instale una aplicación o un IDE siguiendo su guía oficial, o inicie sesión en un entorno en la nube; instale una extensión de agente si es necesario.
2. Inicie sesión o configure un proveedor de modelos según lo requiera la herramienta y, después, seleccione un modelo.
3. Abra la carpeta de su proyecto ACME en la aplicación o el IDE, o suba los archivos del proyecto al espacio de trabajo en la nube.
4. Continúe con los [pasos de configuración del manual](<../Manual de usuario.md#setup>) y los [ejemplos de instrucciones de configuración](<../user-instructions/Ejemplos de instrucciones.md#setup>).
