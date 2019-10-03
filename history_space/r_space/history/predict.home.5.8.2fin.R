install.packages("fpp")
library("fpp")
attach(texasgas)
plot(texasgas)
#指数模型
lnc <- log(consumption)
lm.tex1 <- lm(lnc~price, data=texasgas)
summary(lm.tex1)
#分段模型
p1 <- pmax(texasgas$price-60,0)
lm.tex2 <- lm(consumption ~ price + p1, data=texasgas)
summary(lm.tex2)
#多项式模型
lm.tex3 <- lm(consumption~price+I(price^2))
summary(lm.tex3)

#保存图片为PNG格式
png(file = "exercise5.8.2.picture3.png")
plot(texasgas)
#画指数图
p2 <- seq(min(price), max(price), length.out = 200)
lnc1 <- predict(lm.tex1, data.frame(price=p2))
consumption1 <- exp(lnc1)
lines(p2, consumption1, col="red")
#画分段图
x <- 30:150; z <- pmax(x-60,0)
fcast2 <- forecast(lm.tex2, 
                   newdata=data.frame(price=x,
                                      p1=z))
lines(x, fcast2$mean,col="green")
#画多项式
consumption2 <- predict(lm.tex3, data.frame(price=p2))
lines(p2, consumption2, col="blue")
#加右上角标识
legend("topright", legend=c("指数模型", "分段模型", "多项式模型"),
       lty=1, col=c("red", "green", "blue"))
dev.off()

#调用系数 系数数据框
coeff <- data.frame(
  a = c(lm.tex1$coefficients[1], lm.tex2$coefficients[1],
        lm.tex3$coefficients[1]),
  b = c(lm.tex1$coefficients[2], lm.tex2$coefficients[2],
        lm.tex3$coefficients[2]),
  c = c(NA, lm.tex2$coefficients[3], lm.tex3$coefficients[3])
)
rownames(coeff) <- c("lm.tex1", "lm.tex2", "lm.tex3")
coeff

#残差矩阵
#指数模型的残差不能直接函数得到，需要手动算e指数的残差
lnc2 <- predict(lm.tex1, data.frame(price=price))
consumption2 <- exp(lnc2)   
res1 <- consumption-consumption2
res2 <- residuals(lm.tex2)
res3 <- residuals(lm.tex3)
res <- matrix(c(res1, res2, res3), ncol = 3)
colnames(res) <- c("lm.tex1", "lm.tex2", "lm.tex3")
res

#残差平方和向量
sse <- c(sse.lm.tex1 = sum(res1^2),
         sse.lm.tex2 = deviance(lm.tex2),
         sse.lm.tex3 = deviance(lm.tex3)
         )
sse

#残差图
png(file = "exercise5.8.2.picture2.png")
old.par <- par(mfrow = c(3, 1))
plot(res1);plot(res2);plot(res3)
par(old.par)
dev.off()

# AIC(lm.tex1)
# AIC=2k+nln(SSE/n)
# l=-(n/2)*ln(2*pi)-(n/2)*ln(sse/n)-n/2
# -2*log-likelihood + k*npar,
# aicfun <- function(n, sse, npar, k=2){
#   l <- -(n/2)*log(2*pi)-(n/2)*log(sse/n)-n/2
#   -2*log(-l)+k*npar
# }
#AIC=n*ln(2*pi)+n*ln(sse/n)+n+2(p+1)
# aicfun <- function(n, sse, p)
#   n*log(2*pi)+n*log(sse/n)+n+2*(p+1)

#R^2&AIC数据框
#AIC计算公式按照公式自定义
aic.fun <- function(N, SSE, k){
  N*log(SSE/N)+2*(k+2)
}
aic1 <- aic.fun(20, sse[1], 2)
aic2 <- aic.fun(20, sse[2], 2)
aic3 <- aic.fun(20, sse[3], 2)

r_aic <- data.frame(
  r.sqrt = c(summary(lm.tex1)$r.squared,
             summary(lm.tex2)$r.squared,
             summary(lm.tex3)$r.squared),
  aic    = c(aic1, aic2, aic3)
  )
rownames(r_aic) <- c("lm.tex1", "lm.tex2", "lm.tex3")
r_aic

#预测数值
price1 <- c(40, 60, 80, 100, 120)
pre.2 <- predict(lm.tex2, data.frame(price=price1, 
                                     p1=pmax(price1-60,0)))
names(pre.2) <- c(40, 60, 80, 100, 120)
pre.2
# 分段函数预测应当作两个自变量，即多元函数的预测
# pre <- data.frame(
#   lm.tex1 = exp(predict(lm.tex1, data.frame(price=price1))),
#   lm.tex2 = predict(lm.tex2, data.frame(price=price1,
#                                         p1=pmax(price1-60,0))),
#   lm.tex3 = predict(lm.tex3, data.frame(price=price1))
# )
# pre
lm1.pred <- exp(predict(lm.tex1, data.frame(price=p2),
                    interval="prediction", level=0.95))
lm2.pred <- predict(lm.tex2, 
                    data.frame(price=p2, p1=pmax(p2-60,0)),
                    interval="prediction", level=0.95)
lm3.pred = predict(lm.tex3, data.frame(price=p2),
                   interval="prediction", level=0.95)
plot(texasgas)
lines(p2, lm1.pred[ , 2], col=1)
lines(p2, lm1.pred[ , 3], col=1)
lines(p2, lm2.pred[ , 2], col=2)
lines(p2, lm2.pred[ , 3], col=2)
lines(p2, lm3.pred[ , 2], col=3)
lines(p2, lm3.pred[ , 3], col=3)

lm1.pred <- exp(predict(lm.tex1, data.frame(price=p2),
                        interval="prediction", level=0.05))
lm2.pred <- predict(lm.tex2, 
                    data.frame(price=p2, p1=pmax(p2-60,0)),
                    interval="prediction", level=0.05)
lm3.pred = predict(lm.tex3, data.frame(price=p2),
                   interval="prediction", level=0.05)
plot(texasgas)
lines(p2, lm1.pred[ , 2], col=1)
lines(p2, lm1.pred[ , 3], col=1)
lines(p2, lm2.pred[ , 2], col=2)
lines(p2, lm2.pred[ , 3], col=2)
lines(p2, lm3.pred[ , 2], col=3)
lines(p2, lm3.pred[ , 3], col=3)