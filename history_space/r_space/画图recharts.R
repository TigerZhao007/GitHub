library(devtools)  
library(recharts)

#echart(data=数据, x=~x轴变量,y=~y轴变量,type=‘scatter’, palette=调色盘颜色,title=主标题
#       ,subtitle=副标题,xAxis=x轴选项,yAxis=y轴选项,markLine=标记线,markPoint=标记点,等)
data("iris")


#1.散点图/气泡图
echartr(iris, x=Sepal.Width, y=Petal.Width)
#多个维度：series控制
echartr(iris, x=Sepal.Width, y=Petal.Width, series=Species)
echartr(iris, Sepal.Width, Petal.Width,series = Species, weight=Petal.Length, type='bubble')

#2.管道操作
echartr(iris, Sepal.Width, Petal.Width, weight=Petal.Length) %>%
  setDataRange(calculable=TRUE, splitNumber=0, labels=c('Big','Small'),
               color=c('red', 'yellow', 'green'), valueRange=c(0, 2.5))

#3.折线图
#先改造下内置数据集：
aq <- airquality
aq$Date <- as.Date(paste('1973', aq$Month, aq$Day, sep='-'))
aq$Day <- as.character(aq$Day)
aq$Month <- factor(aq$Month, labels=c("May", "Jun", "Jul", "Aug", "Sep"))
echartr(aq, Date, Temp, type='line') %>%
  setTitle('NY Temperature May - Sep 1973') %>% setSymbols('none')
#含有分类属性：
echartr(aq, Day, Temp, Month, type='line') %>%
  setTitle('NY Temperature May - Sep 1973, by Month') %>% 
  setSymbols('emptycircle')
#带有时间轴（带有动态效果哦~~~）：
echartr(aq, Day, Temp, t=Month, type='line') %>%
  setTitle('NY Temperature May - Sep 1973, by Month') %>% 
  setSymbols('emptycircle')
#也可画面积图：type属性控制
echartr(aq, Day, Temp, Month, type='area', subtype='stack') %>%
  setTitle('NY Temperature May - Sep 1973, by Month') %>% 
  setSymbols('emptycircle')

#4.饼图
#重构内置数据集
titanic <- data.table::melt(apply(Titanic, c(1,4), sum))
names(titanic) <- c('Class', 'Survived', 'Count')
knitr::kable(titanic)
#画饼图，可以和漏斗图切换
echartr(titanic, Class, Count, type='pie') %>%
  setTitle('Titanic: N by Cabin Class')
#多个饼图：
echartr(titanic, Survived, Count, facet=Class, type='pie') %>%
  setTitle('Titanic: Survival Outcome by Cabin Class')
#环图：
echartr(titanic, Survived, Count, facet=Class, type='ring') %>%
  setTitle('Titanic: Survival Outcome by Cabin Class')
#信息图样环图：
ds <- data.frame(q=c('68% feel good', '29% feel bad', '3% have no feelings'),
                 a=c(68, 29, 3))
g <- echartr(ds, q, a, type='ring', subtype='info') %>% 
  setTheme('macarons', width=800, height=600) %>%
  setTitle('How do you feel?','ring_info', 
           pos=c('center','center', 'horizontal'))
g
#南丁格尔玫瑰图：
echartr(titanic, Class, Count, facet=Survived, type='rose', subtype='radius') %>% 
  setTitle('Titanic: Survival Outcome by Cabin Class') 

#5.雷达图
#重构内置数据集
cars = mtcars[c('Merc 450SE','Merc 450SL','Merc 450SLC'),
              c('mpg','disp','hp','qsec','wt','drat')]
cars$model <- rownames(cars)
cars <- data.table::melt(cars, id.vars='model')
names(cars) <- c('model', 'indicator', 'Parameter')
knitr::kable(cars)
#单个雷达图
echartr(cars, indicator, Parameter, model, type='radar', sub='fill') %>%
  setTitle('Merc 450SE  vs  450SL  vs  450SLC')
#多个雷达图：
echartr(cars, indicator, Parameter, facet=model, type='radar') %>%
  setTitle('Merc 450SE  vs  450SL  vs  450SLC')

#6.比较有趣的dashboard
#构造一个数据集：
data = data.frame(x=rep(c('KR/min', 'Kph'), 2), y=c(3.3, 56, 9.5, 88), 
                  z=c(rep('t1', 2), rep('t2', 2)))
knitr::kable(data)
echartr(data, x, y, type='gauge')
#多个dashboard：
echartr(data, x, y, facet=x, type='gauge')
#带时间轴：
echartr(data, x, y, facet=x, t=z, type='gauge')




