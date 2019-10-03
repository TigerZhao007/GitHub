
dat <- read.csv('C:/Users/Think/Desktop/house.csv')
dat$house_name <- as.character(dat$house_name)
dat$house_flood <- as.character(dat$house_flood)
a <- dat$house_name[1]
house.name <- strsplit(dat$house_name,'\\|')
#house.flood <- strsplit(dat$house_flood[1],'\\(')

dat$name <- house.name[[n]][1] 
for (n in 1:length(house.name)) {
  dat[n,6] <- house.name[[n]][1]
  dat[n,7] <- house.name[[n]][2]
  dat[n,8] <- house.name[[n]][3]
  dat[n,9] <- house.name[[n]][4]
  dat[n,10] <- house.name[[n]][5]
  dat[n,11] <- house.name[[n]][6]
}








