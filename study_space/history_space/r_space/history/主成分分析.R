##  主成分分析  ## 

# 数据导入。
library(RODBC)
ch <- odbcConnect("Rspace", uid = "sa", pwd = "sdk")
tianqi <- sqlFetch(ch, "天气")
odbcClose(ch)
tianqi
tianqi01 <- tianqi[,-c(1:2)]
tianqi01


#  数据的标准化。
b2 <- list()
b2.mean <- matrix()
b2.sd   <- matrix()
n <- ncol(tianqi01)
for (i in 1:n) {
  b2.mean[i] <- mean(tianqi01[,i]) 
  b2.sd[i]   <- sd(tianqi01[,i])
  b2[[i]]  <- (tianqi01[i]-b2.mean[i])/b2.sd[i]

}
b2.end   <- as.data.frame(b2)
tianqi02 <- b2.end
tianqi03 <- scale(tianqi01)

#  主成分分析。
pca <- princomp(tianqi01,cor = F) #主成分分析。
pca
names(pca)     #查看输出表中的名字。
summary(pca)   #主成分贡献率。
pca$sdev
(pca$sdev)^2   #主成分特征根。
pca$loadings
pca$center
pca$scale
pca$n.obs
pca$scores
pca$call


##  主成分分析2  ##
# 读取数据
# 数据标准化
pca.1 <- princomp(tianqi01,cor=T)    # 主成分分析函数。
pca.cor <- cor(tianqi01)             # 原始变量相关系数。
screeplot(pca.1,type = "line")       # 绘制碎石图。
screeplot(pca.1)                     # 绘制碎石柱图。
biplot(pca.1)                        # 绘向量图。
pca.eig <- eigen(pca.cor)            # 计算特征值和特征向量。
pca.eig$values                       # 输出特征值。
pca.kz <- sum(pca.eig$values)        # 求出特征值总和。
pca.k3 <- sum(pca.eig$values[1:3])   # 求出前三个特征值总和。
pca.l3 <- pca.k3/pca.kz              # 求出前三个特征值累计贡献率。
pca.1$loadings[,1:3]                 # 计算三个主成分的系数。
pca.b1 <- pca.eig$values[1]/pca.kz
pca.b2 <- pca.eig$values[2]/pca.kz
pca.b3 <- pca.eig$values[3]/pca.kz   # 分别计算三个主成分的贡献度。
pca.b <- sum(pca.b1,pca.b2,pca.b3)
pca.sz <- pca.1$scores[,1:3]         # 计算前三个主成分得分。
pca.q1 <- pca.b1/pca.b
pca.q2 <- pca.b2/pca.b
pca.q3 <- pca.b3/pca.b               # 分别计算前三个主成分权重。
pca.cz <- pca.sz[,1]*pca.q1 + pca.sz[,2]*pca.q2 + pca.sz[,3]*pca.q3
                                     # 计算综合得分。
sorce.end <- cbind(pca.sz, pca.cz)   # 主成分和综合得分汇总。

rownames(sorce.end) <- c("南 京 市","无 锡 市","徐 州 市","常 州 市","苏 州 市","南 通 市","连云港市","淮 安 市","盐 城 市","扬 州 市",
                         "镇 江 市","泰 州 市","宿 迁 市")
sort(pca.cz)
sort(sorce.end[,4],decreasing = T)




##  不可用？ ##
install.packages(psych)
install.packages(GPArotation)
library(psych)
library(GPArotation)
fa.parallel(shuju[,-1],fa="pc", n.iter=100, show.legend=FALSE)
pc<-principal(tianqi01[,-1],nfactors=4,score=T)







