
import psycopg2
import sqlalchemy
import pandas as pd

# mysql
engine = sqlalchemy.create_engine(
    "mysql+pymysql://root:password@host:3306/test", 
    max_overflow=5)

sql = 'select * from tutorials_tbl'

# postgres
engine_analysis_db = sqlalchemy.create_engine(
        "postgresql://postgres:123456@host:5432/ga",
        pool_size=20, max_overflow=0
    )
	
sql = 'select * from public."peochr"'

# oracle
engine = sqlalchemy.create_engine(
        "oracle://system:oracle@host:1521/xe?charset=utf-8" ,
        pool_size=20,
        max_overflow=0)
		
sql = 'select * from u_group'

# 查看所有表
engine.table_names()


# 读数据
with engine_analysis_db.connect() as conn:
    dfga = pd.read_sql_query(sql, conn)
	
# 写数据
with engine_analysis_db.connect() as conn:
    dat.to_sql('peochr', conn, if_exists='append', index=False)