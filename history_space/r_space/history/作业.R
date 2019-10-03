#作业
#题1
sigmali <- function(w, t_i, x_i){
  sigmali <- sum(t_i * t(w) %*% x_i < 0)
  data.frame(sigmali=sigmali)
}

#题2
L_sw <- function(w, t_i, x_i, K=1){
  L_sw <- 1/(1 + exp(K * t_i * t(w) %*% x_i))
  data.frame(L_sw=L_sw)
}

#题3
L_deriv <- function(w, t_i, x_i, K=1){
  ktx <- K*t_i*x_i
  ektwx <- exp(K*t_i*t(w)%*%x_i)
  L_deriv <- -ktx*ektwx/(1+ektwx)^2
  data.frame(L_deriv=L_deriv)
}
set.seed(1234)
w <- rnorm(3,mean = 0,sd=1)
set.seed(4321)
y <- rnorm(20,mean = 0,sd=1)
set.seed(2314)
x1 <- rnorm(60)
x  <- array(x1,dim = c(20,3))
w
t_i <- y
x_i <- x



sigmali(w=w,t_i = y,x_i = x)

L_sw(w=1,t_i = 1,x_i = 1)

L_deriv(w=1,t_i = 1,x_i = 1)
