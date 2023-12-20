n=int(input())
arr = list(map(int,input().split()))
arr.sort()
cnt=0
total=0
for i in range(len(arr)):
    cnt+=arr[i]
    total+=cnt
print(total)