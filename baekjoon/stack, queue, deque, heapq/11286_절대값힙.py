import heapq, sys
input = sys.stdin.readline

n=int(input())
heap=[]
for i in range(n):
    x=int(input())
    if x:
        heapq.heappush(heap,(abs(x), x))
    else:
        if heap:
            print(heapq.heappop(heap)[1]) #x를 반환
        else:
            print(0)