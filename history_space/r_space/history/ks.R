# 以数据框形式导入数据，第一列为pre,第二列为class.
ks_dat_pc <- function(dat_p,low=0,high=1,by=0.05){
  pred0 <- dat_p[which(dat_p[,2]==0),]
  pred1 <- dat_p[which(dat_p[,2]==1),]
  cut_0 <- cut(pred0[,1], breaks = seq(low,high,by))
  cut_1 <- cut(pred1[,1], breaks = seq(low,high,by))
  ks <- data.frame()
  ks[1:length(levels(cut_0)),1] <- levels(cut_0)
  for(i in 1:length(levels(cut_0))){  ks[i,2] <- table(cut_0)[[i]]  }
  for(i in 1:length(levels(cut_0))){  ks[i,3] <- table(cut_1)[[i]]  }
  ks[,4] <- cumsum(table(cut_0))/sum(ks$V2)
  ks[,5] <- cumsum(table(cut_1))/sum(ks$V3)
  ks[,6] <- ks[,4] - ks[,5]
  colnames(ks) <- c('section','bad_0','good_1','add_bad_0','add_good_1','ks_value')
  return(ks)
}

# 以数据分开赋值输入，参数pre和class必须填写。
ks_pc <- function(pre,class,low=0,high=1,by=0.05){
  pred0 <- pre[which(class==0)]
  pred1 <- pre[which(class==1)]
  cut_0 <- cut(pred0, breaks = seq(low,high,by))
  cut_1 <- cut(pred1, breaks = seq(low,high,by))
  ks <- data.frame()
  ks[1:length(levels(cut_0)),1] <- levels(cut_0)
  for(i in 1:length(levels(cut_0))){  ks[i,2] <- table(cut_0)[[i]]  }
  for(i in 1:length(levels(cut_0))){  ks[i,3] <- table(cut_1)[[i]]  }
  ks[,4] <- cumsum(table(cut_0))/sum(ks$V2)
  ks[,5] <- cumsum(table(cut_1))/sum(ks$V3)
  ks[,6] <- ks[,4] - ks[,5]
  colnames(ks) <- c('section','bad_0','good_1','add_bad_0','add_good_1','ks_value')
  return(ks)
}

myks<-function(y,predict_y){  
  library(ROCR)  
  pred <- prediction(predictions=predict_y,labels=y)  
  perf <- performance(pred,"tpr","fpr")  
  tmp<-max(attr(perf,"y.values")[[1]]-attr(perf,"x.values")[[1]])  
  return(tmp)}


