import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
graph = []
for _ in range(n):

    a_list = list(map(int,input().split()))
    graph.append(a_list)

for i in range(n):
    for j in range(n):

        if graph[i][j] == 0:
            graph[i][j] = INF

for k in range(0,n):
    for a in range(0,n):
        for b in range(0,n):

            if graph[a][b] >= (graph[a][k] + graph[k][b]):
                graph[a][b] = 1

for a in range(0,n):
    for b in range(0,n):
        if graph[a][b] > 1:
            graph[a][b] = 0

for a in range(n):
    result = map(str,graph[a])
    print(' '.join(result))