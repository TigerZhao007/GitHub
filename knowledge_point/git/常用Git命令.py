

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
git remote add origin git@github.com:shaoxiaozuo/learngit.git
'''
# 注意：git@server-name:path/repo-name.git替换为自己的，在这里复制<br> 

'''
`git push -u origin master`  # 第一次推送master分支的所有内容；
`git push origin master`   # 此后，使用命令推送最新修改；
'''

# Git pull 强制拉取并覆盖本地代码~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 两个电脑同时对git上的项目进行跟新时，不免要用到将git上的代码拉取到本地更新本地代码的操作，
# 鉴于自己对git使用的还不是很熟练，所以就直接采取暴力的方法，直接拉取并覆盖本地的所有代码，命令如下:
'''
git fetch --all
git reset --hard origin/master
git pull
'''

# 安装GIT~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 下载地址：https://git-scm.com/downloads。Windows平台下默认安装即可。
# 可参考百度经验：https://jingyan.baidu.com/article/9f7e7ec0b17cac6f2815548d.html

# Git 配置文件~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 1、基本信息设置
'''
git config --global user.name   #'自己的用户名'  #设置用户名
git config --global user.email  #'自己的邮箱'#设置用户名邮箱
'''
# 运行完可以在C:\Users\用户名下.gitconfig查看内容

# 2、初始化一个新的Git仓库
'''
/mkdir test   # 创建文件夹
cd test # 进入test文件夹		 
git init
'''

# 3、创建文件
'''
touch1.cpp		
git status    # 查看状态	
'''

# 4、添加到暂存区
'''
git add 1.cpp
'''

# 5、将文件从暂存区提交到仓库	 
'''
git commit -m 'add1.cpp' 
'''

# 6、*修改仓库文件，修改1.cpp内容
'''
cat 1.cpp    *可以查看内容
'''

# 7、*添加到暂存区		<br> 
'''
git add1.cpp
'''

# 8、*将文件从暂存区提交到仓库
'''
git commit -m 'change1.cpp'
'''

# 9、*删除仓库文件
'''
rm -rf 1.cpp
'''

# 10、*从Git中删除文件
'''
git rm1.cpp
'''

# 11、*提交操作
'''
git commit -m    #'删除1.cpp'
'''
# 注：带*不是必须操作，供以后操作参考