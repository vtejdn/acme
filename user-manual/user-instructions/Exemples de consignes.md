# Exemples de consignes

[Manuel d’utilisation](<../Manuel d’utilisation.md>)

Décrivez votre objectif en langage naturel.
Les exemples ci-dessous sont répartis entre les consignes de [configuration](#setup), de [recherche](#research-instructions) et d’[administration](#administration-instructions).
Adaptez les formulations à votre question, à vos fichiers et au périmètre réel de votre travail.

## <a id="setup"></a>Consignes de configuration

Utilisez ces exemples pour préparer votre espace de travail, enregistrer votre identité d’auteur et configurer les ressources locales.
Consultez la section [Configuration](<../Manuel d’utilisation.md#setup>) du manuel pour connaître l’ordre des étapes d’installation et d’enregistrement.

| Exemple de consigne | Actions attendues de l’agent |
| --- | --- |
| Téléchargez [ACME](https://github.com/vtejdn/acme) dans `D:\acme`. | Vérifier que la destination convient à l’installation, télécharger les fichiers du cadre ACME, préserver le contenu existant et indiquer la version ainsi que les éventuelles étapes de configuration restantes. |
| Installez [Git](../git-repository.md#notion-git). | Vérifier si Git est déjà installé, l’installer si nécessaire et indiquer la version disponible ainsi que les éventuelles étapes de configuration restantes. |
| Enregistrez Ali comme ma clé d’auteur ; utilisez Alice comme nom complet. | Après vérification de la clé et des enregistrements existants, utiliser les valeurs fournies : `Ali` comme clé d’auteur et `Alice` comme nom pour l’attribution dans `LICENSE`. Vous enregistrer, ajouter l’attribution en préservant les identités et mentions existantes, et associer cette copie de travail à `Ali` si elle utilise Git. |
| Expliquez-moi comment me connecter à [GitHub](../git-repository.md#notion-github). | Expliquer comment se connecter, s’authentifier et relier l’espace de travail à un dépôt distant, en identifiant les étapes que vous devez effectuer vous-même. |
| Je me suis connecté à GitHub. Testez la connexion. | Vérifier le compte authentifié et tester en lecture seule la connectivité à GitHub et au dépôt cible. Indiquer le résultat ou l’erreur précise. |
| [Clonez](<../Manuel d’utilisation.md#notion-clone>) [ACME](https://github.com/vtejdn/acme) dans `D:\acme`. | Vérifier que Git, les autorisations d’accès et la destination sont prêts, cloner le dépôt ACME avec son historique de versions et indiquer la branche, la version et les étapes d’initialisation restantes. |
| Utilisez `nom du dépôt` comme nom du dépôt. | Vérifier le nom choisi et vous demander d’en choisir un autre s’il est invalide, plutôt que de le modifier automatiquement. Enregistrer le nom accepté dans le cadre et mettre à jour l’affichage actuel du nom du dépôt ainsi que les références concernées, en préservant les clés d’auteur, les identités des documents et les informations historiques de provenance. |
| Configurez Git et reliez-le à mon dépôt <https://github.com/alice/acme>. | Initialiser Git uniquement si nécessaire, compléter les éventuels enregistrements manquants du nom du dépôt ou de l’auteur selon vos choix, puis associer la copie de travail à votre clé d’auteur. Vérifier ou configurer l’identité des commits pour qu’elle corresponde à votre enregistrement, relier le dépôt distant indiqué et tester l’accès par le compte ou le canal d’authentification pertinent. Préserver les commits existants, les paramètres sans rapport avec la demande et les limites des Tasks, puis indiquer la destination configurée et les étapes de configuration restantes. |
| Clonez le dépôt de mon collaborateur <https://github.com/alice/acme> et enregistrez-moi sous le nom Bob. | Cloner le dépôt partagé, vous enregistrer comme Bob et associer la nouvelle copie de travail Git à Bob. Préserver les auteurs et documents de recherche existants et indiquer les paramètres d’identité utilisés pour les commits Git. |

## <a id="research-instructions"></a>Consignes de recherche

Utilisez ces exemples pour travailler sur la littérature et explorer des questions mathématiques.

### Rechercher, enregistrer ou vérifier la littérature

| Exemple de consigne | Actions attendues de l’agent |
| --- | --- |
| Examinez la source locale abc26, enregistrez-la et vérifiez-la. | Identifier l’œuvre, l’édition et l’original local correspondant à abc26 et compléter son enregistrement bibliographique ainsi que celui des fichiers. Si l’original contient une table des matières, en préparer une copie interrogeable. Vérifier le contenu mathématique et consigner le périmètre examiné, les conclusions et les questions non résolues. |
| Vérifiez le théorème 1.7 dans abc26. | Repérer le théorème 1.7 dans l’original, vérifier son énoncé complet, ses hypothèses, sa démonstration et l’applicabilité des résultats nécessaires dont il dépend, puis consigner les constats, les parties non vérifiées et les lacunes précises. |
| Recherchez *On the construction of S* et essayez de l’enregistrer et de le vérifier. | Identifier l’œuvre et l’édition, consulter les enregistrements existants et tenter d’obtenir l’original. Consigner les informations bibliographiques et ce qui a effectivement été obtenu. Si l’original contient une table des matières, en préparer une copie interrogeable. Vérifier le contenu disponible et préciser les éléments indisponibles. |
| Comment cette définition est-elle utilisée dans la littérature pertinente ? | Consulter les enregistrements de définitions existants et les sources originales pertinentes, comparer les objets, hypothèses, notations et usages, fournir des références précises et distinguer les définitions des sources des reformulations ou généralisations locales. |

### <a id="start-or-continue-research"></a>Commencer ou poursuivre un [Task](<../Manuel d’utilisation.md#material-task>)

| Exemple de consigne | Actions attendues de l’agent |
| --- | --- |
| Créez un Task dans la ligne W pour la conjecture 1.3 d’abc26. | Vérifier l’énoncé original, les hypothèses et la portée de la conjecture 1.3 et rechercher d’abord un Task existant sur la même question. Si un nouveau Task est nécessaire, utiliser la [ligne W](<../Manuel d’utilisation.md#notion-research-line-letter>) et préciser la source, la question exacte et les critères d’achèvement. |
| Créez un Task dans la ligne F avec pour objectif « si P, alors Q ». | Préciser les objets, hypothèses et quantificateurs de P et Q, créer un Task dans la ligne F avec « P implique Q » comme objectif complet et définir les critères d’achèvement. |
| Créez un nouveau Task pour généraliser la proposition P du cas de dimension finie au cas de dimension infinie. | Vérifier la proposition d’origine, préciser les nouveaux objets, hypothèses et la conclusion visée, créer le Task et conserver la proposition d’origine comme cas particulier que la généralisation doit couvrir. |
| Créez un Task pour trouver, dans le cadre P, une formule générale qui inclut la formule (1) d’abc26. | Vérifier les hypothèses et la notation de la formule d’origine, préciser le cadre P et la portée de la formule générale, puis créer un Task dont les critères d’achèvement comprennent une dérivation correcte et une explication de la manière dont elle couvre la formule d’origine. |
| Commencez à travailler sur le Task F0001 jusqu’à ce qu’il reste 5 % du quota hebdomadaire, puis organisez les résultats et faites une pause. | Vérifier l’état actuel du Task et ses conditions d’exécution, puis confirmer que la consommation hebdomadaire pertinente peut être consultée avant de poursuivre. Surveiller le quota restant et arrêter la progression au seuil de 5 %, organiser les résultats, les questions ouvertes et un point de reprise, puis faire une pause. |
| Poursuivez le travail sur le Task F0001. | Lire l’objectif actuel, les stratégies, les résultats existants et les conditions d’arrêt, puis reprendre dans le cadre de l’autorisation actuelle et des limites qui restent en vigueur. Si une condition d’arrêt s’applique toujours, expliquer la raison précise qui empêche la poursuite. |

### Objectifs communs

| Exemple de consigne | Actions attendues de l’agent |
| --- | --- |
| Examinez d’abord les démarches des collaborateurs, puis choisissez une approche utile pour mon Task F0001. | Lire les démarches pertinentes, les résultats réutilisables et les échecs instructifs, puis choisir ou adapter votre propre Strategy dans le périmètre de participation et les conditions d’exécution existantes de F0001. Des démarches différentes peuvent réduire les répétitions ; la vérification indépendante, la réplication et les contrôles croisés délibérés restent appropriés. |
| Établissez un Task conjoint pour cette question et associez-le au Task F0001. | Vérifier la question commune, les hypothèses, la portée et les critères d’achèvement, puis établir ou réutiliser un Task conjoint approprié ; associer votre Task F0001 à la version du contrat commun effectivement adoptée, préciser votre périmètre de participation et vos critères d’achèvement individuels, et conserver les conditions d’exécution existantes. Cette association seule ne lance pas la recherche. |


### Importation de contenu

| Exemple de consigne | Actions attendues de l’agent |
| --- | --- |
| Importez le Task F0001 depuis mon dépôt `〈adresse du dépôt〉`. | Vérifier le dépôt source et votre identité d’auteur, importer F0001 et ses dépendances mathématiques nécessaires, et réutiliser les documents locaux existants suffisants ; recevoir les apports nécessaires d’autres auteurs par Intake et, selon la situation, conserver le lien au contrat commun ou préparer un contrat autonome complet. Conserver les conditions d’arrêt et les quotas en vigueur ; l’importation seule ne lance pas la recherche. |
| Importez mes paramètres de rédaction et le manuscrit F0001 depuis mon dépôt `〈adresse du dépôt〉`. | Importer les paramètres personnels de rédaction sélectionnés et encore applicables, ainsi que les fichiers sources, les figures, la bibliographie et les supports mathématiques nécessaires au manuscrit F0001 ; conserver l’attribution et le périmètre d’application des paramètres, réutiliser les documents locaux existants, corriger les références, effectuer les vérifications de compilation nécessaires et signaler les apports manquants ainsi que les problèmes restants. |
| Recevez depuis `〈adresse du dépôt〉` les documents liés au Task A0001 d’Alice. | Vérifier le dépôt source et l’identité d’Alice en tant qu’auteur, sélectionner les résultats, arguments, calculs et vérifications liés à A0001 et nécessaires à cette demande, puis réutiliser les documents existants suffisants ; lors de la réception, conserver l’attribution initiale, les sources exactes, toute la mathématique nécessaire et les limites réelles des vérifications, et signaler les apports nécessaires non obtenus. Mener les recherches ultérieures dans le cadre de votre propre Task et de votre autorisation. |

### Autres consignes courantes

| Exemple de consigne | Actions attendues de l’agent |
| --- | --- |
| Envisagez de construire un S à l’aide de la théorie A ; ajoutez cette [stratégie](<../Manuel d’utilisation.md#material-strategy>) au Task F0001. | Vérifier l’applicabilité de la théorie A et consigner la construction proposée comme stratégie de recherche pour F0001. Préciser les hypothèses, le rôle envisagé, les étapes restant à vérifier et la prochaine action, puis comparer avec les stratégies existantes afin d’éviter les doublons. |
| Intégrez la discussion ci-dessus aux stratégies de F0001. | Identifier l’approche discutée, mettre à jour une stratégie existante ou en créer une si nécessaire, conserver ses fondements, les questions ouvertes et la prochaine étape, puis l’associer à F0001. |
| Organisez et consignez la discussion ci-dessus conformément aux règles du cadre. | Conserver les énoncés et arguments réutilisables, les constats d’exploration et les autres éléments de preuve nécessaires dans les documents appropriés, avec leurs hypothèses, sources et parties non résolues. Réutiliser les enregistrements existants et corriger les références. |
| Faites le point sur l’avancement actuel de F0001. | Vérifier l’état actuel du Task, distinguer les résultats démontrés, les arguments proposés, les observations issues des calculs et les questions ouvertes, fournir les liens vers les documents pertinents et expliquer ce qu’il reste à accomplir pour atteindre l’objectif d’origine. |
| Organisez les résultats obtenus jusqu’ici, puis faites une pause. | Terminer la vérification et l’organisation du travail du cycle en cours. Conserver les résultats utiles, les tentatives infructueuses, les questions restantes et un point de reprise utilisable ; consigner la pause ainsi que les conditions toujours en vigueur, puis arrêter toute progression supplémentaire. |

## <a id="administration-instructions"></a>Consignes d’administration

Utilisez ces exemples pour les opérations Git, les paramètres de l’environnement et la maintenance courante.

### Commit et push

| Exemple de consigne | Actions attendues de l’agent |
| --- | --- |
| Créez un [commit](<../Manuel d’utilisation.md#notion-commit>) et effectuez un [push](<../Manuel d’utilisation.md#notion-push>). | Déterminer le périmètre de livraison prévu et préserver les modifications déjà indexées qui n’en font pas partie. Vérifier l’identité des contributeurs, la branche et le dépôt distant cible ; confirmer la connectivité, créer le commit et effectuer le push, puis indiquer le périmètre du commit et le résultat sur le dépôt distant. |
| Créez un commit et effectuez un push des modifications du répertoire du manuscrit de F0001. | Repérer le projet de manuscrit de F0001, ne committer que les modifications du répertoire indiqué qui doivent être suivies par Git et préserver les autres travaux. Confirmer l’identité, la destination et la connexion avant le push et indiquer le périmètre réel. |
| Créez un commit de toutes les modifications de l’espace de travail. | Vérifier toutes les modifications de l’espace de travail et leur attribution, créer un commit local du contenu qui doit être suivi par Git, préserver les fichiers exclus par les règles d’ignorance et indiquer le périmètre du commit ainsi que les modifications restantes. |
| Créez un commit et effectuez un push sans aucune vérification. | Omettre la revue du contenu, les vérifications de format, les tests et les recherches supplémentaires. Effectuer uniquement les vérifications de périmètre, d’identité, de destination et de connectivité nécessaires à la livraison Git, puis créer le commit, effectuer le push et indiquer le résultat. |

### Pull et fusion

| Exemple de consigne | Actions attendues de l’agent |
| --- | --- |
| [Récupérez](<../Manuel d’utilisation.md#notion-pull>) les dernières modifications distantes et [fusionnez-les](<../Manuel d’utilisation.md#notion-merge>) avec la [branche locale](<../Manuel d’utilisation.md#notion-git-branch>). | Vérifier la branche actuelle et le dépôt distant correspondant, préserver le travail local, récupérer et fusionner les mises à jour distantes et indiquer le résultat. En cas de conflits affectant le sens mathématique, expliquer les différences précises et proposer la suite à donner. |

### Paramètres de l’environnement

| Exemple de consigne | Actions attendues de l’agent |
| --- | --- |
| Créez une jonction de répertoires de [mathematics/literature/pdf](../../mathematics/literature/pdf) vers `D:\MyLiterature`. | Vérifier le chemin du projet et le répertoire cible, préserver les sources existantes, créer la jonction vers le dossier indiqué et confirmer que les fichiers sources sont exclus de Git. |
| Réglez à 512k la [longueur de contexte](<../Manuel d’utilisation.md#notion-context-length>) par défaut de `<nom de l’environnement d’exécution>` pour ce projet. | Identifier la configuration de l’[environnement d’exécution](../agent-harness.md) pour ce projet, confirmer que le modèle et l’environnement prennent en charge la longueur demandée, puis mettre à jour la valeur par défaut du projet. Expliquer comment la modification prend effet et si son effet réel a été vérifié ; indiquer la limite effective si le réglage demandé n’est pas pris en charge. |
| Définissez ma condition d’arrêt par défaut pour les Tasks : faire une pause lorsqu’il reste 5 % du quota hebdomadaire. | Consigner cette condition comme votre préférence personnelle d’exécution par défaut, applicable lorsqu’aucun réglage plus spécifique n’a priorité. Préserver les conditions effectives des Tasks existants et expliquer comment consulter la consommation hebdomadaire pertinente. |

### Maintenance courante

| Exemple de consigne | Actions attendues de l’agent |
| --- | --- |
| Différez la mise à niveau du cadre et continuez le travail en cours. | Conserver la version installée et poursuivre la mission autorisée ; le rappel n’autorise pas une mise à niveau. |
| Désactivez les vérifications automatiques de version du cadre pour ce dépôt. | Désactiver la vérification quotidienne des métadonnées de version de ce dépôt en préservant le cadre actuel et les travaux de recherche. |
| Activez les vérifications automatiques de version du cadre pour ce dépôt. | Activer la vérification quotidienne du dépôt ; toute mise à niveau ultérieure exige toujours votre demande explicite. |
| Vérifiez à nouveau la version officielle du cadre maintenant. | Effectuer une seule nouvelle vérification avec une durée limitée, indiquer la version installée et la version disponible confirmée ou l’impossibilité de la confirmer, et préserver le rappel déjà effectué. |
| Mettez ce dépôt à niveau vers la version officielle du cadre qui vient d’être identifiée. | Déterminer la version choisie, les fichiers locaux du cadre concernés et la migration réelle des documents, préserver les travaux de recherche et les conditions effectives des Tasks, puis effectuer la mise à niveau explicitement autorisée. |
| Examinez les fichiers de `.tmp` et supprimez ceux qui peuvent l’être sans risque. | Vérifier l’usage des fichiers et s’ils sont en cours d’utilisation. Conserver d’abord tout contenu nécessaire qui n’a pas encore été enregistré dans les documents de recherche, puis supprimer les fichiers confirmés comme jetables et inutilisés par d’autres sessions actives. |

## Rédaction de manuscrits

| Exemple de consigne | Actions attendues de l’agent |
| --- | --- |

## Formalisation en Lean

| Exemple de consigne | Actions attendues de l’agent |
| --- | --- |
