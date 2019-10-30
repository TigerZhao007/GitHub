# R语言生成保存图片方法
x <- rnorm(100,1,5)


# 第一种png格式
png(file="C:/Users/Think/Desktop/myplot.png", bg='white')
plot(x)
dev.off()

# 第二种jpeg格式
jpeg(file="C:/Users/Think/Desktop/myplot.jpeg")
plot(x)
dev.off()


# 第三种pdf格式
pdf(file="C:/Users/Think/Desktop/myplot.pdf")
plot(x)
dev.off()




