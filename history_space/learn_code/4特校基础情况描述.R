#----------------------------------------------------
# 查看清洗后的数据
df_load <- "C:\\Users\\Administrator\\Desktop\\毕业论文\\特校数据\\2特校数据清洗00286.xlsx"
df <- read.xlsx(df_load,sheetIndex = 'Sheet1',encoding = 'UTF-8')

# 第三部分 描述性分析

df_dci <- df
# 地区分布情况
table(df_dci$areaid)
for (i in 1:3) {
  df_dci1 <- df_dci[which(df_dci$areaid==i),]
  table1 <- table(df_dci1$s_province)
  table1 <- table1[which(table1>0)]
  print("第几部分")
  print(table1)
}
# 学校类型分布情况
table(df_dci$schooltype)
for (i in 1:3) {
  df_dci1 <- df_dci[which(df_dci$areaid==i),]
  table1 <- table(df_dci1$schooltype)
  #  table1 <- table1[which(table1>0)]
  print("第几部分")
  print(table1)
}
# 学生类型分布情况
stud <- c(sum(df_dci$c10),sum(df_dci$c11),sum(df_dci$c12),sum(df_dci$c13))
for (i in 1:3) {
  df_dci1 <- df_dci[which(df_dci$areaid==i),]
  table1 <- c(sum(df_dci1$c10),sum(df_dci1$c11),sum(df_dci1$c12),sum(df_dci1$c13))
  #  table1 <- table1[which(table1>0)]
  print("第几部分")
  print(table1)
}


## 1、义务教育阶段生均经费达标率C1     (ok)
c01 <- (df$c6*df$g2+df$c7*df$g3)/(df$c6+df$c7)
mean(c01)
c001 <- data.frame(c01=c01,area=df$areaid)
c001$area <- as.factor(c001$area)
aggregate(c01,by=list(c001$area),FUN=mean)
fit=aov(c01~area,data = c001)
summary(fit)
# 两两比较
TukeyHSD(fit)

## 2、师生比C7                         (ok)
c01 <- df$d1/(df$c1+df$c2) 
c001 <- data.frame(c01=c01,area=df$areaid)
c001$area <- as.factor(c001$area)
aggregate(c01,by=list(c001$area),FUN=mean)
fit=aov(c01~area,data = c001)
summary(fit)
# 两两比较
TukeyHSD(fit)

## 3、中级及以上职称教师占比C9         (ok)
c01 <- (df$d14+df$d15+df$d16)/df$d1
c001 <- data.frame(c01=c01,area=df$areaid)
c001$area <- as.factor(c001$area)
aggregate(c01,by=list(c001$area),FUN=mean)
fit=aov(c01~area,data = c001)
summary(fit)
# 两两比较
TukeyHSD(fit)

## 4、校本课程开设率C16               (ok)
c16 <- df$f5
table(c16)
for (i in 1:3) {
  df_dci1 <- df_dci[which(df_dci$areaid==i),]
  table1 <- table(df_dci1$schooltype)
  #  table1 <- table1[which(table1>0)]
  print("第几部分")
  print(table1)
}
## 17、教材开发率C17                   (ok)
c17 <- df$f6
## 18、个别化教学使用率C18             (ok)
c18 <- df$f7