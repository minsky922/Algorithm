import sys

N = int(sys.stdin.readline())
matrix = [[]]

for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

DP = [[float("inf") for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(N + 1):
    DP[i][i] = 0

for a in range(N - 1, 0, -1):  ## 대각선에서 값이 들어갈 칸의 개수
    dif = N - a  # 각 칸의 i, j의 차이
    for b in range(1, a + 1):  # i의 값
        for k in range(b, b + dif):  # DP[b][] + DP[][b+dif] 이므로 b부터 b+dif-1까지 보고 싶음
            DP[b][b + dif] = min(
                DP[b][b + dif],
                DP[b][k]
                + DP[k + 1][b + dif]
                + matrix[b][0] * matrix[k][1] * matrix[b + dif][1],
            )

print(DP[1][N])
