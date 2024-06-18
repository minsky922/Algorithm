#include <iostream>
using namespace std;

int main() {
	int N, result = 0;
	int temp, cnt = 0;
	cin >> N;
	for (int i = 0; i < N; i++) {
        // c/c++은 띄어쓰기=엔터 같이 취급
		cin >> temp;
		for (int div = 1; div <= temp; div++) {
			if (temp%div == 0)
				cnt++;
		}
		if (cnt == 2)	//temp가 소수
			result++;
		cnt = 0;
	}
	cout << result << '\n';
}