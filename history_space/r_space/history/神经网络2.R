library(nnet)            #安装nnet软件包
library(mlbench)         #安装mlbench软件包
data(Vehicle)            #调入数据
n=length(Vehicle[,1])    #样本量
set.seed(1)              #设随机数种子
samp=sample(1:n,n/2)     #随机选择半数观测作为训练集
b=class.ind(Vehicle$Class)           #生成类别的示性函数
test.cl=function(true,pred){
  true<-max.col(true);
  cres=max.col(pred);
  table(true,cres)
  }
a=nnet(Vehicle[samp,-19],b[samp,],
       size=3,rang=0.1,decay=5e-4,maxit=200)
#利用训练集中前18个变量作为输入变量，隐藏层有3个节点，初始随机权值在[-0.1,0.1]，权值是逐渐衰减的。
test.cl(b[samp,],predict(a,Vehicle[samp,-19]))
#给出训练集分类结果
test.cl(b[-samp,],predict(a,Vehicle[-samp,-19]))
#给出测试集分类结果
#构建隐藏层包含15个节点的网络。接着上面的语句输入如下程序：
a=nnet(Vehicle[samp,-19],b[samp,],
       size=15,rang=0.1,decay=5e-4,maxit=10000)
test.cl(b[samp,],predict(a,Vehicle[samp,-19]))
test.cl(b[-samp,],predict(a,Vehicle[-samp,-19]))

ss <- nnetHess(a,Vehicle[samp,-19],b[samp,])
head(ss)
