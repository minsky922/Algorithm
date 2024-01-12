def checkPrime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True


for i in range(int(input())):
    num = int(input())
    a, b = num // 2, num // 2
    while a > 0:
        if checkPrime(a) and checkPrime(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1
