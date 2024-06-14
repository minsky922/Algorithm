    #include <iostream>

    using namespace std;
    string a,b,c;

    int main(){
        ios::sync_with_stdio(0), cin.tie(0); // 전자는 c를 동기화 안하고 c++의 입출력인 cin, cout만 사용
        //cin.tie는  cin과 cout을 묶어 입출력 속도 개선
        // endl 대신 '\n' 써야 빠름
        cin >> a >> b >> c;
        cout << stoi(a) + stoi(b) - stoi(c) << "\n";
        cout << stoi(a+b) - stoi(c);
        return 0;
    }