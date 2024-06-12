import sys

input = sys.stdin.readline
n = int(input())
a = []


def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])

    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1
    if i == len(left):
        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1
    return a


for i in range(n):
    a.append(int(input()))

merge_sort(a)
for i in range(n):
    print(a[i])
