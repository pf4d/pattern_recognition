# tumor data LDA project
# Evan Cummings
# CSCI 548 - Pattern Recognition
# Douglas Raiford, Fall 2015

library(MASS)

# read in the data :
f = read.csv("../../data/breast-cancer-wisconsin.data",
             header=FALSE, na.strings='?')

# get the sample names :
e = f[,1]

# get the classes :
c = f[,11]

# get just the data :
d    = f[,seq(2,10)]

# replace the NANs with the column mean :
for(i in 1:ncol(d))
{
  n_na       = which(!is.na(d[,i]))
  d[-n_na,i] = mean(d[n_na,i])
}
M = as.matrix(d)

# get training indicies :
t = sample(1:699, 600)

# perform LDA on d :
zlda = lda(d[t,], c[t])

# perform MDS on d :
zmds = cmdscale(dist(d))

# perform PCA on d :
zpca = prcomp(d)

# predict the test set -train :
p = predict(zlda, d[-t,])

# get the number predicted correctly :
correct = length(which(p$class == c[-t]))

# get the proportion correct :
prop = correct / length(c[-t])

# print the result to the screen :
cat("accuracy =", prop*100, "%\n")

# set the 1st linear discriminant :
xlda = M %*% zlda$scaling[,1]

# create density to determine range of data :
dens   = density(xlda)
xrange = range(dens$x)

# color sample black for benign (b) and red for malignant (m) :
cols  = c('black', 'red')
cc    = as.vector(e)
b     = which(c == 2)
m     = which(c == 4)
cc[b] = cols[1]
cc[m] = cols[2]

# project just the benigns :
xb = M[b,] %*% zlda$scaling[,1]
db = density(xb)

# project just the malignant :
xm = M[m,] %*% zlda$scaling[,1]
dm = density(xm)

# plot them colored by experiment :
png('../doc/images/tumor.png', res=200, width=9,
    height=3, units='in')
par(mar=c(2.5,2.5,.1,.1),mgp = c(1.5, .5, 0), mfrow=c(1,3))

plot(db$x, db$y, col=cols[1], type='l', pch=21, xlim=xrange,
     xlab='First Linear Discriminant',
     ylab='Density', main='')
lines(dm$x, dm$y, col=cols[2], pch=21,
     xlab='First Linear Discriminant',
     ylab='Density', main='')
legend("topleft", "a.)", bty="n")
grid()

plot(zmds, col=cc, bg=cc, type='p', pch=21,
     xlab='First Principal Coordinate',
     ylab='Second Principal Coordinate', main='')
legend("topleft", "b.)", bty="n")
grid()

plot(zpca$x[,1], zpca$x[,2], col=cc, bg=cc, type='p', pch=21,
     xlab='First Principal Component',
     ylab='Second Principal Component', main='')
legend("topleft", "c.)", bty="n")
grid()

dev.off()
