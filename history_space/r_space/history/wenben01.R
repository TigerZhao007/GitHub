#  英文文本挖掘程序

#  载入软件包
library("SnowballC")
library("tm")
library(wordcloud2)
library(tmcn)
library(Rwordseg)
library(jiebaR)

#  读取文本文件
readLines("trump.txt",encoding="UTF-8")
trump.read <- readLines("trump.txt")

#  将英文大小写一致化。
trump.read.to <- tolower(trump.read)            #toupper(trump.read)    #casefold(y)



#  将列表数据变为一个向量。
trump.read.to.paste <- paste(trump.read.to,collapse = " ")
          #trump.read.to.paste <- unlist(trump.read.to)   #不能完成以上操作。   
  
          #sub(pattern = ".", replacement = "", trump.read.to.paste)

          #?trump.read.to.paste.map<- tm_map(trump.read.to.paste, removeNumbers)
          #?trump.read.to.paste.map<- tm_map(trump.read.to.paste[1], removePunctuation)

#  将一段话进行分词
trump.read.to.paste.split <- strsplit(trump.read.to.paste, split=" ")[[1]]

#  去除其中的标点符号和数据。
trump.read.to.paste.split.gs <- gsub("[0-9 ０１２３４５６７８９ < > ~ 《 》 “ ” ，. ' : ,]","",trump.read.to.paste.split)

#  读取停词表。 
stopwords<- unlist(read.table("E:\\workspace\\tingcibiao\\Etingci01.txt",stringsAsFactors=F)) 
stopwords[1:100]                                #查看停词表。

#  剔除停词表中的内容。
removeStopWords <- function(x,stopwords) {  
  temp      <- character(0)  
  index     <- 1  
  xLen      <- length(x)  
  while (index <= xLen) {  
    if (length(stopwords[stopwords==x[index]]) <1)  
      temp  <- c(temp,x[index])  
    index   <- index +1  
  }  
  temp  
}  
trump.read.to.paste.split.la         <-lapply(trump.read.to.paste.split.gs,removeStopWords,stopwords)  #输出列表格式数据。
trump.read.to.paste.split.la.un      <- unlist(trump.read.to.paste.split.la)                     #将列表数据转为向量格式。

#  列表出各个词语频数，并排序（下降）。
trump.read.to.paste.split.table      <- table(trump.read.to.paste.split.la.un)
trump.read.to.paste.split.table.sort <- sort(trump.read.to.paste.split.table,decreasing = T)

#  画图（类似条形图）。
plot(trump.read.to.paste.split.table.sort,col="red")

#  画图（词云图）。
wordcloud2(trump.read.to.paste.split.table.sort, shape = "circle")
wordcloud2(trump.read.to.paste.split.table.sort, shape = "triangle")
