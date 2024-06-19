#include <iostream>
using namespace std;
/*for 문*/
// int main() {
//   int n;
//   int t = 1;
//   cin >> n;
//   if (n == 0) {
//     t = 1;
//   } else {
//     for (int i = 1; i <= n; i++) {
//       t *= i;
//     }
//   }
//   cout << t;
// }
/* 재귀 */
int f(int x) {
  if (x <= 1) {
    return 1;
  }
  return x * f(x - 1);
}

int main() {
  int n;
  cin >> n;
  cout << f(n);
}