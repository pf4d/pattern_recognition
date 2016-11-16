# functions used for clustering project
# Evan Cummings
# CSCI 548 - Pattern Recognition
# Douglas Raiford, Fall 2015


sequential_forward = function(X, theta, kmax)
{
  m    = dim(X)[1]             # number of samples (rows)
  v    = rep(NA, m)            # cluster vector
  v[1] = 1
  mu   = t(as.matrix(X[1,]))   # centroid matrix

  # iterate through all the samples :
  for (i in 2:m)
  {
    dmin = Inf                 # min distance
    vmin = NA                  # associated min distance cluster
    k    = dim(mu)[1]          # number of clusters

    # iterate through all the clusters created thus far :
    for (j in 1:k)
    {
      d = norm(as.matrix(X[i,] - mu[j,]), 'f')
      
      if (d < dmin)
      {
        dmin = d
        vmin = j
      }

    }
    
    # might create a new cluster :
    if (dmin > theta & k < kmax)
    {
      mu   = rbind(mu, X[i,])
      v[i] = k + 1
    }

    # otherwise, add sample to nearest cluster :
    else
    {
      v[i]      = vmin
      v_i       = which(v == vmin)
      mu[vmin,] = colMeans(X[v_i,])
    }

  }
  return(v)
}



