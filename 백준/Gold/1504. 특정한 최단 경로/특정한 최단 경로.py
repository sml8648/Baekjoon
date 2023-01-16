import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)


n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1 ,v2 = map(int,input().split())

def dijkstra(start):

    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))

    while q:
        cost, V = heapq.heappop(q)

        if distance[V] < cost:
            continue

        #i[0] V
        #i[1] cost

        for i in graph[V]:
            new_cost = distance[V] + i[1]
            if new_cost < distance[i[0]]:
                distance[i[0]] = new_cost
                heapq.heappush(q,(i[1],i[0]))

dijkstra(1)
dist_V1 = distance[v1]
dist_V2 = distance[v2]

distance = [INF] * (n+1)
dijkstra(v1)
for_mid1 = distance[v2]
for_dest1 = distance[n]

distance = [INF] * (n+1)
dijkstra(v2)
for_mid2 = distance[v1]
for_dest2 = distance[n]


answer = min(dist_V1 + for_mid1 + for_dest2, dist_V2 + for_mid2 + for_dest1)

if answer >= INF:
    print(-1)
else:
    print(answer)