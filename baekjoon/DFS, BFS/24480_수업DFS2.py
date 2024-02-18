import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)
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


def dfs(graph, v, visited):
    global cnt
    visited[v] = cnt
    for i in graph[v]:
        if visited[i] == 0:
            cnt += 1
            dfs(graph, i, visited)


dfs(graph, r, visited)
for i in range(1, n + 1):
    print(visited[i])
