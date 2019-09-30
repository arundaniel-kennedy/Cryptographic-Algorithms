char = "abcdefghijklmnopqrstuvwxyz"

def enc(x,k):
  ch=""
  for i in x:
    m=char.find(i)
    n=(m+k)%26 #formula
    ch=ch+char[n]
  return ch

def dec(y,k):
  ch=""
  for i in y:
    m=char.find(i)
    n=(m-k)%26 #formula
    ch= ch+char[n]
  return ch

if __name__=="__main__": #this line alone not needed
  x = input("Enter Plain txt: ")
  k = int(input("Enter Key value: "))

  ci = enc(x,k)
  print(ci)
  print(dec(ci,k))