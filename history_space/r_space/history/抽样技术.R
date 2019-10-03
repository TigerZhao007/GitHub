##　随机数生成。　　##

x1  <- runif(10, 1, 100)    #生成1-100之间10个随机数。（均匀分布）
x2  <- sample(1:100, 10, replace = F)    #生成1-100之间10个整数。
x3  <- rnorm(10, mean=0, sd=1)   # 正态分布。（均值为0，方差为1。）
x4  <- rexp(10, rate=1)   # 指数。（参数为1。）
x   <- data.frame(x1, x2, x3, x4)
x
x5  <- rgamma(10, shape, rate=1, scale=1/rate)   # r 分布
x6  <- rpois(10, lambda)   # 泊松
x7  <- rt(10, df, ncp)   # t 分布
x8  <- rf(10, df1, df2, ncp)   # f 分布
x9  <- rchisq(10, df, ncp=0)   # 卡方分布
x10 <- rbinom(10, size, prob)   # 二项分布
x11 <- rweibull(10, shape, scale=1)   # weibull 分布
x12 <- rbata(10, shape1, shape2)   # bata 分布

##  抽样模拟技术。　　##

##  随机抽样。  ##
y1 <- sample(1:100, 5, replace=T)     # 有放回抽样。
y2 <- sample(1:100, 5, replace=F)     # 无放回抽样。
data.frame(y1, y2)

zt <- c("南 京 市","无 锡 市","徐 州 市","常 州 市","苏 州 市","南 通 市","连云港市","淮 安 市","盐 城 市","扬 州 市",
        "镇 江 市","泰 州 市","宿 迁 市")
y1.1 <- sample(zt, 5, replace = T)
y2.1 <- sample(zt, 5, replace = F)

y1.1 <- sample(zt, size = 1000, replace = T)
table(y1.1)
hist(table(y1.1))

# 随机排序。
y3.s1 <- sample(zt, length(zt), replace = F)
y3.s1

# 随机抽样。（数据框、矩阵）。
library(RODBC)
ch <- odbcConnect("Rspace", uid = "sa", pwd = "sdk")
tq <- sqlFetch(ch, "天气")
odbcClose(ch)
tq1 <- tq[,-c(1:2)]
rownames(tq1) <- c("南 京 市","无 锡 市","徐 州 市","常 州 市","苏 州 市","南 通 市","连云港市","淮 安 市","盐 城 市","扬 州 市",
                   "镇 江 市","泰 州 市","宿 迁 市")
colnames(tq1) <- c("一月","二月","三月","四月","五月","六月","七月","八月","九月","十月","十一月","十二月")
tq1
col.name=colnames(tq1)
row.name=rownames(tq1)
#列名向量不返回抽样
sam.col.name=sample(col.name,5,replace=FALSE)
#行名向量不返回抽样
sam.row.name=sample(row.name,5,replace=FALSE)
B=tq1[sam.row.name,sam.col.name]
B

##  设置随机种子。  ##
set.seed(1234)
x <- rnorm(10)
x
# 设置了随机数种子后，每次产生的分布数都是相同的
set.seed(1234)
x <- rnorm(10)
x
# 移除了随机数种子后，产生的随机分布改变了
rm(.Random.seed)
x <- rnorm(10)
x

##  分层抽样。  ##
library(RODBC)
bj <- odbcConnect("Rspace", uid = "sa", pwd = "sdk")
bj1 <- sqlFetch(bj, "理科")
odbcClose(bj)
bj1
head(bj1)
tail(bj1)
bj2 <- na.omit(bj1)
bj2
tail(bj2)
ncol(bj2)
nrow(bj2)
summary(bj2)
rowname <- rownames(bj2)
colname <- colnames(bj2)
samp.rowname <- sample(rowname, 100)
samp.colname <- sample(colname, 4)
samp <- bj2[samp.rowname, samp.colname]
table(bj2$考场)
install.packages("sampling")
library("sampling")
summary(bj2)
table(bj2$班级)
n <- length(table(bj2$班级))
str.1 <- strata(bj2, stratanames = "班级", size = rep(1,n), method = "srswor", description = F)
str.2 <- strata(bj2, stratanames = "班级", size = rep(1,n), method = "srswor", description = T)
getdata(bj2, str.1)     # 查看分层抽样数据。

##  整群抽样。  ##
clu.1 <- cluster(bj2, clustername = "班级", size = 2, method = "srswor", description = F)
clu.2 <- cluster(bj2, clustername = "班级", size = 2, method = "srswor", description = T)
getdata(bj2, clu.1)

##  训练集和测试集。（应用）  ##
t.s <- sample(nrow(tq1), 3/4*nrow(tq1))
t.train <- tq1[t.s,]
t.text <- tq1[-t.s,]
dim(t.text)












