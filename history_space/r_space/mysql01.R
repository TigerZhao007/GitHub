# 加载软件包
if(!require(RODBC)){install.packages('RODBC')}
if(!require(data.table)){install.packages("data.table")}

# 读取数据&设置工作路径
setwd("F:/工作文件/2宜开工作/2_版权商业价值评估/testdata")
value_work <- fread("value_work.csv", header=TRUE, stringsAsFactors = FALSE)
register_archive_data_info_new <- fread("register_archive_data_info_new.csv", header=TRUE, stringsAsFactors = FALSE,encoding = 'UTF-8')
works_transfer <- fread("copyright_transfer_record_info.csv", header=TRUE, stringsAsFactors = FALSE,encoding = 'UTF-8')
user_register_info <- fread("user_register_info.csv", header=TRUE, stringsAsFactors = FALSE)   

# 链接数据库
channel <- odbcConnect("mysql_yikai", uid = "root", pwd = "s3438838")

sqlSave(channel, value_work, tablename = "value_work", rownames = F,append = T)
sqlSave(channel, works_transfer, tablename = "works_transfer", rownames = F,append = T)
sqlSave(channel, user_register_info, tablename = "user_register_info1", rownames = F,append = T)
sqlSave(channel, register_archive_data_info_new, tablename = "register_archive_data_info_new1", rownames = F, append = T)

str(value_work)
####~####
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~####
odbcClose(channel)



