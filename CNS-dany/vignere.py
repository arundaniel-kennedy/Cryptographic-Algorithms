char = "abcdefghijklmnopqrstuvwxyz"
ch=[]
st=[]

import math

def enc():
  for i in range(len(x)):
    ch.append(char[(int(char.find(x[i]))+int(char.find(y[i])))%26])
  return ''.join(ch)

def dec(i):
  if(i==1):
    for i in range(len(ch)):
      st.append(char[(int(char.find(ch[i]))-int(char.find(y[i])))%26])
    return ''.join(st)
  else:
    for i in range(len(x)):
      st.append(char[(int(char.find(x[i]))-int(char.find(y[i])))%26])
    return ''.join(st)

def pad(y):
  y=y*(math.ceil(len(x)/len(y)))
  y=y[:len(x)]
  return y

x = input()
y = input()

y=pad(y)

#print(y)
print(enc())
print(dec(1))