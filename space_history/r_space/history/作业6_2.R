plastics
pl <- ts(plastics,frequency = 12)
pl

# 题1
plot(pl)

# 题2
seasonplot(pl)
monthplot(pl)
fit1 <- stl(pl,s.window = "period")   # 加法模型
fit1$time.series[1:12,1]
plot(fit1)
fit2 <- decompose(pl, type ="multiplicative")   # 乘法模型
plot(fit2)
pl.s <- fit2$seasonal
pl.s[1,]
# 题3

# 题4
pl1 <- pl-fit1$time.series[1,]
pl1
plot(pl1)

# 题5
pl2 <-pl
pl2[1] <- 500

library(forecast)
fit <- stl(pl, t.window=15, s.window="periodic", robust=TRUE)
eeadj <- seasadj(fit)
plot(naive(eeadj), xlab="New orders index",
     main="Naive forecasts of seasonally adjusted data")

fcast <- forecast ( fit,method = "naive" )
plot ( fcast,ylab = "New orders index" )
install.packages("fma")
