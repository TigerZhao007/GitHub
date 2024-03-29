# 6.1   	实例：利用数据集women建立简单线性回归模型
# 线性回归模型
data(women)
lm.model <- lm( weight ~ height - 1, data = women)  # 建立线性回归模型
summary(lm.model)  # 输出模型的统计信息
coefficients(lm.model)  # 输出参数估计值
confint(lm.model, parm = "speed", level = 0.95)  # parm缺省则计算所有参数的置信区间
fitted(lm.model)  # 列出拟合模型的预测值
anova(lm.model)  # 生成一个拟合模型的方差分析表
vcov(lm.model)  # 列出模型参数的协方差矩阵
residuals(lm.model)  # 列出模型的残差
AIC(lm.model)  # 输出AIC值
par(mfrow = c(2, 2)) 
plot(lm.model)  # 生成评价拟合模型的诊断图



# 6.1   	实例：结婚时间、教育、宗教等其它变量对出轨次数的影响
# 逻辑回归模型
data(Affairs, package = "AER")
# 由于变量affairs为正整数，为了进行Logistic回归先要将其转化为二元变量。
Affairs$ynaffair[Affairs$affairs > 0] <- 1
Affairs$ynaffair[Affairs$affairs == 0] <- 0
Affairs$ynaffair <- factor(Affairs$ynaffair, levels = c(0, 1), 
                           labels = c("No", "Yes"))
# 建立Logistic回归模型
model.L <- glm(ynaffair ~ age + yearsmarried + religiousness + rating, 
               data = Affairs, family = binomial (link = logit))
summary(model.L)  # 展示拟合模型的详细结果
predictdata <- data.frame(Affairs[, c("age", "yearsmarried", "religiousness", "rating")])
# 由于拟合结果是给每个观测值一个概率值，下面以0.4作为分类界限
predictdata$y <- (predict(model.L, predictdata, type = "response") > 0.4)
predictdata$y[which(predictdata$y == FALSE)] = "No"  # 把预测结果转换成原先的值(Yes或No)
predictdata$y[which(predictdata$y == TRUE)] = "Yes" 
confusion <- table(actual = Affairs$ynaffair, predictedclass = predictdata$y)  # 混淆矩阵
confusion 
(sum(confusion) - sum(diag(confusion))) / sum(confusion)  # 计算错判率



# 6.1  	实例：对美国妇女的平均身高和体重数据进行Bonferroni离群点检验
#  Bonferroni离群点检验
library(car)
fit <- lm(weight ~ height, data = women)  # 建立线性模型
outlierTest(fit)   # Bonferroni离群点检验
women[10, ] <- c(70, 200)  # 将第10个观测的数据该成height = 70，weight = 200
fit <- lm(weight ~ height, data = women)
outlierTest(fit)  # Bonferroni离群点检验



# 6.1 	实例：对代码清单 6 1中的模型lm.model的误差做自相关性检验
# 检验误差项的自相关性
durbinWatsonTest(lm.model)



# 6.1 	实例：使用数据集freeny建立逻辑回归模型，并进行自变量选择
# 自变量选择
Data <-  freeny
lm <- lm(y ~ ., data = Data)  # logistic回归模型
summary(lm)
lm.step <- step(lm, direction = "both")  # 一切子集回归
summary(lm.step)
lm.step <- step(lm, direction = "forward")  # 前进法
summary(lm.step)
lm.step <- step(lm, direction = "backward")  # 后退法
summary(lm.step)

# 6.2.1   C4.5决策树预测客户是否流失
# C4.5决策树
# 设置工作空间
setwd("F:/数据及程序/第6章/示例程序")  # 设置工作空间
Data <- read.csv("./data/Telephone.csv")  # 读入数据
Data[, "流失"] <- as.factor(Data[, "流失"])  # 将目标变量转换成因子型
set.seed(1234)  # 设置随机种子

# 数据集随机抽70%定义为训练数据集，30%为测试数据集
ind <- sample(2, nrow(Data), replace = TRUE, prob = c(0.7, 0.3))
traindata <- Data[ind == 1, ]
testdata <- Data[ind == 2, ]

# 建立决策树模型预测客户是否流失
library(party)  # 加载决策树的包
ctree.model <- ctree(流失 ~ ., data = traindata)  # 建立C4.5决策树模型
plot(ctree.model, type = "simple")  # 输出决策树图

# 预测结果
train_predict <- predict(ctree.model)  # 训练数据集
test_predict <- predict(ctree.model, newdata = testdata)  # 测试数据集

# 输出训练数据的分类结果
# 输出训练数据的分类结果
train_predictdata <- cbind(traindata, predictedclass = train_predict) 
#输出训练数据的混淆矩阵
(train_confusion <- table(actual = traindata$流失, predictedclass = train_predict) )
# 输出测试数据的分类结果
test_predictdata <- cbind(testdata, predictedclass = test_predict)
# 输出测试数据的混淆矩阵
(test_confusion <- table(actual = testdata$流失, predictedclass = test_predict))



# 6.2.2     CART决策树预测客户是否流失
# CART决策树
setwd("F:/数据及程序/第6章/示例程序")  # 设置工作空间
Data <- read.csv("./data/telephone.csv")  # 读入数据
Data[, "流失"] <- as.factor(Data[, "流失"])  # 将目标变量转换成因子型
set.seed(1234)  # 设置随机种子

# 数据集随机抽70%定义为训练数据集，30%为测试数据集
ind <- sample(2, nrow(Data), replace = TRUE, prob = c(0.7, 0.3))
traindata <- Data[ind == 1, ]
testdata <- Data[ind == 2, ]

# 建立决策树模型预测客户是否流失
library(tree)  # 加载决策树的包
tree.model <- tree(流失 ~ ., data = traindata)  # 建立CART决策树模型
plot(tree.model, type = "uniform")  # 输出决策树图
text(tree.model)

# 预测结果
train_predict <- predict(tree.model, type = "class")  # 训练数据集
test_predict <- predict(tree.model, newdata = testdata, type = "class")  # 测试数据集

# 输出训练数据的分类结果
train_predictdata <- cbind(traindata, predictedclass = train_predict) 
# 输出训练数据的混淆矩阵
(train_confusion <- table(actual = traindata$流失, predictedclass = train_predict)) 
# 输出测试数据的分类结果
test_predictdata <- cbind(testdata, predictedclass = test_predict)
# 输出测试数据的混淆矩阵
(test_confusion <- table(actual = testdata$流失, predictedclass = test_predict))




# 6.2.3       C5.0决策树预测客户是否流失
# C5.0决策树
setwd("F:/数据及程序/第6章/示例程序")  # 设置工作空间
Data <- read.csv("./data/telephone.csv")  # 读入数据
Data[, "流失"] <- as.factor(Data[, "流失"])  # 将目标变量转换成因子型
set.seed(1234)  # 设置随机种子

# 数据集随机抽70%定义为训练数据集，30%为测试数据集
ind <- sample(2, nrow(Data), replace = TRUE, prob = c(0.7, 0.3))
traindata <- Data[ind == 1, ]
testdata <- Data[ind == 2, ]

# 建立决策树模型预测客户是否流失
library(C50)  # 加载决策树的包
c50.model <- C5.0(流失 ~ ., data = traindata)  # 建立C5.0决策树模型
plot(c50.model)  # 输出决策树图

# 预测结果
train_predict <- predict(c50.model, newdata = traindata, type = "class")  # 训练数据集
test_predict <- predict(c50.model, newdata = testdata, type = "class")  # 测试数据集

# 输出训练数据的分类结果
train_predictdata <- cbind(traindata, predictedclass = train_predict) 
# 输出训练数据的混淆矩阵
(train_confusion <- table(actual = traindata$流失, predictedclass = train_predict)) 
# 输出测试数据的分类结果
test_predictdata <- cbind(testdata, predictedclass = test_predict)
# 输出测试数据的混淆矩阵
(test_confusion <- table(actual = testdata$流失, predictedclass = test_predict))

# 6.3     BP神经网络算法预测客户是否流失
# BP神经网络
setwd("F:/数据及程序/第6章/示例程序")  # 设置工作空间
Data <- read.csv("./data/telephone.csv")  # 读入数据
Data[, "流失"] <- as.factor(Data[, "流失"])  # 将目标变量转换成因子型
set.seed(1234)  # 设置随机种子
# 数据集随机抽70%定义为训练数据集，30%为测试数据集
ind <- sample(2, nrow(Data), replace = TRUE, prob = c(0.7, 0.3))
traindata <- Data[ind == 1, ]
testdata <- Data[ind == 2, ]

# BP神经网络建模
library(nnet) #加载nnet包
# 设置参数
size <- 10  # 隐层节点数为10
decay <- 0.05  # 权值的衰减参数为0.05
nnet.model <- nnet(流失 ~ ., traindata, size = size, decay = decay)  # 建立BP神经网络模型
summary(nnet.model)  # 输出模型概要

# 预测结果
train_predict <- predict(nnet.model, newdata = traindata, type = "class")  # 训练数据集
test_predict <- predict(nnet.model, newdata = testdata, type = "class")  # 测试数据集

# 输出训练数据的分类结果
train_predictdata <- cbind(traindata, predictedclass = train_predict) 
# 输出训练数据的混淆矩阵
(train_confusion <- table(actual = traindata$流失, predictedclass = train_predict)) 
# 输出测试数据的分类结果
test_predictdata <- cbind(testdata, predictedclass = test_predict)
# 输出测试数据的混淆矩阵
(test_confusion <- table(actual = testdata$流失, predictedclass = test_predict))


# 6.4      KNN算法预测客户是否流失
# KNN算法
setwd("F:/数据及程序/第6章/示例程序")  # 设置工作空间
Data <- read.csv("./data/telephone.csv")  # 读入数据
Data[, "流失"] <- as.factor(Data[, "流失"])  # 将目标变量转换成因子型
set.seed(1234)  # 设置随机种子

# 数据集随机抽70%定义为训练数据集，30%为测试数据集
ind <- sample(2, nrow(Data), replace = TRUE, prob = c(0.7, 0.3))
traindata <- Data[ind == 1, ]
testdata <- Data[ind == 2, ]

# 使用kknn函数建立knn分类模型 
library(kknn)  # 加载kknn包
# knn分类模型
kknn.model <- kknn(流失 ~ ., train = traindata, test = traindata, k = 5)  # 训练数据
kknn.model2 <- kknn(流失 ~ ., train = traindata, test = testdata, k = 5)  # 测试数据
summary(kknn.model)  # 输出模型概要
# 预测结果
train_predict <- predict(kknn.model)  # 训练数据
test_predict <- predict(kknn.model2)  # 测试数据
# 输出训练数据的混淆矩阵
(train_confusion <- table(actual = traindata$流失, predictedclass = train_predict)) 
# 输出测试数据的混淆矩阵
(test_confusion <- table(actual = testdata$流失, predictedclass = test_predict))

# 使用knn函数建立knn分类模型
library(class)  # 加载class包
# 建立knn分类模型
knn.model <- knn(traindata, testdata, cl = traindata[, "流失"]) 
# 输出测试数据的混淆矩阵
(test_confusion = table(actual = testdata$流失, predictedclass = knn.model))

# 使用train函数建立knn分类模型
library(caret)  # 加载caret包
# 建立knn分类模型
train.model <- train(traindata, traindata[, "流失"], method = "knn")
# 预测结果
train_predict <- predict(train.model, newdata = traindata)      #训练数据集
test_predict <- predict(train.model, newdata = testdata)       #测试数据集
# 输出训练数据的混淆矩阵
(train_confusion <- table(actual = traindata$流失, predictedclass = train_predict))
# 输出测试数据的混淆矩阵
(test_confusion <- table(actual = testdata$流失, predictedclass = test_predict))

# 6.5     朴素贝叶斯算法预测客户是否流失
# 朴素贝叶斯分类算法
setwd("F:/数据及程序/第6章/示例程序")  # 设置工作空间
Data <- read.csv("./data/telephone.csv")  # 读入数据
Data[, "流失"] <- as.factor(Data[, "流失"])  # 将目标变量转换成因子型
set.seed(1234)  # 设置随机种子
# 数据集随机抽70%定义为训练数据集，30%为测试数据集
ind <- sample(2, nrow(Data), replace = TRUE, prob = c(0.7, 0.3))
traindata <- Data[ind == 1, ]
testdata <- Data[ind == 2, ]

# 使用naiveBayes函数建立朴素贝叶斯分类模型
library(e1071)  # 加载e1071包
naiveBayes.model <- naiveBayes(流失 ~ ., data = traindata)  # 建立朴素贝叶斯分类模型
# 预测结果
train_predict <- predict(naiveBayes.model, newdata = traindata)  # 训练数据集
test_predict <- predict(naiveBayes.model, newdata = testdata)  # 测试数据集
# 输出训练数据的分类结果
train_predictdata <- cbind(traindata, predictedclass = train_predict) 
# 输出训练数据的混淆矩阵
(train_confusion <- table(actual = traindata$流失, predictedclass = train_predict)) 
# 输出测试数据的分类结果
test_predictdata <- cbind(testdata, predictedclass = test_predict)
# 输出测试数据的混淆矩阵
(test_confusion <- table(actual = testdata$流失, predictedclass = test_predict))

# 使用NaiveBayes函数建立朴素贝叶斯分类模型
library(klaR)  # 加载klaR包
NaiveBayes.model <- NaiveBayes(流失 ~ ., data = traindata)  # 建立朴素贝叶斯分类模型
# 预测结果
train_predict <- predict(NaiveBayes.model)  # 训练数据集
test_predict <- predict(NaiveBayes.model, newdata = testdata)  # 测试数据集
# 输出训练数据的分类结果
train_predictdata <- cbind(traindata, predictedclass = train_predict$class) 
# 输出训练数据的混淆矩阵
(train_confusion <- table(actual = traindata$流失, predictedclass = train_predict$class)) 
# 输出测试数据的分类结果
test_predictdata <- cbind(testdata, predictedclass = test_predict$class)
# 输出测试数据的混淆矩阵
(test_confusion <- table(actual = testdata$流失, predictedclass = test_predict$class))

# 6.6    建立lda模型并进行分类预测
# lda模型
setwd("F:/数据及程序/第6章/示例程序")  # 设置工作空间
Data <- read.csv("./data/telephone.csv")  # 读入数据
Data[, "流失"] <- as.factor(Data[, "流失"]) #将目标变量转换成因子型
set.seed(1234)  # 设置随机种子
# 数据集随机抽70%定义为训练数据集，30%为测试数据集

ind <- sample(2, nrow(Data), replace = TRUE, prob = c(0.7, 0.3))
traindata <- Data[ind == 1, ]
testdata <- Data[ind == 2, ]

# 建立lda分类模型
library(MASS)
lda.model <- lda(流失 ~ ., data = traindata)

# 预测结果
train_predict <- predict(lda.model, newdata = traindata)  # 训练数据集
test_predict <- predict(lda.model, newdata = testdata)  # 测试数据集

# 输出训练数据的分类结果
train_predictdata <- cbind(traindata, predictedclass = train_predict$class) 
# 输出训练数据的混淆矩阵
(train_confusion <- table(actual = traindata$流失, predictedclass = train_predict$class))
# 输出测试数据的分类结果
test_predictdata <- cbind(testdata, predictedclass = test_predict$class)
# 输出测试数据的混淆矩阵
(test_confusion <- table(actual = testdata$流失, predictedclass = test_predict$class))



# 6.6    构建rpart模型并进行分类预测
# rpart模型
setwd("F:/数据及程序/第6章/示例程序")  # 设置工作空间
Data <- read.csv("./data/telephone.csv")  # 读入数据
Data[, "流失"] <- as.factor(Data[, "流失"])  # 将目标变量转换成因子型
set.seed(1234)  # 设置随机种子
# 数据集随机抽70%定义为训练数据集，30%为测试数据集
ind <- sample(2, nrow(Data), replace = TRUE, prob = c(0.7, 0.3))
traindata <- Data[ind == 1, ]
testdata <- Data[ind == 2, ]

# 建立rpart分类模型
library(rpart)
library(rpart.plot)
rpart.model <- rpart(流失 ~ ., data = traindata, method = "class", cp = 0.03)  # cp为复杂的参数
# 输出决策树图
rpart.plot(rpart.model, branch = 1, branch.type = 2, type = 1, extra = 102,  
           border.col = "blue", split.col = "red",  
           split.cex = 1, main = "客户流失决策树")
# 预测结果
train_predict <- predict(rpart.model, newdata = traindata, type = "class")  # 训练数据集
test_predict <- predict(rpart.model, newdata = testdata, type = "class")  # 测试数据集

# 输出训练数据的分类结果
train_predictdata <- cbind(traindata, predictedclass = train_predict) 
# 输出训练数据的混淆矩阵
(train_confusion <- table(actual = traindata$流失, predictedclass = train_predict)) 
# 输出测试数据的分类结果
test_predictdata <- cbind(testdata, predictedclass = test_predict)
# 输出测试数据的混淆矩阵
(test_confusion <- table(actual = testdata$流失, predictedclass = test_predict))



# 6.6   构建bagging模型并进行分类预测
# bagging模型
setwd("F:/数据及程序/第6章/示例程序")  # 设置工作空间
Data <- read.csv("./data/telephone.csv")  # 读入数据
Data[, "流失"] <- as.factor(Data[, "流失"])  # 将目标变量转换成因子型
set.seed(1234)  # 设置随机种子
# 数据集随机抽70%定义为训练数据集，30%为测试数据集
ind <- sample(2, nrow(Data), replace = TRUE, prob = c(0.7, 0.3))
traindata <- Data[ind == 1, ]
testdata <- Data[ind == 2, ]

# 建立bagging分类模型
library(adabag)
bagging.model <- bagging(流失 ~ ., data = traindata)

# 预测结果
train_predict <- predict(bagging.model, newdata = traindata)  # 训练数据集
test_predict <- predict(bagging.model, newdata = testdata)  # 测试数据集

# 输出训练数据的分类结果
train_predictdata <- cbind(traindata, predictedclass = train_predict$class) 
# 输出训练数据的混淆矩阵
(train_confusion <- table(actual = traindata$流失, predictedclass = train_predict$class)) 
# 输出测试数据的分类结果
test_predictdata <- cbind(testdata, predictedclass = test_predict$class)
# 输出测试数据的混淆矩阵
(test_confusion <- table(actual = testdata$流失, predictedclass = test_predict$class))



# 6.6    构建randomForest模型并进行分类预测
# randomForest模型
setwd("F:/数据及程序/第6章/示例程序")  # 设置工作空间
Data <- read.csv("./data/telephone.csv")  # 读入数据
Data[, "流失"] <- as.factor(Data[, "流失"])  # 将目标变量转换成因子型
set.seed(1234)  # 设置随机种子
# 数据集随机抽70%定义为训练数据集，30%为测试数据集
ind <- sample(2, nrow(Data), replace = TRUE, prob = c(0.7, 0.3))
traindata <- Data[ind == 1, ]
testdata <- Data[ind == 2, ]

# 建立randomForest模型
library(randomForest)
randomForest.model <- randomForest(流失 ~ ., data = traindata)

# 预测结果
test_predict <- predict(randomForest.model, newdata = testdata)  # 测试数据集

# 输出训练数据的混淆矩阵
(train_confusion <- randomForest.model$confusion)
# 输出测试数据的混淆矩阵
(test_confusion <- table(actual = testdata$流失, predictedclass = test_predict))



# 6.6   构建svm模型并进行分类预测
# svm模型
setwd("F:/数据及程序/第6章/示例程序")  # 设置工作空间
Data <- read.csv("./data/telephone.csv")  # 读入数据
Data[, "流失"] = as.factor(Data[, "流失"])  # 将目标变量转换成因子型
set.seed(1234)  # 设置随机种子
# 数据集随机抽70%定义为训练数据集，30%为测试数据集
ind <- sample(2, nrow(Data), replace = TRUE, prob = c(0.7, 0.3))
traindata <- Data[ind == 1, ]
testdata <- Data[ind == 2, ]

# 建立svm模型
library(e1071)
svm.model <- svm(流失 ~ ., data = traindata)

# 预测结果
train_predict <- predict(svm.model, newdata = traindata)  # 训练数据集
test_predict <- predict(svm.model, newdata = testdata)  # 测试数据集

# 输出训练数据的分类结果
train_predictdata <- cbind(traindata, predictedclass = train_predict) 
# 输出训练数据的混淆矩阵
(train_confusion <- table(actual = traindata$流失, predictedclass = train_predict)) 
# 输出测试数据的分类结果
test_predictdata <- cbind(testdata, predictedclass = test_predict)
# 输出测试数据的混淆矩阵
(test_confusion <- table(actual = testdata$流失, predictedclass = test_predict))



# 6.7     ROC曲线和PR曲线图代码
# ROC曲线和PR曲线
library(ROCR)
library(gplots)

# 预测结果
train_predict <- predict(lda.model, newdata = traindata)  # 训练数据集
test_predict <- predict(lda.model, newdata = testdata)  # 测试数据集

par(mfrow = c(1, 2))
# ROC曲线
# 训练集
predi <- prediction(train_predict$posterior[, 2], traindata$流失)
perfor <- performance(predi, "tpr", "fpr")
plot(perfor, col = "red", type = "l", main = "ROC曲线", lty = 1)  # 训练集的ROC曲线
# 测试集
predi2 <- prediction(test_predict$posterior[, 2], testdata$流失)
perfor2 <- performance(predi2, "tpr", "fpr")
par(new = T)
plot(perfor2, col = "blue", type = "l", pch = 2, lty = 2)  # 测试集的ROC曲线
abline(0, 1)
legend("bottomright", legend = c("训练集", "测试集"), bty = "n", 
       lty = c(1, 2), col = c("red", "blue"))  # 图例

# PR曲线
# 训练集
perfor <- performance(predi, "prec", "rec")
plot(perfor, col = "red", type = "l", main = "PR曲线", xlim = c(0, 1), 
     ylim = c(0, 1), lty = 1)  # 训练集的PR曲线
# 测试集
perfor2 <- performance(predi2, "prec", "rec")
par(new = T)
plot(perfor2, col = "blue", type = "l", pch = 2, xlim = c(0, 1), 
     ylim = c(0, 1), lty = 2)  # 测试集的PR曲线
abline(1, -1)
legend("bottomleft", legend = c("训练集", "测试集"), bty = "n", 
       lty = c(1, 2), col = c("red", "blue"))  # 图例

