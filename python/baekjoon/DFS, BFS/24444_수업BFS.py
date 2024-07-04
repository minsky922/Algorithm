from collections import deque

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

cnt = 1

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(v):
    global cnt

    q = deque([r])
    visited[r] = 1
    while q:
        v = q.popleft()
        graph[v].sort()
        for g in graph[v]:
            if visited[g] == 0:
                cnt += 1
                visited[g] = cnt
                q.append(g)


bfs(r)

for v in visited[1:]:
    print(v)
