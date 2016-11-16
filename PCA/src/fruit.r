# fruit data PCA project
# Evan Cummings
# CSCI 548 - Pattern Recognition
# Douglas Raiford, Fall 2015

# read the variable back in :
f = read.csv("../../data/fruit.csv")

# store the fruit 'classes' :
c = f[,5]

# store the fruit 'data' :
d = f[,seq(1,4)]

# perform PCA on d :
p = prcomp(d)

# set the 1st principle component :
x = p$x[,1]

# set the 2nd principle component :
y = p$x[,2]

# set the 3nd principle component :
z = p$x[,3]

# store indexes of classes :
a = which(c == 'apple')
l = which(c == 'lemon')
o = which(c == 'orange')
z = which(c == 'peach')

# color vector :
cols  = c('red', 'yellow', 'orange', 'burlywood1')
cc    = as.vector(c)
cc[a] = cols[1]
cc[l] = cols[2]
cc[o] = cols[3]
cc[z] = cols[4]

# plot them colored by class :
png('../doc/images/pca_plot_fruit.png')
#X11(width=4, height=4)
par(mar=c(2.5,2.5,2.5,.1),mgp = c(1.5, .5, 0))
plot(x,y, col=cc, bg=cc, type='p', pch=21, xlab='First Principal Component',
     ylab='Second Principal Component', main='Fruit Data')
legend('topright', levels(c), col = cols, pt.bg = cols, pch = 21)
dev.off()

# do a barplot of the proportions of variance :
sig  = p$sdev**2
pvar =  sig / sum(sig)
png('../doc/images/pca_pvar_fruit_barplot.png')
barplot(pvar, names.arg=c('PC1','PC2','PC3','PC4'),
        main='Proportions of Variance')
dev.off()

# import the rgl library for 3D stuff:
library(rgl)

plot3d(x,y,z, col=cc, bg=cc, type='p', pch=21,
       xlab='First Principal Component',
       ylab='Second Principal Component',
       zlab='Third Principal Component')

# plot them colored by class :
png('../doc/images/pca_plot_fruit_23.png')
#X11(width=4, height=4)
par(mar=c(2.5,2.5,2.5,.1),mgp = c(1.5, .5, 0))
plot(y,z, col=cc, bg=cc, type='p', pch=21, xlab='Second Principal Component',
     ylab='Third Principal Component', main='Fruit Data')
legend('topright', levels(c), col = cols, pt.bg = cols, pch = 21)
dev.off()




