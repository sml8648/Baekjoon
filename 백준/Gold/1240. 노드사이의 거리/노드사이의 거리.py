import sys
input = sys.stdin.readline

n, m = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b,c = map(int,input().split())

    graph[a].append((b,c))
    graph[b].append((a,c))

def bfs(vertex):

    visited[vertex] = 1

    for each, cost in graph[vertex]:
        if not visited[each]:
            distance[each] = distance[vertex] + cost
            bfs(each)

for _ in range(m):

    visited = [0] * (n+1)
    x, y = map(int, input().split())
    distance = [0] * (n+1)
    bfs(x)

    print(distance[y])