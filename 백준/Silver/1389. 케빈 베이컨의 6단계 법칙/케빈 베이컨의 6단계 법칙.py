import sys

input = sys.stdin.readline
INF = int(1e4)

n,m = map(int,input().split())

graph = [[INF] * (n) for _ in range(n)]

for a in range(n):
    for b in range(n):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    s, e = map(int, input().split())
    graph[s-1][e-1] = 1
    graph[e-1][s-1] = 1

for k in range(n):
    for a in range(n):
        for b in range(n):
            if a == b:
                graph[a][b] = 0
            else:
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = []
for each in graph:
    result.append(sum(each))

Min = min(result)
for idx, each in enumerate(result):
    if each == Min:
        print(idx+1)
        break