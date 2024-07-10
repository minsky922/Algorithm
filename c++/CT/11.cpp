#include <iostream>
#include <stack>
#include <string>

using namespace std;

int solution(string s) {
  stack<int> stk;
  for (int i = 0; i < s.size(); i++) {
    if (stk.empty() || stk.top() != s[i])
      stk.push(s[i]);
    else
      stk.pop();
  }

  return stk.empty();
}