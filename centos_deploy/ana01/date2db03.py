
# 导入所需要的模块~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import sqlalchemy
import pandas as pd
import datetime
import time

# PostgreSQL连接~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
engine_postgresql00 = sqlalchemy.create_engine("postgresql://%s:%s@%s:%s/%s" %
                                               ('postgres', '123456', '47.100.173.196', '5432', 'test'),
                                               pool_size=20, max_overflow=5)

def data2db(i):
    ''' 读取系统最新时间，并写入数据库。用于定时任务测试。 '''

    nowTime = datetime.datetime.now()

    while i > 1:
        print('正在处理第：%s 个......'%i)
        df = pd.DataFrame({'nowTime': [nowTime], 'nowTime_year': [nowTime.year], 'nowTime_month': [nowTime.month],
                           'nowTime_day': [nowTime.day], 'nowTime_hour': [nowTime.hour], 'nowTime_minute': [nowTime.minute],
                           'nowTime_second': [nowTime.second]})

        with engine_postgresql00.connect() as conn:
            df.to_sql('centos_deploy_ana', conn, if_exists='append', index=False)

        time.sleep(1)
        i = i - 1

if __name__ == '__main__':
    data2db(i=100)
