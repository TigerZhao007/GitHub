residplot <- function(fit, nbreaks=10){
  z <- rstudent(fit)
  hist(z, breaks = nbreaks, freq = FALSE, 
       xlab = "studentized residual",
       main = "distribution of errors")
  rug(jitter(z), col = "brown")
  curve(dnorm(x,mean = mean(z),sd=sd(z)),
        add = TRUE,col="blue", lwd=2)
  lines(density(z)$x,density(z)$y,
        col="red", lwd=2, lty=2)
  legend("topright",
         legend = c("Nromal curve","kernel Density Curve"),
         lty = 1:2,col = c("blue","red"),cex=0.7)
}