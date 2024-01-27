import sys

input = sys.stdin.readline
n, k = map(int, input().split())
cnt = 0
coins = []

for i in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)

for coin in coins:
    cnt += k // coin
    k %= coin

print(cnt)
