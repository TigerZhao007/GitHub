library("xlsx")
library("Rwordseg")
library(rJava)
library(Rwordseg)
library(wordcloud2)
library(tmcn)
library(jiebaR)

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
str(phone.type)
head(phone.type)
phone.type1 <- phone.type[215:332, 2]
str(phone.type1)
tail(phone.type1)
phone.type2 <- c(phone.type1, "iPone", "荣耀", "红米", "魅蓝", 
                 "HUAWEI", "IPad","iPhone","乐","Android",
                 "WeicoPro","王者","iPad","HTML","OnePlus")   #三星手机部分问题，三星android
insertWords(phone.type2)

## ------------------------

# 手机类型：phone.type2
# 手机类型原始数据表：phone_type1


# 按行分词统计
mat1 <- data.frame(matrix(0,ncol=length(phone.type2),nrow=length(phone_type1$uid)))
colnames(mat1) <- phone.type2
getkey <- function(word){return(as.integer(regexpr(word,phone_type1$source)>0))}
mat1 <- sapply(phone.type2,getkey)

# 将矩阵转化为单一变量
cres=max.col(mat1)
phone_type1[,3]<- phone.type2[cres]
fix(phone_type1)
write.csv(phone_type1,"phone_type1.csv")
