# Environnement d’exécution d’agents

[English](agent-harness.md) · [中文](agent运行环境.md) · [Français](<Environnement d’exécution d’agents.md>) · [Deutsch](Agenten-Laufzeitumgebung.md) · [日本語](エージェント実行環境.md) · [Español](<Entorno de ejecución de agentes.md>)

## Qu’est-ce qu’un environnement d’exécution d’agents ?

Un environnement d’exécution d’agents (agent harness) est un logiciel qui permet de confier une tâche à un grand modèle de langage et de le laisser travailler avec des fichiers et d’autres outils.
Le modèle est le moteur ; l’environnement d’exécution est le châssis, la boîte de vitesses et le volant.
Un même modèle peut se comporter très différemment selon l’environnement, car celui-ci gère les outils, le contexte, les autorisations et la boucle d’exécution.

Un environnement d’exécution fournit généralement :

- **Une boucle d’exécution de l’agent** : observer la tâche, planifier, appeler des outils, lire les résultats, réviser le plan et s’arrêter une fois le travail terminé.
- **Des outils** : lecture et modification de fichiers, commandes de terminal, recherche, accès au navigateur, Git et intégrations MCP ou plugins.
- **La gestion du contexte** : réduction de l’historique de conversation, mémoire, recherche dans le code et sous-agents.
- **Les autorisations et la sécurité** : demandes de confirmation, environnements isolés, périmètres en lecture seule ou en écriture et contrôles réseau.
- **L’observabilité et l’évaluation** : journaux, traces d’exécution, suivi des coûts, benchmarks et tests de régression.

Les tableaux ci-dessous résument les principales familles de modèles et les modes d’accès vérifiés le 16 novembre 2026.
La disponibilité dépend de la version de l’application, de l’abonnement, de la région, des identifiants du fournisseur et des paramètres de l’organisation ; consultez les guides officiels liés pour connaître la liste actuelle.
La prise en charge d’un modèle n’inclut pas nécessairement l’accès à son service : certains environnements exigent votre propre clé API, un abonnement auprès du fournisseur ou un serveur de modèles local.

## Environnements avec une application autonome

Sur la page de téléchargement officielle, choisissez le programme d’installation adapté à votre système d’exploitation, puis suivez le guide de prise en main.

| Application | Principaux modèles et accès | Téléchargement officiel | Premiers pas |
| --- | --- | --- | --- |
| Claude Code dans l’application de bureau Claude | Claude Fable, Claude Haiku, Claude Opus et Claude Sonnet ([Modèles](https://code.claude.com/docs/en/model-config)). | [Télécharger](https://claude.com/download) | [Première session](https://code.claude.com/docs/en/desktop-quickstart) |
| DeepSeek Harness (DSH) | DeepSeek ; les fournisseurs configurés proposent aussi Claude, GLM, GPT et Kimi ([Fournisseurs](https://deepseek-harness.github.io/deepseek-harness/en/guide/providers)). | [Télécharger](https://deepseek.com/en/harness/) | [Espace de travail et première tâche](https://deepseek-harness.github.io/deepseek-harness/en/guide/quickstart) |
| Factory Droid | Claude, Gemini, GPT et Grok, ainsi que des modèles à poids ouverts tels que DeepSeek, GLM et Kimi ([Modèles](https://docs.factory.com/models)). | [Télécharger](https://factory.com/product/desktop) | [Première session](https://docs.factory.com/factory-app/quickstart) |
| Goose | Claude, Gemini et GPT configurés par l’utilisateur ; modèles locaux via Ollama et d’autres fournisseurs ([Fournisseurs](https://goose-docs.ai/docs/getting-started/providers/)). | [Télécharger](https://goose-docs.ai/docs/getting-started/installation/) | [Démarrage rapide](https://goose-docs.ai/docs/quickstart/) |
| OpenAI Codex dans l’application de bureau ChatGPT | OpenAI GPT-6 Astra, GPT-6 Luna, GPT-6.1 Sol et GPT-6.1 Terra ([Modèles](https://learn.chatgpt.com/docs/models?surface=app)). | [Télécharger](https://chatgpt.com/download/) | [Démarrage rapide](https://learn.chatgpt.com/docs/quickstart) |
| OpenCode | Claude, Gemini, GPT et modèles à poids ouverts via les fournisseurs configurés ou le catalogue hébergé d’OpenCode ([Fournisseurs](https://opencode.ai/docs/providers/)). | [Télécharger](https://opencode.ai/desktop) | [Se connecter et commencer](https://opencode.ai/docs/) |

- Dans l’application Claude, ouvrez l’onglet Code.
- Dans l’application ChatGPT, sélectionnez Codex dans le menu de l’application.

## Environnements cloud dans le navigateur

| Application | Principaux modèles et accès | Configuration de l’accès | Premiers pas |
| --- | --- | --- | --- |
| [Open Math OS](https://www.openmathmodel.org/) | Modèles à poids ouverts, notamment DeepSeek, GLM et Kimi, hébergés par SAIR Foundation et ses partenaires. | [Demander l’accès](https://apply.openmathmodel.org/) | [Fonctionnalités et déroulement](https://www.openmathmodel.org/) |

Open Math OS est un espace de recherche mathématique qui fournit une machine cloud par projet, des fichiers et des conversations partagés, ainsi que des agents travaillant en parallèle grâce à Ultramath.
Les outils préinstallés comprennent Python, Lean et Mathlib, SageMath et LaTeX.
Connectez-vous avec un compte SAIR et remplissez la demande relative à votre recherche ou à votre équipe ; l’accès commence après approbation.

## <a id="notion-ide"></a>EDI prenant en charge les environnements d’exécution d’agents

Un EDI (environnement de développement intégré) permet de modifier des fichiers, d’exécuter des programmes et de gérer un projet dans un même espace de travail.
Les liens ci-dessous expliquent comment installer l’éditeur et commencer à utiliser ses fonctions d’agent.
Si l’éditeur nécessite une extension d’agent, suivez le guide de l’intégration correspondante.

| EDI | Principaux modèles et accès | Téléchargement officiel | Premiers pas |
| --- | --- | --- | --- |
| Cursor | Composer et Grok ; Claude, Gemini et GPT avec les abonnements compatibles ([Modèles](https://cursor.com/docs/models-and-pricing)). | [Télécharger](https://cursor.com/download) | [Première tâche](https://cursor.com/docs/get-started/quickstart) |
| Devin Desktop (anciennement Windsurf) | Modèles SWE de Cognition, notamment SWE-2 et SWE-2 Flash, ainsi que Claude, Gemini et GPT ([Modèles](https://docs.devin.ai/desktop/models)). | [Télécharger](https://devin.ai/download) | [Premiers pas](https://docs.devin.ai/desktop/getting-started) |
| Eclipse Theia | Claude, Gemini et GPT configurés par l’utilisateur ; modèles locaux via Ollama ([Fournisseurs](https://theia-ide.org/docs/user_ai/)). | [Télécharger](https://theia-ide.org/) | [Utiliser les fonctions d’IA](https://theia-ide.org/docs/user_ai/) |
| Google Antigravity | Claude Opus, Claude Sonnet et Gemini ; les choix dépendent de l’abonnement ([Modèles](https://antigravity.google/docs/models)). | [Télécharger](https://antigravity.google/download) | [Première session](https://antigravity.google/docs/getting-started) |
| JetBrains IDEs | Claude, Gemini et GPT via JetBrains AI ou les fournisseurs configurés ; connexion possible aux modèles locaux pris en charge ([Modèles](https://www.jetbrains.com/help/ai-assistant/supported-llms.html)). | [Télécharger](https://www.jetbrains.com/ides/) | [Utiliser les agents dans AI Chat](https://www.jetbrains.com/help/ai-assistant/ai-chat.html) |
| Kiro | Claude et GPT, ainsi que des modèles à poids ouverts tels que GLM, Kimi et MiniMax ; Auto peut choisir les modèles pour vous ([Modèles](https://kiro.dev/docs/models/available-models/)). | [Télécharger](https://kiro.dev/downloads/) | [Premier projet](https://kiro.dev/docs/getting-started/first-project/) |
| Positron | Claude, DeepSeek, Gemini et GPT via les fournisseurs configurés ; modèles locaux via LM Studio ou Ollama ([Fournisseurs](https://positron.posit.co/assistant-providers.html)). | [Télécharger](https://positron.posit.co/download.html) | [Configuration de l’IA et première utilisation](https://positron.posit.co/assistant-getting-started.html) |
| TRAE | Gemini et GPT ; les catalogues régionaux comprennent aussi DeepSeek, GLM, Grok, Kimi, MiniMax ou Seed, avec prise en charge de fournisseurs personnalisés ([Modèles](https://docs.trae.ai/ide/models?_lang=en)). | [Télécharger](https://www.trae.ai/download) | [Premiers pas](https://docs.trae.ai/ide/get-started-with-trae-desktop?_lang=en) |
| VS Code | Claude, Gemini, GPT et d’autres modèles via Copilot ou les fournisseurs configurés ; l’accès dépend aussi de l’environnement d’exécution choisi ([Modèles et environnements d’exécution](https://code.visualstudio.com/features/models)). | [Télécharger](https://code.visualstudio.com/download) | [Démarrage rapide avec les agents](https://code.visualstudio.com/docs/agents/quickstart) |
| VSCodium | Avec la configuration Cline indiquée ici : Claude, DeepSeek, Gemini et GPT, ainsi que des modèles locaux configurables ([Fournisseurs](https://docs.cline.bot/provider-config/openrouter)). | [Télécharger](https://github.com/VSCodium/vscodium/releases) | [Configurer Cline](https://docs.cline.bot/getting-started/installing-cline) · [Première tâche avec Cline](https://docs.cline.bot/usage/ide) |
| Zed | Claude, Gemini et GPT hébergés ([Modèles](https://zed.dev/docs/account/zed-hosted-models)) ; d’autres fournisseurs et des modèles locaux peuvent être configurés ([Fournisseurs](https://zed.dev/docs/ai/llm-providers)). | [Télécharger](https://zed.dev/download) | [Démarrage rapide de l’IA](https://zed.dev/docs/ai/quick-start) |

## Commencer à utiliser ACME

1. Installez une application ou un EDI en suivant son guide officiel, ou connectez-vous à un environnement cloud ; installez une extension d’agent si nécessaire.
2. Connectez-vous ou configurez un fournisseur de modèles selon les exigences de l’outil, puis sélectionnez un modèle.
3. Ouvrez le dossier de votre projet ACME dans l’application ou l’EDI, ou téléversez les fichiers du projet dans l’espace cloud.
4. Poursuivez avec les [étapes de configuration du manuel](<../Manuel d’utilisation.md#setup>) et les [exemples de consignes de configuration](<../user-instructions/Exemples de consignes.md#setup>).
