#include <iostream>
using namespace std;

void swap(int &a, int &b) {
  int tmp = a;
  a = b;
  b = tmp;
}
void quickSort(int arr[], int start, int end) {
  if (end - start <= 1) return;
  int &pivot = arr[start];
  int left = start + 1, right = end - 1;
  while (true) {
    while (left <= right and arr[left] <= pivot) left++;
    while (left <= right and arr[right] >= pivot) right--;
    if (left > right) break;
    swap(arr[left], arr[right]);
  }
  swap(pivot, arr[right]);
  quickSort(arr, start, right);
  quickSort(arr, right + 1, end);
}
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin >> n;
  int arr[n];
  for (int &x : arr) cin >> x;
  quickSort(arr, 0, n);
  for (const int &x : arr) cout << x << '\n';
}