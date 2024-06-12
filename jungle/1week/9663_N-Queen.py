n = int(input())

ans = 0
row = [0] * n


# 유망한지 판단하는 함수
def is_promising(x):
    for i in range(x):
        # 같은 열이여도 안되고 대각선에 있어도 안된다.
        # (2,1)의 행 2- (1,0)의 행 1 = | (2,1)의 열 1 - (1,0)의 열0 |
        # 행번호차이=열번호차이면 같은 대각선 상에 있는것
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False

    return True


def n_queens(x):
    # x가 마지막 행까지 수행하고 여기까지 오면,찾기완료
    global ans
    if x == n:
        ans += 1
        return

    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i  # x번쩨 헹, i번째 열에 퀸을 놓아본다.
            if is_promising(x):  # 그자리에 두어도 괜찮았다면
                n_queens(x + 1)  # 그 다음행에 대해 퀸을 놓는것을 해본다.


n_queens(0)  # 0부터시작
print(ans)
