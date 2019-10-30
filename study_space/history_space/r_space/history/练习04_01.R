library("RODBC")
connect <- odbcConnect("Rspace",uid = "sa",pwd = "sdk")
sqlQuery(connect,"USE Rspace alter table [dbo].[st]
drop column 耐力项目编号,耐力项目成绩,奖惩项目成绩")
sqlQuery(connect,"USE Rspace alter table [dbo].[st]
drop column 耐力项目编号")
sqlQuery(connect,"USE Rspace alter table [dbo].[st]
drop column 耐力项目成绩")
sqlQuery(connect,"USE Rspace alter table [dbo].[st]
drop column 奖惩项目编号")
st0 <- sqlFetch(connect, "st")
head(st0)
names(st0)
names(st0) <- c("grade.num","class.num","class","student.ID","nation", "name",
               "sex", "data", "ID", "height","weight", "strength.num","strength",
               "speed.num","speed")
head(st0)
st1 <- na.omit(st0)
head(st1)
sqlSave(connect,st1,tablename = "st_new")
View(st1)
fix(st1)
sex
attach(st1)
table(sex)
table(nation)
sample01 <- st1[1:10,]
sample01
sample01$sex[sex=1]<-"boy"
sample01$sex[sex=2]<-"girl"
sample01$class[which(sample01$class==6)] <- "class_six"

library("sqldf")
sqldf("update sample01 
      set class='class_six' 
      where class=6")
sample01
sample02<-sqldf("delete from sample01 where sex='girl'")              ###????????????????
sample02
sqldf("select * from sample01 where sex='girl'")
?sqldf
sqldf("select name from sample01 where sex='girl'")
rm(sample01,sample02)
head(st1)
sex[which(sex==1)] <- "boy"
sex[which(sex==2)] <- "girl"
table(sex)
table(class)
table(st1$sex)
rm(sex,x)
library("Hmisc")
names(st1)
samp.1 <- c("height","weight","speed","strength")
describe(st1[samp.1])
library("pastecs")
stat.desc(st1[samp.1])
library("psych")
describe(st1[samp.1])
Hmisc::describe(st1[samp.1])
st1.1 <- st1[samp.1]
aggregate(st1.1, by=list(sex),mean)
aggregate(st1.1, by=list(sex=sex),mean)
by(st1.1, sex, describe)
install.packages("doBy")
install.packages()
library("doBy")
factor(sex)
summaryBy(height+weight~sex,data=st1,FUN=describe)                 ####????????
names(st1)
st1
describeBy(st1.1,list(sex))
library("vcd")
head(st1.1)
mytable <- with(st1, table(sex))
mytable
mytable.sg<- table(sex,grade.num)
addmargins(mytable.sg,c(1,2))
prop.table(mytable.sg,1)->mytable.sg.p
addmargins(mytable.sg.p)
mytable.sg.p*100
xtabs(~sex+grade.num)
  table(sex,grade.num)
mytable.sg
margin.table(mytable.sg,2)
library("gmodels")
install.packages("gmodels")
CrossTable(sex,grade.num,format = 'SAS',prop.r = T,prop.c = T,prop.t = T,fisher = T)
?CrossTable
CrossTable(sex,grade.num,format = 'SAS',prop.r = T,prop.c = T,prop.t = T,fisher = F, mcnemar = F,expected = T)
table(sex,grade.num,nation)
mytable.sgn<-xtabs(~sex+grade.num+nation)
ftable(st1.1)
ftable(mytable.sgn)
mytable
mytable.sg
mytable.sgn
chisq.test(mytable.sg)
fisher.test(mytable.sg,workspace = 20000000)
?fisher.test

mantelhaen.test(mytable.sgn)
names(st1)
head(st1)
mytable.gcs <- table(grade.num,class.num,sex)
mantelhaen.test(mytable.gcs)
ftable(mytable.gcs)
assocstats(mytable.sg)
cor(st1.1)
cor(st1.1,use = "everything",method = "spearman")
cor(st1.1,use = "everything",method = "kendall")
cor(st1.1[,3:4], st1.1[,1:2])
names(st1.1)  
library("ggm")
install.packages("ggm")
pcor(c(3,4,1),cov(st1.1))
library("polycor")
install.packages("polycor")
hetcor(st1.1)
cor(st1.1)
cor.test(st1.1$height,st1.1$weight)
corr.test(st1.1)
pcor.test(pcor(c(3,4,1,2),cov(st1.1)), 2, nrow(st1.1))
t.test(height~sex,st1)
t.test(height, weight)
wilcox.test(library())
library(MASS)
head(UScrime)
median(UScrime$Prob)
with(UScrime,by(Prob, So, median ))
with(UScrime, by(Prob, So, wilcox.test))
wilcox.test(Prob~So, data = UScrime)
wilcox.test(height~sex)
kruskal.test(height~grade.num)
source("http://www.statmethods.net/RiA/wmc.txt")
wmc(height~grade.num,data=st1,method = "holm")
data("women")
fit <- lm(weight~height)
fit
summary(fit)


































