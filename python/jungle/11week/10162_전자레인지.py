import sys

input = sys.stdin.readline

n = int(input())

a = n // 300
b = (n % 300) // 60
c = ((n % 300) % 60) // 10

if (((n % 300) % 60)) % 10 > 0:
    print(-1)
else:
    print(a, b, c)
