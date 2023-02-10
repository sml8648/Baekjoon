import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    row = list(map(int,input().split()))
    graph.append(row)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    queue = deque([(0,0)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if not visited[nx][ny]:
                if graph[nx][ny] >= 1:
                    graph[nx][ny] += 1
                else:
                    queue.append((nx, ny))
                    visited[nx][ny] = True

def melt():
    finish = True
    for i in range(n):
        for j in range(m):
            if graph[i][j] >= 3:
                graph[i][j] = 0
                finish = False
            elif graph[i][j] == 2:
                graph[i][j] = 1
    return finish

result = 0
while True:
    bfs()
    if melt():
        print(result)
        break
    else:
        result += 1