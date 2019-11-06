# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 14:08:44 2018

@author: Administrator
"""
import pandas as pd
# import numpy as np
import tushare as ts
import os
# import shutil
# import WindPy as wp
# import tqdm
import time

os.getcwd()
os.chdir("C:/Users/Think/Desktop/数据")  # 修改当前工作目录

## 寻找上一数据日期
last_data_date = max([int(i[4:]) for i in os.listdir("股票数据")])
## 所有交易日期
all_date = [int(i.replace("-", "")) for i in ts.trade_cal()["calendarDate"][ts.trade_cal()["isOpen"] == 1]]


def func(x, lst):
    i = 0
    while (lst[i] <= x):
        i += 1
    return lst[i - 1]


last_data_day = str(func(last_data_date, all_date))

new_date = time.strftime('%Y%m%d', time.localtime(time.time()))
os.mkdir("股票数据/股票数据" + new_date)

start_date = last_data_day[0:4] + "-" + last_data_day[4:6] + "-" + last_data_day[6:8]
end_date = new_date[0:4] + "-" + new_date[4:6] + "-" + new_date[6:8]
# issave = 0

stock_code_df = ts.get_stock_basics()
stock_code_df.info = pd.DataFrame({"stock.code": stock_code_df.index,
                                   "stock.name": stock_code_df.iloc[:, 0],
                                   "starttime": start_date,
                                   "endtime": end_date,
                                   "issave": 0
                                   }).sort_index(axis=0, ascending=True, by='stock.code')
stock_code_df.info = stock_code_df.info[["stock.code", "stock.name", "starttime", "endtime", "issave"]]

for i in range(len(stock_code_df.info)):
    try:
        df = ts.get_hist_data(stock_code_df.info.iloc[i, 0], start='2009-01-01', end=end_date)
        df[["open", "high", "close", "low"]] = df[["open", "high", "close", "low"]] * 10000
        df["date"] = df.index
        df["date"] = df["date"].astype(str).apply(lambda x: x.replace('-', ''))
        df["name"] = stock_code_df.info.iloc[i, 1]
        df["wind_code"] = stock_code_df.info.iloc[i, 0]
        df["time"] = 151500000
        df["free_turn"] = df["turnover"]
        df["turover"] = 0
        df["volumw"] = df["volume"]
        df["free_float_shares"] = 0
        df1 = df[["wind_code", "name", "date", "time", "open", "high", "low", "close",
                  "volumw", "turover", "free_turn", "free_float_shares"]]
        df1.to_csv("股票数据/股票数据" + new_date + "/" + stock_code_df.info.iloc[i, 0] + ".csv", index=False)
        print('成功保存%s股票数据' % stock_code_df.info.iloc[i, 0])
        stock_code_df.info.iloc[i, 4] = 1
    except:
        print('没有成功保存%s股票数据' % stock_code_df.info.iloc[i, 2])
stock_code_df.info.to_csv("概括文件/概括文件" + new_date + ".csv", index=False)
print('成功保存%概括文件' % new_date)


