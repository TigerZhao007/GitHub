music <- read.csv("C:/Users/SDK/Desktop/artist1.csv",
                   header =TRUE, stringsAsFactors = FALSE)
str(music)
nrow(music)
head(music)

library(knitr)


weibo.text2     # 评论
weibo.singer1   # 评论分词
weibo.singer2   # 匹配后剩下的歌手名字


singer.other <- c("太阳","方圆")

weibo.singer2 <- lapply(weibo.singer1, keep.word, 
                        weibo.singer2, singer)   # 查找
length(weibo.text2)

singer.sun <- c()
for (i in i:length(weibo.singer2)) {
  
  if(weibo.singer2[[i]]%in%singer.other)singer.sun[i] <- i
  
}

weibo.text2[[9793]]
