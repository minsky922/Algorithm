import sys
from itertools import combinations

while True:
    arr = list(map(int, input().split()))

    k = arr[0]
    s = arr[1:]

    for i in combinations(s, 6):
        print(*i)

    if k == 0:
        exit()
    print()
