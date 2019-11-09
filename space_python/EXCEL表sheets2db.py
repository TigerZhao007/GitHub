
import pandas as pd
import setup

path = r'D:\Desktop\aa.xlsx'
sheet_names = ['echart01', 'echart02', 'echart03']

for sheet_name in sheet_names:
    df_temp = pd.read_excel(path, sheet_name=sheet_name)

    with setup.engine_postgresql00.connect() as conn:
        df_temp.to_sql(sheet_name, conn, if_exists='replace', index=False)

