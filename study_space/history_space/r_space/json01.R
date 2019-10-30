library(rjson)

dat = fromJSON(file = 'F:/pythonspace/学习scrapy/lianjia/items_dict.json')
print(dat)
dat_frame = as.data.frame(dat)
dat_frame1 = as.data.frame(dat[[1]])
dat_frame2 = as.data.frame(dat[[2]])
dat[[1]]
#temp = unlist(dat)
