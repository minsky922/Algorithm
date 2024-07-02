#include <iostream>
#include <queue>
using namespace std;

priority_queue<int, vector<int>, greater<int>>
    pq;  // 내림차순으로 정렬해주는 큐 선언
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    int num;
    cin >> num;
    if (num == 0) {
      if (pq.empty())
        cout << 0 << "\n";
      else {
        cout << pq.top() << "\n";
        pq.pop();
      }
    } else {
      pq.push(num);
    }
  }
}