import sys

input = sys.stdin.readline
n = int(input())
towers = list(map(int, input().split()))
stack = []  # 최댓값 저장
ans = []  # 수신 탑 인덱스

for i in range(n):
    while stack:
        if stack[-1][1] > towers[i]:  # 수신가능한 상황
            ans.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:  # 스택 비면 레이저 수신할 탑 없음
        ans.append(0)
    stack.append([i, towers[i]])  # 인덱스, 값
print(*ans)  # 공백으로 구분하여 출력
