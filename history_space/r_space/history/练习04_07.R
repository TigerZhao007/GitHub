head(state.x77)
states <- as.data.frame(state.x77)
attach(states)
library(coin)
spearman_test(Illiteracy~Murder,data = states,distribution=approximate(B=9999))
fisher.test(states[,c(3,6)])
head(states)
class(states)
detach(states)
library(MASS)
head(UScrime)
wilcox.test(U1~U2,data = UScrime)
kruskal.test(U1~U2,data = UScrime)
wilcoxsign_test(U1~U2,data = UScrime,distribution=approximate(B=9999))
friedman_test(U1~U2,data = UScrime,distribution=approximate(B=9999))
table(UScrime$So)
vignette("coin")
library("lmPerm")
head(women)
set.seed(1234)
fit <- lmp(weight~height,data = women,perm = "Prob", Ca=0.9)
fit
summary(fit)
fit <- lmp(weight~height+I(height^2),data = women,perm = "Prob")
summary(fit)
library(multcomp)
set.seed(1234)
fit<- aovp(response~trt, data = cholesterol, perm="Prob")
anova(fit)
head(cholesterol)
fit <- aovp(weight~gesttime+dose, data = litter,perm = "Prob")
anova(fit)
head(litter)
set.seed(1234)
fit <- aovp(len~supp*dose,data = ToothGrowth, perm = "Prob")
anova(fit)
head(ToothGrowth)


library(boot)
rsq <- function(formula,data, indices){
  d <- data[indices,]
  fit <- lm(formula,data=d)
  return(summary(fit)$r.square)
  
}
set.seed(1234)
head(mtcars)
results <- boot(data = mtcars, statistic = rsq, R=1000, formula=mpg~wt+disp)
print(results)
summary(results)
results$t0
results$t
boot.ci(results, type = c("perc", "bca"))
bs <- function(formula, data, indices){
  d <- data[indices,]
  fit <- lm(formula, data = d)
  return(coef(fit))
}
set.seed(1234)
fit <- boot(data = mtcars,statistic=bs, R=1000, formula = mpg~wt+disp)
print(fit)
fit$t0
boot.ci(fit, conf = 0.95, type = c("perc","bca"),index = c(2,3))

































