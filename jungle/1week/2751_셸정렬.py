import sys

input = sys.stdin.readline
n = int(input())
a = []


def shell_sort(a):
    n = len(a)
    h = 1
    while h < n // 9:
        h = h * 3 + 1
    while h > 0:
        for i in range(h, n):
            j = i - h
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j + h] = a[j]
                j -= h
            a[j + h] = tmp
        h //= 3


for i in range(n):
    a.append(int(input()))

shell_sort(a)
for i in range(n):
    print(a[i])
