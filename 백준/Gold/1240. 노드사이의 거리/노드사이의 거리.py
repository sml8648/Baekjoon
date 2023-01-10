# 트리 문제이다 보니 경로가 하나 밖에 없다.

import sys
input = sys.stdin.readline

def dfs(x):
    for data in graph[x]:
        y = data[0]
        cost = data[1]
        if not visited[y]:
            visited[y] = True
            distance[y] = distance[x] + cost
            dfs(y)

n, m = map(int,input().split())

graph = [[] for _ in range(n+1)]
for i in range(n - 1):
    a, b, c  = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

for i in range(m):
    x, y = map(int,input().split())
    visited = [False]*(n+1)
    distance = [-1]*(n+1)
    visited[x] = True
    distance[x] = 0
    dfs(x)
    print(distance[y])