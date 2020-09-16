def miller(a):
  ch=[]
  b=[]
  w=0
  y=1
  flag=0

  #make number to be even
  if(a%2==0):
    return "not prime"
  else:
    a-=1
  #find the factors of the number
  for i in range(2,int(a/2)+1):
    while(a%i==0):
      a=a/i
      ch.append(i)

  #join 2 together and others together
  for i in ch:
    if(i==2):
      w+=1
    else:
      b.append(i)
  #make other elements into one number
  for i in b:
    y*=i

  #formula
  z=2**y%n

  if(z==1 or z==-1):
    return "prime"

  for i in range(1,w):
    #formula
    z=z**2%n

    if(z==1 or z==-1):
      return "prime"
    else:
      flag+=1

  if(flag!=0):
    return "not prime"

if __name__=="__main__": #this line alone not needed
  a=int(input("Enter number: "))
  n=a
  print(miller(a))