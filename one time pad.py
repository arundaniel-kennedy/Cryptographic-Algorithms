import random as rd

def keygen(n):
    keys=[]
    i=0
    while(i<n):
        t=rd.randint(65,90)
        if t not in keys:
            keys.append(t)
        else :
            i-=1
        i+=1
    return(keys)

pt=input("Enter the plain text : ")
pt=pt.split(" ")
keys=[]
enc=[]
for i in pt:
  n=len(i)
  keys.append(keygen(n))
  t=[]
  for j,k in zip(i,range(n)):
    t.append((ord(j))^(keys[-1][k]))
  enc.append(t)
print("Ciphered =>",enc)

print("Keys =>",keys)

dec=[]
for i,j in zip(enc,keys):
  t=""
  for m,n in zip(i,j):
    t+=chr(m^n)
  dec.append(t)
print("Deciphered =>",dec)
