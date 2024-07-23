#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>
using namespace std;

vector<int> solution(int n, vector<string> words) {
  vector<int> answer(2, 0);
  unordered_set<string> usedWords;
  usedWords.insert(words[0]);

  for (int i = 1; i < words.size(); ++i) {
    // unorderd_set 의 insert() 메서드의 second를 통해 중복을 확인
    if (!usedWords.insert(words[i]).second ||
        words[i].front() != words[i - 1].back()) {
      answer[0] = i % n + 1;
      answer[1] = i / n + 1;
      return answer;
    }
  }
  return answer;
}