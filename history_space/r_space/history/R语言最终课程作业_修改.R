
# 一、数据读取及处理

library(pROC)
cancer <- read.csv("E:\\rspace\\cancer.csv", stringsAsFactors = FALSE)
cancer <- cancer[ , 1:7]
for (i in 1:7) {cancer[cancer[,i]==".",i] <- NA}
for (i in 1:7) {cancer[,i] <- as.numeric(cancer[,i])}
for (i in 1:7) {cancer[is.na(cancer[,i]),i] <- median(na.omit(cancer[,i]))}
for (i in c(1,3,5)) {cancer[,i] <- as.factor(cancer[,i])}

# 二、logictic回归模型建立及检验
set.seed(6)
# 设置训练集和测试集：  
cancer.sample    <- sample(1:nrow(cancer), 3/4*nrow(cancer))
cancer.train     <- cancer[cancer.sample, ]
cancer.test      <- cancer[-cancer.sample, ]
# logistic逐步回归模型：
glm.model        <- glm(Cancer.development ~ ., family=binomial(link = "logit"), data=cancer.train) 
glm.select       <- step(glm.model, direction = "both", trace = 0)
summary(glm.select)
# 模型预测结果检验  
cancer.test.pred <- predict(glm.select, newdata = cancer.test)
cancer.test.pred <- exp(cancer.test.pred)/(1+exp(cancer.test.pred))
result.test.roc  <- roc(cancer.test$Cancer.development, cancer.test.pred)
plot(result.test.roc, print.auc=TRUE, auc.polygon=TRUE, grid=c(0.1, 0.2),
     grid.col=c("green", "red"), max.auc.polygon=TRUE,
     auc.polygon.col="skyblue", print.thres=TRUE)

# 三、重复建模检验
## 1、重复建模

set.seed(6)
n = 3000
result.train.auc <- result.test.auc <- c()
for (i in 1:n) {
  cancer.sample    <- sample(1:nrow(cancer), 3/4*nrow(cancer))
  cancer.train     <- cancer[cancer.sample, ]
  cancer.test      <- cancer[-cancer.sample, ]
  glm.model  <- glm(Cancer.development ~ ., family=binomial(link = "logit"), data=cancer.train) 
  glm.select <- step(glm.model, direction = "both", trace = 0)
  cancer.test.pred <- predict(glm.select, newdata = cancer.test)
  cancer.test.pred <- exp(cancer.test.pred)/(1+exp(cancer.test.pred))
  result.test.roc <- roc(cancer.test$Cancer.development, cancer.test.pred)
  result.test.auc[i] <- result.test.roc$auc 
}


## 2、计算测试集的AUC值及检验，绘制相关图像。 

# 计算3000个模型AUC的均值，并进行单侧T检验。
mean(result.test.auc)
t.test(result.test.auc, alternative = "greater", mu=0.5)
# 绘制3000个模型AUC的直方图，并画出密度曲线。
hist(result.test.auc, freq = F, breaks = 50) 
lines(density(result.test.auc, bw=0.05), col=2, lwd=2)

