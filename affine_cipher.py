def gcd(a,b):
    while(b>0):
        c=a%b
        a=b
        b=c
    return a

def eemod(a,b):
    x2=1
    x1=0
    y2=0
    y1=1
    while(b>1):
        q=a//b
        r=a%b
        x=x2-q*x1
        y=y2-q*y1
        x2=x1
        x1=x
        a=b
        y2=y1
        y1=y
        b=r

    if(b==0):
        return -1
	    
    if(b==1):
        if(y1<0):
            y1=26+y1
        return y1


def add(s,key,idx=0):
    ans=""
    direc=1
    n=len(s)
    i=0
    if(idx):
        direc=-1
    
    while(i<n):
        c=s[i]
        a=ord(s[i])
        if(a>64 and a<91):
            a-=65
            t=(a+(key*direc))%26+65
            c=chr(t)
        ans+=c
        i+=1
    return ans

def mul(s,key):
    ans=""
    n=len(s)
    i=0
    while(i<n):
        c=s[i]
        a=ord(s[i])
        if(a>64 and a<91):
            a-=65
            t=((a*key)%26)+65
            c=chr(t//1)
        ans+=c
        i+=1
    return ans

def affineCipher(s,a,b,ch):
    ans=''
    if(ch==1):
        ans=mul(s,a)
        ans=add(ans,b)
    else:
        ch=eemod(26,a%26)
        ch=ch%26
        ans=add(s,b,1)
        ans=mul(ans,ch)
    return ans

def main():
    txt=input("Enter text : ")
    #label: z
    a=int(input("Enter key1 (alpha) : "))
    if(gcd(a%26,26)!=1):
        print("This key (key1 =",a,") can not be used\n\nEnter new key")
    #    goto z
    b=int(input("Enter key2 (beta) : "))
    ch=int(input("Operation on text :\n1-Encryption\n2-Decryption\nYour option : "))
    print("Resultant text =",affineCipher(txt.upper(),a%26,b%26,ch))

main()
