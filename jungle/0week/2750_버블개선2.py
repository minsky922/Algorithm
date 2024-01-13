n = int(input())
a = []


def bubble_sort(a):
    n = len(a)
    k = 0
    while k < n - 1:
        last = n - 1
        for j in range(n - 1, k, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        k = last


for i in range(n):
    a.append(int(input()))

bubble_sort(a)
for i in range(n):
    print(a[i])
