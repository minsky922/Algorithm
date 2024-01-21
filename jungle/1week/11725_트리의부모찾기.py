import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
# graph, parent 초기화
graph = [[] for _ in range(n + 1)]
parent = [False for _ in range(n + 1)]


def dfs(graph, vertex, visited):
    for i in graph[vertex]:
        # 만약 방문하지 않았을 경우 방물할 정점의 값 할당하고 재귀호출
        if not visited[i]:
            visited[i] = vertex
            dfs(graph, i, visited)


# 주어진 노드로 트리값 할당
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# dfs 함수 사용하여 parent 값 할당
dfs(graph, 1, parent)

for i in range(2, n + 1):
    print(parent[i])
