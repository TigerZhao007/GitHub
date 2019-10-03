# bage
install.packages('RCurl')
library(RCurl);library(XML);library(plyr)

## ----------------------------------------
myheader=c("User-Agent"="Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",  
           "Accept"="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",  
           "Accept-Language"="en-us",  
           "Connection"="keep-alive",  
           "Accept-Charset"="GB2312,utf-8;q=0.7,*;q=0.7"  
)


webpage = getURL('https://item.jd.com/12107414.html#comments-list',httpheader=myheader,.encoding='utf-8')  
pagetree = htmlParse(webpage,encoding='utf-8')  
comment = xpathSApply(pagetree,"//div[@class='comment-content']",xmlValue)  

comment = iconv(comment,"utf-8","LATIN1")  

comment

## ------------------------------------------

library(RCurl)
getcoments <- function(i){
  productid <- '2967929'  #商品id
  t1 <- 'http://club.jd.com/comment/productPageComments.action?productId='
  t2 <- '&score=0&sortType=1&page='  #按时间顺序
  t3 <- '&pageSize=1' #设置每页1条评论
  url <-paste0(t1,productid,t2,i,t3)
  web <- getURL(url, .encoding = 'gbk')
  comments <- substr(web,regexpr("comments", web)+10,regexpr("referenceTime", web)-4)
  content <- substr(comments,regexpr("content", comments)+10,regexpr("creationTime", comments)-4)
}

comment <- c()
n <- 30 #爬取评论条数
for(i in 0:(n-1)){
  comment <- rbind(comment,getcoments(i))
  print(i+1)
  Sys.sleep(1)
}
comment

http://club.jd.com/comment/productPageComments.action?productId=2967929&score=0&sortType=1&page=1&pageSize=1

http://club.jd.com/comment/productPageComments.action?productId=2967929&score=0&sortType=5&page=0&pageSize=10

callback=fetchJSON_comment98vv92760&&isShadowSku=0&fold=1



