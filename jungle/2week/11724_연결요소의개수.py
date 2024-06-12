import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())

parent = [i for i in range(N + 1)]


def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return
    parent[a] = b


for __ in range(M):
    a, b = map(int, input().split())
    union(a, b)

# 이 부분이 최신화를 해주는 부분. 이렇게 한번더 정리해주면 같은 그룹은 같은 숫자를 가지는 parent리스트가 됩니다.
for i in range(N + 1):
    parent[i] = find(i)

print(len(set(parent[1:])))
