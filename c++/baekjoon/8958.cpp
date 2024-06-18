#include <iostream>
using namespace std;

int main(){
    int n;
    string s;
    cin >> n;
    for (int i = 0; i<n; i++){
        cin >> s;
        int total=0, cnt = 0;
        for (int j=0; j<s.length(); j++){
            if (s[j] == 'O') cnt++;
            else cnt = 0;
            total += cnt;
        }
        cout << total << "\n";
    }
    return 0;
}