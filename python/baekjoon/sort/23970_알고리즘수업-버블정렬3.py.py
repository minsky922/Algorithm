import sys

input = sys.stdin.readline

n = int(input())

a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))


def bubble_sort(a, b):
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                if a[j + 1] == b[j + 1]:
                    if a == b:
                        print("1")
                        sys.exit(0)
    print("0")


if a == b:
    print("1")
    sys.exit(0)
else:
    bubble_sort(a, b)
