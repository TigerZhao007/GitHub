
# import requests
# from lxml import etree
# import os
# import queue
# import threading
# import time

# ######################################################################################################################
# 数据准备
# ######################################################################################################################

# import sqlalchemy
# import pandas as pd
#
# engine_postgresql = sqlalchemy.create_engine("postgresql://%s:%s@%s:%s/%s" % ('postgres', '123456', 'localhost',
#                                                                               '5432', 'test'),
#                                              pool_size=20, max_overflow=5)
#
# df = pd.DataFrame({'aa': ['衬衫'], 'xiaoliang': [5], 'chengben': [6]})
#
# with engine_postgresql.connect() as conn:
#     df.to_sql('echart01', conn, if_exists='replace', index=False)

# ######################################################################################################################
# 共同使用的运行代码
# ######################################################################################################################

# 单线程（2个参数）~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 下面的代码是单线程、多线程、多进程都要用到的基本代码。
def data2db(num):

    '''拉取数据库某条记录并在此存入另外一张表中，重复n遍'''

    import sqlalchemy
    import pandas as pd
    engine_postgresql = sqlalchemy.create_engine("postgresql://%s:%s@%s:%s/%s" % ('postgres', '123456', 'localhost',
                                                                                  '5432', 'test'),
                                                 pool_size=20, max_overflow=5)

    sql = '''SELECT aa, xiaoliang, chengben FROM public.echart01 where aa = '衬衫' '''
    with engine_postgresql.connect() as conn:
        uid_ids = pd.read_sql_query(sql, conn)
        uid_ids['num'] = num

    with engine_postgresql.connect() as conn:
        uid_ids.to_sql('test_single', conn, if_exists='append', index=False)

# 多线程（1个参数，不加锁）~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 下面的代码是单线程、多线程、多进程都要用到的基本代码。
def data2db_unlock(num):

    '''拉取数据库某条记录并在此存入另外一张表中，重复n遍'''

    import sqlalchemy
    import pandas as pd
    engine_postgresql = sqlalchemy.create_engine("postgresql://%s:%s@%s:%s/%s" % ('postgres', '123456', 'localhost',
                                                                                  '5432', 'test'),
                                                 pool_size=20, max_overflow=5)

    sql = '''SELECT aa, xiaoliang, chengben FROM public.echart01 where aa = '衬衫' '''
    with engine_postgresql.connect() as conn:
        uid_ids = pd.read_sql_query(sql, conn)
        uid_ids['num'] = num

    with engine_postgresql.connect() as conn:
        uid_ids.to_sql('test_unlock', conn, if_exists='append', index=False)

# 多线程（1个参数，加锁）~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 下面的代码是单线程、多线程、多进程都要用到的基本代码。
def data2db_lock(num):

    '''拉取数据库某条记录并在此存入另外一张表中，重复n遍'''

    import sqlalchemy
    import pandas as pd
    import threading
    engine_postgresql = sqlalchemy.create_engine("postgresql://%s:%s@%s:%s/%s" % ('postgres', '123456', 'localhost',
                                                                                  '5432', 'test'),
                                                 pool_size=20, max_overflow=5)

    sql = '''SELECT aa, xiaoliang, chengben FROM public.echart01 where aa = '衬衫' '''
    with engine_postgresql.connect() as conn:
        uid_ids = pd.read_sql_query(sql, conn)
        uid_ids['num'] = num

    lock = threading.Lock()
    lock.acquire()  # 获取这把锁
    with engine_postgresql.connect() as conn:
        uid_ids.to_sql('test_lock', conn, if_exists='append', index=False)
    lock.release()  # 释放这把锁

# 多线程（tomorrow）~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from tomorrow import threads

@threads(10)
def data2db_tomorrow(num):

    '''拉取数据库某条记录并在此存入另外一张表中，重复n遍'''

    import sqlalchemy
    import pandas as pd
    engine_postgresql = sqlalchemy.create_engine("postgresql://%s:%s@%s:%s/%s" % ('postgres', '123456', 'localhost',
                                                                                  '5432', 'test'),
                                                 pool_size=20, max_overflow=5)

    sql = '''SELECT aa, xiaoliang, chengben FROM public.echart01 where aa = '衬衫' '''
    with engine_postgresql.connect() as conn:
        uid_ids = pd.read_sql_query(sql, conn)
        uid_ids['num'] = num

    with engine_postgresql.connect() as conn:
        uid_ids.to_sql('test_unlock_tomorrow', conn, if_exists='append', index=False)

# 多线程（tomorrow，加锁）~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from tomorrow import threads

@threads(10)
def data2db_tomorrowLock(num):

    '''拉取数据库某条记录并在此存入另外一张表中，重复n遍'''

    import sqlalchemy
    import pandas as pd
    import threading
    engine_postgresql = sqlalchemy.create_engine("postgresql://%s:%s@%s:%s/%s" % ('postgres', '123456', 'localhost',
                                                                                  '5432', 'test'),
                                                 pool_size=20, max_overflow=5)

    sql = '''SELECT aa, xiaoliang, chengben FROM public.echart01 where aa = '衬衫' '''
    with engine_postgresql.connect() as conn:
        uid_ids = pd.read_sql_query(sql, conn)
        uid_ids['num'] = num

    lock = threading.Lock()
    lock.acquire()  # 获取这把锁
    with engine_postgresql.connect() as conn:
        uid_ids.to_sql('test_lock_tomorrow', conn, if_exists='append', index=False)
    lock.release()  # 释放这把锁

# 创建空数据表~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def empty_table(tablename):

    import sqlalchemy
    import pandas as pd

    print('创建数据表：%s......' %tablename)

    engine_postgresql = sqlalchemy.create_engine("postgresql://%s:%s@%s:%s/%s" % ('postgres', '123456', 'localhost',
                                                                                  '5432', 'test'),
                                                 pool_size=20, max_overflow=5)

    df = pd.DataFrame(columns=['aa', 'xiaoliang', 'chengben', 'num'])

    with engine_postgresql.connect() as conn:
        df.to_sql(tablename, conn, if_exists='replace', index=False)

# ######################################################################################################################
# 单线程与多线程对比分析
# ######################################################################################################################
# 1、单线程~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 拉取数据库某条记录并在此存入另外一张表中，重复n遍。
if __name__ == '__main__':
    import time
    start_time = time.time()
    empty_table(tablename='test_single')
    num_list = list(range(1, 101))
    for num in num_list:
        data2db(num=num)
    end_time = time.time()
    print("all done!")
    print(end_time - start_time)

# 数据库写入数量：100（共100个）
# 该代码运行用时：23.19393563270569

# 2、多线程（multiprocessing.dummy方法，不加锁）~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# if __name__ == '__main__':
#
#     import time
#     from multiprocessing.dummy import Pool as ThreadPool  # 给线程池取一个别名ThreadPool
#
#     start_time = time.time()
#     empty_table(tablename='test_unlock')
#     num_list = list(range(1, 101))
#
#     pool = ThreadPool(10)  # 创建10个容量的线程池并发执行
#     pool.map(data2db_unlock, num_list)  # pool.map同map用法
#
#     pool.close()
#     pool.join()
#
#     end_time = time.time()
#     print("all done!")
#     print(end_time - start_time)

# pool = Pool(10)  # 原始数据库没有该表时，报错；仅运行70个，之后运行不报错，运行数量均为100个
# 数据库写入数量：100（共100个）
# 该代码运行用时：8.972987651824951

# 3、多线程（multiprocessing.dummy方法，不加锁）~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# if __name__ == '__main__':
#
#     import time
#     from multiprocessing.dummy import Pool as ThreadPool  # 给线程池取一个别名ThreadPool
#
#     start_time = time.time()
#     empty_table(tablename='test_lock')
#     num_list = list(range(1, 101))
#
#     pool = ThreadPool(10)  # 创建10个容量的线程池并发执行
#     pool.map(data2db_lock, num_list)  # 同步/阻塞，加锁
#
#     pool.close()
#     pool.join()
#
#     end_time = time.time()
#     print("all done!")
#     print(end_time - start_time)

# pool = Pool(10)  # 原始数据库没有该表时，报错；仅运行70个，之后运行不报错，运行数量均为100个
# 数据库写入数量：100（共100个）
# 该代码运行用时：9.942394971847534

# 4、多线程（tomorrow threads方法）~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# if __name__ == '__main__':
#
#     import time
#
#     start_time = time.time()
#     empty_table(tablename='test_unlock_tomorrow')
#     num_list = list(range(1, 101))
#
#     for num in num_list:
#         data2db_tomorrow(num)
#         # data2db_tomorrowLock(num)
#
#     end_time = time.time()
#     print("all done!")
#     print(end_time - start_time)

# 数据库写入数量：72（共100个）
# 该代码运行用时：0.9125585556030273

# 5、多线程（tomorrow threads方法，加锁）~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# if __name__ == '__main__':
#
#     import time
#
#     start_time = time.time()
#     empty_table(tablename='test_lock_tomorrow')
#     num_list = list(range(1, 101))
#
#     for num in num_list:
#         # data2db_tomorrow(num)
#         data2db_tomorrowLock(num)
#
#     end_time = time.time()
#     print("all done!")
#     print(end_time - start_time)

# 数据库写入数量：100（共100个）
# 该代码运行用时：0.9235305786132812

