library(AUC)
library(mice)

## 数据读取
cancer <- read.csv("cancer.csv", stringsAsFactors = FALSE)
cancer <- cancer[ , 1:7]

## 数据类型转换
cancer <- sapply(cancer, as.numeric)
cancer <- as.data.frame(cancer)
colnames(cancer) <- c("develop", "size", "stage", "age", "type", 
                      "Dose.I", "Dose.II")
str(cancer)

## 数据缺失值处理
imp <- mice(cancer, seed=1)
fit <- with(imp,glm(develop~size+stage+age+type+Dose.I+Dose.II, 
                    family=binomial, data = cancer))
pooled <- pool(fit)
cancer <- complete(imp,action=3)

## 数据类型转换
cancer[ , c(3, 5)] <- sapply(cancer[ , c(3, 5)], as.factor)
str(cancer)


## 模型建立和循环计算
matrix.sample <- matrix(ncol=3/4*nrow(cancer), nrow = 3000)
cancer.auc <- c(length=30)
for (i in 1:300){
  matrix.sample[i, ] <- sample(1:nrow(cancer), 3/4*nrow(cancer))
  cancer1 <- cancer[matrix.sample[i, ], ]
  cancer2 <- cancer[-matrix.sample[i, ], ]
  glm.can <- glm(develop~size+stage+age+type+Dose.I+Dose.II, 
                 family=binomial, data=cancer1)
  glm.new <- step(glm.can, trace=0)   #trace=0????ʾ????
  
  cancer.pred <- predict(glm.new, newdata = cancer2)
  develop.hat <- exp(cancer.pred)/(1+exp(cancer.pred))
  
  cancer.roc <- roc(develop.hat, as.factor(cancer2$develop))
  cancer.auc[i] <- auc(cancer.roc)
}

## 计算auc均值和T检验
mean(cancer.auc)
t.test(cancer.auc, alternative = "greater", mu=0.5)

## 绘制auc图形
hist(cancer.auc, freq = F, breaks = 40) 
lines(density(cancer.auc, bw=0.05), col="red", lwd=2)

