n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()

result = []
for i in arr:
    result.append(i * n)
    n -= 1
print(max(result))
