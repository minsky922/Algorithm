n=int(input())
def hanoi(n,start,end,sub):
    if n ==1:
        print(start,end)
    else:
        hanoi(n-1,start, sub, end)# 1단계 : 1에서 2로 n-1개 다옮김
        print(start,end)# 2단계 : 1에서 3으로 옮김
        hanoi(n-1,sub,end,start)# 3단계 : 2에서 3으로 n-1개 다옮김
sum = 2 ** n-1
print(sum)

hanoi(n,1,3,2)