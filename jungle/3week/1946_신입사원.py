import sys

t = int(input())
input = sys.stdin.readline

for _ in range(t):
    n = int(input())
    case = [list(map(int, input().split())) for _ in range(n)]
    case.sort(key=lambda x: x[0])

    cnt = 1
    maxi = case[0][1]
    for i in range(1, n):
        if maxi > case[i][1]:
            cnt += 1
            maxi = case[i][1]
    print(cnt)
