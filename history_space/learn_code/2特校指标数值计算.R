# 第三部分 指标数据计算
# 所需软件包
library(xlsx);
source('G:\\rspace\\自编程序\\list_sdk.R');
df_load <- "C:\\Users\\Administrator\\Desktop\\毕业论文\\特校数据\\2特校数据清洗00286.xlsx"
df <- read.xlsx(df_load,sheetIndex = 'Sheet1',encoding = 'UTF-8')

# 一、办学条件A

## 1、义务教育阶段生均经费达标率C1     (ok)
c1 <- (df$c6*df$g2+df$c7*df$g3)/(df$c6+df$c7)
## 2、无障碍设施达标率C2               (ok)
c2 <- df$e14
## 3、教学及辅助用房达标率C3           (ok)
c3 <- df$e4/df$b5
## 4、公共教学及康复用房达标率C4       (ok)
c4 <- df$e10/df$b5
## 5、办学用房达标率C5                 (ok)
c5 <- df$e12/df$b5
## 6、生活用房达标率C6                 (ok)
c6 <- df$e13/df$b5

# 二、师资队伍
## 7、师生比C7                         (ok)
c7 <- df$d1/(df$c1+df$c2) 
## 8、本科及以上学历教师占比C8         (ok)
c8 <- (df$d10+df$d11)/df$d1
## 9、中级及以上职称教师占比C9         (ok)
c9 <- (df$d14+df$d15+df$d16)/df$d1
## 10、优秀教师占比C10                 (ok)
c10 <- (df$d18+df$d19+df$d20)/df$d1
## 11、巡回指导教师占比C11             (ok)
c11 <- (df$b8)/df$d1
## 12、教师培训率C12                   (ok)
c12 <- df$d9/df$d1
## 13、师均科研课题成单率C13           (ok)
c13 <- (df$h1*20+df$h2*15+df$h3*10+df$h4*5)/(df$d1)

# 三、课程教学A3
## 14、一般性课程占比C14               (ok)
c14 <- df$f2/df$f1
## 15、选择性课程占比C15               (ok)
c15<- df$f3/df$f1
## 16、校本课程开设率C16               (ok)
c16 <- df$f5
## 17、教材开发率C17                   (ok)
c17 <- df$f6
## 18、个别化教学使用率C18             (ok)
c18 <- df$f7

#四、学生发展A4
## 19、生活能力提升度C19
c19 <- df$g6
# 20、残障缺陷补偿度C20                (ok)
c20 <- df$g7
## 21、特长培养重视度C21               (ok)
c21 <- df$g8
## 22、转衔服务提供度C22               (ok)
c22 <- df$g9

#五、学校发展A5
## 23、学校美誉度C23
c23 <- (df$i1*20+df$i2*15+df$i3*10+df$i4*5)/(df$d1+df$c1+df$c2)     #(ok)
## 24、师均教师荣誉度C24
c24 <- (df$i5*20+df$i6*15+df$i7*10+df$i8*5)/(df$d1)                 #(ok)
## 25、生均学生荣誉度C25
c25 <- (df$i9*20+df$i10*15+df$i11*10+df$i12*5)/(df$c1+df$c2)        #(ok)

#----------------------------------------------------
# 第四部分 指标数据的处理
# 将所有指标汇总到单个数据框汇总
df_zb <- data.frame(schoolid=df$schoolid,schoolname=df$b1,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,c6=c6,
                    c7=c7,c8=c8,c9=c9,c10=c10,c11=c11,c12=c12,c13=c13,c14=c14,
                    c15=c15,c16=c16,c17=c17,c18=c18,
                    c19=c19,c20=c20,c21=c21,c22=c22,
                    c23=c23,c24=c24,c25=c25
)

# 将字符变量变为数值变量
bq_c1 <- c('完全符合','符合','一般','不符合','完全不符合')
bq_c2 <- c('a','b','c','d','e')
bq_c3 <- c(1.00,0.80,0.60,0.40,0.20)

for (i in c(4,18:24)) {df_zb[,i] <- as.vector(df_zb[,i])}
names(df_zb)
for (i in 1:5) {
  location1 <- which(df_zb[,4]==bq_c1[i])
  df_zb[,4][location1] <- bq_c3[i]
  for (j in 18:24) {
    location2 <- which(df_zb[,j]==bq_c2[i])
    df_zb[,j][location2] <- bq_c3[i] 
  }
}
for (i in c(4,18:24)) {df_zb[,i] <- as.numeric(df_zb[,i])}

# 将数值规约为两位小数
for (i in 3:27) {df_zb[,i]<- round(df_zb[,i],2)}

df_mean <- c()
for (i in 1:25) {df_mean[i] <- mean(df_zb[,i+2])}
df_sd <- c()
for (i in 1:25) {df_sd[i] <- sd(df_zb[,i+2])}
df_low <- c()
for (i in 1:25) {df_low[i] <- quantile(df_zb[,i+2],probs=0.25)}
df_up <- c()
for (i in 1:25) {df_up[i] <- quantile(df_zb[,i+2],probs=0.75)}

df_dcirble <- data.frame(df_mean=df_mean,df_low=df_low,df_up=df_up,df_sd=df_sd)

#write.xlsx(df_dcirble,'C:\\Users\\Administrator\\Desktop\\df_dcirble.xlsx')


