#第三部分 指标数据计算
# 一、办学条件A
## 数据准备
library(xlsx);
source('G:\\rspace\\自编程序\\list_sdk.R');

df_load <- "C:\\Users\\Administrator\\Desktop\\毕业论文\\特校数据\\2特校数据清洗00286.xlsx"
df <- read.xlsx(df_load,sheetIndex = 'Sheet1',encoding = 'UTF-8')

## 各类用房数据
dat <- data.frame(df$xh,df$schooltype,df$classmun,df$b5,df$e4,df$e10,df$e12,df$e13)
## 查看各类特校用房标准
bz_load <- "C:\\Users\\Administrator\\Desktop\\毕业论文\\特校数据\\指标标准.xlsx"
bz <- read.xlsx(bz_load,sheetIndex = 'Sheet2',encoding = 'UTF-8')
schooltype <- c('聋校','盲校','培智学校','综合类学校')
classnum   <- c(9,18,27)
teach_student <- c(1/3.5,1/3.5,1/3,1/2)
## head(bz)

## 1、义务教育阶段生均经费达标率C1     (ok)
c1 <- (df$c6*df$g2+df$c7*df$g3)/(df$c6+df$c7)/8000
c1 <- c1/1
# （第260、219学生数均为0；）
## 2、无障碍设施达标率C2               (ok)
c2 <- df$e14
## 3、教学及辅助用房达标率C3           (ok)
c3 <- schoolarea(dat,zb,5,3)
c3 <- c3/1

## 4、公共教学及康复用房达标率C4       (ok)
c4 <- schoolarea(dat,zb,6,4)
c4 <- c4/1
## 5、办学用房达标率C5                 (ok)
c5 <- schoolarea(dat,zb,7,5)
c5 <- c5/1
## 6、生活用房达标率C6                 (ok)
c6 <- schoolarea(dat,zb,8,6)
c6 <- c6/1

# 二、师资队伍
## 7、师生比C7                         (ok)
c7 <- df$d1/(df$c1+df$c2) 
for (i in 1:4) {
  location_c7 <- which(df$schooltype==schooltype[i])
  c7[location_c7] <- c7[location_c7]/teach_student[i]
} 
## 8、本科及以上学历教师占比C8         (ok)
c8 <- (df$d10+df$d11)/df$d1
c8 <- c8/0.8
## 9、中级及以上职称教师占比C9         (ok)
c9 <- (df$d14+df$d15+df$d16)/df$d1
c9 <- c9/0.8
## 10、优秀教师占比C10                 (ok)
c10 <- (df$d18+df$d19+df$d20)/df$d1
c10 <- c10/0.4
## 11、巡回指导教师占比C11             (ok)
c11 <- (df$b8)/df$d1
c11 <- c11/0.2
## 12、教师培训率C12                   (ok)
c12 <- df$d9/df$d1
c12 <- c12/0.6
## 13、师均科研课题成单率C13           (ok)
c13 <- (df$h1*20+df$h2*15+df$h3*10+df$h4*5)/(df$d1)
c13 <- c13/2

# 三、课程教学A3
## 14、一般性课程占比C14               (ok)
c14 <- df$f2/df$f1
c14[which(c14<0.5)] <- 0
c14[which(0.5<=c14&c14<=0.7)] <- (c14[which(0.5<=c14&c14<=0.7)]-0.5)/0.2
c14[which(0.7<=c14&c14<=0.8)] <- 1
c14[which(c14>0.8)] <- (c14[which(c14>0.8)]-0.8)/0.2

# （第9、286样本课程均为0；）   
## 15、选择性课程占比C15               (ok)
c15<- df$f3/df$f1
c15[which(c15>=0.5)] <- 0
c15[which(0.3<=c15&c15<=0.5)] <- (c15[which(0.3<=c15&c15<=0.5)]-0.3)/0.2
c15[which(0.2<=c15&c15<=0.3)] <- 1
c15[which(c15<0.2)] <- c15[which(c15<0.2)]/0.2

# （第286样本课程均为0；）
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
c23 <- c23/1
## 24、师均教师荣誉度C24
c24 <- (df$i5*20+df$i6*15+df$i7*10+df$i8*5)/(df$d1)                 #(ok)
c24 <- c24/10
## 25、生均学生荣誉度C25
c25 <- (df$i9*20+df$i10*15+df$i11*10+df$i12*5)/(df$c1+df$c2)        #(ok)
c25 <- c25/2


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

# 将超过1的指标规约为1
for (i in 3:27) {df_zb[which(df_zb[,i]>=1),i] <-1}


# 查看指标数据
head(df_zb)
#fix(df_zb)
#write.xlsx(df_zb,'C:\\Users\\Administrator\\Desktop\\毕业论文\\特校数据\\3特校建模数据00286.xlsx')
df_mean <- c()
for (i in 1:25) {df_mean[i] <- mean(df_zb[,i+2])}
df_sd <- c()
for (i in 1:25) {df_sd[i] <- sd(df_zb[,i+2])}
df_low <- c()
for (i in 1:25) {df_low[i] <- quantile(df_zb[,i+2],probs=0.25)}
df_up <- c()
for (i in 1:25) {df_up[i] <- quantile(df_zb[,i+2],probs=0.75)}

df_dcirble <- data.frame(df_mean=df_mean,df_low=df_low,df_up=df_up,df_sd=df_sd)
head(df_dcirble)

