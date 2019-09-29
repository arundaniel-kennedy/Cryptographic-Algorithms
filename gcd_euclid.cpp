#include<iostream>
using namespace std;

int gcd(int a,int b){
	int c;
	while(b>0){
		c=a%b;
		a=b;
		b=c;
	}
	return a;
}

int main(){
	int a,b;
	cout<<"Enter 2 nos. : ";
	cin>>a>>b;
	cout<<"\nGCD("<<a<<","<<b<<") = "<<gcd(a,b)<<endl;
	return 0;
}
