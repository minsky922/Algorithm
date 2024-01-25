n = int(input())
d = int(input())
parent = [0] * (n + 1)

for i in range(n + 1):
    parent[i] = i


def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(d):
    a, b = map(int, input().split())
    union(a, b)

for i in range(n + 1):
    parent[i] = find(i)

answer = 0
for i in range(1, n + 1):
    if parent[i] == 1:
        answer += 1

print(answer - 1)
