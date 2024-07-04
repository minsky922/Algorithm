n = int(input())

d = [0] * 91


def f(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = f(x - 1) + f(x - 2)
    return d[x]


print(f(n))
