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
  RI <- c(0, 0, 0.58, 0.9, 1.12, 1.24, 1.32, 1.41, 1.45, 1.49, 1.51,1.54,1.56,1.58,1.59,
          1.59,1.61,1.61,1.62,1.63,1.64,1.64,1.65,1.65,1.66,1.66,1.67,1.67,1.67,1.67,
          1.68,1.68,1.68,1.69,1.69,1.69,1.70,1.70,1.70,1.70) #随机一致性指标
  Wi <- weight(judgeMatrix)  ##计算权重
  n <- length(Wi)
  if(n > 40){
    cat("判断矩阵过大,请少于11个指标 \n")
  }
  if (n > 2) {
    W <- matrix(Wi, ncol = 1) 
    judgeW <- judgeMatrix %*% W 
    JudgeW <- as.vector(judgeW)
    la_max <- sum(JudgeW/Wi)/n
    CI = (la_max - n)/(n - 1)
    CR = CI/RI[n]
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
  consequence <- c(round(CI, round), round(CR, round))
  names(consequence) <- c("CI", "CR")
  consequence
}

# 案例实现
A1_6 <- c(1.00	,	2.00	,	0.25	,	0.33	,	0.50	,	3.00	,
          0.50	,	1.00	,	0.20	,	0.25	,	0.33	,	2.00	,
          4.00	,	5.00	,	1.00	,	2.00	,	3.00	,	6.00	,
          3.00	,	4.00	,	0.50	,	1.00	,	2.00	,	5.00	,
          2.00	,	3.00	,	0.33	,	0.50	,	1.00	,	4.00	,
          0.33	,	0.50	,	0.17	,	0.20	,	0.25	,	1.00)
judgeMatix_a16 <- t(matrix(A1_6, ncol=6))

##计算权重
weight(judgeMatix_a16)
##判断矩阵一致性检验
CRtest(judgeMatix_a16)


B1_2 <- c(1.00, 	0.50,  2.00, 	1.00 )
judgeMatix_b12 <- matrix(B1_2, ncol=2)
##计算权重
weight(judgeMatix_b12)
##判断矩阵一致性检验
CRtest(judgeMatix_b12)


B3_5 <- c(1.00, 	0.50 ,	0.33 ,
          2.00, 	1.00 	,1.00 ,
          3.00 ,	1.00 	,1.00 
)
judgeMatix_b12 <- matrix(B3_5, ncol=3)
##计算权重
weight(judgeMatix_b12)
##判断矩阵一致性检验
CRtest(judgeMatix_b12)

B6_8 <- c(1.00, 	0.33 	,1.00 ,
          3.00 ,	1.00 ,	3.00 ,
          1.00 ,	0.33 ,	1.00 )
judgeMatix_b12 <- matrix(B6_8, ncol=3)
##计算权重
weight(judgeMatix_b12)
##判断矩阵一致性检验
CRtest(judgeMatix_b12)

B9_13 <- c(1.00 ,	0.33 ,	0.33 ,	0.25, 	0.50 ,
           3.00 ,	1.00 ,	1.00 ,	0.50 ,	2.00 ,
           3.00 ,	1.00 ,	1.00 ,	0.50 ,	2.00 ,
           4.00 ,	2.00 ,	2.00 ,	1.00 ,	3.00 ,
           2.00 ,	0.50 ,	0.50 ,	0.33 ,	1.00 
           )
judgeMatix_b12 <- matrix(B9_13, ncol=5)
##计算权重
weight(judgeMatix_b12)
##判断矩阵一致性检验
CRtest(judgeMatix_b12)

B14_17 <- c(1.00, 	0.50 	,0.25 ,	0.33 ,
            2.00, 	1.00 ,	0.33 ,	0.50 ,
            4.00, 	3.00 ,	1.00 ,	0.50 ,
            3.00 ,	2.00 ,	2.00 ,	1.00 
            )
judgeMatix_b12 <- matrix(B14_17, ncol=4)
##计算权重
weight(judgeMatix_b12)
##判断矩阵一致性检验
CRtest(judgeMatix_b12)

B18_21 <- c(1.00 ,	0.50 ,	0.33 ,	0.25 ,
            2.00 ,	1.00 ,	0.50 	,0.33 ,
            3.00 	,2.00 ,	1.00 ,	0.50 ,
            4.00 ,	3.00 ,	2.00 ,	1.00 
            )
judgeMatix_b12 <- matrix(B18_21, ncol=4)
##计算权重
weight(judgeMatix_b12)
##判断矩阵一致性检验
CRtest(judgeMatix_b12)

C1_2 <- c(1.00 ,	1.00 ,  1.00 ,	1.00 )
judgeMatix_b12 <- matrix(C1_2, ncol=2)
weight(judgeMatix_b12)
##判断矩阵一致性检验
CRtest(judgeMatix_b12)


C3_9 <- c(1.00, 	0.33, 	0.25, 	0.50, 	2.00, 	3.00, 	0.20, 
          3.00, 	1.00, 	0.50, 	2.00, 	4.00, 	5.00, 	0.33 ,
          4.00, 	2.00, 	1.00, 	3.00, 	5.00, 	6.00, 	0.50 ,
          2.00, 	0.50, 	0.33, 	1.00, 	3.00, 	4.00, 	0.25 ,
          0.50, 	0.25, 	0.20, 	0.33, 	1.00, 	2.00, 	0.17 ,
          0.33, 	0.20, 	0.17, 	0.25, 	0.50, 	1.00, 	0.14 ,
          5.00, 	3.00, 	2.00, 	4.00, 	6.00, 	7.00, 	1.00 
)
judgeMatix_b12 <- matrix(C3_9, ncol=7)
weight(judgeMatix_b12)
##判断矩阵一致性检验
CRtest(judgeMatix_b12)

C14_18 <- c(1.00 ,	0.50 ,	0.33 ,	0.25, 	0.20, 
            2.00 ,	1.00 ,	0.50 ,	0.33 ,	0.25,
            3.00 ,	2.00 ,	1.00 	,0.50 ,	0.33 ,
            4.00 ,	3.00 ,	2.00 ,	1.00 ,	0.50 ,
            5.00 ,	4.00 ,	3.00 ,	2.00 	,1.00 
)
judgeMatix_b12 <- matrix(C14_18, ncol=5)
weight(judgeMatix_b12)
##判断矩阵一致性检验
CRtest(judgeMatix_b12)

C19_20 <- c(1.00 ,	0.50 ,	0.50 ,
            2.00 ,	1.00 ,	1.00, 
            2.00 ,	1.00 ,	1.00 
)
judgeMatix_b12 <- matrix(C19_20, ncol=3)
weight(judgeMatix_b12)
##判断矩阵一致性检验
CRtest(judgeMatix_b12)


