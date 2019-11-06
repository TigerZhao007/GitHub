# 加载软件包
#if(!require(plyr)){install.packages("plyr")}
#if(!require(dplyr)){install.packages("dplyr")}
if(!require(data.table)){install.packages("data.table")}
#if(!require(randomForest)){install.packages("randomForest")}
if(!require(stringr)){install.packages("stringr")}
options(scipen = 200)
# 读取数据&设置工作路径
setwd("C:/Users/Think/Desktop")
testdata <- fread("testdata_xlsx.csv", header=TRUE, stringsAsFactors = FALSE)

# 1、数据清洗，data_whole_flag数据项为96个电压点的标识，0标识有效，1标识无效，NULL为缺失
# 2、根据data_whole_flag，对u1到u96（电压值）进行清洗，电压值正常范围为-10%+7%（198,235.4），保存为csv
# 3、电压值有缺失，有为0，需要进行分情况保存
# 4、对越上界和越下界的ID进行数据探索
dat = as.data.frame(apply(testdata[,-c(2,4)],2,
                          function(x){x[which(x=='NULL')] = NA;x = as.numeric(x);
                          x[which(x==0)] = NA;x[which(x==-9999)] = NA;return(x)}))
dat$data_whole_flag = str_pad(as.character(testdata$data_whole_flag),96,pad = '0')
temp = as.data.frame(apply(dat[,3:98],2,
                           function(x){x[which(x<198)] = -1
                           x[which(x > 235.4)] = 0 
                           x[which(x>=198 & x <= 235.4)] = 1
                           return(x)}))
dat$nanum = apply(temp[,1:96], 1,function(x){n = length(which(is.na(x)));return(n)})
dat$lownum = apply(temp[,1:96], 1,function(x){n = length(which(x==-1));return(n)})
dat$upnum = apply(temp[,1:96], 1,function(x){n = length(which(x==0));return(n)})
dat$oknum = apply(temp[,1:96], 1,function(x){n = length(which(x==1));return(n)})

dat_na = dat[which(dat$nanum != 0),]
dat_low = dat[which(dat$lownum != 0),]
dat_up = dat[which(dat$upnum != 0),]
dat_ok = dat[which(dat$oknum == 96),]

summary(dat_ok)
summary(dat_low)

