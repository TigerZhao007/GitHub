library("RODBC")
connect <- odbcConnect("Rspace",uid = "sa",pwd = "sdk")
#sqlQuery(connect,"use Rspace
#create table [dbo].[sdk02]
#         ([ID][int]not null,[Name][nvarchar](50),[Age][int])")
install.packages("reshape2")
library("reshape2")
st.h <- sqlFetch(connect,"student_health")
head(st.h)
table(st.h)
summary(st.h)
st.h <- st.h[,1:11]
st.h1 <- na.omit(st.h)
st.h1
summary(st.h1)
table(st.h1$性别)
table(st.h1$年级编号)
table(st.h1$班号)
attach(st.h1)
head(st.h1)
names(st.h1)
names(st.h1) <- c("nj.bh","bj.bh","bj","xh","mz","name","sex","date","ID","heigh","weigh")
st.h2 <- st.h1[,10:11]
head(st.h2)

agg.data <- aggregate(st.h1[,10:11],by=list(bj.bh,st.h1$sex),FUN = mean, na.rm = TRUE)
length(bj.bh)
length(sex)
sex <- factor(sex)
st.h1$sex
agg.data <- aggregate(st.h1[,10:11],by=list(bj.bh),FUN = mean, na.rm = TRUE)
agg.data
names(agg.data)<-c("grade","sex","heigh.mean","weigh.mean")
mydata <- agg.data
md <- melt(mydata,id=c("grade","sex"))
md
md$value <-round(md$value,digits = 1)
md
dcast(md,grade+sex~variable)
dcast(md,grade~variable,mean)
dcast(md,sex~variable,mean)
aggregate(st.h1[,10:11],by=list(st.h1$sex),FUN = mean)
dcast(md,sex~grade,mean)
st.grade <- table(st.h1$bj.bh)
st.grade
barplot(st.grade,xlab = "grade",ylab = "the numble of student",
        main = "shanghai high school",sub = "the information of student health ",
        col.main = 2, col.lab = 3, col.sub= 4, fg= 5,bg=1,cex.axis = 1.5,col = rainbow(length(st.grade)))
barplot(st.grade,xlab = "grade",ylab = "the numble of student",
        main = "shanghai high school",sub = "the information of student health ",
        col.main = 2, col.lab = 3, col.sub= 4, fg= 5,bg=1,cex.axis = 1.5,
        col = rainbow(length(st.grade)),
        horiz = T)
st.gs <- aggregate(st.h1["bj.bh","sex"],by=list(st.h1$bj.bh,st.h1$sex),FUN=mean)
st.gs <- table(st.h1$sex,st.h1$bj.bh)
st.gs <- t(st.gs)
names(st.gs)<- c("boy", "girl")
st.gs
names(st.gs)
colnames(st.gs)<- c("boy", "girl")
barplot(st.gs,xlab = "grade",ylab = "the numble of student",
        main = "shanghai high school",sub = "the information of student health ",
        col.main = 2, col.lab = 3, col.sub= 4, fg= 5,bg=1,cex.axis = 1.5,
        col = rainbow(length(st.grade)),
        horiz = T,legend=rownames(st.gs),beside = T)
st.bh <- aggregate(st.h1$heigh,by=list(st.h1$bj.bh),FUN = mean)
st.bh
st.bhs <- st.bh[order(st.bh$x),]
st.bhs
barplot(st.bhs$x,xlab = "grade",ylab = "the numble of student",
        main = "shanghai high school",sub = "the information of student health ",
        col.main = 2, col.lab = 3, col.sub= 4, fg= 5,bg=1,cex.axis = 1.5,
        col = rainbow(length(st.bhs$Group.1)),cex.names = 0.8,cex.lab=1,
        cex.sub = 1,cex.main = 1.5,
        horiz = F,names.arg = st.bhs$Group.1,beside = T)
box()
library("vcd")
attach(st.h1)
rm("sex")
spine(t(st.gs),main = "sss")
pie(st.bhs$x, main = "shanghai high school",sub = "the information of student health ",
    col.main = 2, col.lab = 3, col.sub= 4, fg= 5,bg=1,cex.axis = 1.5,cex.names = 0.8,cex.lab=1,
    cex.sub = 1,cex.main = 1.5,
    col = rainbow(length(st.bhs$x)),
    labels = st.bhs$Group.1,beside = T)


pie3D(st.bhs$x, main = "shanghai high school",sub = "the information of student health ",
      col.main = 2, col.lab = 3, col.sub= 4, fg= 5,bg=1,cex.axis = 1.5,cex.names = 0.8,cex.lab=1,
      cex.sub = 1,cex.main = 1.5,
      col = rainbow(length(st.bhs$x)),
      labels = st.bhs$Group.1,beside = T,explode = 0.1)
hj<- st.bhs$Group.1
as.character(hj)
library("plotrix")
install.packages("plotrix")
fan.plot(st.bhs$x, main = "shanghai high school",labels = as.character(hj))
windows()
hist(st.h1$heigh, main = "shanghai high school",
     breaks=5,
     sub = "the information of student health ")
     # rug plot ,density curve)
dev.off()
box()
lines(density(st.h1$heigh),col=2)
warnings()


d <- density(st.h1$heigh)
plot(d)
polygon(d,col=2,border = 4)
rug(st.h1$heigh)
library("sm")
install.packages("sm")
sm.density.compare(st.h1$heigh,st.h1$bj.bh)
legend(locator(2),levels(st.h1$bj.bh),fill = colfill)

head(st.h1)
boxplot(st.h1$heigh~st.h1$sex)
library("vioplot")
install.packages("vioplot")
vioplot(st.h1$heigh~st.h1$sex)
library("sql")
library("RSQLite")
library("sqldf")
st_h1 <- st.h1
x1 <- sqldf("select heigh from st_h1 where  sex=1 ",row.names=T)

head(x1)
x2 <- sqldf("select heigh from st_h1 where sex=2")
head(x2)
unlist(x2)
vioplot(unlist(x1),unlist(x2),names = c("x1 boy", "x2 girl"),col= "gold")
dotchart(order(unlist(x2)))
head(st.h2)
rownames(st.h2) <- st.h1$name
summary(st.h2)
library("Hmisc")
pastecs::describe(st.h2)
library("pastecs")
install.packages("pastecs")
stat.desc(st.h2)
describe(st.h2)
library("psych")
install.packages("psych")
