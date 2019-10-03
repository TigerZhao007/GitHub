
library(xlsx)
library(Rwordseg)
library(rJava)
# weibo <- read.xlsx("C:/Users/lujian/Desktop/new_weiboxl2.xlsx",
#                     sheetIndex = "Sheet", header =TRUE,
#                     stringsAsFactors = FALSE,encoding = "UTF-8")
weibo <- read.csv("C:\\Users\\SDK\\Desktop\\weibo.csv",
                  header =TRUE, stringsAsFactors = FALSE)
str(weibo)
fix(weibo)

## --------------------------------------------------------------
# sex
weibo.sex <- weibo$sex
weibo.sex <- table(weibo.sex)

lals <- paste(names(weibo.sex), "", round(weibo.sex/sum(weibo.sex)*100, 2), "%", sep="")
pie(weibo.sex, col = c(4, "#ff1493"),labels = lals)


## --------------------------------------------------------------
# address
weibo.address <- substr(weibo$location, 1, 2)
weibo.address.sort <- sort(table(weibo.address), decreasing = TRUE)
bar.weibo <- barplot(weibo.address.sort[1:10],xlab = "地区",ylab = "人数")
tmp <- as.vector(weibo.address.sort[1:10])
text(bar.weibo, tmp, labels=tmp, pos=3) # 添加值标签
# pie(weibo.address.sort, col = 1:35)
sum(weibo.address.sort)

## --------------------------------------------------------------
# comment time
comment.time1 <- weibo$time
comment.time2 <- as.POSIXlt(comment.time1, format="%Y/%m/%d %H:%M")
comment.time  <- comment.time2[!is.na(comment.time2)]
# head(comment.time, 30)
# comment.time <- sort(comment.time)
# str(comment.time)
hist(comment.time, breaks = 24)

## --------------------------------------------------------------
# registered date
regi.date <- as.Date(weibo$date, format="%Y/%m/%d")
regi.date.y <- substr(regi.date,1,4) 
str(regi.date.y)
regi.date1 <- table(regi.date.y)
plot.regi <- plot(regi.date1,  type = "b", col="4", xlab = "年份", ylab = "注册量",
     main = "微博账号年注册量")
tmp <- as.vector(regi.date1)
text(plot.regi, tmp, labels=tmp, pos=3) # 添加值标签

## --------------------------------------------------------------
# unique ID
unique.ID <- duplicated(weibo$uid)  
# head(unique.ID, 30) 
weibo.ID <- weibo$uid[!unique.ID]
# str(weibo.ID)


## --------------------------------------------------------------
# phone type
# all phone type
all.phone <- read.csv(file="C:/Users/SDK/Desktop/phone.csv",
                      stringsAsFactors = FALSE)
# str(all.phone)
all.phone1 <- all.phone[215:332, 2]
# str(all.phone1)
allphone <- c(all.phone1, "荣耀", "红米", "魅蓝", "HUAWEI", 
              "IPad", "iPhone", "Android","乐","Android",
              "WeicoPro","iPad","OnePlus") 

# phone type
insertWords(allphone)   #词库添加
phone.type1 <- segmentCN(weibo$source)    #分词
# JAVA环境出现问题可用以下方法分词
# phone.exa <- enc2utf8(weibo$source) #转utf-8，有些格式它不支持
# phone.exa <- phone.exa[Encoding(phone.exa) != "unknown"]
# phone.type1 <- segmentCN(phone.exa)
# 筛选所需词汇
keep.word <- function(x, y, txt){
  y <- x[x %in% txt]
  y
}
phone.type2 <- c()
phone.type2 <- lapply(phone.type1, keep.word, phone.type2, allphone)
phone.type <- unlist(phone.type2)
str(phone.type)
# 手机厂商分析
phone.type3 <- phone.type
for (i in 1:length(phone.type)) {
  if(phone.type[i] == "魅蓝")    phone.type3[i] <- "魅族"
  if(phone.type[i] == "HUAWEI")  phone.type3[i] <- "华为"
  if(phone.type[i] == "荣耀")    phone.type3[i] <- "华为"
  if(phone.type[i] == "红米")    phone.type3[i] <- "小米"
  if(phone.type[i] == "乐")      phone.type3[i] <- "乐视"
}
# 过小转化为其他？
phone.type4 <- sort(table(phone.type3),decreasing = T)
phone.num1 <- sum(phone.type4 > 10)
phone.num2 <- sum(phone.type4 > 0)
phone.else <-sum(phone.type4[(phone.num1+1):phone.num2])
phone.na  <- length(phone.type2)-length(phone.type)
phone.type5 <- c(phone.type4[1:phone.num1], phone.else,phone.na)
phone.type5.name <- c(names(phone.type5),"其他","未知型号")

lals <- paste(phone.type5.name, "", round(phone.type5/sum(phone.type5), 2)*100, "%", sep="")
pie(phone.type5,labels = lals)

bar.phone <- barplot(phone.type5,col = "4",
        xlab = "手机类型", ylab = "人数", main = "手机类型使用情况")
tmp <- as.vector(phone.type5)
text(bar.phone, tmp, labels=tmp, pos=3) # 添加值标签

sum(!is.na(phone.type2))
