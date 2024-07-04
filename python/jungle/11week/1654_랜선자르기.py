k, n = map(int, input().split())

arr = [int(input()) for i in range(k)]
start = 1
end = max(arr)

while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in arr:
        total += i // mid
    if total >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)
