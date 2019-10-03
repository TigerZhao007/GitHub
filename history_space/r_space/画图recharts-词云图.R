# 基础图形Basic Plots 21 - 词云WordCloud
# 首先，加载recharts:
library(recharts)
# 1 介绍Introduction
# 词云只有一种类型: wordCloud
# 关键是:
# 文本型x，词列表
# 数值型y，词汇的频数
# series与图例无关联，而与颜色关联

# 2 用法Function Call
# echartr(data=数据框, x=（文本型自变量，其他类型会被转为因子。如提供多个变量，只传入第一个。）,
#         y=c(数值型应变量。如提供多个变量，只传入第一个。), 
#         series=数据系列变量,<t>=时间轴变量, <type>=wordCloud)
# 3 举例Showcase
# 3.1 数据准备Data Preparation
# 从百度热词榜获取热词，并解析为数据框，包含热词和频数。
# 为此构建一个函数getBaiduHot，解析_百度热词趋势_ 网页。
getBaiduHot <- function(url, top=30, HTMLencoding=NULL){
  baiduhot <- paste0(readLines(url), collapse="")
  charset <- gsub('^.+charset=([[:alnum:]-]+?)[^[:alnum:]-].+$', "\\1", 
                  baiduhot)
  if (is.null(HTMLencoding)) if (!is.null(charset)) HTMLencoding <- charset
  baiduhot <- stringr::str_conv(baiduhot, HTMLencoding)
  hotword <- gsub(".+?<a class=\"list-title\"[^>]+?>([^<>]+?)</a>.+?<span class=\"icon-(rise|fair|fall)\">(\\d+?)</span>.+?","\\1\t\\3\t\\2\t", baiduhot)
  hotword <- enc2native(gsub("^(.+?)\t{4,}.+$","\\1", hotword))
  hotword <- t(matrix(unlist(strsplit(hotword,"\t")), nrow=3))
  hotword <- as.data.frame(hotword, stringsAsFactors=FALSE)
  names(hotword) <- c("Keyword", "Freq", "Trend")
  hotword$Freq <- as.numeric(hotword$Freq)
  hotword <- hotword[order(hotword$Freq, decreasing=TRUE),]
  return(hotword[1:top,])
}
hotword <- getBaiduHot("http://top.baidu.com/buzz?b=1", HTMLencoding='GBK')
knitr::kable(hotword)

# 3.2 基本图形Basic Plot
# 只要提供x和y。
echartr(hotword, Keyword, Freq, type='wordCloud') %>% 
  setTitle('Baidu Hot Word Top30 (realtime)', as.character(Sys.time()))

# 3.3 按数据系列着色Color by Series
# 我们希望将热词分组。定义一个series变量’Trend’。’rise’系列和’fall’系列用不同的颜色标注。
echartr(hotword, Keyword, Freq, Trend, type='wordCloud') %>% 
  setTitle('Baidu Hot Word Top30 (realtime)', as.character(Sys.time()))

# 3.4 带时间轴With Timeline
# 比较实时、今日和七日热词趋势。
# 首先，获取今日和七日两个榜单的网页并转为数据框，合并。
hotword$t <- 'Realtime'
hotword1 <- getBaiduHot("http://top.baidu.com/buzz?b=341&fr=topbuzz_b1", 
                        HTMLencoding = 'GBK')
hotword1$t <- 'Today'
hotword2 <- getBaiduHot("http://top.baidu.com/buzz?b=42&c=513&fr=topbuzz_b341",
                        HTMLencoding = 'GBK')
hotword2$t <- '7-days'
hotword <- do.call('rbind', list(hotword, hotword1, hotword2))
hotword$t <- factor(hotword$t, levels=c('Realtime', 'Today', '7-days'))
# 然后作图。
g <- echartr(hotword, Keyword, Freq, t=t, type='wordCloud') %>% 
  setTitle('Baidu Hot Word Top30')
g

# 4 其他设定Futher Setup
# 接下来可以配置控件、添加标注点/标注线，以及美化成图。
# 4.1 设置主题setTheme
g %>% setTheme('dark', palette='manyeyes')



















