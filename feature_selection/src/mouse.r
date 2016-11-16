# mouse data feature-selection project
# Evan Cummings
# CSCI 548 - Pattern Recognition
# Douglas Raiford, Fall 2015

source("functs.r")

library(MASS)

# read in the data :
f = read.csv("../../data/otu_table_L6.txt", sep="\t", row.names=1)

# get the experiment names :
e = colnames(f)

# get the genera names :
g = rownames(f)

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
d1 = t(f)
m1 = as.matrix(d1)

v  = getTscores(m1,c)

# get reduced-dimension data :
d2 = d1[,nmax(v,n=5)]
m2 = as.matrix(d2)

# remove and "Other" generas :
fn = f[-grep("Other", rownames(f)),]
m3 = as.matrix(fn)

# get indicies of any constant rows :
r = removeConstantRows(m3, c)
m3 = t(m3[-r,])

# do this other stuff :
v12 = seq_forward(m3,c,12)
v13 = seq_forward(m3,c,13)
v14 = seq_forward(m3,c,14)
v15 = seq_forward(m3,c,15)
n12 = nway_cross_validate_lda(m3[,v12], c)
n13 = nway_cross_validate_lda(m3[,v13], c)
n14 = nway_cross_validate_lda(m3[,v14], c)
n15 = nway_cross_validate_lda(m3[,v15], c)

# print the results of that stuff :
cat("n12 =", n12, "\n")
cat("n13 =", n13, "\n")
cat("n14 =", n14, "\n")
cat("n15 =", n15, "\n")

# plot them colored by class :
pdf(file = '../doc/images/mouse_ttest.pdf', width=6, height=3)
par(mar=c(2.5,2.5,1.0,0.1), mgp=c(1.5, .5, 0), mfrow=c(1,1))

barplot(v,
        ylab='Relative t-statistic',
        xlab='Dimension',
        main='',
        names.arg=1:dim(d1)[2])
grid()
dev.off()

zlda2    = lda(d2, c)
p2       = predict(zlda2, d2)
correct2 = length(which(p2$class == c))
prop2    = correct2 / length(c)
cat("accuracy2 =", prop2*100, "%\n")

# perform nway-cross validation :
n2 = nway_cross_validate_lda(m2,c)
cat("accuracy of t-test nway =", n2, "\n")

# set the 1st linear discriminant :
#xlda1 = m1 %*% zlda1$scaling[,1]
xlda2 = m2 %*% zlda2$scaling[,1]

# set the 2nd linear discriminant :
#ylda1 = m1 %*% zlda1$scaling[,2]
#ylda2 = m2 %*% zlda2$scaling[,2]

# create density to determine range of data :
#dens1   = density(xlda1)
dens2   = density(xlda2)
#xrange1 = range(dens1$x)
xrange2 = range(dens2$x)

# project just the benigns :
#xp1 = m1[P,] %*% zlda1$scaling[,1]
xp2 = m2[P,] %*% zlda2$scaling[,1]
#dp1 = density(xp1)
dp2 = density(xp2)

# project just the malignant :
#xd1 = m1[D,] %*% zlda1$scaling[,1]
xd2 = m2[D,] %*% zlda2$scaling[,1]
#dd1 = density(xd1)
dd2 = density(xd2)

# color vector :
cols  = c('black', 'red')
cc    = as.vector(e)
cc[P] = cols[1]
cc[D] = cols[2]

# plot them colored by experiment :
pdf('../doc/images/mouse.pdf', width=6, height=3)
par(mar=c(2.5,2.5,.1,.1),mgp = c(1.5, .5, 0), mfrow=c(1,1))

#plot(xlda1, ylda1, col=cc, bg=cc, type='p', pch=21,
#     xlab='First Linear Discriminant',
#     ylab='Second Linear Discriminant', main='')
#legend("topleft", "a.)", bty="n") 
#grid()

plot(dp2$x, dp2$y, col=cols[1], type='l', pch=21, xlim=xrange2,
     xlab='First Linear Discriminant',
     ylab='Density', main='')
lines(dd2$x, dd2$y, col=cols[2], pch=21,
     xlab='First Linear Discriminant',
     ylab='Density', main='')
#legend("topright", "a.)", bty="n") 
grid()

#plot(xlda2, ylda2, col=cc, bg=cc, type='p', pch=21,
#     xlab='First Linear Discriminant',
#     ylab='Second Linear Discriminant', main='')
#legend("topleft", "b.)", bty="n") 
#grid()

dev.off()



