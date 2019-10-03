# 基础图形Basic Plots 14 - 韦恩图Venn
# 首先，加载recharts:
library(recharts)
# 1 介绍Introduction
# Echarts中韦恩图的功能较有限。
# 关键是:
# 文本型x和数值型y
# 3行数据，其中最后一行为交集
# series不可用

# 2 用法Function Call
# echartr(data=数据框, x=（文本型自变量，其他类型会被转为因子。如提供多个变量，只传入第一个。）,
#         y=（数值型应变量。如提供多个变量，只传入第一个。）, 
#         <t>=时间轴变量, <type>=venn)

# 3 举例Showcase
# 3.1 数据准备Data Preparation
# 下面是一个虚构数据集。
data = data.frame(x=c('Collection 1', 'Collection 2', 'Intersection'), 
                  y=c(40,50,20))
knitr::kable(data)

# 3.2 基本韦恩图Basic Venn
echartr(data, x, y, type='venn') %>% 
  setTitle('Venn', 'Fictious Data')

# 4 其他设定Futher Setup
# 接下来可以配置控件、添加标注点/标注线，以及美化成图。
# 参考相关函数，尽情探索吧。




