library("fpp")
colnames(texasgas)<-c("pri","con")
texasgas

# 问题1
plot(pri,con)
lines(pri,con)

# 问题2

# 问题3
# 公式1
fit1 <- with(texasgas,lm(log(con)~1+pri))
# 公式2
texasgas1 <- with(texasgas,texasgas[pri<=60,])
texasgas2 <- with(texasgas,texasgas[pri>60,])
fit2.1 <- with(texasgas1,lm(con~1+pri))
fit2.2 <- with(texasgas2,lm(con~1+pri))
# 公式3
fit3 <- with(texasgas,lm(con~1+pri+I(pri^2)))

with(texasgas,plot(pri,con))
with(texasgas,lines(pri,exp(predict(fit1)),col=2))
with(texasgas1,lines(pri,fitted(fit2.1),col=3))
with(texasgas2,lines(pri,fitted(fit2.2),col=3))
with(texasgas,lines(pri,fitted(fit3),col=4))


# 问题4
summary(fit1)$r.squared
summary(fit2.1)$r.squared
summary(fit2.2)$r.squared
summary(fit3)$r.squared
AIC(fit1)
AIC(fit2.1)
AIC(fit2.2)
AIC(fit3)

# 问题5
x1 <- data.frame(pri=c(40,60,80,100,120))
fit1.p <- with(texasgas, exp(predict(fit1,newdata=x1,level=0.95,interval="prediction")))
x2_1 <- data.frame(pri=c(40,60))
x2_2 <- data.frame(texasgas1$pri<-c(80,100,120))
fit2.1.p <- with(texasgas1,predict(fit2.1,newdata = x2_1,level=0.95,interval="prediction"))
fit2.2.p <- with(texasgas2,predict(fit2.2,newdata = x2_2,level=0.95,interval="prediction"))
fit3.p <- with(texasgas, predict(fit3, newdata = x1,level = 0.95,interval = "prediction"))

# 问题6

with(texasgas,plot(pri,con,ylim = c(0,200),main = "fit1"))
with(texasgas,lines(pri,exp(predict(fit1,level=0.95,interval="prediction"))[,1],col=3))
with(texasgas,lines(pri,exp(predict(fit1,level=0.95,interval="prediction"))[,2],col=2))
with(texasgas,lines(pri,exp(predict(fit1,level=0.95,interval="prediction"))[,3],col=2))

with(texasgas,plot(pri,con,ylim = c(0,200),main = "fit2"))
with(texasgas1,lines(pri,predict(fit2.1,level=0.95,interval="prediction")[,1],col=3))
with(texasgas1,lines(pri,predict(fit2.1,level=0.95,interval="prediction")[,2],col=2))
with(texasgas1,lines(pri,predict(fit2.1,level=0.95,interval="prediction")[,3],col=2))
with(texasgas2,lines(pri,predict(fit2.2,level=0.95,interval="prediction")[,1],col=3))
with(texasgas2,lines(pri,predict(fit2.2,level=0.95,interval="prediction")[,2],col=2))
with(texasgas2,lines(pri,predict(fit2.2,level=0.95,interval="prediction")[,3],col=2))

with(texasgas,plot(pri,con,ylim = c(0,200),main = "fit3"))
with(texasgas,lines(pri,predict(fit3,level=0.95,interval="prediction")[,1],col=3))
with(texasgas,lines(pri,predict(fit3,level=0.95,interval="prediction")[,2],col=2))
with(texasgas,lines(pri,predict(fit3,level=0.95,interval="prediction")[,3],col=2))

# 四个值得预测区间。
plot(x1$pri,fit1.p[,1],ylim = c(0,200),type = "l",col=2,main = "fit1",xlab = "price",ylab = "con")
lines(x1$pri,fit1.p[,2],col=3)
lines(x1$pri,fit1.p[,3],col=3)

plot(x2_1$pri,fit2.1.p[,1],ylim = c(0,200),type = "l",col=2,main = "fit2",xlab = "price",ylab = "con")
lines(x1$pri,fit1.p[,2],col=3)
lines(x1$pri,fit1.p[,3],col=3)

plot(x1$pri,fit3.p[,1],ylim = c(0,200),type = "l",col=2,main = "fit3",xlab = "price",ylab = "con")
lines(x1$pri,fit3.p[,2],col=3)
lines(x1$pri,fit3.p[,3],col=3)

# 问题7
with(texasgas,cor(pri,pri^2))



















