#include <iostream>
using namespace std;



bool isPrime(int x) {
    if (x < 2) return false;
    for (int i=2; i<x; i++){
        if (x%i==0) return false;
    }
    return true;
}

int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int t;
    int a,b;
    cin >>t;
    for(int i=0;i<t;i++){
        int temp;
        cin>>temp;
        a = temp/2;
        b = temp/2;
        while(1){
            if (isPrime(a) && isPrime(b)){
                cout<<a<<" "<<b<<"\n";
                break;
            }
            a-=1;
            b+=1;
        }

    }
}