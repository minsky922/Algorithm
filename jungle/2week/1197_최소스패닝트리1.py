# 1단계
# 엣지리스트에 엣지 정보를 저장한 후 부모 노드 데이터를 초기화한다.
# 최소 신장트리는 엣지 중심의 알고리즘이므로 데이터를 엣지 리스트를 활용해 저장해야 한다.
# 사이클 생성유무를 판단하기 위한 유니온 파인드용 부모 노드도 초기화 한다.

# 2단계
# 쿠르스칼 알고리즘을 수행한다. 현재 미사용 엣지 중 가중치가 가장 작은 엣지를 선택하고,
# 이 엣지를 연결했을 때 사이클의 발생 유무를 판단한다.
# 사이클이 발생하면 생략하고, 발생하지 않으면 엣지값을 더한다.

# 3단계
# 2단계에서 엣지를 더한 횟수가 V(노드 개수)-1이 될때까지 반복하고, 반복이 끝나면 엣지의 가중치를 모두 더한 값을 출력


import sys
from queue import PriorityQueue

input = sys.stdin.readline

N, M = map(int, input().split())  # 노드수, 엣지수 input 받기
pq = PriorityQueue()  # 엣지 정보를 저장할 우선순위 큐 만들기
parent = [0] * (N + 1)  # 부모노드 저장 리스트

for i in range(N + 1):
    parent[i] = i

for i in range(M):  # pq에 엣지정보 저장
    start, end, weight = map(int, input().split())
    pq.put((weight, start, end))  # 가중치 기준이기 때문에 가중치를 제일 앞 순서로 넣어준다.


# 유니온 파인드 구현하기


def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a


useEdge = 0  # 사용한 엣지 갯수
result = 0  # MST 완성했을때 가중치

while useEdge < N - 1:  # 사용한 엣지수가 노드수 -1이 될 때 까지
    weight, start, end = pq.get()  # 큐에서 엣지 정보 가져오기
    if find(start) != find(end):
        union(start, end)
        result += weight
        useEdge += 1

print(result)
