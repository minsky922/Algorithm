N, K = map(int, input().split())  # N과 K를 입력받음

weight = [0] * (N + 1)
value = [0] * (N + 1)
d = [[0] * (K + 1) for _ in range(N + 1)]

# 무게와 가치 정보를 입력받음
for i in range(1, N + 1):
    weight[i], value[i] = map(int, input().split())

# 동적 프로그래밍을 이용하여 문제 해결
for i in range(1, N + 1):
    for j in range(1, K + 1):
        if j >= weight[i]:
            d[i][j] = max(d[i - 1][j], d[i - 1][j - weight[i]] + value[i])
        else:
            d[i][j] = d[i - 1][j]

print(d[N][K])
