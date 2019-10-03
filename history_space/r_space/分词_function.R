if(!require(Rwordseg)){install.packages("Rwordseg")}
if(!require(wordcloud2)){install.packages("wordcloud2")}
if(!require(tmcn)){install.packages("tmcn")}
if(!require(jiebaR)){install.packages("jiebaR")}
if(!require(rJava)){install.packages("rJava")}

# 去词函数
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

word_split <- function(text1, stopwords){
  word          <- paste(text1,collapse = " ")
  word.se       <- segmentCN(word)
  word.se.rm    <- lapply(word.se, removeStopWords,stopwords)
  word.se.rm.un <- unlist(word.se.rm)
  word.se.ta    <- table(word.se.rm.un)
  word.se.ta.so <- sort(word.se.ta,decreasing = T)
#  wordcloud2(word.se.ta.so[1:n],shape)
#  return(list(word_list = word.se.ta.so,word_text = text, wordstop = stopwords, wordsinsert = insertWords))
  return(word.se.ta.so) 
}
stopwords<- unlist(read.table("F:\\rspace\\history\\ciku\\tingcibiao\\Ctingci02.txt",stringsAsFactors=F))   #读取停词表。

#  文本读取、挖掘、画图分析
canlian <- readLines("F:\\rspace\\history\\canlian01.txt",encoding="GB2312")
result <- word_split(canlian, stopwords=stopwords)
wordcloud2(result[1:100])

# 特校
library(xlsx)
dat <- read.xlsx('F:/特殊教育学校评估项目二期/词频数据_各项备注.xlsx',sheetIndex = "Sheet2",encoding = "UTF-8")
dat_q <- read.xlsx('F:/特殊教育学校评估项目二期/词频数据_各项备注.xlsx',sheetIndex = "Sheet3",encoding = "UTF-8")

names(dat)

lis <- list()
for (i in 3:length(names(dat))) {
  result   <- word_split(dat[,names(dat)[i]], stopwords=stopwords)
  lis[[i]] <- result
}
lis_q <- list()
for (i in 3:length(names(dat))) {
  result   <- lis[[i]][-which(names(lis[[i]]) %in% names(table(dat_q[,i])))]
  lis_q[[i]] <- result
}
lis_q
names(dat)
n=3
names(dat)[n]
wordcloud2(lis_q[[n]][-c(2,3)], size = 2, fontFamily = "微软雅黑",color = "random-light", backgroundColor = "grey")





#------------------####################----------------------------#########
plot1 <- wordcloud2(lis_q[[3]], size = 2, fontFamily = "微软雅黑",
                color = "random-light", backgroundColor = "grey")
plot1

# 保存图片？？？？？？？？？？？？？？？？？？？？？？？、、
png(file="C:/Users/Think/Desktop/myplot.png", bg='white')
plot1
dev.off()

