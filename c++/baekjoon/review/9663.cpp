#include <iostream>
using namespace std;
int n, total = 0;
int row[15];

bool check(int x) {
  for (int i = 0; i < x; i++) {
    if (row[x] == row[i] || abs(row[x] - row[i]) == abs(x - i)) return false;
  }
  return true;
}
void nqueen(int x) {
  if (x == n)
    total++;
  else {
    for (int i = 0; i < n; i++) {
      row[x] = i;
      if (check(x)) nqueen(x + 1);
    }
  }
}

int main() {
  cin >> n;
  nqueen(0);
  cout << total;
  return 0;
}