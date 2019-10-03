#使用R语言进行图像分类

#本文使用R语言,应用SVM(高斯核)[3]算法对JPEG图片进行二类分。
#SVM使用e1071包, 图像处理用imager包[1]。
#数据使用的是Caltech 101中的Faces和BACKGROUND_Google两类数据[2]
#1 步骤
#代码执行五个步骤。
#• 读取图片• 向量化• 合并图片• 训练模型• 对测试集分类

#2 程序执行时生成的SVM模型的部分信息
#采样不同，结果可能不同。
#summary(fit):
#  SVM-Type:  C-classification 
#SVM-Kernel:  radial 
#cost:  1 
#gamma:  0.0009765625 
#Number of Support Vectors:  349

library(imager)
library(e1071)

#setwd("~/repos/project/R-src/")

read.imags <- function(path = "./") {
  fns <- list.files(path)
  res <- NULL
  for(i in fns) {
    fn <- paste(path, i, sep = "")
    im <- load.image(fn)
    im <- resize(im, size_x = 32L, size_y = 32L,
                 size_z = 1L, size_c = 1L)
    im <- as.array(im)
    im <- matrix(im, 1, mult(dim(im)))
    ifelse(!is.null(res),
           res <- rbind(res, im), res <- im)
  }
  return(res)
}

a.images <- read.imags("./101_ObjectCategories/Faces/")
b.images <- read.imags("./101_ObjectCategories/BACKGROUND_Google/")

(sam.count <- ceiling(min(nrow(a.images) * 0.8, nrow(b.images) * 0.8)))

train.a <- sample(1:nrow(a.images), sam.count, replace = F)
train.b <- sample(1:nrow(b.images), sam.count, replace = F)

data.imags <- rbind(a.images[train.a,], b.images[train.b,])


fit <- svm(data.imags, c(rep(1, length(train.a)), rep(0, length(train.b))),
           probablity = T, cross = 3,
           type = "C-classification", method = "SVM")

a.pred <- predict(fit, a.images[-train.a,])
a.pred <- as.numeric(as.character(a.pred))
prop.table(table(a.pred))

b.pred <- predict(fit, b.images[-train.b,])
b.pred <- as.numeric(as.character(b.pred))
prop.table(table(b.pred))



















