attach(mtcars)
head(mtcars)
plot(wt, mpg)
abline(lm(mpg~wt))
lines(lowess(wt,mpg))
library(car)
scatterplot(mpg~wt|cyl,span=0.75,legend.plot=T,boxplots="xy")

scatterplot(mpg~wt|cyl,span=0.8,legend.plot=T,boxplots="xy")
pairs(~mpg+disp+drat+wt)
scatterplotMatrix(~mpg+disp+drat+wt,spread=F,smoother.args=list(lty=2))
library(g1us)
install.packages("g1us")
library("TeachingDemos")
install.packages("TeachingDemos")
pairs2(~mtcars$mpg+mtcars$wt,data=mtcars)
?pairs2

library(HH)
xysplom(~mpg+wt+drat+disp)
set.seed(1234)
n<-10000
c1 <- matrix(rnorm(n,mean = 0,sd=.5), ncol = 2)
c1
c2 <- matrix(rnorm(n, mean = 3, sd=2),ncol=2)
c2
mydata <- rbind(c1,c2)
mydata <- as.data.frame(mydata)
head(mydata)
colnames(mydata)<- c("x","y")
windows()
with(mydata, plot(x,y,pch=19))
attach(mydata)
with(mydata, smoothScatter(x,y))
library("hexbin")
install.packages("hexbin")
with(mydata,{
  bin <- hexbin(x,y,xbins=50)
  plot(bin)
})

library("IDPmisc")
install.packages("IDPmisc")
ipairs(mydata)
attach(mtcars)

install.packages("scatterplot3d")
library(scatterplot3d)
scatterplot3d(wt,disp,mpg)
s3d <- scatterplot3d(wt,disp,mpg,type = "h",highlight.3d = T)
fit <- lm(mpg~wt+disp)
s3d$plane3d(fit)
library("rgl")
install.packages("rgl")
plot3d(wt,disp,mpg,size = 5)
scatter3d(wt,disp,mpg)
r <- sqrt(disp/pi)
symbols(wt,mpg,circle=r,inches = 0.3)
text(wt,mpg,rownames(mtcars),cex=.6)
plot(wt,mpg,type="b")
t1 <- subset(Orange,Tree==1)
t1
plot(t1$age,t1$circumference,type="l")
options(digits=2)
cor(mtcars)
library("corrgram")
install.packages("corrgram")
corrgram(mtcars)
corrgram(mtcars,order = T,lower.panel = panel.shade,
         upper.panel = NULL,
         text.panel = panel.txt,
         diag.panel = panel.minmax)
ftable(Titanic)
library(vcd)
mosaic(Titanic,shade = T,legend=T)











