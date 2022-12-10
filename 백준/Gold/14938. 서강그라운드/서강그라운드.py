import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m,r = map(int,input().split())
items = list(map(int,input().split()))

graph = [[] for i in range(n + 1)]

for _ in range(r):
    a,b,c = map(int,input().split())

    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

total_result = []
for i in range(1,n+1):
    distance = [INF] * (n + 1)
    dijkstra(i)

    idx_list = []
    for idx, each in enumerate(distance):
        if each <= m:
            idx_list.append(idx)

    tmp = []
    for each in idx_list:
        tmp.append(items[each - 1])

    total_result.append(sum(tmp))

print(max(total_result))