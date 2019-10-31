dat <- read.csv('H:\\工作文件\\user.credit.person.update.csv')
#,encoding = 'UTF-8'
library(ggplot2)

ggplot()
qplot(agentCredit,data = dat) + facet_grid(.~UserCity)
names(dat)

ggplot(dat, aes(x=agentCredit,fill=UserCity)) + geom_density() + coord_flip()



