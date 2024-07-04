import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input().rstrip())

perm_list = permutations(range(1, n + 1), n)

for i in perm_list:
    print(" ".join(map(str, i)))
