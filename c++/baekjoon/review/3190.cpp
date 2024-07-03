#include <deque>
#include <iostream>
#include <vector>

using namespace std;

struct Direction {
  int time;
  char turn;
};

const int dx[] = {0, 1, 0, -1};  // 동, 남, 서, 북
const int dy[] = {1, 0, -1, 0};

deque<pair<int, int>> snake;     // 뱀의 몸
int map[101][101] = {0};         // 사과 위치
vector<Direction> directions;    // 방향 전환 정보
bool check[101][101] = {false};  // 뱀의 몸이 있는지 여부
int n, k, l;

void input() {
  cin >> n >> k;
  for (int i = 0; i < k; i++) {
    int x, y;
    cin >> x >> y;
    map[x - 1][y - 1] = 1;  // 사과 위치 표시
  }

  cin >> l;
  for (int i = 0; i < l; i++) {
    int time;
    char turn;
    cin >> time >> turn;
    directions.push_back({time, turn});
  }
}

int main() {
  input();

  int dir_idx = 0;  // 초기 방향: 동쪽
  int time = 0;
  int cx = 0, cy = 0;  // 현재 뱀의 머리 위치
  snake.push_front({cx, cy});
  check[cx][cy] = true;
  int dir_change_idx = 0;  // 방향 전환 인덱스

  while (true) {
    time++;
    int nx = cx + dx[dir_idx];
    int ny = cy + dy[dir_idx];

    // 벽에 부딪히거나, 뱀의 몸과 부딪히면 게임 종료
    if (nx < 0 || ny < 0 || nx >= n || ny >= n || check[nx][ny]) {
      break;
    }

    // 이동
    cx = nx;
    cy = ny;
    snake.push_front({cx, cy});
    check[cx][cy] = true;

    // 사과가 없다면 꼬리 제거
    if (map[cx][cy] == 0) {
      int tail_x = snake.back().first;
      int tail_y = snake.back().second;
      check[tail_x][tail_y] = false;
      snake.pop_back();
    } else {  // 사과가 있다면 사과 제거
      map[cx][cy] = 0;
    }

    // 방향 전환
    if (dir_change_idx < directions.size() &&
        time == directions[dir_change_idx].time) {
      if (directions[dir_change_idx].turn == 'D') {
        dir_idx = (dir_idx + 1) % 4;  // 시계 방향 회전
      } else {
        dir_idx = (dir_idx + 3) % 4;  // 반시계 방향 회전
      }
      dir_change_idx++;
    }
  }

  cout << time << endl;

  return 0;
}
