library("xlsx")
data0 <- read.xlsx("txsj.xlsx",sheetName = "sheet1",encoding = "UTF-8")
data1 <- data0[,c(2,3,4,5)]

## -----------------------------------------------------------

# 第四部分数据处理
data.part4 <- data1[data1$ym==4,]
head(data.part4,50)

part4.b1 <- na.omit(data.part4[data.part4$bh=="b1",])
part4.b2 <- na.omit(data.part4[data.part4$bh=="b2",])
part4.b3 <- na.omit(data.part4[data.part4$bh=="b3",])
part4.b4 <- na.omit(data.part4[data.part4$bh=="b4",])
part4.b5 <- na.omit(data.part4[data.part4$bh=="b5",])
part4.b6 <- na.omit(data.part4[data.part4$bh=="b6",])
part4.b7 <- na.omit(data.part4[data.part4$bh=="b7",])
part4.b8 <- na.omit(data.part4[data.part4$bh=="b8",])
part4.b_sp <- na.omit(data.part4[data.part4$bh=="s_province",])
part4.b_sci <- na.omit(data.part4[data.part4$bh=="s_city",])
part4.b_sco <- na.omit(data.part4[data.part4$bh=="s_country",])


part4 <- merge(part4.b1,part4.b2,by="bfz",all = T)
part4 <- merge(part4,part4.b3,by="bfz",all = T)
part4 <- merge(part4,part4.b4,by="bfz",all = T)
part4 <- merge(part4,part4.b5,by="bfz",all = T)
part4 <- merge(part4,part4.b6,by="bfz",all = T)
part4 <- merge(part4,part4.b7,by="bfz",all = T)
part4 <- merge(part4,part4.b8,by="bfz",all = T)
part4 <- merge(part4,part4.b_sp,by="bfz",all = T)
part4 <- merge(part4,part4.b_sci,by="bfz",all = T)
part4 <- merge(part4,part4.b_sco,by="bfz",all = T)

part4 <- part4[,c(1,3,6,9,12,15,18,21,24,27,30,33)]
colnames(part4) <- c("bh","school_name","address","telphone","youbian","b5","b6","b7","b8","province","city","country")
head(part4)
nrow(part4)
ncol(part4)

## -----------------------------------------------------------

# 第五部分数据处理
data.part5 <- data1[data1$ym==5,]
head(data.part5,50)

part5.c1 <- na.omit(data.part5[data.part5$bh=="c1",])
part5.c2 <- na.omit(data.part5[data.part5$bh=="c2",])
part5.c3 <- na.omit(data.part5[data.part5$bh=="c3",])
part5.c4 <- na.omit(data.part5[data.part5$bh=="c4",])
part5.c5 <- na.omit(data.part5[data.part5$bh=="c5",])
part5.c6 <- na.omit(data.part5[data.part5$bh=="c6",])
part5.c7 <- na.omit(data.part5[data.part5$bh=="c7",])
part5.c8 <- na.omit(data.part5[data.part5$bh=="c8",])
part5.c9 <- na.omit(data.part5[data.part5$bh=="c9",])
part5.c10 <- na.omit(data.part5[data.part5$bh=="c10",])
part5.c11 <- na.omit(data.part5[data.part5$bh=="c11",])
part5.c12 <- na.omit(data.part5[data.part5$bh=="c12",])
part5.c13 <- na.omit(data.part5[data.part5$bh=="c13",])

part5 <- merge(part5.c1,part5.c2,by="bfz",all = T)
part5 <- merge(part5,part5.c3,by="bfz",all = T)
part5 <- merge(part5,part5.c4,by="bfz",all = T)
part5 <- merge(part5,part5.c5,by="bfz",all = T)
part5 <- merge(part5,part5.c6,by="bfz",all = T)
part5 <- merge(part5,part5.c7,by="bfz",all = T)
part5 <- merge(part5,part5.c8,by="bfz",all = T)
part5 <- merge(part5,part5.c9,by="bfz",all = T)
part5 <- merge(part5,part5.c10,by="bfz",all = T)
part5 <- merge(part5,part5.c11,by="bfz",all = T)
part5 <- merge(part5,part5.c12,by="bfz",all = T)
part5 <- merge(part5,part5.c13,by="bfz",all = T)

part5 <- part5[,c(1,3,6,9,12,15,18,21,24,27,30,33,36,39)]
colnames(part5) <- c("bh","c1","c2","c3","c4","c5","c6","c7","c8","c9","c10","c11","c12","c13")
head(part5)
nrow(part5)
ncol(part5)

## -----------------------------------------------------------

# 第六部分数据处理
data.part6 <- data1[data1$ym==6,]
head(data.part6,50)

part6.d1 <- na.omit(data.part6[data.part6$bh=="d1",])
part6.d2 <- na.omit(data.part6[data.part6$bh=="d2",])
part6.d3 <- na.omit(data.part6[data.part6$bh=="d3",])
part6.d4 <- na.omit(data.part6[data.part6$bh=="d4",])
part6.d5 <- na.omit(data.part6[data.part6$bh=="d5",])
part6.d6 <- na.omit(data.part6[data.part6$bh=="d6",])
part6.d7 <- na.omit(data.part6[data.part6$bh=="d7",])
part6.d8 <- na.omit(data.part6[data.part6$bh=="d8",])
part6.d9 <- na.omit(data.part6[data.part6$bh=="d9",])
part6.d10 <- na.omit(data.part6[data.part6$bh=="d10",])
part6.d11 <- na.omit(data.part6[data.part6$bh=="d11",])
part6.d12 <- na.omit(data.part6[data.part6$bh=="d12",])
part6.d13 <- na.omit(data.part6[data.part6$bh=="d13",])
part6.d14 <- na.omit(data.part6[data.part6$bh=="d14",])
part6.d15 <- na.omit(data.part6[data.part6$bh=="d15",])
part6.d16 <- na.omit(data.part6[data.part6$bh=="d16",])
part6.d17 <- na.omit(data.part6[data.part6$bh=="d17",])
part6.d18 <- na.omit(data.part6[data.part6$bh=="d18",])
part6.d19 <- na.omit(data.part6[data.part6$bh=="d19",])
part6.d20 <- na.omit(data.part6[data.part6$bh=="d20",])

part6 <- merge(part6.d1,part6.d2,by="bfz",all = T)
part6 <- merge(part6,part6.d3,by="bfz",all = T)
part6 <- merge(part6,part6.d4,by="bfz",all = T)
part6 <- merge(part6,part6.d5,by="bfz",all = T)
part6 <- merge(part6,part6.d6,by="bfz",all = T)
part6 <- merge(part6,part6.d7,by="bfz",all = T)
part6 <- merge(part6,part6.d8,by="bfz",all = T)
part6 <- merge(part6,part6.d9,by="bfz",all = T)
part6 <- merge(part6,part6.d10,by="bfz",all = T)
part6 <- merge(part6,part6.d11,by="bfz",all = T)
part6 <- merge(part6,part6.d12,by="bfz",all = T)
part6 <- merge(part6,part6.d13,by="bfz",all = T)
part6 <- merge(part6,part6.d14,by="bfz",all = T)
part6 <- merge(part6,part6.d15,by="bfz",all = T)
part6 <- merge(part6,part6.d16,by="bfz",all = T)
part6 <- merge(part6,part6.d17,by="bfz",all = T)
part6 <- merge(part6,part6.d18,by="bfz",all = T)
part6 <- merge(part6,part6.d19,by="bfz",all = T)
part6 <- merge(part6,part6.d20,by="bfz",all = T)

part6 <- part6[,c(1,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,60)]
colnames(part6) <- c("bh","d1","d2","d3","d4","d5","d6","d7","d8","d9","d10",
                     "d11","d12","d13","d14","d15","d16","d17","d18","d19","d20")
head(part6)
nrow(part6)
ncol(part6)

## -----------------------------------------------------------

# 第二章数据合并

unit2 <- merge(part4,part5, by="bh",all = T)
unit2 <- merge(unit2,part6, by="bh",all = T)
head(unit2)
nrow(unit2)
str(unit1)

# 第二章数据导出
write.csv(unit2,file = "特校数据_第二章.csv")

## --------------------------------------------------------

# 第二章数据分析

unit2.x <- read.xlsx("txsj_2.xlsx",sheetIndex = "sheet1",encoding = "UTF-8")
head(unit2.x)
nrow(unit2.x)
summary(unit2.x)
