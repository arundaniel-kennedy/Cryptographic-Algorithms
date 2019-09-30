import numpy as np
import exteuclid as ex #local file
import math

char = "abcdefghijklmnopqrstuvwxyz"

#forming it into matrix
def make_matrix(val,m,n):
  a=[]
  f=0
  for i in range(n):
    b=[]
    for j in range(m):
      b.append(char.find(val[f]))
      f+=1
    a.append(b)
  return a

def enc(p,k,n):
  #to split plain text into n element pairs
  arr = [p[i:i+n] for i in range(0, len(p), n)]
  for val in arr:
    mat = make_matrix(val,1,n)
    key = make_matrix(k,n,n)

    mm = np.matmul(key,mat)

    r=[]
    for x in mm:
      r.append(char[int(x)%26])

  return ''.join(r)

def dec(p,k,n):

  arr = [p[i:i+n] for i in range(0, len(p), n)]

  for val in arr:
    mat = make_matrix(val,1,n)
    key = make_matrix(k,n,n)

    invkey =  np.linalg.inv(key)
    det = np.linalg.det(key)

    adjkey = det*invkey
    indet = ex.exe(det,26)
    inkey = indet*adjkey
    inkey = inkey%26

    mm = np.matmul(inkey,mat)
    
    r=[]
    for x in mm:
      r.append(char[int(x[0]+0.5)%26])

  return ''.join(r)
  
if __name__=="__main__": #this line alone not needed
  n = int(input("Enter value of n: "))
  p = input("Enter Plaintext value: ")
  k = input("Enter key of "+str(n*n)+" characters: ")
  print(p+"\n")
  en = enc(p,k,n)
  print(en+"\n")
  print(dec(en,k,n))