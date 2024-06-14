    #include <iostream>

    using namespace std;
    string a,b,c;

    //stdio.h는 C에서 printf, scanf를 사용할 수 있는 헤더이다.
    // iostream은 C++에서 cout, cin을 사용할 수 있는 헤더이다.
    // cin, cout은 기본적으로 C의 stdio.h와 동기화되어있다. = stdio.h의 버퍼와 iostream의 버퍼를 같이 쓴다는 말
    

    int main(){
        ios::sync_with_stdio(false), cin.tie(0); // 전자는 c를 안쓰고 c++의 입출력인 cin, cout만 사용 (동기화 해제)
        // 단점 : 멀티쓰레드 불가 - 싱글쓰레드 환경에서만 사용(실무에서 사용 불가)
        //cin.tie는  cin과 cout을 묶어 입출력 속도 개선
        // endl 대신 '\n' 써야 빠름
        cin >> a >> b >> c;
        cout << stoi(a) + stoi(b) - stoi(c) << "\n"; // stoi : string to int
        cout << stoi(a+b) - stoi(c);
        return 0;
    }