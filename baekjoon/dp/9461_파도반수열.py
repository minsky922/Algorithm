import sys
input = sys.stdin.readline
t = int(input())
p = [0] * 101
p[1] = 1
p[2] = 1
p[3] = 1
for i in range(4, 101):
    p[i] = p[i-3] + p[i-2]
for i in range(t):
    n = int(input())
    print(p[n])
    