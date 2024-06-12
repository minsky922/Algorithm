import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

A = list(input())
A.pop()
B = list(input())
B.pop()

DP = [[0 for j in range(len(B) + 1)] for i in range(len(A) + 1)]
Path = []  # LCS 저장 리스트

for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if A[i - 1] == B[j - 1]:  # A[i]와 #B[i]가 같으면
            DP[i][j] = DP[i - 1][j - 1] + 1  # DP[i][j]의 값을 왼쪽 대각선 값+1 로 저장
        else:  # 다른 경우에는 왼쪽값과 위의 값중 큰값으로 DP[i][j]저장
            DP[i][j] = max(DP[i - 1][j], DP[i][j - 1])

print(DP[len(A)][len(B)])


# LCS 출력을 해줘야함
def getText(r, c):
    if r == 0 or c == 0:
        return
    if A[r - 1] == B[c - 1]:
        Path.append(A[r - 1])
        getText(r - 1, c - 1)
    else:
        if DP[r - 1][c] > DP[r][c - 1]:
            getText(r - 1, c)
        else:
            getText(r, c - 1)


getText(len(A), len(B))

for i in range(len(Path) - 1, -1, -1):
    print(Path.pop(i), end="")
print()
