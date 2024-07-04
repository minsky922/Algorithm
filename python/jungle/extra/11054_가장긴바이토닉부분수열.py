n = int(input())
arr = list(map(int, input().split()))

inc_d = [1] * n
dec_d = [1] * n
result = [0] * n
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            inc_d[i] = max(inc_d[i], inc_d[j] + 1)

arr.reverse()

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dec_d[i] = max(dec_d[i], dec_d[j] + 1)
dec_d.reverse()

for i in range(n):
    result[i] += inc_d[i] + dec_d[i]

print(max(result) - 1)
