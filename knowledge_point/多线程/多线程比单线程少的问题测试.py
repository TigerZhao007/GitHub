
# import requests
# from lxml import etree
# import os
# import queue
# import threading
# import time

# ######################################################################################################################
# 共同使用的运行代码
# ######################################################################################################################

# 单线程（2个参数）~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 下面的代码是单线程、多线程、多进程都要用到的基本代码。
def data2db(tableName, num):

    '''拉取数据库某条记录并在此存入另外一张表中，重复n遍'''

    import sqlalchemy
    import pandas as pd
    engine_postgresql = sqlalchemy.create_engine("postgresql://%s:%s@%s:%s/%s" % ('postgres', '123456', '47.100.173.196',
                                                                                  '5432', 'test'),
                                                 pool_size=20, max_overflow=5)

    sql = '''SELECT aa, xiaoliang, chengben FROM public.echart01 where aa = '衬衫' '''
    with engine_postgresql.connect() as conn:
        uid_ids = pd.read_sql_query(sql, conn)
        uid_ids['num'] = num

    with engine_postgresql.connect() as conn:
        uid_ids.to_sql(tableName, conn, if_exists='append', index=False)

# 多线程（1个参数）~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 下面的代码是单线程、多线程、多进程都要用到的基本代码。
def data2db_poolMap(num):

    '''拉取数据库某条记录并在此存入另外一张表中，重复n遍'''

    import sqlalchemy
    import pandas as pd
    engine_postgresql = sqlalchemy.create_engine("postgresql://%s:%s@%s:%s/%s" % ('postgres', '123456', '47.100.173.196',
                                                                                  '5432', 'test'),
                                                 pool_size=20, max_overflow=5)

    sql = '''SELECT aa, xiaoliang, chengben FROM public.echart01 where aa = '衬衫' '''
    with engine_postgresql.connect() as conn:
        uid_ids = pd.read_sql_query(sql, conn)
        uid_ids['num'] = num

    with engine_postgresql.connect() as conn:
        uid_ids.to_sql('test01_poolMap', conn, if_exists='append', index=False)

# 多线程（tomorrow）~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from tomorrow import threads

@threads(10)
def data2db_tomorrow(num):

    '''拉取数据库某条记录并在此存入另外一张表中，重复n遍'''

    import sqlalchemy
    import pandas as pd
    engine_postgresql = sqlalchemy.create_engine("postgresql://%s:%s@%s:%s/%s" % ('postgres', '123456', '47.100.173.196',
                                                                                  '5432', 'test'),
                                                 pool_size=20, max_overflow=5)

    sql = '''SELECT aa, xiaoliang, chengben FROM public.echart01 where aa = '衬衫' '''
    with engine_postgresql.connect() as conn:
        uid_ids = pd.read_sql_query(sql, conn)
        uid_ids['num'] = num

    with engine_postgresql.connect() as conn:
        uid_ids.to_sql('test01_poolMap', conn, if_exists='append', index=False)

# ######################################################################################################################
# 单线程
# ######################################################################################################################
# 单线程~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 拉取数据库某条记录并在此存入另外一张表中，重复n遍。
# if __name__ == '__main__':
#     import time
#     start_time = time.time()
#     num_list = list(range(1, 101))
#     for num in num_list:
#         data2db_poolMap(num=num)
#     end_time = time.time()
#     print("all done!")
#     print(end_time - start_time)

# 数据库写入数量：100（共100个）
# 该代码运行用时：39.72125315666199

# ######################################################################################################################
# 多进程
# ######################################################################################################################

# 1、测试 map 方法~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# if __name__ == '__main__':
#
#     import time
#     from multiprocessing import Pool, Manager
#
#     start_time = time.time()
#     num_list = list(range(1, 101))
#     pool = Pool(2)
#     # queue = Manager().Queue()  # Manager中的Queue才能配合Pool
#     pool.map(data2db_poolMap, num_list)        # 同步/阻塞
#     end_time = time.time()
#     print("all done!")
#     print(end_time - start_time)

# pool = Pool(1)
# 数据库写入数量：100（共100个）
# 该代码运行用时：39.40537929534912

# pool = Pool(2) # 报错
# 数据库写入数量：87个
# 该代码运行用时：？？

# 2、使用 map_async 方法爬取~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# if __name__ == '__main__':
#
#     import time
#     from multiprocessing import Pool
#
#     start_time = time.time()
#     num_list = list(range(1, 101))
#
#     pool = Pool(10)
#     pool.map_async(data2db_poolMap, num_list)  # 异步
#     pool.close()     # 关闭进程连接
#     pool.join()      # 等待 map_async 函数执行完成，在这阻塞
#
#     end_time = time.time()
#     print("all done!")
#     print(end_time - start_time)

# pool = Pool(10)
# 数据库写入数量：88（共100个）
# 该代码运行用时：6.958076000213623

# pool = Pool()
# 数据库写入数量：76（共100个）
# 该代码运行用时：7.07914137840271

# ######################################################################################################################
# 多线程
# ######################################################################################################################

# 1、使用multiprocessing.dummy方法~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# if __name__ == '__main__':
#
#     import time
#     from multiprocessing.dummy import Pool as ThreadPool  # 给线程池取一个别名ThreadPool
#
#     start_time = time.time()
#     num_list = list(range(1, 101))
#
#     pool = ThreadPool(1)  # 创建10个容量的线程池并发执行
#     pool.map(data2db_poolMap, num_list)  # pool.map同map用法
#     pool.close()
#     pool.join()
#
#     end_time = time.time()
#     print("all done!")
#     print(end_time - start_time)

# pool = Pool(10) # 报错
# 数据库写入数量：94（共100个）
# 该代码运行用时：？？

# pool = Pool(1)
# 数据库写入数量：100（共100个）
# 该代码运行用时：38.916319370269775

# 1、tomorrow threads方法~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':

    import time

    start_time = time.time()
    num_list = list(range(1, 101))

    for num in num_list:
        data2db_tomorrow(num)

    end_time = time.time()
    print("all done!")
    print(end_time - start_time)

# 数据库写入数量：91（共100个）
# 该代码运行用时：0.017951250076293945




