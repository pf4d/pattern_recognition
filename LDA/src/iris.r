# iris data LDA project
# Evan Cummings
# CSCI 548 - Pattern Recognition
# Douglas Raiford, Fall 2015

library(MASS)

# store the iris 'classes' :
c = iris[,5]

# store the iris 'data' :
d = iris[,seq(1,4)]
m = as.matrix(d)

# get training indicies :
t = sample(1:150, 125)

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
xlda = m %*% zlda$scaling[,1]

# set the 2nd linear discriminant :
ylda = m %*% zlda$scaling[,2]

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
png('../doc/images/iris.png', res=200, width=9, 
    height=3, units='in')
par(mar=c(2.5,2.5,.1,.1),mgp = c(1.5, .5, 0), mfrow=c(1,3))

plot(xlda, ylda, col=cc, bg=cc, type='p', pch=21,
     xlab='First Linear Discriminant',
     ylab='Second Linear Discriminant', main='')
legend("topleft", "a.)", bty="n") 
grid()
#legend('topright', levels(c),
#       col   = c('red', 'green', 'blue'), 
#       pt.bg = c('red', 'green', 'blue'), pch = 21)

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



