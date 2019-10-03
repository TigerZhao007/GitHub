#  中文文本挖掘程序


#  调入程序包。
library(rJava)
library(Rwordseg)
library(wordcloud2)
library(tmcn)
library(jiebaR)


#  简单的分词程序。
segmentCN("这是个中文分词软件。")                  #分词程序。    
segmentCN("这是个中文分词软件。",nosymbol=FALSE)   #输出标点符号。
segmentCN("这是个中文分词软件。",nature=TRUE)      #输出词性。

#  人名识别功能。
getOption("isNameRecognition")                     #判断是否具有人名识别功能。
segmentCN("刘强东是个好学生。")     
segment.options(isNameRecognition=TRUE)            #具有人名识别功能。
segment.options(isNameRecognition=FALSE)           #去掉人名识别功能。

#  向字典中加入某些词语。
listDict()
segmentCN("这是个分词软件。")
insertWords("这是")                               #向字典中加入“这是”词语。
insertWords("特校")                               #加入词库后可以应用识别。
listDict()

#  向字典中加入某词库。
installDict(dictpath = "canlianciku01.txt",
            dictname = "dep",dicttype = "text",load = "TRUE")      #向字典中加入文件中的词语。
                                                
segmentCN("2015年的几部开年戏都出现了唐嫣的身影")  
installDict(dictpath = "E:\\workspace\\ciku\\canjirenshiye.scel",
            dictname ="canjiren") 
warnings()                                       #查看警告内容。
listDict()                                       #查看R语言中词库列表。
uninstallDict()                                  #删除全部自定义词库

#  将字典中部分词语拆开。
insertWords("错过")       
segmentCN(c("如果你因为错过太阳而流泪", "你也会错过星星"))  
segmentCN("这个错过去你可以犯，但是现在再犯就不应该了") 
deleteWords("错过")  
insertWords("过去")  
segmentCN("这个错过去你可以犯，但是现在再犯就不应该了")  

deleteWords(c("和","的","是","对","2020"))
deleteWords("特殊")
segmentCN("这是个特殊教育学校校长公共事业分词软件。")

#  将字典中的部分数据和符号删去。
fenci <- c("2015年的几部开年戏都出现了唐嫣的身影,《华丽柏拉图》演绎的很好，很“南财”。")
fenci.seg <- segmentCN("2015年的几部开年戏都出现了唐嫣的身影,10《华丽柏拉图》演绎的很好，很“南财”。")
fenci.gsub <- gsub("[0-9 ０１２３４５６７８９ < > ~ 《 》 “ ” ， ,]","",fenci)   
                                                 #0-9删除大于10的数据。
segmentCN(fenci.gsub)

#  将字典中的部分词语、停词删去。
fenci.gsub <- gsub("[的 很 了 年]","",fenci)     #删去部分词语。
stopwords<- unlist(read.table("E:\\rspace\\ciku\\tingcibiao\\Ctingci02.txt",stringsAsFactors=F)) 
                                                 #读取停词表。
stopwords[1:100]                                 #查看停词表。

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
fenci.remove           <-lapply(fenci.seg,removeStopWords,stopwords)  #输出列表格式数据。
fenci.remove.un        <- unlist(fenci.remove)                     #将列表数据转为向量格式。


#  文本读取、挖掘、画图分析
canlian <- readLines("canlian01.txt",encoding="GB2312")
canlian


canlian.paste          <- paste(canlian,collapse = " ")
canlian.paste.se       <- segmentCN(canlian.paste)
canlian.paste.se.rm    <- lapply(canlian.paste.se, removeStopWords,stopwords)
canlian.paste.se.rm.un <- unlist(canlian.paste.se.rm)
canlian.paste.se.ta    <- table(canlian.paste.se.rm.un)
canlian.paste.se.ta.so <- sort(canlian.paste.se.ta,decreasing = T)
length(canlian.paste.se.ta.so[1:100])

wordcloud2(canlian.paste.se.ta.so[1:100])





