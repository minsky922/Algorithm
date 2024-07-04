import sys
from collections import deque

input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0] * (n + 1)
for i in range(n + 1):
    graph[i].sort(reverse=True)

cnt = 1


def bfs(graph, v, visited):
    global cnt
    q = deque([v])
    visited[v] = 1
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                cnt += 1
                visited[i] = cnt
                q.append(i)


bfs(graph, r, visited)
for i in range(1, n + 1):
    print(visited[i])
