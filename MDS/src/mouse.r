# mouse data MDS project
# Evan Cummings
# CSCI 548 - Pattern Recognition
# Douglas Raiford, Fall 2015

# read in the data :
f = read.csv("../../data/otu_table_L6.txt", sep="\t", row.names=1)

# get the experiment names :
e = colnames(f)

# store indexes of proximal (P) and distal (D) experiments, and mouse types
# B and C :
P = grep("[A-Z]+P[0-9]", e)
D = grep("[A-Z]+D[0-9]", e)
B = grep("^B[A-Z]+[0-9]", e)
C = grep("^C[A-Z]+[0-9]", e)

# transpose the data so each row is an experiment :
d = t(f)

# perform MDS on d :
p = cmdscale(dist(d))

# color vector :
cols  = c('black', 'red')
cc    = as.vector(e)
cc[P] = cols[1]
cc[D] = cols[2]

# plot them colored by experiment :
png('../doc/images/mds_plot_mouse_experiment.png', res=200, width=6, 
    height=6, units='in')
par(mar=c(2.5,2.5,2.5,.1),mgp = c(1.5, .5, 0))
plot(p, col=cc, bg=cc, type='p', pch=21, cex=2, 
     xlab='First Principal Component',
     ylab='Second Principal Component', main='Mouse Data Using MDS')
legend('topleft', c('proximal', 'distal'), col = cols, pt.bg = cols, pch = 21)
dev.off()

# color vector :
cols  = c('purple', 'green')
cc    = as.vector(e)
cc[B] = cols[1]
cc[C] = cols[2]

# plot them colored by mousey type :
png('../doc/images/mds_plot_mouse_type.png', res=200, width=6, 
    height=6, units='in')
par(mar=c(2.5,2.5,2.5,.1),mgp = c(1.5, .5, 0))
plot(p, col=cc, bg=cc, type='p', pch=21, cex=2,
     xlab='First Principal Component',
     ylab='Second Principal Component', main='Mouse Data Using MDS')
legend('topleft', c('B', 'C'), col = cols, pt.bg = cols, pch = 21)
dev.off()



