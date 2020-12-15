# mouse data LDA project
# Evan Cummings
# CSCI 548 - Pattern Recognition
# Douglas Raiford, Fall 2015

library(MASS)

# read in the data :
f = read.csv("../../data/otu_table_L6.txt", sep="\t", row.names=1)

# remove and "Other" generas :
fn = f[-grep("Other", rownames(f)),]

# remove any rows with more than 6 zeros :
g = c()
for(i in 1:nrow(fn))
{
  # if too many zeros add to g :
  if (length(which(fn[i,] == 0)) >= 6)
  {
    g = c(g,i)
  }
}
fn = fn[-g,]

# get the experiment names :
e = colnames(fn)

# get the genera names :
g = rownames(fn)

# store indexes of proximal (P) and distal (D) experiments, and mouse types
# B and C :
P = grep("[A-Z]+P[0-9]", e)
D = grep("[A-Z]+D[0-9]", e)
B = grep("^B[A-Z]+[0-9]", e)
C = grep("^C[A-Z]+[0-9]", e)

# create the classes (proximal or distal) :
c    = 1:length(e)
c[P] = 'proximal'
c[D] = 'distal'

# transpose the data so each row is an experiment :
d = t(fn)
m = as.matrix(d)

# get training indicies :
t = sample(1:20, 18)
#t = 1:10

# perform LDA on d :
zlda = lda(d[t,], c[t], tol=0)

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

#===============================================================================
# color vector :
cols  = c('black', 'red')
cc    = as.vector(e)
cc[P] = cols[1]
cc[D] = cols[2]

# plot them colored by experiment :
png('../doc/images/mouse_experiment.png', res=200, width=9,
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

#===============================================================================
# color vector :
cols  = c('purple', 'green')
cc    = as.vector(e)
cc[B] = cols[1]
cc[C] = cols[2]

# plot them colored by class :
png('../doc/images/mouse_class.png', res=200, width=9,
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





