library("xlsx")
library("")

dat <- read.xlsx("C:\\Users\\SDK\\Desktop\\1.xlsx",sheetIndex = "Sheet1")
head(dat)
tail(dat)
attach(dat)
detach(dat)
dat1 <- dat[1:110,]
dat2 <- dat[111:114,]
plot(dat[,4:5])


##  聚类法1
kmeans1 <- kmeans(dat1[,4:5],centers = dat2[,4:5])
dat3 <- kmeans1$centers
points(dat2[,4:5], col="#FF1493",pch=19)
?kmeans

##  聚类法2
library(cluster)#做聚类的包  
library(fpc)#有dbscan  
#ds <- dbscan(x, 2)#2是半径，最小点数默认为5  
ds <- dbscan(dat1[,4:5], 3000, 12)  
#ds <- dbscan(x,1,3)  
ds#可以看border，seed数  
str(ds)#可以看列数  
par(bg="grey")  
plot(ds, dat1[,4:5])  

##  聚类法3
install.packages("amap")
install.packages("R2SWF")
install.packages("animation")
library(amap)#这个包里有kmeans函数
library(R2SWF)
library(animation)#导入包，后两个是作动画的包

output = dev2swf({
  par(mar = c(3, 3, 1, 1.5), mgp = c(1.5, 0.5, 0))
  kmeans.ani(x = dat1[,4:5], centers = 30, #指定age_inc为要处理的文件，指定类数为3
             hints = c("Move centers!", "Find cluster?"), pch = 1:3, col = 1:3)
}, output = "income_age.swf")#输出flash动画
swf2html(output)#将动画放到HTML里

seed(1234)
kmeans2 <- kmeans.ani(x = dat1[,4:5], centers =25, #指定age_inc为要处理的文件，指定类数为3
           hints = c("Move centers!", "Find cluster?"), pch = 1:3, col = 1:3)

summary(kmeans2)
dat6 <- kmeans2$cluster
dat4 <- kmeans2$centers

seed
kmeans3 <- kmeans.ani(x = dat4, centers = 4, #指定age_inc为要处理的文件，指定类数为3
                      hints = c("Move centers!", "Find cluster?"), pch = 1:3, col = 1:3)
dat5 <- kmeans3$centers
dat7 <- kmeans3$cluster

write.csv(dat6,"C:\\Users\\SDK\\Desktop\\dat6.csv")
write.csv(dat7,"C:\\Users\\SDK\\Desktop\\dat7.csv")

str(dat8)
dat8 <- as.numeric(dat4)

