n, k = map(int, input().split())
bag = [[0] * (k + 1) for _ in range(n + 1)]
item = [[0, 0]]
for i in range(1, n + 1):
    item.append(list(map(int, input().split())))
for i in range(1, n + 1):
    for j in range(1, k + 1):
        w = item[i][0]
        v = item[i][1]
        if j < w:
            bag[i][j] = bag[i - 1][j]
        else:
            # bag[i][j] = max(bag[이전 물건][현재 가방 무게], 현재 물건 가치 + bag[이전 물건][현재 가방 무게 - 현재 물건 무게])
            bag[i][j] = max(bag[i - 1][j], bag[i - 1][j - w] + v)
print(bag[n][k])
