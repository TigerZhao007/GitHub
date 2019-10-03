t0 <- c(1,-1)
set.seed(1234)
t <- sample(t0,30,replace = T)
t
set.seed(1234)
w <- rnorm(2)
x <- array(rnorm(60),c(2,30))
x
t.w <- sign(t(w)%*%x)
t(w)%*%x
x.1 <- t(w)%*%x*t
sum(t(w)%*%x*t<=0)
k <- 1
L_sw <- 1/(1 + exp(k*t(w) %*% x*t))
L_sw
as.data.frame(x.1,L_sw)
plot(sort(x.1),sort(L_sw),type = "p")
ss <- data.frame(x1=x.1[1,],x2=L_sw[1,])
ss2<- ss[order(ss[,1]),]
ss2
plot(ss2,type="l")


L_deriv <- function(w, t_i, x_i, K=1){
  ktx <- K*t_i*x_i
  ektwx <- exp(K*t_i*t(w)%*%x_i)
  L_deriv <- -ktx*ektwx/(1+ektwx)^2
  data.frame(L_deriv=L_deriv)
}