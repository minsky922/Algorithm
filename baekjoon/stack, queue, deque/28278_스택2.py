# if stack : if 문의 조건은 지정된 변수나 
# 데이터 구조가 비어 있지 않으면
# True로 간주되고 비어 있으면 False로 간주
import sys
stack = []
input = sys.stdin.readline()
n = int(input())
for i in range(n):
    command = input.split()
    if command[0] == '1':
        stack.append(command[1])
    elif command[0] == '2':
        if stack: 
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == '3':
        print(len(stack))
    elif command[0] == '4':
        if stack:
            print(0)
        else:
            print(1)
    elif command[0]=='5':
        if stack:
            print(stack[-1])
        else:
            print(-1)


