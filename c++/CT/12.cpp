#include <stack>
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> prices) {
  vector<int> answer(prices.size());  // 가격이 떨어지지 않은 기간 저장 벡터
  stack<int> s;  // 스택에는 prices 인덱스가 들어감, 이전가격과 현재가격을
                 // 비교하기 위한 용도
  int priceNum = prices.size();
  for (int i = 0; i < priceNum; i++) {
    while (!s.empty() && prices[s.top()] > prices[i]) {
      answer[s.top()] = i - s.top();
      s.pop();
    }
    s.push(i);
  }
  // 스택에 남아있는 가격은 가격이 떨어지지 않은 경우
  while (!s.empty()) {
    answer[s.top()] = priceNum - s.top() - 1;
    s.pop();
  }
  return answer;
}