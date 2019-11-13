#ȱʧֵ��������

data(sleep, package="VIM")             #��ȡ���ݿ��е�����
sleep                                  #�鿴����
dim(sleep)                             #�鿴�����������ͱ�����
sum(complete.cases(sleep))             #�鿴����������

library(VIM)                           #����VIM�����

aggr(sleep)                            #��ͼ�η�ʽ����ȱʧ����
#��ͼ��ʾ������ȱʧ���ݱ�������ͼ��ʾ�˸���ȱʧģʽ�Ͷ�Ӧ��������Ŀ����ʾnond��dream����ͬʱ����ȱʧֵ��

library(mice)                          #����VIM�����

md.pattern(sleep)                      #�ж�ȱʧ���ݵ�ģʽ�Ƿ����
#�ϱ��е�1��ʾû��ȱʧ���ݣ�0��ʾ����ȱʧ���ݡ����һ�б�ʾ��������ȱʧ���������ϼơ�

exp 1

imp=mice(sleep,seed=1234)
fit=with(imp,lm(Dream~Span+Gest))
pooled=pool(fit)
summary(pooled)

#��R������ʵ�ַ�����ʹ��mice���е�mice���������ɶ���������ݼ�����imp�У�
#�ٶ�imp�������Իع飬�����pool�����Իع������л��ܡ�
#���ܽ����ǰ�沿�ֺ���ͨ�ع������ƣ�
#nmis��ʾ�˱����е�ȱʧ���ݸ�����
#fmi��ʾfraction of missing information������ȱʧ���ݹ��׵ı���

complete.cases(sleep)                  #������ȱʧֵ���
na.omit(sleep)                         #�޳�ȱʧֵ�������
str(sleep)                             #�鿴��������
str(na.omit(sleep))                    #�鿴��������

library("VIM") 
marginplot(sleep[c("Gest","Dream")],
      pch=c(20),col=c("darkgray","red","blue"))
#ͼ�ε�������Gest��Dream�����������ݶ���������ɢ��ͼ��
#��߽������ͼչʾ���ǰ��������ɫ���벻��������ɫ��Gestֵ��Dream�����ֲ���
#ע�⣬�ڻҶ�ͼ�Ϻ�ɫ�Ǹ������Ӱ���ĸ���ɫ�ĵ������ȱʧ��Gest�÷ֵ�Dreamֵ��
#�ڵײ��߽��ϣ�Gest��Dream��Ĺ�ϵ�������ˡ�

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