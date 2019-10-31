library("xlsx")
library(nnet)            #安装nnet软件包

data <- read.xlsx("C:\\Users\\SDK\\Desktop\\shangpin2.xlsx",sheetName = "Sheet1",encoding = "UTF-8")
head(data)

source <- data$price2
srcLen<-length(source)
for(i in 1:10){  #预测最后十个数；
  real <- source[srcLen-i+1] #实际值
  xNum=(srcLen-i+1)%/%7      #组数
  yNum=7                     #每组7个数
  data<-array(1:(xNum*yNum),c(xNum,yNum))
  
  pre=srcLen-i+1;
  for(x in 1:xNum){          #数组赋值
    for(y in 1:yNum){
      data[x,y]=source[pre]
      pre=pre-1;
      
    }
    if(pre<7){
      break;
    }
  }
  ascData<-array(1:(xNum*yNum),c(xNum,yNum)) #数组逆序
  for(x in 1:xNum){
    for(y in 1:yNum){
      ascData[x,y]=data[xNum-x+1,y]
    }
  }
  colnames(ascData) <- c("a","b","c","d","e","f","g") #每列列名
  
  trainData<-data.frame(scale(ascData[,c(1:7)]))      
  
  nn<-nnet(a~b+c+d+e+f+g,trainData[1:(xNum-1),],size=10,decay=0.01,maxit=1000,linout=F,trace=F)
  predict<-predict(nn,trainData[xNum,])
  
  predict=predict*sd(ascData[,1])+mean(ascData[,1])
  percent <- (predict-real)*100/real
  res <- paste("预测值：",predict,"实际值：",real,"误差：",percent)
  print(res)
}
