install.packages("pwr")
library(pwr)
pwr.t.test(d= 0.8, sig.level = 0.05, power= 0.9, type = "two.sample",
           alternative = "two.sided")
pwr.t.test(n=20, d=0.5, sig.level = 0.01, type = "two.sample",
           alternative = "two.sided")
pwr.t2n.test(n1=10,n2=10,d=0.5, sig.level = 0.01,
           alternative = "two.sided")
pwr.anova.test(k=5, f=0.25, sig.level = 0.05, power=0.8)
pwr.r.test(r=.25,sig.level = .05, power = .90, alternative = "greater")
ceiling(0.4)
round(0.4)
pwr.f2.test(u=3, f2=0.0769, sig.level = 0.05, power=0.9)
pwr.2p.test(h=ES.h(.65, .6),sig.level = .05,power=.9,alternative = "greater")
pwr.chisq.test(.1853, df=2,sig.level = .05,power = 0.9)

es <- seq(.1,.5,.01)
nes <- length(es)
samsize <- NULL
for (i in 1:nes) {
  result <- pwr.anova.test(k=5, f=es[i] ,sig.level = .05,power = .9)
  samsize[i]<- ceiling(result$n)
}
plot(samsize,es,type="l",lwd=2,col=2,ylab="Effect",
     xlab="Sample Size (per cell)",
     main="one way ANOVA with Power=o.9 and Alpha=0.05")


r <- seq(.1,.5,.01)
nr <- length(r)
p <- seq(.4,.9,.1)
np <- length(p)

samsize1 <- array(numeric(nr*np), dim = c(nr,np))

for (i in 1:np) {
  for (j in 1:nr) {
    result1 <- pwr.r.test(n=NULL,r=r[j],
                          sig.level = .05,
                          power = p[i],
                          alternative = "two.sided")
                samsize1[j,i] <- ceiling(result1$n)
  }
  
}
samsize1

xrange <- range(r)
yrange <- round(range(samsize1))
xrange
yrange

colors <- rainbow(length(p))
plot(xrange,yrange, type = "n", 
     xlab = "correlaion coefficient (r)",
     ylab = "sample size (n)")

for (i in 1:np) {
  lines(r,samsize1[,i], type = "l", lwd=2,col=colors[i])
}

abline(v=0,h=seq(0, yrange[2],50),lty=2, col="gray89")
abline(h=0,v=seq(xrange[1],xrange[2],.02),lty=2,col="gray89")
title("sample size estimation for corelation studies\n sig=0.05 (two side)")
legend("topright", title="power",as.character(p),fill = colors)






















































































