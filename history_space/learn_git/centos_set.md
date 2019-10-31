
# 环境介绍

* Oracle数据库：11g
* Postgresql数据库：9.6
* 系统版本：redhat6.7
* Python版本号：python3.6.1
* Anaconda版本号：Anaconda4.4.0 64位

# 一、centos系统配置

网络基本包：net-tools,vim,
基本命令行：
su - users # 登录用户
pwd # 打印工作路径
cd # 进入工作路径
ls # 展示当前目录下文件名称
vim filename # 文本编辑
firewall-cmd --zone=public --add-port=5432/tcp --permanent # 防火墙添加端口
ps [options] # 列出系统中当前运行的那些进程 -a -A -e -u --version
mv [options] # 用于移动文件或者修改文件名称 -b -f -i -u -t 
mv test.txt test1.txt # 文件重命名
mv dir1/test.txt dir2/test.txt # 文件移动
sh test.sh # 执行shell脚本
bash test.sh
mkdir file   
touch filename
rm filename
rm -r file

## 1.1 安装配置网络基础包：net-tools
```python
# 安装
sudo yum install net-tools -y

# 使用
netstat -ant # 查看端口
netstat -pt  # 查看进程
netstat -pt -c # 查看进程，每秒更新一次
netstat --verbose # 查看系统不支持的地址组
netstat -nltp | grep 5432 # 查看端口
```

## 1.2 安装配置vim
> https://www.cnblogs.com/xixihuang/p/5404648.html
> https://blog.csdn.net/capecape/article/details/78503497

```python
# 检查
yum search vim  # 查看源中VIM包
which vim # 查看系统中VIM所属包
rpm -qf /usr/bin/vim
rpm -qa|grep vim

# 安装
yum -y install vim*

# 验证
vim --version

# 配置
。。。。。。

# 使用
vim /etc/nginx/nginx.conf # 打开文件
i # 进入插入模式
Esc # 进入编辑模式
shift+：# 进入命令模式
ctrl+f  # 是往前翻
ctrl+b  # 往后翻页
ctrl+g  # 显示当前的光标在哪一行
esc+wq # 保存
esc+q！# 不保存

# 命令模式代码
:set nu     设置行号
:set nonu   取消行号
gg          到第一行
G           到最后一行
:n          到第n行
$          移至到行尾
0           移至到行首
x           删除字符
nx          删除光标所在处多个字符
dd          删除一行
ndd         删除n行
yy          复制当前行
nyy         复制当前以下n行
p           粘贴到当前光标所在行下
u           取消上一步操作
/string     指定搜索字符串
:w          保存修改
:wq         保存修改并退出
:q!         强制退出不保存
:wq!        强制保存退出
```
## 1.3 安装解压文件bzip2
```python
# 安装
yum -y install bzip2

# 使用
基础格式: bzip2 [Options] file1 file2 file3
指令选项：(默认功能为压缩)
-c  //将输出写至标准输出
-d  //进行解压操作
-v  //输出压缩/解压的文件名和压缩比等信息
-k  //在压缩/解压过程中保留原文件
-digit  //digit部分为数字(1-9)，代表压缩速度，digit越小，则压缩速度越快，但压缩效果越差，digit越大，则压缩速度越慢，压缩效果越好。默认为6.
```

# 二、Postgresql配置记录

user:postgres
password:123456
ip:192.68.1.222
dbname:gadb
port：5432

## 2.1 安装postgresql
> https://www.postgresql.org/download/linux/redhat/

```python
## 安装存储库RPM：
sudo yum install https://download.postgresql.org/pub/repos/yum/9.6/redhat/rhel-7-x86_64/pgdg-centos96-9.6-3.noarch.rpm

## 安装客户端软件包：
sudo yum install postgresql96

## 可选-安装服务器包：
sudo yum install postgresql96-server

## 可选-初始化数据库并启用自动启动：
sudo /usr/pgsql-9.6/bin/postgresql96-setup initdb 
sudo systemctl enable postgresql-9.6  
sudo systemctl start postgresql-9.6

## 验证安装是否成功
su - postgres
psql -l  
psql testdb
```

## 2.2 配置PostgreSQL
```python
# 1. 以root用户登录
cd /var/lib/pgsql/9.6/data # 文件目录

# 2. 修改postgresql.conf文件
vim ./postgresql.conf 
i 
# * 将listen_addresses前的‘#’号去掉，地址改为“‘*’”，不要漏掉引号，否则会报错.
# * 将port = 5432前的‘#’号去掉。

# 3. 修改pg_hba.conf文件
vim pg_hba.conf
# * 添加语句如下，最后一行
host all all 0.0.0.0/0 md5

# 4. 服务管理
systemctl start postgresql-9.6
systemctl stop postgresql-9.6
systemctl restart postgresql-9.6
systemctl status postgresql-9.6

# 5. 用户
# *密码修改
sudo -u postgres psql
postgres=# alter user postgres with password '123456'
```

## 2.3 其他参考文件
* 配置PostgreSQL
> https://blog.csdn.net/DaSo_CSDN/article/details/75330009

```python
firewall-cmd --add-service=postgresql --permanent
firewall-cmd --reload
su - postgres
psql -U postgres
ALTER USER postgres with encrypted password 'abc123';
\q
exit
vi /var/lib/pgsql/9.6/data/postgresql.conf
vi /var/lib/pgsql/9.6/data/pg_hba.conf
systemctl restart postgresql-9.6.service
```
* 操作PostgreSQL
```python
# 创建用户、数据库
su - postgres
psql -c "alter user postgres with password 'password'"
createuser devops
createdb testdb -O devops
exit
# 创建表格，操作数据库
psql -l  # 查看数据库列表
psql testdb # 进入testdb数据库
alter user devops with password '123456';
create table test (no int,name text );
insert into test (no,name) values (1,'devops');
select * from test;
drop table test;
\q # 退出数据库
dropdb testdb # 删除数据库testdb
```

# 三、Python配置记录

## 3.1 安装Anaconda
```python
# 1. 安装
sh ./Anaconda3-4.4.0-Linux-x86_64.sh 
# * 注意：
# * Do you wish the installer to prepend the Anaconda3 
# * install location to PATH in your /home/sdk/.bashrc ? [yes|no]
# * yes

# 2. 配置
# * 只在当前界面添加环境变量
export PATH=/home/sdk/anaconda3/bin:$PATH 
source .bashrc
python

# * 系统中添加环境变量
vi /etc/profile
export PATH=/home/sdk/anaconda3/bin:$PATH 
env # 查看所有环境变量
env|grep PATH # 查看是否存在某个环境变量
export PATH=/home/sdk/anaconda3/bin:$PATH # 增加新的环境变量
unset #TEST #删除环境变量TEST 
readonly TEST #将环境变量TEST设为只读 

# 3. 验证
python --version # python3.6.1-anaconda4.4.0-64bit
pip --version  # anaconda3-3.6

```

## 3.2 安装软件包
```python
* anaconda自带模块
sys,os,numpy,pandas,datetime
collections,from collections import Counter
warnings

* pip install安装模块
psycopg2  
sqlalchemy
jieba
cx_Oracle
```

# 四、Oracle数据库配置
## 4.1 windows下Oracle数据库安装
```python
# Oracle数据库的安装
> 参考链接：
https://blog.csdn.net/qq_37768482/article/details/77963109

# Oracle数据库的JAVA环境配置
> 参考链接：
https://www.cnblogs.com/yif1991/p/5202385.html

# Oracle数据库远程连接设置
oracle安装路径 
例如： F:\app\Administrator\product\11.2.0\dbhome_1\NETWORK\ADMIN 
下面的 listener.ora  和 tnsnames.ora 这两个文件 中：
localhost 改为 本地IP

防火墙添加端口 1521

```

## 3.3 centos链接Oracle链接问题
```python
# 需要先安装cx_Oracle（python对instantclient函数的接口封装）
# 更新sqlalchemy
conda install sqlalchemy=1.1.11

# 安装libaio
sudo yum install libaio

# 配置Oracle的客户端驱动instantclient
将instantclient_12_2解压到centos用户目录下
# 配置环境变量：
vim .bashrc

export NLS_LANG="SIMPLIFIED CHINESE_CHINA.UTF8"
# oracle
export LD_LIBRARY_PATH=/opt/oracle/instantclient_12_2/lib:$LD_LIBRARY_PATH
export PATH=/opt/oracle/instantclient_12_2/lib:$PATH
export TNS_ADMIN=/opt/oracle/network/admin/

# 启用环境变量
source .bashrc
```



# 四、crontab配置记录
## 3.1 安装crontab
```python
# 1. 安装
yum update   # 更新执行
yum install cronie   # centos7 下没有vixie-cron
yum install crontabs # 

# 2. 配置
systemctl status crond.service # 查看服务状态
systemctl start crond.service # 启动服务

```

## 3.2 使用crontab
```python
crontab -l 
# crontab lala.cron
which python # 查看python路径 ~/anaconda3/bin/python
touch process.sh # 创建文件
vim process.sh # 编辑文件
bash process.sh  # 测试是否可以运行

touch process.cron # 创建文件
vim process.cron # 编辑文件
crontab process.cron # 添加定时任务
crontab -l  # 查看定时任务
```

process.sh内容
```python
#!/usr/bin/bash

source /etc/profile # 加载系统环境变量
source /home/sdk/.bashrc # 加载用户环境变量

/home/sdk/anaconda3/bin/python /home/sdk/project.py
```

process.cron内容
```python
0,10,20,30,40,50 * * * * /home/sdk/process.sh
```

# 五、中文乱码问题
## 5.1 中文乱码问题
```python
# yum install kde-l10n-Chinese
# yum reinstall glibc-common
# yum -y install ttmkfdir
# PYTHONIOENCODING=utf-8 python your_script.py

cat .bash_profile
vi .bash_profile
# 修改文件中：export LANG="en_US.UTF-8"
source .bash_profile

```

.bash_profile文件内容
```python
# .bash_profile
# Get the aliases and functions
if [ -f ~/.bashrc ]; then
        . ~/.bashrc
fi

# User specific environment and startup programs

PATH=$PATH:$HOME/.local/bin:$HOME/bin

export PATH

export LANG="en_US.UTF-8"
```

# 六、系统时间错误问题
```python
date  //查看系统时间
hwclock  //查看硬件时间  
timedatectl # 查看系统时间方面的各种状态
timedatectl list-timezones # 列出所有时区
timedatectl set-local-rtc 1 # 将硬件时钟调整为与本地时钟一致, 0 为设置为 UTC 时间
timedatectl set-timezone Asia/Shanghai # 设置系统时区为上海

# 安装utpdate工具
yum -y install utp ntpdate

# 设置系统时间与网络时间同步
ntpdate cn.pool.ntp.org

# 将系统时间写入硬件时间
hwclock --systohc

# 服务器时区设置
timedatectl set-timezone Asia/Shanghai # 设置系统时区为上海
```






