# brute force to find inverse

def inv(a,p):
  for i in range(p):
    if(a*i%p==1):
      return i
if __name__=="__main__": #this line alone not needed
  print(inv(7,26))