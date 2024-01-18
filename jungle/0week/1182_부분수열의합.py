import sys
from itertools import combinations

n, s = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0

for i in range(1, n + 1):
    temp = combinations(a, i)
    for j in temp:
        if sum(j) == s:
            cnt += 1
print(cnt)
