## 数据准备
library(xlsx);
source('G:\\rspace\\自编程序\\list_sdk.R');
df_load <- "C:\\Users\\Administrator\\Desktop\\毕业论文\\特校数据\\3特校建模数据00286.xlsx"
df <- read.xlsx(df_load,sheetIndex = 'Sheet1',encoding = 'UTF-8')

#----------------------------------------------------
weight_bp3 <- c(0.062, 0.041, 0.046, 0.024, 0.017, 0.001, 0.05, 0.074, 0.049, 0.008, 0.008, 
               0.071, 0.036, 0.047, 0.018, 0.051, 0.061, 0.033, 0.01, 0.038, 0.04, 0.058, 
               0.029, 0.084, 0.045) 
weight_bp2 <- c(0.062, 0.129, 0.050, 0.139, 0.107, 0.065, 0.112, 0.033, 
                0.010, 0.136, 0.029, 0.128)
weight_bp1 <- c(0.191, 0.296, 0.210, 0.146, 0.157)

score_bp <- data.frame()
for (i in 1:nrow(df)) {
  score_bp[i,1] <- sum(weight_bp3*df[i,4:28])

  score_bp[i,2] <- sum(weight_bp3[1:6]*df[i,4:9])/sum(weight_bp3[1:6])
  score_bp[i,3] <- sum(weight_bp3[7:13]*df[i,10:16])/sum(weight_bp3[7:13])
  score_bp[i,4] <- sum(weight_bp3[14:18]*df[i,17:21])/sum(weight_bp3[14:18])
  score_bp[i,5] <- sum(weight_bp3[19:22]*df[i,22:25])/sum(weight_bp3[19:22])
  score_bp[i,6] <- sum(weight_bp3[23:25]*df[i,26:28])/sum(weight_bp3[23:25])

  score_bp[i,7] <- sum(weight_bp3[1:1]*df[i,4:4])/sum(weight_bp3[1:1])
  score_bp[i,8] <- sum(weight_bp3[2:6]*df[i,5:9])/sum(weight_bp3[2:6])
  score_bp[i,9] <- sum(weight_bp3[7:7]*df[i,10:10])/sum(weight_bp3[7:7])
  score_bp[i,10] <- sum(weight_bp3[8:11]*df[i,11:14])/sum(weight_bp3[8:11])
  score_bp[i,11] <- sum(weight_bp3[12:13]*df[i,15:16])/sum(weight_bp3[12:13])
  score_bp[i,12] <- sum(weight_bp3[14:15]*df[i,17:18])/sum(weight_bp3[14:15])
  score_bp[i,13] <- sum(weight_bp3[16:17]*df[i,19:20])/sum(weight_bp3[16:17])
  score_bp[i,14] <- sum(weight_bp3[18:18]*df[i,21:21])/sum(weight_bp3[18:18])
  score_bp[i,15] <- sum(weight_bp3[19:19]*df[i,22:22])/sum(weight_bp3[19:19])
  score_bp[i,16] <- sum(weight_bp3[20:22]*df[i,23:25])/sum(weight_bp3[20:22])
  score_bp[i,17] <- sum(weight_bp3[23:23]*df[i,26:26])/sum(weight_bp3[23:23])
  score_bp[i,18] <- sum(weight_bp3[24:25]*df[i,27:28])/sum(weight_bp3[24:25])
}
#value_pf <- data.frame(response,score,error,score_bp$V1)
head(score_bp)
colnames(score_bp) <- c('z_pg',paste('A',1:5,sep = ''),
                        paste('B',1:12,sep = ''))

result_bp <- data.frame(df[1:3],score_bp,df[4:28])
write.xlsx(result_bp,'C:\\Users\\Administrator\\Desktop\\BP评价结果00286.xlsx')






