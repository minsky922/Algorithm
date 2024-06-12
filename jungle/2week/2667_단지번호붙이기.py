from collections import deque

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    cnt = 1
    graph[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                cnt += 1
                q.append((nx, ny))
    return cnt


ans = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            ans.append(bfs(i, j))
ans.sort()

print(len(ans))
for i in ans:
    print(i)
