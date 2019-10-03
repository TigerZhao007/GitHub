imdb <- function(v,m,r,c){
  score <- v/(v+m)*r + m/(v+m)*c
  return(score)
}
imdb(100,1,9,7)
imdb(10,1,9.7,7)



