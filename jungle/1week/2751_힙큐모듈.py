import heapq
import sys

input = sys.stdin.readline
n = int(input())
a = []


def heap_sort(a):
    heap = []
    for i in a:
        heapq.heappush(heap, i)
    for i in range(len(a)):
        a[i] = heapq.heappop(heap)


for i in range(n):
    a.append(int(input()))

heap_sort(a)
for i in range(n):
    print(a[i])
