import sys
input = sys.stdin.readline
import heapq
from collections import deque
INF = int(1e9)

def dijkstra():
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:

        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
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
        for i in reversed_graph[now]:
            cost = distance[i[0]] + i[1]
            if cost == distance[now]:
                removes.add((i[0], now))

                if i[0] not in visited:
                    q.append(i[0])
                    visited.add(i[0])
    return removes

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    start, end = map(int,input().split())
    graph = [[] for i in range(n)]
    reversed_graph = [[] for i in range(n)]

    for _ in range(m):
        a, b, c = map(int,input().split())
        graph[a].append((b,c))
        reversed_graph[b].append((a, c))

    distance = [INF] * n
    dijkstra()

    removes = bfs()
    new_graph = [[] for i in range(n)]
    for a in range(n):
        for b, c in graph[a]:
            if (a, b) not in removes:
                new_graph[a].append((b,c))
    graph = new_graph

    distance = [INF]*n
    dijkstra()

    if distance[end] == INF:
        print(-1)
    else:
        print(distance[end])