import sys
n=int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
LIS = [a[0]]
def binary_search(e):
    start = 0
    end = len(LIS) - 1
    while start<=end:
        mid = (start+end)//2
        if LIS[mid] == e:
            return mid
        elif LIS[mid] < e:
            start = mid + 1
        else:
            end = mid -1
    return start
for i in a:
    if LIS[-1] < i:
        LIS.append(i)
    else:
        idx = binary_search(i)
        LIS[idx] = i
print(len(LIS))