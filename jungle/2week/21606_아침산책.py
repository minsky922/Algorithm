import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())

A = input()

graph = [[] for i in range(n + 1)]
visited = [0] * (n + 1)
place = [0] * (n + 1)

for i in range(len(A)):
    if A[i] == "1":
        place[i + 1] = 1


def dfs(v, cnt):  # v: 정점 번호, cnt : 실외와 연결된 실내 노드 개수 카운트
    visited[v] = True

    for i in graph[v]:  # 노드 v와 연결된 인접 노드를 하나씩 불러온다
        if place[i] == 1:  # 해당 노드의 위치가 실내이면
            cnt += 1  # 실내 개수 카운트에 +1 해준다.
        elif not visited[i] and place[i] == 0:  # 방문하지 않았고, 해당 i점의 위치가 실외라면
            cnt = dfs(i, cnt)  # 해당 실외점을 기준으로 dfs를 돈다
    return cnt


ans = 0

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    if place[a] == 1 and place[b] == 1:  # 둘다 실내이면
        ans += 2  # 서로 방문하는 케이스가 2가지이니 바로 2개 세기

sum = 0
for i in range(1, n + 1):
    if not visited[i] and place[i] == 0:  # 실외를 기준으로
        x = dfs(i, 0)  # 현재 cnt는 0
        sum += x * (
            x - 1
        )  # 실외인 노드를 기준으로 인접 노드 애들 개수 세는 것이 n * (n -1)이므로 실외 노드 걸릴때마다 전부 세기

print(sum + ans)
