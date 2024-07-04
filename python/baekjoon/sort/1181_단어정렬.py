n=int(input())
arr=[]
for i in range(n):
    arr.append(input())
set_arr = set(arr) #중복값 제거
arr = list(set_arr)
arr.sort() #알파벳 순서로 정렬
arr.sort(key = len) #문자열 길이순 정렬

#7,8 순으로 작성해야 8번 우선으로 정렬된다

for i in arr:
    print(i)