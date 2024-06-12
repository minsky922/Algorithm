import sys

input = sys.stdin.readline
n=int(input())
for i in range(n):
    line = input()
    stack=[]
    for i in line:
        if i == "(":
            stack.append("(")
        elif i == ')':
            if len(stack) == 0:
                stack.append(')')
                break
            else:
                stack.pop()
    if stack:
        print("NO")
    else:
        print("YES")