char = "abcdefghijklmnopqrstuvwxyz"
import random as r

k=[]
p=[]
c=[]

def gen():
  g=[]
  for i in range(1,9):
    g.append(str(r.randint(0,1)))
  g=''.join(g)
  k.append(g)
  return g

def enc(x):
  b=(''.join(format(char.find(x),'b'))).rjust(8,'0')
  g=gen()  
  return char[int(format(int(b,2)^int(g,2),'b'),2)%26]
  

pt=input("Enter text: ")
for i in pt:
  for j in i:
    c.append(enc(j))

print(''.join(c),' '.join(k))