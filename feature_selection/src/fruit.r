# fruit data feature-selection project
# Evan Cummings
# CSCI 548 - Pattern Recognition
# Douglas Raiford, Fall 2015

source("functs.r")

library(MASS)

# read the variable back in :
f = read.csv("../../data/fruit.csv")

# store the fruit 'classes' :
c = f[,5]

# store the fruit 'data' :
d1 = f[,seq(1,4)]
m1 = as.matrix(d1)

vt = getTscores(m1,c)
vs = seq_forward(m1,c,2)

# get reduced-dimension data :
d2 = f[,nmax(vt,2)]
d3 = f[,vs]
m2 = as.matrix(d2)
m3 = as.matrix(d3)

# plot them colored by class :
pdf(file = '../doc/images/fruit_ttest.pdf', width=6, height=3)
par(mar=c(2.5,2.5,.1,.1),mgp = c(1.5, .5, 0), mfrow=c(1,1))

barplot(vt,
        ylab='Relative t-statistic',
        xlab='Dimension',
        main='',
        names.arg=colnames(d1))
grid()
dev.off()

# get training indicies of 75% of data :
n = dim(m1)[1]
t = sample(1:n, n*0.75)

# perform LDA on d :
zlda1 = lda(d1[t,], c[t])
zlda2 = lda(d2[t,], c[t])
zlda3 = lda(d3[t,], c[t])

# predict the test set -train :
p1 = predict(zlda1, d1[-t,])
p2 = predict(zlda2, d2[-t,])
p3 = predict(zlda3, d3[-t,])

# get the number predicted correctly :
correct1 = length(which(p1$class == c[-t]))
correct2 = length(which(p2$class == c[-t]))
correct3 = length(which(p3$class == c[-t]))

# get the proportion correct :
prop1 = correct1 / length(c[-t])
prop2 = correct2 / length(c[-t])
prop3 = correct3 / length(c[-t])

# get the J-scores :
J11 = J1(m1,c)
J21 = J2(m1,c)
J31 = J3(m1,c)

J12 = J1(m2,c)
J22 = J2(m2,c)
J32 = J3(m2,c)

J13 = J1(m3,c)
J23 = J2(m3,c)
J33 = J3(m3,c)

# perform nway-cross validation :
n1 = nway_cross_validate_lda(m1,c)
n2 = nway_cross_validate_lda(m2,c)
n3 = nway_cross_validate_lda(m3,c)

cat("accuracy of full nway =",   n1, "\n")
cat("accuracy of t-test nway =", n2, "\n")
cat("accuracy of seq nway =",    n3, "\n")

# print the result to the screen :
cat("accuracy of full dataset =", 
    prop1*100, "%\n")
cat("J11 =", J11, ": J21 =", J21, ": J31 =", J31, "\n")
cat("accuracy of t-test dims",
    nmax(vt,2), "=", prop2*100, "%\n")
cat("J12 =", J12, ": J22 =", J22, ": J32 =", J32, "\n")
cat("accuracy of seq-forward for dims",
    vs, "=", prop3*100, "%\n")
cat("J13 =", J13, ": J23 =", J23, ": J33 =", J33, "\n")

# set the 1st linear discriminant :
xlda1 = m1 %*% zlda1$scaling[,1]
xlda2 = m2 %*% zlda2$scaling[,1]
xlda3 = m3 %*% zlda3$scaling[,1]

# set the 2nd linear discriminant :
ylda1 = m1 %*% zlda1$scaling[,2]
ylda2 = m2 %*% zlda2$scaling[,2]
ylda3 = m3 %*% zlda3$scaling[,2]

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
pdf('../doc/images/fruit.pdf', width=9, height=3)
par(mar=c(2.5,2.5,.1,.1),mgp = c(1.5, .5, 0), mfrow=c(1,3))

plot(xlda1, ylda1, col=cc, bg=cc, type='p', pch=21,
     xlab='First Linear Discriminant',
     ylab='Second Linear Discriminant', main='')
legend("topleft", "a.)", bty="n") 
grid()

plot(xlda2, ylda2, col=cc, bg=cc, type='p', pch=21,
     xlab='First Linear Discriminant',
     ylab='Second Linear Discriminant', main='')
legend("topleft", "b.)", bty="n") 
grid()

plot(xlda3, ylda3, col=cc, bg=cc, type='p', pch=21,
     xlab='First Linear Discriminant',
     ylab='Second Linear Discriminant', main='')
legend("topleft", "c.)", bty="n") 
grid()

dev.off()



