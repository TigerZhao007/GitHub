library(VIM)
library(mice)
head(sleep)
summary(sleep)
nrow(sleep)
ncol(sleep)
dim(sleep)
sleep[is.na(sleep),]
which(is.na(sleep$Sleep))
md1 <- md.pattern(sleep)
aggr(sleep, prop=F,numbers=T)
aggr(sleep, prop=T,numbers=T)
matrixplot(sleep)
###scattMiss(as.data.frame(c(sleep$NonD,sleep$Sleep)))
marginplot(sleep[c("Gest","Dream")],pch = c(20),col = c(1,2,4))

x<- as.data.frame(abs(is.na(sleep)))
x
is.na(sleep)
abs(is.na(sleep))
y <- x[which(apply(x, 2, sum)>0)]
head(y)
dim(y)
cor(y)
options(digits = 2)
cor(sleep, y, use = "pairwise.complete.obs")
head(y)
fit <- lm(Dream~Span+Gest, data = na.omit(sleep))
summary(fit)
fit <- lm(Dream~Span+Gest, data = sleep)
imp <- mice(sleep, seed = 1234)
fit <- with(imp, lm(Dream~Span+Gest))
fit
summary(fit)
pooled <- pool(fit)
pooled
summary(pooled)
imp
imp$imp$Dream
dataset3 <- complete(imp,action = 3)
dataset3
dim(dataset3)
which(!complete.cases(dataset3))
which(!complete.cases(sleep))
dim(sleep)

