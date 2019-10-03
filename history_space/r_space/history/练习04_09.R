url <- "trump.txt"
get.wordtab <- function(url,
                        split= "[[:space:]]|[[:punct:]]",
                        Tolower=TRUE,
                        plottab= TRUE){
  lines = readLines(url)
  text  = paste(lines, collapse = " ")
  words = strsplit(text, split= "[[:space:]]|[[:punct:]]")
  words = words[words!=""]
  
  if(Tolower==TRUE) words <- tolower(words)
  
  wordtab = table(words)
  
  if(plottab==TRUE) plot(wordtab)
  
  list(wordtab=wordtab,
       length= sum(wordtab),
       unique= length(wordtab))
 
}
save.image("try.Rdata")



trump <- get.wordtab("trump.txt")
class(trump)
head(trump)
trump1 <- as.data.frame(trump)
head(trump)


samp1 <- function(x,y){list(x,y)}
z <-samp1(x=c(1,3),y=2)
z[[1]][2]
z$x
z
samp2 <- function(x,y){list(x=x,y=y)}
z <- samp2(c(1,3),2)
z

options(digits = 2)
pi
print(pi,digits = 20)
pi
rm(pi)
pi
rm(list = ls())
