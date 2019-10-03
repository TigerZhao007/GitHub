# 调入函数包
#----------------------------------------------------
dat_lib = function(){
  if(!require(data.table)){install.packages("data.table")}
  #if(!require(randomForest)){install.packages("randomForest")}
  if(!require(stringr)){install.packages("stringr")}
  if(!require(plyr)){install.packages("plyr")}
  if(!require(dplyr)){install.packages("dplyr")}
  library(ggplot2)
  library(devtools)  
  library(recharts)
  library(TTR)
  library(zoo)
  library(xts)
  library(forecast)
  library(reshape2)
  options(scipen = 200)
}

dat_buquan = function(dat){
  name = names(table(dat$pms_id));xw = names(table(dat$xw))
  length.out = as.Date("2018/05/31")-as.Date("2017/01/01")+1
  temp = dat %>% mutate(day = substring(day, 1, 10)) %>% mutate(by = paste(pms_id,day,xw,sep = '-')) %>% select(-c(pms_id,day,xw))
  date = seq.Date(from = as.Date("2017/01/01"), by = "day", length.out = length.out)
  temp_dat = data.frame(id = rep(name,each=(length.out*length(xw))),day = rep(date,each=length(xw)), xw=1:length(xw))
  result = temp_dat %>% mutate(by=paste(temp_dat$id,temp_dat$day,temp_dat$xw,sep = '-')) %>% left_join(.,temp,c('by'='by')) %>% select(-c(by))
}
dat_buquan2 = function(dat){
  name = names(table(dat$pms_id));xw = names(table(dat$xw))
  length.out = as.Date("2018/05/31")-as.Date("2017/01/01")+1
  temp = dat %>% mutate(day = substring(day, 1, 10)) %>% mutate(by = paste(pms_id,day,xw,sep = '-')) %>% select(-c(pms_id,day,xw))
  date = seq.Date(from = as.Date("2017/01/01"), by = "day", length.out = length.out)
  temp_dat = data.frame(id = rep(name,each=(length.out*length(xw))),day = rep(date,each=length(xw)), xw=xw)
  result = temp_dat %>% mutate(by=paste(temp_dat$id,temp_dat$day,temp_dat$xw,sep = '-')) %>% left_join(.,temp,c('by'='by')) %>% select(-c(by))
}

dat_to_dat =function(dat,queshi=0){
  # 剔除缺失值，空值，queshi=0利用同一时刻均值代替缺失值,queshi=1缺失值不替换
  func0 = function(x){x[which(is.na(x))] = NA;  x[which(x=='NULL')] = NA; x = as.numeric(x);  x[which(x==0)] = NA; x[which(is.na(x))] = mean(na.omit(x));return(x)}   #  queshi=0利用同一时刻均值代替缺失值,
  func1 = function(x){x[which(is.na(x))] = NA;  x[which(x=='NULL')] = NA; x = as.numeric(x);  x[which(x==0)] = NA; return(x) }   #  queshi=1缺失值不替换
  if(queshi==0){
    dat = data.frame(dat[,1:3],as.data.frame(apply(dat[,4:99],2,func0)))
  }
  else{
    dat = data.frame(dat[,1:3],as.data.frame(apply(dat[,4:99],2,func1)))
  }
  names(dat)[1:3] = c('pms_id','day','xw')
  return(dat)
}

dat_to_hour = function(dat){
  # 将每天96个观测点规约到24小时
  mean_func = function(x){x = na.omit(x);y = mean(x);return(y)}
  temp = data.frame(pms_id=dat$pms_id,day= substring(dat$day, 1, 10),xw =dat$xw,
                    day_xw = paste(substring(dat$day, 1, 10),dat$xw,sep = '_'),
                    h1=apply(dat[,4:7],1,mean_func),h2=apply(dat[,8:11],1,mean_func),
                    h3=apply(dat[,12:15],1,mean_func),h4=apply(dat[,16:19],1,mean_func),
                    h5=apply(dat[,20:23],1,mean_func),h6=apply(dat[,24:27],1,mean_func),
                    h7=apply(dat[,28:31],1,mean_func),h8=apply(dat[,32:35],1,mean_func),
                    h9=apply(dat[,36:39],1,mean_func),h10=apply(dat[,40:43],1,mean_func),
                    h11=apply(dat[,44:47],1,mean_func),h12=apply(dat[,48:51],1,mean_func),
                    h13=apply(dat[,52:55],1,mean_func),h14=apply(dat[,56:59],1,mean_func),
                    h15=apply(dat[,60:63],1,mean_func),h16=apply(dat[,64:67],1,mean_func),
                    h17=apply(dat[,68:71],1,mean_func),h18=apply(dat[,72:75],1,mean_func),
                    h19=apply(dat[,76:79],1,mean_func),h20=apply(dat[,80:83],1,mean_func),
                    h21=apply(dat[,84:87],1,mean_func),h22=apply(dat[,88:91],1,mean_func),
                    h23=apply(dat[,92:95],1,mean_func),h24=apply(dat[,96:99],1,mean_func))
  return(temp)
}


dat_to_quarter = function(dat){
  mean_func = function(x){x = na.omit(x);y = mean(x);return(y)}
  temp = data.frame(pms_id = dat$pms_id,day = substring(dat$day, 1, 10),xw = dat$xw,
                    day_xw = paste(substring(dat$day, 1, 10),dat$xw,sep = '_'),
                    dat[,4:99])
  return(temp)
}


dat_to_df = function(dat){
  df = melt(dat,id=c('pms_id','day','xw','day_xw'))
  df$day_hour = paste(df$day,df$variable,sep = '_')
  #df$value[which(df$value)==0] ==NA
  df$value_bz = (df$value-220)/220
  df$day_day = as.numeric(substring(df$day_hour, 9, 10))
  df = df[order(df$pms_id,df$xw,df$day,df$variable),]
  df$islow = if_else(is.na(df$value),-1,if_else(df$value<=196,1,0))
  df$isup = if_else(is.na(df$value),-1,if_else(df$value>=230,1,0))
  df$isok = if_else(is.na(df$value),-1,if_else(df$value>196&df$value<230,1,0))
  df = df %>% select(pms_id,xw,day_xw,day,day_day,day_hour,variable,value,value_bz,islow,isup,isok)
  #  df = df %>%group_by(xw) %>% mutate(timemean_1 = SMA(df$value,1),timemean_24 =  SMA(df$value,24))
  return(df)
}

dat_to_end_dec = function(dat,queshi=0){
  df = dat_to_df(dat_to_hour(dat_to_dat(dat = dat_buquan(dat),queshi = queshi)))
  return(df)
}

dat_to_end_yc = function(dat,queshi=1){
  df = dat_to_df(dat_to_quarter(dat_to_dat(dat = dat_buquan(dat),queshi = queshi)))
  return(df)
}
dat_to_end_yc2 = function(dat,queshi=1){
  df = dat_to_df(dat_to_quarter(dat_to_dat(dat = dat_buquan2(dat),queshi = queshi)))
  return(df)
}

df_decompose = function(df,pms_id,xw=1,frequency = 24,start = c(2016,5)){
  temp = ts(df$value[df$pms_id == pms_id & df$xw==xw],frequency=frequency,start=start)
  temp_dec = decompose(temp)
  date = seq.Date(from = as.Date("2016/05/01",format = "%Y/%m/%d"), by = "day", length.out = length(temp_dec$x)/24)
  result = data.frame(date = paste(rep(date,each=24),1:24,sep = '-'),series = temp_dec$x,trend = temp_dec$trend,season = temp_dec$seasonal,random = temp_dec$random)
  return(result)
}

dat_to_dec = function(df){
  name=names(table(df$pms_id));xw = names(table(df$xw));
  lis = list();num = 1;
  for(i in 1:length(name)){
    for(j in 1:length(xw)){
      lis[[num]] = df_decompose(df,pms_id = name[i],xw = xw[j])
      num = num+1
    }
  }
  names(lis) = paste(rep(name,each=length(xw)),1:length(xw),sep = '-')
  return(lis)
}

find_yichang <- function(x, k){
  n <- length(x); runs <- NULL
  for(i in 1:(n-k+1)){
    if(all( x[i:(i+k-1)] == 1 ))
      runs <- c(runs, i:(i+k-1))
  }
  yichang = unique(runs)
  return(yichang)
}


