n=int(input())

schedule = [list(map(int, input().split())) for i in range(n)]
dp = [0 for _ in range(n+1)]

for i in range(n-1, -1, -1):
    # i일에 상담하는게 퇴사일 넘기면 상담 x
    if i + schedule[i][0] > n:
        dp[i] = dp[i+1]
    else:
    # i일에 상담 하는것과 안하는것 중 큰 값 선택
        dp[i] = max(dp[i+1], schedule[i][1] + dp[i + schedule[i][0]])
    

print(dp[0])