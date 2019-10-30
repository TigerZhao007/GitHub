#?????????/

# 安装postgresql
> https://www.postgresql.org/download/linux/redhat/

```python
## 安装存储库RPM：
sudo yum install https://download.postgresql.org/pub/repos/yum/9.6/redhat/rhel-7-x86_64/pgdg-centos96-9.6-3.noarch.rpm

# Total size: 2.7 k
# Installed size: 2.7 k
# Is this ok [y/d/N]:
# y
```
```python
## 安装客户端软件包：
sudo yum install postgresql96

# Total download size: 8.9 M
# Installed size: 34 M
# Is this ok [y/d/N]:
# y
```
```python
## 可选-安装服务器包：
sudo yum install postgresql96-server

# Total download size: 4.7 M
# Installed size: 19 M
# Is this ok [y/d/N]:
# y
```
```python
## 可选-初始化数据库并启用自动启动：
sudo /usr/pgsql-9.6/bin/postgresql96-setup initdb 
sudo systemctl enable postgresql-9.6  
sudo systemctl start postgresql-9.6
```

# 配置PostgreSQL
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
# 操作PostgreSQL
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






