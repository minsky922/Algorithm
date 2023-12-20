n,m = map(int, input().split())
arr=[]
cnt=0
for _ in range(n):
    arr.append(int(input()))
for i in reversed(range(n)):
    cnt+=m//arr[i]
    m=m%arr[i]
print(cnt)