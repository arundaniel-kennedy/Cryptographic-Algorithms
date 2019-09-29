//#include <bits/stdc++.h>
#include<iostream>
#include<ctype.h>

using namespace std;

string caesarCipher(string s, int key=3,int idx=0) {
    int i,n=s.length(),t,e;

    key=key%26;
    if(idx){
        key=26-key;
    }
    for(i=0;i<n;i++){
        if(isalpha(s[i])){
            t=int(s[i]);
            e=t+key;
            if(isupper(s[i])){
                t=e>90?e-26:e;          // 65+e-91
            }
            else{
                t=e>122?e-26:e;         // 97+e-123
            }
            s[i]=char(t);
        }
    }
    return s;
}

int main()
{
    int ch,key=3;
    string s;

    cout<<"Enter text : ";
    getline(cin, s);
    cout<<"Encryption key : \n1 - Default key\n2 - Custom key\nYour option : ";
    cin>>ch;
    if(ch==2)
    {
        cout<<"Enter key : ";
        cin>>key;
    }
    cout<<"Operation on the text : \n1 - Encryption \n2 - Decryption\nYour option : ";
    cin>>ch;
    cout<<caesarCipher(s,key,ch-1)<<endl;
    return 0;
}
