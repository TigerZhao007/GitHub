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

#读取停词表。
stopwords<- unlist(read.table("F:\\rspace\\history\\ciku\\tingcibiao\\Ctingci02.txt",stringsAsFactors=F))  

#  文本读取、挖掘、画图分析
#canlian <- readLines("F:\\rspace\\history\\canlian01.txt",encoding="GB2312")
#word <- canlian
canlian_frame <- read.csv('C:\\Users\\Think\\Desktop\\办学特色.csv',encoding = 'UTF-8')
word <- unlist(canlian_frame$text)

word



word          <- paste(word,collapse = " ")
word.se       <- segmentCN(word)
word.se.rm    <- lapply(word.se, removeStopWords,stopwords)
word.se.rm.un <- unlist(word.se.rm)
word.se.ta    <- table(word.se.rm.un)
word.se.ta.so <- sort(word.se.ta,decreasing = T)
wordcloud2(word.se.ta.so,shape='circle')

str(word.se.ta.so)



RI <- c(0, 0, 0.58, 0.9, 1.12, 1.24, 1.32, 1.41, 1.45, 1.49, 1.51,1.54,1.56,1.58,1.59,
        1.59,1.61,1.61,1.62,1.63,1.64,1.64,1.65,1.65,1.66,1.66,1.67,1.67,1.67,1.67,
        1.68,1.68,1.68,1.69,1.69,1.69,1.70,1.70,1.70,1.70)


RI <- c(0, 0, 0.58, 0.9, 1.12, 1.24, 1.32, 1.41, 1.45, 1.49, 1.51,1.54,1.56,1.58,1.59,
        1.59,1.61,1.61,1.62,1.63,1.64,1.64,1.65,1.65,1.66,1.66,1.67,1.67,1.67)
length(RI)
