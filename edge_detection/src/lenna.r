# lenna image edge-detection project
# Evan Cummings
# CSCI 548 - Pattern Recognition
# Douglas Raiford, Fall 2015

source("functs.r")
library(jpeg)

# store the image :
d = readJPEG("../../data/Lenna.jpg")

# convert to grey scale :
g = convert_to_grey(d)

# save the resulting image :
writeJPEG(g, '../doc/images/lenna_grey.jpeg')

# get the gaussian kernel :
G = gaussian_kernel(1.4, 5)

# blur the image with kernel :
B = blur_image(g,G)

# save the resulting image :
writeJPEG(B, '../doc/images/lenna_blurred.jpeg')

# get the edges by the Laplace method :
E = laplacian(g,5)

# save the resulting image Laplacian :
writeJPEG(E, '../doc/images/lenna_laplace.jpeg')

# get the edges by the Laplace method :
Eb = laplacian(B,5)

# save the resulting blurred Laplacian :
writeJPEG(Eb, '../doc/images/lenna_blurred_laplace.jpeg')

# get the edges by the Laplace method :
Et = laplacian(B,5,tol=0.4)

# save the resulting blurred Laplacian :
writeJPEG(Et, '../doc/images/lenna_blurred_tol_laplace.jpeg')



