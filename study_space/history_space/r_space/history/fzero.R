f<-function(x) x^3-x-1
fzero(f,1,2,1e-6)
fzero<-function(f,a,b,eps=1e-5){
  if(f(a)*f(b)>0)
    list(fail="finding root is fall")
  else{
    repeat{
      if(abs(b-a)<eps)break
      x<-(a+b)/2
      if(f(a)*f(x)<0) b<-x else a<-x
    }
    list(root=(a+b)/2,fun=f(x))
  }
}                 #   二分法求一元方程的根。
