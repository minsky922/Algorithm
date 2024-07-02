// long long은 9,223,372,036,854,775,807까지 표현이 가능
// 2,147,483,647 x 2,147,483,647까지는 커버가 가능
#include <iostream>
using namespace std;
// a^b=a^(b/2) * a^(b^2)
long long a, b, c, k;
long long power(long long b) {
  if (b == 1) return a % c;
  k = power(b / 2) % c;
  if (b % 2 == 0) return k * k % c;
  return k * k % c * a % c;
}
int main() {
  cin >> a >> b >> c;
  cout << power(b);
  return 0;
}