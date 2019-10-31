library("xlsx")
library("reshape2")
data0 <- read.xlsx("txsj.xlsx",sheetName = "sheet1",encoding = "UTF-8")
data1 <- data0[,c(2,3,4,5)]

## -----------------------------------------------------------

# 第一部分数据处理
data.part1 <- data1[data1$ym==1,]
head(data.part1,50)
part1.a1 <- na.omit(data.part1[data.part1$bh=="a1",])
part1.a2 <- na.omit(data.part1[data.part1$bh=="a2",])
part1.a3 <- na.omit(data.part1[data.part1$bh=="a3",])
part1.a4 <- na.omit(data.part1[data.part1$bh=="a4",])
part1.a5 <- na.omit(data.part1[data.part1$bh=="a5",])
part1.a6 <- na.omit(data.part1[data.part1$bh=="a6",])
part1.a7 <- na.omit(data.part1[data.part1$bh=="a7",])
part1.a8 <- na.omit(data.part1[data.part1$bh=="a8",])
part1.a9 <- na.omit(data.part1[data.part1$bh=="a9",])
part1.a10 <- na.omit(data.part1[data.part1$bh=="a10",])


part1 <- merge(part1.a1,part1.a2,by="bfz",all = T)
part1 <- merge(part1,part1.a3,by="bfz",all = T)
part1 <- merge(part1,part1.a4,by="bfz",all = T)
part1 <- merge(part1,part1.a5,by="bfz",all = T)
part1 <- merge(part1,part1.a6,by="bfz",all = T)
part1 <- merge(part1,part1.a7,by="bfz",all = T)
part1 <- merge(part1,part1.a8,by="bfz",all = T)
part1 <- merge(part1,part1.a9,by="bfz",all = T)
part1 <- merge(part1,part1.a10,by="bfz",all = T)


part1 <- part1[,c(1,3,6,9,12,15,18,21,24,27,30)]
colnames(part1) <- c("bh", "name", "sex", "age", "degree", "phone.num", "qq", "youxiang","zhicheng","nianzi","nianxian")
head(part1)
nrow(part1)

# 第二部分数据处理
data.part2 <- data1[data1$ym==2,]
head(data.part2,50);
part2.b1 <- na.omit(data.part2[data.part2$bh=="b1",])
part2.b2 <- na.omit(data.part2[data.part2$bh=="b2",])
part2.b3 <- na.omit(data.part2[data.part2$bh=="b3",])
part2.b4 <- na.omit(data.part2[data.part2$bh=="b4",])
part2.b5 <- na.omit(data.part2[data.part2$bh=="b5",])
part2.b6 <- na.omit(data.part2[data.part2$bh=="b6",])
part2.b7 <- na.omit(data.part2[data.part2$bh=="b7",])
part2.b8 <- na.omit(data.part2[data.part2$bh=="b8",])
part2.b9 <- na.omit(data.part2[data.part2$bh=="b9",])
part2.b10 <- na.omit(data.part2[data.part2$bh=="b10",])
part2.b11 <- na.omit(data.part2[data.part2$bh=="b11",])

part2 <- merge(part2.b1,part2.b2,by="bfz",all = T)
part2 <- merge(part2, part2.b3,by="bfz",all = T)
part2 <- merge(part2, part2.b4,by="bfz",all = T)
part2 <- merge(part2, part2.b5,by="bfz",all = T)
part2 <- merge(part2, part2.b6,by="bfz",all = T)
part2 <- merge(part2, part2.b7,by="bfz",all = T)
part2 <- merge(part2, part2.b8,by="bfz",all = T)
part2 <- merge(part2, part2.b9,by="bfz",all = T)
part2 <- merge(part2, part2.b10,by="bfz",all = T)
part2 <- merge(part2, part2.b11,by="bfz",all = T)

part2 <- part2[,c(1,3,6,9,12,15,18,21,24,27,30,33)]
colnames(part2) <- c("bh", "b1", "b2", "b3", "b4", "b5", "b6", "b7","b8","b9","b10","b11")
head(part2)
nrow(part2)

# 第三部分数据处理
data.part3 <- data1[data1$ym==3,]
head(data.part3,50)
part3.c1 <- na.omit(data.part3[data.part3$bh=="c1",],all = T)
part3.c2 <- na.omit(data.part3[data.part3$bh=="c2",],all = T)
part3.c3 <- na.omit(data.part3[data.part3$bh=="c3",],all = T)
part3.c4 <- na.omit(data.part3[data.part3$bh=="c4",],all = T)


part3 <- merge(part3.c1,part3.c2,by="bfz")
part3 <- merge(part3, part3.c3,by="bfz")
part3 <- merge(part3, part3.c4,by="bfz")

part3 <- part3[,c(1,3,6,9,12)]
colnames(part3) <- c("bh", "c1", "c2", "c3", "c4")
head(part3)
nrow(part3)

## 第一章数据合并

unit1 <- merge(part1,part2, by="bh",all = T)
unit1 <- merge(unit1,part3, by="bh",all = T)
head(unit1)
nrow(unit1)
unit1$age <- as.character(unit1$age)
unit1$age <- as.numeric(unit1$age)
str(unit1)

# 第一章数据导出
write.csv(unit1,file = "特校数据_第一章.csv")

## --------------------------------------------
# 第一部分数据分析
unit1.x <- read.xlsx("txsj_1.xlsx",sheetIndex = "sheet1",encoding = "UTF-8")
head(unit1.x)
nrow(unit1.x)
summary(unit1.x[,c(10,11,12)])


## --------------------------------------------
# 培训组织期望

unit1.x$c1

stopwords<- unlist(read.table("E:\\rspace\\ciku\\tingcibiao\\Ctingci02.txt",stringsAsFactors=F)) 
#读取停词表。
removeStopWords <- function(x,stopwords) {  
  temp <- character(0)  
  index <- 1  
  xLen <- length(x)  
  while (index <= xLen) {  
    if (length(stopwords[stopwords==x[index]]) <1)  
      temp<- c(temp,x[index])  
    index <- index +1  
  }  
  temp  
} 
#  文本读取、挖掘、画图分析
canlian.paste          <- paste(unit1.x$c4,collapse = " ")
canlian.paste.se       <- segmentCN(canlian.paste)
canlian.paste.se.rm    <- lapply(canlian.paste.se, removeStopWords,stopwords)
canlian.paste.se.rm.un <- unlist(canlian.paste.se.rm)
canlian.paste.se.ta    <- table(canlian.paste.se.rm.un)
canlian.paste.se.ta.so <- sort(canlian.paste.se.ta,decreasing = T)
str(canlian.paste.se.ta.so)
wordcloud2(canlian.paste.se.ta.so[c(10:400)])


write.table(canlian.paste,file = "c4.txt")



















