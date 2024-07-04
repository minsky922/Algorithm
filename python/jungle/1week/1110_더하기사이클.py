n = int(input())
temp = n
cycle = 0
while True:
    a = temp // 10
    b = temp % 10
    c = (a + b) % 10
    temp = b * 10 + c
    cycle += 1
    if temp == n:
        break
print(cycle)
