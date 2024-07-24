#include <algorithm>
#include <map>
#include <string>
#include <vector>

using namespace std;

map<string, int> combi;  // 주문의 조합 - 조합의 빈도

void combination(string src, string dst, int depth) {
  if (dst.size() == depth)
    combi[dst]++;

  else
    for (int i = 0; i < src.size(); i++)
      combination(src.substr(i + 1), dst + src[i], depth);
}

vector<string> solution(vector<string> orders, vector<int> course) {
  vector<string> answer;
  // 주문 오름차순 정렬
  for (string &order : orders) sort(order.begin(), order.end());

  for (int len : course) {
    for (string &order : orders) combination(order, "", len);
    int maxOrder = 0;
    for (auto it : combi) maxOrder = max(maxOrder, it.second);
    for (auto it : combi)
      if (maxOrder >= 2 && it.second == maxOrder) answer.push_back(it.first);
    combi.clear();
  }
  sort(answer.begin(), answer.end());
  return answer;
}