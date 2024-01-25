import sys

input = sys.stdin.readline
V, E = map(int, input().split())  # 정점(Vertex)의 수 , 간선(Edge)의 수
edges = []  # 그래프의 각 간선과 그 가중치를 저장할 리스트
for i in range(E):  # 정점(A,B), 가중치(C)
    A, B, C = map(int, input().split())
    edges.append((A, B, C))
edges.sort(key=lambda x: x[2])  # C(cost)가 적은 것부터 정렬

# Union-Find
parent = [i for i in range(V + 1)]  # 각 정점의 초기 부모를 자기 자신으로 설정


# 정점 x의 최상위 부모(루트 정점)를 찾는 함수
def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x])  # get_parent 거슬러 올라가면서 parent[x]값도 갱신
    return parent[x]


# 두 정점 a, b의 부모를 합치는 함수
def union_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)

    if a < b:  # 작은 쪽이 부모가 된다. (한 집합 관계라서 부모가 따로 있는건 아님)
        parent[b] = a
    else:
        parent[a] = b


# 두 정점 a, b가 같은 부모(같은 트리)를 가지고 있는지 확인하는 함수
def same_parent(a, b):
    return get_parent(a) == get_parent(b)


answer = 0
for a, b, cost in edges:
    # cost가 작은 edge부터 하나씩 추가해가면서 같은 부모를 공유하지 않을때(사이클 없을때)만 확정
    if not same_parent(a, b):
        union_parent(a, b)
        answer += cost
print(answer)
