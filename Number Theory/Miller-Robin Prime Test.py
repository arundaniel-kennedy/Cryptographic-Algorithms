n = int(input("Enter a number : ")) #for n>2

def isprime(n):
    if(n%2==0):
        return(0)
    else:
        w=0
        y=n-1
        while y % 2 == 0:
            w+=1
            y = y // 2
        z=(2**y)%n
        if((z-1)%n==0):
            return(1)
        else:
            for _ in range(w):
                z=(z*z)%n
                if(z==1):
                    return(1)
    return(0)

if(isprime(n)==0):
    print("Not a prime")
else:
    print("prime")



