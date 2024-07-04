n = int(input())

time = []
for i in range(n):
    s, e = map(int, input().split())
    time.append([s, e])

# 먼저 끝나는 시간을 기준으로 정렬하고, 끝나는 시간이 같을 경우 시작 시간을 기준으로 정렬
time.sort(key=lambda x: (x[1], x[0]))

cnt = 0
end = 0
for s, e in time:
    if s >= end:
        end = e
        cnt += 1

print(cnt)  # 최대 회의 개수 출력
