pros.df = read.table("pros.txt")
dim(pros.df)
head(pros.df)
par(mfrow=c(3,3), mar=c(4,4,2,0.5)) # Setup grid, margins
for (j in 1:ncol(pros.df)) {
  hist(pros.df[,j], xlab=colnames(pros.df)[j],
       main=paste("Histogram of", colnames(pros.df)[j]),
       col="lightblue", breaks=20)
}

pros.cor1 = cor(pros.df)
pros.cor = cor(pros.df)
round(pros.cor,3) 
pros.cor[lower.tri(pros.cor,diag=TRUE)] = 0 # Why only upper tri part?
pros.cor.sorted = sort(abs(pros.cor),decreasing=T)
pros.cor.sorted[1]
vars.big.cor = arrayInd(which(abs(pros.cor)==pros.cor.sorted[1]), 
                        dim(pros.cor)) # Note: arrayInd() is useful
colnames(pros.df)[vars.big.cor] 
arrayInd(70,.dim = c(9,9))
pairs( ~ lpsa + lcavol + lweight + lcp, data=pros.df)
pros.df.subset = pros.df[pros.df$lcp > min(pros.df$lcp),]
nrow(pros.df.subset) # Beware, we've lost a half of our data! 
pairs(~ lpsa + lcavol + lweight + lcp, data=pros.df.subset)
cor(pros.df.subset[,c("lpsa","lcavol","lweight","lcp")])



