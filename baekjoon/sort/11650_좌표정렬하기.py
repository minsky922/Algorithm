import sys

n=int(sys.stdin.readline())
arr=[]
for i in range(n):
    [a,b] = map(int, sys.stdin.readline().split())
    arr.append([a,b])
arr.sort(key=lambda x: (x[1],x[0]))
for i in arr:
    print(i[0], i[1])