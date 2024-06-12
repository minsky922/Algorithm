import sys
n,c=list(map(int,input().split()))
arr = [int(sys.stdin.readline()) for _ in range(n)]
arr.sort()
start=1
end = arr[-1] - arr[0]
result=0

while start <= end:
    mid = (start+end)//2 #가장 인접한 두공유기 사이의 최대거리
    current = arr[0]
    cnt=1
    for i in range(1,n):
        if arr[i] - current >= mid:
            cnt += 1
            current = arr[i] # i번째 인덱스에 공유기 설치
    if cnt >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)