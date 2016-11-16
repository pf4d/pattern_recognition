x = c(5,6,3,2,7,8,9,3)
y = c(1,2,3,4,1,2,3,4)

# vector algebra :
z = 2*x + y + 1

# vector sum :
s = sum(z)

# change the shape of the vector to a matrix :
dim(y) = c(2,4)

# stack two vectors vertically :
t = rbind(c(1,2,3,4,5), c(6,7,8,9,0))

# delete all the variables :
rm(list = ls(all = TRUE))

# store the iris data :
q = iris

# print iris data :
print(q)

# print all defined variables :
print(ls())

# write to a csv file :
write.csv(iris, "output.csv", row.names=FALSE)

# read the variable back in :
readInVar = read.csv("output.csv")

# get the dimension of the data :
d = dim(readInVar)

# print the last column (species) :
print(readInVar[d[2]])

# print the first row :
print(head(readInVar, n=1))

# print each row with apply :
apply(cbind(seq(1,d[1]), readInVar), 1, print)

# print the type of the variable :
print(class(readInVar))
