#单变量函数统计量计算

data_outline <- function(x){
  n   <- length(x)
  m   <- mean(x)
  s   <- sd(x)
  v   <- var(x)
  me  <- median(x)
  cv  <- 100*s/m
  css <- sum((x-m)^2)
  uss <- sum(x^2)
  ma  <- max(x)
  mi  <- min(x)
  d   <- max(x)-min(x)
  d1  <- quantile(x,3/4)-quantile(x,1/4)
  sm  <- s/sqrt(n)
  g1  <- n/((n-1)*(n-2))*sum((x-m)^3)/s^3
  g2  <- n*(n+1)/((n-1)*(n-2)*(n-3))*sum((x-m)^4)/s^4-3*(n-1)^2/((n-2)*(n-3))
  data.frame(N=n, Mean=m, Var=v, Std.dev=s, Median=me, Std.mean=sm, CV=cv,
             CSS=uss, D=d, D1=d1, Skewess=g1, Kurtosis=g2, row.names = 1)
  }            #单变量统计量计算程序