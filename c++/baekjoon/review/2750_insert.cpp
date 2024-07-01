#include <iostream>
#include <vector>

using std::vector;

int main() {
  int n;
  std::cin >> n;
  vector<int> arr(n);
  for (int i = 0; i < n; ++i) {
    std::cin >> arr[i];
  }
  int temp;
  for (int i = 1; i < n; i++) {
    temp = arr[i];
    int j;
    for (j = i - 1; j >= 0 && temp < arr[j]; --j) {
      arr[j + 1] = arr[j];
    }
    arr[j + 1] = temp;
  }
  for (int i = 0; i < n; ++i) std::cout << arr[i] << '\n';
}