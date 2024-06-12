from collections import deque

n, k = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

s, x, y = map(int, input().split())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

q = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:  # 바이러스가 있는 위치
            q.append((graph[i][j], i, j, 0))  # 바이러스 정보, 행, 열, 흘러간 시간
q.sort()  # (주의) 리스트로 받아 정렬 후 queue로 변경!
q = deque(q)

while q:  # BFS
    virus, row, col, time = q.popleft()
    if time == s:  # 시간이 S만큼 지났다면 종료
        break
    for i in range(4):  # 상하좌우 이동
        r = row + dx[i]
        c = col + dy[i]
        if -1 < r < n and -1 < c < n and not graph[r][c]:  # 범위를 벗어나지 않고 위치 값이 0일 때
            graph[r][c] = virus  # 바이러스 배치
            q.append((virus, r, c, time + 1))  # 다음 번 위치를 큐에 저장

print(graph[x - 1][y - 1])
