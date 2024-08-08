#include <queue>
#include <string>
#include <vector>

using namespace std;

// 현재 좌표, 해당좌표까지 이동 횟수
struct Point {
  int y, x, cnt;
};

int dy[4] = {-1, 0, 1, 0};
int dx[4] = {0, 1, 0, -1};
int n, m;

bool isWithinRange(int y, int x) { return 0 <= y && y < n && 0 <= x && x < m; }

// 시작좌표 확인
Point findStartPoint(char start, vector<string> &maps) {
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (maps[i][j] == start) {
        return {i, j, 0};
      }
    }
  }
  return {-1, -1, -1};  // 시작점 찾지 못한 경우
}

int bfs(char start, char end, vector<string> &maps) {
  bool visited[101][101] = {false};
  queue<Point> q;
  q.push(findStartPoint(start, maps));  // 시작노드부터 bfs로 탐색하도록 추가
  while (!q.empty()) {
    Point current = q.front();
    q.pop();
    // 목적지에 도달했으면 해당 목적지까지 이동 횟수 반환
    if (maps[current.y][current.x] == end) {
      return current.cnt;
    }
    // 현재 위치기준 상하좌우 확인
    for (int i = 0; i < 4; i++) {
      int ny = current.y + dy[i];
      int nx = current.x + dx[i];
      // 후보 좌표가 미로범위내에 있고 아직 방분하지 않았으며 벽이아니면
      // 탐색대상에 추가
      if (isWithinRange(ny, nx) && !visited[ny][nx] && maps[ny][nx] != 'X') {
        q.push({ny, nx, current.cnt + 1});
        visited[ny][nx] = true;
      }
    }
  }
  return -1;
}

int solution(vector<string> maps) {
  n = maps.size();
  m = maps[0].size();
  // 시작지점부터 L까지 최단 거리를 구함
  int distanceToL = bfs('S', 'L', maps);
  if (distanceToL == -1) return -1;
  // L부터 도착지점까지 최단거리를 구함
  int distanceToE = bfs('L', 'E', maps);
  return distanceToE == -1 ? -1 : distanceToL + distanceToE;
}