import math
ch=[]
cryp=[]
z=[]

def pad(pt,size):
  si = len(pt)
  rows = math.ceil(si/size)
  tot = rows*size
  mis = tot - si
  pt = pt + mis*'x'
  return pt

def enc(pt,k,size):
  for i in range(0,size):
    ch.append(pt[i::size])
  print(ch)
  for i in range(0,size):
    cryp.append(ch[int(k[i])-1])
  return ''.join(cryp)

def dec(pt,k,size):
  si = len(pt)
  rows = math.ceil(si/size)
  st = [pt[i:i+rows] for i in range(0, len(pt), rows)]
  do=[]
  for i in range(1,size+1):
    mi = k.find(str(i))
    #print(mi,i,st[mi])
    do.append(st[mi])
  di=[]
  for i in range(0,rows):
    for j in range(0,size):
      di.append(do[j][i])
  return ''.join(di)

if __name__=='__main__': #this line alone not needed
  pt=input("Enter plain Text: ")
  k=input("Enter your key: ")
  size = len(k)
  #print(pt)
  pt = pad(pt,size)
  ci = enc(pt,k,size)
  print(ci)
  pl = dec(ci,k,size)
  print(pl)