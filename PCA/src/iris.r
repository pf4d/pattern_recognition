# iris data PCA project
# Evan Cummings
# CSCI 548 - Pattern Recognition
# Douglas Raiford, Fall 2015


# store the iris 'classes' :
c = iris[,5]

# store the iris 'data' :
d = iris[,seq(1,4)]

# perform PCA on d :
p = prcomp(d)

# set the 1st principle component :
x = p$x[,1]

# set the 2nd principle component :
y = p$x[,2]

# plot them :
png('../doc/images/pca_plot.png')
plot(x,y)
dev.off()

# plot them in red :
png('../doc/images/pca_plot_red.png')
plot(x,y, col='red', bg='red', type='p', pch=21)
dev.off()

# store indexes of classes :
s  = which(c == 'setosa')
vc = which(c == 'versicolor')
vg = which(c == 'virginica')

# color vector :
cc     = as.vector(c)
cc[s]  = 'red'
cc[vc] = 'blue'
cc[vg] = 'green'

# plot them colored by class :
png('../doc/images/pca_plot_class.png')
X11(width=4, height=4)
par(mar=c(2.5,2.5,2.5,.1),mgp = c(1.5, .5, 0))
plot(x,y, col=cc, bg=cc, type='p', pch=21, xlab='First Principal Component',
     ylab='Second Principal Component', main='Iris Data')
legend('topright', levels(c),
       col   = c('red', 'green', 'blue'),
       pt.bg = c('red', 'green', 'blue'), pch = 21)
dev.off()

# do a barplot of the proportions of variance :
sig  = p$sdev**2
pvar =  sig / sum(sig)
png('../doc/images/pca_pvar_barplot.png')
barplot(pvar, names.arg=c('PC1','PC2','PC3','PC4'),
        main='Proportions of Variance')
dev.off()




