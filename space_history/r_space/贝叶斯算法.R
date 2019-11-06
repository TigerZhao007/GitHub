#!/usr/bin/Rscript
#构造训练集  
data <- matrix(c("sunny","hot","high","weak","no",  
                 "sunny","hot","high","strong","no",  
                 "overcast","hot","high","weak","yes",  
                 "rain","mild","high","weak","yes",  
                 "rain","cool","normal","weak","yes",  
                 "rain","cool","normal","strong","no",  
                 "overcast","cool","normal","strong","yes",  
                 "sunny","mild","high","weak","no",  
                 "sunny","cool","normal","weak","yes",  
                 "rain","mild","normal","weak","yes",  
                 "sunny","mild","normal","strong","yes",  
                 "overcast","mild","high","strong","yes",  
                 "overcast","hot","normal","weak","yes",  
                 "rain","mild","high","strong","no"), 
               byrow = TRUE,  
               dimnames = list(day = c(),condition = c("outlook","temperature","humidity","wind","playtennis")), 
               nrow=14, 
               ncol=5);  

#计算先验概率  
prior.yes = sum(data[,5] == "yes") / length(data[,5]);  
prior.no  = sum(data[,5] == "no")  / length(data[,5]);  

#贝叶斯模型  
naive.bayes.prediction <- function(condition.vec) {  
  # Calculate unnormlized posterior probability for playtennis = yes.  
  playtennis.yes <-  
    sum((data[,1] == condition.vec[1]) & (data[,5] == "yes")) / sum(data[,5] == "yes") * # P(outlook = f_1 | playtennis = yes)  
    sum((data[,2] == condition.vec[2]) & (data[,5] == "yes")) / sum(data[,5] == "yes") * # P(temperature = f_2 | playtennis = yes)  
    sum((data[,3] == condition.vec[3]) & (data[,5] == "yes")) / sum(data[,5] == "yes") * # P(humidity = f_3 | playtennis = yes)  
    sum((data[,4] == condition.vec[4]) & (data[,5] == "yes")) / sum(data[,5] == "yes") * # P(wind = f_4 | playtennis = yes)  
    prior.yes; # P(playtennis = yes)  
  
  # Calculate unnormlized posterior probability for playtennis = no.  
  playtennis.no <-  
    sum((data[,1] == condition.vec[1]) & (data[,5] == "no"))  / sum(data[,5] == "no")  * # P(outlook = f_1 | playtennis = no)  
    sum((data[,2] == condition.vec[2]) & (data[,5] == "no"))  / sum(data[,5] == "no")  * # P(temperature = f_2 | playtennis = no)  
    sum((data[,3] == condition.vec[3]) & (data[,5] == "no"))  / sum(data[,5] == "no")  * # P(humidity = f_3 | playtennis = no)  
    sum((data[,4] == condition.vec[4]) & (data[,5] == "no"))  / sum(data[,5] == "no")  * # P(wind = f_4 | playtennis = no)  
    prior.no; # P(playtennis = no)  
  
  return(list(post.pr.yes = playtennis.yes,  
              post.pr.no  = playtennis.no,  
              prediction  = ifelse(playtennis.yes >= playtennis.no, "yes", "no")));  
}  

#预测  
naive.bayes.prediction(c("overcast", "mild", "normal", "weak"));
