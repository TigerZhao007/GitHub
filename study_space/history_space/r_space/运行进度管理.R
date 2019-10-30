#--------------------------------------------------------------------------
# 进度条类型1 （推荐）
library(tcltk)  
#开启进度条
pb <- tkProgressBar("进度","已完成 %", 0, 100) 
u <- 1:2000000
for(i in u) {  
  info<- sprintf("已完成 %d%%", round(i*100/length(u)))  
  setTkProgressBar(pb, i*100/length(u), sprintf("进度 (%s)", info),info)  
}     
#关闭进度条  
close(pb)  

#开启进度条
pb <- tkProgressBar("进度","已完成 %", 0, 100) 
u <- 1:2000000
x <- c()
for(i in u) {  
 # info<- sprintf("已完成 %d%%", round(i*100/length(u)))
 # setTkProgressBar(pb, i*100/length(u), sprintf("进度 (%s)", info),info) 
  x[i] <- i*10/2+100 
}     
#关闭进度条  
close(pb) 

#--------------------------------------------------------------------------
# 进度条类型2
library(tcltk)
library(tcltk2)

root <- tktoplevel()
l1 <- tk2label(root)
pb1 <- tk2progress(root, length = 300)
tkconfigure(pb1, value = 0, maximum = 9)
tkgrid(l1, row = 0)
tkgrid(pb1, row = 1)

for (index in 1:10){
  tkconfigure(l1, text = paste("Index", index))
  tkconfigure(pb1, value = index - 1)
  Sys.sleep(1)
}
