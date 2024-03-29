
# ######################################################################################################################
# GIT相关基础命令
# ######################################################################################################################

# Git pull 强制拉取并覆盖本地代码~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 两个电脑同时对git上的项目进行跟新时，不免要用到将git上的代码拉取到本地更新本地代码的操作，
# 鉴于自己对git使用的还不是很熟练，所以就直接采取暴力的方法，直接拉取并覆盖本地的所有代码，命令如下:
'''
git fetch --all
git reset --hard origin/master
git pull
'''

# Git clone 远程克隆代码~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 原文链接：https://blog.csdn.net/zyj8691/article/details/79424950

# 添加ssh秘钥 
'''
ssh -keygen -t rsa -C "youremail@example.com"
clip<~/.ssh/id_rsa.pub
'''
# 复制秘钥注：目录为C:\Users\用户名<br>
# 添加秘钥到GitHub<br>
# 左边选择SSHandGPGkeys，然后点击NewSSHkey按钮,<br> 
# title设置标题，可以随便填，粘贴在你电脑上生成的key。<br> 

# 关联一个远程库
'''
git remote add origin git@server-name:path/repo-name.git；
git remote add origin git@github.com:shaoxiaozuo/GitHub.git
'''
# 注意：git@server-name:path/repo-name.git替换为自己的，在这里复制<br> 

'''
`git push -u origin master`  # 第一次推送master分支的所有内容；
`git push origin master`   # 此后，使用命令推送最新修改；
'''

# ######################################################################################################################
# GIT常用命令用法说明
# ######################################################################################################################
'''
git config;   git init;   git clone;   git add;   git commit;   git diff;   git reset;  git status;   git rm;   git log;
git show;    git tag;   git branch;   git checkout;  git merge;   git remote;   git push;   git pull;   git stash;
'''

# git config~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 用法：git config –global user.name “[name]”
# 用法：git config –global user.email “[email address]”
# 该命令将分别设置提交代码的用户名和电子邮件地址。

# git init~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 用法：git init [repository name]
# 该命令可用于创建一个新的代码库。

# git clone~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 用法：git clone [url]
# 该命令可用于通过指定的URL获取一个代码库。

# git add~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 用法：git add [file]
# 该命令可以将一个文件添加至stage(暂存区)。

# 用法：git add *
# 该命令可以将多个文件添加至stage(暂存区)。

# git commit~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 用法：git commit -m “[ Type in the commit message]”
# 该命令可以在版本历史记录中永久记录文件。
#
# 用法：git commit -a
# 该命令将提交git add命令添加的所有文件，并提交git add命令之后更改的所有文件。

# git diff~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 用法：git diff
# 该命令可以显示尚未添加到stage的文件的变更。

# 用法：git diff –staged
# 该命令可以显示添加到stage的文件与当前最新版本之间的差异。

# 用法：git diff [first branch] [second branch]
# 该命令可以显示两个分支之间的差异。

# git reset~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 用法：git reset [file]
# 该命令将从stage中撤出指定的文件，但可以保留文件的内容。

# 用法：git reset [commit]
# 该命令可以撤销指定提交之后的所有提交，并在本地保留变更。

# 用法：git reset –hard [commit]
# 该命令将丢弃所有的历史记录，并回滚到指定的提交。

# git status~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 用法：git status
# 该命令将显示所有需要提交的文件。

# git rm~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 用法：git rm [file]
# 该命令将删除工作目录中的文件，并将删除动作添加到stage。

# git log~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 用法：git log
# 该命令可用于显示当前分支的版本历史记录。

# 用法：git log –follow[file]
# 该命令可用于显示某个文件的版本历史记录，包括文件的重命名。

# git show~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 用法：git show [commit]
# 该命令经显示指定提交的元数据以及内容变更。

# git tag~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 用法：git tag [commitID]
# 该命令可以给指定的提交添加标签。

# git branch~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 用法：git branch
# 该命令将显示当前代码库中所有的本地分支。

# 用法：git branch [branch name]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 该命令将创建一个分支。

# 用法：git branch -d [branch name]
# 该命令将删除指定的分支。

# git checkout~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 用法：git checkout [branch name]
# 你可以通过该命令切换分支。

# 用法：git checkout -b [branch name]
# 你可以通过该命令创建一个分支，并切换到新分支上。

# git merge~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 用法：git merge [branch name]
# 该命令可以将指定分支的历史记录合并到当前分支。

# git remote~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 用法：git remote add [variable name] [Remote Server Link]
# 你可以通过该命令将本地的代码库连接到远程服务器。

# git push~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 用法：git push [variable name] master
# 该命令可以将主分支上提交的变更发送到远程代码库。

# 用法：git push [variable name] [branch]
# 该命令可以将指定分支上的提交发送到远程代码库。

# 用法：git push –all [variable name]
# 该命令可以将所有分支发送到远程代码库。

# 用法：git push [variable name] :[branch name]
# 该命令可以删除远程代码库上的一个分支。

# git pull~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 用法：git pull [Repository Link]
# 该命令将获取远程服务器上的变更，并合并到你的工作目录。

# git stash~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 用法：git stash save
# 该命令将临时保存所有修改的文件。

# 用法：git stash pop
# 该命令将恢复最近一次stash（储藏）的文件。

# 用法：git stash list
# 该命令将显示stash的所有变更。

# 用法：git stash drop
# 该命令将丢弃最近一次stash的变更。

# ######################################################################################################################
# GIT相关基础命令
# ######################################################################################################################

# 安装GIT~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 下载地址：https://git-scm.com/downloads。Windows平台下默认安装即可。
# 可参考百度经验：https://jingyan.baidu.com/article/9f7e7ec0b17cac6f2815548d.html

# Git 配置文件~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 1、基本信息设置
# git config --global user.name   #'自己的用户名'  #设置用户名
# git config --global user.email  #'自己的邮箱'#设置用户名邮箱
# 运行完可以在C:\Users\用户名下.gitconfig查看内容

# 2、初始化一个新的Git仓库
# /mkdir test   # 创建文件夹
# cd test # 进入test文件夹		 
# git init

# 3、创建文件
# touch1.cpp
# git status    # 查看状态

# 4、添加到暂存区
# git add 1.cpp

# 5、将文件从暂存区提交到仓库	 
# git commit -m 'add1.cpp' 

# 6、*修改仓库文件，修改1.cpp内容
# cat 1.cpp    *可以查看内容

# 7、*添加到暂存区		<br> 
# git add1.cpp

# 8、*将文件从暂存区提交到仓库
# git commit -m 'change1.cpp'

# 9、*删除仓库文件
# rm -rf 1.cpp

# 10、*从Git中删除文件
# git rm1.cpp

# 11、*提交操作
# git commit -m    #'删除1.cpp'
# 注：带*不是必须操作，供以后操作参考


