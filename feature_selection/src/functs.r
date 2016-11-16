# functions used for feature-selection project
# Evan Cummings
# CSCI 548 - Pattern Recognition
# Douglas Raiford, Fall 2015

getTscores = function(d,c)
{
  u = unique(c)
  n = length(u)
  m = dim(d)[2]
  v = rep(NA, m)
  for (k in 1:m)
  {
    s = 0
    for (i in 1:(n-1))
    {
      for (j in (i+1):n)
      {
        i_i  = which(c == u[i])
        j_i  = which(c == u[j])
        p    = t.test(d[i_i,k], d[j_i,k])
        s    = s + abs(p$statistic)
        #cat("k =", k, ": i =", i, ": j =", j, ": v[k] =", s, "\n")
      }
    }
    v[k] = s
  }
  return(v/sum(v))
}

nmax = function(x, n=2)
{
  nx = length(x)
  p  = nx - n
  xp = sort(x, partial=p)[p]
  return(which(x > xp))
}

Sb = function(x,c)
{
  u  = unique(c)
  k  = length(u)
  l  = list()
  
  for(i in 1:k)
  {
    l[[i]] = which(c == u[i])
  }

  m  = dim(x)[1]
  n  = dim(x)[2]
  mu = colMeans(x)
  S  = matrix(0, n, n)
  for(i in 1:k)
  {
    p    = length(l[[i]]) / m
    mu_i = colMeans(x[l[[i]],])
    S    = S + p * (mu_i - mu) %*% t(mu_i - mu)
  }
  return(S)
}

Sw = function(x,c)
{
  u  = unique(c)
  k  = length(u)
  l  = list()
  
  for(i in 1:k)
  {
    l[[i]] = which(c == u[i])
  }

  m  = dim(x)[1]
  n  = dim(x)[2]
  mu = colMeans(x)
  S  = matrix(0, n, n)
  for(i in 1:k)
  {
    x_i  = x[l[[i]],]
    p    = length(l[[i]]) / m
    sig  = cov(x_i)
    S    = S + p*sig
  }
  return(S)
}

J1 = function(x,c)
{
  S_b = Sb(x,c)
  S_w = Sw(x,c)
  J_1 = sum(diag(S_b)) / sum(diag(S_w))
  return(J_1)
}

J2 = function(x,c)
{
  S_b = Sb(x,c)
  S_w = Sw(x,c)
  S_m = S_w + S_b
  J_2 = det(ginv(S_w) %*% S_m)
  return(J_2)
}

J3 = function(x,c)
{
  S_b = Sb(x,c)
  S_w = Sw(x,c)
  J_3 = sum( diag( ginv(S_w) %*% S_b) )
  return(J_3)
}

seq_forward = function(x,c,k)
{
  m  = dim(x)[1]
  n  = dim(x)[2]
  v  = rep(NA, k)

  # populate the list of desired dimensions :
  for(i in 1:k)
  {
    # init the score to zero :
    s = 0
    
    # if the list is currently empty, just use t-test : 
    if(i == 1)
    {
      u  = unique(c)
      y  = length(u)
      for(j in 1:n)
      {
        sn = 0
        for (o in 1:(y-1))
        {
          for (q in (i+1):y)
          {
            o_i  = which(c == u[o])
            q_i  = which(c == u[q])
            p    = t.test(x[o_i,j], x[q_i,j])
            sn   = sn + abs(p$statistic)
          }
        }
        if(sn > s)
        {
          s    = sn
          v[i] = j
        }
      }
    }

    # otherwise, use the J3 metric :
    else
    {
      for(j in 1:n)
      {
        # exclude any dimensions we know we want already :
        if(length(intersect(v[1:i], j)) == 0)
        {
          vn    = v[1:i]
          vn[i] = j
          sn    = J3(x[,vn],c)
          if(sn > s)
          {
            s    = sn
            v[i] = j
          }
        }
      }
    }
  }
  return(v)
}

nway_cross_validate_lda = function(x,c)
{
  s = 0
  for(i in 1:nrow(x))
  {
    zlda  = lda(x[-i,], c[-i])
    p     = predict(zlda, x[i,])
    if(p$class == c[i])
      s   = s + 1
  }
  return(100 * s/nrow(x))
}

testConstantWithinGroup = function(v,c,tol=1.0e-6)
{
  u = unique(c)
  #for each class
  for(i in 1:length(u))
  {
    i_i = which(c == u[i])
    if(mean(v[i_i]) == 0)
      return(1)
    if(var(v[i_i]) < tol)
      return(1)
  }
  return(0)
}

removeConstantRows = function(x, cl, tol=1.0e-6)
{
  r = c()
  for(i in 1:nrow(x))
  {
    b = testConstantWithinGroup(x[i,], cl, tol=tol)
    if (b)
    {
      r = c(r,i)
    }
  }
  return(r)
}



