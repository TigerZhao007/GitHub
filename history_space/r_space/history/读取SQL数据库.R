
##  读取SQL sever 数据库文件  ##

##  连接数据库  ##

library(RODBC)
#这里是载入RODBC库

ch <- odbcConnect("Rspace", uid = "sa", pwd = "sdk")
#数据库Rspace,用户名uid，密码pwd，如果没有设置，可以直接忽略。

#?channel01 <- odbcConnect("Rspace", uid = "sa",case = "sdk")
#连接刚才添加进数据源的“MyTest”数据库

##  将数据保存到数据库中。  ##
data(USArrests)
#将“USArrests”表写进数据库里（这个表是R自带的）

sqlSave(ch,USArrests,rownames = "state",addPK = TRUE)
#将数据流保存，这时候打开SQL Server就可以看到新建的USArrests表了

##  查看数据库中的表。  ##
rm(USArrests)
sqlTables(ch)
#给出数据库中的表

sqlFetch(ch,"理科",rownames = "state")
#输出数据库中相关表中的内容

sqlQuery(ch,"select * from 理科")
#调用SELECT查询语句并返回结果（如图）

sqlDrop(ch,"USArrests")
##删除表

odbcClose(ch)
##最后要记得关闭连接

## 整体过程  ##
Library(RODBC)
odbcDataSources()
conn=odbcConnect('Rspace',uid='sa',pwd='sdk')
odbcClose(conn)















