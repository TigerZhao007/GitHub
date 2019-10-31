# 所需软件包

library(xlsx);
source('G:\\rspace\\自编程序\\list_sdk.R');

#----------------------------------------------------
# 读取原始数据

dat_load <- "C:\\Users\\Administrator\\Desktop\\毕业论文\\特校数据\\特教原始数据34603.csv"
dat <- read.csv(dat_load)
dat <- dat[,c(2,3,4,5)]
head(dat)

#----------------------------------------------------
# 第一部分 数据整理
# 根据文件名分别命名每部分文件名，以备后续刷选。
name_z <- list(part1 = c(paste('a',1:10,sep = '')), part2 = c(paste('b',1:11,sep = '')),
               part3 = c(paste('c',1:4,sep = '')),
               part4 = c(paste('b',1:8,sep = ''),"s_province","s_city","s_country"),
               part5 = c(paste('c',1:13,sep = '')), part6 = c(paste('d',1:20,sep = '')),
               part7 = c(paste('e',1:14,sep = '')), part8 = c(paste('f',1:7,sep = '')),
               part9 = c(paste('g',1:9,sep = '')), part10 = c(paste('h',1:4,sep = '')),
               part11 = c(paste('i',1:12,sep = '')),
               part12 = c('j1',paste('j2_',c('a','b','c','d','e','f','g','h','i','j'),sep = ''),
                          'j3','j4',paste('j5_',c('a','b','c','d','e','f','g','h','i','j'),sep = ''))
)
colname_z <- list(
  part1 = c("bh", "name","sex","age","degree","phone.num","qq","youxiang","zhicheng","nianzi","nianxian"),
  part2 = c("bh", "b01", "b02", "b03", "b04", "b05", "b06", "b07","b08","b09","b010","b011"),
  part3 = c("bh", "c01", "c02", "c03", "c04"),
  part4 = c("bh", paste('b',1:8,sep = ''),"s_province","s_city","s_country"),
  part5 = c("bh", paste('c',1:13,sep = '')), part6 = c("bh", paste('d',1:20,sep = '')),
  part7 = c("bh", paste('e',1:14,sep = '')), part8 = c("bh", paste('f',1:7,sep = '')),
  part9 = c("bh", paste('g',1:9,sep = '')),  part10 = c("bh", paste('h',1:4,sep = '')),
  part11 = c("bh", paste('i',1:12,sep = '')),
  part12 = c("bh", 'j1',paste('j2_',c('a','b','c','d','e','f','g','h','i','j'),sep = ''),
             'j3','j4',paste('j5_',c('a','b','c','d','e','f','g','h','i','j'),sep = ''))
)
colnum_z <- list(
  part1 = c(1,3,6,9,12,15,18,21,24,27,30),  part2 = c(1,3,6,9,12,15,18,21,24,27,30,33),
  part3 = c(1,3,6,9,12),  part4 = c(1,3,6,9,12,15,18,21,24,27,30,33),
  part5 = c(1,3,6,9,12,15,18,21,24,27,30,33,36,39),  
  part6 = c(1,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,60),
  part7 = c(1,3,6,9,12,15,18,21,24,27,30,33,36,39,42),  part8 = c(1,3,6,9,12,15,18,21),
  part9 = c(1,3,6,9,12,15,18,21,24,27),  part10 = c(1,3,6,9,12),
  part11 = c(1,3,6,9,12,15,18,21,24,27,30,33,36),  
  part12 = c(1,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,60,63,66,69)
)

# 将所有数据整理成单个数据框
df <- list_end(dat,name_z,colnum_z,colname_z)
#write.xlsx(df,'C:\\Users\\Administrator\\Desktop\\1特校数据清洗00286.xlsx')

# 查看整理后的数据
# head(df,1)

#----------------------------------------------------
# 第二部分 数据清洗&数据预处理
# 将数据写入Excel中对数据进行数据清洗

## 第一步 文本数据规整
# 将变量中填写不规范的数据进行规整，数字中不得有文字，职称学历按标准划分。
# 查看清洗后的数据
df_load <- "C:\\Users\\Administrator\\Desktop\\毕业论文\\特校数据\\2特校数据清洗00286.xlsx"
df <- read.xlsx(df_load,sheetIndex = 'Sheet1',encoding = 'UTF-8')
#fix(df)

## 第二步 数据取值规约
# 1、教师人数检查
check1_1 <- which(df$d1<df$d2|df$d2!=df$d3+df$d4)
check1_2 <- which(df$d2<df$d9)
check1_3 <- which(df$d2<df$d10+df$d11+df$d12+df$d13)
check1_4 <- which(df$d2<df$d14+df$d15+df$d16+df$d17)
#2、课程课时检查
check2_1 <- which(df$f1<df$f2+df$f3+df$f4)
#-----------------------------------------------------
# head(df)
## 第三步 信度效度分析
#df_xx_load <- "C:\\Users\\Administrator\\Desktop\\毕业论文\\特校数据\\3信度效度数据00286.xlsx"
#df_xx <- read.xlsx(df_xx_load,sheetIndex = 'Sheet1',encoding = 'UTF-8')
#df_xx <- df_xx[,2:52]
#for (i in 1:ncol(df_xx)){
#  df_xx[,i] = (df_xx[,i]-min(df_xx[,i]))/(max(df_xx[,i])-min(df_xx[,i]))
#}
#for (i in 1:nrow(df_xx)) {
#  df_xx[i,52] <- sum(df_xx[i,1:51])
#}
#y <- c()
#for (i in 1:ncol(df_xx)) {
#  y[i] <- var(df_xx[,i])
#}
#value_xindu <- (54/53)*(1-sum(y[1:51])/y[52])
#value_xindu