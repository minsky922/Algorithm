import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
k = int(input())


def dfs(start, visited, graph, group):
    visited[start] = group  # 현재 노드의 그룹 저장
    # 인접 노드 탐색
    for v in graph[start]:
        if visited[v] == 0:  # 아직 방문하지 않은 노드
            # 현재 노드의 group 과 다른 값 전달
            result = dfs(v, visited, graph, -group)
            if not result:
                return False
        else:
            # 이미 방문한 곳 중에서 노드가 현재 그룹과 같으면 이분 그래프가 아님
            if visited[v] == group:
                return False
    return True


for i in range(k):
    v, e = map(int, input().split())
    graph = [[] for i in range(v + 1)]
    visited = [0] * (v + 1)
    for j in range(e):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    for i in range(1, v + 1):
        if visited[i] == 0:
            result = dfs(i, visited, graph, i)
            if not result:
                break
    print("YES") if result else print("NO")
