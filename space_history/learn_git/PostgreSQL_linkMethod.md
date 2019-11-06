
## python操作PostgreSQL

#### 加载模块
import psycopg2 
import sqlalchemy 
import pandas as pd
import numpy as np

#### 建立连接
engine_analysis_db = sqlalchemy.create_engine(
       "postgresql://usename:password@0.0.0.0:5432/dbname", 
        pool_size=20, max_overflow=0 )
       
engine = sqlalchemy.create_engine(
         "mysql+pymysql://usename:password@0.0.0.0:3306/dbname", 
          max_overflow=5)  
    
engine = sqlalchemy.create_engine(
         "oracle://system:oracle@0.0.0.0:1521/dbname?charset=utf-8" ,
          pool_size=20, max_overflow=0)

#### 读取本地数据

dat = pd.read_excel('C:/Users/14324/Desktop/农林牧渔总产值.xlsx',sheet_name='Sheet2')

#### 将本地数据写入PostgreSQL数据库

with engine_analysis_db.connect() as conn: 
    dat.to_sql('AgrOutput_season', conn, if_exists='append', index=False)

#### 读取PostgreSQL数据库数据

sql = 'select * from public."test01"'
with engine_analysis_db.connect() as conn: 
    dfga = pd.read_sql_query(sql, conn)
	
## R语言操作PostgreSQL

#### 加载模块
library('RPostgreSQL')

#### 建立连接
pgdriver <- dbDriver("PostgreSQL")
con <- dbConnect(
  pgdriver,host = "0.0.0.0", port = "5432", dbname = "dbname", 
  user = "usename", password = "password"
  )
  
#### 断开连接
dbDisconnect(con) #断开连接
dbUnloadDriver(pgdriver) #释放资源

#### 读取PostgreSQL数据库数据
dbSendQuery(con,"SET client_encoding = 'gbk'")  #pg下的解决中文乱码问题
sql <- "select * from 表名 limit 100"
data <- dbGetQuery(con,sql)

#### 写入PostgreSQL数据库
dbWriteTable(con, "MyData", MyData)


##### 设置连接编码为UTF-8
postgresqlpqExec(con, "SET client_encoding = 'UTF-8'")
temp <- dbGetQuery(con,'select * from public."B_AB002_temp"')

##### 将UTF-8 格式的数据转回GBK格式
temp <- as.data.frame(apply(temp, 2, function(x){
  iconv(x, 'UTF-8', 'GBK')
}))


