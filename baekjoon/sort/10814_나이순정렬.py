import sys
n=int(input())
arr=[]
for i in range(n):
    a,b = sys.stdin.readline().split()
    a=int(a)
    arr.append((a,b))
arr.sort(key=lambda x:x[0]) #두번째 값은 입력받은 순서대로
for i in arr:
    print(i[0], i[1])