#  调用有道词典词库。
ciba<-function(x){
  link=url(paste('http://dict.youdao.com/m/search?keyfrom=dict.mindex&vendor=&q=',
                 iconv(x,to='UTF-8')),encoding='UTF-8')
  readLines(link)->a
  gsub('(<[^<>]*>)|(^ )|(\t)','',a)->a;gsub(' {2,}','',a)->a
  head(a,-11)->a;tail(a,-35)->a;a[a!='']->a
  paste(a,collapse='\n')->a
  gsub('(\n *){2,}','\n',a)->a;gsub(' *\n *','\n',a)->a
  library(stringr)
  print(str_split(a,pattern='\n'))
  cat(a)
}
ciba("  array ")
