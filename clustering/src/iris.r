# iris data sequential clustering project
# Evan Cummings
# CSCI 548 - Pattern Recognition
# Douglas Raiford, Fall 2015

source("functs.r")

# store the iris 'classes' :
c = iris[,5]

# store the iris 'data' :
d = iris[,seq(1,4)]
m = as.matrix(d)

# get min/max of the distance matrix (complicated, right?!) :
D    = dist(m)
U    = upper.tri(D)
DU   = D[!is.na(D[U])]
tmax = max(DU)
tmin = min(DU)

# number of thetas :
k      = 100

# domain of thetas :
thetas = seq(tmin, tmax, length=k)

# range of clusters given thetas :
clusts = rep(NA, k)

# sequential clustering over range of thetas :
for (i in seq(1:k))
{
  v         = sequential_forward(m, theta=thetas[i], kmax=10)
  numClust  = length(unique(v))
  clusts[i] = numClust
}

#===============================================================================
# print the data colored by most likely cluster :
v  = sequential_forward(m, theta=3.5, kmax=10)

# dimension reduction to plot in 2D :
zpca = prcomp(d)

# plot the domain vs range and optimal clusters :
pdf('../doc/images/iris_clusters.pdf', width=9, height=3)
par(mar=c(2.5,2.5,.1,.1),mgp = c(1.5, .5, 0), mfrow=c(1,3))

plot(thetas, clusts, col='black', type='p', pch=21,
     xlab='theta', ylab='number of clusters', main='')
grid()

# store indexes of classes :
v1 = which(v == 1)
v2 = which(v == 2)

# color vector :
cc     = as.vector(v)
cc[v1] = 'red'
cc[v2] = 'black'

plot(zpca$x[,1], zpca$x[,2], col=cc, bg=cc, type='p', pch=21,
     xlab='First Principal Component',
     ylab='Second Principal Component', main='')
grid()

# store indexes of classes :
s  = which(c == 'setosa')
vc = which(c == 'versicolor')
vg = which(c == 'virginica')

# color vector :
cc     = as.vector(c)
col    = c('red', 'green', 'blue')
cc[s]  = col[1]
cc[vc] = col[2]
cc[vg] = col[3]

plot(zpca$x[,1], zpca$x[,2], col=cc, bg=cc, type='p', pch=21,
     xlab='First Principal Component',
     ylab='Second Principal Component', main='')
legend('topright', levels(c), col=col, pt.bg=col, pch=21)
grid()

dev.off()

#===============================================================================
# print the data colored with 3 clusters :
v  = sequential_forward(m, theta=2.5, kmax=10)

# dimension reduction to plot in 2D :
zpca = prcomp(d)

# plot the domain vs range and optimal clusters :
pdf('../doc/images/iris_3_clusters.pdf', width=4, height=4)
par(mar=c(2.5,2.5,.1,.1),mgp = c(1.5, .5, 0), mfrow=c(1,1))

# store indexes of classes :
v1 = which(v == 1)
v2 = which(v == 2)
v3 = which(v == 3)

# color vector :
cc     = as.vector(v)
cc[v1] = 'red'
cc[v2] = 'black'
cc[v3] = 'green'

plot(zpca$x[,1], zpca$x[,2], col=cc, bg=cc, type='p', pch=21,
     xlab='First Principal Component',
     ylab='Second Principal Component', main='')
grid()

dev.off()



