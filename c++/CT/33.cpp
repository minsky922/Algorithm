#include <vector>

using namespace std;

vector<int> parents;
vector<int> rankData;

int charToInt(char c) { return c - '0'; }

int find(int x) {
  if (parents[x] == x) {
    return x;
  }
  // 파인드 연산시, 경로압축 사용
  parents[x] = find(parents[x]);

  return parents[x];
}

void unionSet(int x, int y) {
  int root1 = find(x);
  int root2 = find(y);

  // 루트 노드가 같으면 유니온 연산 불필요
  if (root1 != root2) {
    // 랭크 기반 알고리즘
    if (rankData[root1] < rankData[root2]) {
      parents[root1] = root2;
    } else if (rankData[root1] > rankData[root2]) {
      parents[root2] = root1;
    } else {
      parents[root2] = root1;
      rankData[root1]++;
    }
  }
}

vector<bool> solution(int k, vector<vector<char>> operations) {
  parents.resize(k);
  rankData.resize(k, 0);
  // 초기에 각 노드는 자신을 부모로 설정
  for (int i = 0; i < k; ++i) {
    parents[i] = i;
  }
  vector<bool> results;
  for (const auto& op : operations) {
    if (op[0] == 'u') {
      int x = charToInt(op[1]);
      int y = charToInt(op[2]);
      unionSet(x, y);
    } else if (op[0] == 'f') {
      int x = charToInt(op[1]);
      int y = charToInt(op[2]);
      results.push_back(find(x) == find(y));
    }
  }
  return results;
}