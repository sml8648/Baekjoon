import sys
input = sys.stdin.readline
import heapq
from collections import deque
INF = int(1e9)

def dijkstra(a, b):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:

        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:

            if i[0] == a and now == b: continue
            elif i[0] == b and now == a: continue
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

def bfs():
    q = deque()
    visited = set()
    q.append(end)
    removes = set()
    while q:
        now = q.popleft()
        if now == start:
            continue
        for i in graph[now]:
            cost = distance[i[0]] + i[1]
            if cost == distance[now]:
                removes.add((i[0], now))
                if i[0] not in visited:
                    q.append(i[0])
                    visited.add(i[0])

    return removes

n, m = map(int, input().split())
start, end = 1, n
graph = [[] for i in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

distance = [INF] * (n + 1)
dijkstra(-1, -1)

removes = bfs()

result = 0
for a, b in removes:
    distance = [INF] * (n + 1)
    dijkstra(a, b)
    result = max(result, distance[end])

print(result)