df <- read.csv('C:\\Users\\SDK\\Desktop\\xinyan_model.csv')
nrow(df)
for(i in 4:40){
    df[which(df[,i] == -99999976),] = ''
}
df_1 <- na.omit(df)
nrow(df_1)
write.csv(df_1,'C:\\Users\\SDK\\Desktop\\xinyan_model_1.csv')



df[which(df[,6] == -99999976),1]
fix(df)
fix(df_1)
