n=input()
arr=list(map(int,n))

arr.sort(reverse=True)

for i in arr:
    print(i,end='')
