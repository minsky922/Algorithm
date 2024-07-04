import sys

input = sys.stdin.readline
from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

high = max(map(max, graph))
# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
queue = deque()


def bfs(i, j, high):
    queue.append((i, j))
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if graph[nx][ny] > high and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))


result = 0  # 최대 안전 영역의 개수를 저장
for k in range(high):
    visited = [[0] * N for _ in range(N)]  # 방문리스트
    ans = 0

    for i in range(N):
        for j in range(N):
            # 위치가 물에 잠기지 않았고(graph[i][j] > k) 아직 방문하지 않았다면(visited[i][j] == 0)
            if graph[i][j] > k and visited[i][j] == 0:
                bfs(i, j, k)  # 그 위치에서 BFS를 시작
                ans += 1  # BFS 실행 후, 안전 영역의 수(ans) 1증가
    # 모든 위치에 대한 탐색이 끝나면, result를 최대 안전 영역 수로 업데이트
    if result < ans:
        result = ans

print(result)
