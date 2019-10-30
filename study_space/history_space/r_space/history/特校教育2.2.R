
## ---------------------------------------------------

# 第七部分数据处理
data.part7 <- data1[data1$ym==7,]
head(data.part7,50)

part7.e1 <- na.omit(data.part7[data.part7$bh=="e1",])
part7.e2 <- na.omit(data.part7[data.part7$bh=="e2",])
part7.e3 <- na.omit(data.part7[data.part7$bh=="e3",])
part7.e4 <- na.omit(data.part7[data.part7$bh=="e4",])
part7.e5 <- na.omit(data.part7[data.part7$bh=="e5",])
part7.e6 <- na.omit(data.part7[data.part7$bh=="e6",])
part7.e7 <- na.omit(data.part7[data.part7$bh=="e7",])
part7.e8 <- na.omit(data.part7[data.part7$bh=="e8",])
part7.e9 <- na.omit(data.part7[data.part7$bh=="e9",])
part7.e10 <- na.omit(data.part7[data.part7$bh=="e10",])
part7.e11 <- na.omit(data.part7[data.part7$bh=="e11",])
part7.e12 <- na.omit(data.part7[data.part7$bh=="e12",])
part7.e13 <- na.omit(data.part7[data.part7$bh=="e13",])
part7.e14 <- na.omit(data.part7[data.part7$bh=="e14",])

part7 <- merge(part7.e1,part7.e2,by="bfz",all = T)
part7 <- merge(part7,part7.e3,by="bfz",all = T)
part7 <- merge(part7,part7.e4,by="bfz",all = T)
part7 <- merge(part7,part7.e5,by="bfz",all = T)
part7 <- merge(part7,part7.e6,by="bfz",all = T)
part7 <- merge(part7,part7.e7,by="bfz",all = T)
part7 <- merge(part7,part7.e8,by="bfz",all = T)
part7 <- merge(part7,part7.e9,by="bfz",all = T)
part7 <- merge(part7,part7.e10,by="bfz",all = T)
part7 <- merge(part7,part7.e11,by="bfz",all = T)
part7 <- merge(part7,part7.e12,by="bfz",all = T)
part7 <- merge(part7,part7.e13,by="bfz",all = T)
part7 <- merge(part7,part7.e14,by="bfz",all = T)

part7 <- part7[,c(1,3,6,9,12,15,18,21,24,27,30,33,36,39,42)]
colnames(part7) <- c("bh",paste("e",1:14))
head(part7)
nrow(part7)
ncol(part7)

## ---------------------------------------------------

# 第八部分数据处理
data.part8 <- data1[data1$ym==8,]
head(data.part8,50)

part8.f1 <- na.omit(data.part8[data.part8$bh=="f1",])
part8.f2 <- na.omit(data.part8[data.part8$bh=="f2",])
part8.f3 <- na.omit(data.part8[data.part8$bh=="f3",])
part8.f4 <- na.omit(data.part8[data.part8$bh=="f4",])
part8.f5 <- na.omit(data.part8[data.part8$bh=="f5",])
part8.f6 <- na.omit(data.part8[data.part8$bh=="f6",])
part8.f7 <- na.omit(data.part8[data.part8$bh=="f7",])


part8 <- merge(part8.f1,part8.f2,by="bfz",all = T)
part8 <- merge(part8,part8.f3,by="bfz",all = T)
part8 <- merge(part8,part8.f4,by="bfz",all = T)
part8 <- merge(part8,part8.f5,by="bfz",all = T)
part8 <- merge(part8,part8.f6,by="bfz",all = T)
part8 <- merge(part8,part8.f7,by="bfz",all = T)

part8 <- part8[,c(1,3,6,9,12,15,18,21)]
colnames(part8) <- c("bh","f1","f2","f3","f4","f5","f6","f7")
head(part8)
nrow(part8)
ncol(part8)

## ---------------------------------------------------

# 第九部分数据处理
data.part9 <- data1[data1$ym==9,]
head(data.part9,50)

part9.g1 <- na.omit(data.part9[data.part9$bh=="g1",])
part9.g2 <- na.omit(data.part9[data.part9$bh=="g2",])
part9.g3 <- na.omit(data.part9[data.part9$bh=="g3",])
part9.g4 <- na.omit(data.part9[data.part9$bh=="g4",])
part9.g5 <- na.omit(data.part9[data.part9$bh=="g5",])
part9.g6 <- na.omit(data.part9[data.part9$bh=="g6",])
part9.g7 <- na.omit(data.part9[data.part9$bh=="g7",])
part9.g8 <- na.omit(data.part9[data.part9$bh=="g8",])
part9.g9 <- na.omit(data.part9[data.part9$bh=="g9",])

part9 <- merge(part9.g1,part9.g2,by="bfz",all = T)
part9 <- merge(part9,part9.g3,by="bfz",all = T)
part9 <- merge(part9,part9.g4,by="bfz",all = T)
part9 <- merge(part9,part9.g5,by="bfz",all = T)
part9 <- merge(part9,part9.g6,by="bfz",all = T)
part9 <- merge(part9,part9.g7,by="bfz",all = T)
part9 <- merge(part9,part9.g8,by="bfz",all = T)
part9 <- merge(part9,part9.g9,by="bfz",all = T)

part9           <- part9[,c(1,3,6,9,12,15,18,21,24,27)]
colnames(part9) <- c("bh","g1","g2","g3","g4","g5","g6","g7","g8","g9")
head(part9)
nrow(part9)
ncol(part9)

## ---------------------------------------------------

# 第十部分数据处理
data.part10 <- data1[data1$ym==10,]
head(data.part10,50)

part10.h1 <- na.omit(data.part10[data.part10$bh=="h1",])
part10.h2 <- na.omit(data.part10[data.part10$bh=="h2",])
part10.h3 <- na.omit(data.part10[data.part10$bh=="h3",])
part10.h4 <- na.omit(data.part10[data.part10$bh=="h4",])

part10 <- merge(part10.h1,part10.h2,by="bfz",all = T)
part10 <- merge(part10,part10.h3,by="bfz",all = T)
part10 <- merge(part10,part10.h4,by="bfz",all = T)

part10           <- part10[,c(1,3,6,9,12)]
colnames(part10) <- c("bh","f1","f2","f3","f4")
head(part10)
nrow(part10)
ncol(part10)

## ---------------------------------------------------

# 第十一部分数据处理
data.part11 <- data1[data1$ym==11,]
head(data.part11,50)

part11.i1 <- na.omit(data.part11[data.part11$bh=="i1",])
part11.i2 <- na.omit(data.part11[data.part11$bh=="i2",])
part11.i3 <- na.omit(data.part11[data.part11$bh=="i3",])
part11.i4 <- na.omit(data.part11[data.part11$bh=="i4",])
part11.i5 <- na.omit(data.part11[data.part11$bh=="i5",])
part11.i6 <- na.omit(data.part11[data.part11$bh=="i6",])
part11.i7 <- na.omit(data.part11[data.part11$bh=="i7",])
part11.i8 <- na.omit(data.part11[data.part11$bh=="i8",])
part11.i9 <- na.omit(data.part11[data.part11$bh=="i9",])
part11.i10 <- na.omit(data.part11[data.part11$bh=="i10",])
part11.i11 <- na.omit(data.part11[data.part11$bh=="i11",])
part11.i12 <- na.omit(data.part11[data.part11$bh=="i12",])

part11 <- merge(part11.i1,part11.i2,by="bfz",all = T)
part11 <- merge(part11,part11.i3,by="bfz",all = T)
part11 <- merge(part11,part11.i4,by="bfz",all = T)
part11 <- merge(part11,part11.i5,by="bfz",all = T)
part11 <- merge(part11,part11.i6,by="bfz",all = T)
part11 <- merge(part11,part11.i7,by="bfz",all = T)
part11 <- merge(part11,part11.i8,by="bfz",all = T)
part11 <- merge(part11,part11.i9,by="bfz",all = T)
part11 <- merge(part11,part11.i10,by="bfz",all = T)
part11 <- merge(part11,part11.i11,by="bfz",all = T)
part11 <- merge(part11,part11.i12,by="bfz",all = T)

part11           <- part11[,c(1,3,6,9,12,15,18,21,24,27,30,33,36)]
colnames(part11) <- c("bh","f1","f2","f3","f4","f5","f6","f7","f8","f9","f10","f11","f12")
head(part11)
nrow(part11)
ncol(part11)

## ---------------------------------------------------

# 第十一部分数据处理
data.part12 <- data1[data1$ym==12,]
head(data.part12,50)

part12.j1 <- na.omit(data.part12[data.part12$bh=="j1",])
part12.j2_a <- na.omit(data.part12[data.part12$bh=="j2_a",])
part12.j2_b <- na.omit(data.part12[data.part12$bh=="j2_b",])
part12.j2_c <- na.omit(data.part12[data.part12$bh=="j2_c",])
part12.j2_d <- na.omit(data.part12[data.part12$bh=="j2_d",])
part12.j2_e <- na.omit(data.part12[data.part12$bh=="j2_e",])
part12.j2_f <- na.omit(data.part12[data.part12$bh=="j2_f",])
part12.j2_g <- na.omit(data.part12[data.part12$bh=="j2_g",])
part12.j2_h <- na.omit(data.part12[data.part12$bh=="j2_h",])
part12.j2_i <- na.omit(data.part12[data.part12$bh=="j2_i",])
part12.j2_j <- na.omit(data.part12[data.part12$bh=="j2_j",])
part12.j3 <- na.omit(data.part12[data.part12$bh=="j3",])
part12.j4 <- na.omit(data.part12[data.part12$bh=="j4",])
part12.j5_a <- na.omit(data.part12[data.part12$bh=="j5_a",])
part12.j5_b <- na.omit(data.part12[data.part12$bh=="j5_b",])
part12.j5_c <- na.omit(data.part12[data.part12$bh=="j5_c",])
part12.j5_d <- na.omit(data.part12[data.part12$bh=="j5_d",])
part12.j5_e <- na.omit(data.part12[data.part12$bh=="j5_e",])
part12.j5_f <- na.omit(data.part12[data.part12$bh=="j5_f",])
part12.j5_g <- na.omit(data.part12[data.part12$bh=="j5_g",])
part12.j5_h <- na.omit(data.part12[data.part12$bh=="j5_h",])
part12.j5_i <- na.omit(data.part12[data.part12$bh=="j5_i",])
part12.j5_j <- na.omit(data.part12[data.part12$bh=="j5_j",])

part12 <- merge(part12.j1,part12.j2_a,by="bfz",all = T)
part12 <- merge(part12,part12.j2_b,by="bfz",all = T)
part12 <- merge(part12,part12.j2_c,by="bfz",all = T)
part12 <- merge(part12,part12.j2_d,by="bfz",all = T)
part12 <- merge(part12,part12.j2_e,by="bfz",all = T)
part12 <- merge(part12,part12.j2_f,by="bfz",all = T)
part12 <- merge(part12,part12.j2_g,by="bfz",all = T)
part12 <- merge(part12,part12.j2_h,by="bfz",all = T)
part12 <- merge(part12,part12.j2_i,by="bfz",all = T)
part12 <- merge(part12,part12.j2_j,by="bfz",all = T)
part12 <- merge(part12,part12.j3,by="bfz",all = T)
part12 <- merge(part12,part12.j4,by="bfz",all = T)
part12 <- merge(part12,part12.j5_a,by="bfz",all = T)
part12 <- merge(part12,part12.j5_b,by="bfz",all = T)
part12 <- merge(part12,part12.j5_c,by="bfz",all = T)
part12 <- merge(part12,part12.j5_d,by="bfz",all = T)
part12 <- merge(part12,part12.j5_e,by="bfz",all = T)
part12 <- merge(part12,part12.j5_f,by="bfz",all = T)
part12 <- merge(part12,part12.j5_g,by="bfz",all = T)
part12 <- merge(part12,part12.j5_h,by="bfz",all = T)
part12 <- merge(part12,part12.j5_i,by="bfz",all = T)
part12 <- merge(part12,part12.j5_j,by="bfz",all = T)


part12           <- part12[,c(1,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,60,63,66,69)]
colnames(part12) <- c("bh","f1","f2_a","f2_b","f2_c","f2_d","f2_e","f2_f","f2_g","f2_h","f2_i","f2_j",
                      "f3","f4","f5_a","f5_b","f5_c","f5_d","f5_e","f5_f","f5_g","f5_h","f5_i","f5_j")
head(part12)
nrow(part12)
ncol(part12)

## -------------------------------------------

# 所有数据汇总
head(part1)
part_z <- merge(part1,part2,by="bh",all = T)
part_z <- merge(part_z,part3,by="bh",all = T)
part_z <- merge(part_z,part4,by="bh",all = T)
part_z <- merge(part_z,part5,by="bh",all = T)
part_z <- merge(part_z,part6,by="bh",all = T)
part_z <- merge(part_z,part7,by="bh",all = T)
part_z <- merge(part_z,part8,by="bh",all = T)
part_z <- merge(part_z,part9,by="bh",all = T)
part_z <- merge(part_z,part10,by="bh",all = T)
part_z <- merge(part_z,part11,by="bh",all = T)
part_z <- merge(part_z,part12,by="bh",all = T)

head(part_z)
fix(part_z)
names(part_z)

## -------------------------------------------
unit.3 <- part_z[,23:26]
fix(unit.3)

keywords2 <- c("")

# 根据选词挖掘
mat2 <- data.frame(matrix(0,ncol=length(keywords1),nrow=length(phone_type1$uid)))
colnames(mat2) <- keywords1
# rownames(mat2) <- phone_type1$uid
getkey <- function(word){return(as.integer(regexpr(word,phone_type1$source)>0))}
mat2 <- sapply(phone.type2,getkey)
rownames(mat2) <- phone_type1
mat2
fix(mat2)

#  文本读取、挖掘、画图分析
# 划分词库
canlian_ciku <- 
insertWords(canlian_ciku)
# 停词表
stopwords <- unlist(read.table("E:\\rspace\\ciku\\tingcibiao\\Ctingci02.txt",stringsAsFactors=F)) 
# 分词程序
canlian.paste          <- paste(unit.3$c4.x,collapse = " ")
canlian.paste.se       <- segmentCN(canlian.paste)
canlian.paste.se.rm    <- lapply(canlian.paste.se, removeStopWords,stopwords)
canlian.paste.se.rm.un <- unlist(canlian.paste.se.rm)
canlian.paste.se.ta    <- table(canlian.paste.se.rm.un)
canlian.paste.se.ta.so <- sort(canlian.paste.se.ta,decreasing = T)
wordcloud2(canlian.paste.se.ta.so[c(1:100)])

write.table(canlian.paste.se.ta.so, "残联分词.txt")
