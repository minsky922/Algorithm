def cut(x, y, n):
    global result
    a = data[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if a != data[i][j]:
                result += "("
                cut(x, y, n // 2)
                cut(x, y + n // 2, n // 2)
                cut(x + n // 2, y, n // 2)
                cut(x + n // 2, y + n // 2, n // 2)
                result += ")"
                return

    result += str(a)


n = int(input())
data = [list(map(int, input())) for _ in range(n)]
result = ""
cut(0, 0, n)
print(result)
