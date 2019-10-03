## 数据准备
library(xlsx);
source('G:\\rspace\\自编程序\\list_sdk.R');
df_load <- "C:\\Users\\Administrator\\Desktop\\毕业论文\\特校数据\\3特校建模数据00286.xlsx"
df <- read.xlsx(df_load,sheetIndex = 'Sheet1',encoding = 'UTF-8')

#----------------------------------------------------
# 第五部分 层次分析法权重下计算综合得分
com_load <- "C:\\Users\\Administrator\\Desktop\\毕业论文\\特校数据\\权重打分表.xlsx"
compare1 <- read.xlsx(com_load,sheetIndex = 'Sheet1',encoding = 'UTF-8')
compare2 <- read.xlsx(com_load,sheetIndex = 'Sheet2',encoding = 'UTF-8')
compare3 <- read.xlsx(com_load,sheetIndex = 'Sheet3',encoding = 'UTF-8')

weight_a0105 <- weight(compare1[,2:6])
weight_b0112 <- c(weight_a0105[1]*weight(compare2[1:2,2:3]),
                  weight_a0105[2]*weight(compare2[3:5,4:6]),
                  weight_a0105[3]*weight(compare2[6:8,7:9]),
                  weight_a0105[4]*weight(compare2[9:10,10:11]),
                  weight_a0105[5]*weight(compare2[11:12,12:13]))
weight_c0125 <- c(weight_b0112[1]*1,  weight_b0112[2]*weight(compare3[2:6,3:7]),
                  weight_b0112[3]*1,  weight_b0112[4]*weight(compare3[8:11,9:12]),
                  weight_b0112[5]*weight(compare3[12:13,13:14]),
                  weight_b0112[6]*weight(compare3[14:15,15:16]),
                  weight_b0112[7]*weight(compare3[16:17,17:18]),
                  weight_b0112[8]*1,  weight_b0112[9]*1,
                  weight_b0112[10]*weight(compare3[20:22,21:23]),  weight_b0112[11]*1,
                  weight_b0112[12]*weight(compare3[24:25,25:26]))

weight1 <- weight_c0125

score1 <- c()
for (i in 1:nrow(df_zb)) {score1[i] <- sum(weight1*df_zb[3:27][i,])}

score1_pm  <- data.frame(df$schoolid,df_zb,score=score1)
score1_pmd <- score1_pm[order(-score1_pm$score),]
#head(score1_pmd)

#----------------------------------------------------
# 第六部分 TOPSIS
weight1 <- weight_c0125
df_zb <- df
z_max <- c()
z_min <- c()
for (i in 1:25) {z_max[i] <- max(df_zb[,i+3])}
for (i in 1:25) {z_min[i] <- min(df_zb[,i+3])}

df_max <- df_zb[,4:28]
for (j in 1:25) {
  for (i in 1:nrow(df_max)) {  
    df_max[i,j] <- (df_max[i,j]-z_max[j])^2*weight1[j]
  }
}
head(df_max)
d_max <- c()
for (i in 1:nrow(df_max)) {
  d_max[i] <- sum(df_max[i,])^(1/2)
}

df_min <- df_zb[,4:28]
for (j in 1:25) {
  for (i in 1:nrow(df_min)) {  
    df_min[i,j] <- (df_min[i,j]-z_min[j])^2*weight1[j]
  }
}
head(df_min)
d_min <- c()
for (i in 1:nrow(df_min)) {
  d_min[i] <- sum(df_min[i,])^(1/2)
}

c_score <- d_min/(d_min+d_max)
c_score
temp <- data.frame(df$schoolid,df$schoolname,c_score,d_min,d_max)
temp1 <- temp[order(-temp$c_score),]
#write.xlsx(temp,'C:\\Users\\Administrator\\Desktop\\TOPSIS综合评价结果00286.xlsx')

#----------------------------------------------------
# 第六部分 BP神经网络权重修正
library(neuralnet)
df_model <- data.frame(df[,-1],score=temp$c_score)
head(df_model)
names(df_model)
model_neur <- neuralnet(score~c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c4+c15+
                          c16+c17+c18+c19+c20+c21+c22+c23+c24+c25,
                        data = df_model[,3:28],hidden = 7)
response <- model_neur$net.result[[1]]
score <- model_neur$response

#library(nnet)
#size = 5;   decay = 0.05;  maxit = 10000;
#model_nnet <- nnet(score~., data = df_model[,c(-1,-2)],size=size,decay=decay,maxit=maxit)
#pred_nnet <- predict(model_nnet, newdata = df_model[,3:28])
#model_nnet$wts
#a <-  plot(model_neur)
#model_neur$weights
#summary(model_neur)

dat_res <- data.frame(score=score,response=response)
dat_res[,3] <- dat_res$score-dat_res$response
head(dat_res,5)
sd(dat_res$V3)
model_neur$weights


sd_error <- c()
hid_num  <- c()
for (i in 1:500) {
  set.seed(1234)
  model_neur <- neuralnet(score~c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c4+c15+
                            c16+c17+c18+c19+c20+c21+c22+c23+c24+c25,
                          data = df_model[,3:28],hidden = i)
  response <- model_neur$net.result[[1]]
  score <- model_neur$response
  error <- response-score
  sd_error[i] <- sd(error)
  hid_num[i]  <- i
}
dat_error <- data.frame(sd_error,hid_num)
#write.xlsx(dat_error,'C:\\Users\\Administrator\\Desktop\\BP误差曲线00286.xlsx')
plot(dat_error$sd_error,type = 'l',xlab = '隐含节点数目',ylab = '模型拟合误差标准差')
abline(h=0.01)
abline(v=18)

set.seed(1234)
model_neur <- neuralnet(score~c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c4+c15+
                          c16+c17+c18+c19+c20+c21+c22+c23+c24+c25,
                        data = df_model[,3:28],hidden = 18)
response <- model_neur$net.result[[1]]
score <- model_neur$response
error <- response-score
sd_error18 <- sd(error)
result1 <- data.frame(response,score,error)
plot(result1$error)
result2 <- model_neur$weights
wet1 <- result2[[1]][[1]]
wet2 <- result2[[1]][[2]]
#write.xlsx(wet2,'C:\\Users\\Administrator\\Desktop\\2-3权重00286.xlsx')
plot(model_neur)






