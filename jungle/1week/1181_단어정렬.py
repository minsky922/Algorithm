import sys

input = sys.stdin.readline

n = int(input())
a = []
for i in range(n):
    a.append(input().rstrip())
set_a = set(a)
a = list(set_a)
a.sort()
a.sort(key=len)
for i in range(len(a)):
    print(a[i])
