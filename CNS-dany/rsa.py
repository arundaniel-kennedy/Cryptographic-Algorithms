import exteuclid as ex #local file
import euler as eu #local file

char = "abcdefghijklmnopqrstuvwxyz"


def key():
  p = int(input("Enter p: "))
  q = int(input("Enter q: "))
  n = p*q
  pn = eu.euler(n)
  e = int(input("Enter e: "))
  ei = ex.exe(e,pn)
  d = ei % pn
  return (e,d,n)

def enc(word,key,n):
  fin=[]
  for i in word:
    j = char.find(i)
    #print("\n"+str(j))
    c = (j**key)%n
    #print(str(c)+"\n")
    fin.append(str(c))
  return fin

def dec(word,key,n):
  fin=[]
  for i in word:
    #j = char.find(i)
    #j = j+1
    #print("\n"+str(i))
    c = (int(i)**key)%n
    #print(str(c)+"\n")
    fin.append(char[c])
  return ''.join(fin)

if __name__ == '__main__': #this line alone not needed
  e,d,n = key()
  print(e,d,n)
  pt=input("Enter plain text: ")
  #pt = pt.split()
  #print(pt)
  a = enc(pt,e,n)
  print(' '.join(a),dec(a,d,n))

  a = enc(pt,d,n)
  print(' '.join(a),dec(a,e,n))