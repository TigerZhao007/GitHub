
userScoreGen <- function(user.score, copyright_cancel_record_info, is.agent = F){
  
  userScoreCom <- function(scores,alpha,c){
    scores1 <- 5-scores  #对作品的信用为0-5，其中5为最差，这里计算人的信用分需要做极性变换
    temp <- 50/(1+exp(-alpha*(scores1 + c))) + 50
    temp <- round(mean(temp),3)
    return(temp)
  }
  
  works.score.comput.user <- user.score[, c("Serial_Num","CopyRightUserName", "CopyRightName",
                                            "UserName","RegisterWay", "score","CurrentStatus" )]
  
  cancel.work <- copyright_cancel_record_info[,c("Serial_Num", "RegisterUserName", "CopyRightName",
                                                 "UserName", "RegisterWay","CurrentStatus")]
  names(cancel.work)[2] <- "CopyRightUserName"
  cancel.work$score <- 5
  works.score.comput.user <- bind_rows(works.score.comput.user, cancel.work)
  
  if(is.agent){
    works.score.comput.user <- filter(works.score.comput.user, RegisterWay %in% c("代理人申请", "代理申请"))
    result <- ddply(works.score.comput.user, .(UserName), function(x){
      # nrow(x)
      temp.num <- nrow(x)
      temp.pass <- nrow(x[which(x$CurrentStatus == "approve_pass" | x$CurrentStatus == "approve_ing_pass"), ])
      temp.nopass <- nrow(x[which(x$CurrentStatus == "approve_nopass"), ])
      temp.retreat <- nrow(x[which(x$CurrentStatus == "approve_retreat" | x$CurrentStatus == "accept_retreat"), ])
      temp.frozen <- nrow(x[which(x$CurrentStatus == "IsFrozen"), ])
      temp.other <- temp.num - (temp.pass+temp.nopass+temp.retreat+temp.frozen)
      pass.ratio <- round(temp.pass/temp.num, digits = 4) * 100
      
      temp <- data.frame(CopyRightName = x$CopyRightName[1], 
                         UserName = x$UserName[1], 
                         RegisterWay = x$RegisterWay[1], 
                         WorkNum = temp.num,
                         WorkPassNum = temp.pass, 
                         WorkNopassNum = temp.nopass,
                         WorkRetreatNum = temp.retreat, 
                         WorkFrozenNum = temp.frozen, 
                         WorkOtherNum = temp.other, 
                         WorkPassRatio = pass.ratio)
      
      loc <- which(x$score >= 0)
      if(length(loc != 0)){
        sum.score <- userScoreCom(x$score[loc], 1.5, -2.5)   
      }else{
        sum.score <-  mean(x$score)
      }
      temp$score <- sum.score
      return(temp)
    }, .progress = "text", .drop = F)
    
  } else {
    works.score.comput.user <- filter(works.score.comput.user, !is.na(CopyRightUserName))
    result <- ddply(works.score.comput.user, .(CopyRightUserName), function(x){
      # nrow(x)
      temp.num <- nrow(x)
      temp.pass <- nrow(x[which(x$CurrentStatus == "approve_pass" | x$CurrentStatus == "approve_ing_pass"), ])
      temp.nopass <- nrow(x[which(x$CurrentStatus == "approve_nopass"), ])
      temp.retreat <- nrow(x[which(x$CurrentStatus == "approve_retreat" | x$CurrentStatus == "accept_retreat"), ])
      temp.frozen <- nrow(x[which(x$CurrentStatus == "IsFrozen"), ])
      temp.other <- temp.num - (temp.pass+temp.nopass+temp.retreat+temp.frozen)
      pass.ratio <- round(temp.pass/temp.num, digits = 4) * 100
      
      temp <- data.frame(CopyRightName = x$CopyRightName[1], 
                         UserName = x$UserName[1], 
                         RegisterWay = x$RegisterWay[1], 
                         WorkNum = temp.num, 
                         WorkPassNum = temp.pass, 
                         WorkNopassNum = temp.nopass, 
                         WorkRetreatNum = temp.retreat, 
                         WorkFrozenNum = temp.frozen, 
                         WorkOtherNum = temp.other, 
                         WorkPassRatio = pass.ratio)
      
      loc <- which(x$score >= 0)
      if(length(loc != 0)){
        sum.score <- userScoreCom(x$score[loc], 1.5, -2.5)   
      }else{
        sum.score <-  mean(x$score)
      }
      temp$score <- sum.score
      return(temp)
    }, .progress = "text", .drop = F)
  }
  
  return(result)
}


scoreCom <- function(s,alpha = 0.33){
  alpha1 <- 1 - alpha
  if(length(which(s == 500)) != 0 ){
    s <- s[!(s == 500)]
  }
  if(length(s)==1){
    return(s)
  }else if(length(s) == 0){
    return(-1000)
  }else{
    temps <- s[1]
    for(i in 2:length(s)){
      temps <- alpha1*s[i] + alpha*temps
    }
  }  
  return(temps)
}
