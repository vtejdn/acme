# Git、Git 仓库与 GitHub

## <a id="notion-git"></a>Git

Git 是运行在自己计算机上的分布式版本控制系统。
它记录文件的改动，让你查看或恢复早期版本，并支持多条并行的开发线。
可以把它理解为带有时间机器的存档系统，每次存档都是一次提交，你可以回到其中任意一个版本。
Git 可以在本地工作，无需网络连接。

主要概念如下。

- **提交（Commit）**是一份已记录的快照，带有说明消息和唯一的哈希值。
- **分支（Branch）**是一条并行的开发线，例如 `main` 或 `feature-x`。
- **合并（Merge）**是将一个分支的改动整合到另一个分支。
- **工作树（Working tree）**是你当前看到并编辑的文件。
- **暂存区（Staging area）**保存为下一次提交选定的改动。

常用命令如下。

```bash
git status                         # 查看改动状态
git diff                           # 查看具体差异
git add FILE                       # 暂存文件改动
git commit -m "Describe the change" # 记录一次快照
git log                            # 查看提交历史
git branch                         # 列出分支
```

## <a id="notion-git-repository"></a>Git 仓库

Git 仓库由项目目录和一个隐藏的 `.git` 目录组成。
`.git` 目录保存完整的提交历史、分支、标签和配置。
你编辑的项目文件构成工作树，仓库则保存这些文件的版本历史。

仓库可以只存放在自己的计算机上，也可以连接到一个或多个远程仓库。
可以用 `git init` 创建仓库，用 `git clone` 克隆仓库，用 `git fetch`、`git pull` 和 `git push` 等命令同步仓库。
`origin` 是主要远程仓库的惯用名称。

Git 仓库保存的不只是一个文件夹中的文件。
它完整记录了这些文件如何演变到当前状态，供你查看和追溯。

## <a id="notion-github"></a>GitHub

GitHub 是用于托管 Git 仓库和开展协作的云平台。
它由微软拥有，与 Git 是两个不同的事物。
GitHub 提供远程存储、网页界面、拉取请求、议题、讨论、权限管理，以及通过 GitHub Actions 实现的自动化。

Git 仓库也可以托管在 GitLab、Gitee、公司服务器，或存放在本地磁盘上。
GitHub 是常用的托管与协作平台，使用 Git 本身并不要求使用 GitHub。

### <a id="connect-github"></a>将本地项目连接到 GitHub

首次将计算机上的项目文件夹连接到 GitHub 时，可以按以下步骤操作。
项目文件夹保存你编辑的文件，GitHub 仓库则是项目的在线存放位置。
本指南使用 SSH，让 Git 通过计算机上的密钥向 GitHub 认证身份。

1. **在浏览器中登录 GitHub。**

   打开 [GitHub](https://github.com/)，选择 **Sign in**。
   如需新账号，选择 **Sign up**，并按提示验证邮箱。
   后续添加 SSH 公钥时，使用同一个账号。
   加入合作者的已有仓库时，请先按[手册中的加入步骤](../用户手册.md#setup-collaboration)接受邀请并确认访问权限。

2. **为项目创建空仓库。**

   如果项目已有 GitHub 仓库，例如以合作者身份加入其他人的仓库，直接进入第 3 步。
   否则，打开[创建仓库页面](https://github.com/new)。

   1. 在 **Owner** 下选择你的 GitHub 账号。
   2. 在 **Repository name** 下输入仓库名称，例如 `my-math-project`。
   3. 在 **Visibility** 下选择谁可以查看仓库。
      选择 **Private** 可限制项目的可见范围。
   4. 关闭添加 README 的选项，并为 `.gitignore` 和许可证选项选择 **None**。
      这样就能为已有项目创建一个空仓库。
   5. 选择 **Create repository**。

   参见 [GitHub 创建仓库指南](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)。

3. **请 agent 准备 Git。**

   已有本地项目时，在 agent 运行环境中打开该项目文件夹，例如已经安装并使用 ACME 框架的文件夹。
   加入合作者的已有仓库时，在本机新建一个空文件夹，并在 agent 运行环境中打开这个空文件夹。
   向 agent 发送[安装 Git 的指令](../user-instructions/用户指令.md#install-git)。
   agent 确认 Git 已准备就绪后，再继续。

4. **为 GitHub 账号配置 SSH 访问。**

   SSH 密钥由两部分组成。
   你将公钥添加到 GitHub，私钥则保留在运行 Git 的计算机上。
   向 agent 发送以下请求。

   > 帮我为新的 GitHub 账号配置 SSH，并显示需要添加的公钥。

   如果终端要求输入密钥口令，请在终端中输入。
   参见 [GitHub 创建 SSH 密钥并将其加载到 SSH agent 的指南](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)。

   在浏览器中将公钥添加到你的 GitHub 账号。

   1. 复制 agent 提供的完整公钥文本行。
      公钥文件名以 `.pub` 结尾。
   2. 在 GitHub 上点击头像，选择 **Settings**。
      在侧边栏选择 **SSH and GPG keys**，再点击 **New SSH key** 或 **Add SSH key**。
   3. 在 **Title** 下输入便于辨认的名称，例如 `Personal laptop`。
      在 **Key type** 下选择 **Authentication Key**。
   4. 将公钥粘贴到 **Key**，点击 **Add SSH key**，并按提示确认账号。

   参见 [GitHub 添加公钥的说明](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)。

   添加公钥后，向 agent 发送 [SSH 连接测试指令](../user-instructions/用户指令.md#test-github-ssh)。
   agent 确认 GitHub 识别出你的账号后，再继续。

5. **将项目连接到 GitHub。**

   已有本地项目时，使用[连接指令](../user-instructions/用户指令.md#connect-github)，将示例地址替换为目标仓库地址。
   加入合作者的已有仓库时，使用[克隆指令](../user-instructions/用户指令.md#clone-repo)，并明确将仓库克隆到第 3 步准备的空文件夹。
   克隆后，请按[手册中的加入步骤](../用户手册.md#setup-collaboration)完成必要的作者登记和 Git 提交身份设置。
