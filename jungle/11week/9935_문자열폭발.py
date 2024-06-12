import sys

input = sys.stdin.readline
S = input().rstrip()
bomb = input().rstrip()

stk = []
bomb_len = len(bomb)

for i in range(len(S)):
    stk.append(S[i])
    # print(stk)
    if "".join(stk[-bomb_len:]) == bomb:
        for _ in range(bomb_len):
            stk.pop()
        # print(stk)

if stk:
    print("".join(stk))
else:
    print("FRULA")
