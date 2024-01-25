import sys
from collections import deque

m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[False] * m for _ in range(n)] for _ in range(h)]

# 상하좌우위아래
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

q = deque()
answer = 0


def bfs():
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx < 0 or ny < 0 or nz < 0 or nx >= h or ny >= n or nz >= m:
                continue
            if graph[nx][ny][nz] == 0 and visited[nx][ny][nz] == False:
                q.append((nx, ny, nz))
                graph[nx][ny][nz] = graph[x][y][z] + 1
                visited[nx][ny][nz] = True


# 모두 1이 아닐 경우

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1 and visited[i][j][k] == 0:
                q.append((i, j, k))
                visited[i][j][k] = True
bfs()

for h in graph:  # 층
    for n in h:  # 층의 행
        for m in n:  # 행의 칸
            if m == 0:
                print(-1)
                exit(0)  # break 말고 전체 종료 해야함
        answer = max(answer, max(n))

print(answer - 1)
