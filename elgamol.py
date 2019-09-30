from exteuclid import exe #local file

p=467
q=2
x=127
w=100
r=213

#designing
y = (q**x)%p
print(y,p,q,"\n")

#signing
a = (q**r)%p
b = ((w-x*a)*(exe(r,p-1)))%(p-1)
#print(w,'-',x,'*',a,'^',exe(r,p-1),'%',p-1,"\n")
print(a,b,"\n")

#verification
f1 = ((y**a)*(a**b))%p
f2 = (q**w)%p 
print(f1,f2)