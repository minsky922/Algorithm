import sys

input = sys.stdin.readline


def d(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        return (d(a, b // 2, c) ** 2) % c
    else:
        return ((d(a, b // 2, c) ** 2) * a) % c


a, b, c = map(int, input().split())
print(d(a, b, c))
