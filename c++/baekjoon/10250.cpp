#include <iostream>

using namespace std;

int main(){
    int N;
    cin >> N;

    for (int i =0; i < N; ++i) {
        int h, w, n;
        cin >> h >> w >> n;

        int X = n % h;
        int Y = n / h + 1;

        if (X == 0) {
            X = h;
            Y -= 1;
        }
        cout << X * 100 + Y << endl;
    }
    return 0;
}

/* 
python 
N=int(input())

for i in range(N):
    h,w,n = map(int,input().split())
    X = n % h
    Y = n//h + 1
    if X == 0:
        X = h
        Y-=1
    print(X * 100 + Y)
*/

