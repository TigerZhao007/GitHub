install.packages("AER")
data(Affairs,package="AER")
head(Affairs)
table(Affairs$affairs)
summary(Affairs)
Affairs$affairs[Affairs$affairs==0]<-0
Affairs$affairs[Affairs$affairs>=1]<-1
head(Affairs)
summary(Affairs)
Affairs$ynaffair <-factor(Affairs$affairs,levels = c(0,1),labels = c("No","Yes"))
summary(Affairs)
Affairs$affairs1<-Affairs$affairs
summary(Affairs)
Affairs$affairs1 <- transform(Affairs,affairs1=factor(affairs1))
summary(Affairs)
head(Affairs)
tail(Affairs)
Affairs<- Affairs[,-11]
ncol(Affairs)
Affairs
head(Affairs)
rm(affairs1)
table(Affairs$ynaffair)
fit.full <- glm(ynaffair~gender+age+yearsmarried
                +children+religiousness+education
                +occupation+rating,
                data = Affairs,
                family = binomial())
fit.full
summary(Affairs)
summary(fit.full)
fit.full2 <- glm(ynaffair~age+yearsmarried
                +religiousness+rating,
                data = Affairs,
                family = binomial())
summary(fit.full2)
anova(fit.full2,fit.full,test = "Chisq")
coef(fit.full2)
exp(coef(fit.full2))
testdata1<- data.frame(rating=c(1,2,3,4,5),
                       age=mean(Affairs$age),
                       yearsmarried=mean(Affairs$yearsmarried),
                       religiousness=mean(Affairs$religiousness))
testdata1
testdata1$Prob <- predict(fit.full2,newdata = testdata1, type = "response")
testdata2<- data.frame(rating=mean(Affairs$rating),
                       age=seq(17,57,10),
                       yearsmarried=mean(Affairs$yearsmarried),
                       religiousness=mean(Affairs$religiousness))
testdata2$Prob <- predict(fit.full2,newdata = testdata2, type = "response")
testdata2
options(digits = 3)
deviance(fit.full2)/df.residual(fit.full2)
fit1 <- glm(ynaffair~age+yearsmarried+religiousness+
              rating,family = binomial(),data = Affairs)
fit2 <- glm(ynaffair~age+yearsmarried+religiousness+
              rating,family = quasibinomial(),data = Affairs)
pchisq(summary(fit2)$dispersion*fit1$df.residual,
       fit1$df.residual,lower=F)
install.packages("robust")
library("robust")
data("breslow.dat")
head(breslow.dat)
names(breslow.dat)
summary(breslow.dat)
opar <- par(no.readonly = T)
par(mfrow=c(1,2))
attach(breslow.dat)
hist(sumY,breaks = 20, xlab = "Seizure Count", main = "Distribution of Seizure")
boxplot(sumY~Trt,xlab="teratment", main= "Group comparious")
par(opar)
fit <- glm(sumY~Base+Age+Trt, data = breslow.dat,family = poisson())
summary(fit)
coef(fit)
exp(coef(fit))
options(digits = 3)
deviance(fit)/df.residual(fit)
library(qcc)
install.packages("qcc")
library(qcc)
qcc.overdispersion.test(breslow.dat$sumY,type = "poisson")
fit.od <- glm(sumY~Base+Age+Trt,data = breslow.dat, family = quasipoisson())
summary(fit.od)
fit1 <- glm(sumY~Base+Age+Trt, data = breslow.dat, offset = log(time),family = poisson())
