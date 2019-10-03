library("xlsx")
library(AMORE)
data <- read.xlsx("C:\\Users\\SDK\\Desktop\\zhishu.xlsx",
                  sheetName = "Sheet1",encoding = "UTF-8")
head(data)
n_data <- nrow(data)
train_data <- data[1:(0.8*n_data),]
test_data  <- data[(0.8*n_data):(n_data),]

net <- newff(n.neurons=c(5,3,3,1), learning.rate.global=1e-2, momentum.global=0.5,
             error.criterium="LMS", Stao=NA, hidden.layer="tansig", 
             output.layer="purelin", method="ADAPTgdwm")

result <- train(net, train_data[2:6], train_data[7], 
                error.criterium="LMS", report=TRUE, show.step=100, n.shows=5 )

summary(result)
str(result)
result$net
result$Merror
head(sim(net,train_data[2:6]))
?sim
