from collections import deque

n=int(input())

graph = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
cnt = 0
x,y,size = 0,0,2
# 위치

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x=i
            y=j



def bfs(x,y,shark_size):
    visited=[[0]*n for _ in range(n)]
    distance=[[0]*n for _ in range(n)]
    
    q=deque()
    q.append((x,y))
    visited[x][y] = 1
    temp=[]

    while q:
        cur_x,cur_y=q.popleft()
        for i in range(4):
            nx = cur_x+dx[i]
            ny = cur_y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0:
                if graph[nx][ny] <= shark_size:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[cur_x][cur_y] + 1
                    if graph[nx][ny] < shark_size and graph[nx][ny] != 0:
                        temp.append((nx,ny,distance[nx][ny]))
    # 거리 ,x좌표 , y좌표 순 우선순위
    return sorted(temp, key=lambda x: (-x[2],-x[0],-x[1]))

result=0
while True:
    shark = bfs(x,y,size)
    if len(shark) == 0:
        break
    nx,ny,dist = shark.pop()
    result += dist # 움직이는 칸수가 곧 시간
    graph[x][y],graph[nx][ny] = 0,0
    # 상어 좌표를 먹은 물고기의 좌표로 이동
    x,y = nx,ny
    cnt+=1
    if cnt == size:
        size += 1
        cnt = 0
print(result)