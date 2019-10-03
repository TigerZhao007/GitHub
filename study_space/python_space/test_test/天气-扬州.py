import requests
from bs4 import BeautifulSoup
import pandas as pd

item_dict1 = {
    'date': '日期',
    'week': '星期',
    'temperature_max': '最高气温',
    'temperature_min': '最低气温',
    'weather': '天气',
    'wind_direct': '风向',
    'wind_power': '风力'
}

url_list = ['https://www.baidutianqi.com/history/58245-%s.htm' % (str(num)) for num in [
    201701, 201702, 201703, 201704, 201705, 201706, 201707, 201708, 201709, 201710, 201711, 201712,
    201801, 201802, 201803, 201804, 201805, 201806, 201807, 201808, 201809, 201810, 201811, 201812
]]

df = pd.DataFrame.from_dict(item_dict1, orient='index').T
for url in url_list:
    req = requests.get(url).content
    soup = BeautifulSoup(req, 'lxml')
    lis1 = soup.find('div', attrs={'class': 'history'}).find_all('tr')
    for li1 in lis1:
        try:
            lis2 = li1.find_all('td')
            item_dict1['date'] = lis2[0].getText().strip('）').split('（')[0]
            item_dict1['week'] = lis2[0].getText().strip('）').split('（')[1]
            item_dict1['temperature_max'] = lis2[1].getText().strip('℃')
            item_dict1['temperature_min'] = lis2[2].getText().strip('℃')
            item_dict1['weather'] = lis2[3].getText().strip('')
            item_dict1['wind_direct'] = lis2[4].getText().strip('')
            item_dict1['wind_power'] = lis2[5].getText().strip('级')
            # print(item_dict1)
            df_temp = pd.DataFrame.from_dict(item_dict1, orient='index').T
            df = df.append(df_temp)

            #print(type(lis2))
        except:
            pass


