# smiley data clustering project
# Evan Cummings
# CSCI 548 - Pattern Recognition
# Douglas Raiford, Fall 2015

library(mlbench)

# read in the data :
f = mlbench.smiley()

# store the 'classes' :
c = f$classes

# store the 'data' :
x = f$x

# store indexes of classes :
c1 = which(c == 1)
c2 = which(c == 2)
c3 = which(c == 3)
c4 = which(c == 4)

# color vector :
cols  = c('red', 'blue', 'orange', 'black')
cc    = as.vector(c)
cc[c1] = cols[1]
cc[c2] = cols[2]
cc[c3] = cols[3]
cc[c4] = cols[4]

# plot them colored by class :
pdf(file = '../doc/images/actual_smiley.pdf', width=4, height=4)
par(mar=c(2.5,2.5,.1,.1),mgp = c(1.5, .5, 0), mfrow=c(1,1))

plot(x, col=cc, bg=cc, type='p', pch=21,
     xlab='x', ylab='y', main='')
legend("top", "a.)", bty="n") 
grid()

dev.off()


#===============================================================================
# k-means clustering :
km = kmeans(x, 4)

ck = km$cluster

# store indexes of classes :
c1 = which(ck == 1)
c2 = which(ck == 2)
c3 = which(ck == 3)
c4 = which(ck == 4)

# color vector :
cols  = c('red', 'blue', 'orange', 'black')
cc    = as.vector(ck)
cc[c1] = cols[1]
cc[c2] = cols[2]
cc[c3] = cols[3]
cc[c4] = cols[4]

# plot them colored by class :
pdf(file = '../doc/images/kmeans_smiley.pdf', width=4, height=4)
par(mar=c(2.5,2.5,.1,.1),mgp = c(1.5, .5, 0), mfrow=c(1,1))

plot(x, col=cc, bg=cc, type='p', pch=21,
     xlab='x', ylab='y', main='')
legend("top", "b.)", bty="n") 
grid()

dev.off()

#===============================================================================
# k-means clustering :
km = kmeans(x, 5)

ck = km$cluster

# store indexes of classes :
c1 = which(ck == 1)
c2 = which(ck == 2)
c3 = which(ck == 3)
c4 = which(ck == 4)
c5 = which(ck == 5)

# color vector :
cols  = c('red', 'blue', 'orange', 'black', 'green')
cc    = as.vector(ck)
cc[c1] = cols[1]
cc[c2] = cols[2]
cc[c3] = cols[3]
cc[c4] = cols[4]
cc[c5] = cols[5]

# plot them colored by class :
pdf(file = '../doc/images/kmeans_5_smiley.pdf', width=4, height=4)
par(mar=c(2.5,2.5,.1,.1),mgp = c(1.5, .5, 0), mfrow=c(1,1))

plot(x, col=cc, bg=cc, type='p', pch=21,
     xlab='x', ylab='y', main='')
legend("top", "c.)", bty="n") 
grid()

dev.off()


#===============================================================================
# hierarchical clustering :
hm = hclust(dist(x))
ch = cutree(hm, k=4)

# store indexes of classes :
c1 = which(ch == 1)
c2 = which(ch == 2)
c3 = which(ch == 3)
c4 = which(ch == 4)

# color vector :
cols  = c('red', 'blue', 'orange', 'black')
cc    = as.vector(ck)
cc[c1] = cols[1]
cc[c2] = cols[2]
cc[c3] = cols[3]
cc[c4] = cols[4]

# plot them colored by class :
pdf(file = '../doc/images/hierClust_smiley.pdf', width=4, height=4)
par(mar=c(2.5,2.5,.1,.1),mgp = c(1.5, .5, 0), mfrow=c(1,1))

plot(x, col=cc, bg=cc, type='p', pch=21,
     xlab='x', ylab='y', main='')
legend("top", "b.)", bty="n") 
grid()

dev.off()


#===============================================================================
# hierarchical clustering :
hm = hclust(dist(x), method='ward')
ch = cutree(hm, k=4)

# store indexes of classes :
c1 = which(ch == 1)
c2 = which(ch == 2)
c3 = which(ch == 3)
c4 = which(ch == 4)

# color vector :
cols  = c('red', 'blue', 'orange', 'black')
cc    = as.vector(ck)
cc[c1] = cols[1]
cc[c2] = cols[2]
cc[c3] = cols[3]
cc[c4] = cols[4]

# plot them colored by class :
pdf(file = '../doc/images/hierClust_ward_smiley.pdf', width=4, height=4)
par(mar=c(2.5,2.5,.1,.1),mgp = c(1.5, .5, 0), mfrow=c(1,1))

plot(x, col=cc, bg=cc, type='p', pch=21,
     xlab='x', ylab='y', main='')
legend("top", "c.)", bty="n") 
grid()

dev.off()





