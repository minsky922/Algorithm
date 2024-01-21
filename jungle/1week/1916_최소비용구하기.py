import heapq
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for i in range(n + 1)]

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])

start, end = map(int, input().split())


def dijkstra(graph, start):
    distances = [int(1e9)] * (n + 1)
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        dist, node = heapq.heappop(queue)

        if distances[node] < dist:
            continue

        for next_node, next_dist in graph[node]:
            distance = dist + next_dist
            if distance < distances[next_node]:
                distances[next_node] = distance
                heapq.heappush(queue, [distance, next_node])
    return distances


dist_start = dijkstra(graph, start)
print(dist_start[end])
