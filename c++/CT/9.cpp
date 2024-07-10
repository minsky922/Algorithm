#include <stack>
#include <string>

using namespace std;

string solution(int decimal) {
  if (decimal == 0) return "0";

  stack<int> stack;
  while (decimal > 0) {
    stack.push(decimal % 2);
    decimal /= 2;
  }
  string binary = "";
  while (!stack.empty()) {
    binary += to_string(stack.top());
    stack.pop();
  }
  return binary;
}
