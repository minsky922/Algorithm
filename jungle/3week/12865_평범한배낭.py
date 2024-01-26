import sys

input = sys.stdin.readline
n, k = map(int, input().split())

d = [0] * (k + 1)
for i in range(n):
    w, v = map(int, input().split())
    for i in range(k, w - 1, -1):
        d[i] = max(d[i], d[i - w] + v)
print(d[-1])
