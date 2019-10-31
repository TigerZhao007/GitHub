# 基础图类Basic Plots 04 - 蜡烛图Candlestick
# 首先，加载recharts:
library(recharts)

# 1 介绍Introduction
# 蜡烛图也叫K线图。
# 关键是：
# 文本型x
# 数值型’y’ (4列) 按’开盘’、‘收盘’、‘最低价’、’最高价’顺序排列

# 2 用法Function Call
# echartr(data=数据框, x=文本型自变量(一个变量), y=数据型自变量(四个变量), 
#         <t>=时间轴变量, <type>=c(k,candlestick))

# 3 举例Showcase
# 3.1 基本图形Basic Plot
echartr(stock, as.character(date), c(open, close, low, high), type='k') %>%
  setXAxis(name='Date', axisLabel=list(rotate=30)) %>%
  setYAxis(name="Price")

# 3.2 带时间轴With Timeline
# 还记得快速入门中的特别注意事项吗？我们要修补一下数据，
# 让它包含x和t各自所有水平的完整组合。
stock$Month <- format(stock$date, '%m')
stock$Day <- format(stock$date, '%d')
fullData <- data.frame(expand.grid(unique(stock$Month), unique(stock$Day)))
names(fullData) <- c("Month", "Day")
stock <- merge(stock, fullData, all.y=TRUE)
echartr(stock, Day, c(open, close, low, high), t=Month, type='k') %>%
  setYAxis(name="Price")

# 4 其他设定Futher Setup
# 接下来可以配置控件、添加标注点/标注线，以及美化成图。
# 参考相关函数，尽情探索吧。










