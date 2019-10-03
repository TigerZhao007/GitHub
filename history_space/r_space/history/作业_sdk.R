#  R语言作业
#  0-1二值分类问题。
#  邵登科 12统计A1班 1220160468

# ---------------------------------------
  
#  given data (t.i, x.i), and w.
#（给定数据(t.i, x.i), 和 w.)
# t.i 为-1或1的真值情况。
# x.i为输入数据。
# w为线的权重系数。

# ---------------------------------------

# 1、write a function to evaluate [1].
# 计算错判的个数。

l_wp <- function(t, x, w){
  t.sum <- sum(t * t(w) %*% x<=0)        # 计算错判数目。
  t.p <- t.sum/length(t)                 # 计算错判概率。
  list(t.sum=t.sum,t.p=t.p)
}

# --------------------------------------

# 2、write a function to evaluate l_s(w) where [2] and k=1.
# 写出渐进函数，及图形。

l_we <- function(t,x,w,k=1){
   l_w <- 1/(1 + exp(k*t*t(w) %*% x))[1,]                                    # 计算渐进函数。
   s0 <- t*t(w)%*%x; s1 <- data.frame(twx=s0[1,],Loss=l_w);s2 <- s1[order(s1[,1]),]  
   l_ws  <- sum(s1$Loss)                                                         # 计算l_s(w)值。
   plot(s2,type="l",main = "Smooth 0-1 Loss Approximaton")                      # 画出渐进图形。
   list(l_w=s1$Loss,l_ws=l_ws)
   }

# --------------------------------------

# 3、write a function to calculate the derivatives of l_s(w) with respect to w.
# 写出l_s(w)的导数。

l_wd <- function(w, t, x, k=1){
  s0  <- k*t*x
  s1  <- exp(k*t*t(w)%*%x)
  l_d <- -t(s0%*%t(s1))/((1+s1)%*%t(1+s1))[1,1]        # 计算l_s(w)导数值。
  list(l_d=l_d)
}

# ---------------------------------------

# 生成实验数据。

t.n <- 300;  w.n <- 9;  x.n <- t.n*w.n; t0 <- c(1,-1);
set.seed(1234); t <- sample(t0,t.n,replace = T)
set.seed(1234); w <- matrix(rnorm(w.n), byrow = TRUE)
set.seed(1234); x <- array(rnorm(x.n),c(w.n,t.n))

# ---------------------------------------
# 题1
ss1 <- l_wp(t=t,x=x,w=w)             # 实验案例计算。
ss1$t.sum                            # 计算案例错判数目
ss1$t.p                              # 计算案例错判概率

# 题2
ss2 <-l_we (t=t,x=x,w=x,k=1)       # 实验案例计算。
ss2$l_w                          # 计算案例渐进估计值。
ss2$l_ws                           # 计算案例l_s(w)值

# 题3
ss3 <- l_wd(w=w,t=t[1],x=x[,1:10])           # 实验案例计算。
ss3 <- l_wd(w=w,t=t,x=x)                     # 实验案例计算。
ss3$l_d                                      # 写出l_s(w)的导数

