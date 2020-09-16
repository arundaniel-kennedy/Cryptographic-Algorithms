def euc(x,y):
  a=x
  b=y
  if(b==0):
    return a
  while(b!=0):
    c=a%b
    a=b
    b=c
  return a

