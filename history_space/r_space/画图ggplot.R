library(ggplot2)
dat <- data.frame(x1=rnorm(100,mean = 5,sd=10),x2=1)

plot1 = ggplot(dat, aes(x=x1))+
  geom_histogram(binwidth = 5, fill = "lightblue", colour = "black")+
  geom_density(alpha=0.3)
plot1
plot1 = ggplot(dat, aes(x=x1))+geom_density(alpha=0.3)


dat <- read.csv('H:\\工作文件\\user.credit.person.update.csv')
qplot(agentCredit,data = dat) + facet_grid(.~UserCity)
# 一列多行
plot1 <- ggplot(dat, aes(x=agentCredit,fill=UserCity)) + geom_density() + facet_grid(UserCity~.) 
plot2 <- plot1 + coord_flip()
# 一行多列
plot3 <- ggplot(dat, aes(x=agentCredit,fill=UserCity)) + geom_density() + facet_grid(.~UserCity)
plot3
plot4 <- ggplot(dat, aes(x=agentCredit,fill=UserCity)) + geom_density() + facet_wrap(~UserCity) 
plot4
