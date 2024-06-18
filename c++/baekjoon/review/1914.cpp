#include <iostream>
#include <cmath>
using namespace std;


void hanoi(int n,int start,int end,int sub){
    if (n==1) {cout<<start<<' '<<end<<"\n";}
    else{
    hanoi(n-1,start,sub,end);
    cout<<start<<' '<<end<<"\n";
    hanoi(n-1,sub,end,start);
    }
}

int main(){
    int n;
    cin>>n;
    // c/c++ 언어 특성상 큰수 처리하기 위해
    string a = to_string(pow(2,n));
    int x = a.find('.');
    a = a.substr(0,x);
    a[a.length()-1] -=1;
    //
    cout<< a <<"\n";
    if (n<=20){
    hanoi(n,1,3,2);
    }
    return 0;
}