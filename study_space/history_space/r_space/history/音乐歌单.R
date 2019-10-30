# 读取数据
music <- read.csv("C:/Users/SDK/Desktop/playlists.csv",
                   header =TRUE, stringsAsFactors = FALSE)

str(music)

# 

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

