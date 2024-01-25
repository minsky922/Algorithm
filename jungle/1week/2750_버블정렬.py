n = int(input())
a = []


def bubble_sort(a):
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]


for i in range(n):
    a.append(int(input()))

bubble_sort(a)
for i in range(n):
    print(a[i])
