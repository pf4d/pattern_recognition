# violet image edge-detection project
# Evan Cummings
# CSCI 548 - Pattern Recognition
# Douglas Raiford, Fall 2015

source("functs.r")
library(jpeg)

# store the image :
d = readJPEG("../../data/violet.jpg")

# get the edges detected by the 'Sobel' method :
s = sobelColor(d)

# save the resulting image :
writeJPEG(s, '../doc/images/violet_sobel.jpeg')


