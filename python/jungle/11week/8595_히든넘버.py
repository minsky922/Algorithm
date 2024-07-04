import re
import sys

input = sys.stdin.readline
n = int(input())
arr = input()

a = re.findall("\d+", arr)

print(sum(map(int, a)))
