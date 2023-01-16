import sys
input = sys.stdin.readline
import heapq
INF = int(1e18)

def dijkstra(start):
    q = []

    heapq.heappush(q, (0,start,0))
    distance[start][0] = 0
    while q:

        dist, now ,paved = heapq.heappop(q)
        if distance[now][paved] < dist: continue

        for i in graph[now]:

            cost = dist + i[1]
            if cost < distance[i[0]][paved]:
                distance[i[0]][paved] = cost
                heapq.heappush(q,(cost, i[0], paved))

            if paved < k and dist < distance[i[0]][paved + 1]:
                distance[i[0]][paved + 1] = dist
                heapq.heappush(q, (dist, i[0], paved + 1))

n, m, k = map(int,input().split())
graph = [[] for i in range(n + 1)]

for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

distance = [[INF]*(k+1) for _ in range(n + 1)]
dijkstra(1)

result = INF
for i in range(k + 1):
    result = min(result, distance[n][i])
print(result)