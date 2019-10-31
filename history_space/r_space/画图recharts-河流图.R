# 基础图类Basic Plots 05 - 事件河流图eventRiver
# 首先，加载recharts:
library(recharts)

# 1 介绍Introduction
# 事件河流图只有一中类型：eventRiver。
# 关键是：
# x必须按顺序包含：
# 2个必备列: 事件切片的时间, 事件名称
# 3个可选列: 事件切片的标题, 事件切片的链接, 事件切片的图标
# y必须按顺序包含：
# 1个必备列: 事件切片赋值
# 1个可选列: 事件切片权重值(默认为1)
# series必须按顺序包含：
# 2个可选列: 数据系列, 数据系列的权重(默认为1)
# 上述变量必须按所述顺序排列。

# 2 用法Function Call
# echartr(data=数据框, x=文本型自变量（转为因子）, 
#         y=数值型应变量（1各必备列-1各可选列）, 
#         <t>=时间轴（转为因子）, <series>=数据系列变量（转为因子,包括2各可选列数据系列及其权重系列）,
#         <type>=‘evenRiver’)

# 3 举例Showcase
# 3.1 基础图形Basic Plot
data(events)
events$link <- 'www.baidu.com'
events$img <- 'inst/favicon.png'
events$title <- paste(rownames(events), events$event)
echartr(events, c(time, event, title, link, img), c(value, weight), series, 
        type='eventRiver') %>% 
  setTitle('Event River', 'Ficticious Data') %>% setXAxis(name='Time') %>%
  setGrid(y2=80)

# 如果在x中为每个事件切片提供细节(title, link 和 image)，成图就会更有信息性。

# 4 其他设定Futher Setup
# 接下来可以配置控件、添加标注点/标注线，以及美化成图。
# 参考相关函数，尽情探索吧。















