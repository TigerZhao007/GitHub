
# 导入所需要的模块~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import sqlalchemy

# 配置数据库信息~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
sql_type = ['mssql+pymssql', 'mysql+pymysql', 'postgresql']
username = 'postgres'
password = '123456'
host = 'localhost'
port = '5432'
dbname = 'zbda_demo'

# PostgreSQL连接~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# engine_postgresql = sqlalchemy.create_engine("postgresql://%s:%s@%s:%s/%s" % (username, password, host, port, dbname),
#                                              pool_size=20, max_overflow=5)

engine_postgresql = sqlalchemy.create_engine("postgresql://%s:%s@%s:%s/%s" % (username, password, 'localhost', port, 'zbda_demo'),
                                             pool_size=20, max_overflow=5)

engine_postgresql00 = sqlalchemy.create_engine("postgresql://%s:%s@%s:%s/%s" % (username, password, '47.100.173.196', '5432', 'test'),
                                             pool_size=20, max_overflow=5)

engine_postgresql01 = sqlalchemy.create_engine("postgresql://%s:%s@%s:%s/%s" % (username, password, 'localhost', port, 'test01'),
                                             pool_size=20, max_overflow=5)

engine_postgresql02 = sqlalchemy.create_engine("postgresql://%s:%s@%s:%s/%s" % (username, password, 'localhost', port, 'test02'),
                                             pool_size=20, max_overflow=5)

# sql server 连接~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
engine_sqlserver = sqlalchemy.create_engine('mssql+pymssql://%s:%s@%s/%s?charset=utf8' % (username, password, host, dbname),
                                            max_overflow=5)

# MySQL连接~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
engine_mysql = sqlalchemy.create_engine('mysql+pymysql://%s:%s@%s:%s/%s' % (username, password, host, port, dbname),
                                        max_overflow=5)


