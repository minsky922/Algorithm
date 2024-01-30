import sys

input = sys.stdin.readline
n = int(input())
s = [0] * 301
for i in range(1, n + 1):
    s[i] = int(input())

d = [0] * 301
d[1] = s[1]
d[2] = s[1] + s[2]
d[3] = max(s[1] + s[3], s[2] + s[3])

for i in range(4, n + 1):
    d[i] = max(s[i] + s[i - 1] + d[i - 3], s[i] + d[i - 2])

print(d[n])
