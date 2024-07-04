import sys

input = sys.stdin.readline
n = int(input())
a = []


def quick_sort(a, left, right):
    pl = left
    pr = right
    x = a[(left + right) // 2]

    while pl <= pr:
        while a[pl] < x:
            pl += 1
        while a[pr] > x:
            pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
    if left < pr:
        quick_sort(a, left, pr)
    if pl < right:
        quick_sort(a, pl, right)


for i in range(n):
    a.append(int(input()))

quick_sort(a, 0, len(a) - 1)
for i in range(n):
    print(a[i])
