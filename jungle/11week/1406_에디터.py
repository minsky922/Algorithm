import sys

input = sys.stdin.readline

# arr = list(input().rstrip())
# cursor = len(arr)

stk1 = list(input().rstrip())
stk2 = []
m = int(input())

# for i in range(m):
#     cmd = list(input().split())
#     if cmd[0] == "L":
#         if cursor == 0:
#             continue
#         else:
#             cursor -= 1
#     elif cmd[0] == "D":
#         if cursor == len(arr):
#             continue
#         else:
#             cursor += 1
#     elif cmd[0] == "B":
#         if cursor == 0:
#             continue
#         else:
#             arr.pop(cursor)
#     else:
#         arr.insert(cursor, cmd[1])
#         cursor += 1

# print("".join(arr))

for i in range(m):
    cmd = list(input().split())
    if cmd[0] == "L":
        if stk1:
            stk2.append(stk1.pop())
    elif cmd[0] == "D":
        if stk2:
            stk1.append(stk2.pop())
    elif cmd[0] == "B":
        if stk1:
            stk1.pop()
    else:
        stk1.append(cmd[1])

stk1.extend(reversed(stk2))
print("".join(stk1))
