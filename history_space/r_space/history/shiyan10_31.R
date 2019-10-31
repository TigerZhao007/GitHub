install.packages('rjson')
library(rjson)
phone <- read.csv('C:\\Users\\SDK\\Desktop\\yuecai\\phone.csv')
fromJSON(phone$y[1],phone_name         )
?fromJSON
