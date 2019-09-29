import re

pfkt=[]                                 # Play Fair Key Table/Matrix
txt_chunks=[]                           # chunks of plain text

def indexof(c):                         # index of charac c in pkft
    for i in range(5):
        for j in range(5):
            if(pfkt[i][j]==c):
                return(i,j)
    return(-1,-1)                       # just for safety
    
def playfairCipher(txt,phrase="MONARCHY",idx=0):
    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    enc=""
    
    key = re.sub(r"[^A-Z]",'',phrase)   # accept only uppercase alpha in key phrase
    txt = re.sub(r"[^A-Z]",'',txt)      # accept only uppercase alpha in plain text
    for i in key:                       # remove multiple entries of the same alpha
        key=key[:key.index(i)+1]+key[key.index(i)+1:].replace(i,"")
        
    if('I' in key and 'J' in key):      # merge I/J in key
        if(key.index('I')>key.index('J')):
            key=key.replace('I',"")
        else:
            key=key.replace('J',"")

    if('I' in txt and 'J' in txt):      # merge I/J in txt
        if(txt.index('I')>txt.index('J')):
            txt=txt.replace('I',"")
        else:
            txt=txt.replace('J',"")
            
    for i in key:                       # remove letters present in key from alpha
        alpha=alpha.replace(i,"")
        
    if('I' in alpha and 'J' in alpha):  # merge I/J in alpha
        alpha=alpha.replace('J',"")
        
    if('I' in key or 'J' in key):       # remove I/J from alpha if present in key
        alpha=alpha.replace('I',"")
        alpha=alpha.replace('J',"")

    i=-1
    t=0
    e=len(key)
    tmp=[]
    while(t<e):                         # make PlayFairKeyTable from key
        if(t%5==0):
            i+=1
            pfkt.append(tmp.copy())     # adding a row to pfkt
            tmp.clear()
        tmp.append(key[t])
        t+=1
    pfkt.remove([])                     # removing [] from pfkt, reason (t=0)%5==0
    pfkt.append(tmp.copy())             # append last tmp key row to pfkt
    tmp.clear()
    
    t=t%5                               # complete that row in pfkt
    k=0
    while(t<5):                         # fill that last row in pkft from alpha
        tmp.append(alpha[k])
        t+=1
        k+=1
    if(k!=0):
        pfkt[-1]=pfkt[-1]+tmp.copy()
        tmp.clear()
    i+=1
    
    while(i<5):                         # make PlayFairKeyTable from remaining alpha
        t=0
        while(t<5):
            tmp.append(alpha[k])
            t+=1
            k+=1
        pfkt.append(tmp.copy())         # adding a row to pfkt
        tmp.clear()
        i+=1

    print("\nPlayFair Key Table =>")
    for i in range(5):                  # print pfkt as a matrix
        for j in range(5):
            print(pfkt[i][j],end=" ")
        print()

    # chuncks
    i=0
    n=len(txt)
    if(idx==0):                         # enc
        if(n==1):
            txt_chunks.append(txt+"X")
        else:
            n-=1
            while(i<n):
                if(txt[i]!=txt[i+1] or txt[i]==txt[i+1]=='X'):
                    txt_chunks.append(txt[i:i+2])
                else:                       # txt[i]=='X'
                    n+=1
                    txt=txt[:i+1]+"X"+txt[i+1:]
                    i-=2
                i+=2
            if(n%2==0):
                txt_chunks.append(txt[-1]+"X")
    else:                                   # dec
        while(i<n):
            txt_chunks.append(txt[i]+txt[i+1])
            i+=2
    print("Text Chunks => ",txt_chunks)
    
    # eval
    direc=((-1)**idx)                       # enc or dec check
    for i in txt_chunks:
        if(i[0]!=i[1]):                     # for 'XX' case check
            r1,c1=indexof(i[0])
            r2,c2=indexof(i[1])
            if(c1==c2):
                r1=(r1+direc)%5             # same col, so goto next row
                r2=(r2+direc)%5
            if(r1==r2):
                c1=(c1+direc)%5             # same row, so goto next col
                c2=(c2+direc)%5
                c1,c2=c2,c1                 # because same row, to maintain order
            enc+=pfkt[r1][c2]+pfkt[r2][c1]
        else:                               # # for 'XX' case
            r,c=indexof(i[0])
            r=(r+direc)%5
            c=(c+direc)%5
            enc+=pfkt[r][c]+pfkt[r][c]  
    return enc

def main():
    key="MONARCHY"                          # default key
    s=input("Enter text : ")
    ch=int(input("Encryption key : \n1 - Default key\n2 - Custom key\nYour option : "))
    if(ch==2):
        key=input("Enter key : ")
    ch=int(input("Operation on the text : \n1 - Encryption \n2 - Decryption\nYour option : "))
    print("Resultant Text = ",playfairCipher(s.upper(),key.upper(),ch-1))

main()
