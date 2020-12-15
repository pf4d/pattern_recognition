# tumor data MDS project
# Evan Cummings
# CSCI 548 - Pattern Recognition
# Douglas Raiford, Fall 2015

# read in the data :
f = read.csv("../../data/breast-cancer-wisconsin.data", header=FALSE)

# get the sample names :
e = f[,1]

# get the classes :
c = f[,11]

# get just the data :
d = f[,seq(2,10)]

# perform MDS on d :
p = cmdscale(dist(d))

# color sample black for benign (b) and red for malignant (m) :
cols  = c('black', 'red')
cc    = as.vector(e)
b     = which(c == 2)
m     = which(c == 4)
cc[b] = cols[1]
cc[m] = cols[2]

# plot them colored by experiment :
png('../doc/images/mds_plot_tumor.png', res=200, width=6,
    height=6, units='in')
par(mar=c(2.5,2.5,2.5,.1),mgp = c(1.5, .5, 0))
plot(p, col=cc, bg=cc, type='p', pch=21, cex=1,
     xlab='First Principal Coordinate',
     ylab='Second Principal Coordinate', main='Tumor Data Using MDS')
legend('topleft', c('benign', 'malignant'), col = cols, pt.bg = cols, pch = 21)
dev.off()



