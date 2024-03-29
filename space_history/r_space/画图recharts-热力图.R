# 基础图形Basic Plots 15 - 热力图Heatmap
# 首先，加载recharts:
library(recharts)
# 1 介绍Introduction
# 热力图只有一种类型：heatmap。
# 关键是：
# 不需要x
# 数值型y，数值型纬度lat和经度lng

# 2 用法Function Call
# echartr(data=数据框, y=（数值型应变量。如提供多个变量，只传入第一个。y表示热力值，要求介于0、1之间。如果y不在此区间内，recharts 会标化后计算。）,
#         lng=经度或x坐标, lat=维度或y坐标,
#         <series>=因子变量, <t>=时间轴, <type>=heatmap)

# 3 举例Showcase
# 3.1 数据准备Data Preparation
# 下面是一个虚构数据集。
data = rbind(
  data.frame(
    lng=100+rnorm(100,0, 1)*600, lat=150+rnorm(100,0, 1)*50, 
    y=abs(rnorm(100,0,1))),
  data.frame(
    lng=rnorm(200,0, 1)*1000, lat=rnorm(200,0, 1)*800, 
    y=abs(rnorm(200,0,1))),
  data.frame(lng=400+rnorm(20,0, 1)*300, lat=5+rnorm(20,0, 1)*10, 
             y=abs(rnorm(100,0,1))))
str(data)

# 3.2 基本图形Basic Plot
echartr(data,lng=lng,lat=lat,y=y,type='heatmap') %>% 
  setTitle("Heatmap", "Fictious Data")
# 热力图在地图中更为实用。请参考addHeatmap函数。

# 4 其他设定Futher Setup
# 接下来可以配置控件、添加标注点/标注线，以及美化成图。
# 参考相关函数，尽情探索吧。