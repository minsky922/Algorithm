import sys
from collections import deque
import copy

input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs():
    q = deque()
    # 원래의 graph는 유지시켜야한다
    tmp_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                q.append((i,j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if tmp_graph[nx][ny] == 0:
                tmp_graph[nx][ny] = 2
                q.append((nx, ny))
    global ans
    cnt = 0

    for i in range(n):
        cnt += tmp_graph[i].count(0)

    ans = max(ans, cnt)

# 백트래킹 - 벽을 세우는 모든 경우의 수 검토
def makeWall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makeWall(cnt+1)
                graph[i][j] = 0

ans = 0
makeWall(0)
print(ans)