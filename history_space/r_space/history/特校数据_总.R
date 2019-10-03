library("xlsx")
tx.data <- read.xlsx("txsj_z.xlsx",sheetIndex = "Sheet1",encoding = "UTF-8")
head(tx.data)
fix(tx.data)
