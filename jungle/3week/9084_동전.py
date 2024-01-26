import sys

input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())

    d = [0] * (m + 1)

    d[0] = 1
    for coin in arr:
        for i in range(1, m + 1):
            if i >= coin:
                d[i] += d[i - coin]
    print(d[m])
