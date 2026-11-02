# Exemples de consignes

[Manuel d’utilisation](<../Manuel d’utilisation.md>)

Décrivez votre objectif en langage naturel.
Les exemples ci-dessous sont répartis entre les consignes de [configuration](#setup), de [recherche](#research-instructions), d’[administration](#administration-instructions), de [rédaction de manuscrits](#writing-instructions) et de [formalisation en Lean](#lean-instructions).
Adaptez les formulations à votre question, à vos fichiers et au périmètre réel de votre travail.

## <a id="setup"></a>Consignes de configuration

Utilisez ces exemples pour préparer votre espace de travail, enregistrer votre identité d’auteur et configurer les ressources locales.
Consultez la section [Configuration](<../Manuel d’utilisation.md#setup>) du manuel pour connaître l’ordre des étapes d’installation et d’enregistrement.

| Exemple de consigne | Actions attendues de l’agent |
| --- | --- |
| Téléchargez ACME (https://github.com/vtejdn/acme) dans `D:\acme`. | Vérifier que la destination convient à l’installation, télécharger les fichiers du cadre ACME, préserver le contenu existant et indiquer la version ainsi que les éventuelles étapes de configuration restantes. |
| Installez [Git](../git-repository.md#notion-git). | Vérifier si Git est déjà installé, l’installer si nécessaire et indiquer la version disponible ainsi que les éventuelles étapes de configuration restantes. |
| Enregistrez Ali comme ma clé d’auteur ; utilisez Alice comme nom complet. | Après vérification de la clé et des enregistrements existants, utiliser les valeurs fournies : `Ali` comme clé d’auteur et `Alice` comme nom pour l’attribution dans `LICENSE`. Vous enregistrer, ajouter l’attribution en préservant les identités et mentions existantes, et associer cette copie de travail à `Ali` si elle utilise Git. |
| Expliquez-moi comment me connecter à [GitHub](../git-repository.md#notion-github). | Expliquer comment se connecter, s’authentifier et relier l’espace de travail à un dépôt distant, en identifiant les étapes que vous devez effectuer vous-même. |
| Je me suis connecté à GitHub. Testez la connexion. | Vérifier le compte authentifié et tester en lecture seule la connectivité à GitHub et au dépôt cible. Indiquer le résultat ou l’erreur précise. |
| [Clonez](<../Manuel d’utilisation.md#notion-clone>) ACME (https://github.com/vtejdn/acme) dans `D:\acme`. | Vérifier que Git, les autorisations d’accès et la destination sont prêts, cloner le dépôt ACME avec son historique de versions et indiquer la branche, la version et les étapes d’initialisation restantes. |
| Définissez la clé du dépôt sur `〈clé du dépôt〉`. | Vérifier la clé choisie, enregistrer une valeur valide et mettre à jour les références actuelles concernées ; vous demander un autre choix si elle est invalide. La clé du dépôt est indépendante de l’abréviation, du nom complet et du titre du README du projet ; préserver le sens des clés d’auteur, des identités des documents et des informations historiques de provenance. |
| Définissez l’abréviation et le nom complet du dépôt sur `〈abréviation〉` et `〈nom complet〉`. | Enregistrer l’abréviation et le nom complet que vous avez choisis séparément, en vérifiant que chacun est un texte non vide sur une seule ligne. Les utiliser pour former le titre principal du README « 〈abréviation〉: 〈nom complet〉 », maintenir la cohérence entre configuration et titre et préserver le reste du texte. Définir la clé du dépôt séparément de ces choix. |
| Configurez Git et reliez-le à mon dépôt <https://github.com/alice/acme>. | Initialiser Git uniquement si nécessaire, compléter les éventuels enregistrements manquants du nom du dépôt ou de l’auteur selon vos choix, puis associer la copie de travail à votre clé d’auteur. Vérifier ou configurer l’identité des commits pour qu’elle corresponde à votre enregistrement, relier le dépôt distant indiqué et tester l’accès par le compte ou le canal d’authentification pertinent. Préserver les commits existants, les paramètres sans rapport avec la demande et les limites des Tasks, puis indiquer la destination configurée et les étapes de configuration restantes. |
| Clonez le dépôt de mon collaborateur <https://github.com/alice/acme> et enregistrez-moi sous le nom Bob. | Cloner le dépôt partagé et vérifier la clé d’auteur `Bob`, votre identité réelle et les enregistrements existants. Lors d’un premier enregistrement, demander le nom d’attribution pour `LICENSE` choisi indépendamment avant de vous enregistrer et d’ajouter la mention nécessaire. Réutiliser une identité existante applicable, associer la nouvelle copie de travail Git à la clé vérifiée, préserver les auteurs et documents de recherche existants et expliquer les paramètres d’identité des commits Git. |

## <a id="research-instructions"></a>Consignes de recherche

Utilisez ces exemples pour travailler sur la littérature et explorer des questions mathématiques.

### Rechercher, enregistrer ou vérifier la littérature

| Exemple de consigne | Actions attendues de l’agent |
| --- | --- |
| Examinez la source locale abc26, enregistrez-la et vérifiez-la. | Identifier l’œuvre, l’édition et l’original local correspondant à abc26, compléter la bibliographie et tenir à jour, au besoin, les notes sur l’édition et l’emplacement de l’original. Si l’original contient une table des matières, en préparer une copie interrogeable. Vérifier le contenu mathématique et consigner le périmètre examiné, les conclusions et les questions non résolues. |
| Vérifiez le théorème 1.7 dans abc26. | Repérer le théorème 1.7 dans l’original, vérifier son énoncé complet, ses hypothèses, sa démonstration et l’applicabilité des résultats nécessaires dont il dépend, puis consigner les constats, les parties non vérifiées et les lacunes précises. |
| Recherchez *On the construction of S* et essayez de l’enregistrer et de le vérifier. | Identifier l’œuvre et l’édition, consulter les documents existants et tenter d’obtenir l’original ; compléter la bibliographie et tenir à jour, au besoin, les notes sur l’édition obtenue et l’emplacement de la source. Si l’original contient une table des matières, en préparer une copie interrogeable. Vérifier le contenu obtenu et signaler les échecs d’acquisition, les parties indisponibles et le périmètre réellement examiné. |
| Comment cette définition est-elle utilisée dans la littérature pertinente ? | Consulter les enregistrements de définitions existants et les sources originales pertinentes, comparer les objets, hypothèses, notations et usages, fournir des références précises et distinguer les définitions des sources des reformulations ou généralisations locales. |

### <a id="start-or-continue-research"></a>[Task](<../Manuel d’utilisation.md#material-task>)

| Exemple de consigne | Actions attendues de l’agent |
| --- | --- |
| Créez un Task dans la [ligne W](<../Manuel d’utilisation.md#notion-research-line-letter>) pour la conjecture 1.3 d’abc26. | Vérifier l’énoncé original, les hypothèses et la portée de la conjecture 1.3 et rechercher d’abord un Task existant sur la même question. Si un nouveau Task est nécessaire, utiliser la ligne W et préciser la source, la question exacte et les critères d’achèvement. |
| Créez un Task dans la ligne F avec pour objectif « si P, alors Q ». | Préciser les objets, hypothèses et quantificateurs de P et Q, créer un Task dans la ligne F avec « P implique Q » comme objectif complet et définir les critères d’achèvement. |
| Créez un nouveau Task pour généraliser la proposition P du cas de dimension finie au cas de dimension infinie. | Vérifier la proposition d’origine, préciser les nouveaux objets, hypothèses et la conclusion visée, créer le Task et conserver la proposition d’origine comme cas particulier que la généralisation doit couvrir. |
| Créez un Task pour trouver, dans le cadre P, une formule générale qui inclut la formule (1) d’abc26. | Vérifier les hypothèses et la notation de la formule d’origine, préciser le cadre P et la portée de la formule générale, puis créer un Task dont les critères d’achèvement comprennent une dérivation correcte et une explication de la manière dont elle couvre la formule d’origine. |
| Commencez à travailler sur le Task F0001 jusqu’à ce qu’il reste 5 % du quota hebdomadaire. | Vérifier l’état actuel du Task et ses conditions d’exécution en vigueur, puis confirmer que la consommation hebdomadaire du compte concerné peut être consultée ; sinon, expliquer la limite et différer la progression. Lorsque les conditions d’exécution sont remplies, avancer et surveiller le quota restant ; s’arrêter dès la première observation d’un quota restant inférieur ou égal à 5 % ou en cas de défaillance du suivi. Conserver les résultats utiles, les questions ouvertes et le point de reprise, puis consigner les conditions d’arrêt en vigueur. |
| Organisez les résultats obtenus jusqu’ici, puis faites une pause. | Terminer la vérification et l’organisation du travail du cycle en cours. Conserver les résultats utiles, les tentatives infructueuses, les questions restantes et un point de reprise utilisable ; consigner la pause ainsi que les conditions toujours en vigueur, puis arrêter toute progression supplémentaire. |
| Faites le point sur l’avancement actuel de F0001. | Vérifier l’état actuel du Task, distinguer les résultats démontrés, les arguments proposés, les observations issues des calculs et les questions ouvertes, fournir les liens vers les documents pertinents et expliquer ce qu’il reste à accomplir pour atteindre l’objectif d’origine. |
| Poursuivez le travail sur le Task F0001. | Lire l’objectif actuel, les stratégies, les résultats existants et les conditions d’arrêt, puis reprendre dans le cadre de l’autorisation actuelle et des limites qui restent en vigueur. Si une condition d’arrêt s’applique toujours, expliquer la raison précise qui empêche la poursuite. |

### [Stratégies](<../Manuel d’utilisation.md#material-strategy>)

| Exemple de consigne | Actions attendues de l’agent |
| --- | --- |
| Envisagez de construire un S à l’aide de la théorie A ; ajoutez cette stratégie au [Task](<../Manuel d’utilisation.md#material-task>) F0001. | Vérifier l’applicabilité de la théorie A et consigner la construction proposée comme stratégie de recherche pour F0001. Préciser les hypothèses, le rôle envisagé, les étapes restant à vérifier et la prochaine action, puis comparer avec les stratégies existantes afin d’éviter les doublons. |
| Intégrez la discussion ci-dessus aux stratégies de F0001. | Identifier l’approche discutée, mettre à jour une stratégie existante ou en créer une si nécessaire, conserver ses fondements, les questions ouvertes et la prochaine étape, puis l’associer à F0001. |
| Recherchez et analysez des approches pour le Task G0001, proposez des stratégies et fixez leurs priorités de façon autonome. | Lire l’objectif de G0001, ses contraintes, les stratégies existantes et les documents pertinents, réutiliser d’abord les résultats locaux, puis rechercher et vérifier la littérature selon les besoins. Comparer les conditions d’applicabilité, les fondements, les obstacles et les ressources nécessaires aux démarches proposées, proposer des stratégies et fixer leurs priorités de façon autonome ; consigner les motifs du classement, les étapes non résolues et la prochaine action, tout en conservant l’objectif d’origine, les critères d’achèvement et les limites d’exécution en vigueur. |

### [Tasks conjoints](<../Manuel d’utilisation.md#material-task>)

| Exemple de consigne | Actions attendues de l’agent |
| --- | --- |
| Examinez d’abord les démarches de la collaboratrice Alice, puis choisissez une approche utile pour mon Task F0001. | Lire les démarches pertinentes, les résultats réutilisables et les échecs instructifs, puis choisir ou adapter votre propre Strategy dans le périmètre de participation et les conditions d’exécution existantes de F0001. Des démarches différentes peuvent réduire les répétitions ; la vérification indépendante, la réplication et les contrôles croisés délibérés restent appropriés. |
| Établissez un Task conjoint pour cette question et associez-le au Task F0001. | Vérifier la question commune, les hypothèses, la portée et les critères d’achèvement, puis établir ou réutiliser un Task conjoint approprié ; associer votre Task F0001 à la version du contrat commun effectivement adoptée, préciser votre périmètre de participation et vos critères d’achèvement individuels, et conserver les conditions d’exécution existantes. Cette association seule ne lance pas la recherche. |

### [Énoncés mathématiques](<../Manuel d’utilisation.md#material-claim>) et [Carnets d’exploration](<../Manuel d’utilisation.md#material-ledger>)

| Exemple de consigne | Actions attendues de l’agent |
| --- | --- |
| Organisez et consignez la discussion ci-dessus conformément aux règles du cadre. | Conserver les énoncés et arguments réutilisables, les constats d’exploration et les autres éléments de preuve nécessaires dans les documents appropriés, avec leurs hypothèses, sources et parties non résolues. Réutiliser les enregistrements existants et corriger les références. |

## <a id="administration-instructions"></a>Consignes d’administration

Utilisez ces exemples pour les opérations [Git](../git-repository.md#notion-git), les paramètres de l’environnement et la maintenance courante.

### [Commit](<../Manuel d’utilisation.md#notion-commit>) et [push](<../Manuel d’utilisation.md#notion-push>)

| Exemple de consigne | Actions attendues de l’agent |
| --- | --- |
| Créez un commit et effectuez un push. | Déterminer le périmètre de livraison prévu et préserver les modifications déjà indexées qui n’en font pas partie. Vérifier l’identité des contributeurs, la branche et le dépôt distant cible ; confirmer la connectivité, créer le commit et effectuer le push, puis indiquer le périmètre du commit et le résultat sur le dépôt distant. |
| Créez un commit et effectuez un push des modifications du répertoire du manuscrit de F0001. | Repérer le projet de manuscrit de F0001, ne committer que les modifications du répertoire indiqué qui doivent être suivies par Git et préserver les autres travaux. Confirmer l’identité, la destination et la connexion avant le push et indiquer le périmètre réel. |
| Créez un commit de toutes les modifications de l’espace de travail. | Vérifier toutes les modifications de l’espace de travail et leur attribution, créer un commit local du contenu qui doit être suivi par Git, préserver les fichiers exclus par les règles d’ignorance et indiquer le périmètre du commit ainsi que les modifications restantes. |
| Créez un commit et effectuez un push sans aucune vérification. | Omettre la revue du contenu, les vérifications de format, les tests et les recherches supplémentaires. Effectuer uniquement les vérifications de périmètre, d’identité, de destination et de connectivité nécessaires à la livraison Git, puis créer le commit, effectuer le push et indiquer le résultat. |

### [Pull](<../Manuel d’utilisation.md#notion-pull>) et [fusion](<../Manuel d’utilisation.md#notion-merge>)

| Exemple de consigne | Actions attendues de l’agent |
| --- | --- |
| Récupérez les dernières modifications distantes et fusionnez-les avec la [branche locale](<../Manuel d’utilisation.md#notion-git-branch>). | Vérifier la branche actuelle et le dépôt distant correspondant, préserver le travail local, récupérer et fusionner les mises à jour distantes et indiquer le résultat. En cas de conflits affectant le sens mathématique, expliquer les différences précises et proposer la suite à donner. |

### Paramètres de l’environnement

| Exemple de consigne | Actions attendues de l’agent |
| --- | --- |
| Créez une jonction de répertoires de [mathematics/literature/pdf](../../mathematics/literature/pdf) vers `D:\MyLiterature`. | Vérifier le chemin du projet et le répertoire cible, préserver les sources existantes, créer la jonction vers le dossier indiqué et confirmer que les fichiers sources sont exclus de Git. |
| Réglez à 512k la [longueur de contexte](<../Manuel d’utilisation.md#notion-context-length>) par défaut de `<nom de l’environnement d’exécution>` pour ce projet. | Identifier la configuration de l’[environnement d’exécution](../agent-harness.md) pour ce projet, confirmer que le modèle et l’environnement prennent en charge la longueur demandée, puis mettre à jour la valeur par défaut du projet. Expliquer comment la modification prend effet et si son effet réel a été vérifié ; indiquer la limite effective si le réglage demandé n’est pas pris en charge. |
| Définissez ma condition d’arrêt par défaut pour les Tasks : faire une pause lorsqu’il reste 5 % du quota hebdomadaire. | Consigner cette condition comme votre préférence personnelle d’exécution par défaut, applicable lorsqu’aucun réglage plus spécifique n’a priorité. Préserver les conditions effectives des Tasks existants et expliquer comment consulter la consommation hebdomadaire pertinente. |

### [Importation](<../Manuel d’utilisation.md#notion-import>) et [réception](<../Manuel d’utilisation.md#notion-intake>)

| Exemple de consigne | Actions attendues de l’agent |
| --- | --- |
| Importez le Task F0001 depuis mon dépôt `〈adresse du dépôt〉`. | Vérifier le dépôt source et votre identité d’auteur, importer F0001 et ses dépendances mathématiques nécessaires, et réutiliser les documents locaux existants suffisants ; recevoir les apports nécessaires d’autres auteurs par Intake et, selon la situation, conserver le lien au contrat commun ou préparer un contrat autonome complet. Conserver les conditions d’arrêt et les quotas en vigueur ; l’importation seule ne lance pas la recherche. |
| Importez mes paramètres de rédaction et le manuscrit F0001 depuis mon dépôt `〈adresse du dépôt〉`. | Importer les paramètres personnels de rédaction sélectionnés et encore applicables, ainsi que les fichiers sources, les figures, la bibliographie et les supports mathématiques nécessaires au manuscrit F0001 ; conserver l’attribution et le périmètre d’application des paramètres, réutiliser les documents locaux existants, corriger les références, effectuer les vérifications de compilation nécessaires et signaler les apports manquants ainsi que les problèmes restants. |
| Recevez depuis `〈adresse du dépôt〉` les documents liés au Task A0001 d’Alice. | Vérifier le dépôt source et l’identité d’Alice en tant qu’auteur, sélectionner les résultats, arguments, calculs et vérifications liés à A0001 et nécessaires à cette demande, puis réutiliser les documents existants suffisants ; lors de la réception, conserver l’attribution initiale, les sources exactes, toute la mathématique nécessaire et les limites réelles des vérifications, et signaler les apports nécessaires non obtenus. Mener les recherches ultérieures dans le cadre de votre propre Task et de votre autorisation. |

### Maintenance courante

| Exemple de consigne | Actions attendues de l’agent |
| --- | --- |
| Activez/désactivez les vérifications automatiques de version du cadre pour ce dépôt. | Mettre à jour le paramètre de ce dépôt selon votre choix d’activer ou de désactiver les vérifications, préserver le reste de la configuration et indiquer le réglage actuel ; une fois les vérifications activées, appliquer les règles de vérification automatique par jour UTC. Une mise à niveau exige toujours une autorisation explicite effective. |
| Mettez le cadre à niveau vers la dernière version. | Vérifier la version installée et la dernière version officielle ; si une mise à jour est disponible, fixer la version et le commit cibles, adapter les fichiers concernés selon les notes de mise à niveau et effectuer les vérifications nécessaires, en préservant les modifications locales, les documents de recherche, les paramètres personnels et les conditions d’exécution en vigueur. Mettre à jour la version installée après réussite des vérifications ; dans un véritable dépôt Git partagé entre plusieurs auteurs, créer le commit, effectuer le push et confirmer le résultat distant selon l’autorisation par défaut, en respectant les restrictions explicites de travail local, de mode hors ligne ou d’interdiction de push. Indiquer les versions avant et après, le commit cible, les vérifications, le résultat de la livraison et toute absence de mise à jour ou opération inachevée. |
| Résolvez les conflits de fusion conformément aux règles du cadre. | Examiner les modifications des deux parties, leur attribution et l’autorité effective, puis résoudre directement les conflits administratifs dont la solution peut être déterminée, notamment les corrections de localisation qui préservent l’objet et le sens mathématique. Pour les désaccords mathématiques de fond, conserver les éléments de preuve des deux parties, expliquer les différences et effectuer une nouvelle vérification délimitée selon l’autorisation existante ou après obtention de l’autorisation nécessaire ; conserver les corrections substantielles du contenu d’un autre auteur dans les documents propres à l’auteur des corrections. Vérifier le résultat de la fusion et les références concernées, puis indiquer le résultat et les questions non résolues. |
| Examinez les fichiers de `.tmp` et supprimez ceux qui peuvent l’être sans risque. | Vérifier l’usage des fichiers et s’ils sont en cours d’utilisation. Conserver d’abord tout contenu nécessaire qui n’a pas encore été enregistré dans les documents de recherche, puis supprimer les fichiers confirmés comme jetables et inutilisés par d’autres sessions actives. |
| Vérifiez si les documents mathématiques locaux sont conformes aux règles du cadre. | Dans le périmètre demandé, faire examiner par lots en lecture seule les documents mathématiques locaux ainsi que les apports et références nécessaires par un agent isolé des étapes de réparation et d’acceptation ; vérifier l’attribution, les versions, les évaluations, les sources, les correspondances entre vérifications et éléments examinés et les autres exigences applicables. Consigner les problèmes de conformité dans `maintenance` et les problèmes mathématiques de fond dans `erratum`, puis indiquer le périmètre réellement couvert, les parties non examinées et les points non résolus. |
| Consultez maintenance et erratum, puis effectuez les réparations selon les règles du cadre. | Lire les points en attente de réparation dans le périmètre demandé ; confier à un agent respectant l’isolation des étapes la vérification des problèmes, les réparations dans les limites de l’autorité effective sur les documents de chaque auteur, l’autocontrôle et la vérification des documents et programmes nécessaires qui en dépendent. Faire accepter les réparations de conformité par un agent indépendant et appliquer aux erreurs mathématiques les exigences effectives de version, d’évaluation et de vérification mathématique ; conserver le problème d’origine, ses fondements, les exigences d’acceptation et les points non réparés ou non acceptés, puis indiquer le périmètre réparé et les limites restantes. |
| Procédez à l’acceptation des réparations de documents selon les règles du cadre. | Faire vérifier les réparations soumises et les documents et programmes nécessaires qui en dépendent par un agent indépendant n’ayant ni participé à l’inspection ou à la réparation du même périmètre, ni hérité des discussions substantielles correspondantes, au regard des problèmes initiaux et des règles actuelles ; indiquer les parties acceptées ou refusées. Ne retirer des listes de suivi les parties acceptées que dans les limites de l’autorité effective de l’auteur concerné ou du destinataire pour leur traitement local, en conservant les points refusés, non acceptés, hors périmètre et ajoutés simultanément ; l’acceptation ne répare pas les documents et l’acceptation de conformité n’est pas une vérification mathématique indépendante. |

## <a id="writing-instructions"></a>Rédaction de manuscrits

| Exemple de consigne | Actions attendues de l’agent |
| --- | --- |

## <a id="lean-instructions"></a>Formalisation en Lean

| Exemple de consigne | Actions attendues de l’agent |
| --- | --- |

