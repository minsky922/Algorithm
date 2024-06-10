### deque.roate 활용하면 편함
from collections import deque
def right(idx, d): #오른쪽 톱니바퀴 확인
    # 마지막 톱니는 확인 x
    if idx > 3:
        return
    # 같은 극이 아니면 회전
    if gears[idx - 1][2] != gears[idx][6]:
        right(idx + 1, -d)
        gears[idx].rotate(d)

def left(idx, d):
    # 첫번재 톱니 확인 x
    if idx < 0:
        return
    # 같은 극이 아니면 회전
    if gears[idx][2] != gears[idx+1][6]:
        left(idx-1, -d)
        gears[idx].rotate(d)
# 톱니바퀴 4개 입력받기
gears = [deque(list(map(int, input()))) for _ in range(4)]
k = int(input()) # 회전 횟수

for _ in range(k):
    # 회전 정보(회전시킨 톱니바퀴의 번호, 회전방향) 입력
    idx, d = map(int,input().split())
    idx -= 1
    # 회전할 톱니 번호의 시계방향, 반시계방향이 회전 가능한지 확인하고 회전한다
    # # -d인 이유는 회전할 톱니번호가 회전하는 방향의 반대방향으로 회전해야 하기 때문
    left(idx -1 , -d)
    right(idx+1, -d)

    # 회전할 톱니 번호의 톱니도 회전
    gears[idx].rotate(d)

# 점수 계산하여 출력
score = 0
for i in range(4):
    if gears[i][0] == 1:
        score += 2 ** i

print(score)