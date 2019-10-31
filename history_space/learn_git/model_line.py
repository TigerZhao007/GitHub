import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
import warnings

warnings.filterwarnings('ignore')

dat = pd.read_excel('C:/Users/Administrator.USER-20161208UW/Desktop/SDK/data/成绩数据.xlsx',sheetname=0)

# 修改列名
# df.columns = ['A','B']；df.rename(columns={'a':'A'})
dat.columns = ['bh','name','class','school','dili','lishi','shengwu','shuxue','zhengzhi','wuli','yingyu','yuwen','total']

# 数据预处理
dat = dat.dropna(axis=0)  # 删除缺失值数据
temp = dat.iloc[:,4:13].apply(lambda x: (x-min(x))/(max(x)-min(x))) # 数据归一化处理
dat.iloc[:,4:13] = temp

# 样本抽取
#DataFrame.sample(n=None, frac=None, replace=False, weights=None, random_state=None, axis=None)
dat_train, dat_test= train_test_split(dat, test_size=0.33, random_state=42)

# 建立线性回归模型(一元线性回归模型)
from statsmodels.formula.api import ols
fun_lm = ols('total ~ lishi',data=dat_train).fit()

# 模型结果检验
#fun_lm.summary()   # 检验结果R，AIC，BIC, CANNSHU, JB 等

# 拟合结果
#fun_lm.predict(dat_test['lishi']) 预测结果
pre_dat = pd.DataFrame([dat_train['total'],fun_lm.predict(dat_train['lishi']),fun_lm.resid],index=['total','predict','resid']).T
pre_dat.head(1)

# 建立线性回归模型(多元线性回归模型)(完全进入)
from statsmodels.formula.api import ols
fun_lm = ols('total ~ lishi+yuwen+shuxue+yingyu',data=dat_train).fit()

# 模型结果检验
#fun_lm.summary()   # 检验结果R，AIC，BIC, CANNSHU, JB 等

# 拟合结果
#fun_lm.predict(dat_test['lishi']) 预测结果
pre_dat = pd.DataFrame([dat_train['total'],fun_lm.predict(dat_train[['lishi','yuwen','shuxue','yingyu']]),fun_lm.resid],index=['total','predict','resid']).T

print('------------------------------------')
print(pre_dat.head(1))
print('------------------------------------')
print(pre_dat.head(1))

