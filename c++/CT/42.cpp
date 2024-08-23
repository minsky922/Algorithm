#include <string>
#include <vector>

using namespace std;

vector<bool> visited;

void dfs(const vector<vector<int>>& network, int node) {
  visited[node] = true;

  for (int i = 0; i < network[node].size(); i++) {
    if (network[node][i] && !visited[i]) {
      dfs(network, i);
    }
  }
}

int solution(int n, vector<vector<int>> computers) {
  visited = vector<bool>(computers.size(), false);
  int networkCount = 0;
  for (int i = 0; i < computers.size(); i++) {
    if (!visited[i]) {
      dfs(computers, i);
      networkCount++;
    }
  }
  return networkCount;
}