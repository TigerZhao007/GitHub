# 加载软件包
if(!require(plyr)){install.packages("plyr")}
if(!require(dplyr)){install.packages("dplyr")}
if(!require(data.table)){install.packages("data.table")}
# 数据库文件
setwd("F:/工作文件/2宜开工作/4_版权商品信用分评估项目/testdata")
register_business_info <- fread('register_business_info.csv', header = T, stringsAsFactors = F) 
# score reference table
config_reasonlist <- fread('config_reasonlist.csv', header = T, stringsAsFactors = F)
# user info
user_register_info <- fread('user_register_info.csv', header = T, stringsAsFactors = F)
# work info
register_data_info <- fread('register_data_info.csv', header = T, stringsAsFactors = F)
# cancel info
copyright_cancel_record_info <- fread('copyright_cancel_record_info.csv', header = T, stringsAsFactors = F)

credit_user <- fread('credit_user.csv', header = T, stringsAsFactors = F)
credit_work <- fread('credit_work.csv', header = T, stringsAsFactors = F)

# 本地文件
register_business_info.old1 <- fread('work_flow_1503_160920.csv', header = T, stringsAsFactors = F)
register_business_info.old1$reason_ids <- as.character(register_business_info.old1$reason_ids)
register_business_info.old2 <- fread("work_flow_160921_161118.csv", header = T, stringsAsFactors = F)
register_business_info.old3 <- fread("work_flow_161118_170119.csv", header = T, stringsAsFactors = F)
#~~


# Serial_Num of whole works 
Serial_Num.whole <- unique(register_data_info$Serial_Num)
# generate work flow by groups of work Serial_Num
workflow <- 
  left_join(register_data_info[,c('CopyRightUserName','Serial_Num')], 
            register_business_info[,c('id',"Serial_Num","OperateTime", "Auditor", "status", "reason_ids")], 
            by = 'Serial_Num') 
workflow <- filter(workflow, !grepl('ing',status), !is.na(OperateTime))
workflow.local <- 
  bind_rows(register_business_info.old1, register_business_info.old2, register_business_info.old3)%>%
  filter(., !grepl('ing',status), !is.na(OperateTime))

workflow <- left_join(workflow, workflow.local[,c("id", "reason_ids")], by = "id")
loc.update <- which(!is.na(workflow$reason_ids.y))
workflow$reason_ids.x[loc.update] <- workflow$reason_ids.y[loc.update]
workflow <- workflow[,-which(names(workflow) == "reason_ids.y")]
names(workflow)[which(names(workflow) == 'reason_ids.x')] <- 'reason_ids'

# extract works with no reason information
workflow.reasonLess <- ddply(workflow, .(Serial_Num), function(x){
  id <- which(is.na(x$reason_ids))
  if (length(id) > 0) x$reason_ids[id] <- ''
  if (all(x$reason_ids == '')) return(x)
},.progress = 'text')

# extract works with reason info
workflow.reason <- dplyr::filter(workflow, !(Serial_Num %in% workflow.reasonLess$Serial_Num))

# seprite reason info, the reason ids of each state were combined as strings by ','.So in this
# step I seprite this strings into single rows of the dataframe.
reason.label <- c("accept_correct", "approve_nopass", "approve_correct", "approve_ing_correct", 
                  "approve_ing_nopass", "accept_nopass", "accept_ing_correct", "accept_ing_nopass")
workflow.reason.sep <- ddply(workflow.reason, .(Serial_Num), function(x){
  reasion.loc <- which(x$status %in% reason.label) # if there is reasion info in this work flow
  if(length(reasion.loc) > 0){
    # seprite reasons to be single rows in the dataframe
    temp.reason <- data.frame()
    for(i in reasion.loc){
      resonid <- unlist(strsplit(x$reason_ids[i], split = ','))
      if(length(resonid) > 1){
        reason.sep <- data.frame(x[i,-which(names(x) == 'reason_ids')],
                                 "reason_ids" = resonid, stringsAsFactors = F)
      }else{
        reason.sep <- x[i,]
      }
      temp.reason <- bind_rows(temp.reason, reason.sep)
    }
    x1 <- bind_rows(x[-reasion.loc,],temp.reason) %>% arrange(., OperateTime)
    
    return(x1)
  }
  return(x)
}, .progress = 'text')

# add scores from config_reasonlist
names(config_reasonlist)[1] <- 'reason_ids'
config_reasonlist$reason_ids <- as.character(config_reasonlist$reason_ids)
workflow.reason.sep.score <- left_join(workflow.reason.sep,
                                       config_reasonlist[,c("reason_ids", "credit_weight")] , 
                                       by = 'reason_ids')
# sum scores in same handle status
workflow.reason.sep.score.sum <-
  ddply(workflow.reason.sep.score, .(Serial_Num, OperateTime), function(x){
    s <- na.omit(x$credit_weight)
    if (length(s) == 0){
      score <- NA
    } else {
      score <- sum(s)
      if (score > 5) score <- 5
    }
    data.frame(x$Auditor[1],x$status[1],score)
  },.progress = 'text')
names(workflow.reason.sep.score.sum)[3:5] <- c('Auditor', 'status', 'score')
# it was found that: 'nrow(workflow.reason.sep.score.sum) < nrow(workflow.reason)', and it is all because of
# there are records like:
# > CopyRightUserName        Serial_Num         OperateTime Auditor status reason_ids  id
# > 1            cyjy88 2016Z11JS00193855 2016-12-20 17:01:36    <NA> submit            148
# > 2            cyjy88 2016Z11JS00193855 2016-12-20 17:01:36    <NA> submit            149
# in workflow.reason so that is why this happen.

workflow.reasonLess$score <- NA
workflow.reasonLess.score <- workflow.reasonLess[, names(workflow.reason.sep.score.sum)]
workflow.reason.sep.score.sum <- transform(workflow.reason.sep.score.sum, 
                                           Auditor = as.character(Auditor), 
                                           status = as.character(status))
# combine data with score and without
workflow.score.sum <- bind_rows(workflow.reason.sep.score.sum, workflow.reasonLess.score)

# data clean in each work flow before comput the final score
date <- Sys.Date()
# x <- filter(workflow.reason.sep.score.sum, Serial_Num == '2015Z11JS00082988')
workflow.score.sum.handle1 <- ddply(workflow.score.sum, .(Serial_Num), function(x){
  len <- nrow(x)
  
  # 通过与不通过的评分
  if(x$status[len] == "approve_pass" || x$status[len] == "accept_pass"){
    x$score[len] <- 0
  }else if(x$status[len] == "approve_nopass" || x$status[len] == "accept_nopass"){
    if(is.na(x$status[len]) || (length(na.omit(x$score)) == 0)){
      x$score[len] <- 5 
    }
  }else if(x$status[len] == "accept_retreat" || x$status[len] == "approve_correct" || x$status[len] == "accept_correct" || x$status[len] == "approve_retreat"){
    dif.time <- as.numeric(date - as.Date(x$OperateTime[len]))
    if(dif.time > 31 & dif.time <= 180){
      if(is.na(x$score[len])){
        x$score[len] <- -1000
      }else if(x$score[len] < 5){  # 如果信用评分不是5分，但是由于超过补证期限因此加上1分的罚分
        x$score[len] <- pmin(x$score[len] + 1, 5) 
      }
    }else if(dif.time > 180){      # 超过半年未补证视为不通过
      x$score[len] <- 5
    }else {
      x$score[len] <- -1000
    }
  }else{
    x$score[len] <- -1000          # 用-1000标记未完成的流程
  }
  return(x)
}, .progress = 'text')


# the final score of each work (input for user credit comput)
work.reason.score.final <- ddply(workflow.score.sum.handle1,.(Serial_Num),function(x){
  score.serise <- as.numeric(na.omit(x$score))  # 得分序列 
  thescore <- scoreCom(score.serise)
  temp <- data.frame('OperateTime' = x$OperateTime[nrow(x)], 'score' = thescore, 'status' = x$status[nrow(x)])
  return(temp)
}, .progress = "text")
names(work.reason.score.final)[which(names(work.reason.score.final) == "Time")]<- "OperateTime"

# reshape data for output
work.score.info <- left_join(work.reason.score.final, register_business_info[,c("Serial_Num","OperateTime",
                                                                               "Nopass_explain")], by = c("Serial_Num", "OperateTime")) %>%
  left_join(., register_data_info[,c("Serial_Num","RegisterType", "UserName", "CopyRightName", "RegisterWay",
                                    "CopyRightUserName", "WorkName", "WorkType","BelongRegion", 
                                    "CurrentStatus")], by = "Serial_Num") %>% unique(.)

work.score.info <- data.frame("Serial_Num" = work.score.info$Serial_Num,
                              "Nopass_explain" = work.score.info$Nopass_explain,
                              "finalScore" = work.score.info$score,
                              "RegisterType" = work.score.info$RegisterType,
                              "UserName" = work.score.info$UserName,
                              "CopyRightName" = work.score.info$CopyRightName,
                              "RegisterWay" = work.score.info$RegisterWay,
                              "CopyRightUserName" = work.score.info$CopyRightUserName,
                              "WorkName" = work.score.info$WorkName,
                              "WorkType" = work.score.info$WorkType,
                              "OperateTime" = work.score.info$OperateTime,
                              "BelongRegion" = work.score.info$BelongRegion,
                              "CurrentStatus" = work.score.info$CurrentStatus,
                              "correctTimes" = NA, stringsAsFactors = F)
work.score.info <- transform(work.score.info, finalScore = 5 - finalScore)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~####
# PART 2 USER CREDIT ####
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##---------------------------------------------------------####
#### 2.1 credit comput      ####
# credit score of each work
# credit score of each user
user.score <- left_join(work.reason.score.final, register_data_info[,c("Serial_Num", 'RegisterType', 
                                                                       'UserName',"RegisterWay", "CopyRightUserName", "CopyRightName","OperateTime",
                                                                       "CurrentStatus")],by = "Serial_Num")

# user credit score 
user.score.agg <- userScoreGen(user.score, copyright_cancel_record_info, is.agent = F)
user.score.agg$UserName <- as.character(user.score.agg$UserName)
user.credit.wholeinfo <- 
  left_join(user.score.agg, user_register_info[c("UserName", "RealName", "CertificateNum",
                                                 "ObtainAddress", "UserCity","UserDistrict", 
                                                 "UserType")], by = 'UserName')

names(user.credit.wholeinfo)[which(names(user.credit.wholeinfo) == 'score')] <- "agentCredit"
user.credit.wholeinfo.person <- user.credit.wholeinfo[c('CopyRightUserName','agentCredit','WorkNum',
                                                        'WorkPassNum','WorkNopassNum','WorkRetreatNum',
                                                        'WorkFrozenNum','WorkOtherNum','WorkPassRatio',
                                                        'RealName','CertificateNum','ObtainAddress',
                                                        'UserCity','UserDistrict','UserType')]
names(user.credit.wholeinfo.person)[1] <- "UserName"     # use CopyRightUserName as UserName
# agent credit score
agent.score.agg <- userScoreGen(user.score, copyright_cancel_record_info, is.agent = T)
agent.score.agg$UserName <- as.character(agent.score.agg$UserName)
agent.credit.wholeinfo <- 
  left_join(agent.score.agg, user_register_info[c("UserName", "RealName", "CertificateNum", 
                                                  "ObtainAddress", "UserCity","UserDistrict", 
                                                  "UserType")], by = 'UserName')
names(agent.credit.wholeinfo)[which(names(agent.credit.wholeinfo) == 'score')] <- "agentCredit"
user.credit.wholeinfo.agent <- 
  agent.credit.wholeinfo[c('UserName','agentCredit','WorkNum','WorkPassNum','WorkNopassNum',
                           'WorkRetreatNum','WorkFrozenNum','WorkOtherNum','WorkPassRatio',
                           'RealName','CertificateNum','ObtainAddress','UserCity','UserDistrict',
                           'UserType')]

names(user.credit.wholeinfo.agent)[3:9] <- 
  c("AgentWorkNum", "AgentWorkPassNum", "AgentWorkNopassNum","AgentWorkRetreatNum", 
    "AgentWorkFrozenNum", "AgentWorkOtherNum", "AgentWorkPassRatio")


































