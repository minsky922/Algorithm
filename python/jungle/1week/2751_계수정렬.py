import sys

input = sys.stdin.readline
n = int(input())
count = [0] * 10001  # 1부터 10,000까지의 자연수

# 입력 받으면서 카운팅
for _ in range(n):
    count[int(input())] += 1

# 정렬된 결과 출력
for i in range(1, 10001):  # 0은 제외하고 1부터 시작
    for j in range(count[i]):
        print(i)
