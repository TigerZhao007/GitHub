##  回归分析  ##

# 读取数据库数据。
library(RODBC)
lj <- odbcConnect("Rspace", uid = "sa", pwd = "sdk")
cj0 <- sqlFetch(lj, "理科")
odbcClose(lj)
cj1  <- na.omit(cj0)
head(cj1)
tail(cj1)
cj <- cj1[,4:12]
head(cj)
tail(cj)
y <- cj$总分
x1 <- cj$数学
x2 <- cj$英语
x3 <- cj$物理
plot(y~x1,col= 8)
abline(lm(y~x1),col= 2)
plot(y~x2,col= 8)
abline(lm(y~x2),col= 2)
plot(y~x3,col= 8)
abline(lm(y~x3),col= 2)
cj_end <- data.frame(y, x1, x2, x3)

##  一元线性回归模型。  ##

# 模型观察。
plot(y~x1,col= 8)
abline(lm(y~x1),col= 2)

# 建立一元线性模型&相关统计量
lm.y1 <- lm(y~1+x1, cj_end)
lm.y1
lm.y1.s <- summary(lm.y1)
lm.y1.s$call
lm.y1.s$terms
lm.y1.res <- lm.y1.s$residuals           # 残差
lm.y1.s$coefficients        # 回归系数、标准误、T统计量、P值。
lm.y1.s$aliased
lm.y1.s$sigma
lm.y1.s$df                  # 自由度。
lm.y1.s$r.squared           # 拟合优度R方
lm.y1.s$adj.r.squared       # 拟合优度调整R方
lm.y1.s$fstatistic          # F统计量（没有P值）。
lm.y1.s$cov.unscaled        # 残差和X1的相关系数。（残差分析）

# 点估计&区间估计
x1 <- c(80, 90, 100, 110, 120)
y  <- c(0, 0, 0, 0, 0) 
data1 <- data.frame(x1,y)
predict(lm.y1, data1)              # 点估计。

point <- data.frame(x1= 90)
predict(lm.y1, point, interval = "prediction", level = 0.95)  # 区间预测和点估计。
length(x1)
length(y)

# 异方差检验&修正。
install.packages("lmtest")  # Breusch－Pagan检验
install.packages("car")     # ncv.test()函数
# 在回归之后，我们可以对拟合的模型采用bptest（）函数
library(foreign)
library("lmtest")
yfc.bptest <-  bptest(lm.y1)               # B-P检验结果
summary(yfc.bptest)
#gqtest(formula, point=0.5, fraction=0, 
        alternative=c("greater", "two.sided", 
        order.by=NULL, data=list())        # G-Q检验
yfc.gqtest <- gqtest(lm.y1, point = 0.5, fraction = 0, alternative = "greater", order.by = NULL, data = list())
plot(lm.y1.res)
qqnorm(lm.y1.res)
qqline(lm.y1.res)
qqplot(qt(ppoints(250), df = 5), lm.y1.res, xlab = "Q-Q plot for t dsn")
qqline(lm.y1.res)
plot(lm.y1,which=1:4)

library("car")
hccm(lm.y1)         # 计算异方差一致性的协方差矩阵。
install.packages("sandwich")
library("sandwich")
NeweyWest(lm.y1)    # 计算异方差一致性的协方差矩阵。
neweywest <- coeftest(lm.y1, vcov = NeweyWest(lm.y1))
neweywest           # 异方差和自相关稳健性Newey-West估计。
summary(lm.y1)
vcovHAC(lm.y1)
vcov(lm.y1)

lm.y1.r <- residuals(lm.y1)               #  两种修正方法。
lm.y1.xz1 <-lm(log(resid(lm.y1)^2)~x1,data=cj_end)
summary(lm.y1.xz1)
lm.y1.xz2 <-lm(y~x1,weights=1/exp(fitted(lm.y1)),data=cj_end)
summary(lm.y1.xz2)

# 序列相关检验。
library("car")
durbinWatsonTest(lm.y1.res)  # D-W统计量检验序列相关。


# 线性性假设检验。
linear.hypothesis(lm.y1, hm, rhs, type = "", white.adjust=TURE, vcov= NeweyWest(lm.y1))

# 残差分析。
lm.y1.res <- lm.y1.s$residuals           # 残差
plot(lm.y1.res)
qqnorm(lm.y1.res)
qqline(lm.y1.res)
shapiro.test(lm.y1.res)              # 当p>0.05，说明正态性。
shapiro.test(lm.y1.res)              # Shapiro-Wilk检验
install.packages("nortest")
library("nortest")
lillie.test(lm.y1.res)               # Kolmogorov-Smirnov检验
ad.test(lm.y1.res)                   # Anderson-Darling正态性检验
cvm.test(lm.y1.res)                  # Cramer-von Mises正态性检验
pearson.test(lm.y1.res)              # Pearson卡方正态性检验
sf.test(lm.y1.res)                   # Shapiro-Francia正态性检验

##  多元线性回归模型。  ##  
lm.y2 <- lm(y~x1 + x2, data = cj_end, weights = NULL,
            method = "qr",model = T, x = F, y = F, 
            qr = T, singular.ok = T,contrasts = NULL)
lm.y2
?lm
# 回归模型&统计量。
summary(lm.y2)
names(lm.y2)
lm.y2.res <- lm.y2$residuals 
lm.y2.res

# 点估计&区间估计
x1 <- c(80, 90, 100, 110, 120)
x2 <- c(80, 85, 90, 95, 100)
y  <- c(0, 0, 0, 0, 0) 
data1 <- data.frame(x1, x2, y)
predict(lm.y2, data1)              # 点估计。

point <- data.frame(x1= 90, x2=90)
predict(lm.y2, point, interval = "prediction", level = 0.95)  # 区间预测和点估计。


# 多重共线性&修正
summary(cj_end)
names(cj_end)
head(cj_end)
lm.y2.cor <- cor(cj_end[c(2,3,4)])
lm.y2.cor.k <- kappa(lm.y2.cor)
lm.y2.cor.eig <- eigen(lm.y2.cor)    #用于发现共线性强的解释变量组合#
lm.test <- lm(y~x1+x2+x3)
summary(lm.test)
step(lm.test)                      # 逐步回归法修正多重共线性。         
# step中可进行参数设置：direction=c("both","forward","backward")来选择逐步回归的方向。
# 默认both，forward时逐渐增加解释变两个数，backward则相反。






##  待进一步检验分析  ##

# 异方差检验&修正。
library(foreign)
library("lmtest")
yfc.bptest2 <-  bptest(lm.y2)               # B-P检验结果
summary(yfc.bptest2)
#gqtest(formula, point=0.5, fraction=0, 
alternative=c("greater", "two.sided", 
              order.by=NULL, data=list())        # G-Q检验
yfc.gqtest2 <- gqtest(lm.y2, point = 0.5, fraction = 0, alternative = "greater", order.by = NULL, data = list())
plot(lm.y2.res)
qqnorm(lm.y2.res)
qqline(lm.y2.res)
qqplot(qt(ppoints(250), df = 5), lm.y2.res, xlab = "Q-Q plot for t dsn")
qqline(lm.y2.res)
plot(lm.y2,which=1:4)

library("car")
hccm(lm.y2)         # 计算异方差一致性的协方差矩阵。
library("sandwich")
NeweyWest(lm.y2)    # 计算异方差一致性的协方差矩阵。
neweywest <- coeftest(lm.y2, vcov = NeweyWest(lm.y2))
neweywest           # 异方差和自相关稳健性Newey-West估计。
summary(lm.y2)
vcovHAC(lm.y2)
vcov(lm.y2)

lm.y2.r <- residuals(lm.y2)               #  两种修正方法。
lm.y2.xz1 <-lm(log(resid(lm.y2)^2)~x1+x2,data=cj_end)
summary(lm.y2.xz1)
lm.y2.xz2 <-lm(y~x1+x2,weights=1/exp(fitted(lm.y1)),data=cj_end)
summary(lm.y2.xz2)

# 序列相关检验。
library("car")
durbinWatsonTest(lm.y2.res)  # D-W统计量检验序列相关。


# 线性性假设检验。
linear.hypothesis(lm.y2, hm, rhs, type = "", white.adjust=TURE, vcov= NeweyWest(lm.y2))

# 残差分析。
lm.y2.res <- lm.y2.s$residuals           # 残差
plot(lm.y2.res)
qqnorm(lm.y2.res)
qqline(lm.y2.res)
shapiro.test(lm.y2.res)              # 当p>0.05，说明正态性。
shapiro.test(lm.y2.res)              # Shapiro-Wilk检验
library("nortest")
lillie.test(lm.y2.res)               # Kolmogorov-Smirnov检验
ad.test(lm.y2.res)                   # Anderson-Darling正态性检验
cvm.test(lm.y2.res)                  # Cramer-von Mises正态性检验
pearson.test(lm.y2.res)              # Pearson卡方正态性检验
sf.test(lm.y2.res)                   # Shapiro-Francia正态性检验











