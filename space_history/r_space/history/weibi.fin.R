
# library(xlsx)
library(Rwordseg)
# library(rJava)
# weibo <- read.xlsx("C:/Users/lujian/Desktop/new_weiboxl2.xlsx",
#                     sheetIndex = "Sheet", header =TRUE,
#                     stringsAsFactors = FALSE,encoding = "UTF-8")
weibo <- read.csv("C:/Users/lujian/Desktop/new_weiboxl2.csv",
                   header =TRUE, stringsAsFactors = FALSE)
str(weibo)


## --------------------------------------------------------------
# sex
weibo.sex <- weibo$sex
table(weibo.sex)
pie(table(weibo.sex), col = c(4, "#ff1493"))


## --------------------------------------------------------------
# address
weibo.address <- substr(weibo$location, 1, 2)
weibo.address.sort <- sort(table(weibo.address), decreasing = TRUE)
plot(weibo.address.sort[1:10], type = "h")
# pie(weibo.address.sort, col = 1:35)


## --------------------------------------------------------------
# comment time
comment.time1 <- weibo$time
comment.time2 <- as.POSIXlt(comment.time1, format="%m-%d %H:%M")
comment.time  <- comment.time2[!is.na(comment.time2)]
# head(comment.time, 30)
# comment.time <- sort(comment.time)
# str(comment.time)
hist(comment.time, breaks = 24)

## --------------------------------------------------------------
# registered date
regi.date <- as.Date(weibo$regi_date, format="%Y-%m-%d")
str(regi.date)
# hist(regi.date, breaks = 10)  ?ʱ��������ô��ͼ


## --------------------------------------------------------------
# unique ID
unique.ID <- duplicated(weibo$uid)  
# head(unique.ID, 30) 
weibo.ID <- weibo$uid[!unique.ID]
# str(weibo.ID)


## --------------------------------------------------------------
# phone type
# all phone type
all.phone <- read.csv(file="C:/Users/lujian/Desktop/phone.csv",
                      stringsAsFactors = FALSE)
# str(all.phone)
all.phone1 <- all.phone[215:332, 2]
# str(all.phone1)
allphone <- c(all.phone1, "��ҫ", "����", "����", "HUAWEI", 
                "IPad", "iPhone", "Android") 

# phone type
insertWords(allphone)   #�ʿ�����
phone.type1 <- segmentCN(weibo$source)    #�ִ�
# JAVA������������������·����ִ�
# phone.exa <- enc2utf8(weibo$source) #תutf-8����Щ��ʽ����֧��
# phone.exa <- phone.exa[Encoding(phone.exa) != "unknown"]
# phone.type1 <- segmentCN(phone.exa)
# ɸѡ����ʻ�
keep.word <- function(x, y, txt){
  y <- x[x %in% txt]
  y
}
phone.type2 <- c()
phone.type2 <- lapply(phone.type1, keep.word, phone.type2, allphone)
phone.type <- unlist(phone.type2)
str(phone.type)
# �ֻ����̷���
phone.type3 <- phone.type
for (i in 1:length(phone.type)) {
  if(phone.type[i] == "����")    phone.type3[i] <- "����"
  if(phone.type[i] == "HUAWEI")  phone.type3[i] <- "��Ϊ"
  if(phone.type[i] == "��ҫ")    phone.type3[i] <- "��Ϊ"
  if(phone.type[i] == "����")    phone.type3[i] <- "С��"
}
# ��Сת��Ϊ������
pie(table(phone.type3))
# ����״ͼ
# ϵͳ��Ӫ����
# ������


