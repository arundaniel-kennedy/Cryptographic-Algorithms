import exteuclid as ex #local file

char = "abcdefghijklmnopqrstuvwxyz"

def enc(x):
  m=char.find(x)
  n=(a*m+b)%26 #formula
  return char[n]

def dec(y):
  c=ex.exe(a,26)
  m=char.find(y)
  n=(c*(m-b))%26 #formula
  return char[n]

cy=[]
px=[]
a=int(input("enter ⍺: "))
b=int(input("enter ß: "))
x=input("Enter plain text: ")

for i in x:
  cy.append(enc(i))
cy=''.join(cy)

print("cipher text: "+cy)

for i in cy:
  px.append(dec(i))
px=''.join(px)

print("plain text: "+px)
