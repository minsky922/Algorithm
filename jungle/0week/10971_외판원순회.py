import sys
from itertools import permutations

input = sys.stdin.readline
INF = 10 * 9
n = int(input())  # 도시수
travel_cost = [list(map(int, input().split())) for _ in range(n)]  # 도시간 이동 비용

all = permutations(
    list(range(n))
)  # 순열 생성 - 가능한 도시 방문 순서 (0,1,2,3)(0,1,3,2)(0,2,1,3)...
print(all)
min_cost = float("inf")
for via in all:
    cost = 0  # 총 이동 비용
    valid = True  # 유효한지
    for i in range(n - 1):
        tmp = travel_cost[via[i]][via[i + 1]]
        if tmp == 0:
            valid = False
            break
        else:
            cost += tmp
    tmp = travel_cost[via[n - 1]][via[0]]
    if tmp == 0:
        valid = False
    else:
        cost += tmp
    if valid:
        min_cost = min(min_cost, cost)

print(min_cost)
