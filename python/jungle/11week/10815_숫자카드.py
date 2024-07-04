import sys


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


input = sys.stdin.readline

result = []
n = int(input())
own = list(map(int, input().split()))
own.sort()
m = int(input())
cards = list(map(int, input().split()))

for i in cards:
    curr = binary_search(own, i, 0, n - 1)
    if curr == None:
        result.append(0)
    else:
        result.append(1)

print(*result)
