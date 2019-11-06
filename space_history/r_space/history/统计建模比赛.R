library("xlsx")
library("Rwordseg")
library(rJava)
library(Rwordseg)
library(wordcloud2)
library(tmcn)
library(jiebaR)

weibo1 <- read.csv("weibo_comments.csv",
                   header =TRUE,stringsAsFactors = FALSE)
str(weibo1)
head(weibo1)
fix(weibo1)

## --------------------------------
weibo3 <- substr(weibo1[ ,5], 1, 2)
str(weibo3)
head(weibo3, 20)
weibo4 <- weibo1[which(weibo3 != "回复"), 5]
str(weibo4)
head(weibo4)
fix(weibo4)

fix(weibo1)
data.sample <- head(weibo4,5)
data.sample <- unlist(data.sample)
data.sample <- lapply(data.sample, segmentCN)
segmentCN(data.sample)

stopwords <- c("有人","人情")

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

data.sample1 <- lapply(data.sample, removeStopWords, stopwords)
data.sample1 <- unlist(data.sample1)
str(data.sample1)
data.sample2 <- paste(data.sample1, "")
data.sample2 <- lapply(data.sample1, paste," ")

## ----------------------------------------

# 手机类型原始数据
phone_type <- weibo1[, c(4,7)] 
head(phone_type)

# ID索引&选择非重复数据
index<-duplicated(phone_type$user_id)  
head(index,100) 
phone_type1 <-phone_type[!index,]  #选中了非重复的数据  
head(phone_type1,100)  

stopwords<- unlist(read.table("C:\\Users\\SDK\\Desktop\\a.txt")) 
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
# 手机类型统计
x.paste          <- paste(phone_type1$source,collapse = " ")
x.paste          <- tolower(x.paste)
x.paste.se       <- segmentCN(x.paste)
x.paste.se.rm    <- lapply(x.paste.se, removeStopWords,stopwords)
x.paste.se.rm.un <- unlist(x.paste.se.rm)
x.paste.se.ta    <- table(x.paste.se.rm.un)
x.paste.se.ta.so <- sort(x.paste.se.ta,decreasing = T)
length(x.paste.se.ta.so)

wordcloud2(x.paste.se.ta.so)
fix(x.paste.se.ta.so)
hist(x.paste.se.ta.so)


write.table(x.paste.se.ta.so,"C:\\Users\\SDK\\Desktop\\a.txt")

str(x.paste.se.ta.so)

## --------------------------------------------------
# 数据读取&筛选
weibo1 <- read.csv("C:\\Users\\SDK\\Desktop\\创新项目\\weibo_comments.csv",
                   header =TRUE,stringsAsFactors = FALSE)
str(weibo1)
weibo3 <- substr(weibo1[ ,5], 1, 2)
weibo4 <- weibo1[which(weibo3 != "回复"), 5]
weibo5 <- gsub("<.*>", "", weibo4)
head(weibo5)
tail(weibo5)

# 处理时间数据
str(weibo1$time)
head(weibo1$time)
weibo.time <- weibo1$time[3586:9527]
str(weibo.time)
weibo.time1 <- as.POSIXlt(weibo.time, format="%m-%d %H:%M")
head(weibo.time1)
weibo.time2 <- sort(weibo.time1)
head(weibo.time2)
str(weibo.time2)
hist(weibo.time2, breaks = 48)

# 手机类型原始数据
phone_type <- weibo1[, c(4,7)] 
head(phone_type)


# 处理性别、所在地
weibo.people <- read.csv("C:\\Users\\SDK\\Desktop\\创新项目\\weibo-fans.csv", 
                         stringsAsFactors = FALSE, header = TRUE)
str(weibo.people)
table(weibo.people[ , 2])
head(weibo.people[ , 3], 20)
table(weibo.people[ , 3])
weibo.address <- substr(weibo.people[ ,3], 1, 2)
str(weibo.address)
table(weibo.address)
sort(table(weibo.address))

## ----------------------------------------------------

# ID索引&选择非重复数据
weibo1 <- read.xlsx("C:\\Users\\SDK\\Desktop\\new_weiboxl1.xlsx",sheetIndex = "Sheet1",
                   header =TRUE,stringsAsFactors = FALSE,encoding = "UTF-8")
head(weibo1)
fix(weibo1)
phone_type <- weibo1[, c(1,5)] 
head(phone_type)

index<-duplicated(phone_type$uid)  
head(index,100) 
phone_type1 <-na.omit(phone_type[!index,])  #选中了非重复的数据  
head(phone_type1,100)  

# 词库设置和安装
phone.type <- read.csv(file="C:/Users/SDK/Desktop/phone.csv",
                       stringsAsFactors = FALSE)
write.table(phone.type,"C:/Users/SDK/Desktop/phone.csv")
str(phone.type)
head(phone.type)
phone.type1 <- phone.type[215:332, 2]
str(phone.type1)
tail(phone.type1)
phone.type2 <- c(phone.type1, "iPone", "荣耀", "红米", "魅蓝", 
                 "HUAWEI", "IPad","iPhone","乐","Android",
                 "WeicoPro","王者","iPad","HTML","OnePlus")   #三星手机部分问题，三星android
insertWords(phone.type2)

# 按行进行分词
phone.type3 <- segmentCN(phone_type1$source)
str(phone.type3)
phone.type4 <- c()
for (i in 1:length(phone.type3)) {
  for (j in 1:length(phone.type2)) {
    if(phone.type3[i]==phone.type2[j])
    phone.type4[i] <- phone.type3[i]
  }
}
for (i in 1:length(phone.type4)) {
  if(phone.type3[i]=="魅蓝")
    phone.type4[i] <- "魅族"
}
for (i in 1:length(phone.type4)) {
  if(phone.type3[i]=="HUAWEI")
    phone.type4[i] <- "华为"
}
for (i in 1:length(phone.type4)) {
  if(phone.type3[i]=="荣耀")
    phone.type4[i] <- "华为"
}
nrow(phone.type)
nrow(weibo1)
qita <-  nrow(weibo1)-sum(table(phone.type4))

phone.type5 <- sort(table(phone.type4),decreasing = T)
phone.type5 <- c(phone.type5,"其他"=qita)
wordcloud2(phone.type5)
plot(phone.type5)
plot(phone.type5,type = "h")


## -------------------------------------

text <- c('求职','银行招聘2015年招聘','薪资计算器','佛山英语翻译',
          '招聘网站酒店','烟台人才招聘')
keywords <- c('招聘','银行','网站')
mat <- data.frame(matrix(0,ncol=length(keywords),nrow=nrow(text)),
                  row.names=text$uid)
colnames(mat) <- keywords
getkey <- function(word){return(as.integer(regexpr(word,text)>0))}
mat <- sapply(keywords,getkey)
rownames(mat) <- text
mat
as.integer(regexpr(keywords[2],text)>0)

## ------------------------

mat1 <- data.frame(matrix(0,ncol=length(keywords1),nrow=length(phone_type1$uid)))
colnames(mat1) <- keywords1
# rownames(mat1) <- phone_type1$uid
getkey <- function(word){return(as.integer(regexpr(word,phone_type1$source)>0))}
mat1 <- sapply(phone.type2,getkey)
rownames(mat1) <- phone_type1
mat1

# 将矩阵转化为单一变量
cres=max.col(mat1)
phone_type1[,3]<- keywords1[cres]
fix(phone_type1)
write.csv(phone_type1,"phone_type1.csv")

##  ------------------------------
#x是手机型号分词后每个list， txt是手机型号文本库
Keep.vocabulary <- function(x, txt){
  for(i in 1:length(x)){
    if(!(x[i] %in% txt))  x[i] <- NA
  }
  x
}

phone.name4 <- lapply(phone.example, Keep.vocabulary, phone.type2)
#变量名按照你自己的替换




