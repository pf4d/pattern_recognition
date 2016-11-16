sobelGrey = function(img)
{
  GX      = c(-1,-2,-1,0,0,0,1,2,1)
  dim(GX) = c(3,3)
  GY      = c(1,0,-1,2,0,-2,1,0,-1)
  dim(GY) = c(3,3)
  returnImg = img
  imgDims = dim(img)
  
  numRows = imgDims[1]
  numCols = imgDims[2]
  numMatrices = imgDims[3]
  
  # sumX = 0
  # sumY = 0
  # SUM = 0
  for(rowID in 1:(numRows - 1))
  {
    for(colID in 1:(numCols - 1))
    {
      sumX = 0
      sumY = 0
      SUM = 0
      if(rowID==1 || rowID==numRows-1)
      {
        SUM = 0;
      }else if(colID==1 || colID==numCols-1)
      {
        SUM = 0;
      }
      else
      {
        for(I in -1:1)
        {
          for(J in -1:1)
          {
            sumX = sumX + img[rowID + I, colID + J] * GX[I+2,J+2];
          }
        }
        for(I in -1:1)
        {
          for(J in -1:1)
          {
            sumY = sumY + img[rowID + I, colID + J] * GX[I+2,J+2];
          }
        }
        # GRADIENT MAGNITUDE APPROXIMATION (Myler p.218)
        SUM = abs(sumX) + abs(sumY); 
        if(SUM > 1)
        {
          # cat("setting to 1, was ",SUM,"\n")
          SUM = 1;
        }
      }
      returnImg[rowID,colID] = SUM
    }
  }
  return(returnImg)
}


sobelColor = function(img)
{
  GX      = c(-1,-2,-1,0,0,0,1,2,1)
  dim(GX) = c(3,3)
  GY      = c(1,0,-1,2,0,-2,1,0,-1)
  dim(GY) = c(3,3)
  returnImg = img
  imgDims = dim(img)
  
  numRows = imgDims[1]
  numCols = imgDims[2]
  numMatrices = imgDims[3]
  
  # sumX = 0
  # sumY = 0
  # SUM = 0
  
  for(matrixID in 1:numMatrices)
  {
    for(rowID in 1:(numRows - 1))
    {
      for(colID in 1:(numCols - 1))
      {
        sumX = 0;
        sumY = 0;
        SUM = 0
        if(rowID==1 || rowID==numRows-1)
        {
          SUM = 0;
        }
        else if(colID==1 || colID==numCols-1)
        {
          SUM = 0;
        }
        else
        {
          for(I in -1:1)
          {
            for(J in -1:1)
            {
              sumX = sumX + img[rowID + I, colID + J,matrixID] * GX[I+2,J+2];
            }
          }
          for(I in -1:1)
          {
            for(J in -1:1)
            {
              sumY = sumY + img[rowID + I, colID + J,matrixID] * GX[I+2,J+2];
            }
          }
          # GRADIENT MAGNITUDE APPROXIMATION (Myler p.218)
          SUM = abs(sumX) + abs(sumY); 
          # cat("sum is ", SUM,"\n")
          if(SUM > 1)
          {
            # cat("setting to 1, was ",SUM,"\n")
            SUM = 1;
          }
        }
        returnImg[rowID,colID,matrixID] = SUM
      }
    }
  }
  for(i in 1:numMatrices)
  {
    returnImg[,,i] = 1 - returnImg[,,i]
  }
  return(returnImg)
}


convert_to_grey = function(img)
{
  numMatrices = dim(img)[3]
  aveImg = img[,,1]
  if(numMatrices > 1)
  {
    for(i in 2:numMatrices)
    {
      aveImg = aveImg + img[,,i]
    }
  }
  aveImg = aveImg/max(aveImg)
  return(aveImg)
}

invertGrey = function(img)
{
  returnImg = 1 - img
  return(returnImg)
}

laplacian = function(img, p, tol=0)
{
  # create 5 x 5 discrete Laplacian operator :
  q = median(1:p)
  M = matrix(-1, p, p)
  M[q,q] = p*p - 1

  m = dim(img)[1]
  n = dim(img)[2]
  
  # edge image to return :
  E = matrix(0, m, n)
  
  for (i in q:(m-q))
  {
    for (j in q:(n-q))
    {
      t = M * img[(i-q+1):(i+q-1), (j-q+1):(j+q-1)]
      v = sum(t)
      if (v < tol)
        v = 0
      if (v > 1)
        v = 1
      E[i,j] = v
    }

  }
  return(1 - E)
}


gauss_weights = function(r,sigma)
{
  return(exp( -(r**2) / (2 * sigma**2) ))
}

gaussian_kernel = function(sigma,n)
{
  # form the distance matrix from the center pixel :
  K = matrix(0,n,n)
  p = median(1:n)
  for (i in 1:n)
  {
    for (j in 1:n)
    {
      K[i,j] = sqrt((i - p)**2 + (j - p)**2)
    }
  }
  
  # form the gaussian kernel :
  G = round(15*gauss_weights(K,sigma))
  G = G / sum(G)

  return(G)
}

blur_image = function(img, M)
{
  q = median(1:dim(M)[1])
  m = dim(img)[1]
  n = dim(img)[2]
 
  # blurred image to return :
  B = matrix(0,m,n)
  
  for (i in q:(m-q))
  {
    for (j in q:(n-q))
    {
      t = M * img[(i-q+1):(i+q-1), (j-q+1):(j+q-1)]
      v = sum(t)
      B[i,j] = v
    }

  }
  return(B)
}



