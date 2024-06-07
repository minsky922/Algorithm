import sys
input = sys.stdin.readline
n,m=map(int,input().split())
r,c,d=map(int,input().split())
room =[list(map(int,input().split())) for i in range(n)]
visited = [[0]*m for i in range(n)]

visited[r][c] = 1
cnt = 1

# 북0, 동1, 남2, 서3
dr = [-1,0,1,0]
dc = [0,1,0,-1]

while True:
    flag = 0
    for i in range(4):
        d = (d+3) % 4 #반시계 회전
        nr = r + dr[d]
        nc = c + dc[d]
        # 범위안, 청소가능하면
        if 0<=nr<n and 0<=nc<m and room[nr][nc] == 0:
            if visited[nr][nc] == 0:
                visited[nr][nc] = 1
                cnt += 1
                r = nr
                c = nc
                flag = 1
                break
    if flag == 0:
        if room[r-dr[d]][c-dc[d]] == 1:
            print(cnt)
            break
        else:
            r,c = r-dr[d], c-dc[d]