import math

def enc(x):
  s1=x[0::2]
  s2=x[1::2]
  return s1+s2

def dec(y):
  f1=y[0:math.ceil(len(y)/2)]
  f2=y[math.ceil(len(y)/2):]
  ch=[]
  for i,j in zip(f1,f2):
    ch.append(i)
    ch.append(j)
  if(len(f1)>len(f2)):
    ch.append(f1[-1])
  else:
    ch.append(f2[-1])

  return ''.join(ch)