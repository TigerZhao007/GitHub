library(waveslim)
N <- 1024; k <- 6
x <- ((1:N)-N/2)*2*pi*k/N
y <- ifelse(x>0, sin(x),sin(3*x))
signal <- y + rnorm(N)/10
d <- dwt(signal, n.levels = 4)
data.frame(d$d1, d$d2, d$d3, d$d4)
