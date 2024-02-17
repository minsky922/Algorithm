import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

cnt = 1


def dfs(graph, v, visited):
    global cnt
    visited[v] = cnt  # 방문하면 순서 나타내기
    for i in graph[v]:
        if visited[i] == 0:
            cnt += 1
            dfs(graph, i, visited)


for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n + 1):
    graph[i].sort()

dfs(graph, r, visited)

for i in range(1, n + 1):
    print(visited[i])
