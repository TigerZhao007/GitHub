if(!require(RODBC)){install.packages('RODBC')}
if(!require(data.table)){install.packages("data.table")}

channel <- odbcConnect("mysql_test", uid = "root", pwd = "s3438838")
attr(channel,'case') <- 'nochange'
sqlQuery(channel,'select * from test1')
dat <- data.frame(id=c(3,6),x1=c(1001,2001),x2=c(2001,400))
dat <- data.frame(id=c(1),x1=c(21),x2=c(40))
sqlUpdate(channel,dat = dat[c('id','x1','x2')],tablename = 'test1',
          index = 'x1',verbose = F, test = F, fast = F)
sqlQuery(channel,'select * from test1')

