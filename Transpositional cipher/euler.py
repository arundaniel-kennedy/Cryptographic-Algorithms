def euler(a):
  ch=[]
  d=[]
  sum=1
  #find factors
  for i in range(2,int(a/2)+1):
    while(a%i==0):
      a=a/i
      ch.append(i)
  #grouping same elements and making tuple pairs
  for i in range(len(ch)):
    count=0
    for j in range(len(ch)):
      if(ch[i]==ch[j]):
        count+=1
        #print(ch[i],ch[j])
    d.append((ch[i],count))
  #make elements unique
  d = list(set(d))

  #applying formulae
  for i in d:
    if(i[1]==1):
      sum*=i[0]-1
    else:
      temp=i[0]**i[1]-i[0]**(i[1]-1)
      sum*=temp
  return sum

if __name__=="__main__": #this line alone not needed
  val=int(input("Enter number: "))
  print("The number of coprimes of "+str(val)+" is "+str(euler(val)))