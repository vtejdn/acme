# Git, dépôts Git et GitHub

## <a id="notion-git"></a>Git

Git est un système de gestion de versions distribué qui s’exécute sur votre ordinateur.
Il enregistre les modifications des fichiers, permet de consulter ou de restaurer des versions antérieures et prend en charge plusieurs lignes de développement parallèles.
On peut le comparer à un système de sauvegarde doté d’une machine à remonter le temps, où chaque sauvegarde est un commit auquel vous pouvez revenir.
Git fonctionne localement, sans connexion réseau.

Les principaux concepts sont les suivants.

- Un **commit** est un instantané enregistré, accompagné d’un message et d’une empreinte de hachage unique.
- Une **branche** est une ligne de développement parallèle, par exemple `main` ou `feature-x`.
- Une **fusion** intègre les modifications d’une branche dans une autre.
- L’**arbre de travail** contient les fichiers que vous consultez et modifiez actuellement.
- La **zone de préparation** contient les modifications sélectionnées pour le prochain commit.

Voici quelques commandes courantes.

```bash
git status                         # afficher l’état des modifications
git diff                           # afficher les différences exactes
git add FILE                       # préparer une modification
git commit -m "Describe the change" # enregistrer un instantané
git log                            # consulter l’historique
git branch                         # lister les branches
```

## <a id="notion-git-repository"></a>Dépôt Git

Un dépôt Git comprend un répertoire de projet et un répertoire caché `.git`.
Le répertoire `.git` conserve l’historique complet des commits, les branches, les étiquettes et la configuration.
Les fichiers du projet que vous modifiez constituent l’arbre de travail, tandis que le dépôt conserve leur historique de versions.

Un dépôt peut rester uniquement sur votre ordinateur ou être relié à un ou plusieurs dépôts distants.
On le crée avec `git init`, on le copie avec `git clone` et on le synchronise avec des commandes telles que `git fetch`, `git pull` et `git push`.
`origin` est le nom conventionnel du principal dépôt distant.

Un dépôt Git contient plus qu’un simple dossier de fichiers.
Il conserve un historique complet et consultable de leur évolution jusqu’à leur état actuel.

## <a id="notion-github"></a>GitHub

GitHub est une plateforme cloud d’hébergement de dépôts Git et de collaboration.
Elle appartient à Microsoft et constitue un service distinct de Git.
GitHub fournit du stockage distant, une interface web, des demandes de tirage, des tickets, des discussions, la gestion des permissions et l’automatisation avec GitHub Actions.

Les dépôts Git peuvent aussi être hébergés sur GitLab, Gitee, un serveur d’entreprise ou même un disque local.
GitHub est une plateforme d’hébergement et de collaboration courante, mais son utilisation n’est pas nécessaire pour utiliser Git.

### <a id="connect-github"></a>Relier un projet local à GitHub

Suivez ces étapes pour relier pour la première fois un dossier de projet de votre ordinateur à GitHub.
Le dossier du projet contient les fichiers que vous modifiez, tandis que le dépôt GitHub constitue l’emplacement en ligne du projet.
Ce guide utilise SSH, qui permet à Git de s’authentifier auprès de GitHub avec une clé conservée sur votre ordinateur.

1. **Connectez-vous à GitHub dans votre navigateur.**

   Ouvrez [GitHub](https://github.com/) et sélectionnez **Sign in**.
   Si vous avez besoin d’un compte, sélectionnez **Sign up**, puis suivez les instructions pour vérifier votre adresse électronique.
   Utilisez ce même compte pour ajouter votre clé SSH par la suite.
   Si vous rejoignez le dépôt existant d’un collaborateur, suivez d’abord les [étapes pour rejoindre une collaboration](<../Manuel d’utilisation.md#setup-collaboration>) afin d’accepter l’invitation et de vérifier vos droits d’accès.

2. **Créez un dépôt vide pour votre projet.**

   Si le projet dispose déjà d’un dépôt GitHub, par exemple lorsque vous rejoignez le dépôt d’un collaborateur, passez à l’étape 3.
   Sinon, ouvrez la [page de création d’un dépôt](https://github.com/new).

   1. Dans **Owner**, sélectionnez votre compte GitHub.
   2. Dans **Repository name**, saisissez un nom tel que `my-math-project`.
   3. Dans **Visibility**, choisissez qui pourra consulter le dépôt.
      Sélectionnez **Private** pour restreindre la visibilité du projet.
   4. Désactivez l’ajout d’un README et choisissez **None** pour les options `.gitignore` et de licence.
      Vous obtiendrez ainsi un dépôt vide pour votre projet existant.
   5. Sélectionnez **Create repository**.

   Consultez le [guide GitHub de création d’un dépôt](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository).

3. **Demandez à votre agent de préparer Git.**

   Pour un projet local existant, ouvrez son dossier dans votre environnement d’exécution d’agents, par exemple le dossier où ACME est déjà installé et utilisé.
   Si vous rejoignez le dépôt existant d’un collaborateur, créez un nouveau dossier local vide et ouvrez ce dossier dans votre environnement d’exécution d’agents.
   Envoyez à votre agent la [consigne d’installation de Git](<../user-instructions/Exemples de consignes.md#install-git>).
   Poursuivez lorsque l’agent confirme que Git est prêt.

4. **Configurez l’accès SSH pour votre compte GitHub.**

   Une clé SSH comporte deux parties.
   Vous ajoutez la clé publique à GitHub, tandis que la clé privée reste sur l’ordinateur où Git s’exécute.
   Envoyez la demande suivante à votre agent.

   > Aidez-moi à configurer SSH pour mon nouveau compte GitHub et montrez-moi la clé publique à ajouter.

   Si le terminal demande la phrase secrète de la clé, saisissez-la dans le terminal.
   Consultez le [guide GitHub de création d’une clé SSH et de son ajout à l’agent SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

   Dans votre navigateur, ajoutez la clé publique à votre compte GitHub.

   1. Copiez la ligne complète de la clé publique fournie par l’agent.
      Le nom du fichier de clé publique se termine par `.pub`.
   2. Sur GitHub, cliquez sur votre photo de profil, puis choisissez **Settings**.
      Dans la barre latérale, sélectionnez **SSH and GPG keys**, puis cliquez sur **New SSH key** ou **Add SSH key**.
   3. Dans **Title**, saisissez un nom facile à reconnaître, tel que `Personal laptop`.
      Dans **Key type**, choisissez **Authentication Key**.
   4. Collez la clé publique dans **Key**, cliquez sur **Add SSH key** et confirmez votre compte si cela vous est demandé.

   Consultez les [instructions GitHub pour ajouter une clé publique](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).

   Après avoir ajouté la clé, envoyez à votre agent la [consigne de test SSH](<../user-instructions/Exemples de consignes.md#test-github-ssh>).
   Poursuivez lorsque l’agent confirme que GitHub reconnaît votre compte.

5. **Reliez votre projet à GitHub.**

   Pour un projet local existant, utilisez la [consigne de connexion](<../user-instructions/Exemples de consignes.md#connect-github>) et remplacez l’adresse d’exemple par celle du dépôt cible.
   Pour rejoindre le dépôt existant d’un collaborateur, utilisez la [consigne de clonage](<../user-instructions/Exemples de consignes.md#clone-repo>) et demandez explicitement à l’agent de cloner le dépôt dans le dossier vide préparé à l’étape 3.
   Après le clonage, suivez les [étapes pour rejoindre une collaboration](<../Manuel d’utilisation.md#setup-collaboration>) pour compléter, si nécessaire, votre enregistrement comme auteur et la configuration de l’identité utilisée pour vos commits Git.
