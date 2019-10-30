#基础图类Basic Plots 01 - 散点图Scatterplot

library(recharts)

# 1 介绍Introduction
# 散点图scatter包含两种基本类型：
# 散点图scatter/point
# 气泡图bubble
# 关键是：
# x和y为数值型
# 对于气泡图，指定合法的数值型weight

# 2 用法Function Call
# echartr(data=数据框, x=数值型变量, y=数值型自变量, <series>=数值型系数变量（处理为因子）,
#         <weight>=数值型权重变量（与dataRange控件关联）, <t>=时间轴变量（处理成因子）,
#         <type>=x,y均为数值型auto,或指定为scatter,point,bubble ) 

# 3 举例Showcase
# 3.1 散点图Scatter Plot
# 3.1.1 单个数据系列Singular Series
data("iris")
# 如未指定series，则不显示图例。
echartr(iris, x=Sepal.Width, y=Petal.Width)
# 该命令等价于
echartr(iris, Sepal.Width, Petal.Width, type='scatter')
echartr(iris, ~Sepal.Width, Petal.Width, type='point')
echartr(iris, Sepal.Width, "Petal.Width", type='bubble')
echartr(iris, ~Sepal.Width, "Petal.Width", type='auto')

# 3.1.2 多个数据系列Multiple Series
data("iris")
# 如指定series，则显示图例。
echartr(iris, x=Sepal.Width, y=Petal.Width, series=Species)

# 3.1.3 带时间轴的散点图Scatter Plot with Timeline
# 时间轴要求数值型或日期/时间型的Z变量。如果传入文本型变量，
# echartr会将其转为因子，并用其索引值作图，因子标签作为时间轴标签。
echartr(iris, Sepal.Width, Petal.Width, z=Species)

# 3.2 气泡图Bubble Chart
# 关键是传入有效的数值型weight变量。如果weight被接受，且type为’bubble’，可生成气泡图。
echartr(iris, Sepal.Width, Petal.Width, weight=Petal.Length, type='bubble')
# 如type是’scatter’/‘point’，不会显示气泡图，但weight可映射dataRange控件。
echartr(iris, Sepal.Width, Petal.Width, weight=Petal.Length, series=Species) %>%
  setDataRange(calculable=TRUE, splitNumber=0, labels=c('Big','Small'),
               color=c('red', 'yellow', 'green'), valueRange=c(0, 2.5))
# 其他类型气泡图Other Kinds of Bubbles
# 带时间轴的多系列分组气泡图与同类型的散点图相仿。

# 4 其他设定Futher Setup
# 接下来可以配置控件、添加标注点/标注线，以及美化成图。
# 4.1 标注线和标注点addMarkLine And addMarkPoint
# 可以拟合一条回归曲线，并定义标注线的两个点。
lm <- with(iris, lm(Petal.Width~Sepal.Width))
pred <- predict(lm, data.frame(Sepal.Width=c(2, 4.5)))

echartr(iris, Sepal.Width, Petal.Width, Species) %>%
  addML(series=1, data=data.frame(name1='Max', type='max')) %>%
  addML(series=2, data=data.frame(name1='Mean', type='average')) %>%
  addML(series=3, data=data.frame(name1='Min', type='min')) %>%
  addMP(series=2, data=data.frame(name='Max', type='max')) %>%
  addML(series='Linear Reg', data=data.frame(
    name1='Reg', value=lm$coefficients[2], 
    xAxis1=2, yAxis1=pred[1], xAxis2=4.5, yAxis2=pred[2]))

# 你可以一个系列一个系列地添加标注线/标注点，如同上例所示。
# 但有时用户可能希望一次性给多个数据系列添加标注线/标注点，
# 可以在data中添加一个series变量，映射到addML/addMP函数的参数series。

data <- data.frame(
  name1=c('Max', 'Mean', 'Min'), type=c('max', 'average', 'min'),
  series=levels(iris$Species))
echartr(iris, Sepal.Width, Petal.Width, Species) %>%
  addML(series=1:3, data=data) %>%
  addMP(series=2, data=data.frame(name='Max', type='max')) %>%
  addML(series='Linear Reg', data=data.frame(
    name1='Reg', value=lm$coefficients[2], 
    xAxis1=2, yAxis1=pred[1], xAxis2=4.5, yAxis2=pred[2]))


