# 加载软件包
if(!require(RODBC)){install.packages('RODBC')}
if(!require(data.table)){install.packages("data.table")}


#### 1.1 DATA DEALING     ####
# 读取特殊教育原始数据表，并进行整理，得到整理后的数据data_deal.
data_origianl <- fread('F:\\毕业论文\\0特教原始数据34603.csv', encoding = "UTF-8")
#data_origianl <- fread('F:\\毕业论文\\txsj.csv', encoding = "UTF-8")
data_origianl$bhym  <- paste(data_origianl$ym,'_',data_origianl$bh,sep ='') 

names_col <- unique(data_origianl$bhym) 
names_row <- unique(data_origianl$bfz)

data_deal <- data.frame(xh=names_row)
for(i in 1:length(names_col)) { data_deal[,i+1] <- NA}
names(data_deal) <-c('xh',names_col)

for (j in 2:length(names_col)) {
  for (i in 1:length(names_row)) {
    location <- location <- which(data_origianl$bfz==names_row[i]&data_origianl$bhym==names_col[j])
    if(length(location==1))
      data_deal[i,j] <- data_origianl[location,4]
    else
      next
  }
}
write.csv(data_deal,'C:/Users/Think/Desktop/data_deal.csv')

#### 1.1 DATA DEALING     ####
# 读取特殊教育原始数据表，并进行整理，得到整理后的数据data_deal.
# 链接数据库
channel <- odbcConnect("mysql_texiao", uid = "root", pwd = "s3438838")
attr(channel,'case') <- 'nochange'

sqlSave(channel, data_origianl, tablename = "texiaodata2016_org", rownames = F, append = T)
sqlSave(channel, data_deal, tablename = "texiaodata2016_deal", rownames = F, append = T)
write.csv(data_deal,'C:\\Users\\Think\\Desktop\\texiaodata2016_deal.csv')
names(data_deal)
####~####
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~####
# PART 5 END ENV ####
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##---------------------------------------------------------####                        
#### 5.1 close channel ####
odbcClose(channel)
