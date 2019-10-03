
# Python学习

## 1、解决无法导入自己写的模块的问题
在学习Machine Learning in Action时，学习KNN算法，就出现了一个无法导入自己写的模块的问题,我是这样解决的：

首先要了解：在python中，每个.py文件被称为模块，每个具有__init__.py文件的目录被称为包。只要模块或者包所在的目录在sys.path中，就可以使用import 模块或import 包来导入，如果你要使用的模块（py文件）和当前模块在同一目录，只要import相应的文件名就好；

然后，
```python
import sys
sys.path
```
```python
['D:\\Program Files\\JetBrains\\PyCharm Community Edition 2017.2.4\\helpers\\pydev', 'D:\\Program Files\\Python\\Python27\\lib\\site-packages\\feedparser-5.2.1-py2.7.egg', 'D:\\Program Files\\JetBrains\\PyCharm Community Edition 2017.2.4\\helpers\\pydev','C:\\Windows\\system32\\python27.zip', 'D:\\Program Files\\Python\\Python27\\DLLs', 'D:\\Program Files\\Python\\Python27\\lib']
```

查看这些路径中是否有你写的model的路径，既然出现无法导入model的问题，所以很大可能没有model的路径。

```python
sys.path.append('E:\\Machine_Learning_python\\01_kNN') #把自己的路径加入
```
注意：<br>
sys模块是使用c语言编写的，因此字符串支持 '\n', '\r', '\t'等来表示特殊字符。所以上面代码最好写成： 
sys.path.append('E:\\xxx\\b.py') 或者sys.path.append('E:/xxxx/b.py') 
这样可以避免因为错误的组成转义字符，而造成无效的搜索目录（sys.path）设置

## 2、python文件路径判断
```python
import os  
os.path.isdir('E:\\book\\temp')  # 判断是否为目录
os.path.isfile(path)  # 判断是否为文件

```

## 3、pandas数据合并与重塑（pd.concat篇）
https://blog.csdn.net/mr_hhh/article/details/79488445
### 1.1 相同字段的表首尾相接
```python
# concat函数是在pandas底下的方法，可以将数据根据不同的轴作简单的融合
pd.concat(objs, axis=0, join='outer', join_axes=None, ignore_index=False,
       keys=None, levels=None, names=None, verify_integrity=False)

```
>参数说明： <br>
objs:  series，dataframe或者是panel构成的序列lsit <br>
axis： 需要合并链接的轴，0是行，1是列 <br>
join： 连接的方式 inner，或者outer <br>

```python
frames = [df1, df2, df3]
result = pd.concat(frames)
```

要在相接的时候在加上一个层次的key来识别数据源自于哪张表，可以增加key参数
```python
result = pd.concat(frames, keys=['x', 'y', 'z'])
```
### 1.2 横向表拼接（行对齐）
#### 1.2.1 axis
当axis = 1的时候，concat就是行对齐，然后将不同列名称的两张表合并
```python
result = pd.concat([df1, df4], axis=1)
```
#### 1.2.2 join
加上join参数的属性，如果为’inner’得到的是两表的交集，如果是outer，得到的是两表的并集。
```python
result = pd.concat([df1, df4], axis=1, join='inner')
```
#### 1.2.3 join_axes
如果有join_axes的参数传入，可以指定根据那个轴来对齐数据 
例如根据df1表对齐数据，就会保留指定的df1表的轴，然后将df4的表与之拼接
```python
result = pd.concat([df1, df4], axis=1, join_axes=[df1.index])
```
### 1.3 append
```python
append是series和dataframe的方法，使用它就是默认沿着列进行凭借（axis = 0，列对齐）
result = df1.append(df2)
```

### 1.4 无视index的concat
如果两个表的index都没有实际含义，使用ignore_index参数，置true，合并的两个表就睡根据列字段对齐，然后合并。
最后再重新整理一个新的index。 

### 1.5 合并的同时增加区分数据组的键
前面提到的keys参数可以用来给合并后的表增加key来区分不同的表数据来源
#### 1.5.1 可以直接用key参数实现
```python
result = pd.concat(frames, keys=['x', 'y', 'z'])
```
#### 1.5.2 传入字典来增加分组键
```
pieces = {'x': df1, 'y': df2, 'z': df3}
result = pd.concat(pieces)
```
#### 1.6 在dataframe中加入新的行
append方法可以将 series 和 字典就够的数据作为dataframe的新一行插入。
```python
s2 = pd.Series(['X0', 'X1', 'X2', 'X3'], index=['A', 'B', 'C', 'D'])
 
result = df1.append(s2, ignore_index=True)
```
#### 1.7 表格列字段不同的表合并
如果遇到两张表的列字段本来就不一样，但又想将两个表合并，其中无效的值用nan来表示。那么可以使用ignore_index来实现。
```python
dicts = [{'A': 1, 'B': 2, 'C': 3, 'X': 4},
         {'A': 5, 'B': 6, 'C': 7, 'Y': 8}]
 
result = df1.append(dicts, ignore_index=True)
```

## 4、缺失值处理
```python
DataFrame.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None, **kwargs)
```
```python
df = pd.DataFrame([[np.nan, 2, np.nan, 0],
                    [3, 4, np.nan, 1],
                    [np.nan, np.nan, np.nan, 5],
                    [np.nan, 3, np.nan, 4]],
                    columns=list('ABCD'))
# 用0替换所有NaN元素。
df.fillna(0) 
# 我们还可以向前或向后传播非空值。
df.fillna(method='ffill') 
# 将“A”，“B”，“C”和“D”列中的所有NaN元素分别替换为0,1,2和3。
values = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
df.fillna(value=values)
# 只替换第一个NaN元素。
df.fillna(value=values, limit=1)
```
## 5、字典多对一转为一对一
```python
x_dict = {} 
    for key, value in temp.items():
        for x in value:
            x_dict[app] = key

[x_dict.get(x, None) for x in data['x_NAME']]
```
## 6、操作CSV文件

#### 1 读取表头的两种方式
```python
#方式一
import csv
with open("D:\\test.csv") as f:
    reader = csv.reader(f)
    rows=[row for row in  reader]
    print(rows[0])

#方式二
import csv
with open("D:\\test.csv") as f:
    #1.创建阅读器对象
    reader = csv.reader(f)
    #2.读取文件第一行数据
    head_row=next(reader)
    print(head_row)
```
#### 2 读取文件某一列数据
```python
#1.获取文件某一列数据
import csv
with open("D:\\test.csv") as f:
    reader = csv.reader(f)
    column=[row[0] for row in  reader]
    print(column)
```
#### 3.向csv文件中写入数据
```python
#1.向csv文件中写入数据
import csv
with open("D:\\test.csv",'a') as f:
     row=['曹操','23','学生','黑龙江','5000']
     write=csv.writer(f)
     write.writerow(row)
     print("写入完毕！")
```
#### 4.获取文件头及其索引
```
import csv
with open("D:\\test.csv") as f:
    #1.创建阅读器对象
    reader = csv.reader(f)
    #2.读取文件第一行数据
    head_row=next(reader)
    print(head_row)
    #4.获取文件头及其索引
    for index,column_header in enumerate(head_row):
        print(index,column_header)
```
#### 5.获取某列的最大值
```python
# ['姓名', '年龄', '职业', '家庭地址', '工资']
import csv
with open("D:\\test.csv") as f:
    reader = csv.reader(f)
    header_row=next(reader)
    # print(header_row)
    salary=[]
    for row in reader:
        #把第五列数据保存到列表salary中
         salary.append(int(row[4]))
    print(salary)
    print("员工最高工资为："+str(max(salary)))
```
#### 6.复制CSV格式文件
```python
import csv
f=open('test.csv')
#1.newline=''消除空格行
aim_file=open('Aim.csv','w',newline='')
write=csv.writer(aim_file)
reader=csv.reader(f)
rows=[row for row in reader]
#2.遍历rows列表
for row in rows:
    #3.把每一行写到Aim.csv中
    write.writerow(row)
```
* 01.未添加关键字参数newline=’ ‘的结果： 
* 02添加关键字参数newline=’ ‘的Aim.csv文件的内容： 

#### 7.读取csv文件所有数据
```python
import pandas as pd
path= 'D:\\test.csv'
with open(path)as file:
    data=pd.read_csv(file)
    print(data)
```

#### 8.数据框重命名
```python
import pandas as pd
a = pd.DataFrame({'A':[1,2,3], 'B':[4,5,6], 'C':[7,8,9]})
a.rename(columns={'A':'a', 'B':'b', 'C':'c'}, inplace = True)
a.columns = ['a','b','c']
```

#### 9.日期格式转换
```python
# method 1
data['交易时间'] = pd.to_datetime(data['交易时间'])

# method 2
## 使用python的datetime包中的 
## strptime函数,datetime.strptime(value,’%Y/%M/%D’) 
## strftime函数,datetime.strftime(‘%Y/%M/%D’) 
## 注意使用datetime包中后面的字符串匹配需要和原字符串的格式相同,才能转义过来,相当于yyyy-mm-dd格式的需要按照’%Y-%M-%D’来实现,而不是’%Y/%M/%D’
data['交易时间']=data['交易时间'].apply(lambda x:datetime.strptime(x,'%Y-%m-%d %H:%M:%S')
## 注意到上面代码的’%Y-%m-%d %H:%M:%S’嘛? 
## 这里的格式必须与原数值的格式一模一样才能转换,如果原数值里面是精确到时分秒的,那么你此处不写%H:%M:%S就没办法转换!!!切记
```
#### 10.多层索引转换
```python
# 1.set_index

# DataFrame可以通过set_index方法，可以设置单索引和复合索引。 
DataFrame.set_index(keys, drop=True, append=False, inplace=False, verify_integrity=False) 
# append添加新索引，drop为False，inplace为True时，索引将会还原为列
```

```python
# 2.reset_index
#reset_index可以还原索引，从新变为默认的整型索引 
DataFrame.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill=”) 
#level控制了具体要还原的那个等级的索引 
#drop为False则索引列会被还原为普通列，否则会丢失
```

```python
frame_1123=pd.DataFrame({'a':range(4),'b':range(4,0,-1),'c':['one','one','two','two'],'d':[0,1,2,3]})
 
frame_1224=frame_1123.set_index(['c','d'])

frame_1123.set_index(['c','d'],drop=False)
 
frame_1123.reset_index()
 
frame_1123.set_index(['c','d'],drop=False,append=True)



```
#### 11.数据框数据重塑
类似R语言的melt和dcast函数功能
```python
# R 语言
reshape2::melt/dcast
tidyr::gather/spread

# 数据行变列（R - melt）
# melt函数是reshape2包中的数据宽转长的函数
mydata<-melt(
       mydata,                     #待转换的数据集名称
       id.vars=c("Conpany","Name"),#要保留的主字段
       variable.name="Year",       #转换后的分类字段名称（维度）
       value.name="Sale"           #转换后的度量值名称
)

data1<-gather(
      data=mydata,         #待转换的数据集名称
      key="Year",          #转换后的分类字段名称（维度）
      value="Sale" ,       #转换后的度量值名称
      Sale2013:Sale2016    #选择将要被拉长的字段组合
      )         #（可以使用x:y的格式选择连续列，也可以以-z的格式排除主字段）

# 数据列变行（R - dcast）
dcast(
     data=data1,         #数据集名称
     Name+Conpany~Year   #x1+x2+……~class 
    #这一项是一个转换表达式，表达式左侧列      
    #出要保留的主字段（即不会被扩宽的字段，右侧则是要分割的分类变量，扩展之后的       
    #宽数据会增加若干列度量值，列数等于表达式右侧分类变量的类别个数
  ）

spread(
   data=data1,   #带转换长数据框名称
   key=Year,     #带扩宽的类别变量（编程新增列名称）  
   value=Sale)   #带扩宽的度量值 （编程新增列度量值）
```

```python
# Python
melt/pivot_table

# 数据行变列（melt）
mydata1=mydata.melt(
    id_vars=["Name","Conpany"],          #要保留的主字段
    var_name="Year",                     #拉长的分类变量
    value_name="Sale"                    #拉长的度量值名称
)

# 数据列变行（dcast）
mydata1.pivot_table(
    index=["Name","Conpany"],            #行索引（可以使多个类别变量）
    columns=["Year"],                    #列索引（可以使多个类别变量）
    values=["Sale"]                      #值（一般是度量指标）
)
```

#### 12.python识别工作日节假日
```python
from datetime import datetime
import pandas as pd

startdate = '2016-01-01'
enddate = '2016-12-31'
holiday = ['01-01', '05-01']

datalist = list(pd.date_range(start=startdate, end=enddate))
df = pd.DataFrame({'date':datalist})

df['month'] = df['date'].apply(lambda x: x.month) 
df['day'] = df['date'].apply(lambda x: x.day) 
df['weekday'] = df['date'].apply(lambda x: x.weekday()+1)

#工作日与休息日
isrest = ((df['weekday'] == 6) | (df['weekday'] == 7))  
df['label'] = isrest*1
#节假日
for h in holiday:
    #h = '01-01'
    h_month,h_day = h.split('-')
    h_index = ((df['month'] == int(h_month)) & (df['day'] == int(h_day)))
    df.loc[h_index, 'label'] = 2
```

#### 13.python排序
```python
df.sort_values(by = 'DATE',axis = 0,ascending = True)
df.loc['2016-04-07',:]
```

#### 14、lambda使用
```python
# lambda形式一
lambdafun = lambda x,y:x+y
res = lambdafun(4,5)
print(res)

# lambda形式二
lambdafun1 = lambda x:'男' if x=='man' else '女'
res = lambdafun1('man')
print(res)

# lambda 形式三
def sum(x,y):
    return x+y
lambdafun3 = lambda x,y:sum(x,y)
res = lambdafun3(4,6)
print(res)
```

#### 15、Python list 生成式(推导式list comprehension)中嵌套if else
```python
[ x if x%2 else x*100 for x in range(1, 10) ]

# [false,true][condition] is the syntax：
[[x*100,x][x %2] for x in range(1,10)]
```

#### 16、python导入自编模块
编写PY文件： pizza.py
```python
def make_pizza(size, *toppings):
    """概述要制作的披萨"""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
```

加载自定义分析模块路径
```python
sys.path.append('I:/GA_Project/project')
```

* 1. 导入整个模块
要让函数是可导的， 得先创建模块。 模块是扩展名为 .py 的文件， 包含要导入到程序中的全部代码。
下面创建一个包含函数 make_pizza（）的模块。
```python
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```









