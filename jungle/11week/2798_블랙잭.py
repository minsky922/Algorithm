n, m = map(int, input().split())

cards = list(map(int, input().split()))
result = []

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):

            curr_res = cards[i] + cards[j] + cards[k]
            if curr_res <= m:
                result.append(curr_res)

print(max(result))
