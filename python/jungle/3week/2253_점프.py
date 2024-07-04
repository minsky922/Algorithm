import sys

input = sys.stdin.readline

N, stone_n = map(int, input().split())

stone = []
for _ in range(stone_n):
    stone.append(int(input()))
# 최댓값으로 dp 테이블 초기화
dp = [[10001] * (int((2 * N) ** 0.5) + 2) for _ in range(N + 1)]

dp[1][0] = 0  # 시작돌에서 시작돌로 가는 초기값만 0으로 초기화
for i in range(2, N + 1):
    if i in stone:  # 작은돌 패스
        continue
    # 점프의 최댓값은 int(((2*N)**0.5)인데 range에서 해당 값까지 보기 위해서는 1을 더해줘야 함
    for j in range(1, int((2 * i) ** 0.5) + 1):
        dp[i][j] = min(dp[i - j][j - 1], dp[i - j][j], dp[i - j][j + 1]) + 1
        # dp[i][j] = i번째 돌에 도달하는데 j크기의 점프를 사용한 경우 최소 점프 횟수


ans = min(dp[N])
if ans == 10001:
    print(-1)
else:
    print(ans)
