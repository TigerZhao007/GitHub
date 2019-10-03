##  聚类分析   ##

#  数据读取。
library(RODBC)
ch <- odbcConnect("Rspace", uid = "sa", pwd = "sdk")
tq <- sqlFetch(ch, "天气")
odbcClose(ch)
tq1 <- tq[,-c(1:2)]
rownames(tq1) <- c("南 京 市","无 锡 市","徐 州 市","常 州 市","苏 州 市","南 通 市","连云港市","淮 安 市","盐 城 市","扬 州 市",
                         "镇 江 市","泰 州 市","宿 迁 市")
colnames(tq1) <- c("一月","二月","三月","四月","五月","六月","七月","八月","九月","十月","十一月","十二月")
tq1
sqlSave(ch,tq1,tablename = "天气2")
odbcClose(ch)
str(tq1)
head(tq1)
summary(tq1)
pie(table(tq1$一月))
var(tq1$一月)
cov(tq1)
cor(tq1)
hist(tq1$一月)
plot(tq1)
pairs(tq1)

##  K-means聚类。（动态聚类法） ##

install.packages("knncat")
library(class)
set.seed(25296)
jl.K_means <- kmeans(tq1,3)
jl.K_means$cluster            #查看每类结果。

table(jl.K_means$cluster)
jl.K_means$centers
jl.K_means$totss
jl.K_means$withinss
jl.K_means$tot.withinss
jl.K_means$betweenss
jl.K_means$size
jl.K_means$iter
jl.K_means$ifault
summary(jl.K_means)
sort(jl.K_means$cluster)


##  系统聚类法。  ##

tq1
d <- dist(scale(tq1))
hc1 <- hclust(d);hc1
hc2 <- hclust(d,"average");hc2
hc3 <- hclust(d,"centroid");hc3
hc4 <- hclust(d,"ward");hc4
opar <- par(mfrow = c(2,1), mar = c(5.2, 4, 0, 0))
summary(hc1)
hc1$merge
hc1$height
hc1$order
hc1$labels
hc1$method
hc1$call
hc1$dist.method

# 绘制谱系图和聚类情况-最长聚类。
plclust(hc1,hang = 1)                          # 绘制树状图。
re1 <-rect.hclust(hc1, k = 3, border = "red")  # 圈出三类图。
re1                                            # 查看每类结果。

# 绘制谱系图和聚类情况-类平均法。
plclust(hc2,hang = 1)
re2 <-rect.hclust(hc2, k = 3, border = "red")

# 绘制谱系图和聚类情况-重心法。
plclust(hc3,hang = 1)
re3 <-rect.hclust(hc3, k = 3, border = "red")

# 绘制谱系图和聚类情况-Ward法。
plclust(hc4,hang = 1)
re4 <-rect.hclust(hc4, k = 3, border = "red")
re4
summary(re4)





