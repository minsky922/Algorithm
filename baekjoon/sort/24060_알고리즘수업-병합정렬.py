
#merge sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = (len(arr) + 1) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    sorted_arr = []
    l = h = 0
    while l < len(left) and h < len(right):
        if left[l] <= right[h]:
            sorted_arr.append(left[l])
            ans.append(left[l])
            l += 1
        else:
            sorted_arr.append(right[h])
            ans.append(right[h])
            h += 1

    while l < len(left):
        sorted_arr.append(left[l])
        ans.append(left[l])
        l += 1

    while h < len(right):
        sorted_arr.append(right[h])
        ans.append(right[h])
        h += 1

    return sorted_arr


ans = []
N, K = map(int, input().split())
merge_sort(list(map(int, input().split())))
print(ans)
print(ans[K - 1] if K <= len(ans) else -1)
