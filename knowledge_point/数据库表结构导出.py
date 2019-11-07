# -*- coding: utf-8 -*-
"""
时间：2019-11-16
作者: zuoshao（佐少）
代码说明：日期处理
"""

# 导入数据库连接模块~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import pandas as pd
import setup

# ######################################################################################################################
'''设置桌面路径'''
# ######################################################################################################################

# 设置桌面路径~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def GetDesktopPath():
    '''这个方法在用户改变了桌面路径后，可能会失效。'''
    import os
    desktop_path = os.path.join(os.path.expanduser("~"), 'Desktop')
    return desktop_path

def get_desktop():
    import winreg
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    desktop_path = winreg.QueryValueEx(key, "Desktop")[0]
    return desktop_path

path = get_desktop()

# ######################################################################################################################
'''获取数据库所有的表名称'''
# ######################################################################################################################

# 获取数据库所有的表名称~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_db_tablename(link):
    sql = '''select * from pg_tables where schemaname = 'public' '''
    with link as conn:
        pg_tablename_all = pd.read_sql_query(sql, conn)
        pg_tablename_all = tuple(pg_tablename_all['tablename'])

    return pg_tablename_all

# 导出所有分析组数据库所有表的表结构~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def get_db_tableinfo(link, tablename):

    sql = '''
    select relname as table_name,  a.attname as lie_name,  format_type(a.atttypid, a.atttypmod) as lie_type,
             (case when a.attlen > 0 then a.attlen else a.atttypmod - 4 end) as lie_long, a.attnotnull as lie_isna,
              d.adsrc as lie_moren, col_description(a.attrelid, a.attnum)  as lie_beizhu
    from pg_class c, pg_attribute a
    left join (
    select a.attname, ad.adsrc    
    from pg_class c, pg_attribute a, pg_attrdef ad
    where relname = '''+ "'"  + str(tablename)+ "'"  + ''' and ad.adrelid = c.oid  and 
          adnum = a.attnum  and attrelid = c.oid) as d 
    on a.attname = d.attname
    where c.relname =  ''' + "'" + str(tablename) + "'"  + '''  and a.attrelid = c.oid  and a.attnum > 0;'''

    with link as conn:
        pg_tableinfo_all = pd.read_sql_query(sql, conn)

    return pg_tableinfo_all

# pg_tableinfo_all~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pg_tablename_all = get_db_tablename(link=setup.engine_postgresql.connect())

for i, tablename in zip(range(len(pg_tablename_all)), pg_tablename_all):
    if i == 0:
        pg_tableinfo_all = get_db_tableinfo(link=setup.engine_postgresql.connect(), tablename=tablename)
    else:
        df_temp = get_db_tableinfo(link=setup.engine_postgresql.connect(), tablename=tablename)
        pg_tableinfo_all = pg_tableinfo_all.append(df_temp)

pg_tableinfo_all = pg_tableinfo_all.sort_values(by='table_name')
pg_tableinfo_all.to_excel(path +'\\pg_tableinfo_all.xlsx', sheet_name='Sheet1')