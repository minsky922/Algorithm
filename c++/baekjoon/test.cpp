#include <iostream>
#include <string>

using namespace std;

int main() {
  int t;
  int r;
  string s;
  cin >> t;
  for (int i = 0; i < t; i++) {
    cin >> r >> s;
    for (int j = 0; j < s.length(); j++) {
      for (int k = 0; k < r; k++) {
        cout << s[j];
      }
    }
    cout << endl;
  }
  return 0;
}