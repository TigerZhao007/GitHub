library(car)
install.packages("gplots")
library("gplots")
install.packages("HH")
library("HH")
install.packages("rrcov")
library("rrcov")
#install.packages("multicomp")
#library("multicomp")
library("effects")
library("MASS")
install.packages("mvoutlier")
library("mvoutlier")
library("multcomp")
head(cholesterol)
table(cholesterol)
cholesterol$trt
attach(cholesterol)
table(trt)
aggregate(response,by=list(trt),FUN=mean)
aggregate(response,by=list(trt),FUN=sd)
fit <- aov(response ~ trt)
fit
fix(cholesterol)
summary(fit)
plotmeans(response~trt, xlab = "Treatmeant", ylab = "Response", main= "mean plot\nwith 95% CI")
detach(cholesterol)
fit.T <- TukeyHSD(fit)
par(las=2,mar=c(5,8,4,2))
plot(fit.T)
summary(fit.T)
par(mar=c(5,4,6,2))
tuk <- glht(fit, linfct = mcp(trt= "Tukey"))
tuk
summary(tuk)
plot(cld(tuk,level = .05),col="lightgrey")
fit.lm <- lm(response~trt,data = cholesterol)
summary(fit.lm)
attach(cholesterol)
bartlett.test(response~trt)
outlierTest(fit)
attach(litter)
head(litter)
table(dose)
aggregate(weight,by=list(dose),FUN=mean)
table(gesttime)
fit <- aov(weight~ gesttime+dose)
fit
summary(fit)
effect("dose",fit)
contrast <- rbind("no drug vs. drug" = c(3, -1, -1,-1))
contrast
summary(glht(fit, linfct=mcp(dose=contrast)))
fit2 <- aov(weight~gesttime*dose, data = litter)
fit2
summary(fit2)
detach(litter)
attach(ToothGrowth)
head(ToothGrowth)
ancova(weight~gesttime+dose,data= litter)
table(supp)
table(dose)
table(supp,dose)
aggregate(len,by=list(supp=supp,dose=dose),FUN=mean)
dose <- factor(dose)
fit <- aov(len~supp*dose)
fit
summary(fit)
interaction.plot(dose, supp, len, type = "b",
                 col = c("red","blue"), pch = c(16,18),
                 main= "interaction between dose and supplement type")
plotmeans(len~interaction(supp, dose, sep = " "),
          connect = list(c(1,3,5),c(2,4,6)),
          col = c("red", "darkgreen"),
          main= "Interaction plot with 95% CIs",
          xlab = "treatment and dose combination")
interaction2wt(len~supp*dose)
detach(ToothGrowth)
attach(CO2)
head(CO2)
conc <- factor(conc)
w1b1 <- subset(CO2, Treatment=='chilled')
w1b1
fit <- aov(uptake~conc*Type+Error(Plant/(conc)),w1b1)
fit
summary(fit)
par(las=2,mar=c(10,4,4,2))
with(w1b1,interaction.plot(conc,Type, uptake,
                           type = "b",col = c("red","blue"),pch = c(16,18),
                           main="Interation Plot for Plant Type and c
                           oncentration"))

boxplot(uptake~Type*conc, data = w1b1, col= (c("gold","green")),
        main= "chilled quebec and mississippi plants",
        ylab="carbon dioxide uptake rate (umol/m^2 sec)")
attach(UScereal)
shelf <- factor(shelf)
head(UScereal)
y <- cbind(calories, fat, sugars)
y
aggregate(y, by=list(shelf=shelf), FUN=mean)
cov(y)
fit <- manova(y~shelf)
fit
summary(fit)
summary.aov(fit)

center <- colMeans(y)
center
n <- nrow(y)
p <- ncol(y)
n
p
cov<- cov(y)
cov
d <- mahalanobis(y,center, cov)
d
library(ggplot2)
??ppionts
library("MASS")
coord <- qqplot(qchisq(ppoints(n),df=p),
                d, main="Q-Qplot", ylab="Maha D2")
abline(a=0,b=1)
identify(coord$x,coord$y,labels = row.names(UScereal))
library(mvoutlier)
outlines <- aq.plot(y)
outlines
library(rrcov)
Wilks.test(y, shelf, method="mcd")

library(multcomp)
levels(cholesterol$trt)
fit.aov <- aov(response~trt,data = cholesterol)
fit.aov
summary(fit.aov)
fit.lm <- lm(response~trt,data=cholesterol)
fit.lm
summary(fit.lm)
head(cholesterol)
contrasts(cholesterol$trt)
fit.lm2 <- lm(response~trt,data = cholesterol,contrasts = "contr.helmert")
fit.lm2
summary(fit.lm2)
options(contrasts=c("contr.SAS","contr.helmert"))








