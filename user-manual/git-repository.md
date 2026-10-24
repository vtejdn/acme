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
