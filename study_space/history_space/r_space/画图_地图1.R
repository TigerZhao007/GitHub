
# 绘制世界地图&美国地图
library(maps)  # maps包括世界赌徒和美国地图数据
#maps::world.cities
map("world", fill = TRUE, col = rainbow(200),ylim = c(-60, 90), mar = c(0, 0, 0, 0))
title("世界地图")

# 绘制中国地图1
library(maps)
library(mapdata)
map("china", col = "red4", ylim = c(18, 54), panel.first = grid())
title(" 中国地图")

# 绘制中国地图2
library(sp)
library(maptools)
library(ggplot2)
library(mapproj)
x=readShapePoly('F:/data/map/bou2_4m/bou2_4p.shp')
plot(x)
ggplot(x,aes(x=long,y=lat,group=group))+
  geom_polygon(fill="white",colour="grey") +
  coord_map("polyconic")

xz <- x@data  #读取行政信息
xs <- data.frame(x,id=seq(0:924)-1)          #含岛屿共925个形状

china_map1 <- fortify(x)     #转化为数据框
library(plyr)
china_map_data <- join(china_map1, xs,by='id', type = "full")#合并两个数据框

# 绘制业务数据（缺数据）
#mydata <- read.csv('')
#china_data <- join(china_map_data,mydata,type='full')
#ggplot(china_data, aes(x = long, y = lat, group = group, fill = zhibiao)) +
#  geom_polygon(colour="grey40") +
#  scale_fill_gradient(low="white",high="steelblue") +  #指定渐变填充色，可使用RGB
#  coord_map("polyconic")        #指定投影方式为polyconic，获得常见视角中国地图

# 给制定省份填上颜色
getColor=function(mapdata,provname,provcol,othercol){    
  f=function(x,y) ifelse(x %in% y,which(y==x),0); 
  colIndex=sapply(mapdata@data$NAME,f,provname); 
  col=c(othercol,provcol)[colIndex+1]; 
  return(col); 
}
provname=c("北京市","广东省","海南省","重庆市") 
provcol=c("red","green","yellow","purple") 
plot(x,col=getColor(x,provname,provcol,"white")) 
as.character(na.omit(unique(x@data$NAME)))
provname=c("北京市","天津市","河北省","山西省","内蒙古自治区", "辽宁省","吉林省","黑龙江省","上海市","江苏省", "浙江省","安徽省","福建省","江西省","山东省", "河南省","湖北省","湖南省","广东省", "广西壮族自治区","海南省","重庆市","四川省","贵州省", "云南省","西藏自治区","陕西省","甘肃省","青海省", "宁夏回族自治区","新疆维吾尔自治区","台湾省", "香港特别行政区") 
pop=c(1633,1115,6943,3393,2405,4298,2730,3824,1858,7625, 5060,6118,3581,4368,9367,9360,5699,6355,9449, 4768,845,2816,8127,3762,4514,284,3748,2617, 552,610,2095,2296,693) 
plot(x,fg=getColor(x,provname,provcol,"white"),xlab="",ylab="")
#???????????????????????????

# 绘制部分省份地图          （推荐）
getID=function(mapdata,provname){ 
  index=mapdata$att.data$NAME %in% provname;
  ids=rownames(mapdata@data[index,]);
  return(as.numeric(ids)); }

midchina=c("河南省","山西省","湖北省","安徽省","湖南省","江西省");
plot(x, col = getColor(x, midchina, rep("green", 6),"white"), border = "white", xlab = "", ylab = "")



# 利用googleVis包
library(googleVis)
provname=c("CN-11","CN-12","CN-13","CN-14","CN-15","CN-21","CN-22","CN-23","CN-31","CN-32","CN-33","CN-34","CN-35","CN-36","CN-37","CN-41","CN-42","CN-43","CN-44","CN-45","CN-46","CN-50","CN-51","CN-52","CN-53","CN-54","CN-61","CN-62","CN-63","CN-64","CN-65");
pop=c(110.56,112.51,113.43,112.52,108.45,112.83,111.23,109.71,110.64,116.51,113.86,127.85,117.93,114.74,112.17,118.46,128.18,126.16,130.30,125.55,135.64,115.13,116.01,107.03,108.71,102.73,122.10,114.82,110.35,108.79,106.12)
a<-data.frame(provname,pop)
G2 <- gvisGeoChart(a, locationvar='provname', colorvar='pop',options=list(region='CN',displayMode="regions",resolution="provinces",colorAxis="{colors: ['yellow','red']}" ))
plot(G2)

# 利用ggmap包 （翻墙）
library(ggmap)
#1) geocode():可以返回一个地方的经纬度
geocode("Guangzhou")

#2) mapdist():可以返回两地的距离
mapdist('China Agricultural University','Renmin University of China', 'walking')

#3）画中国地图：
library(ggmap) 
library(mapproj)
map <- get_map(location = 'China', zoom = 4)
ggmap(map)



