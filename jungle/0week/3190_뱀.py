import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
k = int(input())

arr = [[0] * n for _ in range(n)]
for i in range(k):
    x, y = map(int, input().split())
    arr[x - 1][y - 1] = 1

# 방향전환 횟수
l = int(input())
time_dic = {}
for i in range(l):
    x, c = input().split()
    time_dic[int(x)] = c
# 우하좌상
dx = [0, 1, 0, -1]  # 행
dy = [1, 0, -1, 0]  # 열
# 뱀 위치, 방향 초기
x, y, d = 0, 0, 0
# 뱀
snake = deque()
time = 0
while True:
    # 뱀머리 현재 위치
    snake.append((x, y))
    time += 1

    x += dx[d]
    y += dy[d]
    # 벽에 부딪히거나 자기 몸과 부딪히면
    if x < 0 or x >= n or y < 0 or y >= n or arr[x][y] == 2:
        break
    # 벽이 아니면
    # 사과가 없다면
    if not arr[x][y]:
        # 꼬리 없애주고
        i, j = snake.popleft()
        arr[i][j] = 0
    arr[x][y] = 2

    if time in time_dic:
        # 만약 시계방향으로 돈다면
        if time_dic[time] == "D":
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4
print(time)
