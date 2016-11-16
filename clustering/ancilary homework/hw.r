

d = rbind(c(0.0,  9.5, 10.5, 9.5, 10.5),
          c(9.5,  0.0,  3.0, 6.0,  7.0),
          c(10.5, 3.0,  0.0, 7.0,  8.0),
          c(9.0,  6.0,  7.0, 0.0,  3.0),
          c(10.5, 7.0,  8.0, 3.0,  0.0))

cl = hclust(as.dist(d))


# plot them colored by class :
png(file = 'dendo.png', width=400, height=400)

plot(cl)
dev.off()

# store the iris 'classes' :
c = iris[,5]

# store the iris 'data' :
d = iris[,seq(1,4)]
m = as.matrix(d)

cmin = apply(m, 2, min)
cmax = apply(m, 2, max)

CPCC = 0.0

for (i in seq(1:10000))
{
  c1 = runif(150, min=cmin[1], max=cmax[1])
  c2 = runif(150, min=cmin[2], max=cmax[2])
  c3 = runif(150, min=cmin[3], max=cmax[3])
  c4 = runif(150, min=cmin[4], max=cmax[4])

  C   = cbind(c1,c2,c3,c4)
  DC1 = dist(C)
  hC  = hclust(DC1, 'ave')
  DC2 = cophenetic(hC)

  CPCC = CPCC + cor(DC1, DC2)
}

CPCC = CPCC / 10000

D1 = dist(m)
hc = hclust(D1, 'ave')
D2 = cophenetic(hc)

dataCPCC = cor(D1,D2)
