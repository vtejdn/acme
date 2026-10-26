# Manuel d’utilisation

[Exemples de consignes](<user-instructions/Exemples de consignes.md>) · [Exemple de déclaration d’utilisation de l’IA](ai-disclosure-example.md)

## ACME : Autonomous and Collaborative Mathematical Exploration

ACME est un cadre léger pour la recherche mathématique autonome et collaborative.
Il associe des règles en Markdown destinées aux [agents d’IA](#notion-agent) à des scripts auxiliaires pour soutenir des recherches dans la durée et conserver des travaux qui peuvent être examinés, réutilisés et poursuivis.
Il répond à deux objectifs principaux : permettre à des agents d’IA autonomes de mener des recherches mathématiques sous la direction de mathématiciens humains et faciliter la collaboration entre auteurs humains.

### Mathématiciens humains

Les mathématiciens humains ont la responsabilité de :

1. Définir les questions de recherche, leur périmètre autorisé et les critères d’achèvement afin de lancer des [tâches de recherche (Task)](#material-task).
2. Orienter avec les [agents](#notion-agent) le développement des [stratégies de recherche](#material-strategy).
3. Apporter des idées, préciser l’intention mathématique, fixer les priorités scientifiques, questionner les arguments, affiner les questions et réorienter les recherches.
4. Comprendre les résultats des recherches et explorer les frontières des connaissances mathématiques.
5. Assumer la responsabilité des résultats mathématiques.

### Agents fondés sur des [LLM](#notion-llm)

Dans le périmètre autorisé, les [agents](#notion-agent) autonomes ont la responsabilité de :

1. Étudier la littérature et vérifier les résultats nécessaires à la recherche.
2. Développer et évaluer des [stratégies de recherche](#material-strategy), repérer les lacunes et prendre de façon autonome les décisions méthodologiques courantes dans le cadre de la mission.
3. Explorer des questions ouvertes et préciser la portée et les limites des résultats en cours d’élaboration.
4. Rechercher des démonstrations et des contre-exemples pour des questions précises et effectuer des calculs reproductibles pour obtenir des observations, des éléments de preuve et des pistes de compréhension.
5. Conserver les hypothèses, arguments, éléments de preuve, dépendances, tentatives infructueuses utiles, questions non résolues et étapes substantielles de la recherche dans les documents appropriés, notamment les [Claims](#material-claim) et les [Ledgers](#material-ledger).
6. Organiser des [vérifications](#material-review) indépendantes lorsque cela est requis et en consigner le périmètre, les constats et les limites.
7. Préparer et examiner les manuscrits conformément aux usages généraux de la rédaction mathématique et aux préférences de l’auteur responsable.

### Collaboration

Les mathématiciens peuvent collaborer au moyen d’un [dépôt Git](git-repository.md#notion-git-repository) commun, partager les documents de recherche et réutiliser les résultats des autres.
Le dépôt peut être hébergé sur une plateforme telle que [GitHub](git-repository.md#notion-github), permettant aux collaborateurs de travailler sur leurs propres appareils et de synchroniser les modifications.
Voir le [schéma de collaboration au moyen d’un dépôt Git](git-repo.png).

Les collaborateurs d’un même dépôt peuvent établir un [Task](#material-task) conjoint pour un objectif mathématique commun, en précisant la question commune, les hypothèses et les critères d’achèvement ;
chaque participant précise son périmètre de participation dans son propre Task et organise des démarches de recherche concrètes au moyen de [stratégies de recherche (Strategy)](#material-strategy).
Il est recommandé de choisir des stratégies de recherche différentes en concertation avec les collaborateurs, afin de limiter les efforts mathématiques redondants et d’utiliser plus efficacement les ressources de calcul pour l’IA.
Pour une vérification indépendante, une réplication ou des contrôles croisés, il est également possible d’adopter délibérément la même démarche de recherche.

Différents mathématiciens ou équipes peuvent aussi collaborer entre dépôts en recevant des documents sélectionnés par [Intake](#notion-intake) ; voir le [schéma de collaboration entre dépôts](collaboration.jpg).

### Déroulement du travail

La recherche commence par un [Task](#material-task) défini par un humain et précisant les critères d’achèvement.
Les [agents](#notion-agent) consultent et réutilisent d’abord les documents de recherche et la littérature disponibles localement, puis recherchent au besoin des sources supplémentaires sur le Web.
Ils vérifient l’applicabilité des résultats, développent des [stratégies](#material-strategy) et alternent tentatives de démonstration, calculs et recherches de contre-exemples.
Chaque tentative éclaire la suivante : les constats utiles, les échecs et les questions non résolues sont conservés dans les documents de recherche appropriés, notamment les [Claims](#material-claim) et les [Ledgers](#material-ledger).
Les stratégies évoluent dans le cadre de l’objectif autorisé.
Les résultats proposés font l’objet d’une [vérification](#material-review) mathématique et l’achèvement du Task est évalué au regard des critères d’origine.

Voir le [schéma de déroulement du travail](workflow.jpg).

## <a id="setup"></a>Configuration

Pour un nouveau projet de recherche, suivez les étapes I à III ci-dessous.
Si vous rejoignez une collaboration existante, configurez votre espace de travail, puis suivez les étapes prévues pour rejoindre la collaboration.

### Étape I. Choisir des [LLM](#notion-llm) performants

Comparez les performances des LLM sur des problèmes mathématiques de niveau recherche.
Prenez comme points de repère [FrontierMath Tier 4](https://epoch.ai/frontiermath/tiers-1-4?tier=Tier+4+%28v2%29&view=graph&tab=leaderboard), [MathArena](https://matharena.ai/models), [Riemann-bench](https://surgehq.ai/benchmarks/riemann-bench) et d’autres évaluations pertinentes.
Choisissez des modèles pour la recherche mathématique et les tâches administratives en tenant compte de leur caractère open source, de leur accessibilité et de leur coût.

### Étape II. Configurer votre espace de travail

Pour une recherche individuelle sur un seul appareil, utilisez un [environnement d’exécution d’agents](agent-harness.md) adapté, donnant accès à un [LLM](#notion-llm) performant.

1. Installez un environnement d’exécution d’agents, sous forme d’application autonome ou au sein d’un [EDI](agent-harness.md#notion-ide), puis connectez-vous si cela est nécessaire ou souhaité.
2. Choisissez un dossier sur votre appareil pour y conserver le cadre et les futurs documents de recherche.
3. Choisissez le modèle et le fournisseur dans les paramètres ou le sélecteur de modèles.

Sans [Git](git-repository.md#notion-git), le mode par défaut est la recherche personnelle sur votre appareil local.
Pour synchroniser votre travail entre appareils ou collaborer au moyen d’un [dépôt Git](git-repository.md#notion-git-repository) partagé, vous pouvez choisir une plateforme d’hébergement telle que [GitHub](git-repository.md#notion-github).
Téléverser les travaux de recherche et rendre un dépôt public sont deux choix distincts.

4. (Facultatif) Installez Git sur votre appareil ou demandez à un [agent](#notion-agent) de l’installer dans l’environnement d’exécution choisi.
5. (Facultatif) Créez un compte sur une plateforme d’hébergement de dépôts ou connectez-vous, puis reliez votre espace de travail à un dépôt existant ou créez-en un.

- Voir les [consignes de configuration](<user-instructions/Exemples de consignes.md#setup>).

### Étape III. Installer et initialiser le cadre

Si vous rejoignez un dépôt de recherche existant qui contient déjà ACME, suivez plutôt les étapes de la section suivante.

1. Demandez à un [agent](#notion-agent) de télécharger le [cadre ACME](https://github.com/vtejdn/acme) dans le dossier de votre projet, ou de [cloner](#notion-clone) son dépôt si vous utilisez [Git](git-repository.md#notion-git).
2. Choisissez une clé d’auteur unique, par exemple `Alice` ou `Ali`, et choisissez indépendamment le nom à faire figurer dans l’attribution de `LICENSE`.
   Demandez à un agent de vous enregistrer comme auteur et d’ajouter cette attribution.
   Dans un espace de travail Git, demandez à l’agent d’associer cette copie de travail à votre clé d’auteur afin que les nouveaux enregistrements portent la bonne attribution.
3. (Si vous utilisez Git) Configurez le nom et l’adresse électronique associés à vos [commits](#notion-commit), ou demandez à un agent de le faire.
4. (Si vous utilisez Git) Choisissez ou confirmez un nom court pour votre [dépôt](git-repository.md#notion-git-repository) de recherche et demandez à un agent de vérifier qu’il est correctement enregistré dans le cadre.
5. (Facultatif) Lorsque cela est approprié, nous vous recommandons vivement de partager vos travaux de recherche dans un dépôt public.

- Voir les [consignes de configuration](<user-instructions/Exemples de consignes.md#setup>).

### Rejoindre un [dépôt Git](git-repository.md#notion-git-repository) existant comme collaborateur

1. Connectez-vous à la plateforme d’hébergement du dépôt et acceptez l’invitation de votre coauteur.
2. Demandez à un [agent](#notion-agent) de vous aider à configurer l’accès au dépôt partagé.
3. Donnez l’adresse du dépôt à un agent et demandez-lui de le [cloner](#notion-clone) dans un nouveau dossier local.
   Ouvrez ce dossier dans votre environnement d’exécution d’agents.
4. Si vous n’êtes pas encore enregistré dans le dépôt de recherche, choisissez une clé d’auteur différente de celles de vos collaborateurs et choisissez indépendamment le nom à faire figurer dans l’attribution de `LICENSE`,
   puis demandez à un agent de vous enregistrer et d’ajouter cette attribution.
   Demandez à l’agent d’associer cette copie de travail à votre clé d’auteur dans ACME.
5. Configurez le nom et l’adresse électronique utilisés pour vos [commits](#notion-commit) [Git](git-repository.md#notion-git), ou demandez à un agent de le faire.

- Voir les [consignes de configuration](<user-instructions/Exemples de consignes.md#setup>).

## Premiers pas

### Commencer un Task

1. (Facultatif) Fournissez la littérature pertinente ou demandez à un [agent](#notion-agent) de la rechercher.
   Demandez à l’agent de conserver les fichiers sources dans le [répertoire local de littérature](../mathematics/literature/pdf) et de vérifier les parties indiquées des articles pertinents au niveau de profondeur demandé.
2. Définissez un [Task](#material-task) en discutant avec les agents, en précisant les questions, les contraintes et les critères d’achèvement.
   Vous pouvez choisir une [lettre de ligne de recherche](#notion-research-line-letter) pour organiser le Task et les documents associés.
3. Pour un travail autonome prolongé, précisez ou adoptez des limites d’exécution et des conditions d’arrêt.
4. Autorisez les actions nécessaires des outils lorsque cela vous est demandé et répondez aux questions posées par les agents.
5. Réfléchissez aux documents mathématiques produits par les agents et comprenez-les ; aucun agent ne peut le faire à votre place.
   Discutez des mathématiques avec les agents pour approfondir et accélérer votre compréhension.
   Demandez des références pertinentes et questionnez de manière socratique les sources des arguments et des idées, en particulier lorsqu’un argument s’appuie sur les connaissances du modèle sans source explicite.
6. (Facultatif, si vous utilisez [Git](git-repository.md#notion-git)) Enregistrez les modifications que vous souhaitez conserver dans des [commits](#notion-commit) ; au besoin, annulez les modifications locales ou utilisez un revert pour annuler des commits.
   Lorsque vous collaborez avec d’autres mathématiciens, demandez aux agents de gérer les [pushs](#notion-push), les [pulls](#notion-pull), les [fusions](#notion-merge) et de vous aider à résoudre les conflits.

- Voir les [exemples de consignes de recherche](<user-instructions/Exemples de consignes.md#research-instructions>).

### Points d’attention

- Les [agents](#notion-agent) tenteront de télécharger la littérature publiquement accessible dans le [répertoire local de littérature](../mathematics/literature/pdf).
  Ce répertoire est ignoré par [Git](git-repository.md#notion-git) par défaut.
  Si vous y placez vos propres documents privés, assurez-vous qu’il est ignoré par Git et qu’il n’est pas téléversé vers un dépôt public.
- Si des collaborateurs devaient utiliser la même clé d’auteur, convenez de clés distinctes, par exemple `Wang1` et `Wang2`.
- Utilisez des [lettres de ligne de recherche](#notion-research-line-letter) différentes pour les [Tasks](#material-task) menés en parallèle par des agents principaux de recherche distincts.
  Choisissez ces lettres lors de la configuration des Tasks afin de séparer la numérotation des documents et de réduire les conflits d’écriture.
  Demandez aux agents de coordonner les modifications des fichiers partagés, notamment les index, la bibliographie et les enregistrements d’identité du dépôt.
  Il n’est pas recommandé de créer des worktrees de recherche parallèles supplémentaires ; le cadre ne définit aucun processus pour les gérer.
- ACME guide les agents au moyen de règles écrites et d’outils auxiliaires.
  Si un agent s’écarte de vos consignes ou des règles du cadre, demandez-lui d’expliquer l’écart et de corriger le travail concerné.
- Les règles du cadre peuvent comporter des ambiguïtés, des incohérences ou des lacunes.
  Vous pouvez demander à un agent de les réviser si vous le jugez approprié.
  Vous pouvez également le signaler à l’[auteur](https://github.com/vtejdn) du cadre ACME.

### Habitudes utiles

- Interrogez un [agent](#notion-agent) dès que vous avez des questions sur le cadre.
- Si vous conservez la littérature dans un répertoire local synchronisé par un service cloud, demandez à un agent d’y relier le [répertoire local de littérature](../mathematics/literature/pdf) au moyen d’une jonction de répertoires (directory junction).
  Accordez à l’agent les autorisations nécessaires pour lire et gérer les fichiers de ce répertoire.
- Lorsque les agents automatisent des tâches associées nécessitant des identifiants d’accès, conservez les secrets de manière appropriée et excluez-les de [Git](git-repository.md#notion-git).

### Rédiger un manuscrit

En cours de rédaction.

### Formalisation en Lean

En cours de rédaction.

## Informations utiles

### Version du cadre

La version actuelle du cadre est 0.2.0.

Lorsque les vérifications automatiques sont activées et que l’accès au réseau est autorisé,
l’[agent](#notion-agent) vérifie au début du travail, au plus une fois par jour UTC, si une nouvelle version du [cadre ACME officiel](https://github.com/vtejdn/acme) est disponible.
Si une nouvelle version est disponible, il indique la version installée et la version disponible et vous demande s’il faut organiser une mise à niveau ; le travail en cours peut continuer pendant votre décision.
Un rappel n’installe ni ne met à niveau aucun fichier, et vous pouvez le différer.
Vous pouvez demander de désactiver ou de réactiver les vérifications automatiques pour ce dépôt, de vérifier à nouveau immédiatement ou d’effectuer explicitement une mise à niveau.

### <a id="common-instructions"></a>Exemples de consignes

Les [exemples de consignes](<user-instructions/Exemples de consignes.md>) illustrent des demandes courantes et expliquent les résultats à attendre.

### Répertoires et fichiers à la racine

Les tableaux ci-dessous décrivent les principaux fichiers et répertoires à la racine du dépôt.
Certains répertoires ne sont créés qu’en cas de besoin.

| Chemin | Fonction |
| --- | --- |
| `.tmp/` | Contient les entrées temporaires et les fichiers intermédiaires créés par les [agents](#notion-agent) et supprimés après utilisation. |
| `execution/` | Consigne l’état d’exécution actuel, les limites et les conditions d’arrêt des [Tasks](#material-task) de recherche individuels. |
| [`framework/`](../framework/readme.md) | Contient les règles du cadre, les modèles de documents, les spécifications de format et les indications de version. |
| `intake/` | Consigne les documents reçus d’autres [dépôts](git-repository.md#notion-git-repository), leurs sources et le périmètre de chaque acquisition. |
| [`mathematics/`](../mathematics/readme.md) | Contient les documents de recherche, les enregistrements bibliographiques, les calculs, les manuscrits et les présentations. |
| `profiles/` | Contient les politiques personnelles de recherche, les préférences d’exécution et les choix de rédaction mathématique. |
| [`repository/`](../repository/readme.md) | Conserve les paramètres du dépôt, les enregistrements des auteurs et les correspondances avec les dépôts et auteurs externes. |
| [`scripts/`](../scripts/readme.md) | Fournit des outils facultatifs en ligne de commande pour la configuration, la gestion des documents, la navigation et les vérifications. |
| [`user-manual/`](./) | Contient les guides d’utilisation, les explications de configuration et les exemples de consignes. |
| `.gitattributes` | Configure le traitement des fichiers texte et binaires par [Git](git-repository.md#notion-git), notamment les fins de ligne. |
| `.gitignore` | Indique les fichiers et répertoires non suivis que Git doit ignorer. |
| `AGENTS.md` | Fournit les consignes d’entrée qui orientent les agents vers les règles et documents applicables du cadre. |
| `LICENSE` | Contient les conditions de licence et les mentions du dépôt. |
| `readme.md` | Présente le dépôt et renvoie vers le manuel d’utilisation, les règles du cadre et les documents de recherche. |

Selon vos outils et votre configuration, les répertoires suivants peuvent également être présents.

| Chemin | Fonction |
| --- | --- |
| `.agents/` | Contient les skills d’agents propres au dépôt. |
| `.claude/` | Contient les paramètres locaux de Claude Code pour cet espace de travail. |
| `.codex/` | Contient la configuration locale de Codex pour cet espace de travail. |
| `.git/` | Contient l’historique Git, les références, la configuration et les autres métadonnées de gestion de versions. |
| `.venv/` | Contient l’environnement virtuel Python local et ses dépendances installées. |
| `.vscode/` | Contient la configuration de l’espace de travail VS Code et les recommandations d’extensions. |

### Catégories de documents de recherche

| Abréviation | Document | Emplacement | Fonction |
| --- | --- | --- | --- |
| T | [Tâche de recherche (Task)](#material-task) | [`mathematics/tasks/`](../mathematics/tasks/index.md) | Définit une question de recherche, son périmètre autorisé et ses critères d’achèvement, et consigne les décisions concernant son cycle de vie. |
| S | [Stratégie de recherche (Strategy)](#material-strategy) | [`mathematics/strategies/`](../mathematics/strategies/index.md) | Développe et évalue une voie de recherche, organise les priorités et identifie les obstacles ainsi que les prochaines étapes. |
| C | [Énoncé mathématique (Claim)](#material-claim) | [`mathematics/claims/`](../mathematics/claims/index.md) | Formule des énoncés mathématiques précis, conserve leurs arguments et dépendances, et consigne leur évaluation mathématique ainsi que les vérifications les concernant. |
| R | [Compte rendu de vérification (Review)](#material-review) | [`mathematics/audits/reviews/`](../mathematics/audits/reviews/readme.md) | Consigne les vérifications mathématiques d’arguments précis du projet, notamment les éléments examinés, les constats, l’organisation de la vérification et ses limites. |
| D | Brouillon (Draft) | [`mathematics/drafts/`](../mathematics/drafts/readme.md) | Fournit un espace de travail pour développer des arguments mathématiques, des calculs et des solutions alternatives encore à l’étude. |
| L | [Carnet d’exploration (Ledger)](#material-ledger) | [`mathematics/ledger/`](../mathematics/ledger/readme.md) | Conserve les explorations, comparaisons, synthèses et tentatives infructueuses utiles, ainsi que les raisons et les résultats des modifications mathématiques substantielles. |
| J | Calcul (Computation) | [`mathematics/computations/programs/`](../mathematics/computations/readme.md) | Organise les programmes et les données d’entrée nécessaires aux calculs reproductibles et consigne l’état des exécutions, leurs résultats et leurs limites. |
| U | Unité de vérification de la littérature (Literature audit unit) | [`mathematics/audits/literature/`](../mathematics/audits/literature/readme.md) | Rend la littérature examinée réutilisable en consignant l’édition et les passages de la source, le contenu mathématique, l’applicabilité et les limites de l’examen. |
| — | Manuscrit (Manuscript) | [`mathematics/manuscripts/`](../mathematics/manuscripts/index.md) | Permet d’élaborer des articles et des documents mathématiques associés, avec leur exposition, leurs citations, leurs choix de rédaction et leurs relevés de compilation. |
| — | Présentation (Presentation) | [`mathematics/presentations/`](../mathematics/presentations/readme.md) | Permet de préparer des exposés et des diapositives pour un public donné, avec les fichiers sources, les choix de rédaction, les informations de compilation et les comptes rendus de vérification. |

- Chaque calcul dispose d’un répertoire J numéroté contenant ses programmes, les données d’entrée nécessaires et un fichier `readme.md`.
  Les sorties générées sont conservées séparément sous le chemin local `mathematics/computations/outputs/<J>/`, ignoré par [Git](git-repository.md#notion-git).
- Les unités de vérification de la littérature sont regroupées par clé de citation sous `mathematics/audits/literature/`.
- L’[index des définitions](../mathematics/definitions/index.md) organise les définitions, la terminologie et les symboles par concept, avec des liens vers leurs formulations complètes dans les documents C, L ou U qui en sont responsables.
- La [bibliographie](../mathematics/literature/references.bib) de référence consigne l’identité des publications et leurs clés de citation.
  L’acquisition des sources, les versions des fichiers et leur disponibilité sont consignées séparément dans le [registre de littérature](../mathematics/literature/registry.md).

### Notions de base

| Terme | Signification |
| --- | --- |
| <a id="notion-llm"></a>LLM (grand modèle de langage) | Modèle d’IA entraîné sur de grandes quantités de texte pour traiter et produire du langage, notamment des explications mathématiques et du code informatique. |
| <a id="notion-agent"></a>Agent | Système d’IA fondé sur un [LLM](#notion-llm), capable de planifier et d’exécuter des tâches, d’utiliser des outils et d’adapter ses actions aux résultats. Il fonctionne au moyen d’un [environnement d’exécution d’agents](agent-harness.md), dans le périmètre et les limites autorisés par l’utilisateur humain. Il n’a pas encore évolué en [Agent](https://fr.wikipedia.org/wiki/Matrix_%28s%C3%A9rie_de_films%29#Les_Agents). |
| <a id="notion-context"></a>Contexte (Context) | Informations dont dispose un LLM lors d’un appel au modèle, notamment les consignes, l’historique de la conversation, les documents fournis et les résultats des outils. Le contexte actuel peut ne contenir qu’une sélection ou un résumé de l’historique complet de la [session](#notion-session). |
| <a id="notion-context-length"></a>Longueur de contexte (Context length) | Longueur totale maximale des entrées et de la sortie qu’un LLM peut traiter en une fois, généralement mesurée en tokens, de petites unités de texte. Elle comprend les consignes, l’historique de la conversation, les documents fournis et la réponse générée. |
| <a id="notion-session"></a>Session | Interaction continue avec un [agent](#notion-agent), gérée par un [environnement d’exécution d’agents](agent-harness.md). Elle peut comporter plusieurs tours de conversation, chacun commençant généralement par un message de l’utilisateur et comprenant les réponses de l’agent ainsi que les opérations des outils. L’environnement conserve l’historique de la conversation et prépare le [contexte](#notion-context) de chaque appel au modèle ; pour respecter la [longueur de contexte](#notion-context-length) du modèle, il peut sélectionner ou résumer les parties antérieures de l’historique. |
| Identifiant de document | Référence structurée identifiant un document et, le cas échéant, sa version. Par exemple, `Alice_C_F0007_v1.md` identifie un [Claim](#material-claim) par auteur, type, ligne de recherche, numéro de série et version. |
| <a id="notion-research-line-letter"></a>Lettre de ligne de recherche | Lettre, telle que `F` dans `Alice_C_F0007_v1.md`, servant à organiser les documents de recherche numérotés. Les documents issus d’un Task héritent de sa lettre, mais reçoivent leurs propres numéros de série. Par défaut, la lettre `A` est utilisée lorsqu’aucune ligne n’est indiquée. |
| Clé d’auteur | Clé stable enregistrée pour un auteur humain, par exemple `Alice`, utilisée dans les identifiants de documents et les enregistrements d’auteur. |
| Famille de documents | Ensemble des versions conservées d’un même document, par exemple `Alice_C_F0007_v1.md` et `Alice_C_F0007_v2.md`. |
| Version de document | Révision particulière conservée d’un document, par exemple la version `v1` ou `v2` d’un Claim. |
| <a id="notion-main-research-agent"></a>Agent principal de recherche | Agent qui dirige le travail sur un [Task](#material-task), coordonne les éventuels sous-agents et veille à la cohérence des enregistrements de recherche. |
| Cycle de travail d’un Task | Période de travail sur un Task, qui se termine par un relevé des progrès, des questions non résolues et du point de reprise. |
| <a id="notion-git-branch"></a>Branche Git (Branch) | Ligne de développement nommée dans un [dépôt Git](git-repository.md#notion-git-repository), permettant de développer des modifications séparément des autres lignes de travail. |
| <a id="notion-clone"></a>Clonage (Clone) | Copie d’un dépôt Git existant dans un nouveau dossier local, avec ses fichiers et son historique de versions. |
| <a id="notion-commit"></a>Commit | Version enregistrée dans l’historique [Git](git-repository.md#notion-git) local, contenant une sélection de modifications et un message qui les décrit. |
| <a id="notion-push"></a>Push | Envoi des commits locaux vers un dépôt Git distant afin d’y rendre le travail enregistré disponible. |
| <a id="notion-pull"></a>Pull | Récupération des modifications d’un dépôt Git distant et intégration de celles-ci au travail local. |
| <a id="notion-merge"></a>Fusion (Merge) | Intégration des modifications d’une autre [branche](#notion-git-branch) à la branche Git actuelle, avec résolution des modifications conflictuelles si nécessaire. |
| <a id="notion-intake"></a>Importation (Intake) | Introduction dans votre dépôt de documents de recherche sélectionnés dans un autre dépôt ACME public, en conservant l’attribution, l’origine et les limites de vérification. |
| Clé de citation | Identifiant court d’une référence dans la bibliographie, utilisé pour la citer de manière cohérente dans les enregistrements de recherche et les manuscrits. |

### <a id="material-task"></a>Tâche de recherche (Task)

Un Task organise la recherche autour d’un objectif mathématique précis, de son périmètre autorisé et de critères d’achèvement convenus.

| État du Task | Signification pour le lecteur |
| --- | --- |
| `proposed` | Une question de recherche a été proposée, mais n’est pas encore devenue un objectif de recherche actif. |
| `active` | La recherche est autorisée et se poursuit. |
| `paused` | La recherche est volontairement suspendue, avec une intention de reprise et une base explicitement indiquée pour celle-ci. |
| `blocked` | Une donnée d’entrée précise manque ou un prérequis n’est pas satisfait, empêchant la prochaine étape nécessaire. L’enregistrement explique ce qui est requis pour reprendre la progression. |
| `completed` | Les critères d’achèvement convenus sont satisfaits, avec les éléments mathématiques justificatifs et la vérification requise. |
| `retired` | La recherche a été abandonnée. Ses raisons, les constats utiles et les parties inachevées restent consignés. |

- Un Task peut rester actif même si aucun [agent](#notion-agent) n’y travaille à cet instant.
- Un Task rassemble les documents de recherche qui soutiennent votre investigation.
  Les manuscrits associés, rapports d’avancement et autres documents que vous demandez peuvent être réunis dans un projet tel que `mathematics/manuscripts/Alice_T_A0007/`.
- Vous pouvez demander la réactivation d’un Task achevé afin de poursuivre le travail sur l’objectif de recherche concerné.
  Expliquez ce que vous souhaitez étudier ensuite et les éventuels changements de périmètre ou de limites.
  Un objectif de recherche substantiellement différent doit faire l’objet d’un nouveau Task.

### <a id="material-strategy"></a>Stratégie de recherche (Strategy)

Une Strategy décrit une voie concrète vers un objectif de recherche, notamment son mécanisme, les obstacles restants et les prochaines étapes utiles.

| État de la Strategy | Signification pour le lecteur |
| --- | --- |
| `proposed` | Une approche possible a été identifiée, mais n’a pas encore été retenue pour la recherche en cours. |
| `active` | Cette voie est actuellement retenue pour faire avancer la recherche vers l’objectif du Task. |
| `paused` | Cette voie est temporairement mise de côté pour des raisons de priorité, d’ordre des travaux ou de ressources disponibles. Cela n’implique aucun échec mathématique. |
| `blocked` | Un prérequis précis non satisfait empêche la prochaine étape prévue. L’enregistrement identifie l’obstacle et les conditions permettant de poursuivre cette voie. |
| `completed` | Cette voie a fourni le résultat ou la contribution annoncés, avec les éléments justificatifs requis. D’autres travaux peuvent rester nécessaires pour achever le Task. |
| `refuted` | Des éléments mathématiques vérifiés excluent le mécanisme consigné ou une assertion auxiliaire dont il a besoin, sous les hypothèses indiquées. |
| `superseded` | Cette voie a été remplacée par des stratégies qui lui succèdent et sont explicitement identifiées, ou intégrée à une autre voie. Son historique et ses constats utiles restent accessibles. |

- Un [Task](#material-task) peut comporter plusieurs stratégies, comme alternatives ou comme composantes d’une approche combinée.
  Achever, suspendre ou écarter une stratégie ne détermine pas à lui seul l’état de l’ensemble du Task.
- Vous pouvez proposer des approches, demander à l’[agent](#notion-agent) de comparer des possibilités ou préciser des priorités.
  Indiquez explicitement si une priorité ou un ordre doit rester fixe ; sinon, l’agent peut adapter son choix de voies dans le périmètre convenu.
- Dans le périmètre autorisé, les agents autonomes peuvent ajouter ou réviser des stratégies, en modifier les priorités, les scinder, les fusionner, les suspendre ou les reprendre en fonction des constats et des ressources.
- Une voie infructueuse peut néanmoins être instructive.
  Elle peut révéler un obstacle, écarter une approche ou indiquer où une hypothèse supplémentaire serait nécessaire.

### <a id="material-claim"></a>Énoncé mathématique (Claim)

Un Claim consigne un énoncé mathématique important et précis ainsi que ce que l’on sait actuellement de sa validité.

| État mathématique | Signification pour le lecteur |
| --- | --- |
| `open` | L’énoncé exact reste non résolu. Des résultats partiels, des réductions ou un argument proposé peuvent exister, mais les conditions pour `proved` ou `refuted` ne sont pas encore remplies. |
| `proved` | Une démonstration complète établit l’énoncé exact sous les hypothèses indiquées. Tous les résultats d’appui nécessaires sont établis et applicables, et une [vérification](#material-review) mathématique consignée n’a relevé aucune lacune restante. |
| `refuted` | Un contre-exemple ou un argument vérifié réfute l’énoncé exact dans le périmètre indiqué. Tous les résultats d’appui nécessaires sont établis et applicables, et une vérification mathématique consignée n’a relevé aucune lacune restante. |

### <a id="material-review"></a>Compte rendu de vérification (Review)

Un Review consigne l’examen d’un énoncé ou d’un argument mathématique par un [agent](#notion-agent), notamment les éléments et le périmètre exacts de l’examen, les constats et les limites non résolues.

| Relation du vérificateur au travail | Signification pour le lecteur |
| --- | --- |
| `self-reviewed` | La démonstration a été vérifiée par un agent qui a participé à son élaboration ou connaît la discussion mathématique dont elle est issue. |
| `independently reviewed` | Un autre agent a vérifié la démonstration sans participer à son élaboration ni recevoir la discussion correspondante comme [contexte](#notion-context) propre. |
| `unknown` | La relation d’une vérification ancienne ou provenant d’une source n’est pas réellement établie ; cela n’implique ni une erreur ni un examen indépendant. |

- Ces étiquettes décrivent la relation des agents vérificateurs à la démonstration, et non la justesse de celle-ci.
  L’absence de déclaration de cette relation diffère de `unknown` ; l’absence de vérification sélectionnée signifie que le Claim ne retient aucun élément de vérification.
- La vérification par un autre agent reste une auto-vérification si celui-ci hérite de discussions ayant servi à élaborer la démonstration, de résumés mathématiques, d’explications de l’auteur ou de conclusions de vérifications antérieures.
  Changer seulement de [session](#notion-session) ou de modèle ne suffit pas à établir l’indépendance.
- L’[agent principal de recherche](#notion-main-research-agent) organise des vérifications indépendantes aux points clés de la démonstration et, après l’achèvement du [Task](#material-task), sur toute la chaîne logique.
  Vous pouvez également demander la vérification d’un résultat ou d’une étape de démonstration en particulier.

### <a id="material-ledger"></a>Carnet d’exploration (Ledger)

Un Ledger conserve les explorations mathématiques utiles, notamment les comparaisons, les approches infructueuses et les raisons des changements d’orientation.
Une entrée peut expliquer ce qui a été étudié, sous quelles hypothèses, ce qui a été tenté, ce que le raisonnement ou les éléments de preuve ont montré et ce qui reste non résolu.

Un Ledger peut conserver des arguments partiels et des idées utiles même lorsqu’une recherche n’a pas encore produit de [Claim](#material-claim) autonome.
Par exemple, des tentatives infructueuses ou non concluantes peuvent révéler des obstacles, distinguer des approches ou aider à éviter de refaire le même travail.

- Vous pouvez demander à un [agent](#notion-agent) de comparer des [stratégies](#material-strategy), d’expliquer une tentative infructueuse, de synthétiser les constats de plusieurs sources ou de conserver un raisonnement utile pour des travaux ultérieurs.
- Vous pouvez également demander à un agent de consigner tout ce que vous jugez mathématiquement substantiel et digne d’être conservé.
