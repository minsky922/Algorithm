n = 6
arr1 = [46, 33, 33, 22, 31, 50]
arr2 = [27, 56, 19, 14, 14, 10]

answer = []
arr1_bin = []
arr2_bin = []

for i in range(n):
    temp = bin(arr1[i] | arr2[i])[2:]
    # if len(temp) < n:
    #     temp = "0" * (n - len(temp)) + temp
    temp = temp.zfill(n)
    temp = temp.replace("1", "#")
    temp = temp.replace("0", " ")

    answer.append(temp)

print(answer)
