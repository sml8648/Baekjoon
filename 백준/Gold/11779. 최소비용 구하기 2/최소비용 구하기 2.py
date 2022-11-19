import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[] for i in range(n + 1)]

distance = [[INF,[]] for _ in range(n+1)]


for _ in range(m):
    a,b,c = map(int,input().split())

    graph[a].append((b,c))

start, end = map(int,input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))

    distance[start][0] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now][0] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]][0]:
                distance[i[0]][0] = cost
                distance[i[0]][1] = now
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

# print(distance[end])

ans = []
tmp = end
while tmp != start:
    ans.append(str(tmp))
    tmp = distance[tmp][1]

ans.append(str(start))
ans.reverse()

print(distance[end][0])
print(len(ans))
print(" ".join(ans))