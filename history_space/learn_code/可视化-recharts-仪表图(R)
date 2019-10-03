# 基础图形Basic Plots 24 - 仪表盘Gauge
# 首先，加载recharts:
library(recharts)
# 1 介绍Introduction
# 仪表盘gauge也叫dashboard。
# 关键是:
# 文本型x
# 数值型y
# 文本型facet可获得多个仪表盘
# 设置t，让仪表盘动起来
# 2 用法Function Call
# echartr(data=数据框, x=（文本型自变量。如提供多个变量，只传入前两个。）, 
#         y=（数值型应变量。如提供多个变量，只传入第一个。）, 
#         <series>=转为因子, <facet>=（每个水平被处理为分组因子，用于产生独立的极坐标系。如提供多个变量，只传入第一个。）, 
#         <t>=时间轴变量, <type>=gauge)

# 3 举例Showcase
# 3.1 数据准备Data Preparation
#下面是一个虚构数据集。
data = data.frame(x=rep(c('KR/min', 'Kph'), 2), y=c(6.3, 54, 9.5, 82), 
                  z=c(rep('t1', 2), rep('t2', 2)))
knitr::kable(data)

# 3.2 单个仪表盘Single Gauge
echartr(data, x, y, type='gauge')

# 3.3 多个仪表盘Multiple Gauges
echartr(data, x, y, facet=x, type='gauge')

# 3.4 带时间轴With Timeline
echartr(data, x, y, facet=x, t=z, type='gauge')

# 4 其他设置Futher Setup
# 接下来可以配置控件、添加标注点/标注线，以及美化成图。
# 参考相关函数，尽情探索吧。



