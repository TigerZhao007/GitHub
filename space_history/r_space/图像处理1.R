# 加载包
library(jpeg);library(reshape2)
## 数据读取,Box和picture ##
#box <- read.table(file="Data/55c9d201N7d9cc61a.box", header = F)
#picture <- readJPEG("E:/图片/张润/照片/IMG_0020.JPG")

picture <- readJPEG("C:/Users/Think/Desktop/pythondownload/3.JPG")
dim(picture) # 三维数组
## 数据整理 ##
longImage <- melt(picture)
##转换成Rbg矩阵
rgbImage <- reshape(longImage, timevar='Var3',idvar=c('Var1','Var2'), direction='wide')
##转换成RGB矩阵,其中Var1，2是坐标值，value1,2,3对应R,B,G的值
head(rgbImage)
## 提取颜色
colorColumns<- rgbImage[, substr(colnames(rgbImage), 1, 5)== "value"]  
# 画图，图片是反的，旋转坐标轴
with(rgbImage,plot(Var2, Var1, col = rgb(colorColumns), asp = 1, pch =".",axes=T,xlab='',ylab=''))
## 坐标轴转换
rgbImage$Var1 <- rep(max(rgbImage$Var1):1, ncol(picture))
## 画图 
with(rgbImage,plot(Var2, Var1, col = rgb(colorColumns), asp = 1, pch =".",axes=T,xlab='',ylab=''))
### 画出Box文件中在图片中的位置
#rect(box$V2, box$V3, box$V4, box$V5)















































