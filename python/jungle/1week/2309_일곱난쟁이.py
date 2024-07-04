a = []
for i in range(9):
    a.append(int(input()))
x = sorted(a)

for i in range(9):
    for j in range(i + 1, 9):
        if sum(x) - (x[i] + x[j]) == 100:
            temp1 = x[i]
            temp2 = x[j]

x.remove(temp1)
x.remove(temp2)
for i in range(7):
    print(x[i])
