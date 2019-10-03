library("xlsx")
library(nnet)            #安装nnet软件包

data <- read.xlsx("C:\\Users\\SDK\\Desktop\\大数据论文\\txsj.xlsx",sheetName = "Sheet1",encoding = "UTF-8")
head(data)

n=length(data[,1])    #样本量
set.seed(1)              #设随机数种子
samp=sample(1:n,n/2)     #随机选择半数观测作为训练集
a=nnet(data[samp,c(6:30)],data[samp,5],
       size=3,rang=0.1,decay=5e-4,maxit=200)
#利用训练集中前18个变量作为输入变量，隐藏层有3个节点，初始随机权值在[-0.1,0.1]，权值是逐渐衰减的。
