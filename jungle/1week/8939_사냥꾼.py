import sys

input = sys.stdin.readline

m, n, l = map(int, input().split())
man = list(map(int, input().split()))
man.sort()
animal = [list(map(int, input().split())) for i in range(n)]

cnt = 0
for x, y in animal:
    start = 0
    end = len(man) - 1
    while start < end:
        mid = (start + end) // 2
        if man[mid] < x:
            start = mid + 1
        else:
            end = mid
    if start > 0 and abs(man[start - 1] - x) + y <= l:
        cnt += 1
    elif abs(man[start] - x) + y <= l:
        cnt += 1

print(cnt)
