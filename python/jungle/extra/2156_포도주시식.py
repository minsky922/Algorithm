import sys

input = sys.stdin.readline
n = int(input())

p = [0] * 10001
for i in range(1, n + 1):
    p[i] = int(input())

d = [0] * 10001

d[1] = p[1]
d[2] = p[1] + p[2]
d[3] = max(p[1] + p[3], p[2] + p[3], d[2])

for i in range(4, n + 1):
    # 계단문제와 다르게 d[i-1] 케이스도 고려- 마지막잔을 마시지 않을 수도 있기 때문
    d[i] = max(p[i] + p[i - 1] + d[i - 3], p[i] + d[i - 2], d[i - 1])

print(max(d))
