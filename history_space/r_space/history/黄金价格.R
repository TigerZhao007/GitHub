library("xlsx")

# 导入数据
dat <- read.xlsx("C:\\Users\\SDK\\Desktop\\huangjin.xlsx",
                  sheetName = "Sheet1",encoding = "UTF-8")
head(dat)
str(dat)
names(dat) <- c("date", "price_gold", "index_dollar","rate_dollar", "index_djia", "price_crude")


# 绘制趋势图
plot(dat$price_gold)
axis(1,1:length(dat$date),labels= dat$date)

par(mfrow=c(2,2))
plot(dat$index_dollar)
axis(1,1:length(dat$date),labels= dat$date)
plot(dat$rate_dollar)
axis(1,1:length(dat$date),labels= dat$date)
plot(dat$index_djia)
axis(1,1:length(dat$date),labels= dat$date)
plot(dat$price_crude)
axis(1,1:length(dat$date),labels= dat$date)

# 归一化处理
for(i in 2:6){
  dat[,i+10]=(dat[,i]-min(dat[,i]))/(max(dat[,i])-min(dat[,i])) 
  }


