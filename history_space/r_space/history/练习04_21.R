install.packages("fpp")
library("fpp")
attach(texasgas)
colnames(texasgas)<-c("pri","con")
texasgas
plot(pri,con)
lines(pri,con)

# 公式1
fit1 <- lm(log(con)~1+pri)

# 公式2
##if(pri<=60) fit2<- lm(con~1+pri)
##else fit2 <- lm(con~1+pri)
texasgas1 <- texasgas[pri<=60,]
texasgas2 <- texasgas[pri>60,]
fit2.1 <- lm(texasgas1$con~1+texasgas1$pri)
fit2.2 <- lm(texasgas2$con~1+texasgas2$pri)

# 公式3
fit3 <- lm(con~1+pri+I(pri^2))

summary(fit1)
summary(fit2.1)
summary(fit2.2)
summary(fit3)
AIC(fit1)
AIC(fit2.1)
AIC(fit2.2)
AIC(fit3)

x1 <- data.frame(pri=c(40,60,80,100,120))
fit1.p <- exp(predict(fit1,newdata = x1,level=0.95,interval="prediction"))
detach(texasgas)
attach(texasgas1)
x2_1 <- data.frame(pri=c(40,60))
x2_2 <- data.frame(texasgas1$pri<-c(80,100,120))
fit2.1.p <- predict(fit2.1,newdata = x2_1,level=0.95,interval="prediction")
fit2.2.p <- predict(fit2.2,newdata = x2_2,level=0.95,interval="prediction")
fit3.p <- predict(fit3, newdata = x1,level = 0.95,interval = "prediction")


