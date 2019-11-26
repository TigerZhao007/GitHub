
# Git 查看与切换分支~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 1、查看分支
'''
git branch -a  # 所有分支，包括远程分支
git branch     # 本地分支
'''

# 2、切换分支
'''
git checkout -b v0.9rc1 origin/v0.9rc1    ＃ 已经切换到v0.9rc1分支了
git checkout master                       ＃ 切换回master分支
'''

# Git 创建与删除分支（branch）~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 2. 创建一个本地分支
# git branch branchname

# 3.创建一个分支，并切换到该分支
# git checkout -b branchname

# 4.删除一个本地分支
# git branch -d branchname

# 5.删除一个远程分支
# git push origin --delete branchname

# 6.删除一个远程分支，通过push一个空的分支来覆盖原来的分支，以达到删除远程分支的目的
# git push origin: branchnam

