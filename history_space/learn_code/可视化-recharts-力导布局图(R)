# 基础图类Basic Plots 14 - 力导向布局图Force Chart
# 首先，加载recharts:
library(recharts)

# 1 介绍Introduction
# 力导向布局图包括两类：
# 曲线连接
# 直线连接

# 关键是：
# 数据结构:
# 矩阵模式: 一个数据框，其中一列为节点名，余下的是一个矩阵。将节点名赋值给x, 矩阵赋值给y。
# 节点/联结模式：一个节点数据框[x, NA, series, weight]和一个联结数据框[x, x1, relation, value]。用rbind将两者合并。如果未提供节点数据框，recharts会基于联结数据框自动构建。相应地，提供[x, x1, series/relation, weight/value]数据框。
#力导向布局图和和弦图可通过工具箱按钮快速切换。

# 2 用法Function Call
# echartr(data=数据框, x=文本型自变量（一个）, 
#         <y>=数值型应变量。节点/联结模式下，只传入y的第一个变量。矩阵模式下，y的所有列都被传入,
#         <series>=数据系列（一个因子）, <t>=事件轴变量, 
#         <type>=c(force/force_curve,force_line), 
#         <subtype>={force: c(“arrow”, “triangle”),arrow: 连线末端图标为箭头,triangle: 连线末端图标为三角.force_line: c(“arrow”, “triangle”)})

# 3 举例Showcase
# 3.1 数据准备Data Preparation
# 3.1.1 矩阵模式Matrix Mode
grpmtx <- matrix(c(11975, 5871, 8916, 2868, 1951, 10048, 2060, 6171, 8010, 16145,
                   8090, 8045, 1013, 990, 940, 6907), byrow=TRUE, nrow=4)
grpmtx <- as.data.frame(grpmtx)
names(grpmtx) <- paste0('Group', 1:4)
grpmtx$Name <- paste0('Group', 1:4)
knitr::kable(grpmtx, align=c('lllll'))
# 数据框的前四列就是一个矩阵，而最后一列则是名称向量。所以其数据结构符合矩阵模式的要求。
# 矩阵模式可以转换为节点/联结模式。Matrix[i, j]代表了两个节点(i & j)和一个联结(i -> j)。

# 3.1.2 节点Node/联结link模式
str(yuNetwork);head(yuNetwork)
# yuNetwork数据集包含一个节点数据框(nodes)及一个联结数据框(links)。可以合并为一个数据框。
# nodes节点:name: 节点名称,series: 节点所属数据系列,value: 节点的重要性分值
# links联结:source和target: 定义了联结的方向,relation: 联结的名称,weight: 联结的重要性分值
nodes <- cbind(yuNetwork$nodes[,1], NA, yuNetwork$nodes[,2:3],
               stringsAsFactors=FALSE)
names(nodes) <- names(yuNetwork$links)
yu <- rbind(yuNetwork$links, nodes, stringsAsFactors=FALSE)

# 3.2 力导向布局图Force Chart
# 3.2.1 曲线联结Force with Curve
# 设type为’force’。
echartr(yu, c(source, target), weight, relation, type='force') %>% 
  setTitle("Yu Family of Shaoxing") %>% setTheme(palette=c(
    'tan3','green3','green2','lawngreen','olivedrab1'))

# 3.2.2 直线联结Force with Line
# 3.2.2.1 矩阵模式Matrix Mode
echartr(grpmtx, Name, c(Group1, Group2, Group3, Group4), type='force_line') %>% 
  setTitle('Test Data', 'Force with ribbon')
# 3.2.2.2 节点Node/联结link模式
# 设type为’force_line’。
echartr(yu, c(source, target), weight, relation, type='force_line') %>% 
  setTitle("Yu Family of Shaoxing") %>% setTheme(palette=c(
    'tan3','green3','green2','lawngreen','olivedrab1'))

# 3.2.3 带时间轴的力导向布局图Force with Timeline
#用year列作为时间轴。
echartr(deutsch, c(club, player), weight, role, t=year,
        type='force', sub='arrow') %>% 
  setTitle('Club Orientation of Deutsch Soccer Team')

# 4 其他设定Futher Setup
# 接下来可以配置控件、添加标注点/标注线，以及美化成图。
# 参考相关函数，尽情探索吧。




