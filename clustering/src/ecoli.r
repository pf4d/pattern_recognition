# E. coli data sequential clustering project
# Evan Cummings
# CSCI 548 - Pattern Recognition
# Douglas Raiford, Fall 2015

library(gplots)
source("functs.r")

# read in the data :
f = read.csv("../../data/ecoliDiffExpReduced.csv", sep=",")

# store data :
d = as.matrix(f[,seq(3,6)])

# run hierarchical clustering on the data with three clusters :
hm = hclust(dist(d))
ch = cutree(hm, k=3)

# store indexes of classes :
c1 = which(ch == 1)
c2 = which(ch == 2)
c3 = which(ch == 3)

# color vector :
cols  = c('red', 'orange', 'black')
cc    = as.vector(ch)
cc[c1] = cols[1]
cc[c2] = cols[2]
cc[c3] = cols[3]

# dimension reduction to plot in 2D :
zpca = prcomp(d)

# plot the domain vs range and optimal clusters :
pdf('../doc/images/ecoli_pca.pdf', width=4, height=4)
par(mar=c(2.5,2.5,.1,.1),mgp = c(1.5, .5, 0), mfrow=c(1,1))

plot(zpca$x[,1], zpca$x[,2], col=cc, bg=cc, type='p', pch=21,
     xlab='First Principal Component',
     ylab='Second Principal Component', main='')
grid()

dev.off()

# plot the heatmap :
pdf('../doc/images/ecoli_heat.pdf', width=8, height=8)
par(mar=c(2.5,2.5,.1,.1),mgp = c(1.5, .5, 0), mfrow=c(1,1))

lmat = rbind(c(3,4),c(2,1))
lwid = c(1.5,4.0)
lhei = c(1.2,4.1)

heatmap.2(d, Colv = NA, col = redgreen(75), labRow = NA,
          lmat = lmat, lwid = lwid, lhei=lhei)

dev.off()

# plot lines for each cluster :
pdf('../doc/images/ecoli_lines.pdf', width=9, height=3)
par(mar=c(2.5,2.5,.1,.1),mgp = c(1.5, .5, 0), mfrow=c(1,3))

ylim = c(min(d), max(d))

matplot(t(d[c1,]), col=cols[1], bg=cols[1], type='l', lty=1, pch=21,
        ylim=ylim, xlab='time', ylab='expression level', main='')
grid()

matplot(t(d[c2,]), col=cols[2], bg=cols[2], type='l', lty=1, pch=21,
        ylim=ylim, xlab='time', ylab='', main='')
grid()

matplot(t(d[c3,]), col=cols[3], bg=cols[3], type='l', lty=1, pch=21,
        ylim=ylim, xlab='time', ylab='', main='')
grid()

dev.off()



