from collections import deque

q = deque()
n, k = map(int, input().split())
for i in range(1, n + 1):
    q.append(i)
answer = []
for i in range(n):
    for i in range(k - 1):
        q.append(q.popleft())
    answer.append(q.popleft())
print("<" + ", ".join(map(str, answer)) + ">")
