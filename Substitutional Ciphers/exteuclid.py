def exe(X, Y):
  x2 = 1
  x1 = 0
  a = Y
  y2 = 0
  y1 = 1
  b = X
  if (b == 0):
      return a
  if (b == 1):
      return b
  while (b != 0):
      q = int(a / b)
      r = a % b
      x = x2 - (q * x1)
      y = y2 - (q * y1)
      #print(x2, x1, x, y2, y1, y, a, b, r, q, "\n")
      x2 = x1
      x1 = x
      a = b
      y2 = y1
      y1 = y
      b = r
      if (b == 1):
          #print(x2, x1, ' ', y2, y1, ' ', a, b, ' ', ' ', "\n")
          if(y1<0):
            return Y+y1
          return y1
  return a


#print('x2', 'x1', 'x', 'y2', 'y1', 'y', 'a', 'b', 'r', 'q', "\n")
#print(exe(intinput(),input()))
