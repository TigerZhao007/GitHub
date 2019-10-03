library("RGame")
library("RODBC")
connect <-odbcConnect("Rspace",uid="sa",pwd="sdk")
summary(connect,Rspace)
sqlQuery(connect,"select*from Rspace")
sqlQuery(connect,"select*from table")
gdp <- sqlQuery(connect,"select*from GDP")
head(gdp)
names(gdp$年份) <- "year"
row.names(gdp) <- gdp$rownames
col.names(gdp) <- c("rownames1", "year", "gdpy", "gdpd","rate.increasing","per.gdpy",
                    "per.gdpd","per.rate.increasing","gdpyy","person.rate.increasing",
                    "inflation", "totle.peopie")
colnames(gdp) <- c("rownames1", "year", "gdpy", "gdpd","rate.increasing","per.gdpy",
                   "per.gdpd","per.rate.increasing","gdpyy","person.rate.increasing",
                   "inflation", "totle.peopie")
sqlSave(connect,gdp,tablename = "GDP",append = T)
odbcUpdate(connect,"GDP")
sc.data <- odbcFetchRows(connect,"理科")
head(sc.data)
sc.data
sc.data <- sqlFetch(connect,"理科")
head(sc.data)
library("xlsx")
ss.data1 <- read.xlsx("C:\\Users\\SDK\\Desktop\\3.xls",sheetIndex = "Sheet1",encoding = "UTF-8")
head(ss.data)
sqlSave(connect, ss.data, tablename = "学生身体素质数据")
ss.data[1:2,1:2]
ss.data$班级名称
ss.data$性别
ss.data[which(ss.data$性别==2),]
tail(ss.data)
ss.girl <- sqlQuery(connect,"select*from 学生身体素质数据 where 性别=2")
with(ss.data,x01 <<- ss.data$性别)
x01
ss.data$性别 <- factor(ss.data$性别)
summary(ss.data$身高,ss.sex)
str(ss.data)
ss.data$性别 <- factor(ss.data$性别,levels =c(1,2), labels = c("boy","girl"))
ss.data$班级名称 <- factor(ss.data$班级名称,levels=2, labels="二班")
head(ss.data)
ss.data$民族代码 <- factor(ss.data$民族代码, levels = 1, labels = "汉族")
sqlSave(connect,ss.data,tablename = "学生身体素质数据1",append=F)
sqlUpdate(connect,tablename = "学生身体素质数据", ss.data)
sqlQuery(connect,"delete 学生身体素质数据 where 性别=1")
head(ss.data1)
ss.data2 <- ss.data1[1:10,]
ss.data2
sqlSave(connect,ss.data2,tablename = "学生身体素质数据",append = T)
sqlUpdate(connect,ss.data2,tablename = "学生身体素质数据")
sqlQuery(connect,"select * from 学生身体素质数据
where 姓名 in (select   姓名 from 学生身体素质数据 group by 姓名 having count
          (姓名) > 1)
         ")
sqlQuery(connect,"delete from 学生身体素质数据 where 姓名='张薇'")

sqlQuery(connect,"delete from 学生身体素质数据 
where 姓名 in (select 姓名 from 学生身体素质数据 group by having count(姓名) > 1)")
sqlQuery(connect,"delect  from 学生身体素质数据
where 姓名 in (select   姓名 from 学生身体素质数据 group by 姓名 having count (姓名) > 1)
and rownames not in (select min(rownames) from  学生身体素质数据 group by 姓名 having count(姓名)>1
         
         ")

ss.girl2 <- sqlQuery(connect, "select distinct*from 学生身体素质数据")
ss.girl2
sqlSave(connect, ss.girl2[,-1], tablename = "学生身体素质",append = T)

sqlQuery(connect, "select distinct * into #Tmp from 学生身体素质 
drop table 学生身体素质
select * into 学生身体素质 from #Tmp
drop table #Tmp")

library("ggplot2")
par(col=1,fg=4,lty=2,pch=17,bg=1,col.axis=2,col.lab=5,col.main=3,col.sub=9,main="xiantu")
plot(ss.girl$rownames,ss.girl$身高,type="b")
plot(ss.girl$rownames,ss.girl$体重,type = "b")
opar <- par(no.readonly = T)
par(opar)
dev.off()


library(RColorBrewer)
barplot(rep(1,7),col=brewer.pal(7,"Set1"))
hist(ss.girl2$肺活量,col=brewer.pal(7,"Set1"))
x <- runif(100,-100,100)
y <- runif(100,-10,10)
abline(h=0)
abline(v=0)

plot(x,y,fg="white",col=rainbow(10),xlim = c(-100,100),ylim = c(-10,10))
axis(2,at=seq(from=-10,to=10,by=5),pos=0,lty = 1,tck=0.01,cex.lab=0.1)
axis(1,at=seq(from=-100,to=100,by=20),pos=0,lty = 1,col = 2,tck=0.01,cex.lab=0.01,las=1)


x <- y <- c(1:10)
x.name<- paste("x",1:10,rep="")
x.name
z <- 10/x
z
opar<- par(no.readonly = T)
par(mar=c(5,4,4,8)+0.1)
plot(x,y,type = "b",pch=21,col=2,yaxt="n",lty=3,ann = F)
lines(x,z,type = "b", pch=22,col=4,lty=2)
axis(2,at=x,labels = x,col.axis=2,lty = 2)
axis(4,at=z,labels=round(z,digits = 1),col.axis=4,las=2,cex.axis=0.7,tck=-0.01)
mtext("y=1/x",side = 4,line = 3,cex.lab=1,las=2,col = 4)
title("ss", xlab = "sss", ylab = "sssss")
install.packages("Hmisc")
library("Hmisc")
minor.tick(nx=2,ny=2,tick.ratio = 0.5)
legend("topleft",inset = .05, title = "DG",c("A","B"),lty = c(3,2),pch = c(21,22),col = c(2,4))
text(x,y,x.name,cex=0.6,pos=3, col=2)
dev.off()
layout(matrix(c(1,1,2,3),2,2,byrow = TRUE))
hist(ss.data1$身高)
hist(ss.data1$体重)
hist(ss.data1$肺活量)
windows()
layout(matrix(c(1,1,2,3),2,2,byrow = TRUE),widths = c(3,1),heights = c(1,2))
hist(ss.data1$身高)
hist(ss.data1$体重)
hist(ss.data1$肺活量)
opar <- par(no.readonly = T)
par(fig=c(0,0.8,0,0.8),col=4)
plot(ss.data1$身高,ss.data1$体重,fg=4,bg=1,col.lab=4,col.main=4,col.axis=2,col.sub=4,main="ddd")
par(fig=c(0,0.8,0.55,1),new=T)
boxplot(ss.data1$身高,horizontal=T,axes=F,col=4)
par(fig=c(0.65,1,0,0.8),new=T,col=2)
boxplot(ss.data1$体重,axes=F,col = red)

mydata <- data.frame(high=ss.girl2$身高,weigh=ss.girl2$体重,gas=ss.girl2$肺活量)
mydata
mydata$sum1 <- mydata$high +mydata$weigh + mydata$gas
mydata$mean1 <- (mydata$high +mydata$weigh + mydata$gas)/3
mydata
mydata <-transform(mydata,sumx=high+weigh+gas,meanx=(high+weigh+gas)/3)
mydata
#mydata <- with(mydata,
#                    ag[which(mydata$high>=160)]="good",
#                    ag[which(150<=mydata$high<160)]="well",
#                    ag[which(mydata$high<150)]="bad")
mydata <- within(mydata,{
  ag <- NA
  ag[high>=160]="good"
  ag[150<=high<160]="well"
  ag[high<150]="bad"})
mydata$ag[mydata$high>=160] <- "good"
mydata$ag[mydata$high>=150&mydata$high<160]<- "well"
mydata$ag[mydata$high<150] <- "bad"
mydata
mydata <- within(mydata,{
  ag1 <- NA
  ag1[high>=160]<- "good"
  ag1[high>=150&high<160]<-"well"
  ag1[high<150] <- "bad"
})

fix(mydata)
names(mydata)[1]<-"height"
mydata
install.packages("plyr")
names(mydata)
mydata <-rename(mydata,c(ag="agent",ag1="agent1"))
mydata

mydates<- as.Date(c("2007-06-22","2004-09-30"))
mydates
strDates <- c("01/05/1965","08/16/1975")
strDates
myformat <- "%m/%d/%y"
dates<- as.Date(strDates,myformat)
dates
Sys.Date()
date()
today <- Sys.Date()
format(today,myformat)
days <- mydates[2]-mydates[1]
days
as.character(dates)


ss.girl2
ss.girl3 <- ss.girl2[order(ss.girl2$体重,ss.girl2$身高),]
ss.girl3
ss.girl4 <- data.frame("姓名"=ss.girl3$姓名,mydata)
ss.girl4
ss.girl5 <- merge(ss.girl3,ss.girl4,by="姓名")
ss.girl5
new.ss <- ss.girl5[ss.girl5$height>=160,] 
new.ss <- new.ss[order(new.ss$weigh),]
new.ss

new.data11 <- subset(ss.girl5, weigh =< 50 |  height >= 160,
                   select=c("姓名","height","weight"))


new.d <- subset(new.ss, weigh<=50&height>=160,
                select = c("姓名", "height","weigh","出生日期"))
new.d
as.Date(new.d$出生日期)
mysample <- new.d[sample(1:nrow(new.d),4,replace = F),]
mysample
library("sampling")
library("survey")
install.packages("survey")
library("survey")
install.packages("sqldf")
library("sqldf")
new.d1 <- as.data.frame(new.d)
new.d2 <- as.list(new.d)
new.df <- sqldf("select*from x where weigh<45", row.names=T)
new.df
x <- new.d
