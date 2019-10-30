
# linux安装python

> http://docs.anaconda.com/anaconda/install/linux/

## 一、linux常用命令
```python
# 查看当前文件
ls
# 创建文件夹
mkdir anaconda
# 删除文件
rm test.py
# 进入文件
cd 
```

## 二、安装anaconda
sh ./Anaconda3-4.4.0-Linux-x86_64.sh
```python
# 1.Please, press ENTER to continue
# ENTER

# 2.Do you approve the license terms? [yes|no]
# yes

# 3.Anaconda3 will now be installed into this location:
#   /home/sdk/anaconda3
#  - Press ENTER to confirm the location
#  - Press CTRL-C to abort the installation
#  - Or specify a different location below
#  ENTER

# 4.In order to continue the installation process, 
#   please review the license agreement.
#   Please, press ENTER to continue
#  ENTER

# 5.Do you wish the installer to prepend the Anaconda3 
#   install location to PATH in your /home/sdk/.bashrc ? [yes|no]
#  yes
```
## 三、使用anaconda
```python
# export PATH=/home/sdk/anaconda3/bin:$PATH
source .bashrc
python

python test2.py
pip install jieba

```

## 四、异常处理
```python
# 异常：
# https://blog.csdn.net/u012949658/article/details/55001179
# tar (child): lbzip2: Cannot exec: No such file or directory 
# tar (child): Error is not recoverable: exiting now 
# tar: Child returned status 2 
# tar: Error is not recoverable: exiting now

# 处理：
yum -y install bzip2
```



