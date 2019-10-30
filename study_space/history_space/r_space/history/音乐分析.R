head(weibo.singer,100)

## --------------------------------------------------------------

# reply tex
nrow(weibo)
weibo.index <- substr(weibo$text, 1, 2)   # 选取首词两个词。
weibo.text1  <- weibo$text[which(weibo.index != "回复")]   # 删除首词为回复的行
str(weibo.text1)
head(weibo.text1, 20)
weibo.text2 <- gsub("<.*>", "", weibo.text1)   # 删除<>中不需要词句
str(weibo.text2)
## --------------------------------------------------------------

# singer list
singer1 <- read.csv("C:/Users/SDK/Desktop/创新项目/artist.csv", 
                    header=FALSE, stringsAsFactors = FALSE)
str(singer1)
singer <- singer1[201:nrow(singer1), 2]
str(singer)
# weibo commment singer
insertWords(singer)   #词库添加
weibo.singer1 <- segmentCN(weibo.text2) 
str(weibo.singer1)
# keep.word <- function(x, y, txt){
#   y <- x[x %in% txt]
#   y
# }
weibo.singer2 <- c()
weibo.singer2 <- lapply(weibo.singer1, keep.word, 
                        weibo.singer2, singer)
weibo.singer <- unlist(weibo.singer2)
str(weibo.singer)
weibo.singer3 <- sort(table(weibo.singer), decreasing = TRUE)[1:15]
weibo.singer4 <- as.data.frame(weibo.singer3)
write.table(weibo.singer4$Freq,"C:/Users/SDK/Desktop/c.csv")

bar.weibo.singer <- barplot(weibo.singer3[1:15],xlab = "歌手",
                     ylab = "评论人数",ylim=c(0,250))
tmp <- as.vector(weibo.singer3[1:15])
text(bar.weibo.singer, tmp, labels=tmp, pos=3) # 添加值标签

## ------------------------------------------------------
## ------------------------------------------------------
# music list
#wangyiyun music
music.wangyiyun1 <- read.csv("C:/Users/SDK/Desktop/playlists.csv", 
                             header=TRUE, stringsAsFactors = FALSE)
# str(music.wangyiyun1)
music.wangyiyun2 <- music.wangyiyun1[ ,c(1, 3, 4)]
# str(music.wangyiyun2)
music.name1 <- music.wangyiyun2$MusicName
# str(music.name1)
# head(music.name1, 20)
# music.name1[c(116,122)]
music.name2 <- gsub("-.*", "", music.name1)
# music.name2[116]
music.name2 <- gsub("《.*》", "", music.name2)
music.name2 <- gsub("【.*】", "", music.name2)
music.name2 <- gsub("（.*）", "", music.name2)
music.name2 <- gsub("\\(.*\\)", "", music.name2)
# music.name2[122]
music.name3 <- trimws(music.name2)  #去除左右空格
# music.name3[116]
# music.name3[300:350]

## -------------------------------
# part music matching
music.part1 <- read.csv("C:/Users/lujian/Desktop/music.summary.csv", 
                        header=FALSE, stringsAsFactors = FALSE)
# str(music.part1)
music.part2 <- as.vector(as.matrix(music.part1))
# str(music.part2)
music.part <- gsub("（.*）", "", music.part2)
# music.part3[1:20]

insertWords(music.part)
weibo.text2[1:10]
weibo.music.part1 <- segmentCN(weibo.text2) 
# keep.word <- function(x, y, txt){
#   y <- x[x %in% txt]
#   y
# }
weibo.music.part2 <- c()
weibo.music.part2 <- lapply(weibo.music.part1, keep.word, 
                            weibo.music.part2, music.part)
weibo.music.part <- unlist(weibo.music.part2)
head(weibo.music.part, 10)
sort(table(weibo.music.part), decreasing = TRUE)[1:30]

