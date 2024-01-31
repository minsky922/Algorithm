import sys

input = sys.stdin.readline
n = int(input())
d = [1] * 501
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x: x[0])

for i in range(n):
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            d[i] = max(d[i], d[j] + 1)

print(n - max(d))
