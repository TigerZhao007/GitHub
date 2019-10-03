library(nnet)            #安装nnet软件包
sj <- data.frame(x1<-c(0,0,1,1),x2<-c(0,1,0,1),y<-c(0,1,1,0))

b=class.ind(sj$y....c.0..1..1..0.)           #生成类别的示性函数
test.cl=function(true,pred){
  true<-max.col(true);
  cres=max.col(pred);
  table(true,cres)
}
a=nnet(sj[,-3],b,
       size=2,rang=0.1,decay=5e-4,maxit=1000)
#利用训练集中前18个变量作为输入变量，隐藏层有3个节点，初始随机权值在[-0.1,0.1]，权值是逐渐衰减的。
test.cl(b,predict(a,sj[,-3]))
#给出训练集分类结果
test.cl(b[-samp,],predict(a,Vehicle[-samp,-19]))
#给出测试集分类结果

ss <- nnetHess(a,Vehicle[samp,-19],b[samp,])
head(ss)
summary(a)
a1=nnet(sj[,-3],sj[,3],
       size=2,rang=0.1,decay=5e-4,maxit=1000)
summary(a1)
test.cl(b,predict(a1,sj[,-3]))
