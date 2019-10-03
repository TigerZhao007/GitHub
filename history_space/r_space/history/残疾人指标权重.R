library("xlsx")
library("pmr")
# dat <- read.xlsx("C:\\Users\\SDK\\Desktop\\指标数据1.xlsx",
#                  sheetName = "Sheet1",encoding = "UTF-8")


## -------------------------------------------------------------

##输入：judgeMatrix 判断矩阵；round 结果约分位数
##输出：权重
weight <- function (judgeMatrix, round=3) {
  n = ncol(judgeMatrix)
  cumProd <- vector(length=n)
  cumProd <- apply(judgeMatrix, 1, prod)  ##求每行连乘积
  weight <- cumProd^(1/n)  ##开n次方(特征向量)
  weight <- weight/sum(weight) ##求权重
  round(weight, round)
}
###注：CRtest调用了weight函数
###输入：judgeMatrix
###输出：CI, CR
CRtest <- function (judgeMatrix, round=3){
  RI <- c(0, 0, 0.58, 0.9, 1.12, 1.24, 1.32, 1.41, 1.45, 1.49, 1.51) #随机一致性指标
  Wi <- weight(judgeMatrix)  ##计算权重
  n <- length(Wi)
  if(n > 11){
    cat("判断矩阵过大,请少于11个指标 \n")
  }
  if (n > 2) {
    W <- matrix(Wi, ncol = 1) 
    judgeW <- judgeMatrix %*% W 
    JudgeW <- as.vector(judgeW)
    la_max <- sum(JudgeW/Wi)/n
    CI = (la_max - n)/(n - 1)
    CR = CI/RI[n]
    RI = CI/CR
    cat("\n CI=", round(CI, round), "\n")
    cat("\n CR=", round(CR, round), "\n")
    if (CR <= 0.1) {
      cat(" 通过一致性检验 \n")
      cat("\n Wi: ", round(Wi, round), "\n")
    }
    else {
      cat(" 请调整判断矩阵,使CR<0.1 \n")
      Wi = NULL
    }
  }
  else if (n <= 2) {
    return(Wi)
  }
  consequence <- c(round(la_max,round),round(RI,round),round(CI, round), round(CR, round))
  names(consequence) <- c("La_Max", "RI", "CI", "CR")
  consequence
}

## ---------------------------------------------------------
# 一级指标权重计算

a <- c(1, 1/3,1/3,1/4,1/2,3,1, 1,1/2,	2,3, 1,1, 1/2,2,    
  4,2,2, 1,3, 2,1/2,	1/2,1/3,1)
A <- t(matrix(a, ncol=5))

##计算权重
weight(A)

##判断矩阵一致性检验
CRtest(A)

## ---------------------------------------------------------
# 二级指标权重计算

b1 <- c(1,1/2,2,1)
B1 <- t(matrix(b1, ncol=2))

b2 <- c(1,2,1,1/2,1,1/2,1,2,1)
B2 <- t(matrix(b2, ncol=3))

b3 <- c(1,2,2,1/2,1,2,1/2,1/2,1)
B3 <- t(matrix(b3, ncol=3))

b4 <- c(1,1,1,1)
B4 <- t(matrix(b4, ncol=2))

b5 <- c(1,1/2,2,1)
B5 <- t(matrix(b5, ncol=2))

##计算权重
weight(B1)
weight(B2)
weight(B3)
weight(B4)
weight(B5)

##判断矩阵一致性检验
CRtest(B1)
CRtest(B2)
CRtest(B3)
CRtest(B4)
CRtest(B5)

## ---------------------------------------------------------
# 三级指标权重计算

c2 <- c(1,1/2,1/3,2,3,2,1,1/2,2,2,3,2,1,2,3,1/2,1/2,1/2,1,2,1/3,1/2,1/3,1/2,1)
C2 <- t(matrix(c2, ncol=5))

c4 <- c(1,1,2,3,1,1,2,3,1/2,1/2,1,2,1/3,1/3,1/2,1)
C4 <- t(matrix(c4, ncol=4))

c5 <- c(1,1/2,2,1)
C5 <- t(matrix(c5, ncol=2))

c6 <- c(1,1,1,1)
C6 <- t(matrix(c6, ncol=2))

c7 <- c(1,1,1,1)
C7 <- t(matrix(c7, ncol=2))

c10 <- c(1,2,3,1/2,1,2,1/3,1/2,1)
C10 <- t(matrix(c10, ncol=3))

c12 <- c(1,2,1/2,1)
C12 <- t(matrix(c12, ncol=2))

##计算权重
weight(C2)
weight(C4)
weight(C5)
weight(C6)
weight(C7)
weight(C10)
weight(C12)

##判断矩阵一致性检验
CRtest(C2)
CRtest(C4)
CRtest(C5)
CRtest(C6)
CRtest(C7)
CRtest(C10)
CRtest(C12)















