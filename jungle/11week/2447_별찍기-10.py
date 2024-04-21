import sys

input = sys.stdin.readline

n = int(input())


def make_stars(n):
    if n == 1:
        return "*"

    stars = make_stars(n // 3)

    res = []
    for i in stars:
        res.append(i * 3)
    for i in stars:
        res.append(i + " " * (n // 3) + i)
    for i in stars:
        res.append(i * 3)
    return res


print("\n".join(make_stars(n)))
