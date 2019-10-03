ls <- rnorm(10000)
ls
v1 <- ceiling(ls)

result <- kmeans(ls, 6)
result
v3 <- result$cluster
v3
plot(ls,v3)
plot(ls,v1)

ls <- sj2$x4
ls
v2.seq <- seq(min(ls), max(ls), (max(ls)-min(ls))/4)
length(ls)
v2.sort <- sort(ls)
v2.new  <- rep(0,length(ls))
for (i in 1:length(ls)) {
    v2.new[i]=
      ifelse(ls[i] <= 21.5, 1,
             ifelse(ls[i] <= 25, 2,
                    ifelse(ls[i] <= 28.5, 3,
                           ifelse(ls[i] <= 32, 4,0))))
  
}
v3 <-v2.new
v2 <- v2.new
v <- data.frame(x1=ls,x2=v2, x3=v3)
v
table(v3)
table(v2)
