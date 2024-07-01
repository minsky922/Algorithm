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
  for (int j = 0; j < n - 1; ++j) {
    for (int i = 0; i < n - j - 1; ++i) {
      if (arr[i] > arr[i + 1]) {
        temp = arr[i + 1];
        arr[i + 1] = arr[i];
        arr[i] = temp;
      }
    }
  }
  for (int i = 0; i < n; ++i) std::cout << arr[i] << '\n';
}