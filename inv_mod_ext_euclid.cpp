#include<iostream>
using namespace std;

int x,x1=0,x2=1,y,y1=1,y2=0,r,q,n;

int eemod(int a,int b){
	while(b>1){
        q=a/b;
        r=a%b;
        x=x2-q*x1;
        y=y2-q*y1;
        x2=x1;	x1=x;	a=b;
        y2=y1;	y1=y;	b=r;
    }

	if(b==0){
		return -1;
	}
	if(b==1){
		if(y1<0){
                        y1=n+y1;
                }
		return y1;
	}
}

int main(){
	int a,ch;
	cout<<"Enter base no. : ";
	cin>>a;
	cout<<"Enter mod no. : ";
	cin>>n;
	ch=eemod(n,a%n);
	if(ch!=-1){
		ch%=n;
		if(ch<0){
			ch=n+ch;
		}
		cout<<"("<<a<<"^-1) mod "<<n<<" = "<<ch<<endl;
	}
	else
		cout<<"Inverse modulo does not exist"<<endl;
	return 0;
}
