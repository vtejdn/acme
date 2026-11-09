# Git, Git Repositories and GitHub

## <a id="notion-git"></a>Git

Git is a distributed version-control system that runs on your own computer.
It records changes to files, lets you inspect or restore earlier versions, and supports parallel lines of work.
A useful analogy is a save system with a time machine: each save is a commit, and you can travel back to any of them.
Git works locally and does not require a network connection.

The main concepts are:

- **Commit**: one recorded snapshot with a message and a unique hash.
- **Branch**: a parallel line of development, such as `main` or `feature-x`.
- **Merge**: combining the changes from one branch into another.
- **Working tree**: the files you currently see and edit.
- **Staging area**: the changes selected for the next commit.

Typical commands are:

```bash
git status        # show what has changed
git diff          # show the actual differences
git add FILE      # stage a change
git commit -m ""  # record a snapshot
git log           # show the history
git branch        # list branches
```

## <a id="notion-git-repository"></a>Git Repository

A Git repository is a project directory together with a hidden `.git` directory.
The `.git` directory stores the full commit history, branches, tags and configuration.
The project files you edit are the working tree; the repository is the versioned history behind them.

A repository can live only on your computer, or it can be linked to one or more remote repositories.
It is created with `git init`, copied with `git clone`, and synchronized with commands such as `git fetch`, `git pull` and `git push`.
The remote named `origin` is simply the conventional name for the main remote copy.

A Git repository is more than a folder of files.
It is the complete, inspectable record of how those files reached their current state.

## <a id="notion-github"></a>GitHub

GitHub is a cloud platform for hosting and collaborating on Git repositories.
It is owned by Microsoft, and it is not the same thing as Git.
GitHub adds remote storage, a web interface, pull requests, issues, discussions, permissions and automation through GitHub Actions.

Git repositories can also be hosted on GitLab, Gitee, a company server or even a local disk.
GitHub is a popular hosting and collaboration layer, not a requirement for using Git.

### Connect a local project to GitHub

Use these steps to connect a project folder on your computer to GitHub for the first time.
The project folder holds the files you edit, and the GitHub repository is the online location for the project.
This walkthrough uses SSH, which lets Git sign in to GitHub with a key from your computer.

1. **Sign in to GitHub in your browser.**

   Open [GitHub](https://github.com/) and select **Sign in**.
   If you need an account, select **Sign up** and follow the instructions to verify your email address.
   Use this account when you add your SSH key later.

2. **Create an empty repository for your project.**

   If your project already has a GitHub repository, skip to step 3.
   Open the [new repository page](https://github.com/new).

   1. Under **Owner**, select your GitHub account.
   2. Under **Repository name**, enter a name such as `my-math-project`.
   3. Choose who can see the repository under **Visibility**.
      Select **Private** to restrict who can see the project.
   4. Leave the README option off and choose **None** for the `.gitignore` and license options.
      This gives you an empty repository for your existing project.
   5. Select **Create repository**.

   See [GitHub's guide to creating a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository).

3. **Ask your agent to prepare Git.**

   Open your project folder in the app where you use your agent.
   Send your agent the [Install Git instruction](user-instructions/user-instructions.md#install-git).
   Continue when the agent confirms that Git is ready.

4. **Set up SSH access for your GitHub account.**

   An SSH key has two parts.
   You add the public key to GitHub, and the private key stays where Git runs.
   Send your agent the following request.

   > Help me set up SSH for my new GitHub account and show me the public key to add.

   If the terminal asks for a key passphrase, enter it there.
   See [GitHub's guide to creating and loading an SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

   Add the public key to your GitHub account in your browser.

   1. Copy the full line of public key text provided by the agent.
      The public key file name ends in `.pub`.
   2. On GitHub, click your profile picture and choose **Settings**.
      In the sidebar, select **SSH and GPG keys**, then click **New SSH key** or **Add SSH key**.
   3. Under **Title**, enter a name you will recognize, such as `Personal laptop`.
      Under **Key type**, choose **Authentication Key**.
   4. Paste the public key into **Key**, click **Add SSH key**, and confirm your account if prompted.

   See [GitHub's instructions for adding a public key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).

   After adding the key, send your agent the [SSH test instruction](user-instructions/user-instructions.md#test-github-ssh).
   Continue when the agent confirms that GitHub recognizes your account.

5. **Connect your project to GitHub.**

   In the [connection instruction](user-instructions/user-instructions.md#connect-github), replace the example address with your repository's GitHub page address.
   Send the instruction to your agent.
   The connection is ready when the agent confirms it can read the repository.
