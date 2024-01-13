n = int(input())
a = []


def insert_sort(a):
    n = len(a)
    for i in range(1, n):
        j = i
        tmp = a[i]
        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp


for i in range(n):
    a.append(int(input()))

insert_sort(a)
for i in range(n):
    print(a[i])
