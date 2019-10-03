# 基础图类Basic Plots 03 - 线图Line/面积图Area

# 首先，加载recharts:
library(recharts)

# 1 介绍Introduction
# 线图Line plot包括4个基本类型：
# 线图: line
# 平滑线图: curve
# 面积图: area
# 平滑面积图: wave

# 关键是:
# 文本型x和数值型y
# x (和series) 的各水平的每个组合只能对应一个y数据点
# 平铺和堆积线图可通过工具箱按钮快速切换
# 线图/面积图可通过工具箱快速切换为柱图/条图

# 2 用法Function Call
# echartr(data=数据框, x=文本自变量（转为因子）, y=数据型变量,
#         <series>=数据系列变量（转为因子）, <weight>=权重变量映射线宽,
#         <t>=时间轴变量（转为因子）, <type>=c(line,curve,area,wave), 
#         <subtype>={line:c(stack堆积,smooth平滑,dotted虚线,solid实线,dashed虚划线)})

# 3 举例Showcase
# 3.1 数据准备Data Preparation
# 让我们使用datasets包自带数据集airquality。数据结构如下：
aq <- airquality
aq$Date <- as.Date(paste('1973', aq$Month, aq$Day, sep='-'))
aq$Day <- as.character(aq$Day)
aq$Month <- factor(aq$Month, labels=c("May", "Jun", "Jul", "Aug", "Sep"))
head(aq)

# 3.2 线图Line Chart
# 3.2.1 单个数据系列Singular Series
# type设为’line’。
echartr(aq, Date, Temp, type='line') %>%
  setTitle('NY Temperature May - Sep 1973') %>% setSymbols('none')

# 3.2.2 多个数据系列Multiple Series
echartr(aq, Day, Temp, Month, type='line') %>%
  setTitle('NY Temperature May - Sep 1973, by Month') %>% 
  setSymbols('emptycircle')

# 3.2.3 堆积线图Stacked Line Chart
# 设type为’line’，subtype为’stack’。
echartr(aq, Day, Temp, Month, type='line', subtype='stack') %>%
  setTitle('NY Temperature May - Sep 1973, by Month') %>% 
  setSymbols('emptycircle')

# 3.2.4 权重变量映射线宽Line Width Mapped to Weight
# 把线宽和各系列(Month)风速均值关联起来。
echartr(aq, Day, Temp, Month, weight=Wind, type='line') %>%
  setTitle('NY Temperature May - Sep 1973, by Month') %>% 
  setSymbols('emptycircle')

# 3.2.5 带时间轴的线图Line Chart with Timeline
echartr(aq, Day, Temp, t=Month, type='line') %>%
  setTitle('NY Temperature May - Sep 1973, by Month') %>% 
  setSymbols('emptycircle')

# 3.3 平滑线图Curve (Smooth Line) Chart
# 3.3.1 平铺平滑线图Tiled Smooth Line Chart
# 设type为’curve’。
echartr(aq, Day, Temp, Month, type='curve') %>%
  setTitle('NY Temperature May - Sep 1973, by Month') %>% 
  setSymbols('emptycircle')

# 3.3.2 堆积平滑线图Stacked Smooth Line Chart
# 设type为’curve’，subtype为’stack’。
echartr(aq, Day, Temp, Month, type='curve', subtype='stack') %>%
  setTitle('NY Temperature May - Sep 1973, by Month') %>% 
  setSymbols('emptycircle')

# 3.4 面积图Area Chart
# 3.4.1 平铺面积图Tiled Area Chart
# 面积图实际上和线图是一回事，唯一不同之处是前者设定了areaStyle特性。
# 设type为’area’。
echartr(aq, Date, Temp, type='area') %>%
  setTitle('NY Temperature May - Sep 1973') %>% 
  setSymbols('emptycircle')

# 3.4.2 堆积面积图Stacked Area Chart
# 设type为’area’，subtype为’stack’。
echartr(aq, Day, Temp, Month, type='area', subtype='stack') %>%
  setTitle('NY Temperature May - Sep 1973, by Month') %>% 
  setSymbols('emptycircle')

# 3.5 平滑面积图Wave (Smooth Area) Chart
# 3.5.1 平铺平滑面积图Tiled Smooth Area Chart
# 设type为’wave’。
echartr(aq, Date, Temp, type='wave') %>%
  setTitle('NY Temperature May - Sep 1973') %>% 
  setSymbols('emptycircle')

# 3.5.2 堆积平滑面积图Stacked Smooth Area Chart
# 设type为’wave’，subtype为’stack’。
echartr(aq, Day, Temp, Month, type='wave', subtype='stack') %>%
  setTitle('NY Temperature May - Sep 1973, by Month') %>% 
  setSymbols('emptycircle')

# 4 其他设定Futher Setup
# 接下来可以配置控件、添加标注点/标注线，以及美化成图。
# 参考相关函数，尽情探索吧。




