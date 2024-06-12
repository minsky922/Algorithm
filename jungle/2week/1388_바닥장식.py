from collections import deque

# 세로,가로
n, m = map(int, input().split())

graph = [list(input()) for _ in range(n)]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        if graph[x][y] == "-":
            graph[x][y] = 0
            if y + 1 < m and graph[x][y + 1] == "-":
                q.append((x, y + 1))
        elif graph[x][y] == "|":
            graph[x][y] = 0
            if x + 1 < n and graph[x + 1][y] == "|":
                q.append((x + 1, y))


cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            bfs(i, j)
            cnt += 1
print(cnt)
