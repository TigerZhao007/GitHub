# 基础图类Basic Plots 02 - 条图Bar/柱图Column
# 首先，加载recharts:
library(recharts)

# 1 介绍Introduction
# 条图Bar plot包含3种基本类型：
# 条图: bar|hbar
# 柱图: column|vbar
# 直方图: histogram|hist
# 关键是：
# 文本型x和数值型y
# x各水平(和series各水平)的每一个组合只能对应于一个y数据点
# 平铺和堆积条图/柱图可通过工具箱按钮快速相互切换

# 2 用法Function Call
# echartr(data=数据框, x=文本型自变量（转为因子）, <y>=数值型变量（存缺失值绘直方图）,
#         <series>=数据系列（转为因子）, <t>=时间变量（转为因子）,
#         <type>= c(auto,bar,hbar,vbar,column), 
#         <subtype>={bar/column:c(stack-要堆积的系列),hist:c('count'/'freq'-按频数统计,'density'-按密度统计)})

# 3 举例Showcase
# 3.1 数据准备Data Preparation
# 让我们看一下datasets包自带的Titanic数据集。不同舱位的生存人数如下:
titanic <- data.table::melt(apply(Titanic, c(1,4), sum))
names(titanic) <- c('Class', 'Survived', 'Count')
knitr::kable(titanic)

# 3.2 条图Horizontal Bar Chart
# 3.2.1 单个数据系列Singular Series
# type可以是’hbar’、‘bar’或’auto’。
# setTitle---添加标题
echartr(titanic[titanic$Survived=='Yes',], Class, Count) %>%
  setTitle('Titanic: N Survival by Cabin Class')

# 3.2.2 多个数据系列Multiple Series
echartr(titanic, Class, Count, Survived) %>%
  setTitle('Titanic: Survival Outcome by Cabin Class')

# 3.2.3 堆积条图Stacked Horizontal Bar Chart
# 相比于hbar，你需要设置subtype为’stack’。
# 单系列和多系列堆积条图的实现语法和普通条图类似。
echartr(titanic, Class, Count, Survived, type='hbar', subtype='stack') %>%
  setTitle('Titanic: Survival Outcome by Cabin Class') 

# 3.2.4 龙卷风图Tornado Chart
# 龙卷风图是条图的特例。关键是：
# 提供一个全正值变量，和一个全负值变量
# 平铺，不要堆积
titanic_tc <- titanic
titanic_tc$Count[titanic_tc$Survived=='No'] <- -titanic_tc$Count[titanic_tc$Survived=='No']
g =echartr(titanic_tc, Class, Count, Survived, type='hbar') %>%
  setTitle("Titanic: Survival Outcome by Cabin Class")
g
# 当然，我们还得微调一下坐标轴。Y轴应该和x轴交会于零点，
# 且x轴标签都要取绝对值 (略有点复杂，需要懂一点JaveScript)。
g %>% setYAxis(axisLine=list(onZero=TRUE)) %>% 
  setXAxis(axisLabel=list(
    formatter=JS('function (value) {return Math.abs(value);}')
  ))

# 3.2.5 人口学金字塔Population Pyramid
# 如果设type为’hbar’，subtype为’stack’，就得到了社会学中常用的人口学金字塔。
echartr(titanic_tc, Class, Count, Survived, type='hbar', subtype='stack') %>%
  setTitle("Titanic: Survival Outcome by Cabin Class") %>%
  setYAxis(axisLine=list(onZero=TRUE)) %>%
  setXAxis(axisLabel=list(
    formatter=JS('function (value) {return Math.abs(value);}')
  ))

# 3.2.6 带时间轴的条图Bar Chart with Timeline
# 需要一个时间轴变量。不妨用’sex’变量。
titanic_sex <- data.table::melt(apply(Titanic, c(1,2,4), sum))
names(titanic_sex)[4] <- "Count"
knitr::kable(titanic_sex)

echartr(titanic_sex, Class, Count, Survived, t=Sex, type='bar') %>% 
  setTitle("Titanic: Survival Outcome by Cabin Class Across Sex")

# 3.3 柱图Vertical Bar (Column) Chart
# 3.3.1 平铺柱图Tiled Vertical Bar (Column) Chart
# 相比于hbar，需要设type为’vbar’或’column’。
# 单系列或多系列柱图的实现语法和普通条图类似。
echartr(titanic, Class, Count, Survived, type='column') %>%
  setTitle('Titanic: Survival Outcome by Cabin Class') 

# 3.3.2 堆积柱图Stacked Vertical Bar (Column) Chart
# 相比于vbar，需要设subtype为’stack’。
# 单系列或多系列柱图的实现语法和普通条图类似。
echartr(titanic, Class, Count, Survived, type='column', subtype='stack') %>%
  setTitle('Titanic: Survival Outcome by Cabin Class') 

# 3.4 直方图Histogram
# 3.4.1 按频数统计Stat by Frequency
# 直方图是柱图的特例，只需要提供一个数值型x变量。
# type可以是’histogram’、‘hist’。setTooltip(formatter='none'调用默认的tooltip模板。
# Echarts2无法自适应设定barWidth，所以你需要自己设定一个合理的数值。
echartr(iris, Sepal.Width, width=600) %>%
  setTitle('Iris: Histogram of Sepal.Width') %>%
  setTooltip(formatter='none') %>% 
  setSeries(1, barWidth=500/13)

# 3.4.2 按密度统计Stat by Density
# 有时需要一幅密度直方图，那么设subtype为’density’。
echartr(iris, Sepal.Width, type='hist', subtype='density', width=600) %>%
  setTitle('Iris: Histogram of Sepal.Width') %>% 
  setYAxis(name="Density") %>%
  setTooltip(formatter='none') %>% 
  setSeries(1, barWidth=500/13)

# 4 其他设定Futher Setup
# 接下来可以配置控件、添加标注点/标注线，以及美化成图。
