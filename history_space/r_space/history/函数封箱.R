rm(list=ls()) 
setwd("E:\\rspace") 
package.skeleton(name="ks",
                 code_files="ks.R")


library(ks)
install.packages('E:\\rspace\\ks_1.0.tar.gz',repos = NULL, type = 'source')
library('ks_s')
ks
install.packages(ks_s)

