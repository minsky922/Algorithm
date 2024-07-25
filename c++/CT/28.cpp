#include <string>
#include <vector>

using namespace std;

string preorder(vector<int> nodes, int idx) {
  if (idx < nodes.size()) {
    string ret = to_string(nodes[idx]) + " ";
    ret += preorder(nodes, idx * 2 + 1);
    ret += preorder(nodes, idx * 2 + 2);
    return ret;
  }
  return "";
}
string inorder(const vector<int>& nodes, int idx) {
  if (idx < nodes.size()) {
    string ret = inorder(nodes, idx * 2 + 1);
    ret += to_string(nodes[idx]) + " ";
    ret += inorder(nodes, idx * 2 + 2);
    return ret;
  }
  return "";
}
string postorder(const vector<int>& nodes, int idx) {
  if (idx < nodes.size()) {
    string ret = postorder(nodes, idx * 2 + 1);
    ret += postorder(nodes, idx * 2 + 2);
    ret += to_string(nodes[idx]) + " ";
    return ret;
  }
}

vector<string> solution(vector<int> nodes) {
  vector<string> result;
  string pre = preorder(nodes, 0);
  string in = inorder(nodes, 0);
  string post = postorder(nodes, 0);
  // 마지막 공백 제거
  pre.pop_back();
  in.pop_back();
  post.pop_back();

  result.push_back(pre);
  result.push_back(in);
  result.push_back(post);

  return result;
}