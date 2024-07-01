#include <iostream>
using namespace std;

bool numbers[2001];

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    int num;
    cin >> num;
    numbers[num + 1000] = true;
  }
  for (int i = 0, cnt = 0; cnt != n && i < 2001; i++) {
    if (numbers[i]) {
      cnt++;
      cout << i - 1000 << '\n';
    }
  }
}