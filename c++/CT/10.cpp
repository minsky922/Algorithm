#include <stack>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;
// 닫힌 괄호를 키로
unordered_map<char, char> bracketPair = {{')', '('}, {']', '['}, {'}', '{'}};
bool isValid(string &s, int start) {
  stack<char> stk;
  unsigned int sz = s.size();
  for (int i = 0; i < sz; i++) {
    char ch = s[(start + i) % sz];
    if (bracketPair.count(ch)) {  // ch 닫힌 괄호인 경우
      if (stk.empty() || stk.top() != bracketPair[ch]) return false;
      stk.pop();
    } else {
      stk.push(ch);
    }
  }
  return stk.empty();
}

int solution(string s) {
  int answer = 0;
  int n = s.size();
  for (int i = 0; i < n; i++) {
    answer += isValid(s, i);
  }
  return answer;
}