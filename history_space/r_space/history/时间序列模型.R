##  时间序列模型。  ##

##  数据导入  ##

library(RODBC)
library(timeSeries )
library(forecast)
library(fUnitRoots)

connect <- odbcConnect("Rspace", uid = "sa", pwd = "sdk")
gdp <- sqlFetch(connect, "GDP")
head(gdp)
tail(gdp)
odbcClose(connect)
gdpy <- gdp$gdpy
tail(gdpy)

##  数据转换为时间序列数。  ##
x <- ts(gdpy, frequency = 1, start = 1952)
x
plot.ts(x, xlab="时间", ylab="元/人")
acf(x)
lnx <- log(x)
plot.ts(lnx, xlab="时间", ylab="元/人")
acf(lnx)
unitrootTest(x)                         # P=1
unitrootTest(lnx)                       # P=0.9997
sx <- sqrt(x)
plot.ts(sx, xlab="时间", ylab="元/人")

dlnx <- diff(lnx)
plot.ts(dlnx, xlab="时间", ylab="元/人")
acf(dlnx)
pacf(dlnx)
unitrootTest(dlnx)                      # P=0.0519
Box.test(dlnx, type = "Ljung-Box")

ddlnx <- diff(dlnx)
plot(ddlnx)
acf(ddlnx)
pacf(ddlnx)
unitrootTest(ddlnx)                     # P=1.769*10^(-10)
Box.test(ddlnx, type = "Ljung-Box")
write.table(x, "gdpy.txt")
# (由于ddlnx是白噪声序列，x、lnx序列不平稳，暂且放宽条件，令阿尔法为0.1， 区dlnx为分析数据序列。)

dlnx.arima <- arima(log(x), order = c(1, 1, 0))
dlnx.arima
dlnx.forecast <- forecast(dlnx.arima, h= 5, level = c(99.5))
dlnx.forecast1 <- forecast(dlnx.arima, h= 5) 
dlnx.forecast
##? x.forcast <- exp(unlist(dlnx.forecast))
##? exp(log(c(5,3)))
dlnx.forecast$x
dlnx.forecast$method
dlnx.forecast$model
dlnx.forecast$level
dlnx.forecast$mean
dlnx.forecast$lower
dlnx.forecast$upper
dlnx.forecast$series
dlnx.forecast$fitted
dlnx.forecast$residuals

##? accuracy(dlnx.forecast$mean, text)

accuracy(dlnx.forecast1)






