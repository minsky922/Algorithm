import heapq
import sys

input = sys.stdin.readline

n = int(input())
cards = []
for i in range(n):
    heapq.heappush(cards, int(input()))

sum = 0
total = 0
while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)

    sum = a + b
    total += sum
    heapq.heappush(cards, sum)
print(total)
