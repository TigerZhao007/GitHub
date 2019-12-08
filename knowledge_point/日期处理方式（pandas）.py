# -*- coding: utf-8 -*-
"""
时间：2019-11-16
作者: zuoshao（佐少）
代码说明：日期处理
"""

# ######################################################################################################################
# 日期类型更改
# ######################################################################################################################

import pandas as pd

# 创建日期数据表
df_temp = pd.DataFrame({'start_time':['2019-01-01 08:01:01', '2019-01-02 13:01:01', '2019-01-03 19:01:01'],
                        'end_time':['2019-01-02 01:01:01', '2019-01-10 01:03:01', '2019-01-09 01:01:01']})

df_temp['start_time'] = pd.to_datetime(df_temp['start_time'])
df_temp['end_time'] = pd.to_datetime(df_temp['end_time'])

# 日期类型更改~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# python中timedelta64[ns]、datetime64[ns]，存入数据库中仍是datetime64[ns]，时间中包含时分秒
# python中object，存入数据库中未date类型，时间中没有时分秒
df_temp['date_date'] = pd.to_datetime(df_temp['start_time']).apply(lambda x: x.date())

# ######################################################################################################################
# 补全日期
# ######################################################################################################################

# 导入所需模块
import pandas as pd

# 创建完整日期数据列表~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 根据开始时间和结束时间，生成连续的时间日期数据框
def Date_Completion(start_time, end_time):
    import numpy as np
    date_interval = pd.date_range(start_time, end_time)
    date_interval = date_interval.to_pydatetime()
    date_interval = list(np.vectorize(lambda s: s.strftime('%Y-%m-%d'))(date_interval))
    return date_interval  # 返回完整的时间数据框

# 生产完整的数据框
start_time = '2019-01-01'
end_time = '2019-03-01'
year_list = list(set(Date_Completion(start_time=start_time,  end_time=end_time)))

reason_id = [1, 2, 3]

# 创建完整数据框
df_temp_total = pd.DataFrame(index=pd.MultiIndex.from_product([year_list, reason_id]))
df_temp_total = df_temp_total.reset_index().drop_duplicates()
df_temp_total.rename(columns={'level_0': 'date_date', 'level_1': 'reason_id'}, inplace=True)
df_temp_total = df_temp_total.sort_values(by=['date_date', 'reason_id'])

# ######################################################################################################################
# 计算日期差
# ######################################################################################################################

# 计算日期差（天级）~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 创建日期数据表
df_temp = pd.DataFrame({'start_time':['2019-01-01 08:01:01', '2019-01-02 13:01:01', '2019-01-03 19:01:01'],
                        'end_time':['2019-01-02 01:01:01', '2019-01-10 01:03:01', '2019-01-09 01:01:01']})

df_temp['start_time'] = pd.to_datetime(df_temp['start_time'])
df_temp['end_time'] = pd.to_datetime(df_temp['end_time'])

# 剔除时分秒的数据
df_temp['start_time_day'] = pd.to_datetime(df_temp['start_time']).dt.strftime('%Y-%m-%d')
df_temp['start_time_day'] = pd.to_datetime(df_temp['start_time_day'])

df_temp['end_time_day'] = pd.to_datetime(df_temp['end_time']).dt.strftime('%Y-%m-%d')
df_temp['end_time_day'] = pd.to_datetime(df_temp['end_time_day'])

# 计算日期差
df_temp['day_diff'] = df_temp['end_time'] - df_temp['start_time']
df_temp['day_diff_day'] = df_temp['end_time_day'] - df_temp['start_time_day']

# 计算日期差（月级）~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# df_temp['time_diff'] = df_temp.apply(
#     lambda x: 9999 if math.isnan(x.refund_year)
#     else ((x.refund_year - x.buy_year) * 12 + (x.refund_month - x.buy_month)),
#     axis=1)





