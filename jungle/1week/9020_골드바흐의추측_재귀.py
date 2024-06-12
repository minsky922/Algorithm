def checkPrime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True


def goldBach(n):
    half = n // 2
    for i in range(half, n):
        if checkPrime(i) and checkPrime(n - i):
            return [n - i, i]


t = int(input())
for i in range(t):
    answer = goldBach(int(input()))
    print(answer[0], answer[1])
