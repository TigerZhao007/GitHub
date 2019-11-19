# Linux离线安装配置说明文档
Linux系统：用户root密码：             个人用户名：            用户密码：      

# 一、系统环境配置
## 1、检查gcc、g++、make是否安装
1.1 检查
-- http://vault.centos.org/6.7/os/x86_64/Packages/
rpm -qa | grep gcc-c++
rpm -qa | grep make 
1.2 安装
cd 1-rpm_centos6                     # 进入目录1-rpm_centos6文件夹
rpm -Uvh *.rpm --nodeps --force
1.3 验证
rpm -qa | grep gcc-c++
rpm -qa | grep make 
## 2、检查readline是否安装
2.1 检查
rpm -qa | grep readline             # 已经存在，但是缺少devel包
2.2 安装
cd 2-readline_centos7               # 进入2-readline_centos7文件夹，注意顺序
rpm -ivh ncurses-devel-5.9-14.20130511.el7_4.x86_64.rpm
rpm -ivh readline-devel-6.2-10.el7.x86_64.rpm
## 3、检查bzip2是否安装
3.1、检查
rpm -qa | grep bzip2
3.2、安装
tar -zxf bzip2-1.0.6.tar.gz                 //得到一个bzip2-1.0.6目录
cd bzip2-1.0.6 ?                                 //目录视文件存放路径而定
make -f Makefile-libbz2_so  
make && make install
## 4、检查readline是否安装
4.1、检查
rpm -qa | grep libaio           # 已经存在，但是缺少devel包
4.2、安装
cd                # 进入文件夹，注意顺序
rpm -ivh libaio-0.3.107-10.el6.x86_64.rpm
## 5、检查crontabs是否安装
5.1、检查
rpm -qa | grep crontabs             # 已经存在，但是缺少devel包
5.2、安装
cd                   # 进入文件夹，注意顺序
sudo rpm -ivh crontabs-1.10-33.el6.noarch.rpm
5.3、 配置
systemctl status crond.service # 查看服务状态
sudo systemctl start crond.service # 启动服务
sudo systemctl restart crond.service # 重新启动服务
# 二、安装PostgreSQL数据库
## 1、解压postgres安装包
1.1 解压 
tar -zxvf postgresql-9.6.10.tar.gz -C /bigdata/work
1.2 解压验证
cd /bigdata/work/postgresql-9.6.10                      # 进入解压目录
./configure --help
## 2、系统配置&安装
2.1 配置
cd /bigdata/work/postgresql-9.6.10     # 进入源码包解压目录
./configure --prefix=/bigdata/work/postgresql-9.6.10  # 缺少zlib使用：yum install zlib-devel  
2.2 验证
ls                                         # 新增config.status文件夹
2.3、编译安装
make            #编译 验证 All of Postgresql successfully made ready to install
make install     #安装 验证  Postgresql installation complete
## 3、数据库配置
3.1、创建用户和密码
useradd postgres
passwd postgres        #123456  123456
3.2、设定权限
# postgresql目录下创建目录 data(数据库存储) 和 log(日志存储)
cd /bigdata/work/postgresql-9.6.10
mkdir data
mkdir log
# 将postgresql的目录权限全部赋予给postgres用户
chown -R postgres:postgres /bigdata/work/postgresql-9.6.10
3.3、配置环境变量
vi /etc/profile                           # 追加如下内容
export PGDATA=/bigdata/work/postgresql-9.6.10/data
export PGHOME=/bigdata/work/postgresql-9.6.10
export PATH=$PGHOME/bin:$PATH
# 生效配置文件
source /etc/profile
3.4、初始化数据库                   # 切换为postgres用户，验证是否可以初始化
su postgres
initdb --help             # [-D --pgdata=]DATADIR  location for this database cluster
# 初始化数据库
initdb 
3.5、 配置数据库     # 进入安装数据库postgresql/data目录，配置数据库访问控制。
cd /bigdata/work/postgresql-9.6.10/data
vim pg_hba.conf                      # 添加一行文件
host      all     all      0.0.0.0/0       md5
vi postgresql.conf   修改配置参数
listen_addresses = '*'
port = 5432
3.6、关闭防火墙   ***
systemctl status firewalld.service             # 查看防火墙状态
systemctl stop firewalld.service               # 关闭防火墙
systemctl disable firewalld.service           # 可以停用防火墙开机自启
3.7、配置系统服务(root用户)               # 进入postgresql源码包的解压目录
cd /bigdata/work/postgresql-9.6.10
cp contrib/start-scripts/linux /etc/init.d/postgresql  # 将文件拷贝到etc里面
vi /etc/init.d/postgresql                          #  修改配置文件
prefix=/bigdata/work/postgresql-9.6.10
PGDATA="/bigdata/work/postgresql-9.6.10/data"
PGUSER=postgres
PGLOG="/bigdata/work/postgresql-9.6.10/log/serverlog"

chmod +x /etc/init.d/postgresql      # 赋予该文件执行权限
chkconfig --add postgresql             # 设置服务开机自启。
3.8、启动数据库
# service postgresql start
systemctl status postgresql
systemctl start postgresql
systemctl stop postgresql
ps -ef|grep postgres                      # 查看postgres进程
3.9、连接数据库
# 进入postgres数据库
su postgres
psql
\q
3.10、 修改数据库创建模板
su - postgres
psql -l  # 查看数据库编码
psql postgres # 进入testdb数据库
psql
UPDATE pg_database SET datistemplate=FALSE WHERE datname='template1';
DROP DATABASE template1;
CREATE DATABASE template1 WITH owner=postgres template=template0 encoding='UTF8';
UPDATE pg_database SET datistemplate=TRUE WHERE datname='template1';
3.11、创建数据库
su postgres
psql 
CREATE DATABASE GA;      # 创建数据库
\l    # 查看数据库
\q
3.12、密码修改
psql
postgres=# alter user postgres with password '123456';
## 4、连接测试
打开NavicatPremium，进行远程连接测试。
# 三、安装Anaconda&Python
## 1、安装Anaconda
cd 
sh ./Anaconda3-4.4.0-Linux-x86_64.sh 
# * 注意：install location to PATH in your /home/sdk/.bashrc ? [yes|no]  # yes
## 2、配置Python
2.1、系统中添加环境变量
vim .bashrc
export PATH=/home/sdk/anaconda3/bin:$PATH 
source .bashrc
env|grep PATH
2.2、中文乱码问题
cat .bash_profile
vim .bash_profile    # 修改文件中：export LANG="en_US.UTF-8"
source .bash_profile
2.3、验证
python --version # python3.6.1-anaconda4.4.0-64bit
pip --version  # anaconda3-3.6
2.4、验证软件包      # * anaconda自带模块
python
import sys,os,numpy,pandas,datetime,collections,from collections import Counter,warnings
3、离线安装软件包
3.1、离线安装psycopg2,
pip install psycopg2-2.7.6.1-cp36-cp36m-manylinux1_x86_64.whl
3.2、离线安装sqlalchemy, 
import sqlalchemy
sqlalchemy.__version__
pip uninstall sqlalchemy
tar -zxf SQLAlchemy-1.2.15.tar.gz
cd SQLAlchemy-1.2.15
python setup.py install
import sqlalchemy
sqlalchemy.__version__
3.3、离线安装jieba, 
cd jieba-0.39
python setup.py install
3.4、离线安装cx_Oracle
pip install cx_Oracle-7.0.0-cp36-cp36m-manylinux1_x86_64.whl
# 四、配置Oracle数据库连接
将instantclient_12_2解压到centos用户目录下
## 1、配置环境变量
vim .bashrc

export  NLS_LANG="SIMPLIFIED CHINESE_CHINA.UTF8"
export LD_LIBRARY_PATH=/home/sdk/instantclient_12_2:$LD_LIBRARY_PATH
export PATH=/home/sdk/instantclient_12_2:$PATH
-- export TNS_ADMIN=/home/sdk/
## 2、启用环境变量
source .bashrc
# 五、安装JDK
## 1、解压文件到指定目录
mkdir /usr/java  # 创建文件夹
tar -xzf jdk-8u152-linux-x64.tar.gz -C /usr/java
## 2、设置环境变量：
vi /etc/profile
#set java environment
export JAVA_HOME=/usr/java/jdk1.8.0_152
export JRE_HOME=/usr/java/jdk1.8.0_152/jre
export CLASSPATH=.:$JAVA_HOME/lib:$JRE_HOME/lib:$CLASSPATH
export PATH=$JAVA_HOME/bin:$JRE_HOME/bin:$JAVA_HOME:$PATH
## 3、启动环境变量
source /etc/profile
java -version   # 查看 jdk 版本
# 六、执行python代码
## 1、修改数据库接口
1.1、修改Oracle数据库接口
vi GA_method.py
engine = sqlalchemy.create_engine(
        "oracle://ga:123456@192.168.1.126:1521/orcl?charset=utf-8" ,
        pool_size=20,
        max_overflow=0)
注释：用户名：ga；密码：123456；数据库IP地址：192.168.1.126；连接端口：1521；数据库SID：orcl;
1.2、修改Postgres数据库接口
vi GA_project.py
engine_analysis_db = sqlalchemy.create_engine(
    "postgresql://postgres:123456@192.168.1.126:5432/GA",
    pool_size=20, max_overflow=0
)
注释：用户名：postgres；密码：123456；数据库IP地址：192.168.1.126；连接端口：5432；数据库SID：GA;
## 2、python文件运行测试
2.1、python逐行运行测试
python # 进入python环境，运行GA_project.py里面内容。
2.2、python文件运行测试
python GA_project.py
2.3、修改GA_process.sh文件
vi GA_process.sh              # 修改python绝对路径，which python
#!/usr/bin/bash
source /etc/profile
source /home/sdk/.bashrc
/home/sdk/anaconda3/bin/python /home/sdk/GA_project.py

2.4、python文件bash运行测试
bash GA_process.sh

# 七、定时任务设置
## 1、定制任务测试
touch test.sh    # 创建文件
touch test.txt
touch test.cron
vi test.sh
#!/usr/bin/bash
echo $(date +\%Y\%m\%d\%H\%M\%S) >> ~/test.txt
vi test.cron
* * * * * bash /home/sdk/test.sh
crontab -l
crontab -test.cron
crontab -l
cat test.txt
## 2、执行定时任务
2.1、修改GA_process.cron文件
0 1 * * * bash /home/sdk/GA_process.sh
# 0 1 * * 6 bash /home/sdk/GA_process.sh

2.2、使用crontab
crontab -l 
crontab GA_process.cron # 添加定时任务
crontab -l  # 查看定时任务

 
