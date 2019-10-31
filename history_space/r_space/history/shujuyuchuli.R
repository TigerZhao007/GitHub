##  准备工作。 ##

#  读取文件。
library(xlsx)
sj0 <- read.xlsx("shiyan01.xlsx",sheetIndex = "Sheet1",encoding = "UTF-8")
sj0

#  标题转化。
sj1 <- data.frame(bianma = sj0$编码, x1 = sj0$X1, x2 = sj0$X2, x3 = sj0$X3, x4 = sj0$X4)
sj1

##  数据清洗。  ##

#  数据截取。
sj2 <- sj1[5:25,2:5]
sj2         
fix(sj2)

# 缺失值识别。
is.na(sj2)
n   <- sum(is.na(sj2)) 
n

#  异常值识别。
windows()             #  单变量散点图。
par(mfrow = c(2, 2))
dotchart(sj2$x1,main = "x1",xlab = "取值", ylab = "频数")
dotchart(sj2$x2,main = "x2",xlab = "取值", ylab = "频数")
dotchart(sj2$x3,main = "x3",xlab = "取值", ylab = "频数")
dotchart(sj2$x4,main = "x4",xlab = "取值", ylab = "频数")
graphics.off()

sj2$x1
sj2[[1]]

windows()             #  单变量散点图。(利用循环语句)
par(mfrow = c(2, m/2))
for (i in 1:m) {
  sj2
  dotchart(sj2[[i]],main = paste("x",i), xlab = "取值", ylab = "频数")
  
}

windows()             #  水平箱线图。
par(mfrow = c(2, 2))
boxplot(sj2$x1,main = "x1", horizontal = F)
boxplot(sj2$x2,main = "x2", horizontal = F)
boxplot(sj2$x3,main = "x3", horizontal = F)
boxplot(sj2$x4,main = "x4", horizontal = F)
graphics.off()

m <- ncol(sj2)         #  水平箱线图。(利用循环语句)
m
windows()        
par(mfrow = c(2, m/2))
for (i in 1:m) {
  sj2
  boxplot(sj2[[i]],main = paste("x",i), horizontal = F)
  
}

sp=boxplot(sj2$x3,boxwex=0.7)    # 异常值检查箱线图。 
title("x3")  
xi=1.1  
sd.s=sd(sj2[complete.cases(sj2$x3),]$x3)  
mn.s=mean(sj2[complete.cases(sj2$x3),]$"x3")  
points(xi,mn.s,col="red",pch=18)  
arrows(xi, mn.s - sd.s, xi, mn.s + sd.s, code = 3, col = "pink", angle = 75, length = .1)  
text(rep(c(1.05,1.05,0.95,0.95),length=length(sp$out)),labels=sp$out[order(sp$out)],  
     sp$out[order(sp$out)]+rep(c(150,-150,150,-150),length=length(sp$out)),col="red") # 不清楚做什么。


##  异常值差值案例分析  ##
set.seed(3147)
# 产生100个服从正态分布的数据
x <- rnorm(100)
summary(x)
# 输出异常值
boxplot.stats(x)$out
# 绘制箱线图
boxplot(x)
y <- rnorm(100)
# 生成一个包含列名分别为x与y的数据框df
df <- data.frame(x, y)
rm(x, y)
head(df)
# 连接数据框df
attach(df)
# 输出x的异常值
(a <- which(x %in% boxplot.stats(x)$out))
# 输出y中的异常值
(b <- which(y %in% boxplot.stats(y)$out))
detach(df) # 断开与数据框的连接
# 输出x,y相同的异常值
(outlier.list1 <- intersect(a,b))
plot(df)
# 标注异常点
points(df[outlier.list1,], col="red", pch="+", cex=2.5)
# x或y中的异常值
(outlier.list2 <- union(a,b))
plot(df)
points(df[outlier.list2,], col="blue", pch="x", cex=2)

##  数据处理准备阶段。  ##

#  缺失值、异常值行定位。
qw1 <- which(is.na(sj2$x1))
qw2 <- which(is.na(sj2$x2))
qw3 <- which(is.na(sj2$x3))
qw4 <- which(is.na(sj2$x4))
qw <- list(qw1, qw2, qw3, qw4)
qw[[1]]

yw1 <- which(sj2$x1 == boxplot.stats(sj2$x1)$out)
yw2 <- which(sj2$x2 == boxplot.stats(sj2$x2)$out)
yw3 <- which(sj2$x3 == boxplot.stats(sj2$x3)$out[1])
yw4 <- which(sj2$x4 == boxplot.stats(sj2$x4)$out[2])
yw  <- list(yw1, yw2, yw3, yw4)
w <- yw[[2]]
sj2$x2[w]

m <- ncol(sj2)               #缺失值定位（利用循环语句）  
m
qwz    <- list()
for (i in 1:m) {
  qwz[[i]] <- which(is.na(sj2[[i]]))
  
}
qwz
 
m <- ncol(sj2)               #异常值定位（利用循环语句）  
m
ywz1    <- list()
for (i in 1:m) {
  n     <- length(boxplot.stats(sj2[[i]])$out)
  ywz2   <- list()
  for (j in 1:n) {
    ywz2[j] <- which(sj2[[i]] == boxplot.stats(sj2[[i]])$out[j]) 
    
  }
  ywz1[[i]] <- unlist(ywz2)
}
ywz1
ywz1[[3]]

#  异常值处理。(利用循环语句)

n = ncol(sj2)
for (i in 1:n) {
  tz <- sj2[[i]]
  tz[ywz1[[i]]] <- NA
  sj2[[i]] <- tz
}
sj2
fix(sj2)

#  缺失样本分开。（利用循环语句）

n <- ncol(sj2)             # 编写循环语句。
sub1 <- list()
for (i in 1:n) {
  sub1[[i]] <- which(is.na(sj2[i]))
}
unlist(sub1)
sub2 <- unique(unlist(sub1))     # 缺失样本所在行。
sj2.1 <- sj2[-sub2, ]
sj2.2 <- sj2[ sub2, ]

##  数据处理  ## 

# 行删除法处理缺失。
result1.1 <- na.omit(sj2)  # 程序自带函数。
result1.1

n <- ncol(sj2)             # 编写循环语句。
tz <- list()
for (i in 1:n) {
  tz[[i]] <- which(is.na(sj2[i]))
  sj2     <- sj2[-tz[[i]],]
}
sj2


sub <- which(is.na(sj2$x1))  # 一步一步计算。
sub
sj2 <- sj2[-sub,]
sj2
sub <- which(is.na(sj2$x2))
sub
sj2 <- sj2[-sub,]
sj2
sub <- which(is.na(sj2$x3))
sub
sj2 <- sj2[-sub,]
sj2
sub <- which(is.na(sj2$x4))
sub
sj2 <- sj2[-sub,]
sj2

# 均值替代法。
n <- ncol(sj2)             # 求均值循环语句。
avg.sj2.1 <- list()
for (i in 1:n) {
  avg.sj2.1[i] <- mean(sj2.1[[i]])
}
avg.sj2.1

n <- ncol(sj2)             # 均值替代循环语句。
tz <- list()
for (i in 1:n) {
  tz[[i]] <- which(is.na(sj2[i]))
  sj2[tz[[i]],i] <- avg.sj2.1[[i]]
}
fix(sj2)

##  回归插补法。  ##

#  数据准备阶段。
st0 <- read.xlsx("shijian01.xlsx",sheetIndex = "Sheet1")
st0
st1 <- data.frame(date = st0$data,x1 = st0$x11, x2 = st0$x3, x3 = st0$x4, x4 = st0$x6)

n <- ncol(st1)             # 编写循环语句。
sub1 <- list()
for (i in 1:2) {
  sub1[[i]] <- which(is.na(st1[i]))
}
unlist(sub1)
sub2 <- unique(unlist(sub1))     # 缺失样本所在行。
st1.1 <- st1[-sub2, ]
st1.2 <- st1[sub2, ]

#  回归模型插补。
model <- lm(x1~date, data = st1.1)
summary(model)
st1.2$x1 <- predict(model,st1.2)
result3 <- rbind(st1.1,st1.2)
fix(result3)

##  多重插补法。 ##
library(lattice)
library(MASS)
library(nnet)
library(mice)
st2 <- st1
imp <- mice(st2,m=4)
fit <- with(imp, lm(x1~date,data = st2))
fit
summary(fit)
pooled <- pool(fit)
pooled
summary(pooled)
result4 <- complete(imp, action = 3)
fix(result4)







