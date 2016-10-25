sandbox <- 1:5
names(sandbox) <- c('a','b','c','d','e')
barplot(sandbox)
land<-matrix(1, 8, 8)
land[4,4]<-0
persp(land, expand =.25)
print(land)
plot(sandbox)
barplot(sandbox)
abline(h=mean(sandbox))
deviation<-sd(sandbox)
abline(h=mean(sandbox)-deviation)
abline(h=mean(sandbox)+deviation)
