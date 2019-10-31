library(RODBC)
ch <- odbcConnect("Rspace", uid = "sa", pwd = "sdk")
sqlFetch(ch,"理科",rownames = "state")
sqlQuery(ch,"select * from 理科")
data(USArrests)
sqlSave(ch,USArrests,rownames = "state",addPK = TRUE)
sqlTables(ch, tableType = "table")
sqlTables(ch)
sqlTables(ch,schema = "dbo")
sqlTables(ch,tableName = "理科")


x <- sqlFetch(ch, "理科", rownames = "state") 
x
head(x$姓名)
天气 <- read.xlsx("tianqi01.xlsx", sheetIndex = "Sheet1", encoding = "UTF-8")
天气
sqlSave(ch,天气, rownames = "state", addPK = TRUE)
sqlColumns(ch, "理科")
ncol(x)
nrow(x)
y <- na.omit(x)
y[3]
y[which(y$姓名=="白林"),]
sqlDrop(ch, "USArrests", errors = FALSE)
y[which(y$总分>600),]
y[which(y$考场==1),]
levels(y$考场)
`levels<-.factor`(y$考场)
factor(y$考场)$levels
a01 <- table(y$考场)
hist(a01)
list(a01)
hist(unname(a01))

odbcClose(ch)
