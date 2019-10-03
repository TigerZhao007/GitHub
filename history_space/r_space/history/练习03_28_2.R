install.packages("maps")
install.packages("mapdata")
install.packages("maptools")
library("maps")
library("mapdata")
library("maptools")
x <- readShapeSpatial("E:\\rspace\\map\\bou2_4m\\bou2_4p")
par(mar=c(0,0,0,0))
plot(x,col=rainbow(n=33))
x <- rnorm(1000, 4 , 4)
par(col.lab="red")
windows()
par(mar=c(2,2,2,2))
hist(x, col.axis=2,fg=3,bg=2,col = 6,col.lab=4,col.main=5,
     cex.main=1.5,cex.lab=1,cex.axis=0.5,
     font=4,font.main=4,font.lab=4)
y <- rnorm(10, 4 , 4)
windows()
plot(ts(y,frequency = 1,start = 2000),pch=19,fg=3,
     col=2,col.lab=5, col.main=3,col.axis=8,
     cex.main=1.5,cex.lab=0.5,cex.axis=0.5,
     xlab="year",ylab="gdp",main="the series of gdp",
     lty=21,lwd=2)
plot(-4:4,-4:4,type ="p",col="blue",lty=19,pch=19)
abline(h=0)
abline(v=0)
abline(a=0,b=1)
segments(x0=2,y0=-4,x1=4,y1=-2,col = 2,lty = "dotted")
arrows(x0=-4,y0=-2,x1=-2,y1=0,length = 0.15,angle = 30,code=3)
grid(nx=3,ny=5,col = 4,lty = "dotted")
polygon(x=c(3,-2,-1,3,2),y=c(1,2,-2,2,3),col="red")
rect(xleft = c(-4,0),ybottom = c(2,-4),xright = c(-2,2),ytop = c(-4,2),col = c(2,4))
plot(-4:4,-4:4,type ="p",col="blue",lty=19,pch=19,
     main="GDP",col.main=2,fg=5,xlab="year",ylab="gdp",col.lab=3,cex.lab=0.5,
     col.axis=6)
text(-4:4,-4:4,lables=row.names(mtcars),cex=0.6,pos=4,col=2)
mtext("Added by mtext()",side = 2,line = 2,col = 5)



x <- readShapeSpatial("E:\\rspace\\map\\bou2_4m\\bou2_4p")
par(mar=c(0,0,0,0))
plot(x,col=rainbow(n=33))
library("ggxy")
install.packages("ggplot2")
library("ggplot2")
data(diamonds)
head(diamonds)
set.seed(1410)
dsmall <- diamonds[sample(nrow(diamonds),100),]
dsmall
qplot(carat, price, data=diamonds,alpha=I(1/10))
qplot(log(carat), log(price),data = diamonds)
qplot(carat,x*y*z,data=diamonds)
qplot(carat,price,data=dsmall,colour=color)
qplot(carat,price,data = dsmall,shape=cut,colour=color)
qplot(carat,price,data=dsmall,geom= c("point","smooth"),span=1)
qplot(carat,price,data=diamonds,geom= c("point","smooth"))
library(mgcv)
library(splines)
qplot(carat,price, data=dsmall,geom = c("point","smooth"),
      method= "gam", formula=y ~ s(x,bs="cs"))
qplot(carat,price, data=dsmall,geom = c("point","smooth"),
      method= "gam", formula=y ~ s(x))
qplot(carat,price, data=dsmall,geom = c("point","smooth"),
      method= "lm")

qplot(carat,price, data=dsmall,geom = c("point","smooth"),
      method= "lm", formula=y~ns(x,5))
qplot(color,price/carat,data=diamonds, geom = "jitter", alpha=I(1/5))
qplot(color,price/carat,data=diamonds, geom = "boxplot", alpha=I(1/5))
qplot(carat,data = diamonds, geom = "histogram")
qplot(carat,data = diamonds, geom = "density")
qplot(carat,data = diamonds, geom = "histogram",binwidth=1, xlim = c(0,3))
qplot(carat,data = diamonds, geom = "histogram",binwidth=.01, xlim = c(0,3))
qplot(carat,data = diamonds, geom = "density",colour=color)
qplot(carat,data = diamonds, geom = "histogram",fill=color)
qplot(color,data = diamonds, geom = "bar",fill=color)
data(date)
date
unemploy
data("economics")
head(economics)
qplot(date,unemploy/pop,data = economics,geom = "line")
nrow(economics)
qplot(date,uempmed,data = economics,geom = "line")
