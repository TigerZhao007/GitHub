
## 模型结果说明
## 采用逐步回归logistic模型进行建模，通过计算测试集合训练集的AUC值，并进行检验，结果表明：此模型具有一定的预测功能。   

library(pROC)

## 数据读取
cancer <- read.csv("cancer.csv", stringsAsFactors = FALSE)
cancer <- cancer[ , 1:7]

## 数据处理
for(i in 1:length(cancer)){cancer[cancer[,i]==".",i] <- NA}
cancer <- na.omit(cancer)

for (i in c(2,4,6,7)) {cancer[,i] <- as.numeric(cancer[,i])}
for (i in c(1,3,5)) {cancer[,i] <- as.factor(cancer[,i])}

str(cancer)

##  logistic回归模型

set.seed(3)
n = 3000
result.train.auc <- result.test.auc <- c()
for (i in 1:n) {
  cancer.sample    <- sample(1:nrow(cancer), 2/3*nrow(cancer))
  cancer.train     <- cancer[cancer.sample, ]
  cancer.test      <- cancer[-cancer.sample, ]
  
  glm.model  <- glm(Cancer.development ~ ., family=binomial(link = "logit"), data=cancer.train) 
  glm.select <- step(glm.model, direction = "both", trace = 0)
  
  cancer.test.pred <- predict(glm.select, newdata = cancer.test)
  cancer.test.pred <- exp(cancer.test.pred)/(1+exp(cancer.test.pred))
  result.test.roc <- roc(cancer.test$Cancer.development, cancer.test.pred)
  result.test.auc[i] <- result.test.roc$auc 
  
  cancer.train.pred <- predict(glm.select, newdata = cancer.train)
  cancer.train.pred <- exp(cancer.train.pred)/(1+exp(cancer.train.pred))
  result.train.roc <- roc(cancer.train$Cancer.development, cancer.train.pred)
  result.train.auc[i] <- result.train.roc$auc
}

## 计算测试集合训练集的AUC值及检验，绘制相关图像。 

mean(result.test.auc)
t.test(result.test.auc, alternative = "greater", mu=0.5)
hist(result.test.auc, freq = F, breaks = 50) 
lines(density(result.test.auc, bw=0.05), col=2, lwd=2)

mean(result.train.auc)
t.test(result.train.auc, alternative = "greater", mu=0.5)
hist(result.train.auc, freq = F, breaks = 50) 
lines(density(result.train.auc, bw=0.05), col=2, lwd=2)

