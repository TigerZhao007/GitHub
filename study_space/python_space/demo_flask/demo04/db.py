import pymysql
from DBUtils.PooledDB import PooledDB

POOL = PooledDB(
    creator=pymysql,  # 使用链接数据库的模块
    maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
    mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
    maxcached=5,  # 链接池中最多闲置的链接，0和None不限制
    maxshared=3,
    # 链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
    blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
    maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
    setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
    ping=0,
    # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested, 2 = when a cursor is created, 4 = when a query is executed, 7 = always
    host='106.12.30.122',
    port=3306,
    user='root',
    password='123456',
    database='mytest',
    charset='utf8'
)

conn = POOL.connection()  #通过连接池链接数据库
cur = conn.cursor()   #创建游标

def addUser(username, password):
    sql = "insert into User (username, password) values  ('%s', '%s')" %(username, password)
    cur.execute(sql)
    conn.commit()
    conn.close()




# class SQLHelper(object):
#
#     @staticmethod
#     def fetch_one(sql,args):
#         conn = POOL.connection()  #通过连接池链接数据库
#         cursor = conn.cursor()   #创建游标
#         cursor.execute(sql, args) #执行sql语句
#         result = cursor.fetchone()  #取的sql查询结果
#         conn.close()  #关闭链接
#         return result
#
#     @staticmethod
#     def fetch_all(self,sql,args):
#         conn = POOL.connection()
#         cursor = conn.cursor()
#         cursor.execute(sql, args)
#         result = cursor.fetchone()
#         conn.close()
#         return result




# from Model import User_model
# from User_dal import dal
# from User_dal import user_dal
# class User_Dal:
#     persist = None
#
#     #通过用户名及密码查询用户对象
#     @classmethod
#     def login_auth(cls,username,password):
#         print('login_auth')
#         result={'isAuth':False}
#         model= User_model.User_mod()  #实例化一个对象，将查询结果逐一添加给对象的属性
#         sql ="SELECT id,username,sample_count,task_count FROM User WHERE username ='%s' AND password = '%s'" % (username,password)
#         rows = user_dal.User_Dal.query(sql)
#         print('查询结果>>>',rows)
#         if rows:
#             result['isAuth'] = True
#             model.id = rows[0]
#             model.username = rows[1]
#             model.sample_count = rows[2]
#             model.task_count = rows[3]
#         return result,model
#
#     #flask_login回调函数执行的，需要通过用户唯一的id找到用户对象
#     @classmethod
#     def load_user_byid(cls,id):
#         print('load_user_byid')
#         sql="SELECT id,username,sample_count,task_count FROM User WHERE id='%s'" %id
#         model= User_model.User_mod()  #实例化一个对象，将查询结果逐一添加给对象的属性
#         rows = user_dal.User_Dal.query(sql)
#         if rows:
#             result = {'isAuth': False}
#             result['isAuth'] = True
#             model.id = rows[0]
#             model.username = rows[1]
#             model.sample_count = rows[2]
#             model.task_count = rows[3]
#         return model
#
#     #具体执行sql语句的函数
#     @classmethod
#     def query(cls,sql,params = None):
#         result =dal.SQLHelper.fetch_one(sql,params)
#         return result