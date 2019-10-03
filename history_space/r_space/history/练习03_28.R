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
w <- data.frame(gdpy= gdp$gdpy, gdpy.mean= gdp$人均GDPy, people= gdp$总人口数)
head(w)
x <- ts(w[1:3], start = c(1952, 1),frequency = 1)
x
plot(x)
plot(x, ylab= "year", type="o", pch=16, nc=1, main="")
title("NZR")
plot(x1, ylab= "year", type="o", pch=16, plot.type= "single" , nc=1, main="",lty=1:3,col=1:3)
legend("topleft", c("mmm", "nnn", "ppp"),lty = 1:3, col = 1:3)
x1 <- x[,1]
x1

##  AR(1)
par(mfrow=c(4,3))
ts.plot(x1,type="o",lty=1,col=2,main="the series of x1", xlab= "year", ylab= "gdpy")
acf(x1, col= "blue")
pacf(x1, col= "blue")
ts.plot(log(x1),type="o",lty=1,col=2,main="the series of lnx1", xlab= "year", ylab= "gdpy")
acf(log(x1), col= "blue")
pacf(log(x1), col= "blue")
ts.plot(diff(x1),type="o",lty=1,col=2,main="the series of dx1", xlab= "year", ylab= "gdpy")
acf(diff(x1), col= "blue")
pacf(diff(x1), col= "blue")
ts.plot(diff(log(x1)),type="o",lty=1,col=2,main="the series of dlnx1", xlab= "year", ylab= "gdpy")
acf(diff(log(x1)), col= "blue")
pacf(diff(log(x1)), col= "blue")

dev.off()
windows()


set.seed(101)
x=NULL
for (i in 1:200) {
  x <- c(x, 0.5-0.3*i+rnorm(1))
  
}
par(mfrow=c(2,2))
ts.plot(x)
acf(x)
ts.plot(diff(x))
acf(diff(x))
dev.off()


## MA(2)
set.seed(6301)
windows()
par(mfrow=c(1,3))
plot(pacf(arima.sim(n=200, list(ar=c(0.5, 0.3))),plot = F),
     ylab="pacf", type="h", pch=16, 
     main=expression(paste("AR(2):",phi[1]==0.5, ",",phi[2]==0.3)))
plot(pacf(arima.sim(n=200, list(ar=c(0.5, -0.5))),plot = F),
     ylab="pacf", type="o", pch=16, 
     main=expression(paste("AR(2):",phi[1]==0.5, ",",phi[2]==-0.5)))
plot(pacf(arima.sim(n=200, list(ar=c(-0.75, -0.3))),plot = F),
     ylab="pacf", type="o", pch=16, 
     main=expression(paste("AR(2):",phi[1]==-0.75, ",",phi[2]==--0.3)))

set.seed(6301)
windows()
par(mfrow=c(1,3))
pacf(arima.sim(n=200, list(ar=c(0.5, 0.3))),
     ylab="pacf", type="h", pch=16, 
     main=expression(paste("AR(2):",phi[1]==0.5, ",",phi[2]==0.3)))
pacf(pacf(arima.sim(n=200, list(ar=c(0.5, -0.5))),plot = F),
     ylab="pacf", type="o", pch=16, 
     main=expression(paste("AR(2):",phi[1]==0.5, ",",phi[2]==-0.5)))
pacf(pacf(arima.sim(n=200, list(ar=c(-0.75, -0.3))),plot = F),
     ylab="pacf", type="o", pch=16, 
     main=expression(paste("AR(2):",phi[1]==-0.75, ",",phi[2]==--0.3)))


##  ARMA(1,1)&ARIMA(1,1,1)
set.seed(6301)
windows()
par(mfrow=c(2,2))
plot(arima.sim(n=200,list(ar=0.4, ma=0.5)),ylab="x", type="o", pch=16,
     main=expression(paste("ARMA(1,1):",phi== 0.4, theta==0.5)))
plot(arima.sim(n=200,list(ar=-0.4, ma=-0.5)),ylab="x", type="o", pch=16,
     main=expression(paste("ARMA(1,1):",phi== -0.4, theta==-0.5)))
plot(arima.sim(n=200,list(order=c(1,1,1), ar=0.4, d=1, ma=0.5)),ylab="x", type="o", pch=16,
     main=expression(paste("ARMA(1,1):",phi== 0.4, theta==0.5)))
plot(arima.sim(n=200,list(order=c(1,1,1), ar=-0.4, d=1, ma=-0.5)),ylab="x", type="o", pch=16,
     main=expression(paste("ARMA(1,1):",phi== -0.4,theta==-0.5)))
dev.off()


plot(x1,main="GDPY", xlab="time", ylab="gdpy",col="green",pch=16,type="o")
ts.plot(diff(x1),main=expression(paste(nabla,"(x)")))
ts.plot(diff(diff(x1,12)),main=expression(paste(nabla[12],"(x)")))
ts.plot(diff(diff(x1,12)),main=expression(paste(nabla,nabla[12],"(x)")))

x2 <- ts(x[,3],frequency = 12,start = 2000)
x2
bstl <- stl(x2,"per")
plot(bstl,main= "STl")
b1 <- HoltWinters(x2,seasonal = "multiplicative")
plot(b1$fitted,main="HW")
e <- b1$x-b1$fitted[,1]
plot(e)
summary(b1$fitted)
b1$fitted
y <- predict(b1,n.ahead = 12, prediction.interval = F)
y
plot(x1, ylim=range(c(x1,y)),lty=3,lwd=2)
lines(y,lwd=2)

x3 <- window(x2, end=c(2003,12),frequency=12)
x3
a <- HoltWinters(x3,seasonal = "multiplicative")
y <- predict(a, n.ahead = 12, prediction.interval = F)
y
plot(x2, ylim = range(c(x2,y)),lty=3, lwd=2)
legend("topleft",c("O","P"),lty = c(2,1),lwd = 2)
lines(y,lwd=2)
y1 <- predict(a,n.ahead = 12,prediction.interval = T)
plot(a,y)
y
a
x2


### 理论AR、MA模型&模拟AR、MA模型。####
windows()
dev.off()
par(mfrow=c(3,2))
plot(ARMAacf(ma=c(.5,-.4),lag.max = 18,pacf = F),type="h", ylab="AFC",
     main="Exact ACF for MA(0.5,-0.4) MA(2)")
abline(h=0)
acf(arima.sim(n=63,list(ma=c(.5,-0.4)),sd=sqrt(0.2)),
    main="ACF of Simulated MA(0.5, -0.4) MA(2)")

plot(ARMAacf(ar=c(-.5,.4),lag.max = 18,pacf = T),type="h", ylab="PAFC",
     main="Exact PACF for AR(-0.5,0.4) AR(2)")
abline(h=0)
pacf(arima.sim(n=63,list(ar=c(-.5,0.4)),sd=sqrt(0.2)),
    main="PACF of Simulated AR(-0.5, 0.4) AR(2)")

plot(ARMAacf(ar=c(-.3, .4) , ma=c(-.3,.25),lag.max = 18,pacf = F),type="h", ylab="AFC",
     main="Exact ACF for ARMA(ar=(-0.3, 0.4),ma=(-0.3,0.25)) ARMA(2,2)")
abline(h=0)
acf(arima.sim(n=63,list(ar=c(-.3, .4) , ma=c(-.3,.25)),sd=sqrt(0.2)),
    main="ACF of Simulated ARMA(ar=(-0.3, 0.4),ma=(-0.3,0.25)) ARMA(2,2)")



x4 <- diff(log(x1))
plot.ts(x4)
x4
par(mfrow = c(1,2))
acf(x4,col=2,xlab="year",ylab="ACF",main="the ACF of dlnGDPy")
pacf(x4,col=2,xlab="year",ylab="PACF",main="the PACF of dlnGDPy")
dev.off()
library(TSA)
x4.res <- armasubsets(y=x4, nar = 15, nma = 15, y.name = 'test',ar.method = 'ols')
plot(x4.res)
x4.res$nbest
colors()
arma.1.7 <- arima(x=x4,order = c(1,0,7))
arma.1.0 <-arima(x=x4,order = c(1,0,0))
summary(arma.1.7)
arma.1.7$model
arma.1.7$coef
arma.1.7$arma
arma.1.7$sigma2
arma.1.7$var.coef
arma.1.7$mask
arma.1.7$loglik
arma.1.7$aic
arma.1.7$residuals
arma.1.7$call
arma.1.7$series
arma.1.7$codea
arma.1.7$n.cond
arma.1.7$nobs
arma.1.7$model

library(forecast)
library(portes)
par(mfrow=c(2,2))
plot(gvtest(arma.1.7,1:30)[,4],main="GVT",ylab="P-value",xlab="lag",pch=16,ylim=c(0,1))
abline(h=0.05,lty=2)
plot(LjungBox(arma.1.7,1:30)[,4],main="LBT",ylab="P-value",xlab="lag",pch=16,ylim=c(0,1))
abline(h=0.05,lty=2)
acf(arma.1.7$residuals, main= "ACF of residual",lag.max = 30)
plot(arma.1.7$residuals,type="o", ylab="Residual",pch=16)
title("Residual series")
abline(h=0,lty=2)



###  自动拟合ＡＲＩＭＡ模型。
ra2 <- auto.arima(x1,ic="bic")
ra2$coef
ra2

par(mfrow=c(2,2))
plot(gvtest(ra2$residuals,1:30)[,4],main="GVT",ylab="P-value",xlab="lag",pch=16,ylim=c(0,1))
abline(h=0.05,lty=2)
plot(LjungBox(ra2$residuals,1:30)[,4],main="LBT",ylab="P-value",xlab="lag",pch=16,ylim=c(0,1))
abline(h=0.05,lty=2)
acf(ra2$residuals, main= "ACF of residual",lag.max = 30)
plot(ra2$residuals,type="o", ylab="Residual",pch=16)
title("Residual series")
abline(h=0,lty=2)
dev.off()





















