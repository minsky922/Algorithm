def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


n = int(input())
A = list(map(int, input().split()))
A.sort()
m = int(input())
M = list(map(int, input().split()))

for i in M:
    result = binary_search(A, i, 0, n - 1)
    if result == None:
        print(0)
    else:
        print(1)
