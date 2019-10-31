# 发表文本分析

weibo1 <- read.csv("C:/Users/lujian/Desktop/weibo_comments.csv",
                   header =TRUE,stringsAsFactors = FALSE)
str(weibo1)
# head(weibo1[ ,5])
str(weibo1[ ,5])
# weibo2 <- strsplit(weibo1[ ,5], split="<")
# str(weibo2)
weibo3 <- substr(weibo1[ ,5], 1, 2)
str(weibo3)
head(weibo3, 20)
# z <- c()
# for(i in 1:length(weibo3)){
#   if(weibo3[i] != "回复") 
#     z <- c(z, i)
# } 
# str(z)
# weibo4 <- weibo1[z, 5]
# head(weibo3 == "回复")
weibo4 <- weibo1[which(weibo3 != "回复"), 5]
str(weibo4)
head(weibo4, 10)
# weibo5 <- gsub("\\<.*?\\>","",weibo4)
weibo5 <- gsub("<.*>", "", weibo4)
head(weibo5, 50)
str(weibo5)
