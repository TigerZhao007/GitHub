dat_lib()

setwd('F:/工作文件/2宜开工作/6_电力项目')

worksentity = fread('WORKSENTITY.csv')
applyentity = fread('APPLYENTITY2.csv')

work_in = worksentity[worksentity$ID %in% applyentity$WORKS_ID,]
work_out = worksentity[-which(worksentity$ID %in% applyentity$WORKS_ID),]

work_join = worksentity %>% left_join(.,applyentity,by = c('ID'='WORKS_ID'))

work_join = left_join(worksentity,applyentity,by = c('ID'='WORKS_ID'))

which(worksentity$ID %in% applyentity$WORKS_ID) %>% length

table(applyentity[,'REGISTERAT']=='')

