sj0 <- read.xlsx("tianqi01.xlsx", sheetIndex = "Sheet3")
sj0

##  0-1规范化。  ##
b11 <- (sj0[,1]-min(sj0[,1]))/(max(sj0[,1])-min(sj0[,1]))
b12 <- (sj0[,2]-min(sj0[,2]))/(max(sj0[,2])-min(sj0[,2]))
b11[1]
cbind(b11,b12)
b11  <- (sj0[1]-min(sj0[1]))/(max(sj0[1])-min(sj0[1]))
b12  <- (sj0[2]-min(sj0[2]))/(max(sj0[2])-min(sj0[2]))
b11[[1]]
cbind(b11,b12)
## b <- matrix()

b1 <- list()
n <- ncol(sj0)
for (i in 1:n) {
  b1[[i]]  <- (sj0[i]-min(sj0[i]))/(max(sj0[i])-min(sj0[i]))
  b1.end   <- as.data.frame(b1)
}
b1.end


##  零均值规范化。  ##
b21.mean <- mean(sj0[,1]) 
b21.sd   <- sd(sj0[,1])
b21 <- (sj0[1]-b21.mean)/b21.sd 

b2 <- list()
b2.mean <- matrix()
b2.sd   <- matrix()
n <- ncol(sj0)
for (i in 1:n) {
  b2.mean[i] <- mean(sj0[,i]) 
  b2.sd[i]   <- sd(sj0[,i])
  b2[[i]]  <- (sj0[1]-b21.mean)/b21.sd
  b2.end   <- as.data.frame(b2)
}
b2.end










