import math 

def primeFactors(n):
    p={}
    while n % 2 == 0:
        if '2' in p:
            p['2']+=1
        else:
            p['2']=1
        n = n // 2
		
    for i in range(3,int(math.sqrt(n))+1,2):
        while (n % i== 0):
            if str(i) in p:
                p[str(i)]+=1
            else:
                p[str(i)]=1
            n = n // i 
    if (n > 2):
        p[str(n)]=1
    return(p)


n = int(input("Enter a number : "))
p=primeFactors(n)
ans=1
for i in p:
    ans*=((int(i)**p[i])-(int(i)**(p[i]-1)))
print("No. of coprimes of",n,"=",ans)



