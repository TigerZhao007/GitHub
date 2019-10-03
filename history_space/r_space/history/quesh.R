#缺失值处理程序

data(sleep, package="VIM")             #读取数据库中的数据
sleep                                  #查看数据
dim(sleep)                             #查看数据样本数和变量数
sum(complete.cases(sleep))             #查看完整样本数
summary(sleep)                         #查看每个变量的信息和缺失值情况。

library(VIM)                           #载入VIM程序包

aggr(sleep)                            #以图形方式描述缺失数据
#左图显示各变量缺失数据比例，右图显示了各种缺失模式和对应的样本数目，显示nond和dream经常同时出现缺失值。

library(mice)                          #载入VIM程序包

md.pattern(sleep)                      #判断缺失数据的模式是否随机
#上表中的1表示没有缺失数据，0表示存在缺失数据。最后一行表示各个变量缺失的样本数合计。

exp 1

imp=mice(sleep,seed=1234)
fit=with(imp,lm(Dream~Span+Gest))
pooled=pool(fit)
summary(pooled)

#在R语言中实现方法是使用mice包中的mice函数，生成多个完整数据集存在imp中，
#再对imp进行线性回归，最后用pool函数对回归结果进行汇总。
#汇总结果的前面部分和普通回归结果相似，
#nmis表示了变量中的缺失数据个数，
#fmi表示fraction of missing information，即由缺失数据贡献的变异

complete.cases(sleep)                  #数据中缺失值情况
na.omit(sleep)                         #剔除缺失值后的数据
str(sleep)                             #查看数据类型
str(na.omit(sleep))                    #查看数据类型

library("VIM") 
marginplot(sleep[c("Gest","Dream")],
           pch=c(20),col=c("darkgray","red","blue"))
#图形的主体是Gest和Dream（两变量数据都完整）的散点图。
#左边界的箱线图展示的是包含（深灰色）与不包含（红色）Gest值的Dream变量分布。
#注意，在灰度图上红色是更深的阴影。四个红色的点代表着缺失了Gest得分的Dream值。
#在底部边界上，Gest和Dream间的关系反过来了。

head(sleep) 
str(sleep) 
x<-as.data.frame(abs(is.na(sleep))) 
head(sleep,n=5) 
head(x,n=5) 


library(mydata)
code1 
newdata<-mydata[complete.cases(mydata),] 
newdata<-na.omit(mydata) 
code2 
options(digits=1) 
cor(na.omit(sleep)) 
cor(sleep,use="complete.obs") 
fit<-lm(Dream~Span+Gest,data=na.omit(sleep)) 
summary(fit)
